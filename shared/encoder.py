from sentence_transformers import SentenceTransformer

from shared.config import (
    EMBEDDING_MODEL_NAME
)

_model = None


def get_model():

    global _model

    if _model is None:

        _model = SentenceTransformer(
            EMBEDDING_MODEL_NAME
        )

    return _model


def encode_documents(texts):

    model = get_model()

    embeddings = model.encode(
        texts,
        normalize_embeddings=True
    )

    return embeddings


def encode_query(text):

    model = get_model()

    embedding = model.encode(
        text,
        normalize_embeddings=True
    )

    return embedding