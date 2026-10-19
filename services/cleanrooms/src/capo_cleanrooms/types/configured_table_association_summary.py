"""Generated from Smithy shape ``com.amazonaws.cleanrooms#ConfiguredTableAssociationSummary``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import datetime

    import capo_cleanrooms.types.configured_table_association_analysis_rule_type_list
    import capo_cleanrooms.types.configured_table_association_arn
    import capo_cleanrooms.types.membership_arn
    import capo_cleanrooms.types.membership_identifier
    import capo_cleanrooms.types.table_alias
    import capo_cleanrooms.types.uuid


class ConfiguredTableAssociationSummary(TypedDict, closed=True):
    configured_table_id: "capo_cleanrooms.types.uuid.UUID"
    """<p>The unique configured table ID that this configured table association refers to.</p>"""
    membership_id: "capo_cleanrooms.types.membership_identifier.MembershipIdentifier"
    """<p>The unique ID for the membership that the configured table association belongs to.</p>"""
    membership_arn: "capo_cleanrooms.types.membership_arn.MembershipArn"
    """<p>The unique ARN for the membership that the configured table association belongs to.</p>"""
    name: "capo_cleanrooms.types.table_alias.TableAlias"
    """<p>The name of the configured table association. The table is identified by this name when running Protected Queries against the underlying data.</p>"""
    create_time: "datetime.datetime"
    """<p>The time the configured table association was created.</p>"""
    update_time: "datetime.datetime"
    """<p>The time the configured table association was last updated.</p>"""
    id: "capo_cleanrooms.types.uuid.UUID"
    """<p>The unique ID for the configured table association.</p>"""
    arn: "capo_cleanrooms.types.configured_table_association_arn.ConfiguredTableAssociationArn"
    """<p>The unique ARN for the configured table association.</p>"""
    analysis_rule_types: NotRequired[
        "capo_cleanrooms.types.configured_table_association_analysis_rule_type_list.ConfiguredTableAssociationAnalysisRuleTypeList"
    ]
    """<p>The analysis rule types that are associated with the configured table associations in this summary. </p>"""


# --- restJson1 ser/de ---
def serialize_json(value: ConfiguredTableAssociationSummary) -> dict:
    out: dict = {}
    out["configuredTableId"] = value["configured_table_id"]
    out["membershipId"] = value["membership_id"]
    out["membershipArn"] = value["membership_arn"]
    out["name"] = value["name"]
    import capo_cleanrooms.types._prelude.timestamp

    out["createTime"] = capo_cleanrooms.types._prelude.timestamp.serialize_json(
        value["create_time"]
    )
    import capo_cleanrooms.types._prelude.timestamp

    out["updateTime"] = capo_cleanrooms.types._prelude.timestamp.serialize_json(
        value["update_time"]
    )
    out["id"] = value["id"]
    out["arn"] = value["arn"]
    if "analysis_rule_types" in value:
        import capo_cleanrooms.types.configured_table_association_analysis_rule_type_list

        out["analysisRuleTypes"] = (
            capo_cleanrooms.types.configured_table_association_analysis_rule_type_list.serialize_json(
                value["analysis_rule_types"]
            )
        )
    return out


def deserialize_json(data: dict) -> ConfiguredTableAssociationSummary:
    out: ConfiguredTableAssociationSummary = {}  # type: ignore[typeddict-item]
    if data.get("configuredTableId") is not None:
        out["configured_table_id"] = data["configuredTableId"]
    else:
        out["configured_table_id"] = ""
    if data.get("membershipId") is not None:
        out["membership_id"] = data["membershipId"]
    else:
        out["membership_id"] = ""
    if data.get("membershipArn") is not None:
        out["membership_arn"] = data["membershipArn"]
    else:
        out["membership_arn"] = ""
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
    if data.get("id") is not None:
        out["id"] = data["id"]
    else:
        out["id"] = ""
    if data.get("arn") is not None:
        out["arn"] = data["arn"]
    else:
        out["arn"] = ""
    if data.get("analysisRuleTypes") is not None:
        import capo_cleanrooms.types.configured_table_association_analysis_rule_type_list

        out["analysis_rule_types"] = (
            capo_cleanrooms.types.configured_table_association_analysis_rule_type_list.deserialize_json(
                data["analysisRuleTypes"]
            )
        )
    return out
