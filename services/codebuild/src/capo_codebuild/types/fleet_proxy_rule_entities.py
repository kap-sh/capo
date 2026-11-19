"""Generated from Smithy shape ``com.amazonaws.codebuild#FleetProxyRuleEntities``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import capo_codebuild.types.string

FleetProxyRuleEntities: TypeAlias = list["capo_codebuild.types.string.String"]


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: FleetProxyRuleEntities) -> list:
    return list(value)


def deserialize_aws_json_1_1(data: list) -> FleetProxyRuleEntities:
    return [item for item in data if item is not None]


# --- rpcv2Cbor ser/de ---
def serialize_cbor(value: FleetProxyRuleEntities) -> list:
    return list(value)


def deserialize_cbor(data: list) -> FleetProxyRuleEntities:
    return [item for item in data if item is not None]
