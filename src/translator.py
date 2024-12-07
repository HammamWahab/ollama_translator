from ollama import chat 
from src.utils.data import Translation

def generate_translations(text: str) -> dict: 
    response = chat(
    messages=[
        {
        'role': 'user',
        'content': f'translate this to german: {text}',
        }
    ],
    model='llama3.1',
    format=Translation.model_json_schema(),
    )
    result = Translation.model_validate_json(response.message.content)
    return result