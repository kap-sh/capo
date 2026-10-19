"""Generated from Smithy shape ``com.amazonaws.datapipeline#SetStatusInput``."""

from typing import TYPE_CHECKING

from typing_extensions import TypedDict

if TYPE_CHECKING:
    import capo_data_pipeline.types.id
    import capo_data_pipeline.types.id_list
    import capo_data_pipeline.types.string


class SetStatusInput(TypedDict, closed=True):
    pipeline_id: "capo_data_pipeline.types.id.id"
    """<p>The ID of the pipeline that contains the objects.</p>"""
    object_ids: "capo_data_pipeline.types.id_list.idList"
    """<p>The IDs of the objects. The corresponding objects can be either physical or components, but not a mix of both types.</p>"""
    status: "capo_data_pipeline.types.string.string"
    """<p>The status to be set on all the objects specified in <code>objectIds</code>. For components, use <code>PAUSE</code> or <code>RESUME</code>. For instances, use <code>TRY_CANCEL</code>, <code>RERUN</code>, or <code>MARK_FINISHED</code>.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: SetStatusInput) -> dict:
    out: dict = {}
    out["pipelineId"] = value["pipeline_id"]
    import capo_data_pipeline.types.id_list

    out["objectIds"] = capo_data_pipeline.types.id_list.serialize_aws_json_1_1(
        value["object_ids"]
    )
    out["status"] = value["status"]
    return out


def deserialize_aws_json_1_1(data: dict) -> SetStatusInput:
    out: SetStatusInput = {}  # type: ignore[typeddict-item]
    if data.get("pipelineId") is not None:
        out["pipeline_id"] = data["pipelineId"]
    else:
        out["pipeline_id"] = ""
    if data.get("objectIds") is not None:
        import capo_data_pipeline.types.id_list

        out["object_ids"] = capo_data_pipeline.types.id_list.deserialize_aws_json_1_1(
            data["objectIds"]
        )
    else:
        out["object_ids"] = []
    if data.get("status") is not None:
        out["status"] = data["status"]
    else:
        out["status"] = ""
    return out
