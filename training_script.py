# Data paths
data:
  instruct_data: "/home/ubuntu/data/ultrachat_chunk_train.jsonl"
  eval_instruct_data: "/home/ubuntu/data/ultrachat_chunk_eval.jsonl"

# Model path
model_id_or_path: "/home/ubuntu/mistral_models/7B-v0.3"

# LoRA (Low-Rank Adaptation) settings
lora:
  rank: 16  # Reduced to avoid overfitting on small dataset

# Training parameters
seq_len: 8192
batch_size: 1
num_microbatches: 1  # Fixed microbatching issue
max_steps: 200  # Lowered from 500 to prevent overfitting
optim:
  lr: 5.e-5  # Slightly lower learning rate
  weight_decay: 0.01  # Reduced for better generalization
  pct_start: 0.05

# Other settings
seed: 0
log_freq: 1
eval_freq: 20  # More frequent evaluation
ckpt_freq: 50  # More frequent checkpoints
save_adapters: True
run_dir: "/home/ubuntu/test_ultra"

# Disable wandb (Weights & Biases)
wandb:
  offline: True
