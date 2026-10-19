"""Generated from Smithy shape ``com.amazonaws.cleanrooms#IntermediateTable``."""

from typing import TYPE_CHECKING, Any

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import datetime

    import capo_cleanrooms.types.child_resource_list
    import capo_cleanrooms.types.collaboration_arn
    import capo_cleanrooms.types.dependency_list
    import capo_cleanrooms.types.display_name
    import capo_cleanrooms.types.intermediate_table_active_version
    import capo_cleanrooms.types.intermediate_table_analysis_rule_type_list
    import capo_cleanrooms.types.intermediate_table_arn
    import capo_cleanrooms.types.intermediate_table_schema
    import capo_cleanrooms.types.intermediate_table_status
    import capo_cleanrooms.types.kms_key_arn
    import capo_cleanrooms.types.membership_arn
    import capo_cleanrooms.types.population_analysis_configuration
    import capo_cleanrooms.types.resource_description
    import capo_cleanrooms.types.uuid


class IntermediateTable(TypedDict, closed=True):
    id: "capo_cleanrooms.types.uuid.UUID"
    """<p>The unique identifier of the intermediate table.</p>"""
    arn: "capo_cleanrooms.types.intermediate_table_arn.IntermediateTableArn"
    """<p>The Amazon Resource Name (ARN) of the intermediate table.</p>"""
    name: "capo_cleanrooms.types.display_name.DisplayName"
    """<p>The name of the intermediate table.</p>"""
    description: NotRequired[
        "capo_cleanrooms.types.resource_description.ResourceDescription"
    ]
    """<p>The description of the intermediate table.</p>"""
    membership_arn: "capo_cleanrooms.types.membership_arn.MembershipArn"
    """<p>The Amazon Resource Name (ARN) of the membership that contains the intermediate table.</p>"""
    membership_id: "capo_cleanrooms.types.uuid.UUID"
    """<p>The unique identifier of the membership that contains the intermediate table.</p>"""
    collaboration_arn: "capo_cleanrooms.types.collaboration_arn.CollaborationArn"
    """<p>The Amazon Resource Name (ARN) of the collaboration that contains the intermediate table.</p>"""
    collaboration_id: "capo_cleanrooms.types.uuid.UUID"
    """<p>The unique identifier of the collaboration that contains the intermediate table.</p>"""
    child_resources: NotRequired[
        "capo_cleanrooms.types.child_resource_list.ChildResourceList"
    ]
    """<p>The child resources that depend on this intermediate table.</p>"""
    create_time: "datetime.datetime"
    """<p>The time the intermediate table was created.</p>"""
    update_time: "datetime.datetime"
    """<p>The time the intermediate table was last updated.</p>"""
    status: "capo_cleanrooms.types.intermediate_table_status.IntermediateTableStatus"
    """<p>The current status of the intermediate table.</p>"""
    status_reason: NotRequired["str"]
    """<p>The reason for the current status of the intermediate table.</p>"""
    kms_key_arn: NotRequired["capo_cleanrooms.types.kms_key_arn.KMSKeyArn"]
    """<p>The Amazon Resource Name (ARN) of the KMS key used to encrypt the intermediate table data.</p>"""
    population_analysis_configuration: "capo_cleanrooms.types.population_analysis_configuration.PopulationAnalysisConfiguration"
    """<p>The analysis configuration that defines the query used to populate the intermediate table.</p>"""
    retention_in_days: NotRequired["int"]
    """<p>The number of days that populated data is retained before expiring.</p>"""
    table_dependencies: NotRequired[
        "capo_cleanrooms.types.dependency_list.DependencyList"
    ]
    """<p>The list of base tables that this intermediate table depends on.</p>"""
    intermediate_table_version: NotRequired[
        "capo_cleanrooms.types.intermediate_table_active_version.IntermediateTableActiveVersion"
    ]
    """<p>The details of the currently active version of the intermediate table.</p>"""
    analysis_rule_types: NotRequired[
        "capo_cleanrooms.types.intermediate_table_analysis_rule_type_list.IntermediateTableAnalysisRuleTypeList"
    ]
    """<p>The types of analysis rules associated with the intermediate table.</p>"""
    schema: NotRequired[
        "capo_cleanrooms.types.intermediate_table_schema.IntermediateTableSchema"
    ]
    """<p>The schema of the intermediate table, containing column definitions. Available after the table has been successfully populated.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: IntermediateTable) -> dict:
    out: dict = {}
    out["id"] = value["id"]
    out["arn"] = value["arn"]
    out["name"] = value["name"]
    if "description" in value:
        out["description"] = value["description"]
    out["membershipArn"] = value["membership_arn"]
    out["membershipId"] = value["membership_id"]
    out["collaborationArn"] = value["collaboration_arn"]
    out["collaborationId"] = value["collaboration_id"]
    if "child_resources" in value:
        import capo_cleanrooms.types.child_resource_list

        out["childResources"] = (
            capo_cleanrooms.types.child_resource_list.serialize_json(
                value["child_resources"]
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
    import capo_cleanrooms.types.intermediate_table_status

    out["status"] = capo_cleanrooms.types.intermediate_table_status.serialize_json(
        value["status"]
    )
    if "status_reason" in value:
        out["statusReason"] = value["status_reason"]
    if "kms_key_arn" in value:
        out["kmsKeyArn"] = value["kms_key_arn"]
    import capo_cleanrooms.types.population_analysis_configuration

    out["populationAnalysisConfiguration"] = (
        capo_cleanrooms.types.population_analysis_configuration.serialize_json(
            value["population_analysis_configuration"]
        )
    )
    if "retention_in_days" in value:
        out["retentionInDays"] = value["retention_in_days"]
    if "table_dependencies" in value:
        import capo_cleanrooms.types.dependency_list

        out["tableDependencies"] = capo_cleanrooms.types.dependency_list.serialize_json(
            value["table_dependencies"]
        )
    if "intermediate_table_version" in value:
        import capo_cleanrooms.types.intermediate_table_active_version

        out["intermediateTableVersion"] = (
            capo_cleanrooms.types.intermediate_table_active_version.serialize_json(
                value["intermediate_table_version"]
            )
        )
    if "analysis_rule_types" in value:
        import capo_cleanrooms.types.intermediate_table_analysis_rule_type_list

        out["analysisRuleTypes"] = (
            capo_cleanrooms.types.intermediate_table_analysis_rule_type_list.serialize_json(
                value["analysis_rule_types"]
            )
        )
    if "schema" in value:
        import capo_cleanrooms.types.intermediate_table_schema

        out["schema"] = capo_cleanrooms.types.intermediate_table_schema.serialize_json(
            value["schema"]
        )
    return out


def deserialize_json(data: dict) -> IntermediateTable:
    out: IntermediateTable = {}  # type: ignore[typeddict-item]
    if data.get("id") is not None:
        out["id"] = data["id"]
    else:
        out["id"] = ""
    if data.get("arn") is not None:
        out["arn"] = data["arn"]
    else:
        out["arn"] = ""
    if data.get("name") is not None:
        out["name"] = data["name"]
    else:
        out["name"] = ""
    if data.get("description") is not None:
        out["description"] = data["description"]
    if data.get("membershipArn") is not None:
        out["membership_arn"] = data["membershipArn"]
    else:
        out["membership_arn"] = ""
    if data.get("membershipId") is not None:
        out["membership_id"] = data["membershipId"]
    else:
        out["membership_id"] = ""
    if data.get("collaborationArn") is not None:
        out["collaboration_arn"] = data["collaborationArn"]
    else:
        out["collaboration_arn"] = ""
    if data.get("collaborationId") is not None:
        out["collaboration_id"] = data["collaborationId"]
    else:
        out["collaboration_id"] = ""
    if data.get("childResources") is not None:
        import capo_cleanrooms.types.child_resource_list

        out["child_resources"] = (
            capo_cleanrooms.types.child_resource_list.deserialize_json(
                data["childResources"]
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
    if data.get("status") is not None:
        import capo_cleanrooms.types.intermediate_table_status

        out["status"] = (
            capo_cleanrooms.types.intermediate_table_status.deserialize_json(
                data["status"]
            )
        )
    else:
        import typing

        out["status"] = typing.cast(
            "capo_cleanrooms.types.intermediate_table_status.IntermediateTableStatus",
            "",
        )
    if data.get("statusReason") is not None:
        out["status_reason"] = data["statusReason"]
    if data.get("kmsKeyArn") is not None:
        out["kms_key_arn"] = data["kmsKeyArn"]
    if data.get("populationAnalysisConfiguration") is not None:
        import capo_cleanrooms.types.population_analysis_configuration

        out["population_analysis_configuration"] = (
            capo_cleanrooms.types.population_analysis_configuration.deserialize_json(
                data["populationAnalysisConfiguration"]
            )
        )
    else:
        import capo_cleanrooms.types._unknown

        out["population_analysis_configuration"] = (
            capo_cleanrooms.types._unknown.UnknownUnionMember("")
        )
    if data.get("retentionInDays") is not None:
        out["retention_in_days"] = data["retentionInDays"]
    if data.get("tableDependencies") is not None:
        import capo_cleanrooms.types.dependency_list

        out["table_dependencies"] = (
            capo_cleanrooms.types.dependency_list.deserialize_json(
                data["tableDependencies"]
            )
        )
    if data.get("intermediateTableVersion") is not None:
        import capo_cleanrooms.types.intermediate_table_active_version

        out["intermediate_table_version"] = (
            capo_cleanrooms.types.intermediate_table_active_version.deserialize_json(
                data["intermediateTableVersion"]
            )
        )
    if data.get("analysisRuleTypes") is not None:
        import capo_cleanrooms.types.intermediate_table_analysis_rule_type_list

        out["analysis_rule_types"] = (
            capo_cleanrooms.types.intermediate_table_analysis_rule_type_list.deserialize_json(
                data["analysisRuleTypes"]
            )
        )
    if data.get("schema") is not None:
        import capo_cleanrooms.types.intermediate_table_schema

        out["schema"] = (
            capo_cleanrooms.types.intermediate_table_schema.deserialize_json(
                data["schema"]
            )
        )
    return out


def redact_sensitive(value: IntermediateTable) -> dict[str, Any]:
    out: dict[str, Any] = dict(value)
    if "population_analysis_configuration" in value:
        import capo_cleanrooms.types.population_analysis_configuration

        out["population_analysis_configuration"] = (
            capo_cleanrooms.types.population_analysis_configuration.redact_sensitive(
                value["population_analysis_configuration"]
            )
        )
    if "intermediate_table_version" in value:
        import capo_cleanrooms.types.intermediate_table_active_version

        out["intermediate_table_version"] = (
            capo_cleanrooms.types.intermediate_table_active_version.redact_sensitive(
                value["intermediate_table_version"]
            )
        )
    return out
