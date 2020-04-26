import os
import random
import numpy as np
import pandas as pd


ATTRIBUTE_NAMES = [
    ["Age", "Gender", "Lives in Retirement Home"],
    ["Arterial Hypertension", "Diabetes", "Coronary Disease", "Prior AMI/CVI", "Hearth Failure",
     "Chronic Kidney Disease", "Obesity", "Asthma", "Compromised Immune System", "Malignant Disease",
     "Contact with Diseased", "ACIE Therapy", "ARB Therapy"],
    ["Fever (>37.5)", "Cough", "Breathing Problems", "Fatigue", "Headache", "Breast Pain", "Muscle/Joint Pain",
     "Changed Smell/Taste", "Sore Throat", "Stuffed Nose", "Diarrhea", "Night Sweating", "Nausea", "Runny Nose"],
    ["Body Temperature", "Breathing Frequency", "Blood Pressure High", "Blood Pressure High",
     "O2 Saturation", "Additional O2"],
    ["AF", "AST", "ALT", "LDH", "CRP", "Lkci", "Hb", "Ht", "Trombo", "Nevtrofilci", "Limfociti", "pH", "pCO2", "pO2",
     "D-dimer"],
    ["Infiltrates"],
    ["Hospitalisation", "Needs O2", "Intensive treatment", "Needs ventilator", "Treatment duration", "Survived"]
]
NUM = "numeric"
BIN = "binary"
ATTRIBUTE_TYPES = [
    [NUM, BIN, BIN],
    [BIN for _ in range(len(ATTRIBUTE_NAMES[1]))],
    [BIN for _ in range(len(ATTRIBUTE_NAMES[2]))],
    [NUM, NUM, NUM, NUM, NUM, BIN],
    [NUM for _ in range(len(ATTRIBUTE_NAMES[4]))],
    [BIN],
    [BIN, BIN, BIN, BIN, NUM, BIN]
]
DATA_DIR = "data"


def sanity_check():
    assert len(ATTRIBUTE_NAMES) == len(ATTRIBUTE_TYPES)
    for names, types in zip(ATTRIBUTE_NAMES, ATTRIBUTE_TYPES):
        assert len(names) == len(types)


sanity_check()


def generate_value(is_binary):
    t = random.random()
    if is_binary:
        return float(round(t))
    else:
        return t


def generate_data(n_hospitals, n_patients_total, target_indices, noise_level=0.1, seed=123):
    random.seed(seed)
    np.random.seed(seed)
    matrix = []
    for _ in range(n_patients_total):
        patient = []
        for types in ATTRIBUTE_TYPES:
            for t in types:
                patient.append(generate_value(t == BIN))
        matrix.append(patient)
    matrix = np.array(matrix)
    # replace the target values by the "actual values"
    n_features = matrix.shape[1] - len(target_indices)
    is_target = np.zeros(matrix.shape[1], dtype=bool)
    is_target[target_indices] = True
    coefficients = np.random.rand(n_features, len(target_indices))
    noise = np.random.rand(n_patients_total, len(target_indices)) * noise_level
    matrix[:, is_target] = np.dot(matrix[:, ~is_target], coefficients) + noise
    for t in target_indices:
        t_mean = np.mean(matrix[:, t])
        matrix[:, t] = [1 if matrix[i, t] > t_mean else 0 for i in range(n_patients_total)]
    flatten_columns = [c for cs in ATTRIBUTE_NAMES for c in cs]
    os.makedirs(DATA_DIR, exist_ok=True)
    for h in range(n_hospitals):
        data_frame = pd.DataFrame(data=matrix[h::n_hospitals, :], columns=flatten_columns)
        data_frame.to_csv(os.path.join(DATA_DIR, f"hospital{h}.csv"), index=False)
    data_frame = pd.DataFrame(data=matrix, columns=flatten_columns)
    data_frame.to_csv(os.path.join(DATA_DIR, f"hospitals.csv"), index=False)


generate_data(10, 1000, [52, 53, 54, 55, 56, 57])
