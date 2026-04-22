import numpy as np

def create_features(df):
    df['body_per_trip'] = df['body_instr_count'] / np.log2(df['trip_count'] + 1)
    df['memory_density'] = df['memory_accesses'] / (df['body_instr_count'] + 1)
    df['register_pressure'] = df['live_vars'] * df['body_instr_count']

    features = [
        'trip_count', 'body_instr_count', 'memory_accesses', 'has_branch',
        'loop_depth', 'vectorizable', 'live_vars', 'cache_line_hits',
        'instruction_level_parallelism', 'branch_misprediction_rate',
        'cache_miss_rate',
        'body_per_trip', 'memory_density', 'register_pressure'
    ]

    return df[features], df['unroll_factor']