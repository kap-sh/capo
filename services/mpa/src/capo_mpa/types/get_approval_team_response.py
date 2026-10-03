"""Generated from Smithy shape ``com.amazonaws.mpa#GetApprovalTeamResponse``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_mpa.types.approval_strategy_response
    import capo_mpa.types.approval_team_status
    import capo_mpa.types.approval_team_status_code
    import capo_mpa.types.description
    import capo_mpa.types.get_approval_team_response_approvers
    import capo_mpa.types.iso_timestamp
    import capo_mpa.types.message
    import capo_mpa.types.pending_update
    import capo_mpa.types.policies_references
    import capo_mpa.types.string


class GetApprovalTeamResponse(TypedDict, closed=True):
    creation_time: NotRequired["capo_mpa.types.iso_timestamp.IsoTimestamp"]
    """<p>Timestamp when the team was created.</p>"""
    approval_strategy: NotRequired[
        "capo_mpa.types.approval_strategy_response.ApprovalStrategyResponse"
    ]
    """<p>An <code>ApprovalStrategyResponse</code> object. Contains details for how the team grants approval.</p>"""
    number_of_approvers: NotRequired["int"]
    """<p>Total number of approvers in the team.</p>"""
    approvers: NotRequired[
        "capo_mpa.types.get_approval_team_response_approvers.GetApprovalTeamResponseApprovers"
    ]
    """<p>An array of <code>GetApprovalTeamResponseApprover </code> objects. Contains details for the approvers in the team.</p>"""
    arn: NotRequired["capo_mpa.types.string.String"]
    """<p>Amazon Resource Name (ARN) for the team.</p>"""
    description: NotRequired["capo_mpa.types.description.Description"]
    """<p>Description for the team.</p>"""
    name: NotRequired["capo_mpa.types.string.String"]
    """<p>Name of the approval team.</p>"""
    status: NotRequired["capo_mpa.types.approval_team_status.ApprovalTeamStatus"]
    """<p>Status for the team. For more information, see <a href="https://docs.aws.amazon.com/mpa/latest/userguide/mpa-health.html">Team health</a> in the <i>Multi-party approval User Guide</i>.</p>"""
    status_code: NotRequired[
        "capo_mpa.types.approval_team_status_code.ApprovalTeamStatusCode"
    ]
    """<p>Status code for the approval team. For more information, see <a href="https://docs.aws.amazon.com/mpa/latest/userguide/mpa-health.html">Team health</a> in the <i>Multi-party approval User Guide</i>.</p>"""
    status_message: NotRequired["capo_mpa.types.message.Message"]
    """<p>Message describing the status for the team.</p>"""
    update_session_arn: NotRequired["capo_mpa.types.string.String"]
    """<p>Amazon Resource Name (ARN) for the session.</p>"""
    version_id: NotRequired["capo_mpa.types.string.String"]
    """<p>Version ID for the team.</p>"""
    policies: NotRequired["capo_mpa.types.policies_references.PoliciesReferences"]
    """<p>An array of <code>PolicyReference</code> objects. Contains a list of policies that define the permissions for team resources.</p>"""
    last_update_time: NotRequired["capo_mpa.types.iso_timestamp.IsoTimestamp"]
    """<p>Timestamp when the team was last updated.</p>"""
    pending_update: NotRequired["capo_mpa.types.pending_update.PendingUpdate"]
    """<p>A <code>PendingUpdate</code> object. Contains details for the pending updates for the team, if applicable.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: GetApprovalTeamResponse) -> dict:
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
    if "approvers" in value:
        import capo_mpa.types.get_approval_team_response_approvers

        out["Approvers"] = (
            capo_mpa.types.get_approval_team_response_approvers.serialize_json(
                value["approvers"]
            )
        )
    if "arn" in value:
        out["Arn"] = value["arn"]
    if "description" in value:
        out["Description"] = value["description"]
    if "name" in value:
        out["Name"] = value["name"]
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
    if "update_session_arn" in value:
        out["UpdateSessionArn"] = value["update_session_arn"]
    if "version_id" in value:
        out["VersionId"] = value["version_id"]
    if "policies" in value:
        import capo_mpa.types.policies_references

        out["Policies"] = capo_mpa.types.policies_references.serialize_json(
            value["policies"]
        )
    if "last_update_time" in value:
        import capo_mpa.types.iso_timestamp

        out["LastUpdateTime"] = capo_mpa.types.iso_timestamp.serialize_json(
            value["last_update_time"]
        )
    if "pending_update" in value:
        import capo_mpa.types.pending_update

        out["PendingUpdate"] = capo_mpa.types.pending_update.serialize_json(
            value["pending_update"]
        )
    return out


def deserialize_json(data: dict) -> GetApprovalTeamResponse:
    out: GetApprovalTeamResponse = {}  # type: ignore[typeddict-item]
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
    if data.get("Approvers") is not None:
        import capo_mpa.types.get_approval_team_response_approvers

        out["approvers"] = (
            capo_mpa.types.get_approval_team_response_approvers.deserialize_json(
                data["Approvers"]
            )
        )
    if data.get("Arn") is not None:
        out["arn"] = data["Arn"]
    if data.get("Description") is not None:
        out["description"] = data["Description"]
    if data.get("Name") is not None:
        out["name"] = data["Name"]
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
    if data.get("UpdateSessionArn") is not None:
        out["update_session_arn"] = data["UpdateSessionArn"]
    if data.get("VersionId") is not None:
        out["version_id"] = data["VersionId"]
    if data.get("Policies") is not None:
        import capo_mpa.types.policies_references

        out["policies"] = capo_mpa.types.policies_references.deserialize_json(
            data["Policies"]
        )
    if data.get("LastUpdateTime") is not None:
        import capo_mpa.types.iso_timestamp

        out["last_update_time"] = capo_mpa.types.iso_timestamp.deserialize_json(
            data["LastUpdateTime"]
        )
    if data.get("PendingUpdate") is not None:
        import capo_mpa.types.pending_update

        out["pending_update"] = capo_mpa.types.pending_update.deserialize_json(
            data["PendingUpdate"]
        )
    return out
