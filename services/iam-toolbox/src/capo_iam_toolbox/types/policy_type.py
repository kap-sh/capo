"""Generated from Smithy shape ``com.amazonaws.iamtoolbox#PolicyType``."""

from typing import Literal, TypeAlias, cast

"""<p>The policy type.</p>"""
PolicyType: TypeAlias = Literal[
    "IDENTITY_BASED_POLICY",
    "RESOURCE_BASED_POLICY",
    "PERMISSIONS_BOUNDARY",
    "SESSION_POLICY",
    "SERVICE_CONTROL_POLICY",
    "RESOURCE_CONTROL_POLICY",
    "VPC_ENDPOINT_POLICY",
]


# --- restJson1 ser/de ---
def serialize_json(value: PolicyType) -> str:
    return value


def deserialize_json(data: str) -> PolicyType:
    return cast(PolicyType, data)
