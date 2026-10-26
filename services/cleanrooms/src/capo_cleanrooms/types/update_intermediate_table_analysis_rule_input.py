"""Generated from Smithy shape ``com.amazonaws.cleanrooms#UpdateIntermediateTableAnalysisRuleInput``."""

from typing import TYPE_CHECKING

from typing_extensions import TypedDict

if TYPE_CHECKING:
    import capo_cleanrooms.types.intermediate_table_analysis_rule_policy
    import capo_cleanrooms.types.intermediate_table_analysis_rule_type
    import capo_cleanrooms.types.intermediate_table_identifier
    import capo_cleanrooms.types.membership_identifier


class UpdateIntermediateTableAnalysisRuleInput(TypedDict, closed=True):
    membership_identifier: (
        "capo_cleanrooms.types.membership_identifier.MembershipIdentifier"
    )
    """<p>The unique identifier of the membership that contains the intermediate table.</p>"""
    intermediate_table_identifier: "capo_cleanrooms.types.intermediate_table_identifier.IntermediateTableIdentifier"
    """<p>The unique identifier of the intermediate table for which to update the analysis rule.</p>"""
    analysis_rule_type: "capo_cleanrooms.types.intermediate_table_analysis_rule_type.IntermediateTableAnalysisRuleType"
    """<p>The type of analysis rule to update. Currently, only <code>CUSTOM</code> is supported.</p>"""
    analysis_rule_policy: "capo_cleanrooms.types.intermediate_table_analysis_rule_policy.IntermediateTableAnalysisRulePolicy"
    """<p>The updated analysis rule policy for the intermediate table.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: UpdateIntermediateTableAnalysisRuleInput) -> dict:
    out: dict = {}
    import capo_cleanrooms.types.intermediate_table_analysis_rule_policy

    out["analysisRulePolicy"] = (
        capo_cleanrooms.types.intermediate_table_analysis_rule_policy.serialize_json(
            value["analysis_rule_policy"]
        )
    )
    return out


def deserialize_json(data: dict) -> UpdateIntermediateTableAnalysisRuleInput:
    out: UpdateIntermediateTableAnalysisRuleInput = {}  # type: ignore[typeddict-item]
    if data.get("analysisRulePolicy") is not None:
        import capo_cleanrooms.types.intermediate_table_analysis_rule_policy

        out["analysis_rule_policy"] = (
            capo_cleanrooms.types.intermediate_table_analysis_rule_policy.deserialize_json(
                data["analysisRulePolicy"]
            )
        )
    else:
        out["analysis_rule_policy"] = {"$unknown": {"name": ""}}
    return out
