"""Generated from Smithy shape ``com.amazonaws.glue#GetMLTransformRequest``."""

from typing import TYPE_CHECKING

from typing_extensions import TypedDict

if TYPE_CHECKING:
    import capo_glue.types.hash_string


class GetMLTransformRequest(TypedDict, closed=True):
    transform_id: "capo_glue.types.hash_string.HashString"
    """<p>The unique identifier of the transform, generated at the time that the transform was created.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: GetMLTransformRequest) -> dict:
    out: dict = {}
    out["TransformId"] = value["transform_id"]
    return out


def deserialize_aws_json_1_1(data: dict) -> GetMLTransformRequest:
    out: GetMLTransformRequest = {}  # type: ignore[typeddict-item]
    if data.get("TransformId") is not None:
        out["transform_id"] = data["TransformId"]
    else:
        out["transform_id"] = ""
    return out
