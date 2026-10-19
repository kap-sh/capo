"""Generated from Smithy shape ``com.amazonaws.budgets#ExpressionDimensionValues``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_budgets.types.dimension
    import capo_budgets.types.match_options
    import capo_budgets.types.values


class ExpressionDimensionValues(TypedDict, closed=True):
    key: "capo_budgets.types.dimension.Dimension"
    """<p>The name of the dimension that you want to filter on.</p>"""
    values: "capo_budgets.types.values.Values"
    """<p>The metadata values you can specify to filter upon, so that the results all match at least one of the specified values.</p>"""
    match_options: NotRequired["capo_budgets.types.match_options.MatchOptions"]
    """<p>The match options that you can use to filter your results. You can specify only one of these values in the array.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: ExpressionDimensionValues) -> dict:
    out: dict = {}
    import capo_budgets.types.dimension

    out["Key"] = capo_budgets.types.dimension.serialize_aws_json_1_1(value["key"])
    import capo_budgets.types.values

    out["Values"] = capo_budgets.types.values.serialize_aws_json_1_1(value["values"])
    if "match_options" in value:
        import capo_budgets.types.match_options

        out["MatchOptions"] = capo_budgets.types.match_options.serialize_aws_json_1_1(
            value["match_options"]
        )
    return out


def deserialize_aws_json_1_1(data: dict) -> ExpressionDimensionValues:
    out: ExpressionDimensionValues = {}  # type: ignore[typeddict-item]
    if data.get("Key") is not None:
        import capo_budgets.types.dimension

        out["key"] = capo_budgets.types.dimension.deserialize_aws_json_1_1(data["Key"])
    else:
        import typing

        out["key"] = typing.cast("capo_budgets.types.dimension.Dimension", "")
    if data.get("Values") is not None:
        import capo_budgets.types.values

        out["values"] = capo_budgets.types.values.deserialize_aws_json_1_1(
            data["Values"]
        )
    else:
        out["values"] = []
    if data.get("MatchOptions") is not None:
        import capo_budgets.types.match_options

        out["match_options"] = (
            capo_budgets.types.match_options.deserialize_aws_json_1_1(
                data["MatchOptions"]
            )
        )
    return out
