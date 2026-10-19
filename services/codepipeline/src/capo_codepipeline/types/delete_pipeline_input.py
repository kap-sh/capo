"""Generated from Smithy shape ``com.amazonaws.codepipeline#DeletePipelineInput``."""

from typing import TYPE_CHECKING

from typing_extensions import TypedDict

if TYPE_CHECKING:
    import capo_codepipeline.types.pipeline_name


class DeletePipelineInput(TypedDict, closed=True):
    name: "capo_codepipeline.types.pipeline_name.PipelineName"
    """<p>The name of the pipeline to be deleted.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: DeletePipelineInput) -> dict:
    out: dict = {}
    out["name"] = value["name"]
    return out


def deserialize_aws_json_1_1(data: dict) -> DeletePipelineInput:
    out: DeletePipelineInput = {}  # type: ignore[typeddict-item]
    if data.get("name") is not None:
        out["name"] = data["name"]
    else:
        out["name"] = ""
    return out
