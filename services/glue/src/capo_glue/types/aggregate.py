"""Generated from Smithy shape ``com.amazonaws.glue#Aggregate``."""

from typing import TYPE_CHECKING

from typing_extensions import TypedDict

if TYPE_CHECKING:
    import capo_glue.types.aggregate_operations
    import capo_glue.types.glue_studio_path_list
    import capo_glue.types.node_name
    import capo_glue.types.one_input


class Aggregate(TypedDict, closed=True):
    name: "capo_glue.types.node_name.NodeName"
    """<p>The name of the transform node.</p>"""
    inputs: "capo_glue.types.one_input.OneInput"
    """<p>Specifies the fields and rows to use as inputs for the aggregate transform.</p>"""
    groups: "capo_glue.types.glue_studio_path_list.GlueStudioPathList"
    """<p>Specifies the fields to group by.</p>"""
    aggs: "capo_glue.types.aggregate_operations.AggregateOperations"
    """<p>Specifies the aggregate functions to be performed on specified fields. </p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: Aggregate) -> dict:
    out: dict = {}
    out["Name"] = value["name"]
    import capo_glue.types.one_input

    out["Inputs"] = capo_glue.types.one_input.serialize_aws_json_1_1(value["inputs"])
    import capo_glue.types.glue_studio_path_list

    out["Groups"] = capo_glue.types.glue_studio_path_list.serialize_aws_json_1_1(
        value["groups"]
    )
    import capo_glue.types.aggregate_operations

    out["Aggs"] = capo_glue.types.aggregate_operations.serialize_aws_json_1_1(
        value["aggs"]
    )
    return out


def deserialize_aws_json_1_1(data: dict) -> Aggregate:
    out: Aggregate = {}  # type: ignore[typeddict-item]
    if data.get("Name") is not None:
        out["name"] = data["Name"]
    else:
        out["name"] = ""
    if data.get("Inputs") is not None:
        import capo_glue.types.one_input

        out["inputs"] = capo_glue.types.one_input.deserialize_aws_json_1_1(
            data["Inputs"]
        )
    else:
        out["inputs"] = []
    if data.get("Groups") is not None:
        import capo_glue.types.glue_studio_path_list

        out["groups"] = capo_glue.types.glue_studio_path_list.deserialize_aws_json_1_1(
            data["Groups"]
        )
    else:
        out["groups"] = []
    if data.get("Aggs") is not None:
        import capo_glue.types.aggregate_operations

        out["aggs"] = capo_glue.types.aggregate_operations.deserialize_aws_json_1_1(
            data["Aggs"]
        )
    else:
        out["aggs"] = []
    return out
