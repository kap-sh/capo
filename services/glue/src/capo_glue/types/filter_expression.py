"""Generated from Smithy shape ``com.amazonaws.glue#FilterExpression``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_glue.types.boxed_boolean
    import capo_glue.types.filter_operation
    import capo_glue.types.filter_values


class FilterExpression(TypedDict, closed=True):
    operation: "capo_glue.types.filter_operation.FilterOperation"
    """<p>The type of operation to perform in the expression.</p>"""
    negated: NotRequired["capo_glue.types.boxed_boolean.BoxedBoolean"]
    """<p>Whether the expression is to be negated.</p>"""
    values: "capo_glue.types.filter_values.FilterValues"
    """<p>A list of filter values.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: FilterExpression) -> dict:
    out: dict = {}
    import capo_glue.types.filter_operation

    out["Operation"] = capo_glue.types.filter_operation.serialize_aws_json_1_1(
        value["operation"]
    )
    if "negated" in value:
        out["Negated"] = value["negated"]
    import capo_glue.types.filter_values

    out["Values"] = capo_glue.types.filter_values.serialize_aws_json_1_1(
        value["values"]
    )
    return out


def deserialize_aws_json_1_1(data: dict) -> FilterExpression:
    out: FilterExpression = {}  # type: ignore[typeddict-item]
    if data.get("Operation") is not None:
        import capo_glue.types.filter_operation

        out["operation"] = capo_glue.types.filter_operation.deserialize_aws_json_1_1(
            data["Operation"]
        )
    else:
        import typing

        out["operation"] = typing.cast(
            "capo_glue.types.filter_operation.FilterOperation", ""
        )
    if data.get("Negated") is not None:
        out["negated"] = data["Negated"]
    if data.get("Values") is not None:
        import capo_glue.types.filter_values

        out["values"] = capo_glue.types.filter_values.deserialize_aws_json_1_1(
            data["Values"]
        )
    else:
        out["values"] = []
    return out
