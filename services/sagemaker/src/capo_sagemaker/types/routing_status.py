"""Generated from Smithy shape ``com.amazonaws.sagemaker#RoutingStatus``."""

from typing import Literal, TypeAlias, cast

"""<p>Whether an inference router can send requests to a destination.</p>"""
RoutingStatus: TypeAlias = Literal[
    "Routable",
    "Unroutable",
    "Unknown",
]


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: RoutingStatus) -> str:
    return value


def deserialize_aws_json_1_1(data: str) -> RoutingStatus:
    return cast(RoutingStatus, data)
