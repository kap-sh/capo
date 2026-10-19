"""Generated from Smithy shape ``com.amazonaws.mturk#UpdateHITTypeOfHITRequest``."""

from typing import TYPE_CHECKING

from typing_extensions import TypedDict

if TYPE_CHECKING:
    import capo_mturk.types.entity_id


class UpdateHITTypeOfHITRequest(TypedDict, closed=True):
    hit_id: "capo_mturk.types.entity_id.EntityId"
    """<p>The HIT to update.</p>"""
    hit_type_id: "capo_mturk.types.entity_id.EntityId"
    """<p>The ID of the new HIT type.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: UpdateHITTypeOfHITRequest) -> dict:
    out: dict = {}
    out["HITId"] = value["hit_id"]
    out["HITTypeId"] = value["hit_type_id"]
    return out


def deserialize_aws_json_1_1(data: dict) -> UpdateHITTypeOfHITRequest:
    out: UpdateHITTypeOfHITRequest = {}  # type: ignore[typeddict-item]
    if data.get("HITId") is not None:
        out["hit_id"] = data["HITId"]
    else:
        out["hit_id"] = ""
    if data.get("HITTypeId") is not None:
        out["hit_type_id"] = data["HITTypeId"]
    else:
        out["hit_type_id"] = ""
    return out
