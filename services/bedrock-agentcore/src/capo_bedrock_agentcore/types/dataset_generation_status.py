"""Generated from Smithy shape ``com.amazonaws.bedrockagentcore#DatasetGenerationStatus``."""

from typing import Literal, TypeAlias, cast

"""<p>The status of a dataset generation.</p>"""
DatasetGenerationStatus: TypeAlias = Literal[
    "IN_PROGRESS",
    "COMPLETED",
    "COMPLETED_WITH_ERRORS",
    "FAILED",
    "DELETING",
]


# --- restJson1 ser/de ---
def serialize_json(value: DatasetGenerationStatus) -> str:
    return value


def deserialize_json(data: str) -> DatasetGenerationStatus:
    return cast(DatasetGenerationStatus, data)
