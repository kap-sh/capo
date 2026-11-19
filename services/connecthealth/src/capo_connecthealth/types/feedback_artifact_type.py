"""Generated from Smithy shape ``com.amazonaws.connecthealth#FeedbackArtifactType``."""

from typing import Literal, TypeAlias, cast

FeedbackArtifactType: TypeAlias = Literal[
    "CLINICAL_DOC",
    "MEDICAL_CODES",
]


# --- restJson1 ser/de ---
def serialize_json(value: FeedbackArtifactType) -> str:
    return value


def deserialize_json(data: str) -> FeedbackArtifactType:
    return cast(FeedbackArtifactType, data)
