"""Generated from Smithy shape ``com.amazonaws.bedrock#CreateModelCopyJobResponse``."""

from typing import TYPE_CHECKING

from typing_extensions import TypedDict

if TYPE_CHECKING:
    import capo_bedrock.types.model_copy_job_arn


class CreateModelCopyJobResponse(TypedDict, closed=True):
    job_arn: "capo_bedrock.types.model_copy_job_arn.ModelCopyJobArn"
    """<p>The Amazon Resource Name (ARN) of the model copy job.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: CreateModelCopyJobResponse) -> dict:
    out: dict = {}
    out["jobArn"] = value["job_arn"]
    return out


def deserialize_json(data: dict) -> CreateModelCopyJobResponse:
    out: CreateModelCopyJobResponse = {}  # type: ignore[typeddict-item]
    if data.get("jobArn") is not None:
        out["job_arn"] = data["jobArn"]
    else:
        out["job_arn"] = ""
    return out
