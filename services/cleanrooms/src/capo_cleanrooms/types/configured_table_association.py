"""Generated from Smithy shape ``com.amazonaws.cleanrooms#ConfiguredTableAssociation``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import datetime

    import capo_cleanrooms.types.child_resource_list
    import capo_cleanrooms.types.configured_table_arn
    import capo_cleanrooms.types.configured_table_association_analysis_rule_type_list
    import capo_cleanrooms.types.configured_table_association_arn
    import capo_cleanrooms.types.membership_arn
    import capo_cleanrooms.types.role_arn
    import capo_cleanrooms.types.table_alias
    import capo_cleanrooms.types.table_description
    import capo_cleanrooms.types.uuid


class ConfiguredTableAssociation(TypedDict, closed=True):
    arn: "capo_cleanrooms.types.configured_table_association_arn.ConfiguredTableAssociationArn"
    """<p>The unique ARN for the configured table association.</p>"""
    id: "capo_cleanrooms.types.uuid.UUID"
    """<p>The unique ID for the configured table association.</p>"""
    configured_table_id: "capo_cleanrooms.types.uuid.UUID"
    """<p>The unique ID for the configured table that the association refers to.</p>"""
    configured_table_arn: (
        "capo_cleanrooms.types.configured_table_arn.ConfiguredTableArn"
    )
    """<p>The unique ARN for the configured table that the association refers to.</p>"""
    membership_id: "capo_cleanrooms.types.uuid.UUID"
    """<p>The unique ID for the membership this configured table association belongs to.</p>"""
    membership_arn: "capo_cleanrooms.types.membership_arn.MembershipArn"
    """<p>The unique ARN for the membership this configured table association belongs to.</p>"""
    role_arn: "capo_cleanrooms.types.role_arn.RoleArn"
    """<p>The service will assume this role to access catalog metadata and query the table.</p>"""
    name: "capo_cleanrooms.types.table_alias.TableAlias"
    """<p>The name of the configured table association, in lowercase. The table is identified by this name when running protected queries against the underlying data.</p>"""
    description: NotRequired["capo_cleanrooms.types.table_description.TableDescription"]
    """<p>A description of the configured table association.</p>"""
    analysis_rule_types: NotRequired[
        "capo_cleanrooms.types.configured_table_association_analysis_rule_type_list.ConfiguredTableAssociationAnalysisRuleTypeList"
    ]
    """<p> The analysis rule types for the configured table association.</p>"""
    create_time: "datetime.datetime"
    """<p>The time the configured table association was created.</p>"""
    update_time: "datetime.datetime"
    """<p>The time the configured table association was last updated.</p>"""
    child_resources: NotRequired[
        "capo_cleanrooms.types.child_resource_list.ChildResourceList"
    ]
    """<p>The child resources that depend on this configured table association.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: ConfiguredTableAssociation) -> dict:
    out: dict = {}
    out["arn"] = value["arn"]
    out["id"] = value["id"]
    out["configuredTableId"] = value["configured_table_id"]
    out["configuredTableArn"] = value["configured_table_arn"]
    out["membershipId"] = value["membership_id"]
    out["membershipArn"] = value["membership_arn"]
    out["roleArn"] = value["role_arn"]
    out["name"] = value["name"]
    if "description" in value:
        out["description"] = value["description"]
    if "analysis_rule_types" in value:
        import capo_cleanrooms.types.configured_table_association_analysis_rule_type_list

        out["analysisRuleTypes"] = (
            capo_cleanrooms.types.configured_table_association_analysis_rule_type_list.serialize_json(
                value["analysis_rule_types"]
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
    if "child_resources" in value:
        import capo_cleanrooms.types.child_resource_list

        out["childResources"] = (
            capo_cleanrooms.types.child_resource_list.serialize_json(
                value["child_resources"]
            )
        )
    return out


def deserialize_json(data: dict) -> ConfiguredTableAssociation:
    out: ConfiguredTableAssociation = {}  # type: ignore[typeddict-item]
    if data.get("arn") is not None:
        out["arn"] = data["arn"]
    else:
        out["arn"] = ""
    if data.get("id") is not None:
        out["id"] = data["id"]
    else:
        out["id"] = ""
    if data.get("configuredTableId") is not None:
        out["configured_table_id"] = data["configuredTableId"]
    else:
        out["configured_table_id"] = ""
    if data.get("configuredTableArn") is not None:
        out["configured_table_arn"] = data["configuredTableArn"]
    else:
        out["configured_table_arn"] = ""
    if data.get("membershipId") is not None:
        out["membership_id"] = data["membershipId"]
    else:
        out["membership_id"] = ""
    if data.get("membershipArn") is not None:
        out["membership_arn"] = data["membershipArn"]
    else:
        out["membership_arn"] = ""
    if data.get("roleArn") is not None:
        out["role_arn"] = data["roleArn"]
    else:
        out["role_arn"] = ""
    if data.get("name") is not None:
        out["name"] = data["name"]
    else:
        out["name"] = ""
    if data.get("description") is not None:
        out["description"] = data["description"]
    if data.get("analysisRuleTypes") is not None:
        import capo_cleanrooms.types.configured_table_association_analysis_rule_type_list

        out["analysis_rule_types"] = (
            capo_cleanrooms.types.configured_table_association_analysis_rule_type_list.deserialize_json(
                data["analysisRuleTypes"]
            )
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
    if data.get("childResources") is not None:
        import capo_cleanrooms.types.child_resource_list

        out["child_resources"] = (
            capo_cleanrooms.types.child_resource_list.deserialize_json(
                data["childResources"]
            )
        )
    return out
