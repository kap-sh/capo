"""Generated from Smithy shape ``com.amazonaws.fms#NetworkAclRuleAction``."""

from typing import Literal, TypeAlias, cast

NetworkAclRuleAction: TypeAlias = Literal[
    "allow",
    "deny",
]


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: NetworkAclRuleAction) -> str:
    return value


def deserialize_aws_json_1_1(data: str) -> NetworkAclRuleAction:
    return cast(NetworkAclRuleAction, data)


# --- rpcv2Cbor ser/de ---
def serialize_cbor(value: NetworkAclRuleAction) -> str:
    return value


def deserialize_cbor(data: str) -> NetworkAclRuleAction:
    return cast(NetworkAclRuleAction, data)
