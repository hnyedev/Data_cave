#here start
print("hola")
import psycopg2
import pandas as pd
import matplotlib.pyplot as plt

print("-"*50)
print("EXERCISE 3: PostgreSQL DATABASE CONNECTION")
print("="*60)


#CONNECT WITH POSTGRESSQL
print("\nconecting with postgres")
try:#we are exposing information not cybersecure
    connection=psycopg2.connect(
        host='localhost',
        port=5435,#defining port 
        user='datauser',
        password='rootpass123',
        database='finance_db'
    )
except Exception as e:  
    print(f"bad connection{e}") 
    exit()

#QUERY STEP
cursor=connection.cursor()
sql_query="""
    SELECT
        category,
        COUNT(*) as transaction_count,
        SUM(amount) as total_amount
    FROM transactions
    GROUP BY category 
    ORDER BY total_amount DESC 
"""        
cursor.execute(sql_query) #cursor we are using a external
#curson into the container root
#it is like conect to my container via bash and i should use th cursor


results=cursor.fetchall()#funcion extract data 

#columnns
column_names=[desc[0] for desc in cursor.description]
print(f"query executed succesfully")
print(f"{len(results)}")#printing the len of the fetecheds

#dataframe
print("\n data framing the queries")
df=pd.DataFrame(results,columns=column_names)
#it is a data frame of the query with their names

print(df.to_string(index=False))
#to we print in strings

#calculating
total_amount=df['total_amount'].sum()
df['percentage'] = (df['total_amount'] / total_amount * 100).round(2)

print(f"\nTotal Expenses: ${total_amount:,.2f}")

#visualization

fig, ax= plt.subplots(figsize=(10,8))

colors=['#22543D', '#38A169', '#48BB78', '#9AE6B4', '#D9E70C', '#C6F6D5']

wedges,texts,autotexts= ax.pie(
    df['total_amount'],
    labels=df['category'],
    colors=colors,
    autopct='%1.1f%%',
    startangle=90,
    pctdistance=0.85
)
# Enhance text styling
for text in texts:
    text.set_fontsize(12)
    text.set_fontweight('bold')

for autotext in autotexts:
    autotext.set_color('white')
    autotext.set_fontsize(11)
    autotext.set_fontweight('bold')

# Add title
plt.title('Expense Distribution by Category', 
          fontsize=16, fontweight='bold', color='#1A202C', pad=20)

# Add center text showing total
centre_circle = plt.Circle((0, 0), 0.70, fc='white')
ax.add_artist(centre_circle)
ax.text(0, 0, f'Total\n${total_amount:.2f}',
        ha='center', va='center', fontsize=14, fontweight='bold')


plt.tight_layout()
plt.savefig('exercise3_visualization.png', dpi=300, bbox_inches='tight')
print("✓ Visualization saved as: exercise3_visualization.png")
plt.show()
print("\nStep 5: Category Breakdown")
for idx, row in df.iterrows():
    print(f"{row['category']:.<20} ${row['total_amount']:>8,.2f} ({row['percentage']:>5.1f}%)")

print(f"\nHighest Expense Category: {df.iloc[0]['category']} (${df.iloc[0]['total_amount']:,.2f})")
print(f"Lowest Expense Category: {df.iloc[-1]['category']} (${df.iloc[-1]['total_amount']:,.2f})")

#closing the cursor bash
cursor.close()
connection.close()
print("bash session closed")
