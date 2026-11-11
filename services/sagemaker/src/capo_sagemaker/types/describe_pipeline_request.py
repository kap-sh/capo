"""Generated from Smithy shape ``com.amazonaws.sagemaker#DescribePipelineRequest``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_sagemaker.types.pipeline_name_or_arn
    import capo_sagemaker.types.pipeline_version_alias
    import capo_sagemaker.types.pipeline_version_id


class DescribePipelineRequest(TypedDict, closed=True):
    pipeline_name: NotRequired[
        "capo_sagemaker.types.pipeline_name_or_arn.PipelineNameOrArn"
    ]
    """<p>The name or Amazon Resource Name (ARN) of the pipeline to describe.</p>"""
    pipeline_version_id: NotRequired[
        "capo_sagemaker.types.pipeline_version_id.PipelineVersionId"
    ]
    """<p>The ID of the pipeline version to describe. You can't specify this with <code>PipelineVersionAlias</code>.</p>"""
    pipeline_version_alias: NotRequired[
        "capo_sagemaker.types.pipeline_version_alias.PipelineVersionAlias"
    ]
    """<p>The alias of the pipeline version to describe. You can't specify this with <code>PipelineVersionId</code>. If no version of the pipeline has this alias, the request fails with a <code>ResourceNotFound</code> error. If you specify neither, SageMaker describes the latest version of the pipeline.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: DescribePipelineRequest) -> dict:
    out: dict = {}
    if "pipeline_name" in value:
        out["PipelineName"] = value["pipeline_name"]
    if "pipeline_version_id" in value:
        out["PipelineVersionId"] = value["pipeline_version_id"]
    if "pipeline_version_alias" in value:
        out["PipelineVersionAlias"] = value["pipeline_version_alias"]
    return out


def deserialize_aws_json_1_1(data: dict) -> DescribePipelineRequest:
    out: DescribePipelineRequest = {}  # type: ignore[typeddict-item]
    if data.get("PipelineName") is not None:
        out["pipeline_name"] = data["PipelineName"]
    if data.get("PipelineVersionId") is not None:
        out["pipeline_version_id"] = data["PipelineVersionId"]
    if data.get("PipelineVersionAlias") is not None:
        out["pipeline_version_alias"] = data["PipelineVersionAlias"]
    return out
