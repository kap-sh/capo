"""Generated from Smithy shape ``com.amazonaws.cleanrooms#UpdateConfiguredTableAnalysisRuleInput``."""

from typing import TYPE_CHECKING

from typing_extensions import TypedDict

if TYPE_CHECKING:
    import capo_cleanrooms.types.configured_table_analysis_rule_policy
    import capo_cleanrooms.types.configured_table_analysis_rule_type
    import capo_cleanrooms.types.configured_table_identifier


class UpdateConfiguredTableAnalysisRuleInput(TypedDict, closed=True):
    configured_table_identifier: (
        "capo_cleanrooms.types.configured_table_identifier.ConfiguredTableIdentifier"
    )
    """<p>The unique identifier for the configured table that the analysis rule applies to. Currently accepts the configured table ID.</p>"""
    analysis_rule_type: "capo_cleanrooms.types.configured_table_analysis_rule_type.ConfiguredTableAnalysisRuleType"
    """<p>The analysis rule type to be updated. Configured table analysis rules are uniquely identified by their configured table identifier and analysis rule type.</p>"""
    analysis_rule_policy: "capo_cleanrooms.types.configured_table_analysis_rule_policy.ConfiguredTableAnalysisRulePolicy"
    """<p>The new analysis rule policy for the configured table analysis rule.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: UpdateConfiguredTableAnalysisRuleInput) -> dict:
    out: dict = {}
    import capo_cleanrooms.types.configured_table_analysis_rule_policy

    out["analysisRulePolicy"] = (
        capo_cleanrooms.types.configured_table_analysis_rule_policy.serialize_json(
            value["analysis_rule_policy"]
        )
    )
    return out


def deserialize_json(data: dict) -> UpdateConfiguredTableAnalysisRuleInput:
    out: UpdateConfiguredTableAnalysisRuleInput = {}  # type: ignore[typeddict-item]
    if data.get("analysisRulePolicy") is not None:
        import capo_cleanrooms.types.configured_table_analysis_rule_policy

        out["analysis_rule_policy"] = (
            capo_cleanrooms.types.configured_table_analysis_rule_policy.deserialize_json(
                data["analysisRulePolicy"]
            )
        )
    else:
        out["analysis_rule_policy"] = {"$unknown": {"name": ""}}
    return out
