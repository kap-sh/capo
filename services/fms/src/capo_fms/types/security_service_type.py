"""Generated from Smithy shape ``com.amazonaws.fms#SecurityServiceType``."""

from typing import Literal, TypeAlias, cast

SecurityServiceType: TypeAlias = Literal[
    "WAF",
    "WAFV2",
    "SHIELD_ADVANCED",
    "SECURITY_GROUPS_COMMON",
    "SECURITY_GROUPS_CONTENT_AUDIT",
    "SECURITY_GROUPS_USAGE_AUDIT",
    "NETWORK_FIREWALL",
    "DNS_FIREWALL",
    "THIRD_PARTY_FIREWALL",
    "IMPORT_NETWORK_FIREWALL",
    "NETWORK_ACL_COMMON",
]


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: SecurityServiceType) -> str:
    return value


def deserialize_aws_json_1_1(data: str) -> SecurityServiceType:
    return cast(SecurityServiceType, data)


# --- rpcv2Cbor ser/de ---
def serialize_cbor(value: SecurityServiceType) -> str:
    return value


def deserialize_cbor(data: str) -> SecurityServiceType:
    return cast(SecurityServiceType, data)
