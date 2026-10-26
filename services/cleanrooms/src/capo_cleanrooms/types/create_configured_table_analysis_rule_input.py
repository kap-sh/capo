"""Generated from Smithy shape ``com.amazonaws.cleanrooms#CreateConfiguredTableAnalysisRuleInput``."""

from typing import TYPE_CHECKING

from typing_extensions import TypedDict

if TYPE_CHECKING:
    import capo_cleanrooms.types.configured_table_analysis_rule_policy
    import capo_cleanrooms.types.configured_table_analysis_rule_type
    import capo_cleanrooms.types.configured_table_identifier


class CreateConfiguredTableAnalysisRuleInput(TypedDict, closed=True):
    configured_table_identifier: (
        "capo_cleanrooms.types.configured_table_identifier.ConfiguredTableIdentifier"
    )
    """<p>The identifier for the configured table to create the analysis rule for. Currently accepts the configured table ID. </p>"""
    analysis_rule_type: "capo_cleanrooms.types.configured_table_analysis_rule_type.ConfiguredTableAnalysisRuleType"
    """<p>The type of analysis rule.</p>"""
    analysis_rule_policy: "capo_cleanrooms.types.configured_table_analysis_rule_policy.ConfiguredTableAnalysisRulePolicy"
    """<p>The analysis rule policy that was created for the configured table.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: CreateConfiguredTableAnalysisRuleInput) -> dict:
    out: dict = {}
    import capo_cleanrooms.types.configured_table_analysis_rule_type

    out["analysisRuleType"] = (
        capo_cleanrooms.types.configured_table_analysis_rule_type.serialize_json(
            value["analysis_rule_type"]
        )
    )
    import capo_cleanrooms.types.configured_table_analysis_rule_policy

    out["analysisRulePolicy"] = (
        capo_cleanrooms.types.configured_table_analysis_rule_policy.serialize_json(
            value["analysis_rule_policy"]
        )
    )
    return out


def deserialize_json(data: dict) -> CreateConfiguredTableAnalysisRuleInput:
    out: CreateConfiguredTableAnalysisRuleInput = {}  # type: ignore[typeddict-item]
    if data.get("analysisRuleType") is not None:
        import capo_cleanrooms.types.configured_table_analysis_rule_type

        out["analysis_rule_type"] = (
            capo_cleanrooms.types.configured_table_analysis_rule_type.deserialize_json(
                data["analysisRuleType"]
            )
        )
    else:
        import typing

        out["analysis_rule_type"] = typing.cast(
            "capo_cleanrooms.types.configured_table_analysis_rule_type.ConfiguredTableAnalysisRuleType",
            "",
        )
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
