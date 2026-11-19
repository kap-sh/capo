"""Generated from Smithy shape ``com.amazonaws.workspaces#WorkspacesIpGroup``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_workspaces.types.ip_group_desc
    import capo_workspaces.types.ip_group_id
    import capo_workspaces.types.ip_group_name
    import capo_workspaces.types.ip_rule_list


class WorkspacesIpGroup(TypedDict, closed=True):
    group_id: NotRequired["capo_workspaces.types.ip_group_id.IpGroupId"]
    """<p>The identifier of the group.</p>"""
    group_name: NotRequired["capo_workspaces.types.ip_group_name.IpGroupName"]
    """<p>The name of the group.</p>"""
    group_desc: NotRequired["capo_workspaces.types.ip_group_desc.IpGroupDesc"]
    """<p>The description of the group.</p>"""
    user_rules: NotRequired["capo_workspaces.types.ip_rule_list.IpRuleList"]
    """<p>The rules.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: WorkspacesIpGroup) -> dict:
    out: dict = {}
    if "group_id" in value:
        out["groupId"] = value["group_id"]
    if "group_name" in value:
        out["groupName"] = value["group_name"]
    if "group_desc" in value:
        out["groupDesc"] = value["group_desc"]
    if "user_rules" in value:
        import capo_workspaces.types.ip_rule_list

        out["userRules"] = capo_workspaces.types.ip_rule_list.serialize_aws_json_1_1(
            value["user_rules"]
        )
    return out


def deserialize_aws_json_1_1(data: dict) -> WorkspacesIpGroup:
    out: WorkspacesIpGroup = {}  # type: ignore[typeddict-item]
    if data.get("groupId") is not None:
        out["group_id"] = data["groupId"]
    if data.get("groupName") is not None:
        out["group_name"] = data["groupName"]
    if data.get("groupDesc") is not None:
        out["group_desc"] = data["groupDesc"]
    if data.get("userRules") is not None:
        import capo_workspaces.types.ip_rule_list

        out["user_rules"] = capo_workspaces.types.ip_rule_list.deserialize_aws_json_1_1(
            data["userRules"]
        )
    return out


# --- rpcv2Cbor ser/de ---
def serialize_cbor(value: WorkspacesIpGroup) -> dict:
    out: dict = {}
    if "group_id" in value:
        out["groupId"] = value["group_id"]
    if "group_name" in value:
        out["groupName"] = value["group_name"]
    if "group_desc" in value:
        out["groupDesc"] = value["group_desc"]
    if "user_rules" in value:
        import capo_workspaces.types.ip_rule_list

        out["userRules"] = capo_workspaces.types.ip_rule_list.serialize_cbor(
            value["user_rules"]
        )
    return out


def deserialize_cbor(data: dict) -> WorkspacesIpGroup:
    out: WorkspacesIpGroup = {}  # type: ignore[typeddict-item]
    if data.get("groupId") is not None:
        out["group_id"] = data["groupId"]
    if data.get("groupName") is not None:
        out["group_name"] = data["groupName"]
    if data.get("groupDesc") is not None:
        out["group_desc"] = data["groupDesc"]
    if data.get("userRules") is not None:
        import capo_workspaces.types.ip_rule_list

        out["user_rules"] = capo_workspaces.types.ip_rule_list.deserialize_cbor(
            data["userRules"]
        )
    return out
