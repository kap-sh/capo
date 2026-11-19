"""Generated from Smithy shape ``com.amazonaws.securityhub#ConfigurationPolicyAssociationStatus``."""

from typing import Literal, TypeAlias, cast

ConfigurationPolicyAssociationStatus: TypeAlias = Literal[
    "PENDING",
    "SUCCESS",
    "FAILED",
    "DISABLED",
]


# --- restJson1 ser/de ---
def serialize_json(value: ConfigurationPolicyAssociationStatus) -> str:
    return value


def deserialize_json(data: str) -> ConfigurationPolicyAssociationStatus:
    return cast(ConfigurationPolicyAssociationStatus, data)
