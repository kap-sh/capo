"""Generated from Smithy shape ``com.amazonaws.quicksight#StartAutomationJobResponse``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_quicksight.types.arn
    import capo_quicksight.types.automate_id
    import capo_quicksight.types.status_code


class StartAutomationJobResponse(TypedDict, closed=True):
    arn: "capo_quicksight.types.arn.Arn"
    """<p>The Amazon Resource Name (ARN) of the automation job.</p>"""
    job_id: "capo_quicksight.types.automate_id.AutomateId"
    """<p>The ID of the automation job that was started.</p>"""
    status: "capo_quicksight.types.status_code.StatusCode"
    """<p>The HTTP status of the request.</p>"""
    request_id: NotRequired["str"]
    """<p>The Amazon Web Services request ID for this operation.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: StartAutomationJobResponse) -> dict:
    out: dict = {}
    out["Arn"] = value["arn"]
    out["JobId"] = value["job_id"]
    if "request_id" in value:
        out["RequestId"] = value["request_id"]
    return out


def deserialize_json(data: dict) -> StartAutomationJobResponse:
    out: StartAutomationJobResponse = {}  # type: ignore[typeddict-item]
    if data.get("Arn") is not None:
        out["arn"] = data["Arn"]
    else:
        out["arn"] = ""
    if data.get("JobId") is not None:
        out["job_id"] = data["JobId"]
    else:
        out["job_id"] = ""
    if data.get("RequestId") is not None:
        out["request_id"] = data["RequestId"]
    return out
