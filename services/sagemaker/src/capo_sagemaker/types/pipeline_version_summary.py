"""Generated from Smithy shape ``com.amazonaws.sagemaker#PipelineVersionSummary``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_sagemaker.types.pipeline_arn
    import capo_sagemaker.types.pipeline_execution_arn
    import capo_sagemaker.types.pipeline_version_alias_list
    import capo_sagemaker.types.pipeline_version_description
    import capo_sagemaker.types.pipeline_version_id
    import capo_sagemaker.types.pipeline_version_name
    import capo_sagemaker.types.timestamp


class PipelineVersionSummary(TypedDict, closed=True):
    pipeline_arn: NotRequired["capo_sagemaker.types.pipeline_arn.PipelineArn"]
    """<p>The Amazon Resource Name (ARN) of the pipeline.</p>"""
    pipeline_version_id: NotRequired[
        "capo_sagemaker.types.pipeline_version_id.PipelineVersionId"
    ]
    """<p>The ID of the pipeline version.</p>"""
    creation_time: NotRequired["capo_sagemaker.types.timestamp.Timestamp"]
    """<p>The creation time of the pipeline version.</p>"""
    pipeline_version_description: NotRequired[
        "capo_sagemaker.types.pipeline_version_description.PipelineVersionDescription"
    ]
    """<p>The description of the pipeline version.</p>"""
    pipeline_version_display_name: NotRequired[
        "capo_sagemaker.types.pipeline_version_name.PipelineVersionName"
    ]
    """<p>The display name of the pipeline version.</p>"""
    last_execution_pipeline_execution_arn: NotRequired[
        "capo_sagemaker.types.pipeline_execution_arn.PipelineExecutionArn"
    ]
    """<p>The Amazon Resource Name (ARN) of the most recent pipeline execution created from this pipeline version.</p>"""
    pipeline_version_aliases: NotRequired[
        "capo_sagemaker.types.pipeline_version_alias_list.PipelineVersionAliasList"
    ]
    """<p>The aliases assigned to the pipeline version.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: PipelineVersionSummary) -> dict:
    out: dict = {}
    if "pipeline_arn" in value:
        out["PipelineArn"] = value["pipeline_arn"]
    if "pipeline_version_id" in value:
        out["PipelineVersionId"] = value["pipeline_version_id"]
    if "creation_time" in value:
        import capo_sagemaker.types.timestamp

        out["CreationTime"] = capo_sagemaker.types.timestamp.serialize_aws_json_1_1(
            value["creation_time"]
        )
    if "pipeline_version_description" in value:
        out["PipelineVersionDescription"] = value["pipeline_version_description"]
    if "pipeline_version_display_name" in value:
        out["PipelineVersionDisplayName"] = value["pipeline_version_display_name"]
    if "last_execution_pipeline_execution_arn" in value:
        out["LastExecutionPipelineExecutionArn"] = value[
            "last_execution_pipeline_execution_arn"
        ]
    if "pipeline_version_aliases" in value:
        import capo_sagemaker.types.pipeline_version_alias_list

        out["PipelineVersionAliases"] = (
            capo_sagemaker.types.pipeline_version_alias_list.serialize_aws_json_1_1(
                value["pipeline_version_aliases"]
            )
        )
    return out


def deserialize_aws_json_1_1(data: dict) -> PipelineVersionSummary:
    out: PipelineVersionSummary = {}  # type: ignore[typeddict-item]
    if data.get("PipelineArn") is not None:
        out["pipeline_arn"] = data["PipelineArn"]
    if data.get("PipelineVersionId") is not None:
        out["pipeline_version_id"] = data["PipelineVersionId"]
    if data.get("CreationTime") is not None:
        import capo_sagemaker.types.timestamp

        out["creation_time"] = capo_sagemaker.types.timestamp.deserialize_aws_json_1_1(
            data["CreationTime"]
        )
    if data.get("PipelineVersionDescription") is not None:
        out["pipeline_version_description"] = data["PipelineVersionDescription"]
    if data.get("PipelineVersionDisplayName") is not None:
        out["pipeline_version_display_name"] = data["PipelineVersionDisplayName"]
    if data.get("LastExecutionPipelineExecutionArn") is not None:
        out["last_execution_pipeline_execution_arn"] = data[
            "LastExecutionPipelineExecutionArn"
        ]
    if data.get("PipelineVersionAliases") is not None:
        import capo_sagemaker.types.pipeline_version_alias_list

        out["pipeline_version_aliases"] = (
            capo_sagemaker.types.pipeline_version_alias_list.deserialize_aws_json_1_1(
                data["PipelineVersionAliases"]
            )
        )
    return out
