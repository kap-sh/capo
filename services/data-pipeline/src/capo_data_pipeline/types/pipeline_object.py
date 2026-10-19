"""Generated from Smithy shape ``com.amazonaws.datapipeline#PipelineObject``."""

from typing import TYPE_CHECKING

from typing_extensions import TypedDict

if TYPE_CHECKING:
    import capo_data_pipeline.types.field_list
    import capo_data_pipeline.types.id


class PipelineObject(TypedDict, closed=True):
    id: "capo_data_pipeline.types.id.id"
    """<p>The ID of the object.</p>"""
    name: "capo_data_pipeline.types.id.id"
    """<p>The name of the object.</p>"""
    fields: "capo_data_pipeline.types.field_list.fieldList"
    """<p>Key-value pairs that define the properties of the object.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: PipelineObject) -> dict:
    out: dict = {}
    out["id"] = value["id"]
    out["name"] = value["name"]
    import capo_data_pipeline.types.field_list

    out["fields"] = capo_data_pipeline.types.field_list.serialize_aws_json_1_1(
        value["fields"]
    )
    return out


def deserialize_aws_json_1_1(data: dict) -> PipelineObject:
    out: PipelineObject = {}  # type: ignore[typeddict-item]
    if data.get("id") is not None:
        out["id"] = data["id"]
    else:
        out["id"] = ""
    if data.get("name") is not None:
        out["name"] = data["name"]
    else:
        out["name"] = ""
    if data.get("fields") is not None:
        import capo_data_pipeline.types.field_list

        out["fields"] = capo_data_pipeline.types.field_list.deserialize_aws_json_1_1(
            data["fields"]
        )
    else:
        out["fields"] = []
    return out
