"""Generated from Smithy shape ``com.amazonaws.fms#ThirdPartyFirewallAssociationStatus``."""

from typing import Literal, TypeAlias, cast

ThirdPartyFirewallAssociationStatus: TypeAlias = Literal[
    "ONBOARDING",
    "ONBOARD_COMPLETE",
    "OFFBOARDING",
    "OFFBOARD_COMPLETE",
    "NOT_EXIST",
]


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: ThirdPartyFirewallAssociationStatus) -> str:
    return value


def deserialize_aws_json_1_1(data: str) -> ThirdPartyFirewallAssociationStatus:
    return cast(ThirdPartyFirewallAssociationStatus, data)


# --- rpcv2Cbor ser/de ---
def serialize_cbor(value: ThirdPartyFirewallAssociationStatus) -> str:
    return value


def deserialize_cbor(data: str) -> ThirdPartyFirewallAssociationStatus:
    return cast(ThirdPartyFirewallAssociationStatus, data)
