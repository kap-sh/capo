"""Generated from Smithy shape ``com.amazonaws.sagemaker#DescribePipelineResponse``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_sagemaker.types.parallelism_configuration
    import capo_sagemaker.types.pipeline_arn
    import capo_sagemaker.types.pipeline_definition
    import capo_sagemaker.types.pipeline_description
    import capo_sagemaker.types.pipeline_name
    import capo_sagemaker.types.pipeline_status
    import capo_sagemaker.types.pipeline_version_alias_list
    import capo_sagemaker.types.pipeline_version_description
    import capo_sagemaker.types.pipeline_version_name
    import capo_sagemaker.types.role_arn
    import capo_sagemaker.types.timestamp
    import capo_sagemaker.types.user_context


class DescribePipelineResponse(TypedDict, closed=True):
    pipeline_arn: NotRequired["capo_sagemaker.types.pipeline_arn.PipelineArn"]
    """<p>The Amazon Resource Name (ARN) of the pipeline.</p>"""
    pipeline_name: NotRequired["capo_sagemaker.types.pipeline_name.PipelineName"]
    """<p>The name of the pipeline.</p>"""
    pipeline_display_name: NotRequired[
        "capo_sagemaker.types.pipeline_name.PipelineName"
    ]
    """<p>The display name of the pipeline.</p>"""
    pipeline_definition: NotRequired[
        "capo_sagemaker.types.pipeline_definition.PipelineDefinition"
    ]
    """<p>The JSON pipeline definition.</p>"""
    pipeline_description: NotRequired[
        "capo_sagemaker.types.pipeline_description.PipelineDescription"
    ]
    """<p>The description of the pipeline.</p>"""
    role_arn: NotRequired["capo_sagemaker.types.role_arn.RoleArn"]
    """<p>The Amazon Resource Name (ARN) that the pipeline uses to execute.</p>"""
    pipeline_status: NotRequired["capo_sagemaker.types.pipeline_status.PipelineStatus"]
    """<p>The status of the pipeline execution.</p>"""
    creation_time: NotRequired["capo_sagemaker.types.timestamp.Timestamp"]
    """<p>The time when the pipeline was created.</p>"""
    last_modified_time: NotRequired["capo_sagemaker.types.timestamp.Timestamp"]
    """<p>The time when the pipeline was last modified.</p>"""
    last_run_time: NotRequired["capo_sagemaker.types.timestamp.Timestamp"]
    """<p>The time when the pipeline was last run.</p>"""
    created_by: NotRequired["capo_sagemaker.types.user_context.UserContext"]
    last_modified_by: NotRequired["capo_sagemaker.types.user_context.UserContext"]
    parallelism_configuration: NotRequired[
        "capo_sagemaker.types.parallelism_configuration.ParallelismConfiguration"
    ]
    """<p>Lists the parallelism configuration applied to the pipeline.</p>"""
    pipeline_version_display_name: NotRequired[
        "capo_sagemaker.types.pipeline_version_name.PipelineVersionName"
    ]
    """<p>The display name of the pipeline version.</p>"""
    pipeline_version_description: NotRequired[
        "capo_sagemaker.types.pipeline_version_description.PipelineVersionDescription"
    ]
    """<p>The description of the pipeline version.</p>"""
    pipeline_version_aliases: NotRequired[
        "capo_sagemaker.types.pipeline_version_alias_list.PipelineVersionAliasList"
    ]
    """<p>The aliases assigned to the pipeline version.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: DescribePipelineResponse) -> dict:
    out: dict = {}
    if "pipeline_arn" in value:
        out["PipelineArn"] = value["pipeline_arn"]
    if "pipeline_name" in value:
        out["PipelineName"] = value["pipeline_name"]
    if "pipeline_display_name" in value:
        out["PipelineDisplayName"] = value["pipeline_display_name"]
    if "pipeline_definition" in value:
        out["PipelineDefinition"] = value["pipeline_definition"]
    if "pipeline_description" in value:
        out["PipelineDescription"] = value["pipeline_description"]
    if "role_arn" in value:
        out["RoleArn"] = value["role_arn"]
    if "pipeline_status" in value:
        import capo_sagemaker.types.pipeline_status

        out["PipelineStatus"] = (
            capo_sagemaker.types.pipeline_status.serialize_aws_json_1_1(
                value["pipeline_status"]
            )
        )
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
    if "last_run_time" in value:
        import capo_sagemaker.types.timestamp

        out["LastRunTime"] = capo_sagemaker.types.timestamp.serialize_aws_json_1_1(
            value["last_run_time"]
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
    if "parallelism_configuration" in value:
        import capo_sagemaker.types.parallelism_configuration

        out["ParallelismConfiguration"] = (
            capo_sagemaker.types.parallelism_configuration.serialize_aws_json_1_1(
                value["parallelism_configuration"]
            )
        )
    if "pipeline_version_display_name" in value:
        out["PipelineVersionDisplayName"] = value["pipeline_version_display_name"]
    if "pipeline_version_description" in value:
        out["PipelineVersionDescription"] = value["pipeline_version_description"]
    if "pipeline_version_aliases" in value:
        import capo_sagemaker.types.pipeline_version_alias_list

        out["PipelineVersionAliases"] = (
            capo_sagemaker.types.pipeline_version_alias_list.serialize_aws_json_1_1(
                value["pipeline_version_aliases"]
            )
        )
    return out


def deserialize_aws_json_1_1(data: dict) -> DescribePipelineResponse:
    out: DescribePipelineResponse = {}  # type: ignore[typeddict-item]
    if data.get("PipelineArn") is not None:
        out["pipeline_arn"] = data["PipelineArn"]
    if data.get("PipelineName") is not None:
        out["pipeline_name"] = data["PipelineName"]
    if data.get("PipelineDisplayName") is not None:
        out["pipeline_display_name"] = data["PipelineDisplayName"]
    if data.get("PipelineDefinition") is not None:
        out["pipeline_definition"] = data["PipelineDefinition"]
    if data.get("PipelineDescription") is not None:
        out["pipeline_description"] = data["PipelineDescription"]
    if data.get("RoleArn") is not None:
        out["role_arn"] = data["RoleArn"]
    if data.get("PipelineStatus") is not None:
        import capo_sagemaker.types.pipeline_status

        out["pipeline_status"] = (
            capo_sagemaker.types.pipeline_status.deserialize_aws_json_1_1(
                data["PipelineStatus"]
            )
        )
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
    if data.get("LastRunTime") is not None:
        import capo_sagemaker.types.timestamp

        out["last_run_time"] = capo_sagemaker.types.timestamp.deserialize_aws_json_1_1(
            data["LastRunTime"]
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
    if data.get("ParallelismConfiguration") is not None:
        import capo_sagemaker.types.parallelism_configuration

        out["parallelism_configuration"] = (
            capo_sagemaker.types.parallelism_configuration.deserialize_aws_json_1_1(
                data["ParallelismConfiguration"]
            )
        )
    if data.get("PipelineVersionDisplayName") is not None:
        out["pipeline_version_display_name"] = data["PipelineVersionDisplayName"]
    if data.get("PipelineVersionDescription") is not None:
        out["pipeline_version_description"] = data["PipelineVersionDescription"]
    if data.get("PipelineVersionAliases") is not None:
        import capo_sagemaker.types.pipeline_version_alias_list

        out["pipeline_version_aliases"] = (
            capo_sagemaker.types.pipeline_version_alias_list.deserialize_aws_json_1_1(
                data["PipelineVersionAliases"]
            )
        )
    return out
