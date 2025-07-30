import torch
from transformers import AutoTokenizer, AutoModelForCausalLM

def generate_text(model, tokenizer, prompt):
    inputs = tokenizer(prompt, return_tensors="pt")
    print("Input tokens:", inputs.input_ids[0].tolist())

    outputs = model.generate(
        **inputs,
        max_new_tokens=100,
        do_sample=False,  # greedy decoding
        pad_token_id=tokenizer.eos_token_id,
        eos_token_id=tokenizer.eos_token_id,
    )
    text = tokenizer.decode(outputs[0], skip_special_tokens=True)
    return text

def main():
    device = torch.device("cpu")
    print(f"Device set to: {device}")

    # Change these paths accordingly
    base_model_path = r"C:\Users\Vivek Ratan\Documents\llm\llama-env\Scripts\TinyLlama-1.1B-Chat-v1.0"
    finetuned_model_path = r"C:\Users\Vivek Ratan\Documents\llm\llama-env\tinyllama-ft"

    prompt = "Poem about the moon"

    print("\n--- Base model generation ---")
    tokenizer_base = AutoTokenizer.from_pretrained(base_model_path)
    model_base = AutoModelForCausalLM.from_pretrained(base_model_path).to(device)
    base_output = generate_text(model_base, tokenizer_base, prompt)
    print("Base model output:\n", base_output)

    print("\n--- Fine-tuned model generation ---")
    tokenizer_ft = AutoTokenizer.from_pretrained(finetuned_model_path)
    model_ft = AutoModelForCausalLM.from_pretrained(finetuned_model_path).to(device)
    ft_output = generate_text(model_ft, tokenizer_ft, prompt)
    print("Fine-tuned model output:\n", ft_output)

if __name__ == "__main__":
    main()
