"""Generated from Smithy shape ``com.amazonaws.codepipeline#PipelineSummary``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_codepipeline.types.execution_mode
    import capo_codepipeline.types.pipeline_name
    import capo_codepipeline.types.pipeline_type
    import capo_codepipeline.types.pipeline_version
    import capo_codepipeline.types.timestamp


class PipelineSummary(TypedDict, closed=True):
    name: NotRequired["capo_codepipeline.types.pipeline_name.PipelineName"]
    """<p>The name of the pipeline.</p>"""
    version: NotRequired["capo_codepipeline.types.pipeline_version.PipelineVersion"]
    """<p>The version number of the pipeline.</p>"""
    pipeline_type: NotRequired["capo_codepipeline.types.pipeline_type.PipelineType"]
    """<p>CodePipeline provides the following pipeline types, which differ in characteristics and price, so that you can tailor your pipeline features and cost to the needs of your applications.</p> <ul> <li> <p>V1 type pipelines have a JSON structure that contains standard pipeline, stage, and action-level parameters.</p> </li> <li> <p>V2 type pipelines have the same structure as a V1 type, along with additional parameters for release safety and trigger configuration.</p> </li> </ul> <important> <p>Including V2 parameters, such as triggers on Git tags, in the pipeline JSON when creating or updating a pipeline will result in the pipeline having the V2 type of pipeline and the associated costs.</p> </important> <p>For information about pricing for CodePipeline, see <a href="http://aws.amazon.com/codepipeline/pricing/">Pricing</a>.</p> <p> For information about which type of pipeline to choose, see <a href="https://docs.aws.amazon.com/codepipeline/latest/userguide/pipeline-types-planning.html">What type of pipeline is right for me?</a>.</p>"""
    execution_mode: NotRequired["capo_codepipeline.types.execution_mode.ExecutionMode"]
    """<p>The method that the pipeline will use to handle multiple executions. The default mode is SUPERSEDED.</p>"""
    created: NotRequired["capo_codepipeline.types.timestamp.Timestamp"]
    """<p>The date and time the pipeline was created, in timestamp format.</p>"""
    updated: NotRequired["capo_codepipeline.types.timestamp.Timestamp"]
    """<p>The date and time of the last update to the pipeline, in timestamp format.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: PipelineSummary) -> dict:
    out: dict = {}
    if "name" in value:
        out["name"] = value["name"]
    if "version" in value:
        out["version"] = value["version"]
    if "pipeline_type" in value:
        import capo_codepipeline.types.pipeline_type

        out["pipelineType"] = (
            capo_codepipeline.types.pipeline_type.serialize_aws_json_1_1(
                value["pipeline_type"]
            )
        )
    if "execution_mode" in value:
        import capo_codepipeline.types.execution_mode

        out["executionMode"] = (
            capo_codepipeline.types.execution_mode.serialize_aws_json_1_1(
                value["execution_mode"]
            )
        )
    if "created" in value:
        import capo_codepipeline.types.timestamp

        out["created"] = capo_codepipeline.types.timestamp.serialize_aws_json_1_1(
            value["created"]
        )
    if "updated" in value:
        import capo_codepipeline.types.timestamp

        out["updated"] = capo_codepipeline.types.timestamp.serialize_aws_json_1_1(
            value["updated"]
        )
    return out


def deserialize_aws_json_1_1(data: dict) -> PipelineSummary:
    out: PipelineSummary = {}  # type: ignore[typeddict-item]
    if data.get("name") is not None:
        out["name"] = data["name"]
    if data.get("version") is not None:
        out["version"] = data["version"]
    if data.get("pipelineType") is not None:
        import capo_codepipeline.types.pipeline_type

        out["pipeline_type"] = (
            capo_codepipeline.types.pipeline_type.deserialize_aws_json_1_1(
                data["pipelineType"]
            )
        )
    if data.get("executionMode") is not None:
        import capo_codepipeline.types.execution_mode

        out["execution_mode"] = (
            capo_codepipeline.types.execution_mode.deserialize_aws_json_1_1(
                data["executionMode"]
            )
        )
    if data.get("created") is not None:
        import capo_codepipeline.types.timestamp

        out["created"] = capo_codepipeline.types.timestamp.deserialize_aws_json_1_1(
            data["created"]
        )
    if data.get("updated") is not None:
        import capo_codepipeline.types.timestamp

        out["updated"] = capo_codepipeline.types.timestamp.deserialize_aws_json_1_1(
            data["updated"]
        )
    return out
