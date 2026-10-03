"""Generated from Smithy shape ``com.amazonaws.bedrockagent#EmbeddingModelType``."""

from typing import Literal, TypeAlias, cast

"""<p>Choose <code>CUSTOM</code> to provide your own Bedrock embedding model ARN. Choose <code>MANAGED</code> to use a service-managed embedding model. For more information, see <a href="https://docs.aws.amazon.com/bedrock/latest/userguide/kb-managed-create.html#kb-managed-embedding-models">Embedding model options</a>.</p>"""
EmbeddingModelType: TypeAlias = Literal[
    "CUSTOM",
    "MANAGED",
]


# --- restJson1 ser/de ---
def serialize_json(value: EmbeddingModelType) -> str:
    return value


def deserialize_json(data: str) -> EmbeddingModelType:
    return cast(EmbeddingModelType, data)
