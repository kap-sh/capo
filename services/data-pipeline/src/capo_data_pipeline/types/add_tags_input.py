"""Generated from Smithy shape ``com.amazonaws.datapipeline#AddTagsInput``."""

from typing import TYPE_CHECKING

from typing_extensions import TypedDict

if TYPE_CHECKING:
    import capo_data_pipeline.types.id
    import capo_data_pipeline.types.tag_list


class AddTagsInput(TypedDict, closed=True):
    pipeline_id: "capo_data_pipeline.types.id.id"
    """<p>The ID of the pipeline.</p>"""
    tags: "capo_data_pipeline.types.tag_list.tagList"
    """<p>The tags to add, as key/value pairs.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: AddTagsInput) -> dict:
    out: dict = {}
    out["pipelineId"] = value["pipeline_id"]
    import capo_data_pipeline.types.tag_list

    out["tags"] = capo_data_pipeline.types.tag_list.serialize_aws_json_1_1(
        value["tags"]
    )
    return out


def deserialize_aws_json_1_1(data: dict) -> AddTagsInput:
    out: AddTagsInput = {}  # type: ignore[typeddict-item]
    if data.get("pipelineId") is not None:
        out["pipeline_id"] = data["pipelineId"]
    else:
        out["pipeline_id"] = ""
    if data.get("tags") is not None:
        import capo_data_pipeline.types.tag_list

        out["tags"] = capo_data_pipeline.types.tag_list.deserialize_aws_json_1_1(
            data["tags"]
        )
    else:
        out["tags"] = []
    return out
