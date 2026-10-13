"""Generated from Smithy shape ``com.amazonaws.mpa#ListApprovalTeamsResponseApprovalTeams``."""

from typing import TYPE_CHECKING, Any, TypeAlias

if TYPE_CHECKING:
    import capo_mpa.types.list_approval_teams_response_approval_team

ListApprovalTeamsResponseApprovalTeams: TypeAlias = list[
    "capo_mpa.types.list_approval_teams_response_approval_team.ListApprovalTeamsResponseApprovalTeam"
]


# --- restJson1 ser/de ---
def serialize_json(value: ListApprovalTeamsResponseApprovalTeams) -> list:
    import capo_mpa.types.list_approval_teams_response_approval_team

    out: list = []
    for item in value:
        out.append(
            capo_mpa.types.list_approval_teams_response_approval_team.serialize_json(
                item
            )
        )
    return out


def deserialize_json(data: list) -> ListApprovalTeamsResponseApprovalTeams:
    import capo_mpa.types.list_approval_teams_response_approval_team

    out: ListApprovalTeamsResponseApprovalTeams = []
    for item in data:
        if item is None:
            continue
        out.append(
            capo_mpa.types.list_approval_teams_response_approval_team.deserialize_json(
                item
            )
        )
    return out


def redact_sensitive(value: ListApprovalTeamsResponseApprovalTeams) -> list[Any]:
    import capo_mpa.types.list_approval_teams_response_approval_team

    return [
        capo_mpa.types.list_approval_teams_response_approval_team.redact_sensitive(item)
        for item in value
    ]
