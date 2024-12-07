from ollama import chat 
from src.utils.data import Translation, Acceptable, FinalResult 


def review_translation(result)-> FinalResult:
    response = chat(
      messages=[
        {
          'role': 'user',
          'content': f"is the translation from english to german acceptable? English:{result.original_english_text}\n German:{result.full_german_translation}",
        }
      ],
      model='llama3.1',
      format=Acceptable.model_json_schema(),
    )
    result_acceptance = Acceptable.model_validate_json(response.message.content)
    return result_acceptance
