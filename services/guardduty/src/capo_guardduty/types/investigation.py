"""Generated from Smithy shape ``com.amazonaws.guardduty#Investigation``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_guardduty.types.cloud_details
    import capo_guardduty.types.confidence
    import capo_guardduty.types.investigation_error_details
    import capo_guardduty.types.investigation_id
    import capo_guardduty.types.investigation_metadata
    import capo_guardduty.types.investigation_scope
    import capo_guardduty.types.investigation_status
    import capo_guardduty.types.investigation_summary_data
    import capo_guardduty.types.investigation_summary_text
    import capo_guardduty.types.risk_details
    import capo_guardduty.types.risk_level
    import capo_guardduty.types.timestamp
    import capo_guardduty.types.trigger_prompt
    import capo_guardduty.types.triggered_by


class Investigation(TypedDict, closed=True):
    investigation_id: NotRequired[
        "capo_guardduty.types.investigation_id.InvestigationId"
    ]
    """<p>The unique identifier of the investigation.</p>"""
    status: NotRequired["capo_guardduty.types.investigation_status.InvestigationStatus"]
    """<p>The current status of the investigation. Possible values are <code>RUNNING</code>, <code>COMPLETED</code>, and <code>FAILED</code>.</p>"""
    trigger_prompt: NotRequired["capo_guardduty.types.trigger_prompt.TriggerPrompt"]
    """<p>The natural-language prompt that initiated this investigation.</p>"""
    triggered_by: NotRequired["capo_guardduty.types.triggered_by.TriggeredBy"]
    """<p>The account that initiated the investigation.</p>"""
    metadata: NotRequired[
        "capo_guardduty.types.investigation_metadata.InvestigationMetadata"
    ]
    """<p>Metadata about the product and version that produced the investigation.</p>"""
    cloud: NotRequired["capo_guardduty.types.cloud_details.CloudDetails"]
    """<p>Details about the cloud environment in which the investigation was performed, including the provider, region, and account.</p>"""
    risk_level: NotRequired["capo_guardduty.types.risk_level.RiskLevel"]
    """<p>The assessed risk level of the investigated threat. Possible values are <code>Info</code>, <code>Low</code>, <code>Medium</code>, <code>High</code>, and <code>Critical</code>.</p>"""
    risk: NotRequired["capo_guardduty.types.risk_details.RiskDetails"]
    """<p>A human-readable description of the assessed risk.</p>"""
    confidence: NotRequired["capo_guardduty.types.confidence.Confidence"]
    """<p>The confidence level of the investigation's assessment. Possible values are <code>Unknown</code>, <code>Low</code>, <code>Medium</code>, and <code>High</code>.</p>"""
    summary: NotRequired[
        "capo_guardduty.types.investigation_summary_text.InvestigationSummaryText"
    ]
    """<p>A summary of the investigation results as text, up to 262,144 characters. Returned only when the investigation status is <code>COMPLETED</code>. When you set <code>SummaryFormat</code> to <code>STRUCTURED</code>, the summary is returned in <code>SummaryData</code> instead, unless it isn't available in a structured form, in which case it's returned in this field.</p>"""
    summary_data: NotRequired[
        "capo_guardduty.types.investigation_summary_data.InvestigationSummaryData"
    ]
    """<p>A structured summary of the investigation results. GuardDuty returns this field only when you set <code>SummaryFormat</code> to <code>STRUCTURED</code>, the investigation status is <code>COMPLETED</code>, and the summary is available in a structured form. When this field is returned, <code>Summary</code> isn't returned.</p>"""
    scope: NotRequired["capo_guardduty.types.investigation_scope.InvestigationScope"]
    """<p>Information about what the investigation analyzed, including the investigation type, the finding, account, or organization that was analyzed, and, for <code>ACCOUNT</code> and <code>ORGANIZATION</code> investigations, the time window over which the investigation queried data. Returned only when the investigation status is <code>COMPLETED</code>.</p>"""
    start_time: NotRequired["capo_guardduty.types.timestamp.Timestamp"]
    """<p>The timestamp at which the investigation started.</p>"""
    end_time: NotRequired["capo_guardduty.types.timestamp.Timestamp"]
    """<p>The timestamp at which the investigation completed.</p>"""
    error: NotRequired[
        "capo_guardduty.types.investigation_error_details.InvestigationErrorDetails"
    ]
    """<p>Details about the error if the investigation status is <code>FAILED</code>.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: Investigation) -> dict:
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
    if "triggered_by" in value:
        out["triggeredBy"] = value["triggered_by"]
    if "metadata" in value:
        import capo_guardduty.types.investigation_metadata

        out["metadata"] = capo_guardduty.types.investigation_metadata.serialize_json(
            value["metadata"]
        )
    if "cloud" in value:
        import capo_guardduty.types.cloud_details

        out["cloud"] = capo_guardduty.types.cloud_details.serialize_json(value["cloud"])
    if "risk_level" in value:
        import capo_guardduty.types.risk_level

        out["riskLevel"] = capo_guardduty.types.risk_level.serialize_json(
            value["risk_level"]
        )
    if "risk" in value:
        out["risk"] = value["risk"]
    if "confidence" in value:
        import capo_guardduty.types.confidence

        out["confidence"] = capo_guardduty.types.confidence.serialize_json(
            value["confidence"]
        )
    if "summary" in value:
        out["summary"] = value["summary"]
    if "summary_data" in value:
        import capo_guardduty.types.investigation_summary_data

        out["summaryData"] = (
            capo_guardduty.types.investigation_summary_data.serialize_json(
                value["summary_data"]
            )
        )
    if "scope" in value:
        import capo_guardduty.types.investigation_scope

        out["scope"] = capo_guardduty.types.investigation_scope.serialize_json(
            value["scope"]
        )
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
    if "error" in value:
        out["error"] = value["error"]
    return out


def deserialize_json(data: dict) -> Investigation:
    out: Investigation = {}  # type: ignore[typeddict-item]
    if data.get("investigationId") is not None:
        out["investigation_id"] = data["investigationId"]
    if data.get("status") is not None:
        import capo_guardduty.types.investigation_status

        out["status"] = capo_guardduty.types.investigation_status.deserialize_json(
            data["status"]
        )
    if data.get("triggerPrompt") is not None:
        out["trigger_prompt"] = data["triggerPrompt"]
    if data.get("triggeredBy") is not None:
        out["triggered_by"] = data["triggeredBy"]
    if data.get("metadata") is not None:
        import capo_guardduty.types.investigation_metadata

        out["metadata"] = capo_guardduty.types.investigation_metadata.deserialize_json(
            data["metadata"]
        )
    if data.get("cloud") is not None:
        import capo_guardduty.types.cloud_details

        out["cloud"] = capo_guardduty.types.cloud_details.deserialize_json(
            data["cloud"]
        )
    if data.get("riskLevel") is not None:
        import capo_guardduty.types.risk_level

        out["risk_level"] = capo_guardduty.types.risk_level.deserialize_json(
            data["riskLevel"]
        )
    if data.get("risk") is not None:
        out["risk"] = data["risk"]
    if data.get("confidence") is not None:
        import capo_guardduty.types.confidence

        out["confidence"] = capo_guardduty.types.confidence.deserialize_json(
            data["confidence"]
        )
    if data.get("summary") is not None:
        out["summary"] = data["summary"]
    if data.get("summaryData") is not None:
        import capo_guardduty.types.investigation_summary_data

        out["summary_data"] = (
            capo_guardduty.types.investigation_summary_data.deserialize_json(
                data["summaryData"]
            )
        )
    if data.get("scope") is not None:
        import capo_guardduty.types.investigation_scope

        out["scope"] = capo_guardduty.types.investigation_scope.deserialize_json(
            data["scope"]
        )
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
    if data.get("error") is not None:
        out["error"] = data["error"]
    return out
