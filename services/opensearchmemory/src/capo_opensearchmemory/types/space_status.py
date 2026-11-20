"""Generated from Smithy shape ``com.amazonaws.opensearchmemory#SpaceStatus``."""

from typing import Literal, TypeAlias, cast

"""<p>The status of a space.</p>"""
SpaceStatus: TypeAlias = Literal[
    "CREATING",
    "ACTIVE",
    "UPDATING",
    "DELETING",
    "DELETED",
    "FAILED",
]


# --- awsJson1_0 ser/de ---
def serialize_aws_json_1_0(value: SpaceStatus) -> str:
    return value


def deserialize_aws_json_1_0(data: str) -> SpaceStatus:
    return cast(SpaceStatus, data)
