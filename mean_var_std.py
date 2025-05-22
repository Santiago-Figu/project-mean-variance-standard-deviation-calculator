import numpy as np

def calculate(list):
    if len(list) != 9:
        raise ValueError("List must contain nine numbers.")
    matrix = np.array(list).reshape(3, 3)
    flattened_matrix = matrix.flatten()
    
    calculations = {
        'mean': [
            matrix.mean(axis=0, dtype=float).tolist(),
            matrix.mean(axis=1, dtype=float).tolist(),
            float(np.mean(flattened_matrix))
        ],
        'variance': [
            matrix.var(axis=0, dtype=float).tolist(),
            matrix.var(axis=1, dtype=float).tolist(),
            float(flattened_matrix.var(dtype=float))
        ],
        'standard deviation': [
            matrix.std(axis=0, dtype=float).tolist(),
            matrix.std(axis=1, dtype=float).tolist(),
            float(flattened_matrix.std(dtype=float))
        ],
        'max': [
            matrix.max(axis=0).tolist(),
            matrix.max(axis=1).tolist(),
            int(flattened_matrix.max())
        ],
        'min': [
            matrix.min(axis=0).tolist(),
            matrix.min(axis=1).tolist(),
            int(flattened_matrix.min())
        ],
        'sum': [
            matrix.sum(axis=0).tolist(),
            matrix.sum(axis=1).tolist(),
            int(flattened_matrix.sum())
        ],
    }
    return calculations