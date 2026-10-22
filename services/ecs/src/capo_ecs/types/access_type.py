"""Generated from Smithy shape ``com.amazonaws.ecs#AccessType``."""

from typing import Literal, TypeAlias, cast

"""<p>Specifies whether a resource is publicly accessible from the internet or private to a VPC.</p>"""
AccessType: TypeAlias = Literal[
    "PUBLIC",
    "PRIVATE",
]


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: AccessType) -> str:
    return value


def deserialize_aws_json_1_1(data: str) -> AccessType:
    return cast(AccessType, data)
