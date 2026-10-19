"""Generated from Smithy shape ``com.amazonaws.workspaces#CreateIpGroupRequest``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_workspaces.types.ip_group_desc
    import capo_workspaces.types.ip_group_name
    import capo_workspaces.types.ip_rule_list
    import capo_workspaces.types.tag_list


class CreateIpGroupRequest(TypedDict, closed=True):
    group_name: "capo_workspaces.types.ip_group_name.IpGroupName"
    """<p>The name of the group.</p>"""
    group_desc: NotRequired["capo_workspaces.types.ip_group_desc.IpGroupDesc"]
    """<p>The description of the group.</p>"""
    user_rules: NotRequired["capo_workspaces.types.ip_rule_list.IpRuleList"]
    """<p>The rules to add to the group.</p>"""
    tags: NotRequired["capo_workspaces.types.tag_list.TagList"]
    """<p>The tags. Each WorkSpaces resource can have a maximum of 50 tags.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: CreateIpGroupRequest) -> dict:
    out: dict = {}
    out["GroupName"] = value["group_name"]
    if "group_desc" in value:
        out["GroupDesc"] = value["group_desc"]
    if "user_rules" in value:
        import capo_workspaces.types.ip_rule_list

        out["UserRules"] = capo_workspaces.types.ip_rule_list.serialize_aws_json_1_1(
            value["user_rules"]
        )
    if "tags" in value:
        import capo_workspaces.types.tag_list

        out["Tags"] = capo_workspaces.types.tag_list.serialize_aws_json_1_1(
            value["tags"]
        )
    return out


def deserialize_aws_json_1_1(data: dict) -> CreateIpGroupRequest:
    out: CreateIpGroupRequest = {}  # type: ignore[typeddict-item]
    if data.get("GroupName") is not None:
        out["group_name"] = data["GroupName"]
    else:
        out["group_name"] = ""
    if data.get("GroupDesc") is not None:
        out["group_desc"] = data["GroupDesc"]
    if data.get("UserRules") is not None:
        import capo_workspaces.types.ip_rule_list

        out["user_rules"] = capo_workspaces.types.ip_rule_list.deserialize_aws_json_1_1(
            data["UserRules"]
        )
    if data.get("Tags") is not None:
        import capo_workspaces.types.tag_list

        out["tags"] = capo_workspaces.types.tag_list.deserialize_aws_json_1_1(
            data["Tags"]
        )
    return out
