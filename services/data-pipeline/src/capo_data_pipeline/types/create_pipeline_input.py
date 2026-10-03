"""Generated from Smithy shape ``com.amazonaws.datapipeline#CreatePipelineInput``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

from capo_data_pipeline.errors import DeserializationError

if TYPE_CHECKING:
    import capo_data_pipeline.types.id
    import capo_data_pipeline.types.string
    import capo_data_pipeline.types.tag_list


class CreatePipelineInput(TypedDict, closed=True):
    name: "capo_data_pipeline.types.id.id"
    """<p>The name for the pipeline. You can use the same name for multiple pipelines associated with your AWS account, because AWS Data Pipeline assigns each pipeline a unique pipeline identifier.</p>"""
    unique_id: "capo_data_pipeline.types.id.id"
    """<p>A unique identifier. This identifier is not the same as the pipeline identifier assigned by AWS Data Pipeline. You are responsible for defining the format and ensuring the uniqueness of this identifier. You use this parameter to ensure idempotency during repeated calls to <code>CreatePipeline</code>. For example, if the first call to <code>CreatePipeline</code> does not succeed, you can pass in the same unique identifier and pipeline name combination on a subsequent call to <code>CreatePipeline</code>. <code>CreatePipeline</code> ensures that if a pipeline already exists with the same name and unique identifier, a new pipeline is not created. Instead, you'll receive the pipeline identifier from the previous attempt. The uniqueness of the name and unique identifier combination is scoped to the AWS account or IAM user credentials.</p>"""
    description: NotRequired["capo_data_pipeline.types.string.string"]
    """<p>The description for the pipeline.</p>"""
    tags: NotRequired["capo_data_pipeline.types.tag_list.tagList"]
    """<p>A list of tags to associate with the pipeline at creation. Tags let you control access to pipelines. For more information, see <a href="http://docs.aws.amazon.com/datapipeline/latest/DeveloperGuide/dp-control-access.html">Controlling User Access to Pipelines</a> in the <i>AWS Data Pipeline Developer Guide</i>.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: CreatePipelineInput) -> dict:
    out: dict = {}
    out["name"] = value["name"]
    out["uniqueId"] = value["unique_id"]
    if "description" in value:
        out["description"] = value["description"]
    if "tags" in value:
        import capo_data_pipeline.types.tag_list

        out["tags"] = capo_data_pipeline.types.tag_list.serialize_aws_json_1_1(
            value["tags"]
        )
    return out


def deserialize_aws_json_1_1(data: dict) -> CreatePipelineInput:
    out: CreatePipelineInput = {}  # type: ignore[typeddict-item]
    if data.get("name") is not None:
        out["name"] = data["name"]
    else:
        raise DeserializationError("CreatePipelineInput.name required")
    if data.get("uniqueId") is not None:
        out["unique_id"] = data["uniqueId"]
    else:
        raise DeserializationError("CreatePipelineInput.unique_id required")
    if data.get("description") is not None:
        out["description"] = data["description"]
    if data.get("tags") is not None:
        import capo_data_pipeline.types.tag_list

        out["tags"] = capo_data_pipeline.types.tag_list.deserialize_aws_json_1_1(
            data["tags"]
        )
    return out
