import numpy as np
import pandas as pd
from keras.models import Sequential
from keras.layers import Dense, Activation
from sklearn.preprocessing import StandardScaler
from sklearn.linear_model import SGDClassifier
from sklearn.ensemble import RandomForestClassifier
from sklearn.neighbors import KNeighborsClassifier
from sklearn.svm import SVC
from sklearn.metrics import confusion_matrix, accuracy_score, precision_score, recall_score, f1_score, roc_curve, roc_auc_score
from time import time
import matplotlib
import matplotlib.pyplot as plt

# Data Preprocessing
np.random.seed(1337)
scaler = StandardScaler()
df = pd.read_csv('G:\\Team Drives\\ML-Based Anomaly Detection on Smart Power Grid\\KDD CUP Example\\expDataNumOnlyRemoveAttributesZerosOnly.csv')

# Setup training data
df_train = df.iloc[:20000, :]

features = ['duration', 'protocol_type', 'service', 'flag','src_bytes', 'dst_bytes',
            'wrong_fragment',	'hot',	'num_failed_logins',	'logged_in', 'num_compromised',
            'root_shell',	'su_attempted',	'num_root',	'num_file_creations','num_shells',
            'num_access_files',	'is_guest_login', 'count',	'srv_count',	'serror_rate',	'srv_serror_rate',
             'rerror_rate',	'srv_rerror_rate',	'same_srv_rate',	'diff_srv_rate',	'srv_diff_host_rate',
             'dst_host_count',	'dst_host_srv_count',	'dst_host_same_srv_rate',	'dst_host_diff_srv_rate',
             'dst_host_same_src_port_rate',	'dst_host_srv_diff_host_rate',	'dst_host_serror_rate',	'dst_host_srv_serror_rate',
             'dst_host_rerror_rate',	'dst_host_srv_rerror_rate']

X_train = scaler.fit_transform(df_train[features].values)
y_train = df_train['Result'].values
y_train_onehot = pd.get_dummies(df_train['Result']).values # one-hot encoding

# Setup testing data
df_test = df.iloc[20000:, :]
X_test = scaler.transform(df_test[features].values)
y_test = df_test['Result'].values

# ROC Plot Function
def plot_roc_curve(fpr, tpr, label=None):
    plt.plot(fpr, tpr, linewidth=2, label=label)
    plt.plot([0, 1], [0, 1], 'k--')
    plt.axis([0, 1, 0, 1])
    plt.xlabel('False Positive Rate', fontsize=16)
    plt.ylabel('True Positive Rate', fontsize=16)

"""
1-layer Neural Network using Keras
"""

start = time()

model = Sequential()
model.add(Dense(input_dim=37, output_dim=2))
model.add(Activation("softmax"))

model.compile(loss='categorical_crossentropy', optimizer='sgd', metrics=['accuracy'])

model.fit(X_train, y_train_onehot, epochs=10)

print ('\ntime taken %s seconds' % str(time() - start))

y_prediction = model.predict_classes(X_test)
print ("\n\naccuracy =", np.sum(y_prediction == y_test) / float(len(y_test)))
print ("\n\nprecision =", precision_score(y_test, y_prediction))
print ("\n\nrecall =", recall_score(y_test, y_prediction))
print ("\n\nF1 =", f1_score(y_test, y_prediction))
print ("\n\nAUC =", roc_auc_score(y_test, y_prediction))

y_scores = model.predict_proba(X_test)
y_scores = y_scores[:, 1]
fpr_NN1, tpr_NN1, thresholds_NN1 = roc_curve(y_test, y_scores)
plot_roc_curve(fpr_NN1, tpr_NN1, "1-Layer NN")
plt.legend(loc="lower right", fontsize=16)
plt.show()




"""
2-layer Neural Network using Keras
"""
start = time()

model = Sequential()
model.add(Dense(input_dim=37, output_dim=100))
model.add(Dense(output_dim=2))
model.add(Activation("softmax"))

model.compile(loss='categorical_crossentropy', optimizer='sgd', metrics=['accuracy'])

model.fit(X_train, y_train_onehot,epochs=10)

print ('\ntime taken %s seconds' % str(time() - start))

y_prediction = model.predict_classes(X_test)
print ("\n\naccuracy =", np.sum(y_prediction == y_test) / float(len(y_test)))
print ("\n\nprecision =", precision_score(y_test, y_prediction))
print ("\n\nrecall =", recall_score(y_test, y_prediction))
print ("\n\nF1 =", f1_score(y_test, y_prediction))
print ("\n\nAUC =", roc_auc_score(y_test, y_prediction))

y_scores = model.predict_proba(X_test)
y_scores = y_scores[:, 1]
fpr_NN2, tpr_NN2, thresholds_NN2 = roc_curve(y_test, y_scores)
plt.plot(fpr_NN1, tpr_NN1, "b:", linewidth=2, label="1-Layer NN")
plot_roc_curve(fpr_NN2, tpr_NN2, "2-Layer NN")
plt.legend(loc="lower right", fontsize=16)
plt.show()



"""
3-layer Neural Network using Keras
"""
start = time()

model = Sequential()
model.add(Dense(input_dim=37, output_dim=100))
model.add(Dense(output_dim=100))
model.add(Dense(output_dim=2))
model.add(Activation("softmax"))

model.compile(loss='categorical_crossentropy', optimizer='sgd', metrics=['accuracy'])

model.fit(X_train, y_train_onehot, epochs=10)

print ('\ntime taken %s seconds' % str(time() - start))

y_prediction = model.predict_classes(X_test)
print ("\n\naccuracy =", np.sum(y_prediction == y_test) / float(len(y_test)))
print ("\n\nprecision =", precision_score(y_test, y_prediction))
print ("\n\nrecall =", recall_score(y_test, y_prediction))
print ("\n\nF1 =", f1_score(y_test, y_prediction))
print ("\n\nAUC =", roc_auc_score(y_test, y_prediction))

y_scores = model.predict_proba(X_test)
y_scores = y_scores[:, 1]
fpr_NN3, tpr_NN3, thresholds_NN3 = roc_curve(y_test, y_scores)
plt.plot(fpr_NN1, tpr_NN1, "b:", linewidth=2, label="1-Layer NN")
plt.plot(fpr_NN2, tpr_NN2, "b:", linewidth=2, label="2-Layer NN")
plot_roc_curve(fpr_NN3, tpr_NN3, "3-Layer NN")
plt.legend(loc="lower right", fontsize=16)
plt.show()



"""
10-layer Neural Network using Keras
"""
start = time()

model = Sequential()
model.add(Dense(input_dim=37, output_dim=100))
model.add(Dense(output_dim=100))
model.add(Dense(output_dim=100))
model.add(Dense(output_dim=100))
model.add(Dense(output_dim=100))
model.add(Dense(output_dim=100))
model.add(Dense(output_dim=100))
model.add(Dense(output_dim=100))
model.add(Dense(output_dim=100))
model.add(Dense(output_dim=2))
model.add(Activation("softmax"))

model.compile(loss='categorical_crossentropy', optimizer='sgd', metrics=['accuracy'])

model.fit(X_train, y_train_onehot, epochs=10)

print ('\ntime taken %s seconds' % str(time() - start))

y_prediction = model.predict_classes(X_test)
print ("\n\naccuracy =", np.sum(y_prediction == y_test) / float(len(y_test)))
print ("\n\nprecision =", precision_score(y_test, y_prediction))
print ("\n\nrecall =", recall_score(y_test, y_prediction))
print ("\n\nF1 =", f1_score(y_test, y_prediction))
print ("\n\nAUC =", roc_auc_score(y_test, y_prediction))

y_scores = model.predict_proba(X_test)
y_scores = y_scores[:, 1]
fpr_NN10, tpr_NN10, thresholds_NN10 = roc_curve(y_test, y_scores)
plt.plot(fpr_NN1, tpr_NN1, "b:", linewidth=2, label="1-Layer NN")
plt.plot(fpr_NN2, tpr_NN2, "b:", linewidth=2, label="2-Layer NN")
plt.plot(fpr_NN3, tpr_NN3, "b:", linewidth=2, label="3-Layer NN")
plot_roc_curve(fpr_NN10, tpr_NN10, "10-Layer NN")
plt.legend(loc="lower right", fontsize=14)
plt.show()


"""
Stochastic Gradient Descent (SGD) Classifier using Scikit-Learn
"""
start = time()

sgd_clf = SGDClassifier(random_state=42, max_iter=10, tol=None)
sgd_clf.fit(X_train, y_train)

print ('\ntime taken %s seconds' % str(time() - start))

y_prediction = sgd_clf.predict(X_test)
print ("\n\naccuracy =", np.sum(y_prediction == y_test) / float(len(y_test)))
print ("\n\nprecision =", precision_score(y_test, y_prediction))
print ("\n\nrecall =", recall_score(y_test, y_prediction))
print ("\n\nF1 =", f1_score(y_test, y_prediction))
print ("\n\nAUC =", roc_auc_score(y_test, y_prediction))

fpr_SGD, tpr_SGD, thresholds_SGD = roc_curve(y_test, y_prediction)
plt.plot(fpr_NN1, tpr_NN1, "b:", linewidth=2, label="1-Layer NN")
plt.plot(fpr_NN2, tpr_NN2, "r:", linewidth=2, label="2-Layer NN")
plt.plot(fpr_NN3, tpr_NN3, "y:", linewidth=2, label="3-Layer NN")
plt.plot(fpr_NN10, tpr_NN10, "b:", linewidth=2, label="10-Layer NN")
plot_roc_curve(fpr_SGD, tpr_SGD, "SGD")
plt.legend(loc="lower right", fontsize=14)
plt.show()



"""
Random Forest Classifier using Scikit-Learn
"""
start = time()

RF_clf = RandomForestClassifier(random_state=42)
RF_clf.fit(X_train, y_train)

print ('\ntime taken %s seconds' % str(time() - start))

y_prediction = RF_clf.predict_proba(X_test)
y_scores = y_prediction[:, 1]
y_prediction = (y_scores > 0.5)

print ("\n\naccuracy =", np.sum(y_prediction == y_test) / float(len(y_test)))
print ("\n\nprecision =", precision_score(y_test, y_prediction))
print ("\n\nrecall =", recall_score(y_test, y_prediction))
print ("\n\nF1 =", f1_score(y_test, y_prediction))
print ("\n\nAUC =", roc_auc_score(y_test, y_prediction))

fpr_RF, tpr_RF, thresholds_RF = roc_curve(y_test, y_scores)
plt.figure(figsize=(20, 20))
plt.plot(fpr_NN1, tpr_NN1, "b:", linewidth=2, label="1-Layer NN")
plt.plot(fpr_NN2, tpr_NN2, "r:", linewidth=2, label="2-Layer NN")
plt.plot(fpr_NN3, tpr_NN3, "y:", linewidth=2, label="3-Layer NN")
plt.plot(fpr_NN10, tpr_NN10, "b:", linewidth=2, label="10-Layer NN")
plt.plot(fpr_SGD, tpr_SGD, "p:", linewidth=2, label="SGD")
plot_roc_curve(fpr_RF, tpr_RF, "RF")
plt.legend(loc="lower right", fontsize=14)
plt.show()





"""
K-Nearest Neighbors Classifier using Scikit-Learn
"""
start = time()

knn_clf = KNeighborsClassifier(n_jobs=-1, weights='distance', n_neighbors=10)
knn_clf.fit(X_train, y_train)

print ('\ntime taken %s seconds' % str(time() - start))

y_prediction = knn_clf.predict(X_test)

print ("\n\naccuracy =", accuracy_score(y_test, y_prediction))
print ("\n\nprecision =", precision_score(y_test, y_prediction))
print ("\n\nrecall =", recall_score(y_test, y_prediction))
print ("\n\nF1 =", f1_score(y_test, y_prediction))
print ("\n\nAUC =", roc_auc_score(y_test, y_prediction))




"""
Support Vector Machine Classifier using Scikit-Learn
"""
start = time()

svm_clf = SVC()
svm_clf.fit(X_train, y_train)

print ('\ntime taken %s seconds' % str(time() - start))

y_prediction = svm_clf.predict(X_test)

print ("\n\naccuracy =", accuracy_score(y_test, y_prediction))
print ("\n\nprecision =", precision_score(y_test, y_prediction))
print ("\n\nrecall =", recall_score(y_test, y_prediction))
print ("\n\nF1 =", f1_score(y_test, y_prediction))
print ("\n\nAUC =", roc_auc_score(y_test, y_prediction))