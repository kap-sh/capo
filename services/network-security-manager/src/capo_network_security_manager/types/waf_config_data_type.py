"""Generated from Smithy shape ``com.amazonaws.networksecuritymanager#WAFConfigDataType``."""

from typing import Literal, TypeAlias, cast

WAFConfigDataType: TypeAlias = Literal[
    "DefaultAction",
    "VisibilityConfig",
    "CaptchaConfig",
    "ChallengeConfig",
    "CustomResponseBodies",
    "LoggingConfiguration",
    "DataProtectionConfig",
    "AssociationConfig",
    "OnSourceDDoSProtectionConfig",
    "TokenDomains",
]


# --- restJson1 ser/de ---
def serialize_json(value: WAFConfigDataType) -> str:
    return value


def deserialize_json(data: str) -> WAFConfigDataType:
    return cast(WAFConfigDataType, data)
