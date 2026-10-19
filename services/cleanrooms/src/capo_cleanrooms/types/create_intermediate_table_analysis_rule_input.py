"""Generated from Smithy shape ``com.amazonaws.cleanrooms#CreateIntermediateTableAnalysisRuleInput``."""

from typing import TYPE_CHECKING

from typing_extensions import TypedDict

if TYPE_CHECKING:
    import capo_cleanrooms.types.intermediate_table_analysis_rule_policy
    import capo_cleanrooms.types.intermediate_table_analysis_rule_type
    import capo_cleanrooms.types.intermediate_table_identifier
    import capo_cleanrooms.types.membership_identifier


class CreateIntermediateTableAnalysisRuleInput(TypedDict, closed=True):
    membership_identifier: (
        "capo_cleanrooms.types.membership_identifier.MembershipIdentifier"
    )
    """<p>The unique identifier of the membership that contains the intermediate table.</p>"""
    intermediate_table_identifier: "capo_cleanrooms.types.intermediate_table_identifier.IntermediateTableIdentifier"
    """<p>The unique identifier of the intermediate table for which to create the analysis rule.</p>"""
    analysis_rule_type: "capo_cleanrooms.types.intermediate_table_analysis_rule_type.IntermediateTableAnalysisRuleType"
    """<p>The type of analysis rule to create. Currently, only <code>CUSTOM</code> is supported.</p>"""
    analysis_rule_policy: "capo_cleanrooms.types.intermediate_table_analysis_rule_policy.IntermediateTableAnalysisRulePolicy"
    """<p>The analysis rule policy to apply to the intermediate table.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: CreateIntermediateTableAnalysisRuleInput) -> dict:
    out: dict = {}
    import capo_cleanrooms.types.intermediate_table_analysis_rule_type

    out["analysisRuleType"] = (
        capo_cleanrooms.types.intermediate_table_analysis_rule_type.serialize_json(
            value["analysis_rule_type"]
        )
    )
    import capo_cleanrooms.types.intermediate_table_analysis_rule_policy

    out["analysisRulePolicy"] = (
        capo_cleanrooms.types.intermediate_table_analysis_rule_policy.serialize_json(
            value["analysis_rule_policy"]
        )
    )
    return out


def deserialize_json(data: dict) -> CreateIntermediateTableAnalysisRuleInput:
    out: CreateIntermediateTableAnalysisRuleInput = {}  # type: ignore[typeddict-item]
    if data.get("analysisRuleType") is not None:
        import capo_cleanrooms.types.intermediate_table_analysis_rule_type

        out["analysis_rule_type"] = (
            capo_cleanrooms.types.intermediate_table_analysis_rule_type.deserialize_json(
                data["analysisRuleType"]
            )
        )
    else:
        import typing

        out["analysis_rule_type"] = typing.cast(
            "capo_cleanrooms.types.intermediate_table_analysis_rule_type.IntermediateTableAnalysisRuleType",
            "",
        )
    if data.get("analysisRulePolicy") is not None:
        import capo_cleanrooms.types.intermediate_table_analysis_rule_policy

        out["analysis_rule_policy"] = (
            capo_cleanrooms.types.intermediate_table_analysis_rule_policy.deserialize_json(
                data["analysisRulePolicy"]
            )
        )
    else:
        import capo_cleanrooms.types._unknown

        out["analysis_rule_policy"] = capo_cleanrooms.types._unknown.UnknownUnionMember(
            ""
        )
    return out
