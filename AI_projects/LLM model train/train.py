import torch
from transformers import AutoTokenizer, AutoModelForCausalLM, Trainer, TrainingArguments
from datasets import load_dataset

# Step 1: Load the model and tokenizer
MODEL_PATH = "C:/Users/Vivek Ratan/Documents/llm/llama-env/Scripts/TinyLlama-1.1B-Chat-v1.0"
tokenizer = AutoTokenizer.from_pretrained(MODEL_PATH)
model = AutoModelForCausalLM.from_pretrained(MODEL_PATH)

# Step 2: Load the dataset
dataset = load_dataset("json", data_files="C:/Users/Vivek Ratan/Documents/llm/llama-env/journey_finetune_50_styled.jsonl", split="train")

# Step 3: Tokenize the dataset
def tokenize_function(examples):
    # Tokenize instruction, input, and output
    return tokenizer(
        examples['instruction'], 
        examples['input'], 
        examples['output'], 
        padding="max_length", 
        truncation=True,
        max_length=512  # adjust max_length according to your needs
    )

# Apply the tokenization to the dataset
tokenized_dataset = dataset.map(tokenize_function, batched=True)

# Step 4: Define the training arguments
training_args = TrainingArguments(
    output_dir="C:/Users/Vivek Ratan/Documents/llm/llama-env/tinyllama-ft",  # path to save the model
    per_device_train_batch_size=4,  # batch size per device during training
    num_train_epochs=3,  # number of training epochs
    logging_dir="logs",  # directory for storing logs
    logging_steps=10,
    save_steps=100,  # number of steps before saving the model checkpoint
    save_total_limit=2,  # limit on the total number of checkpoints
    remove_unused_columns=False,  # remove unused columns after tokenization
)

# Step 5: Initialize the Trainer
trainer = Trainer(
    model=model,  # the model you are fine-tuning
    args=training_args,
    train_dataset=tokenized_dataset,  # your tokenized dataset
)

# Step 6: Start training
trainer.train()

# Step 7: Save the trained model
trainer.save_model("C:/Users/Vivek Ratan/Documents/llm/llama-env/tinyllama-ft")

# Optionally save tokenizer as well (if you made any changes)
tokenizer.save_pretrained("C:/Users/Vivek Ratan/Documents/llm/llama-env/tinyllama-ft")
