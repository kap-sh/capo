"""Generated from Smithy shape ``com.amazonaws.networkfirewall#RuleGroupType``."""

from typing import Literal, TypeAlias, cast

RuleGroupType: TypeAlias = Literal[
    "STATELESS",
    "STATEFUL",
    "STATEFUL_DOMAIN",
    "FIREWALL",
    "IPS",
]


# --- awsJson1_0 ser/de ---
def serialize_aws_json_1_0(value: RuleGroupType) -> str:
    return value


def deserialize_aws_json_1_0(data: str) -> RuleGroupType:
    return cast(RuleGroupType, data)


# --- rpcv2Cbor ser/de ---
def serialize_cbor(value: RuleGroupType) -> str:
    return value


def deserialize_cbor(data: str) -> RuleGroupType:
    return cast(RuleGroupType, data)
