"""Generated from Smithy shape ``com.amazonaws.costexplorer#TotalImpactFilter``."""

from typing import TYPE_CHECKING

from typing_extensions import TypedDict

if TYPE_CHECKING:
    import capo_cost_explorer.types.generic_double
    import capo_cost_explorer.types.numeric_operator


class TotalImpactFilter(TypedDict, closed=True):
    numeric_operator: "capo_cost_explorer.types.numeric_operator.NumericOperator"
    """<p>The comparing value that's used in the filter. </p>"""
    start_value: "capo_cost_explorer.types.generic_double.GenericDouble"
    """<p>The lower bound dollar value that's used in the filter. </p>"""
    end_value: "capo_cost_explorer.types.generic_double.GenericDouble"
    """<p>The upper bound dollar value that's used in the filter. </p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: TotalImpactFilter) -> dict:
    out: dict = {}
    import capo_cost_explorer.types.numeric_operator

    out["NumericOperator"] = (
        capo_cost_explorer.types.numeric_operator.serialize_aws_json_1_1(
            value["numeric_operator"]
        )
    )
    out["StartValue"] = (
        "NaN"
        if value.get("start_value", 0) != value.get("start_value", 0)
        else "Infinity"
        if value.get("start_value", 0) == float("inf")
        else "-Infinity"
        if value.get("start_value", 0) == float("-inf")
        else value.get("start_value", 0)
    )
    out["EndValue"] = (
        "NaN"
        if value.get("end_value", 0) != value.get("end_value", 0)
        else "Infinity"
        if value.get("end_value", 0) == float("inf")
        else "-Infinity"
        if value.get("end_value", 0) == float("-inf")
        else value.get("end_value", 0)
    )
    return out


def deserialize_aws_json_1_1(data: dict) -> TotalImpactFilter:
    out: TotalImpactFilter = {}  # type: ignore[typeddict-item]
    if data.get("NumericOperator") is not None:
        import capo_cost_explorer.types.numeric_operator

        out["numeric_operator"] = (
            capo_cost_explorer.types.numeric_operator.deserialize_aws_json_1_1(
                data["NumericOperator"]
            )
        )
    else:
        import typing

        out["numeric_operator"] = typing.cast(
            "capo_cost_explorer.types.numeric_operator.NumericOperator", ""
        )
    if data.get("StartValue") is not None:
        out["start_value"] = float(data["StartValue"])
    else:
        out["start_value"] = 0
    if data.get("EndValue") is not None:
        out["end_value"] = float(data["EndValue"])
    else:
        out["end_value"] = 0
    return out
