from datasets import load_dataset
from pydantic import BaseModel
from ollama import chat 
import concurrent.futures
from tqdm import tqdm 
from src.pipeline import translation_pipeline


#load data 

dataset_path = ''
dataset = load_dataset('json', data_files=dataset_path, split='train')
print(dataset)

discharge_instructions = dataset['text']

def main():


    results = []
    num_workers = 32
    with concurrent.futures.ThreadPoolExecutor(max_workers=num_workers) as executor:
        futures = [executor.submit(translation_pipeline, extract)  for extract in discharge_instructions[:2]]
        for future in tqdm(concurrent.futures.as_completed(futures), total=len(futures)):
            results.append(future.result())

    print(results)


if __name__ == "__main__":
    main()