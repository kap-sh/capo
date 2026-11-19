"""Generated from Smithy shape ``com.amazonaws.guardduty#InvestigationSummary``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_guardduty.types.confidence
    import capo_guardduty.types.finding_id
    import capo_guardduty.types.investigation_id
    import capo_guardduty.types.investigation_status
    import capo_guardduty.types.investigation_title
    import capo_guardduty.types.investigation_type
    import capo_guardduty.types.risk_level
    import capo_guardduty.types.string
    import capo_guardduty.types.timestamp
    import capo_guardduty.types.trigger_prompt


class InvestigationSummary(TypedDict, closed=True):
    investigation_id: NotRequired[
        "capo_guardduty.types.investigation_id.InvestigationId"
    ]
    """<p>The unique identifier of the investigation.</p>"""
    status: NotRequired["capo_guardduty.types.investigation_status.InvestigationStatus"]
    """<p>The current status of the investigation.</p>"""
    trigger_prompt: NotRequired["capo_guardduty.types.trigger_prompt.TriggerPrompt"]
    """<p>The natural-language prompt that initiated this investigation.</p>"""
    risk_level: NotRequired["capo_guardduty.types.risk_level.RiskLevel"]
    """<p>The assessed risk level of the investigated threat.</p>"""
    confidence: NotRequired["capo_guardduty.types.confidence.Confidence"]
    """<p>The confidence level of the investigation's assessment.</p>"""
    title: NotRequired["capo_guardduty.types.investigation_title.InvestigationTitle"]
    """<p>A short title summarizing the investigation.</p>"""
    investigation_type: NotRequired[
        "capo_guardduty.types.investigation_type.InvestigationType"
    ]
    """<p>The type of investigation. Possible values are <code>FINDING</code>, <code>ACCOUNT</code>, and <code>ORGANIZATION</code>. GuardDuty sets this field when the investigation completes.</p>"""
    finding_id: NotRequired["capo_guardduty.types.finding_id.FindingId"]
    """<p>For a <code>FINDING</code> investigation, the ID of the finding that the investigation analyzed. GuardDuty sets this field when the investigation completes.</p>"""
    account_id: NotRequired["capo_guardduty.types.string.String"]
    """<p>The Amazon Web Services account ID associated with the investigation.</p>"""
    admin_account_id: NotRequired["capo_guardduty.types.string.String"]
    """<p>For an <code>ORGANIZATION</code> investigation, the ID of the administrator account of the organization that the investigation analyzed. GuardDuty sets this field when the investigation completes.</p>"""
    start_time: NotRequired["capo_guardduty.types.timestamp.Timestamp"]
    """<p>The timestamp at which the investigation started.</p>"""
    end_time: NotRequired["capo_guardduty.types.timestamp.Timestamp"]
    """<p>The timestamp at which the investigation completed.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: InvestigationSummary) -> dict:
    out: dict = {}
    if "investigation_id" in value:
        out["investigationId"] = value["investigation_id"]
    if "status" in value:
        import capo_guardduty.types.investigation_status

        out["status"] = capo_guardduty.types.investigation_status.serialize_json(
            value["status"]
        )
    if "trigger_prompt" in value:
        out["triggerPrompt"] = value["trigger_prompt"]
    if "risk_level" in value:
        import capo_guardduty.types.risk_level

        out["riskLevel"] = capo_guardduty.types.risk_level.serialize_json(
            value["risk_level"]
        )
    if "confidence" in value:
        import capo_guardduty.types.confidence

        out["confidence"] = capo_guardduty.types.confidence.serialize_json(
            value["confidence"]
        )
    if "title" in value:
        out["title"] = value["title"]
    if "investigation_type" in value:
        import capo_guardduty.types.investigation_type

        out["investigationType"] = (
            capo_guardduty.types.investigation_type.serialize_json(
                value["investigation_type"]
            )
        )
    if "finding_id" in value:
        out["findingId"] = value["finding_id"]
    if "account_id" in value:
        out["accountId"] = value["account_id"]
    if "admin_account_id" in value:
        out["adminAccountId"] = value["admin_account_id"]
    if "start_time" in value:
        import capo_guardduty.types.timestamp

        out["startTime"] = capo_guardduty.types.timestamp.serialize_json(
            value["start_time"]
        )
    if "end_time" in value:
        import capo_guardduty.types.timestamp

        out["endTime"] = capo_guardduty.types.timestamp.serialize_json(
            value["end_time"]
        )
    return out


def deserialize_json(data: dict) -> InvestigationSummary:
    out: InvestigationSummary = {}  # type: ignore[typeddict-item]
    if data.get("investigationId") is not None:
        out["investigation_id"] = data["investigationId"]
    if data.get("status") is not None:
        import capo_guardduty.types.investigation_status

        out["status"] = capo_guardduty.types.investigation_status.deserialize_json(
            data["status"]
        )
    if data.get("triggerPrompt") is not None:
        out["trigger_prompt"] = data["triggerPrompt"]
    if data.get("riskLevel") is not None:
        import capo_guardduty.types.risk_level

        out["risk_level"] = capo_guardduty.types.risk_level.deserialize_json(
            data["riskLevel"]
        )
    if data.get("confidence") is not None:
        import capo_guardduty.types.confidence

        out["confidence"] = capo_guardduty.types.confidence.deserialize_json(
            data["confidence"]
        )
    if data.get("title") is not None:
        out["title"] = data["title"]
    if data.get("investigationType") is not None:
        import capo_guardduty.types.investigation_type

        out["investigation_type"] = (
            capo_guardduty.types.investigation_type.deserialize_json(
                data["investigationType"]
            )
        )
    if data.get("findingId") is not None:
        out["finding_id"] = data["findingId"]
    if data.get("accountId") is not None:
        out["account_id"] = data["accountId"]
    if data.get("adminAccountId") is not None:
        out["admin_account_id"] = data["adminAccountId"]
    if data.get("startTime") is not None:
        import capo_guardduty.types.timestamp

        out["start_time"] = capo_guardduty.types.timestamp.deserialize_json(
            data["startTime"]
        )
    if data.get("endTime") is not None:
        import capo_guardduty.types.timestamp

        out["end_time"] = capo_guardduty.types.timestamp.deserialize_json(
            data["endTime"]
        )
    return out
