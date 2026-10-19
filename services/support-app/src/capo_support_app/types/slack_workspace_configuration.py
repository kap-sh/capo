"""Generated from Smithy shape ``com.amazonaws.supportapp#SlackWorkspaceConfiguration``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_support_app.types.boolean_value
    import capo_support_app.types.team_id
    import capo_support_app.types.team_name


class SlackWorkspaceConfiguration(TypedDict, closed=True):
    team_id: "capo_support_app.types.team_id.teamId"
    """<p>The team ID in Slack. This ID uniquely identifies a Slack workspace, such as <code>T012ABCDEFG</code>.</p>"""
    team_name: NotRequired["capo_support_app.types.team_name.teamName"]
    """<p>The name of the Slack workspace.</p>"""
    allow_organization_member_account: NotRequired[
        "capo_support_app.types.boolean_value.booleanValue"
    ]
    """<p>Whether to allow member accounts to authorize Slack workspaces. Member accounts must be part of an organization in Organizations.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: SlackWorkspaceConfiguration) -> dict:
    out: dict = {}
    out["teamId"] = value["team_id"]
    if "team_name" in value:
        out["teamName"] = value["team_name"]
    if "allow_organization_member_account" in value:
        out["allowOrganizationMemberAccount"] = value[
            "allow_organization_member_account"
        ]
    return out


def deserialize_json(data: dict) -> SlackWorkspaceConfiguration:
    out: SlackWorkspaceConfiguration = {}  # type: ignore[typeddict-item]
    if data.get("teamId") is not None:
        out["team_id"] = data["teamId"]
    else:
        out["team_id"] = ""
    if data.get("teamName") is not None:
        out["team_name"] = data["teamName"]
    if data.get("allowOrganizationMemberAccount") is not None:
        out["allow_organization_member_account"] = data[
            "allowOrganizationMemberAccount"
        ]
    return out
