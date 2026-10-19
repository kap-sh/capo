"""Generated from Smithy shape ``com.amazonaws.cleanrooms#AggregationThreshold``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_cleanrooms.types.aggregation_threshold_type
    import capo_cleanrooms.types.allowed_aggregate_expression_type
    import capo_cleanrooms.types.analysis_rule_column_list
    import capo_cleanrooms.types.output_column_threshold_list


class AggregationThreshold(TypedDict, closed=True):
    identity_columns: (
        "capo_cleanrooms.types.analysis_rule_column_list.AnalysisRuleColumnList"
    )
    """<p>The identity column, such as <code>user_id</code>, whose distinct values Clean Rooms counts to enforce minimum aggregation thresholds. Currently, you can specify only one column, and its data type must be string, varchar, or char.</p>"""
    minimum_identity_count: "int"
    """<p>The minimum number of distinct identities that each query output group must represent. This threshold applies to all output columns in the table. To override this threshold for a specific column, use <code>outputColumnThresholds</code>.</p>"""
    type: "capo_cleanrooms.types.aggregation_threshold_type.AggregationThresholdType"
    """<p>The type of aggregation that the threshold enforces. Currently, the only supported value is <code>COUNT_DISTINCT</code>, which counts the distinct values in the identity column.</p>"""
    output_column_thresholds: NotRequired[
        "capo_cleanrooms.types.output_column_threshold_list.OutputColumnThresholdList"
    ]
    """<p>The per-column overrides of <code>minimumIdentityCount</code>. An output column without an override uses <code>minimumIdentityCount</code>.</p>"""
    allowed_aggregate_expression_type: "capo_cleanrooms.types.allowed_aggregate_expression_type.AllowedAggregateExpressionType"
    """<p>Specifies whether a query can aggregate a transformed column. This applies to the arguments of both aggregate and window functions. Valid values are:</p> <p> <code>COLUMNS_ONLY</code> – A query can aggregate only a direct column reference, such as <code>SUM(amount)</code>, or a constant. Clean Rooms rejects a query that transforms a column and then aggregates it, such as <code>SUM(amount * 2)</code> or <code>SUM(ROUND(amount))</code>.</p> <p> <code>ANY_EXPRESSION</code> – A query can aggregate any expression. This includes arithmetic, such as <code>SUM(price * quantity)</code>; a cast, such as <code>SUM(CAST(amount AS DECIMAL))</code>; a nested function call, such as <code>SUM(COALESCE(amount, 0))</code>; and a conditional, such as <code>SUM(CASE WHEN region = 'EU' THEN amount ELSE 0 END)</code>.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: AggregationThreshold) -> dict:
    out: dict = {}
    import capo_cleanrooms.types.analysis_rule_column_list

    out["identityColumns"] = (
        capo_cleanrooms.types.analysis_rule_column_list.serialize_json(
            value["identity_columns"]
        )
    )
    out["minimumIdentityCount"] = value["minimum_identity_count"]
    import capo_cleanrooms.types.aggregation_threshold_type

    out["type"] = capo_cleanrooms.types.aggregation_threshold_type.serialize_json(
        value["type"]
    )
    if "output_column_thresholds" in value:
        import capo_cleanrooms.types.output_column_threshold_list

        out["outputColumnThresholds"] = (
            capo_cleanrooms.types.output_column_threshold_list.serialize_json(
                value["output_column_thresholds"]
            )
        )
    import capo_cleanrooms.types.allowed_aggregate_expression_type

    out["allowedAggregateExpressionType"] = (
        capo_cleanrooms.types.allowed_aggregate_expression_type.serialize_json(
            value["allowed_aggregate_expression_type"]
        )
    )
    return out


def deserialize_json(data: dict) -> AggregationThreshold:
    out: AggregationThreshold = {}  # type: ignore[typeddict-item]
    if data.get("identityColumns") is not None:
        import capo_cleanrooms.types.analysis_rule_column_list

        out["identity_columns"] = (
            capo_cleanrooms.types.analysis_rule_column_list.deserialize_json(
                data["identityColumns"]
            )
        )
    else:
        out["identity_columns"] = []
    if data.get("minimumIdentityCount") is not None:
        out["minimum_identity_count"] = data["minimumIdentityCount"]
    else:
        out["minimum_identity_count"] = 0
    if data.get("type") is not None:
        import capo_cleanrooms.types.aggregation_threshold_type

        out["type"] = capo_cleanrooms.types.aggregation_threshold_type.deserialize_json(
            data["type"]
        )
    else:
        import typing

        out["type"] = typing.cast(
            "capo_cleanrooms.types.aggregation_threshold_type.AggregationThresholdType",
            "",
        )
    if data.get("outputColumnThresholds") is not None:
        import capo_cleanrooms.types.output_column_threshold_list

        out["output_column_thresholds"] = (
            capo_cleanrooms.types.output_column_threshold_list.deserialize_json(
                data["outputColumnThresholds"]
            )
        )
    if data.get("allowedAggregateExpressionType") is not None:
        import capo_cleanrooms.types.allowed_aggregate_expression_type

        out["allowed_aggregate_expression_type"] = (
            capo_cleanrooms.types.allowed_aggregate_expression_type.deserialize_json(
                data["allowedAggregateExpressionType"]
            )
        )
    else:
        import typing

        out["allowed_aggregate_expression_type"] = typing.cast(
            "capo_cleanrooms.types.allowed_aggregate_expression_type.AllowedAggregateExpressionType",
            "",
        )
    return out
