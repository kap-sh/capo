"""Generated from Smithy shape ``com.amazonaws.securityhub#OrganizationConfigurationStatus``."""

from typing import Literal, TypeAlias, cast

OrganizationConfigurationStatus: TypeAlias = Literal[
    "PENDING",
    "ENABLED",
    "FAILED",
    "DISABLED",
]


# --- restJson1 ser/de ---
def serialize_json(value: OrganizationConfigurationStatus) -> str:
    return value


def deserialize_json(data: str) -> OrganizationConfigurationStatus:
    return cast(OrganizationConfigurationStatus, data)
