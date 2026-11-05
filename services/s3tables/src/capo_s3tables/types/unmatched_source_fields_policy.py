"""Generated from Smithy shape ``com.amazonaws.s3tables#UnmatchedSourceFieldsPolicy``."""

from typing import Literal, TypeAlias, cast

UnmatchedSourceFieldsPolicy: TypeAlias = Literal[
    "fail",
    "drop",
]


# --- restJson1 ser/de ---
def serialize_json(value: UnmatchedSourceFieldsPolicy) -> str:
    return value


def deserialize_json(data: str) -> UnmatchedSourceFieldsPolicy:
    return cast(UnmatchedSourceFieldsPolicy, data)
