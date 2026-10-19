"""Generated from Smithy shape ``com.amazonaws.ssmincidents#BatchGetIncidentFindingsError``."""

from typing import TYPE_CHECKING

from typing_extensions import TypedDict

if TYPE_CHECKING:
    import capo_ssm_incidents.types.finding_id


class BatchGetIncidentFindingsError(TypedDict, closed=True):
    finding_id: "capo_ssm_incidents.types.finding_id.FindingId"
    """<p>The ID of a specified finding for which an error was returned for a <code>BatchGetIncidentFindings</code> operation.</p>"""
    code: "str"
    """<p>The code associated with an error that was returned for a <code>BatchGetIncidentFindings</code> operation.</p>"""
    message: "str"
    """<p>The description for an error that was returned for a <code>BatchGetIncidentFindings</code> operation.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: BatchGetIncidentFindingsError) -> dict:
    out: dict = {}
    out["findingId"] = value["finding_id"]
    out["code"] = value["code"]
    out["message"] = value["message"]
    return out


def deserialize_json(data: dict) -> BatchGetIncidentFindingsError:
    out: BatchGetIncidentFindingsError = {}  # type: ignore[typeddict-item]
    if data.get("findingId") is not None:
        out["finding_id"] = data["findingId"]
    else:
        out["finding_id"] = ""
    if data.get("code") is not None:
        out["code"] = data["code"]
    else:
        out["code"] = ""
    if data.get("message") is not None:
        out["message"] = data["message"]
    else:
        out["message"] = ""
    return out
