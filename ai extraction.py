import instructor
from schema import MovieSchema

MODEL = "gemma3:4b"

client = instructor.from_provider(f"ollama/{MODEL}")

SYSTEM_PROMPT = """
Extract the movie title and review from the text.
Return:
- title
- review
"""

FEW_SHOT_EXAMPLES = [
    {
        "role": "user",
        "content": "Tenet 2020 Nolan film. Confusing but cool",
    },
    {
        "role": "assistant",
        "content": '{"title": "Tenet", "review": "Confusing but cool Nolan film from 2020."}',
    },
]

def extract_movie(text: str) -> MovieSchema:
    return client.create(
        response_model=MovieSchema,
        messages=[
            {"role": "system", "content": SYSTEM_PROMPT},
            *FEW_SHOT_EXAMPLES,
            {"role": "user", "content": text},
        ],
    )

if __name__ == "__main__":
    result = extract_movie(
        "Inception is a mind-bending sci-fi movie by Nolan. Very confusing but brilliant."
    )
    print(result)