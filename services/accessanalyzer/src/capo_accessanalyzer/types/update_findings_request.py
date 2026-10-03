"""Generated from Smithy shape ``com.amazonaws.accessanalyzer#UpdateFindingsRequest``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

from capo_accessanalyzer.errors import DeserializationError

if TYPE_CHECKING:
    import capo_accessanalyzer.types.analyzer_arn
    import capo_accessanalyzer.types.finding_id_list
    import capo_accessanalyzer.types.finding_status_update
    import capo_accessanalyzer.types.resource_arn


class UpdateFindingsRequest(TypedDict, closed=True):
    analyzer_arn: "capo_accessanalyzer.types.analyzer_arn.AnalyzerArn"
    """<p>The <a href="https://docs.aws.amazon.com/IAM/latest/UserGuide/access-analyzer-getting-started.html#permission-resources">ARN of the analyzer</a> that generated the findings to update.</p>"""
    status: "capo_accessanalyzer.types.finding_status_update.FindingStatusUpdate"
    """<p>The state represents the action to take to update the finding Status. Use <code>ARCHIVE</code> to change an Active finding to an Archived finding. Use <code>ACTIVE</code> to change an Archived finding to an Active finding.</p>"""
    ids: NotRequired["capo_accessanalyzer.types.finding_id_list.FindingIdList"]
    """<p>The IDs of the findings to update.</p>"""
    resource_arn: NotRequired["capo_accessanalyzer.types.resource_arn.ResourceArn"]
    """<p>The ARN of the resource identified in the finding.</p>"""
    client_token: NotRequired["str"]
    """<p>A client token.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: UpdateFindingsRequest) -> dict:
    out: dict = {}
    out["analyzerArn"] = value["analyzer_arn"]
    out["status"] = value["status"]
    if "ids" in value:
        import capo_accessanalyzer.types.finding_id_list

        out["ids"] = capo_accessanalyzer.types.finding_id_list.serialize_json(
            value["ids"]
        )
    if "resource_arn" in value:
        out["resourceArn"] = value["resource_arn"]
    if "client_token" in value:
        out["clientToken"] = value["client_token"]
    return out


def deserialize_json(data: dict) -> UpdateFindingsRequest:
    out: UpdateFindingsRequest = {}  # type: ignore[typeddict-item]
    if data.get("analyzerArn") is not None:
        out["analyzer_arn"] = data["analyzerArn"]
    else:
        raise DeserializationError("UpdateFindingsRequest.analyzer_arn required")
    if data.get("status") is not None:
        out["status"] = data["status"]
    else:
        raise DeserializationError("UpdateFindingsRequest.status required")
    if data.get("ids") is not None:
        import capo_accessanalyzer.types.finding_id_list

        out["ids"] = capo_accessanalyzer.types.finding_id_list.deserialize_json(
            data["ids"]
        )
    if data.get("resourceArn") is not None:
        out["resource_arn"] = data["resourceArn"]
    if data.get("clientToken") is not None:
        out["client_token"] = data["clientToken"]
    return out
