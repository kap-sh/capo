"""Generated from Smithy shape ``com.amazonaws.mturk#DeleteHITRequest``."""

from typing import TYPE_CHECKING

from typing_extensions import TypedDict

if TYPE_CHECKING:
    import capo_mturk.types.entity_id


class DeleteHITRequest(TypedDict, closed=True):
    hit_id: "capo_mturk.types.entity_id.EntityId"
    """<p>The ID of the HIT to be deleted.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: DeleteHITRequest) -> dict:
    out: dict = {}
    out["HITId"] = value["hit_id"]
    return out


def deserialize_aws_json_1_1(data: dict) -> DeleteHITRequest:
    out: DeleteHITRequest = {}  # type: ignore[typeddict-item]
    if data.get("HITId") is not None:
        out["hit_id"] = data["HITId"]
    else:
        out["hit_id"] = ""
    return out
