"""Generated from Smithy shape ``com.amazonaws.workspaces#IpRuleList``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import capo_workspaces.types.ip_rule_item

IpRuleList: TypeAlias = list["capo_workspaces.types.ip_rule_item.IpRuleItem"]


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: IpRuleList) -> list:
    import capo_workspaces.types.ip_rule_item

    out: list = []
    for item in value:
        out.append(capo_workspaces.types.ip_rule_item.serialize_aws_json_1_1(item))
    return out


def deserialize_aws_json_1_1(data: list) -> IpRuleList:
    import capo_workspaces.types.ip_rule_item

    out: IpRuleList = []
    for item in data:
        if item is None:
            continue
        out.append(capo_workspaces.types.ip_rule_item.deserialize_aws_json_1_1(item))
    return out


# --- rpcv2Cbor ser/de ---
def serialize_cbor(value: IpRuleList) -> list:
    import capo_workspaces.types.ip_rule_item

    out: list = []
    for item in value:
        out.append(capo_workspaces.types.ip_rule_item.serialize_cbor(item))
    return out


def deserialize_cbor(data: list) -> IpRuleList:
    import capo_workspaces.types.ip_rule_item

    out: IpRuleList = []
    for item in data:
        if item is None:
            continue
        out.append(capo_workspaces.types.ip_rule_item.deserialize_cbor(item))
    return out
