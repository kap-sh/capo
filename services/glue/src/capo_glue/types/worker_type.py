"""Generated from Smithy shape ``com.amazonaws.glue#WorkerType``."""

from typing import Literal, TypeAlias, cast

WorkerType: TypeAlias = Literal[
    "Standard",
    "G.1X",
    "G.2X",
    "G.4X",
    "G.8X",
    "G.025X",
    "Z.2X",
    "G.12X",
    "G.16X",
    "R.1X",
    "R.2X",
    "R.4X",
    "R.8X",
]


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: WorkerType) -> str:
    return value


def deserialize_aws_json_1_1(data: str) -> WorkerType:
    return cast(WorkerType, data)
