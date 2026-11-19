"""Generated from Smithy shape ``com.amazonaws.sagemaker#InferenceRouterStatus``."""

from typing import Literal, TypeAlias, cast

"""<p>The status of an inference router.</p>"""
InferenceRouterStatus: TypeAlias = Literal[
    "InService",
    "Creating",
    "Updating",
    "Failed",
    "Deleting",
]


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: InferenceRouterStatus) -> str:
    return value


def deserialize_aws_json_1_1(data: str) -> InferenceRouterStatus:
    return cast(InferenceRouterStatus, data)
