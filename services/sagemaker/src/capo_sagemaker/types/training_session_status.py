"""Generated from Smithy shape ``com.amazonaws.sagemaker#TrainingSessionStatus``."""

from typing import Literal, TypeAlias, cast

"""<p>The status of a training session.</p>"""
TrainingSessionStatus: TypeAlias = Literal[
    "Created",
    "Blocked",
    "Running",
    "Failed",
    "Scheduled",
    "Stopping",
    "Stopped",
    "Expired",
    "Deleting",
    "DeletionFailed",
]


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: TrainingSessionStatus) -> str:
    return value


def deserialize_aws_json_1_1(data: str) -> TrainingSessionStatus:
    return cast(TrainingSessionStatus, data)
