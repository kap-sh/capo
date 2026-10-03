"""Generated from Smithy shape ``com.amazonaws.mpa#ListApprovalTeamsResponseApprovalTeam``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_mpa.types.approval_strategy_response
    import capo_mpa.types.approval_team_arn
    import capo_mpa.types.approval_team_name
    import capo_mpa.types.approval_team_status
    import capo_mpa.types.approval_team_status_code
    import capo_mpa.types.description
    import capo_mpa.types.iso_timestamp
    import capo_mpa.types.message


class ListApprovalTeamsResponseApprovalTeam(TypedDict, closed=True):
    creation_time: NotRequired["capo_mpa.types.iso_timestamp.IsoTimestamp"]
    """<p>Timestamp when the team was created.</p>"""
    approval_strategy: NotRequired[
        "capo_mpa.types.approval_strategy_response.ApprovalStrategyResponse"
    ]
    """<p>An <code>ApprovalStrategyResponse</code> object. Contains details for how an approval team grants approval.</p>"""
    number_of_approvers: NotRequired["int"]
    """<p>Total number of approvers in the team.</p>"""
    arn: NotRequired["capo_mpa.types.approval_team_arn.ApprovalTeamArn"]
    """<p>Amazon Resource Name (ARN) for the team.</p>"""
    name: NotRequired["capo_mpa.types.approval_team_name.ApprovalTeamName"]
    """<p>Name of the team.</p>"""
    description: NotRequired["capo_mpa.types.description.Description"]
    """<p>Description for the team.</p>"""
    status: NotRequired["capo_mpa.types.approval_team_status.ApprovalTeamStatus"]
    """<p>Status for the team. For more information, see <a href="https://docs.aws.amazon.com/mpa/latest/userguide/mpa-health.html">Team health</a> in the <i>Multi-party approval User Guide</i>.</p>"""
    status_code: NotRequired[
        "capo_mpa.types.approval_team_status_code.ApprovalTeamStatusCode"
    ]
    """<p>Status code for the team. For more information, see <a href="https://docs.aws.amazon.com/mpa/latest/userguide/mpa-health.html">Team health</a> in the <i>Multi-party approval User Guide</i>.</p>"""
    status_message: NotRequired["capo_mpa.types.message.Message"]
    """<p>Message describing the status for the team.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: ListApprovalTeamsResponseApprovalTeam) -> dict:
    out: dict = {}
    if "creation_time" in value:
        import capo_mpa.types.iso_timestamp

        out["CreationTime"] = capo_mpa.types.iso_timestamp.serialize_json(
            value["creation_time"]
        )
    if "approval_strategy" in value:
        import capo_mpa.types.approval_strategy_response

        out["ApprovalStrategy"] = (
            capo_mpa.types.approval_strategy_response.serialize_json(
                value["approval_strategy"]
            )
        )
    if "number_of_approvers" in value:
        out["NumberOfApprovers"] = value["number_of_approvers"]
    if "arn" in value:
        out["Arn"] = value["arn"]
    if "name" in value:
        out["Name"] = value["name"]
    if "description" in value:
        out["Description"] = value["description"]
    if "status" in value:
        import capo_mpa.types.approval_team_status

        out["Status"] = capo_mpa.types.approval_team_status.serialize_json(
            value["status"]
        )
    if "status_code" in value:
        import capo_mpa.types.approval_team_status_code

        out["StatusCode"] = capo_mpa.types.approval_team_status_code.serialize_json(
            value["status_code"]
        )
    if "status_message" in value:
        out["StatusMessage"] = value["status_message"]
    return out


def deserialize_json(data: dict) -> ListApprovalTeamsResponseApprovalTeam:
    out: ListApprovalTeamsResponseApprovalTeam = {}  # type: ignore[typeddict-item]
    if data.get("CreationTime") is not None:
        import capo_mpa.types.iso_timestamp

        out["creation_time"] = capo_mpa.types.iso_timestamp.deserialize_json(
            data["CreationTime"]
        )
    if data.get("ApprovalStrategy") is not None:
        import capo_mpa.types.approval_strategy_response

        out["approval_strategy"] = (
            capo_mpa.types.approval_strategy_response.deserialize_json(
                data["ApprovalStrategy"]
            )
        )
    if data.get("NumberOfApprovers") is not None:
        out["number_of_approvers"] = data["NumberOfApprovers"]
    if data.get("Arn") is not None:
        out["arn"] = data["Arn"]
    if data.get("Name") is not None:
        out["name"] = data["Name"]
    if data.get("Description") is not None:
        out["description"] = data["Description"]
    if data.get("Status") is not None:
        import capo_mpa.types.approval_team_status

        out["status"] = capo_mpa.types.approval_team_status.deserialize_json(
            data["Status"]
        )
    if data.get("StatusCode") is not None:
        import capo_mpa.types.approval_team_status_code

        out["status_code"] = capo_mpa.types.approval_team_status_code.deserialize_json(
            data["StatusCode"]
        )
    if data.get("StatusMessage") is not None:
        out["status_message"] = data["StatusMessage"]
    return out
