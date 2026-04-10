import pandas as pd 

# Define column names (41 features + 1 label)
# columns = [
#     'duration', 'protocol_type', 'service', 'flag', 'src_bytes', 'dst_bytes',
#     'land', 'wrong_fragment', 'urgent', 'hot', 'num_failed_logins',
#     'logged_in', 'num_compromised', 'root_shell', 'su_attempted',
#     'num_root', 'num_file_creations', 'num_shells', 'num_access_files',
#     'num_outbound_cmds', 'is_host_login', 'is_guest_login', 'count',
#     'srv_count', 'serror_rate', 'srv_serror_rate', 'rerror_rate',
#     'srv_rerror_rate', 'same_srv_rate', 'diff_srv_rate', 'srv_diff_host_rate',
#     'dst_host_count', 'dst_host_srv_count', 'dst_host_same_srv_rate',
#     'dst_host_diff_srv_rate', 'dst_host_same_src_port_rate',
#     'dst_host_srv_diff_host_rate', 'dst_host_serror_rate',
#     'dst_host_srv_serror_rate', 'dst_host_rerror_rate',
#     'dst_host_srv_rerror_rate'
# ]

# Read the .txt file as CSV
data  = pd.read_csv('/home/hadil/Desktop/Automated_threat_detection/backend/data/KDDTrain+.txt', header=None) 
# data.columns = columns
sample = data.copy()
# Convert label to binary (0 = normal, 1 = attack)
# df['binary_label'] = (df['label'] != 'normal.').astype(int)
print(f"Number of columns in file: {len(sample.columns)}")
# Define column names based on what we found
if len(sample.columns) == 43:
    # Has difficulty column
    column_names = [f'feature_{i}' for i in range(41)] + ['label', 'difficulty']
    df = pd.read_csv('/home/hadil/Desktop/Automated_threat_detection/backend/data/KDDTrain+.txt', header=None, names=column_names)
print(df.head())
print(f"Shape: {df.shape}")

print(f"\nColumn name: 'difficulty'")
print(f"Data type: {df['difficulty'].dtype}")
print(f"Minimum value: {df['difficulty'].min()}")
print(f"Maximum value: {df['difficulty'].max()}")
print(f"Unique values: {sorted(df['difficulty'].unique())}")