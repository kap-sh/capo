"""Generated from Smithy shape ``com.amazonaws.partnercentralselling#EngagementProspectingResult``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_partnercentral_selling.types.engagement_identifier
    import capo_partnercentral_selling.types.prospecting_task_status


class EngagementProspectingResult(TypedDict, closed=True):
    engagement_identifier: (
        "capo_partnercentral_selling.types.engagement_identifier.EngagementIdentifier"
    )
    """<p>The unique identifier of the engagement that was processed.</p>"""
    engagement_context_id: NotRequired["str"]
    """<p>The identifier of the prospecting context created for this engagement. This field is only populated when the engagement was processed successfully (status is <code>COMPLETED</code>). Use this identifier to reference the prospecting context in subsequent operations.</p>"""
    status: "capo_partnercentral_selling.types.prospecting_task_status.ProspectingTaskStatus"
    """<p>The processing status of this specific engagement. Possible values are <code>PENDING</code>, <code>IN_PROGRESS</code>, <code>COMPLETED</code>, and <code>FAILED</code>.</p>"""
    reason_code: NotRequired["str"]
    """<p>An enumerated code indicating the reason this engagement failed to process. This field is only populated when <code>Status</code> is <code>FAILED</code>.</p>"""
    message: NotRequired["str"]
    """<p>A human-readable description of the failure for this engagement, including suggested recovery steps. This field is only populated when <code>Status</code> is <code>FAILED</code>.</p>"""


# --- awsJson1_0 ser/de ---
def serialize_aws_json_1_0(value: EngagementProspectingResult) -> dict:
    out: dict = {}
    out["EngagementIdentifier"] = value["engagement_identifier"]
    if "engagement_context_id" in value:
        out["EngagementContextId"] = value["engagement_context_id"]
    import capo_partnercentral_selling.types.prospecting_task_status

    out["Status"] = (
        capo_partnercentral_selling.types.prospecting_task_status.serialize_aws_json_1_0(
            value["status"]
        )
    )
    if "reason_code" in value:
        out["ReasonCode"] = value["reason_code"]
    if "message" in value:
        out["Message"] = value["message"]
    return out


def deserialize_aws_json_1_0(data: dict) -> EngagementProspectingResult:
    out: EngagementProspectingResult = {}  # type: ignore[typeddict-item]
    if data.get("EngagementIdentifier") is not None:
        out["engagement_identifier"] = data["EngagementIdentifier"]
    else:
        out["engagement_identifier"] = ""
    if data.get("EngagementContextId") is not None:
        out["engagement_context_id"] = data["EngagementContextId"]
    if data.get("Status") is not None:
        import capo_partnercentral_selling.types.prospecting_task_status

        out["status"] = (
            capo_partnercentral_selling.types.prospecting_task_status.deserialize_aws_json_1_0(
                data["Status"]
            )
        )
    else:
        import typing

        out["status"] = typing.cast(
            "capo_partnercentral_selling.types.prospecting_task_status.ProspectingTaskStatus",
            "",
        )
    if data.get("ReasonCode") is not None:
        out["reason_code"] = data["ReasonCode"]
    if data.get("Message") is not None:
        out["message"] = data["Message"]
    return out
