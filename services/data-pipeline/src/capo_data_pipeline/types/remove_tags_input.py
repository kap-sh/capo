"""Generated from Smithy shape ``com.amazonaws.datapipeline#RemoveTagsInput``."""

from typing import TYPE_CHECKING

from typing_extensions import TypedDict

if TYPE_CHECKING:
    import capo_data_pipeline.types.id
    import capo_data_pipeline.types.string_list


class RemoveTagsInput(TypedDict, closed=True):
    pipeline_id: "capo_data_pipeline.types.id.id"
    """<p>The ID of the pipeline.</p>"""
    tag_keys: "capo_data_pipeline.types.string_list.stringList"
    """<p>The keys of the tags to remove.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: RemoveTagsInput) -> dict:
    out: dict = {}
    out["pipelineId"] = value["pipeline_id"]
    import capo_data_pipeline.types.string_list

    out["tagKeys"] = capo_data_pipeline.types.string_list.serialize_aws_json_1_1(
        value["tag_keys"]
    )
    return out


def deserialize_aws_json_1_1(data: dict) -> RemoveTagsInput:
    out: RemoveTagsInput = {}  # type: ignore[typeddict-item]
    if data.get("pipelineId") is not None:
        out["pipeline_id"] = data["pipelineId"]
    else:
        out["pipeline_id"] = ""
    if data.get("tagKeys") is not None:
        import capo_data_pipeline.types.string_list

        out["tag_keys"] = capo_data_pipeline.types.string_list.deserialize_aws_json_1_1(
            data["tagKeys"]
        )
    else:
        out["tag_keys"] = []
    return out
