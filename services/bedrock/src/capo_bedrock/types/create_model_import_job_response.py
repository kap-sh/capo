"""Generated from Smithy shape ``com.amazonaws.bedrock#CreateModelImportJobResponse``."""

from typing import TYPE_CHECKING

from typing_extensions import TypedDict

if TYPE_CHECKING:
    import capo_bedrock.types.model_import_job_arn


class CreateModelImportJobResponse(TypedDict, closed=True):
    job_arn: "capo_bedrock.types.model_import_job_arn.ModelImportJobArn"
    """<p>The Amazon Resource Name (ARN) of the model import job.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: CreateModelImportJobResponse) -> dict:
    out: dict = {}
    out["jobArn"] = value["job_arn"]
    return out


def deserialize_json(data: dict) -> CreateModelImportJobResponse:
    out: CreateModelImportJobResponse = {}  # type: ignore[typeddict-item]
    if data.get("jobArn") is not None:
        out["job_arn"] = data["jobArn"]
    else:
        out["job_arn"] = ""
    return out
