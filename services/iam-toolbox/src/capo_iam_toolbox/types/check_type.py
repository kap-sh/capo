"""Generated from Smithy shape ``com.amazonaws.iamtoolbox#CheckType``."""

from typing import Literal, TypeAlias, cast

"""<p>The authorization requirement that a check evaluates, such as SCPs at one organization target, principal permissions, or the session.</p>"""
CheckType: TypeAlias = Literal[
    "SERVICE_CONTROL_POLICY",
    "RESOURCE_CONTROL_POLICY",
    "VPC_ENDPOINT",
    "RESOURCE",
    "PRINCIPAL",
    "PERMISSIONS_BOUNDARY",
    "SESSION",
]


# --- restJson1 ser/de ---
def serialize_json(value: CheckType) -> str:
    return value


def deserialize_json(data: str) -> CheckType:
    return cast(CheckType, data)
