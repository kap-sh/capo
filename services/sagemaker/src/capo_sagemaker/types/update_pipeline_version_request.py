"""Generated from Smithy shape ``com.amazonaws.sagemaker#UpdatePipelineVersionRequest``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_sagemaker.types.alias_operations
    import capo_sagemaker.types.pipeline_arn
    import capo_sagemaker.types.pipeline_version_description
    import capo_sagemaker.types.pipeline_version_id
    import capo_sagemaker.types.pipeline_version_name


class UpdatePipelineVersionRequest(TypedDict, closed=True):
    pipeline_arn: NotRequired["capo_sagemaker.types.pipeline_arn.PipelineArn"]
    """<p>The Amazon Resource Name (ARN) of the pipeline.</p>"""
    pipeline_version_id: NotRequired[
        "capo_sagemaker.types.pipeline_version_id.PipelineVersionId"
    ]
    """<p>The pipeline version ID to update.</p>"""
    pipeline_version_display_name: NotRequired[
        "capo_sagemaker.types.pipeline_version_name.PipelineVersionName"
    ]
    """<p>The display name of the pipeline version.</p>"""
    pipeline_version_description: NotRequired[
        "capo_sagemaker.types.pipeline_version_description.PipelineVersionDescription"
    ]
    """<p>The description of the pipeline version.</p>"""
    pipeline_version_alias_operations: NotRequired[
        "capo_sagemaker.types.alias_operations.AliasOperations"
    ]
    """<p>The aliases to add to or remove from the pipeline version.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: UpdatePipelineVersionRequest) -> dict:
    out: dict = {}
    if "pipeline_arn" in value:
        out["PipelineArn"] = value["pipeline_arn"]
    if "pipeline_version_id" in value:
        out["PipelineVersionId"] = value["pipeline_version_id"]
    if "pipeline_version_display_name" in value:
        out["PipelineVersionDisplayName"] = value["pipeline_version_display_name"]
    if "pipeline_version_description" in value:
        out["PipelineVersionDescription"] = value["pipeline_version_description"]
    if "pipeline_version_alias_operations" in value:
        import capo_sagemaker.types.alias_operations

        out["PipelineVersionAliasOperations"] = (
            capo_sagemaker.types.alias_operations.serialize_aws_json_1_1(
                value["pipeline_version_alias_operations"]
            )
        )
    return out


def deserialize_aws_json_1_1(data: dict) -> UpdatePipelineVersionRequest:
    out: UpdatePipelineVersionRequest = {}  # type: ignore[typeddict-item]
    if data.get("PipelineArn") is not None:
        out["pipeline_arn"] = data["PipelineArn"]
    if data.get("PipelineVersionId") is not None:
        out["pipeline_version_id"] = data["PipelineVersionId"]
    if data.get("PipelineVersionDisplayName") is not None:
        out["pipeline_version_display_name"] = data["PipelineVersionDisplayName"]
    if data.get("PipelineVersionDescription") is not None:
        out["pipeline_version_description"] = data["PipelineVersionDescription"]
    if data.get("PipelineVersionAliasOperations") is not None:
        import capo_sagemaker.types.alias_operations

        out["pipeline_version_alias_operations"] = (
            capo_sagemaker.types.alias_operations.deserialize_aws_json_1_1(
                data["PipelineVersionAliasOperations"]
            )
        )
    return out
