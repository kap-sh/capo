"""Generated from Smithy shape ``com.amazonaws.workspaces#RevokeIpRulesRequest``."""

from typing import TYPE_CHECKING

from typing_extensions import TypedDict

if TYPE_CHECKING:
    import capo_workspaces.types.ip_group_id
    import capo_workspaces.types.ip_revoked_rule_list


class RevokeIpRulesRequest(TypedDict, closed=True):
    group_id: "capo_workspaces.types.ip_group_id.IpGroupId"
    """<p>The identifier of the group.</p>"""
    user_rules: "capo_workspaces.types.ip_revoked_rule_list.IpRevokedRuleList"
    """<p>The rules to remove from the group.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: RevokeIpRulesRequest) -> dict:
    out: dict = {}
    out["GroupId"] = value["group_id"]
    import capo_workspaces.types.ip_revoked_rule_list

    out["UserRules"] = (
        capo_workspaces.types.ip_revoked_rule_list.serialize_aws_json_1_1(
            value["user_rules"]
        )
    )
    return out


def deserialize_aws_json_1_1(data: dict) -> RevokeIpRulesRequest:
    out: RevokeIpRulesRequest = {}  # type: ignore[typeddict-item]
    if data.get("GroupId") is not None:
        out["group_id"] = data["GroupId"]
    else:
        out["group_id"] = ""
    if data.get("UserRules") is not None:
        import capo_workspaces.types.ip_revoked_rule_list

        out["user_rules"] = (
            capo_workspaces.types.ip_revoked_rule_list.deserialize_aws_json_1_1(
                data["UserRules"]
            )
        )
    else:
        out["user_rules"] = []
    return out
