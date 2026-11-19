"""Generated from Smithy shape ``com.amazonaws.lightsail#SubdomainState``."""

from typing import Literal, TypeAlias, cast

SubdomainState: TypeAlias = Literal[
    "CREATING",
    "CREATE_FAILED",
    "UNATTACHED",
    "ATTACHING",
    "ATTACHED",
    "DETACHING",
    "TRANSFERRING",
    "IMPLICIT",
]


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: SubdomainState) -> str:
    return value


def deserialize_aws_json_1_1(data: str) -> SubdomainState:
    return cast(SubdomainState, data)
