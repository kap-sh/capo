"""Generated from Smithy shape ``com.amazonaws.cleanrooms#IntermediateTableAnalysisRule``."""

from typing import TYPE_CHECKING

from typing_extensions import TypedDict

if TYPE_CHECKING:
    import datetime

    import capo_cleanrooms.types.intermediate_table_analysis_rule_policy
    import capo_cleanrooms.types.intermediate_table_analysis_rule_type
    import capo_cleanrooms.types.intermediate_table_arn
    import capo_cleanrooms.types.uuid


class IntermediateTableAnalysisRule(TypedDict, closed=True):
    intermediate_table_identifier: "capo_cleanrooms.types.uuid.UUID"
    """<p>The unique identifier of the intermediate table associated with this analysis rule.</p>"""
    intermediate_table_arn: (
        "capo_cleanrooms.types.intermediate_table_arn.IntermediateTableArn"
    )
    """<p>The Amazon Resource Name (ARN) of the intermediate table associated with this analysis rule.</p>"""
    analysis_rule_policy: "capo_cleanrooms.types.intermediate_table_analysis_rule_policy.IntermediateTableAnalysisRulePolicy"
    """<p>The policy of the analysis rule.</p>"""
    analysis_rule_type: "capo_cleanrooms.types.intermediate_table_analysis_rule_type.IntermediateTableAnalysisRuleType"
    """<p>The type of the analysis rule.</p>"""
    create_time: "datetime.datetime"
    """<p>The time the analysis rule was created.</p>"""
    update_time: "datetime.datetime"
    """<p>The time the analysis rule was last updated.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: IntermediateTableAnalysisRule) -> dict:
    out: dict = {}
    out["intermediateTableIdentifier"] = value["intermediate_table_identifier"]
    out["intermediateTableArn"] = value["intermediate_table_arn"]
    import capo_cleanrooms.types.intermediate_table_analysis_rule_policy

    out["analysisRulePolicy"] = (
        capo_cleanrooms.types.intermediate_table_analysis_rule_policy.serialize_json(
            value["analysis_rule_policy"]
        )
    )
    import capo_cleanrooms.types.intermediate_table_analysis_rule_type

    out["analysisRuleType"] = (
        capo_cleanrooms.types.intermediate_table_analysis_rule_type.serialize_json(
            value["analysis_rule_type"]
        )
    )
    import capo_cleanrooms.types._prelude.timestamp

    out["createTime"] = capo_cleanrooms.types._prelude.timestamp.serialize_json(
        value["create_time"]
    )
    import capo_cleanrooms.types._prelude.timestamp

    out["updateTime"] = capo_cleanrooms.types._prelude.timestamp.serialize_json(
        value["update_time"]
    )
    return out


def deserialize_json(data: dict) -> IntermediateTableAnalysisRule:
    out: IntermediateTableAnalysisRule = {}  # type: ignore[typeddict-item]
    if data.get("intermediateTableIdentifier") is not None:
        out["intermediate_table_identifier"] = data["intermediateTableIdentifier"]
    else:
        out["intermediate_table_identifier"] = ""
    if data.get("intermediateTableArn") is not None:
        out["intermediate_table_arn"] = data["intermediateTableArn"]
    else:
        out["intermediate_table_arn"] = ""
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
    if data.get("createTime") is not None:
        import capo_cleanrooms.types._prelude.timestamp

        out["create_time"] = capo_cleanrooms.types._prelude.timestamp.deserialize_json(
            data["createTime"]
        )
    else:
        import datetime

        out["create_time"] = datetime.datetime.fromtimestamp(
            0, tz=datetime.timezone.utc
        )
    if data.get("updateTime") is not None:
        import capo_cleanrooms.types._prelude.timestamp

        out["update_time"] = capo_cleanrooms.types._prelude.timestamp.deserialize_json(
            data["updateTime"]
        )
    else:
        import datetime

        out["update_time"] = datetime.datetime.fromtimestamp(
            0, tz=datetime.timezone.utc
        )
    return out
