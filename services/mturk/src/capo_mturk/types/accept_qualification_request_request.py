"""Generated from Smithy shape ``com.amazonaws.mturk#AcceptQualificationRequestRequest``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_mturk.types.integer
    import capo_mturk.types.string


class AcceptQualificationRequestRequest(TypedDict, closed=True):
    qualification_request_id: "capo_mturk.types.string.String"
    """<p>The ID of the Qualification request, as returned by the <code>GetQualificationRequests</code> operation.</p>"""
    integer_value: NotRequired["capo_mturk.types.integer.Integer"]
    """<p> The value of the Qualification. You can omit this value if you are using the presence or absence of the Qualification as the basis for a HIT requirement. </p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: AcceptQualificationRequestRequest) -> dict:
    out: dict = {}
    out["QualificationRequestId"] = value["qualification_request_id"]
    if "integer_value" in value:
        out["IntegerValue"] = value["integer_value"]
    return out


def deserialize_aws_json_1_1(data: dict) -> AcceptQualificationRequestRequest:
    out: AcceptQualificationRequestRequest = {}  # type: ignore[typeddict-item]
    if data.get("QualificationRequestId") is not None:
        out["qualification_request_id"] = data["QualificationRequestId"]
    else:
        out["qualification_request_id"] = ""
    if data.get("IntegerValue") is not None:
        out["integer_value"] = data["IntegerValue"]
    return out
