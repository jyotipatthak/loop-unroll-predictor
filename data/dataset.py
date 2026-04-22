import numpy as np
import pandas as pd

def generate_realistic_dataset(n=5000):
    np.random.seed(42)
    data = []

    for _ in range(n):
        # Core features
        trip_count = np.random.choice([4, 8, 16, 32, 64, 128, 256, 512])
        body_instr_count = np.random.randint(2, 50)
        memory_accesses = np.random.randint(0, 15)
        has_branch = np.random.randint(0, 2)
        loop_depth = np.random.randint(1, 5)
        vectorizable = np.random.randint(0, 2)
        live_vars = np.random.randint(1, 15)
        cache_line_hits = np.random.uniform(0.3, 1.0)

        # 🔥 NEW COMPLEX FEATURES
        instruction_level_parallelism = np.random.uniform(0.1, 1.0)
        branch_misprediction_rate = np.random.uniform(0, 0.4)
        cache_miss_rate = np.random.uniform(0, 0.6)

        # 🔥 SOFT PROBABILISTIC LABELING (not strict rules)
        score = 0

        # Positive signals for unrolling
        if trip_count >= 32:
            score += 2
        if body_instr_count < 20:
            score += 2
        if vectorizable:
            score += 2
        if cache_line_hits > 0.7:
            score += 1
        if instruction_level_parallelism > 0.6:
            score += 1

        # Negative signals
        if has_branch:
            score -= 2
        if live_vars > 10:
            score -= 2
        if branch_misprediction_rate > 0.2:
            score -= 1
        if cache_miss_rate > 0.4:
            score -= 1

        # 🔥 Convert score → class (OVERLAPPING BOUNDARIES)
        if score >= 5:
            factor = np.random.choice([4, 8], p=[0.4, 0.6])
        elif score >= 3:
            factor = np.random.choice([2, 4], p=[0.6, 0.4])
        elif score >= 1:
            factor = np.random.choice([1, 2], p=[0.7, 0.3])
        else:
            factor = 1

        # 🔥 Add noise (VERY IMPORTANT)
        if np.random.random() < 0.2:
            factor = np.random.choice([1, 2, 4, 8])

        data.append([
            trip_count, body_instr_count, memory_accesses, has_branch,
            loop_depth, vectorizable, live_vars, cache_line_hits,
            instruction_level_parallelism, branch_misprediction_rate,
            cache_miss_rate, factor
        ])

    cols = [
        'trip_count', 'body_instr_count', 'memory_accesses', 'has_branch',
        'loop_depth', 'vectorizable', 'live_vars', 'cache_line_hits',
        'instruction_level_parallelism', 'branch_misprediction_rate',
        'cache_miss_rate', 'unroll_factor'
    ]

    return pd.DataFrame(data, columns=cols)