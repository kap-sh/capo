"""Generated from Smithy shape ``com.amazonaws.glue#Status``."""

from typing import Literal, TypeAlias, cast

"""<p>The current status of an upgrade analysis. Possible values are <code>OBSERVING</code>, <code>WAITING_FOR_CONSENT</code>, <code>UPGRADING</code>, <code>SUCCEEDED</code>, <code>FAILED</code>, <code>TIMEOUT</code>, and <code>STOPPED</code>.</p>"""
Status: TypeAlias = Literal[
    "OBSERVING",
    "WAITING_FOR_CONSENT",
    "UPGRADING",
    "SUCCEEDED",
    "FAILED",
    "TIMEOUT",
    "STOPPED",
]


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: Status) -> str:
    return value


def deserialize_aws_json_1_1(data: str) -> Status:
    return cast(Status, data)
