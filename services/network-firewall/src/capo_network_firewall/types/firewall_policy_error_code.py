"""Generated from Smithy shape ``com.amazonaws.networkfirewall#FirewallPolicyErrorCode``."""

from typing import Literal, TypeAlias, cast

FirewallPolicyErrorCode: TypeAlias = Literal[
    "DNS_FIREWALL_RULE_GROUP_UNAVAILABLE",
    "ROUTE53_RESOLVED_IP_VALIDATION_MISSING",
]


# --- awsJson1_0 ser/de ---
def serialize_aws_json_1_0(value: FirewallPolicyErrorCode) -> str:
    return value


def deserialize_aws_json_1_0(data: str) -> FirewallPolicyErrorCode:
    return cast(FirewallPolicyErrorCode, data)


# --- rpcv2Cbor ser/de ---
def serialize_cbor(value: FirewallPolicyErrorCode) -> str:
    return value


def deserialize_cbor(data: str) -> FirewallPolicyErrorCode:
    return cast(FirewallPolicyErrorCode, data)
