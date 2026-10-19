"""Generated from Smithy shape ``com.amazonaws.bedrock#CreateEvaluationJobResponse``."""

from typing import TYPE_CHECKING

from typing_extensions import TypedDict

if TYPE_CHECKING:
    import capo_bedrock.types.evaluation_job_arn


class CreateEvaluationJobResponse(TypedDict, closed=True):
    job_arn: "capo_bedrock.types.evaluation_job_arn.EvaluationJobArn"
    """<p>The Amazon Resource Name (ARN) of the evaluation job.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: CreateEvaluationJobResponse) -> dict:
    out: dict = {}
    out["jobArn"] = value["job_arn"]
    return out


def deserialize_json(data: dict) -> CreateEvaluationJobResponse:
    out: CreateEvaluationJobResponse = {}  # type: ignore[typeddict-item]
    if data.get("jobArn") is not None:
        out["job_arn"] = data["jobArn"]
    else:
        out["job_arn"] = ""
    return out
