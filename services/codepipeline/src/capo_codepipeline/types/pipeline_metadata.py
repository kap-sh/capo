"""Generated from Smithy shape ``com.amazonaws.codepipeline#PipelineMetadata``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_codepipeline.types.pipeline_arn
    import capo_codepipeline.types.timestamp


class PipelineMetadata(TypedDict, closed=True):
    pipeline_arn: NotRequired["capo_codepipeline.types.pipeline_arn.PipelineArn"]
    """<p>The Amazon Resource Name (ARN) of the pipeline.</p>"""
    created: NotRequired["capo_codepipeline.types.timestamp.Timestamp"]
    """<p>The date and time the pipeline was created, in timestamp format.</p>"""
    updated: NotRequired["capo_codepipeline.types.timestamp.Timestamp"]
    """<p>The date and time the pipeline was last updated, in timestamp format.</p>"""
    polling_disabled_at: NotRequired["capo_codepipeline.types.timestamp.Timestamp"]
    """<p>The date and time that polling for source changes (periodic checks) was stopped for the pipeline, in timestamp format. </p> <important> <p>Pipelines that are inactive for longer than 30 days will have polling disabled for the pipeline. For more information, see <a href="https://docs.aws.amazon.com/codepipeline/latest/userguide/reference-pipeline-structure.html#metadata.pollingDisabledAt">pollingDisabledAt</a> in the pipeline structure reference. For the steps to migrate your pipeline from polling to event-based change detection, see <a href="https://docs.aws.amazon.com/codepipeline/latest/userguide/update-change-detection.html">Migrate polling pipelines to use event-based change detection</a>.</p> </important> <p>You can migrate (update) a polling pipeline to use event-based change detection. For example, for a pipeline with a CodeCommit source, we recommend you migrate (update) your pipeline to use CloudWatch Events. To learn more, see <a href="https://docs.aws.amazon.com/codepipeline/latest/userguide/update-change-detection.html">Migrate polling pipelines to use event-based change detection</a> in the <i>CodePipeline User Guide</i>.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: PipelineMetadata) -> dict:
    out: dict = {}
    if "pipeline_arn" in value:
        out["pipelineArn"] = value["pipeline_arn"]
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
    if "polling_disabled_at" in value:
        import capo_codepipeline.types.timestamp

        out["pollingDisabledAt"] = (
            capo_codepipeline.types.timestamp.serialize_aws_json_1_1(
                value["polling_disabled_at"]
            )
        )
    return out


def deserialize_aws_json_1_1(data: dict) -> PipelineMetadata:
    out: PipelineMetadata = {}  # type: ignore[typeddict-item]
    if data.get("pipelineArn") is not None:
        out["pipeline_arn"] = data["pipelineArn"]
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
    if data.get("pollingDisabledAt") is not None:
        import capo_codepipeline.types.timestamp

        out["polling_disabled_at"] = (
            capo_codepipeline.types.timestamp.deserialize_aws_json_1_1(
                data["pollingDisabledAt"]
            )
        )
    return out
