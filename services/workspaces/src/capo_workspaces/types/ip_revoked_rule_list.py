"""Generated from Smithy shape ``com.amazonaws.workspaces#IpRevokedRuleList``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import capo_workspaces.types.ip_rule

IpRevokedRuleList: TypeAlias = list["capo_workspaces.types.ip_rule.IpRule"]


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: IpRevokedRuleList) -> list:
    return list(value)


def deserialize_aws_json_1_1(data: list) -> IpRevokedRuleList:
    return [item for item in data if item is not None]


# --- rpcv2Cbor ser/de ---
def serialize_cbor(value: IpRevokedRuleList) -> list:
    return list(value)


def deserialize_cbor(data: list) -> IpRevokedRuleList:
    return [item for item in data if item is not None]
