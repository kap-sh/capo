"""Generated from Smithy shape ``com.amazonaws.cleanrooms#ConfiguredTableAssociationAnalysisRule``."""

from typing import TYPE_CHECKING

from typing_extensions import TypedDict

if TYPE_CHECKING:
    import datetime

    import capo_cleanrooms.types.configured_table_association_analysis_rule_policy
    import capo_cleanrooms.types.configured_table_association_analysis_rule_type
    import capo_cleanrooms.types.configured_table_association_arn
    import capo_cleanrooms.types.configured_table_association_identifier
    import capo_cleanrooms.types.membership_identifier


class ConfiguredTableAssociationAnalysisRule(TypedDict, closed=True):
    membership_identifier: (
        "capo_cleanrooms.types.membership_identifier.MembershipIdentifier"
    )
    """<p> The membership identifier for the configured table association analysis rule.</p>"""
    configured_table_association_id: "capo_cleanrooms.types.configured_table_association_identifier.ConfiguredTableAssociationIdentifier"
    """<p> The unique identifier for the configured table association.</p>"""
    configured_table_association_arn: "capo_cleanrooms.types.configured_table_association_arn.ConfiguredTableAssociationArn"
    """<p> The Amazon Resource Name (ARN) of the configured table association.</p>"""
    policy: "capo_cleanrooms.types.configured_table_association_analysis_rule_policy.ConfiguredTableAssociationAnalysisRulePolicy"
    """<p> The policy of the configured table association analysis rule.</p>"""
    type: "capo_cleanrooms.types.configured_table_association_analysis_rule_type.ConfiguredTableAssociationAnalysisRuleType"
    """<p> The type of the configured table association analysis rule.</p>"""
    create_time: "datetime.datetime"
    """<p> The creation time of the configured table association analysis rule.</p>"""
    update_time: "datetime.datetime"
    """<p> The update time of the configured table association analysis rule.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: ConfiguredTableAssociationAnalysisRule) -> dict:
    out: dict = {}
    out["membershipIdentifier"] = value["membership_identifier"]
    out["configuredTableAssociationId"] = value["configured_table_association_id"]
    out["configuredTableAssociationArn"] = value["configured_table_association_arn"]
    import capo_cleanrooms.types.configured_table_association_analysis_rule_policy

    out["policy"] = (
        capo_cleanrooms.types.configured_table_association_analysis_rule_policy.serialize_json(
            value["policy"]
        )
    )
    import capo_cleanrooms.types.configured_table_association_analysis_rule_type

    out["type"] = (
        capo_cleanrooms.types.configured_table_association_analysis_rule_type.serialize_json(
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


def deserialize_json(data: dict) -> ConfiguredTableAssociationAnalysisRule:
    out: ConfiguredTableAssociationAnalysisRule = {}  # type: ignore[typeddict-item]
    if data.get("membershipIdentifier") is not None:
        out["membership_identifier"] = data["membershipIdentifier"]
    else:
        out["membership_identifier"] = ""
    if data.get("configuredTableAssociationId") is not None:
        out["configured_table_association_id"] = data["configuredTableAssociationId"]
    else:
        out["configured_table_association_id"] = ""
    if data.get("configuredTableAssociationArn") is not None:
        out["configured_table_association_arn"] = data["configuredTableAssociationArn"]
    else:
        out["configured_table_association_arn"] = ""
    if data.get("policy") is not None:
        import capo_cleanrooms.types.configured_table_association_analysis_rule_policy

        out["policy"] = (
            capo_cleanrooms.types.configured_table_association_analysis_rule_policy.deserialize_json(
                data["policy"]
            )
        )
    else:
        import capo_cleanrooms.types._unknown

        out["policy"] = capo_cleanrooms.types._unknown.UnknownUnionMember("")
    if data.get("type") is not None:
        import capo_cleanrooms.types.configured_table_association_analysis_rule_type

        out["type"] = (
            capo_cleanrooms.types.configured_table_association_analysis_rule_type.deserialize_json(
                data["type"]
            )
        )
    else:
        import typing

        out["type"] = typing.cast(
            "capo_cleanrooms.types.configured_table_association_analysis_rule_type.ConfiguredTableAssociationAnalysisRuleType",
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
