"""Generated from Smithy shape ``com.amazonaws.codebuild#FleetProxyRuleType``."""

from typing import Literal, TypeAlias, cast

FleetProxyRuleType: TypeAlias = Literal[
    "DOMAIN",
    "IP",
]


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: FleetProxyRuleType) -> str:
    return value


def deserialize_aws_json_1_1(data: str) -> FleetProxyRuleType:
    return cast(FleetProxyRuleType, data)


# --- rpcv2Cbor ser/de ---
def serialize_cbor(value: FleetProxyRuleType) -> str:
    return value


def deserialize_cbor(data: str) -> FleetProxyRuleType:
    return cast(FleetProxyRuleType, data)
