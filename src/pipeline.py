from src.translator import generate_translations 
from src.reviewer import review_translation 
from src.utils.data import FinalResult

def translation_pipeline(text):
    translation_result= generate_translations(text=text)
    acceptance_result= review_translation(translation_result)
    return FinalResult(translation=translation_result, is_acceptable=acceptance_result)

