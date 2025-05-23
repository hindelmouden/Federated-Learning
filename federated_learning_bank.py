
# pip install tensorflow tensorflow_federated numpy matplotlib

import numpy as np
import tensorflow as tf
from tensorflow import keras
from tensorflow.keras import layers
import matplotlib.pyplot as plt

#  Générer des données synthétiques pour simuler des clients
def generate_synthetic_data():
    n = 1000 
    np.random.seed(42) 

    age = np.random.randint(18, 71, size=n)

    monthly_income = np.random.normal(loc=7000, scale=2000, size=n)
    monthly_income = np.clip(monthly_income, 1000, 15000)

    credit_score = np.random.normal(loc=600, scale=100, size=n)
    credit_score = np.clip(credit_score, 300, 850)

    num_products = np.random.randint(0, 6, size=n)

    transaction_activity = np.random.poisson(lam=30, size=n)

    X = np.stack([age, monthly_income, credit_score, num_products, transaction_activity], axis=1)

    y = np.random.randint(0, 2, size=n)

    return X, y


#  Définir un modèle de réseau de neurones
def create_model():
    model = keras.Sequential([
        layers.Dense(64, activation='relu', input_shape=(5,)),
        layers.Dense(32, activation='relu'),
        layers.Dense(1, activation='sigmoid')
    ])
    model.compile(optimizer='adam', loss='binary_crossentropy', metrics=['accuracy'])
    return model

#  Entraînement fédéré 
def federated_training(rounds=20, num_clients=5):
    global_model = create_model()
    history = {'loss': [], 'accuracy': []}

    for round_num in range(rounds):
        client_weights = []

        for client_id in range(num_clients):
            # Chaque client a ses propres données
            X, y = generate_synthetic_data()
            client_model = create_model()
            client_model.set_weights(global_model.get_weights())  
            client_model.fit(X, y, epochs=1, batch_size=32, verbose=0)  
            client_weights.append(client_model.get_weights())  

        # Agrégation des poids : moyenne
        new_weights = np.mean(client_weights, axis=0)
        global_model.set_weights(new_weights)

       
        X_test, y_test = generate_synthetic_data()
        loss, accuracy = global_model.evaluate(X_test, y_test, verbose=0)
        history['loss'].append(loss)
        history['accuracy'].append(accuracy)

        print(f"Round {round_num + 1}, Loss: {loss:.4f}, Accuracy: {accuracy:.4f}")

    return history


history = federated_training(rounds=20, num_clients=5)

#  Visualisation des performances
plt.figure(figsize=(12, 5))

# Courbe de la perte (loss)
plt.subplot(1, 2, 1)
plt.plot(range(1, 21), history['loss'], marker='o', color='red')
plt.title("Évolution de la Perte (Loss)")
plt.xlabel("Round")
plt.ylabel("Perte")
plt.grid(True)

# Courbe de la précision (accuracy)
plt.subplot(1, 2, 2)
plt.plot(range(1, 21), history['accuracy'], marker='o', color='green')
plt.title("Évolution de la Précision (Accuracy)")
plt.xlabel("Round")
plt.ylabel("Précision")
plt.grid(True)

plt.tight_layout()
plt.show()






# exemple illustratif
import matplotlib.pyplot as plt

# Données simulées des 20 rounds
rounds = list(range(1, 21))
pertes = [0.65, 0.61, 0.58, 0.55, 0.53, 0.51, 0.49, 0.47, 0.46, 0.45,
          0.44, 0.43, 0.42, 0.41, 0.40, 0.39, 0.38, 0.37, 0.36, 0.35]
precisions = [0.72, 0.75, 0.77, 0.78, 0.80, 0.81, 0.82, 0.83, 0.84, 0.85,
              0.85, 0.86, 0.86, 0.87, 0.87, 0.87, 0.88, 0.88, 0.88, 0.88]

plt.figure(figsize=(12, 5))

# Courbe de la perte
plt.subplot(1, 2, 1)
plt.plot(rounds, pertes, marker='o', color='red')
plt.title("Évolution de la Perte (Loss)")
plt.xlabel("Round")
plt.ylabel("Perte")
plt.grid(True)

# Courbe de la précision
plt.subplot(1, 2, 2)
plt.plot(rounds, precisions, marker='o', color='green')
plt.title("Évolution de la Précision (Accuracy)")
plt.xlabel("Round")
plt.ylabel("Précision")
plt.grid(True)

plt.tight_layout()
plt.show()


![Image](https://github.com/user-attachments/assets/bc7463e8-e58f-4c25-b3f7-82c67e5e82bc)



