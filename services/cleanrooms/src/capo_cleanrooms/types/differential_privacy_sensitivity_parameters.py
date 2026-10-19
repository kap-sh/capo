"""Generated from Smithy shape ``com.amazonaws.cleanrooms#DifferentialPrivacySensitivityParameters``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_cleanrooms.types.differential_privacy_aggregation_expression
    import capo_cleanrooms.types.differential_privacy_aggregation_type


class DifferentialPrivacySensitivityParameters(TypedDict, closed=True):
    aggregation_type: "capo_cleanrooms.types.differential_privacy_aggregation_type.DifferentialPrivacyAggregationType"
    """<p>The type of aggregation function that was run.</p>"""
    aggregation_expression: "capo_cleanrooms.types.differential_privacy_aggregation_expression.DifferentialPrivacyAggregationExpression"
    """<p>The aggregation expression that was run.</p>"""
    user_contribution_limit: "int"
    """<p>The maximum number of rows contributed by a user in a SQL query.</p>"""
    min_column_value: NotRequired["float"]
    """<p>The lower bound of the aggregation expression.</p>"""
    max_column_value: NotRequired["float"]
    """<p>The upper bound of the aggregation expression.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: DifferentialPrivacySensitivityParameters) -> dict:
    out: dict = {}
    import capo_cleanrooms.types.differential_privacy_aggregation_type

    out["aggregationType"] = (
        capo_cleanrooms.types.differential_privacy_aggregation_type.serialize_json(
            value["aggregation_type"]
        )
    )
    out["aggregationExpression"] = value["aggregation_expression"]
    out["userContributionLimit"] = value["user_contribution_limit"]
    if "min_column_value" in value:
        out["minColumnValue"] = (
            "NaN"
            if value["min_column_value"] != value["min_column_value"]
            else "Infinity"
            if value["min_column_value"] == float("inf")
            else "-Infinity"
            if value["min_column_value"] == float("-inf")
            else value["min_column_value"]
        )
    if "max_column_value" in value:
        out["maxColumnValue"] = (
            "NaN"
            if value["max_column_value"] != value["max_column_value"]
            else "Infinity"
            if value["max_column_value"] == float("inf")
            else "-Infinity"
            if value["max_column_value"] == float("-inf")
            else value["max_column_value"]
        )
    return out


def deserialize_json(data: dict) -> DifferentialPrivacySensitivityParameters:
    out: DifferentialPrivacySensitivityParameters = {}  # type: ignore[typeddict-item]
    if data.get("aggregationType") is not None:
        import capo_cleanrooms.types.differential_privacy_aggregation_type

        out["aggregation_type"] = (
            capo_cleanrooms.types.differential_privacy_aggregation_type.deserialize_json(
                data["aggregationType"]
            )
        )
    else:
        import typing

        out["aggregation_type"] = typing.cast(
            "capo_cleanrooms.types.differential_privacy_aggregation_type.DifferentialPrivacyAggregationType",
            "",
        )
    if data.get("aggregationExpression") is not None:
        out["aggregation_expression"] = data["aggregationExpression"]
    else:
        out["aggregation_expression"] = ""
    if data.get("userContributionLimit") is not None:
        out["user_contribution_limit"] = data["userContributionLimit"]
    else:
        out["user_contribution_limit"] = 0
    if data.get("minColumnValue") is not None:
        out["min_column_value"] = float(data["minColumnValue"])
    if data.get("maxColumnValue") is not None:
        out["max_column_value"] = float(data["maxColumnValue"])
    return out
