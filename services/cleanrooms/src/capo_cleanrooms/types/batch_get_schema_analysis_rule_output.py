"""Generated from Smithy shape ``com.amazonaws.cleanrooms#BatchGetSchemaAnalysisRuleOutput``."""

from typing import TYPE_CHECKING

from typing_extensions import TypedDict

if TYPE_CHECKING:
    import capo_cleanrooms.types.batch_get_schema_analysis_rule_error_list
    import capo_cleanrooms.types.schema_analysis_rule_list


class BatchGetSchemaAnalysisRuleOutput(TypedDict, closed=True):
    analysis_rules: (
        "capo_cleanrooms.types.schema_analysis_rule_list.SchemaAnalysisRuleList"
    )
    """<p>The retrieved list of analysis rules.</p>"""
    errors: "capo_cleanrooms.types.batch_get_schema_analysis_rule_error_list.BatchGetSchemaAnalysisRuleErrorList"
    """<p>Error reasons for schemas that could not be retrieved. One error is returned for every schema that could not be retrieved.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: BatchGetSchemaAnalysisRuleOutput) -> dict:
    out: dict = {}
    import capo_cleanrooms.types.schema_analysis_rule_list

    out["analysisRules"] = (
        capo_cleanrooms.types.schema_analysis_rule_list.serialize_json(
            value["analysis_rules"]
        )
    )
    import capo_cleanrooms.types.batch_get_schema_analysis_rule_error_list

    out["errors"] = (
        capo_cleanrooms.types.batch_get_schema_analysis_rule_error_list.serialize_json(
            value["errors"]
        )
    )
    return out


def deserialize_json(data: dict) -> BatchGetSchemaAnalysisRuleOutput:
    out: BatchGetSchemaAnalysisRuleOutput = {}  # type: ignore[typeddict-item]
    if data.get("analysisRules") is not None:
        import capo_cleanrooms.types.schema_analysis_rule_list

        out["analysis_rules"] = (
            capo_cleanrooms.types.schema_analysis_rule_list.deserialize_json(
                data["analysisRules"]
            )
        )
    else:
        out["analysis_rules"] = []
    if data.get("errors") is not None:
        import capo_cleanrooms.types.batch_get_schema_analysis_rule_error_list

        out["errors"] = (
            capo_cleanrooms.types.batch_get_schema_analysis_rule_error_list.deserialize_json(
                data["errors"]
            )
        )
    else:
        out["errors"] = []
    return out
