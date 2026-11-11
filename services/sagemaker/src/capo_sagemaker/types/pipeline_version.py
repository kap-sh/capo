"""Generated from Smithy shape ``com.amazonaws.sagemaker#PipelineVersion``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_sagemaker.types.pipeline_arn
    import capo_sagemaker.types.pipeline_execution_arn
    import capo_sagemaker.types.pipeline_execution_name
    import capo_sagemaker.types.pipeline_execution_status
    import capo_sagemaker.types.pipeline_version_alias_list
    import capo_sagemaker.types.pipeline_version_description
    import capo_sagemaker.types.pipeline_version_id
    import capo_sagemaker.types.pipeline_version_name
    import capo_sagemaker.types.timestamp
    import capo_sagemaker.types.user_context


class PipelineVersion(TypedDict, closed=True):
    pipeline_arn: NotRequired["capo_sagemaker.types.pipeline_arn.PipelineArn"]
    """<p>The Amazon Resource Name (ARN) of the pipeline.</p>"""
    pipeline_version_id: NotRequired[
        "capo_sagemaker.types.pipeline_version_id.PipelineVersionId"
    ]
    """<p>The ID of the pipeline version.</p>"""
    pipeline_version_display_name: NotRequired[
        "capo_sagemaker.types.pipeline_version_name.PipelineVersionName"
    ]
    """<p>The display name of the pipeline version.</p>"""
    pipeline_version_description: NotRequired[
        "capo_sagemaker.types.pipeline_version_description.PipelineVersionDescription"
    ]
    """<p>The description of the pipeline version.</p>"""
    creation_time: NotRequired["capo_sagemaker.types.timestamp.Timestamp"]
    """<p>The creation time of the pipeline version.</p>"""
    last_modified_time: NotRequired["capo_sagemaker.types.timestamp.Timestamp"]
    """<p>The time when the pipeline version was last modified.</p>"""
    created_by: NotRequired["capo_sagemaker.types.user_context.UserContext"]
    last_modified_by: NotRequired["capo_sagemaker.types.user_context.UserContext"]
    last_executed_pipeline_execution_arn: NotRequired[
        "capo_sagemaker.types.pipeline_execution_arn.PipelineExecutionArn"
    ]
    """<p>The Amazon Resource Name (ARN) of the most recent pipeline execution created from this pipeline version.</p>"""
    last_executed_pipeline_execution_display_name: NotRequired[
        "capo_sagemaker.types.pipeline_execution_name.PipelineExecutionName"
    ]
    """<p>The display name of the most recent pipeline execution created from this pipeline version.</p>"""
    last_executed_pipeline_execution_status: NotRequired[
        "capo_sagemaker.types.pipeline_execution_status.PipelineExecutionStatus"
    ]
    """<p>The status of the most recent pipeline execution created from this pipeline version.</p>"""
    pipeline_version_aliases: NotRequired[
        "capo_sagemaker.types.pipeline_version_alias_list.PipelineVersionAliasList"
    ]
    """<p>The aliases assigned to the pipeline version.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: PipelineVersion) -> dict:
    out: dict = {}
    if "pipeline_arn" in value:
        out["PipelineArn"] = value["pipeline_arn"]
    if "pipeline_version_id" in value:
        out["PipelineVersionId"] = value["pipeline_version_id"]
    if "pipeline_version_display_name" in value:
        out["PipelineVersionDisplayName"] = value["pipeline_version_display_name"]
    if "pipeline_version_description" in value:
        out["PipelineVersionDescription"] = value["pipeline_version_description"]
    if "creation_time" in value:
        import capo_sagemaker.types.timestamp

        out["CreationTime"] = capo_sagemaker.types.timestamp.serialize_aws_json_1_1(
            value["creation_time"]
        )
    if "last_modified_time" in value:
        import capo_sagemaker.types.timestamp

        out["LastModifiedTime"] = capo_sagemaker.types.timestamp.serialize_aws_json_1_1(
            value["last_modified_time"]
        )
    if "created_by" in value:
        import capo_sagemaker.types.user_context

        out["CreatedBy"] = capo_sagemaker.types.user_context.serialize_aws_json_1_1(
            value["created_by"]
        )
    if "last_modified_by" in value:
        import capo_sagemaker.types.user_context

        out["LastModifiedBy"] = (
            capo_sagemaker.types.user_context.serialize_aws_json_1_1(
                value["last_modified_by"]
            )
        )
    if "last_executed_pipeline_execution_arn" in value:
        out["LastExecutedPipelineExecutionArn"] = value[
            "last_executed_pipeline_execution_arn"
        ]
    if "last_executed_pipeline_execution_display_name" in value:
        out["LastExecutedPipelineExecutionDisplayName"] = value[
            "last_executed_pipeline_execution_display_name"
        ]
    if "last_executed_pipeline_execution_status" in value:
        import capo_sagemaker.types.pipeline_execution_status

        out["LastExecutedPipelineExecutionStatus"] = (
            capo_sagemaker.types.pipeline_execution_status.serialize_aws_json_1_1(
                value["last_executed_pipeline_execution_status"]
            )
        )
    if "pipeline_version_aliases" in value:
        import capo_sagemaker.types.pipeline_version_alias_list

        out["PipelineVersionAliases"] = (
            capo_sagemaker.types.pipeline_version_alias_list.serialize_aws_json_1_1(
                value["pipeline_version_aliases"]
            )
        )
    return out


def deserialize_aws_json_1_1(data: dict) -> PipelineVersion:
    out: PipelineVersion = {}  # type: ignore[typeddict-item]
    if data.get("PipelineArn") is not None:
        out["pipeline_arn"] = data["PipelineArn"]
    if data.get("PipelineVersionId") is not None:
        out["pipeline_version_id"] = data["PipelineVersionId"]
    if data.get("PipelineVersionDisplayName") is not None:
        out["pipeline_version_display_name"] = data["PipelineVersionDisplayName"]
    if data.get("PipelineVersionDescription") is not None:
        out["pipeline_version_description"] = data["PipelineVersionDescription"]
    if data.get("CreationTime") is not None:
        import capo_sagemaker.types.timestamp

        out["creation_time"] = capo_sagemaker.types.timestamp.deserialize_aws_json_1_1(
            data["CreationTime"]
        )
    if data.get("LastModifiedTime") is not None:
        import capo_sagemaker.types.timestamp

        out["last_modified_time"] = (
            capo_sagemaker.types.timestamp.deserialize_aws_json_1_1(
                data["LastModifiedTime"]
            )
        )
    if data.get("CreatedBy") is not None:
        import capo_sagemaker.types.user_context

        out["created_by"] = capo_sagemaker.types.user_context.deserialize_aws_json_1_1(
            data["CreatedBy"]
        )
    if data.get("LastModifiedBy") is not None:
        import capo_sagemaker.types.user_context

        out["last_modified_by"] = (
            capo_sagemaker.types.user_context.deserialize_aws_json_1_1(
                data["LastModifiedBy"]
            )
        )
    if data.get("LastExecutedPipelineExecutionArn") is not None:
        out["last_executed_pipeline_execution_arn"] = data[
            "LastExecutedPipelineExecutionArn"
        ]
    if data.get("LastExecutedPipelineExecutionDisplayName") is not None:
        out["last_executed_pipeline_execution_display_name"] = data[
            "LastExecutedPipelineExecutionDisplayName"
        ]
    if data.get("LastExecutedPipelineExecutionStatus") is not None:
        import capo_sagemaker.types.pipeline_execution_status

        out["last_executed_pipeline_execution_status"] = (
            capo_sagemaker.types.pipeline_execution_status.deserialize_aws_json_1_1(
                data["LastExecutedPipelineExecutionStatus"]
            )
        )
    if data.get("PipelineVersionAliases") is not None:
        import capo_sagemaker.types.pipeline_version_alias_list

        out["pipeline_version_aliases"] = (
            capo_sagemaker.types.pipeline_version_alias_list.deserialize_aws_json_1_1(
                data["PipelineVersionAliases"]
            )
        )
    return out
