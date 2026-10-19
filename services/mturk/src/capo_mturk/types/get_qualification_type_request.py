"""Generated from Smithy shape ``com.amazonaws.mturk#GetQualificationTypeRequest``."""

from typing import TYPE_CHECKING

from typing_extensions import TypedDict

if TYPE_CHECKING:
    import capo_mturk.types.entity_id


class GetQualificationTypeRequest(TypedDict, closed=True):
    qualification_type_id: "capo_mturk.types.entity_id.EntityId"
    """<p>The ID of the QualificationType.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: GetQualificationTypeRequest) -> dict:
    out: dict = {}
    out["QualificationTypeId"] = value["qualification_type_id"]
    return out


def deserialize_aws_json_1_1(data: dict) -> GetQualificationTypeRequest:
    out: GetQualificationTypeRequest = {}  # type: ignore[typeddict-item]
    if data.get("QualificationTypeId") is not None:
        out["qualification_type_id"] = data["QualificationTypeId"]
    else:
        out["qualification_type_id"] = ""
    return out
