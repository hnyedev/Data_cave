#RANDOM FOREST

#gather data accross diferents clusters 
# then recoignaise the most often value

#tree --> one cluster
#forest --> all

"""
Instead of relying 
on a single tree,
 Random Forest aggregates their
 outputs —
usually by majority voting 
(for classification) or averaging (for regression).


Less overfitting:
 A single decision 
 tree can memorize the
   data too well and fail
to generalize. A forest of trees reduces this risk.

overfitting it is like get too acurate
with a single set of values and the model 
fails generalizing it memorize to well few values
that not represents 

on the other hand underfitting the 
model understanding about data is 
un-fittet like a XXL T-shirt
so it gets to general ad data

RANDOM FOREST HAS less overfitting

high acuracy

FEATURE RECOIGNISION


WORKS OUT OF THE BOX
minimal parameter tunning requierd to get 
decent results


EXAMPLES
VOTING OR AVERAGING REMEBER

Spam detection: Classify emails as spam or not spam.
Credit scoring: Decide whether a loan applicant is likely to repay.
Medical diagnosis: Help predict diseases based on symptoms and test results.
Fraud detection: Spot suspicious transactions in banking.
"""

"""
R-forest work technical aspects

first bootstraping

randomnly samples it multiple times
to create different subsets of training
"creating trees"

each subset is a tree


Random feature Selection

election
At each split in the tree, Random Forest 
randomly picks a subset of features to
consider. 
This ensures trees aren’t
 too similar to each other.

 diferent features to consider

 CLASSIFICATION --> VOTE

 REGRESSION --> AVERAGIN

 IT IS harder to understand that a single decition tree
 but better if masterizing
"""

"""
Advantages
Robust to noisy data
Handles missing values gracefully
Works well without heavy parameter tuning
Provides feature importance for insights


Limitations
Can be slower to train and predict if you have thousands of trees
Uses more memory
Less interpretable than a single decision tree
"""

from sklearn.ensemble import RandomForestClassifier
from sklearn.datasets import load_iris
from sklearn.model_selection import train_test_split
from sklearn.metrics import accuracy_score

data = load_iris()

#spliting data diferent times
X_train, X_test, y_train, y_test = train_test_split(data.data, data.target, test_size=0.3, random_state=42)
model = RandomForestClassifier(n_estimators=100, random_state=42)
model.fit(X_train, y_train)
print("Accuracy:", accuracy_score(y_test, y_pred))