"""Generated from Smithy shape ``com.amazonaws.datapipeline#PipelineDescription``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

from capo_data_pipeline.errors import DeserializationError

if TYPE_CHECKING:
    import capo_data_pipeline.types.field_list
    import capo_data_pipeline.types.id
    import capo_data_pipeline.types.string
    import capo_data_pipeline.types.tag_list


class PipelineDescription(TypedDict, closed=True):
    pipeline_id: "capo_data_pipeline.types.id.id"
    """<p>The pipeline identifier that was assigned by AWS Data Pipeline. This is a string of the form <code>df-297EG78HU43EEXAMPLE</code>.</p>"""
    name: "capo_data_pipeline.types.id.id"
    """<p>The name of the pipeline.</p>"""
    fields: "capo_data_pipeline.types.field_list.fieldList"
    """<p>A list of read-only fields that contain metadata about the pipeline: @userId, @accountId, and @pipelineState.</p>"""
    description: NotRequired["capo_data_pipeline.types.string.string"]
    """<p>Description of the pipeline.</p>"""
    tags: NotRequired["capo_data_pipeline.types.tag_list.tagList"]
    """<p>A list of tags to associated with a pipeline. Tags let you control access to pipelines. For more information, see <a href="http://docs.aws.amazon.com/datapipeline/latest/DeveloperGuide/dp-control-access.html">Controlling User Access to Pipelines</a> in the <i>AWS Data Pipeline Developer Guide</i>.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: PipelineDescription) -> dict:
    out: dict = {}
    out["pipelineId"] = value["pipeline_id"]
    out["name"] = value["name"]
    import capo_data_pipeline.types.field_list

    out["fields"] = capo_data_pipeline.types.field_list.serialize_aws_json_1_1(
        value["fields"]
    )
    if "description" in value:
        out["description"] = value["description"]
    if "tags" in value:
        import capo_data_pipeline.types.tag_list

        out["tags"] = capo_data_pipeline.types.tag_list.serialize_aws_json_1_1(
            value["tags"]
        )
    return out


def deserialize_aws_json_1_1(data: dict) -> PipelineDescription:
    out: PipelineDescription = {}  # type: ignore[typeddict-item]
    if data.get("pipelineId") is not None:
        out["pipeline_id"] = data["pipelineId"]
    else:
        raise DeserializationError("PipelineDescription.pipeline_id required")
    if data.get("name") is not None:
        out["name"] = data["name"]
    else:
        raise DeserializationError("PipelineDescription.name required")
    if data.get("fields") is not None:
        import capo_data_pipeline.types.field_list

        out["fields"] = capo_data_pipeline.types.field_list.deserialize_aws_json_1_1(
            data["fields"]
        )
    else:
        raise DeserializationError("PipelineDescription.fields required")
    if data.get("description") is not None:
        out["description"] = data["description"]
    if data.get("tags") is not None:
        import capo_data_pipeline.types.tag_list

        out["tags"] = capo_data_pipeline.types.tag_list.deserialize_aws_json_1_1(
            data["tags"]
        )
    return out
