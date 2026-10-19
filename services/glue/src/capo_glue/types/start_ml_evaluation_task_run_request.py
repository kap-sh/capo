"""Generated from Smithy shape ``com.amazonaws.glue#StartMLEvaluationTaskRunRequest``."""

from typing import TYPE_CHECKING

from typing_extensions import TypedDict

if TYPE_CHECKING:
    import capo_glue.types.hash_string


class StartMLEvaluationTaskRunRequest(TypedDict, closed=True):
    transform_id: "capo_glue.types.hash_string.HashString"
    """<p>The unique identifier of the machine learning transform.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: StartMLEvaluationTaskRunRequest) -> dict:
    out: dict = {}
    out["TransformId"] = value["transform_id"]
    return out


def deserialize_aws_json_1_1(data: dict) -> StartMLEvaluationTaskRunRequest:
    out: StartMLEvaluationTaskRunRequest = {}  # type: ignore[typeddict-item]
    if data.get("TransformId") is not None:
        out["transform_id"] = data["TransformId"]
    else:
        out["transform_id"] = ""
    return out
