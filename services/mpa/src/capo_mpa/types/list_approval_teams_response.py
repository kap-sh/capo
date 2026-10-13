"""Generated from Smithy shape ``com.amazonaws.mpa#ListApprovalTeamsResponse``."""

from typing import TYPE_CHECKING, Any

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_mpa.types.list_approval_teams_response_approval_teams
    import capo_mpa.types.token


class ListApprovalTeamsResponse(TypedDict, closed=True):
    next_token: NotRequired["capo_mpa.types.token.Token"]
    """<p>If present, indicates that more output is available than is included in the current response. Use this value in the <code>NextToken</code> request parameter in a next call to the operation to get more output. You can repeat this until the <code>NextToken</code> response element returns <code>null</code>.</p>"""
    approval_teams: NotRequired[
        "capo_mpa.types.list_approval_teams_response_approval_teams.ListApprovalTeamsResponseApprovalTeams"
    ]
    """<p>An array of <code>ListApprovalTeamsResponseApprovalTeam</code> objects. Contains details for approval teams.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: ListApprovalTeamsResponse) -> dict:
    out: dict = {}
    if "next_token" in value:
        out["NextToken"] = value["next_token"]
    if "approval_teams" in value:
        import capo_mpa.types.list_approval_teams_response_approval_teams

        out["ApprovalTeams"] = (
            capo_mpa.types.list_approval_teams_response_approval_teams.serialize_json(
                value["approval_teams"]
            )
        )
    return out


def deserialize_json(data: dict) -> ListApprovalTeamsResponse:
    out: ListApprovalTeamsResponse = {}  # type: ignore[typeddict-item]
    if data.get("NextToken") is not None:
        out["next_token"] = data["NextToken"]
    if data.get("ApprovalTeams") is not None:
        import capo_mpa.types.list_approval_teams_response_approval_teams

        out["approval_teams"] = (
            capo_mpa.types.list_approval_teams_response_approval_teams.deserialize_json(
                data["ApprovalTeams"]
            )
        )
    return out


def redact_sensitive(value: ListApprovalTeamsResponse) -> dict[str, Any]:
    out: dict[str, Any] = dict(value)
    if "approval_teams" in value:
        import capo_mpa.types.list_approval_teams_response_approval_teams

        out["approval_teams"] = (
            capo_mpa.types.list_approval_teams_response_approval_teams.redact_sensitive(
                value["approval_teams"]
            )
        )
    return out
