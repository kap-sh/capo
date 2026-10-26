"""Generated from Smithy shape ``com.amazonaws.cleanrooms#AnalysisRule``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import datetime

    import capo_cleanrooms.types.analysis_rule_policy
    import capo_cleanrooms.types.analysis_rule_type
    import capo_cleanrooms.types.collaboration_identifier
    import capo_cleanrooms.types.configured_table_association_analysis_rule_policy
    import capo_cleanrooms.types.consolidated_policy
    import capo_cleanrooms.types.table_alias


class AnalysisRule(TypedDict, closed=True):
    collaboration_id: (
        "capo_cleanrooms.types.collaboration_identifier.CollaborationIdentifier"
    )
    """<p>The unique ID for the associated collaboration.</p>"""
    type: "capo_cleanrooms.types.analysis_rule_type.AnalysisRuleType"
    """<p>The type of analysis rule.</p>"""
    name: "capo_cleanrooms.types.table_alias.TableAlias"
    """<p>The name for the analysis rule.</p>"""
    create_time: "datetime.datetime"
    """<p>The time the analysis rule was created.</p>"""
    update_time: "datetime.datetime"
    """<p>The time the analysis rule was last updated.</p>"""
    policy: "capo_cleanrooms.types.analysis_rule_policy.AnalysisRulePolicy"
    """<p>A policy that describes the associated data usage limitations.</p>"""
    collaboration_policy: NotRequired[
        "capo_cleanrooms.types.configured_table_association_analysis_rule_policy.ConfiguredTableAssociationAnalysisRulePolicy"
    ]
    consolidated_policy: NotRequired[
        "capo_cleanrooms.types.consolidated_policy.ConsolidatedPolicy"
    ]
    """<p> The consolidated policy for the analysis rule.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: AnalysisRule) -> dict:
    out: dict = {}
    out["collaborationId"] = value["collaboration_id"]
    import capo_cleanrooms.types.analysis_rule_type

    out["type"] = capo_cleanrooms.types.analysis_rule_type.serialize_json(value["type"])
    out["name"] = value["name"]
    import capo_cleanrooms.types._prelude.timestamp

    out["createTime"] = capo_cleanrooms.types._prelude.timestamp.serialize_json(
        value["create_time"]
    )
    import capo_cleanrooms.types._prelude.timestamp

    out["updateTime"] = capo_cleanrooms.types._prelude.timestamp.serialize_json(
        value["update_time"]
    )
    import capo_cleanrooms.types.analysis_rule_policy

    out["policy"] = capo_cleanrooms.types.analysis_rule_policy.serialize_json(
        value["policy"]
    )
    if "collaboration_policy" in value:
        import capo_cleanrooms.types.configured_table_association_analysis_rule_policy

        out["collaborationPolicy"] = (
            capo_cleanrooms.types.configured_table_association_analysis_rule_policy.serialize_json(
                value["collaboration_policy"]
            )
        )
    if "consolidated_policy" in value:
        import capo_cleanrooms.types.consolidated_policy

        out["consolidatedPolicy"] = (
            capo_cleanrooms.types.consolidated_policy.serialize_json(
                value["consolidated_policy"]
            )
        )
    return out


def deserialize_json(data: dict) -> AnalysisRule:
    out: AnalysisRule = {}  # type: ignore[typeddict-item]
    if data.get("collaborationId") is not None:
        out["collaboration_id"] = data["collaborationId"]
    else:
        out["collaboration_id"] = ""
    if data.get("type") is not None:
        import capo_cleanrooms.types.analysis_rule_type

        out["type"] = capo_cleanrooms.types.analysis_rule_type.deserialize_json(
            data["type"]
        )
    else:
        import typing

        out["type"] = typing.cast(
            "capo_cleanrooms.types.analysis_rule_type.AnalysisRuleType", ""
        )
    if data.get("name") is not None:
        out["name"] = data["name"]
    else:
        out["name"] = ""
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
    if data.get("policy") is not None:
        import capo_cleanrooms.types.analysis_rule_policy

        out["policy"] = capo_cleanrooms.types.analysis_rule_policy.deserialize_json(
            data["policy"]
        )
    else:
        out["policy"] = {"$unknown": {"name": ""}}
    if data.get("collaborationPolicy") is not None:
        import capo_cleanrooms.types.configured_table_association_analysis_rule_policy

        out["collaboration_policy"] = (
            capo_cleanrooms.types.configured_table_association_analysis_rule_policy.deserialize_json(
                data["collaborationPolicy"]
            )
        )
    if data.get("consolidatedPolicy") is not None:
        import capo_cleanrooms.types.consolidated_policy

        out["consolidated_policy"] = (
            capo_cleanrooms.types.consolidated_policy.deserialize_json(
                data["consolidatedPolicy"]
            )
        )
    return out
