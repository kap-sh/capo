"""Generated from Smithy shape ``com.amazonaws.cleanrooms#AnalysisRuleAggregation``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_cleanrooms.types.additional_analyses
    import capo_cleanrooms.types.aggregate_column_list
    import capo_cleanrooms.types.aggregation_constraints
    import capo_cleanrooms.types.analysis_rule_column_list
    import capo_cleanrooms.types.join_operators_list
    import capo_cleanrooms.types.join_required_option
    import capo_cleanrooms.types.scalar_functions_list


class AnalysisRuleAggregation(TypedDict, closed=True):
    aggregate_columns: "capo_cleanrooms.types.aggregate_column_list.AggregateColumnList"
    """<p>The columns that query runners are allowed to use in aggregation queries.</p>"""
    join_columns: (
        "capo_cleanrooms.types.analysis_rule_column_list.AnalysisRuleColumnList"
    )
    """<p>Columns in configured table that can be used in join statements and/or as aggregate columns. They can never be outputted directly.</p>"""
    join_required: NotRequired[
        "capo_cleanrooms.types.join_required_option.JoinRequiredOption"
    ]
    """<p>Control that requires member who runs query to do a join with their configured table and/or other configured table in query.</p>"""
    allowed_join_operators: NotRequired[
        "capo_cleanrooms.types.join_operators_list.JoinOperatorsList"
    ]
    """<p>Which logical operators (if any) are to be used in an INNER JOIN match condition. Default is <code>AND</code>.</p>"""
    dimension_columns: (
        "capo_cleanrooms.types.analysis_rule_column_list.AnalysisRuleColumnList"
    )
    """<p>The columns that query runners are allowed to select, group by, or filter by.</p>"""
    scalar_functions: "capo_cleanrooms.types.scalar_functions_list.ScalarFunctionsList"
    """<p>Set of scalar functions that are allowed to be used on dimension columns and the output of aggregation of metrics.</p>"""
    output_constraints: (
        "capo_cleanrooms.types.aggregation_constraints.AggregationConstraints"
    )
    """<p>Columns that must meet a specific threshold value (after an aggregation function is applied to it) for each output row to be returned.</p>"""
    additional_analyses: NotRequired[
        "capo_cleanrooms.types.additional_analyses.AdditionalAnalyses"
    ]
    """<p> An indicator as to whether additional analyses (such as Clean Rooms ML) can be applied to the output of the direct query. </p> <p>The <code>additionalAnalyses</code> parameter is currently supported for the list analysis rule (<code>AnalysisRuleList</code>) and the custom analysis rule (<code>AnalysisRuleCustom</code>).</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: AnalysisRuleAggregation) -> dict:
    out: dict = {}
    import capo_cleanrooms.types.aggregate_column_list

    out["aggregateColumns"] = (
        capo_cleanrooms.types.aggregate_column_list.serialize_json(
            value["aggregate_columns"]
        )
    )
    import capo_cleanrooms.types.analysis_rule_column_list

    out["joinColumns"] = capo_cleanrooms.types.analysis_rule_column_list.serialize_json(
        value["join_columns"]
    )
    if "join_required" in value:
        out["joinRequired"] = value["join_required"]
    if "allowed_join_operators" in value:
        import capo_cleanrooms.types.join_operators_list

        out["allowedJoinOperators"] = (
            capo_cleanrooms.types.join_operators_list.serialize_json(
                value["allowed_join_operators"]
            )
        )
    import capo_cleanrooms.types.analysis_rule_column_list

    out["dimensionColumns"] = (
        capo_cleanrooms.types.analysis_rule_column_list.serialize_json(
            value["dimension_columns"]
        )
    )
    import capo_cleanrooms.types.scalar_functions_list

    out["scalarFunctions"] = capo_cleanrooms.types.scalar_functions_list.serialize_json(
        value["scalar_functions"]
    )
    import capo_cleanrooms.types.aggregation_constraints

    out["outputConstraints"] = (
        capo_cleanrooms.types.aggregation_constraints.serialize_json(
            value["output_constraints"]
        )
    )
    if "additional_analyses" in value:
        import capo_cleanrooms.types.additional_analyses

        out["additionalAnalyses"] = (
            capo_cleanrooms.types.additional_analyses.serialize_json(
                value["additional_analyses"]
            )
        )
    return out


def deserialize_json(data: dict) -> AnalysisRuleAggregation:
    out: AnalysisRuleAggregation = {}  # type: ignore[typeddict-item]
    if data.get("aggregateColumns") is not None:
        import capo_cleanrooms.types.aggregate_column_list

        out["aggregate_columns"] = (
            capo_cleanrooms.types.aggregate_column_list.deserialize_json(
                data["aggregateColumns"]
            )
        )
    else:
        out["aggregate_columns"] = []
    if data.get("joinColumns") is not None:
        import capo_cleanrooms.types.analysis_rule_column_list

        out["join_columns"] = (
            capo_cleanrooms.types.analysis_rule_column_list.deserialize_json(
                data["joinColumns"]
            )
        )
    else:
        out["join_columns"] = []
    if data.get("joinRequired") is not None:
        out["join_required"] = data["joinRequired"]
    if data.get("allowedJoinOperators") is not None:
        import capo_cleanrooms.types.join_operators_list

        out["allowed_join_operators"] = (
            capo_cleanrooms.types.join_operators_list.deserialize_json(
                data["allowedJoinOperators"]
            )
        )
    if data.get("dimensionColumns") is not None:
        import capo_cleanrooms.types.analysis_rule_column_list

        out["dimension_columns"] = (
            capo_cleanrooms.types.analysis_rule_column_list.deserialize_json(
                data["dimensionColumns"]
            )
        )
    else:
        out["dimension_columns"] = []
    if data.get("scalarFunctions") is not None:
        import capo_cleanrooms.types.scalar_functions_list

        out["scalar_functions"] = (
            capo_cleanrooms.types.scalar_functions_list.deserialize_json(
                data["scalarFunctions"]
            )
        )
    else:
        out["scalar_functions"] = []
    if data.get("outputConstraints") is not None:
        import capo_cleanrooms.types.aggregation_constraints

        out["output_constraints"] = (
            capo_cleanrooms.types.aggregation_constraints.deserialize_json(
                data["outputConstraints"]
            )
        )
    else:
        out["output_constraints"] = []
    if data.get("additionalAnalyses") is not None:
        import capo_cleanrooms.types.additional_analyses

        out["additional_analyses"] = (
            capo_cleanrooms.types.additional_analyses.deserialize_json(
                data["additionalAnalyses"]
            )
        )
    return out
