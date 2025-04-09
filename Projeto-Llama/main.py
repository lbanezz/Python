from transformers import LlamaTokenizer, LlamaForCausalLM
import torch
import sentencepiece

# Carregar o tokenizador e o modelo
model_name = "facebook/llama-7b"  # Ou o nome do modelo que você quer usar

tokenizer = LlamaTokenizer.from_pretrained(model_name)
model = LlamaForCausalLM.from_pretrained(model_name)

# Função para gerar texto
def gerar_texto(prompt):
    inputs = tokenizer(prompt, return_tensors="pt")
    outputs = model.generate(inputs['input_ids'], max_length=100, num_return_sequences=1)
    return tokenizer.decode(outputs[0], skip_special_tokens=True)

# Testar com um prompt
prompt = "Como a inteligência artificial pode transformar a educação?"
texto_gerado = gerar_texto(prompt)
print(texto_gerado)
