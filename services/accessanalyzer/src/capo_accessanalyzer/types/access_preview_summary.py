"""Generated from Smithy shape ``com.amazonaws.accessanalyzer#AccessPreviewSummary``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_accessanalyzer.types.access_preview_id
    import capo_accessanalyzer.types.access_preview_status
    import capo_accessanalyzer.types.access_preview_status_reason
    import capo_accessanalyzer.types.analyzer_arn
    import capo_accessanalyzer.types.timestamp


class AccessPreviewSummary(TypedDict, closed=True):
    id: "capo_accessanalyzer.types.access_preview_id.AccessPreviewId"
    """<p>The unique ID for the access preview.</p>"""
    analyzer_arn: "capo_accessanalyzer.types.analyzer_arn.AnalyzerArn"
    """<p>The ARN of the analyzer used to generate the access preview.</p>"""
    created_at: "capo_accessanalyzer.types.timestamp.Timestamp"
    """<p>The time at which the access preview was created.</p>"""
    status: "capo_accessanalyzer.types.access_preview_status.AccessPreviewStatus"
    """<p>The status of the access preview.</p> <ul> <li> <p> <code>Creating</code> - The access preview creation is in progress.</p> </li> <li> <p> <code>Completed</code> - The access preview is complete and previews the findings for external access to the resource.</p> </li> <li> <p> <code>Failed</code> - The access preview creation has failed.</p> </li> </ul>"""
    status_reason: NotRequired[
        "capo_accessanalyzer.types.access_preview_status_reason.AccessPreviewStatusReason"
    ]


# --- restJson1 ser/de ---
def serialize_json(value: AccessPreviewSummary) -> dict:
    out: dict = {}
    out["id"] = value["id"]
    out["analyzerArn"] = value["analyzer_arn"]
    import capo_accessanalyzer.types.timestamp

    out["createdAt"] = capo_accessanalyzer.types.timestamp.serialize_json(
        value["created_at"]
    )
    out["status"] = value["status"]
    if "status_reason" in value:
        import capo_accessanalyzer.types.access_preview_status_reason

        out["statusReason"] = (
            capo_accessanalyzer.types.access_preview_status_reason.serialize_json(
                value["status_reason"]
            )
        )
    return out


def deserialize_json(data: dict) -> AccessPreviewSummary:
    out: AccessPreviewSummary = {}  # type: ignore[typeddict-item]
    if data.get("id") is not None:
        out["id"] = data["id"]
    else:
        out["id"] = ""
    if data.get("analyzerArn") is not None:
        out["analyzer_arn"] = data["analyzerArn"]
    else:
        out["analyzer_arn"] = ""
    if data.get("createdAt") is not None:
        import capo_accessanalyzer.types.timestamp

        out["created_at"] = capo_accessanalyzer.types.timestamp.deserialize_json(
            data["createdAt"]
        )
    else:
        import datetime

        out["created_at"] = datetime.datetime.fromtimestamp(0, tz=datetime.timezone.utc)
    if data.get("status") is not None:
        out["status"] = data["status"]
    else:
        out["status"] = ""
    if data.get("statusReason") is not None:
        import capo_accessanalyzer.types.access_preview_status_reason

        out["status_reason"] = (
            capo_accessanalyzer.types.access_preview_status_reason.deserialize_json(
                data["statusReason"]
            )
        )
    return out
