from pydantic import BaseModel

class Translation(BaseModel):
    original_english_text: str 
    full_german_translation: str 


class Acceptable(BaseModel):
    is_translation_acceptable: bool 


class FinalResult(BaseModel):
    translation: Translation
    is_acceptable: Acceptable 