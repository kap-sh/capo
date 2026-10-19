"""Generated from Smithy shape ``com.amazonaws.cleanrooms#ConfiguredTableAnalysisRule``."""

from typing import TYPE_CHECKING

from typing_extensions import TypedDict

if TYPE_CHECKING:
    import datetime

    import capo_cleanrooms.types.configured_table_analysis_rule_policy
    import capo_cleanrooms.types.configured_table_analysis_rule_type
    import capo_cleanrooms.types.configured_table_arn
    import capo_cleanrooms.types.uuid


class ConfiguredTableAnalysisRule(TypedDict, closed=True):
    configured_table_id: "capo_cleanrooms.types.uuid.UUID"
    """<p>The unique ID for the configured table.</p>"""
    configured_table_arn: (
        "capo_cleanrooms.types.configured_table_arn.ConfiguredTableArn"
    )
    """<p>The unique ARN for the configured table.</p>"""
    policy: "capo_cleanrooms.types.configured_table_analysis_rule_policy.ConfiguredTableAnalysisRulePolicy"
    """<p>The policy that controls SQL query rules.</p>"""
    type: "capo_cleanrooms.types.configured_table_analysis_rule_type.ConfiguredTableAnalysisRuleType"
    """<p>The type of configured table analysis rule.</p>"""
    create_time: "datetime.datetime"
    """<p>The time the configured table analysis rule was created.</p>"""
    update_time: "datetime.datetime"
    """<p>The time the configured table analysis rule was last updated.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: ConfiguredTableAnalysisRule) -> dict:
    out: dict = {}
    out["configuredTableId"] = value["configured_table_id"]
    out["configuredTableArn"] = value["configured_table_arn"]
    import capo_cleanrooms.types.configured_table_analysis_rule_policy

    out["policy"] = (
        capo_cleanrooms.types.configured_table_analysis_rule_policy.serialize_json(
            value["policy"]
        )
    )
    import capo_cleanrooms.types.configured_table_analysis_rule_type

    out["type"] = (
        capo_cleanrooms.types.configured_table_analysis_rule_type.serialize_json(
            value["type"]
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


def deserialize_json(data: dict) -> ConfiguredTableAnalysisRule:
    out: ConfiguredTableAnalysisRule = {}  # type: ignore[typeddict-item]
    if data.get("configuredTableId") is not None:
        out["configured_table_id"] = data["configuredTableId"]
    else:
        out["configured_table_id"] = ""
    if data.get("configuredTableArn") is not None:
        out["configured_table_arn"] = data["configuredTableArn"]
    else:
        out["configured_table_arn"] = ""
    if data.get("policy") is not None:
        import capo_cleanrooms.types.configured_table_analysis_rule_policy

        out["policy"] = (
            capo_cleanrooms.types.configured_table_analysis_rule_policy.deserialize_json(
                data["policy"]
            )
        )
    else:
        import capo_cleanrooms.types._unknown

        out["policy"] = capo_cleanrooms.types._unknown.UnknownUnionMember("")
    if data.get("type") is not None:
        import capo_cleanrooms.types.configured_table_analysis_rule_type

        out["type"] = (
            capo_cleanrooms.types.configured_table_analysis_rule_type.deserialize_json(
                data["type"]
            )
        )
    else:
        import typing

        out["type"] = typing.cast(
            "capo_cleanrooms.types.configured_table_analysis_rule_type.ConfiguredTableAnalysisRuleType",
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
