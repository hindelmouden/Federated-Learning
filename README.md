# Federated_Learning_Banking

Federated Learning is a machine learning approach that allows a model to be trained across multiple decentralized devices or servers holding **local client data** (such as age, job, marital status, etc.) without ever transferring raw data to a central server. Instead, model updates are shared, ensuring **data privacy**. This technique is particularly suited for sectors like **banking**, where customer data is sensitive. It reduces the risk of data breaches and helps comply with privacy regulations.

This project simulates a federated learning environment where each client holds a portion of banking data used to train a model to predict **subscription to a bank term deposit**.

## Key Features:

- Simulates a Federated Learning scenario using **banking subscription data**.
- Uses the **Flower** framework to orchestrate federated learning.
- Trains a global model across **multiple local client datasets** without sharing data.
- Visualizes **Loss** and **Accuracy** over training rounds using `matplotlib`.

## Dependencies

- Python ≥ 3.8  
- NumPy  
- Pandas  
- TensorFlow  
- scikit-learn  
- Matplotlib  
- Flower (`flwr`)

To install all dependencies, run:

```bash
pip install -r requirements.txt
```

Or install them individually:

```bash
pip install flwr tensorflow scikit-learn matplotlib pandas
```

## Simulated Banking Dataset

The dataset simulates features commonly found in bank marketing campaigns:

- `age`
- `balance` (account balance)
- `job` (encoded as numeric)
- `marital` (encoded as numeric)
- `education` (encoded as numeric)
- `target` (1 if the client subscribed to a term deposit, 0 otherwise)

Data is randomly split across 5 simulated clients.

## How Federated Learning Works in This Project

1. Each client trains a local model on its subset of banking data.
2. After each round, only **model weights** (not data) are sent to a central server.
3. The server **aggregates** the weights and updates the global model.
4. The process repeats for multiple rounds.

## Visualizing Training Progress

Training performance is visualized over 20 rounds:

- **Loss decreases** as the model converges.
- **Accuracy increases** indicating better predictions.

You can visualize it using:

```python
import matplotlib.pyplot as plt
plt.plot(rounds, losses)
plt.plot(rounds, accuracies)
```
## Viedeo Demo 

**https://bit.ly/437uhTi**



## Resultat Federated Learning exemple
![Image](https://github.com/user-attachments/assets/f2bd447b-57d7-4c77-81a5-a2c06eccb1d8)

## Resultat exemple typique
![Image](https://github.com/user-attachments/assets/bc7463e8-e58f-4c25-b3f7-82c67e5e82bc)

## Data Client

https://archive.ics.uci.edu/dataset/222/bank+marketing


## Usage

To run this project locally:

1. Launch the server:
   ```bash
   python server.py
   ```

2. Launch each client in separate terminals:
   ```bash
   python client.py --client_id=0
   python client.py --client_id=1
   ...
   ```

3. Observe the output and final evaluation metrics.

Or use the Jupyter notebook `federated_learning_bank.ipynb` for an end-to-end run in a single environment.

## Contributing

If you'd like to improve or expand this project:

```bash
# Fork the repository
git checkout -b feature/your-feature
# Make your changes
git commit -m "Add new feature"
git push origin feature/your-feature
# Open a Pull Request
```

## License

This project is licensed under the [MIT License](https://opensource.org/license/mit/).
