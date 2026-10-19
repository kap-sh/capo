"""Generated from Smithy shape ``com.amazonaws.cleanrooms#CreateConfiguredTableAssociationAnalysisRuleInput``."""

from typing import TYPE_CHECKING

from typing_extensions import TypedDict

if TYPE_CHECKING:
    import capo_cleanrooms.types.configured_table_association_analysis_rule_policy
    import capo_cleanrooms.types.configured_table_association_analysis_rule_type
    import capo_cleanrooms.types.configured_table_association_identifier
    import capo_cleanrooms.types.membership_identifier


class CreateConfiguredTableAssociationAnalysisRuleInput(TypedDict, closed=True):
    membership_identifier: (
        "capo_cleanrooms.types.membership_identifier.MembershipIdentifier"
    )
    """<p> A unique identifier for the membership that the configured table association belongs to. Currently accepts the membership ID.</p>"""
    configured_table_association_identifier: "capo_cleanrooms.types.configured_table_association_identifier.ConfiguredTableAssociationIdentifier"
    """<p> The unique ID for the configured table association. Currently accepts the configured table association ID.</p>"""
    analysis_rule_type: "capo_cleanrooms.types.configured_table_association_analysis_rule_type.ConfiguredTableAssociationAnalysisRuleType"
    """<p> The type of analysis rule.</p>"""
    analysis_rule_policy: "capo_cleanrooms.types.configured_table_association_analysis_rule_policy.ConfiguredTableAssociationAnalysisRulePolicy"
    """<p>The analysis rule policy that was created for the configured table association.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: CreateConfiguredTableAssociationAnalysisRuleInput) -> dict:
    out: dict = {}
    import capo_cleanrooms.types.configured_table_association_analysis_rule_type

    out["analysisRuleType"] = (
        capo_cleanrooms.types.configured_table_association_analysis_rule_type.serialize_json(
            value["analysis_rule_type"]
        )
    )
    import capo_cleanrooms.types.configured_table_association_analysis_rule_policy

    out["analysisRulePolicy"] = (
        capo_cleanrooms.types.configured_table_association_analysis_rule_policy.serialize_json(
            value["analysis_rule_policy"]
        )
    )
    return out


def deserialize_json(data: dict) -> CreateConfiguredTableAssociationAnalysisRuleInput:
    out: CreateConfiguredTableAssociationAnalysisRuleInput = {}  # type: ignore[typeddict-item]
    if data.get("analysisRuleType") is not None:
        import capo_cleanrooms.types.configured_table_association_analysis_rule_type

        out["analysis_rule_type"] = (
            capo_cleanrooms.types.configured_table_association_analysis_rule_type.deserialize_json(
                data["analysisRuleType"]
            )
        )
    else:
        import typing

        out["analysis_rule_type"] = typing.cast(
            "capo_cleanrooms.types.configured_table_association_analysis_rule_type.ConfiguredTableAssociationAnalysisRuleType",
            "",
        )
    if data.get("analysisRulePolicy") is not None:
        import capo_cleanrooms.types.configured_table_association_analysis_rule_policy

        out["analysis_rule_policy"] = (
            capo_cleanrooms.types.configured_table_association_analysis_rule_policy.deserialize_json(
                data["analysisRulePolicy"]
            )
        )
    else:
        import capo_cleanrooms.types._unknown

        out["analysis_rule_policy"] = capo_cleanrooms.types._unknown.UnknownUnionMember(
            ""
        )
    return out
