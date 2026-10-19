"""Generated from Smithy shape ``com.amazonaws.codepipeline#GetPipelineInput``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_codepipeline.types.pipeline_name
    import capo_codepipeline.types.pipeline_version


class GetPipelineInput(TypedDict, closed=True):
    name: "capo_codepipeline.types.pipeline_name.PipelineName"
    """<p>The name of the pipeline for which you want to get information. Pipeline names must be unique in an Amazon Web Services account.</p>"""
    version: NotRequired["capo_codepipeline.types.pipeline_version.PipelineVersion"]
    """<p>The version number of the pipeline. If you do not specify a version, defaults to the current version.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: GetPipelineInput) -> dict:
    out: dict = {}
    out["name"] = value["name"]
    if "version" in value:
        out["version"] = value["version"]
    return out


def deserialize_aws_json_1_1(data: dict) -> GetPipelineInput:
    out: GetPipelineInput = {}  # type: ignore[typeddict-item]
    if data.get("name") is not None:
        out["name"] = data["name"]
    else:
        out["name"] = ""
    if data.get("version") is not None:
        out["version"] = data["version"]
    return out
