# transaction_rollback.py
# Exercise 3: Transaction with ROLLBACK

import psycopg2
import pandas as pd
import matplotlib.pyplot as plt

print("="*70)
print("EXERCISE 3: TRANSACTION WITH ROLLBACK")
print("="*70)

# Connect with autocommit disabled
conn = psycopg2.connect(
    host='localhost', port=5435,
    user='datauser', password='rootpass123',
    database='postgres',
    options='-c search_path=sales_db'
)
conn.autocommit = False
cursor = conn.cursor()

# Transaction parameters
product_name = 'Office Chair Pro'
quantity_requested = 100  # Intentionally too much

print(f"\nAttempting Order: {quantity_requested}x {product_name}")
print("="*70)

# Capture initial state
print("\n0. Capturing Initial Database State...")
cursor.execute("""
    SELECT product_id, name, stock FROM productos
    WHERE name = %s
""", (product_name,))
initial_state = cursor.fetchone()
initial_product_id = initial_state[0]
initial_stock = initial_state[2]

cursor.execute("SELECT COUNT(*) FROM ordenes")
initial_order_count = cursor.fetchone()[0]

print(f"   Initial Stock: {initial_stock}")
print(f"   Initial Order Count: {initial_order_count}")

try:
    # Step 1: BEGIN TRANSACTION
    print("\n1. Starting Transaction...")
    print("   ✓ Transaction initiated")
    
    # Step 2: Lock and get product
    print("\n2. Retrieving Product Information...")
    cursor.execute("""
        SELECT product_id, name, price, stock
        FROM productos
        WHERE name = %s
        FOR UPDATE
    """, (product_name,))
    
    product = cursor.fetchone()
    if not product:
        raise Exception(f"Product '{product_name}' not found")
    
    product_id, name, price, current_stock = product
    print(f"   Product ID: {product_id}")
    print(f"   Current Stock: {current_stock}")
    print(f"   Requested: {quantity_requested}")
    print(f"   ✓ Row locked")
    
    # Step 3: Validate stock - THIS WILL FAIL
    print("\n3. Validating Stock Availability...")
    print(f"   Checking: {current_stock} >= {quantity_requested}?")
    
    if current_stock < quantity_requested:
        shortage = quantity_requested - current_stock
        raise Exception(
            f"INSUFFICIENT STOCK!\n"
            f"   Available: {current_stock} units\n"
            f"   Requested: {quantity_requested} units\n"
            f"   Shortage: {shortage} units"
        )
    
    # Following code won't execute
    cursor.execute("""
        UPDATE productos
        SET stock = stock - %s
        WHERE product_id = %s
    """, (quantity_requested, product_id))
    
    cursor.execute("""
        INSERT INTO ordenes (product_id, quantity, status)
        VALUES (%s, %s, 'pending')
    """, (product_id, quantity_requested)) 
    
    conn.commit()

except Exception as e:
    # ROLLBACK HANDLER
    print(f"\n✗ ERROR DETECTED:")
    print(f"   {str(e)}")
    
    print("\n4. Executing ROLLBACK...")
    print("   Rolling back all changes...")
    conn.rollback()
    print("   ✓ TRANSACTION ROLLED BACK")
    print("   ✓ Database restored to pre-transaction state")
    
    # Step 5: Verify NO changes persisted
    print("\n5. Verifying Database State After Rollback...")
    
    cursor.execute("""
        SELECT product_id, name, stock FROM productos
        WHERE name = %s
    """, (product_name,))
    final_state = cursor.fetchone()
    final_stock = final_state[2]
    
    cursor.execute("SELECT COUNT(*) FROM ordenes")
    final_order_count = cursor.fetchone()[0]
    
    print(f"   Stock for '{product_name}':")
    print(f"      Before Transaction: {initial_stock}")
    print(f"      After Rollback: {final_stock}")
    print(f"      Change: {final_stock - initial_stock}")
    print()
    print(f"   Order Count:")
    print(f"      Before Transaction: {initial_order_count}")
    print(f"      After Rollback: {final_order_count}")
    print(f"      Change: {final_order_count - initial_order_count}")
    
    if final_stock == initial_stock and final_order_count == initial_order_count:
        print("\n   ✓ VERIFIED: No changes persisted!")
        print("   ✓ ROLLBACK successful - data integrity maintained")
    else:
        print("\n   ✗ WARNING: State changed (should not happen)")
    
    # Step 6: ACID Properties Demonstration
    print("\n6. ACID Properties Demonstrated:")
    print("="*70)
    print("   [A] ATOMICITY:")
    print("       Transaction failed at validation")
    print("       NO partial changes - neither UPDATE nor INSERT executed")
    print("       All-or-nothing principle enforced")
    print()
    print("   [C] CONSISTENCY:")
    print(f"       Stock remains {final_stock} (unchanged)")
    print("       No invalid state created (prevented negative stock)")
    print("       Business rule enforced: cannot sell more than available")
    print()
    print("   [I] ISOLATION:")
    print("       FOR UPDATE locked the row during transaction attempt")
    print("       Other transactions could not see/modify this product")
    print("       Lock released after ROLLBACK")
    print()
    print("   [D] DURABILITY:")
    print("       ROLLBACK ensures failed transaction leaves NO trace")
    print("       Database state identical to before attempt")
    print("       No corruption or partial data")
    
    # Step 7: Error scenarios
    print("\n7. Common Scenarios Requiring ROLLBACK:")
    print("="*70)
    print("   • Insufficient stock (business rule violation)")
    print("   • Foreign key constraint violation")
    print("   • Check constraint violation (negative values)")
    print("   • Unique constraint violation (duplicate keys)")
    print("   • Data type mismatch")
    print("   • Connection loss during transaction")
    print("   • Deadlock with another transaction")
    print("   • Timeout or resource exhaustion")
    
    # Step 8: Visualization
    print("\n8. Creating Error Handling Visualization...")
    
    # Get stock levels
    cursor.execute("""
        SELECT name, stock, supplier
        FROM productos
        ORDER BY stock ASC
        LIMIT 10
    """)
    products = cursor.fetchall()
    df_products = pd.DataFrame(products,
        columns=['Product', 'Stock', 'Supplier'])
    
    fig, (ax1, ax2) = plt.subplots(1, 2, figsize=(16, 6))
    
    # Chart 1: Stock levels
    colors = ['#00008B' if p == product_name else '#DDA0DD'
              for p in df_products['Product']]
    
    bars = ax1.barh(range(len(df_products)), df_products['Stock'],
                    color=colors, edgecolor='#1A202C', linewidth=1.5)
    
    ax1.set_yticks(range(len(df_products)))
    ax1.set_yticklabels([p[:25] for p in df_products['Product']])
    ax1.set_xlabel('Stock Quantity', fontsize=11)
    ax1.set_title('Current Stock Levels\n(Red = Insufficient)',
                  fontsize=12, fontweight='bold')
    ax1.invert_yaxis()
    ax1.grid(axis='x', alpha=0.3)
    
    # Add requested quantity line
    for i, (name_p, stock) in enumerate(zip(df_products['Product'],
                                             df_products['Stock'])):
        if name_p == product_name:
            ax1.axvline(x=quantity_requested, color='red',
                       linestyle='--', linewidth=2)
            ax1.text(quantity_requested + 2, i,
                    f'Requested: {quantity_requested}',
                    va='center', color='red',
                    fontweight='bold', fontsize=9)
        ax1.text(stock + 1, i, str(int(stock)),
                va='center', fontsize=9, fontweight='bold')
    
    # Chart 2: Transaction outcomes
    outcomes = ['Successful\nTransactions', 'Failed Transaction\n(Rolled Back)']
    values = [5, 1]
    colors_outcome = ['#6B46C1', '#DC143C']
    
    bars = ax2.bar(outcomes, values, color=colors_outcome,
                   edgecolor='#1A202C', linewidth=2)
    
    for bar in bars:
        height = bar.get_height()
        ax2.text(bar.get_x() + bar.get_width()/2., height,
                f'{int(height)}', ha='center', va='bottom',
                fontsize=12, fontweight='bold')
    
    ax2.set_ylabel('Count', fontsize=11)
    ax2.set_title('Transaction Outcomes\n(Error Handling Demo)',
                  fontsize=12, fontweight='bold')
    ax2.grid(axis='y', alpha=0.3)
    
    plt.tight_layout()
    plt.savefig('transaction_rollback.png', dpi=300, bbox_inches='tight')
    print("   ✓ Visualization saved: transaction_rollback.png")
    plt.show()

finally:
    cursor.close()
    conn.close()

print("\n" + "="*70)
print("EXERCISE 3: TRANSACTION ROLLBACK - COMPLETE!")
print("="*70)
print("\nKEY TAKEAWAY:")
print("Transactions protect data integrity by rolling back ALL changes")
print("when ANY error occurs, preventing partial or invalid states.")
