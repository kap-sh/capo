"""Generated from Smithy shape ``com.amazonaws.quicksight#TopicIRMetric``."""

from typing import TYPE_CHECKING, Any

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_quicksight.types.agg_function
    import capo_quicksight.types.calculated_field_reference_list
    import capo_quicksight.types.display_format
    import capo_quicksight.types.display_format_options
    import capo_quicksight.types.expression
    import capo_quicksight.types.identifier
    import capo_quicksight.types.named_entity_ref
    import capo_quicksight.types.operand_list
    import capo_quicksight.types.topic_ir_comparison_method


class TopicIRMetric(TypedDict, closed=True):
    metric_id: NotRequired["capo_quicksight.types.identifier.Identifier"]
    """<p>The metric ID for the <code>TopicIRMetric</code>.</p>"""
    function: NotRequired["capo_quicksight.types.agg_function.AggFunction"]
    """<p>The function for the <code>TopicIRMetric</code>.</p>"""
    operands: NotRequired["capo_quicksight.types.operand_list.OperandList"]
    """<p>The operands for the <code>TopicIRMetric</code>.</p>"""
    comparison_method: NotRequired[
        "capo_quicksight.types.topic_ir_comparison_method.TopicIRComparisonMethod"
    ]
    """<p>The comparison method for the <code>TopicIRMetric</code>.</p>"""
    expression: NotRequired["capo_quicksight.types.expression.Expression"]
    """<p>The expression for the <code>TopicIRMetric</code>.</p>"""
    calculated_field_references: NotRequired[
        "capo_quicksight.types.calculated_field_reference_list.CalculatedFieldReferenceList"
    ]
    """<p>The calculated field references for the <code>TopicIRMetric</code>.</p>"""
    display_format: NotRequired["capo_quicksight.types.display_format.DisplayFormat"]
    """<p>The display format for the <code>TopicIRMetric</code>.</p>"""
    display_format_options: NotRequired[
        "capo_quicksight.types.display_format_options.DisplayFormatOptions"
    ]
    named_entity: NotRequired["capo_quicksight.types.named_entity_ref.NamedEntityRef"]
    """<p>The named entity for the <code>TopicIRMetric</code>.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: TopicIRMetric) -> dict:
    out: dict = {}
    if "metric_id" in value:
        import capo_quicksight.types.identifier

        out["MetricId"] = capo_quicksight.types.identifier.serialize_json(
            value["metric_id"]
        )
    if "function" in value:
        import capo_quicksight.types.agg_function

        out["Function"] = capo_quicksight.types.agg_function.serialize_json(
            value["function"]
        )
    if "operands" in value:
        import capo_quicksight.types.operand_list

        out["Operands"] = capo_quicksight.types.operand_list.serialize_json(
            value["operands"]
        )
    if "comparison_method" in value:
        import capo_quicksight.types.topic_ir_comparison_method

        out["ComparisonMethod"] = (
            capo_quicksight.types.topic_ir_comparison_method.serialize_json(
                value["comparison_method"]
            )
        )
    if "expression" in value:
        out["Expression"] = value["expression"]
    if "calculated_field_references" in value:
        import capo_quicksight.types.calculated_field_reference_list

        out["CalculatedFieldReferences"] = (
            capo_quicksight.types.calculated_field_reference_list.serialize_json(
                value["calculated_field_references"]
            )
        )
    if "display_format" in value:
        import capo_quicksight.types.display_format

        out["DisplayFormat"] = capo_quicksight.types.display_format.serialize_json(
            value["display_format"]
        )
    if "display_format_options" in value:
        import capo_quicksight.types.display_format_options

        out["DisplayFormatOptions"] = (
            capo_quicksight.types.display_format_options.serialize_json(
                value["display_format_options"]
            )
        )
    if "named_entity" in value:
        import capo_quicksight.types.named_entity_ref

        out["NamedEntity"] = capo_quicksight.types.named_entity_ref.serialize_json(
            value["named_entity"]
        )
    return out


def deserialize_json(data: dict) -> TopicIRMetric:
    out: TopicIRMetric = {}  # type: ignore[typeddict-item]
    if data.get("MetricId") is not None:
        import capo_quicksight.types.identifier

        out["metric_id"] = capo_quicksight.types.identifier.deserialize_json(
            data["MetricId"]
        )
    if data.get("Function") is not None:
        import capo_quicksight.types.agg_function

        out["function"] = capo_quicksight.types.agg_function.deserialize_json(
            data["Function"]
        )
    if data.get("Operands") is not None:
        import capo_quicksight.types.operand_list

        out["operands"] = capo_quicksight.types.operand_list.deserialize_json(
            data["Operands"]
        )
    if data.get("ComparisonMethod") is not None:
        import capo_quicksight.types.topic_ir_comparison_method

        out["comparison_method"] = (
            capo_quicksight.types.topic_ir_comparison_method.deserialize_json(
                data["ComparisonMethod"]
            )
        )
    if data.get("Expression") is not None:
        out["expression"] = data["Expression"]
    if data.get("CalculatedFieldReferences") is not None:
        import capo_quicksight.types.calculated_field_reference_list

        out["calculated_field_references"] = (
            capo_quicksight.types.calculated_field_reference_list.deserialize_json(
                data["CalculatedFieldReferences"]
            )
        )
    if data.get("DisplayFormat") is not None:
        import capo_quicksight.types.display_format

        out["display_format"] = capo_quicksight.types.display_format.deserialize_json(
            data["DisplayFormat"]
        )
    if data.get("DisplayFormatOptions") is not None:
        import capo_quicksight.types.display_format_options

        out["display_format_options"] = (
            capo_quicksight.types.display_format_options.deserialize_json(
                data["DisplayFormatOptions"]
            )
        )
    if data.get("NamedEntity") is not None:
        import capo_quicksight.types.named_entity_ref

        out["named_entity"] = capo_quicksight.types.named_entity_ref.deserialize_json(
            data["NamedEntity"]
        )
    return out


def redact_sensitive(value: TopicIRMetric) -> dict[str, Any]:
    out: dict[str, Any] = dict(value)
    if "expression" in value:
        out["expression"] = "*** Sensitive Data Redacted ***"
    return out
