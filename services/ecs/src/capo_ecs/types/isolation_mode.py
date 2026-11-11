"""Generated from Smithy shape ``com.amazonaws.ecs#IsolationMode``."""

from typing import Literal, TypeAlias, cast

"""<p>The isolation mode determines how a task is isolated from other tasks on the same Amazon EC2 instance.</p>"""
IsolationMode: TypeAlias = Literal[
    "SHARED",
    "ISOLATED_SANDBOX",
    "CONFIDENTIAL_SANDBOX",
]


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: IsolationMode) -> str:
    return value


def deserialize_aws_json_1_1(data: str) -> IsolationMode:
    return cast(IsolationMode, data)
