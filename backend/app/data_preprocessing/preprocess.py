import pandas as pd 

# Define column names (41 features + 1 label)
column_names = [
    # Basic features 
    'duration', 'protocol_type', 'service', 'flag', 'src_bytes', 'dst_bytes',
    'land', 'wrong_fragment', 'urgent',
    
    # Content features
    'hot', 'num_failed_logins', 'logged_in', 'num_compromised', 'root_shell',
    'su_attempted', 'num_root', 'num_file_creations', 'num_shells',
    'num_access_files', 'num_outbound_cmds', 'is_host_login', 'is_guest_login',
    
    # Time-based traffic features 
    'count', 'srv_count', 'serror_rate', 'srv_serror_rate', 'rerror_rate',
    'srv_rerror_rate', 'same_srv_rate', 'diff_srv_rate', 'srv_diff_host_rate',
    'dst_host_count',
    
    # Host-based traffic features 
    'dst_host_srv_count', 'dst_host_same_srv_rate', 'dst_host_diff_srv_rate',
    'dst_host_same_src_port_rate', 'dst_host_srv_diff_host_rate',
    'dst_host_serror_rate', 'dst_host_srv_serror_rate', 'dst_host_rerror_rate',
    'dst_host_srv_rerror_rate',
    
    # Label and difficulty
    'label', 'difficulty'
]
# Read the .txt file as CSV
data  = pd.read_csv('/home/hadil/Desktop/Automated_threat_detection/backend/data/KDDTrain+.txt', header=None , names=column_names) 
# data.columns = columns
df = data.copy()

print(df.head())
print(f"Shape: {df.shape}")
