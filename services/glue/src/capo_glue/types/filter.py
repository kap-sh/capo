"""Generated from Smithy shape ``com.amazonaws.glue#Filter``."""

from typing import TYPE_CHECKING

from typing_extensions import TypedDict

if TYPE_CHECKING:
    import capo_glue.types.filter_expressions
    import capo_glue.types.filter_logical_operator
    import capo_glue.types.node_name
    import capo_glue.types.one_input


class Filter(TypedDict, closed=True):
    name: "capo_glue.types.node_name.NodeName"
    """<p>The name of the transform node.</p>"""
    inputs: "capo_glue.types.one_input.OneInput"
    """<p>The data inputs identified by their node names.</p>"""
    logical_operator: "capo_glue.types.filter_logical_operator.FilterLogicalOperator"
    """<p>The operator used to filter rows by comparing the key value to a specified value.</p>"""
    filters: "capo_glue.types.filter_expressions.FilterExpressions"
    """<p>Specifies a filter expression.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: Filter) -> dict:
    out: dict = {}
    out["Name"] = value["name"]
    import capo_glue.types.one_input

    out["Inputs"] = capo_glue.types.one_input.serialize_aws_json_1_1(value["inputs"])
    import capo_glue.types.filter_logical_operator

    out["LogicalOperator"] = (
        capo_glue.types.filter_logical_operator.serialize_aws_json_1_1(
            value["logical_operator"]
        )
    )
    import capo_glue.types.filter_expressions

    out["Filters"] = capo_glue.types.filter_expressions.serialize_aws_json_1_1(
        value["filters"]
    )
    return out


def deserialize_aws_json_1_1(data: dict) -> Filter:
    out: Filter = {}  # type: ignore[typeddict-item]
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
    if data.get("LogicalOperator") is not None:
        import capo_glue.types.filter_logical_operator

        out["logical_operator"] = (
            capo_glue.types.filter_logical_operator.deserialize_aws_json_1_1(
                data["LogicalOperator"]
            )
        )
    else:
        import typing

        out["logical_operator"] = typing.cast(
            "capo_glue.types.filter_logical_operator.FilterLogicalOperator", ""
        )
    if data.get("Filters") is not None:
        import capo_glue.types.filter_expressions

        out["filters"] = capo_glue.types.filter_expressions.deserialize_aws_json_1_1(
            data["Filters"]
        )
    else:
        out["filters"] = []
    return out
