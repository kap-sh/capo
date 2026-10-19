"""Generated from Smithy shape ``com.amazonaws.mturk#RejectQualificationRequestRequest``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_mturk.types.string


class RejectQualificationRequestRequest(TypedDict, closed=True):
    qualification_request_id: "capo_mturk.types.string.String"
    """<p> The ID of the Qualification request, as returned by the <code>ListQualificationRequests</code> operation. </p>"""
    reason: NotRequired["capo_mturk.types.string.String"]
    """<p>A text message explaining why the request was rejected, to be shown to the Worker who made the request.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: RejectQualificationRequestRequest) -> dict:
    out: dict = {}
    out["QualificationRequestId"] = value["qualification_request_id"]
    if "reason" in value:
        out["Reason"] = value["reason"]
    return out


def deserialize_aws_json_1_1(data: dict) -> RejectQualificationRequestRequest:
    out: RejectQualificationRequestRequest = {}  # type: ignore[typeddict-item]
    if data.get("QualificationRequestId") is not None:
        out["qualification_request_id"] = data["QualificationRequestId"]
    else:
        out["qualification_request_id"] = ""
    if data.get("Reason") is not None:
        out["reason"] = data["Reason"]
    return out
