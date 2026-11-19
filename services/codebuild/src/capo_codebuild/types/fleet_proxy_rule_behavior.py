"""Generated from Smithy shape ``com.amazonaws.codebuild#FleetProxyRuleBehavior``."""

from typing import Literal, TypeAlias, cast

FleetProxyRuleBehavior: TypeAlias = Literal[
    "ALLOW_ALL",
    "DENY_ALL",
]


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: FleetProxyRuleBehavior) -> str:
    return value


def deserialize_aws_json_1_1(data: str) -> FleetProxyRuleBehavior:
    return cast(FleetProxyRuleBehavior, data)


# --- rpcv2Cbor ser/de ---
def serialize_cbor(value: FleetProxyRuleBehavior) -> str:
    return value


def deserialize_cbor(data: str) -> FleetProxyRuleBehavior:
    return cast(FleetProxyRuleBehavior, data)
