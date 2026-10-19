"""Generated from Smithy shape ``com.amazonaws.cleanrooms#Schema``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import datetime

    import capo_cleanrooms.types.account_id
    import capo_cleanrooms.types.analysis_method
    import capo_cleanrooms.types.analysis_rule_type_list
    import capo_cleanrooms.types.collaboration_arn
    import capo_cleanrooms.types.column_list
    import capo_cleanrooms.types.schema_resource_arn
    import capo_cleanrooms.types.schema_status_detail_list
    import capo_cleanrooms.types.schema_type
    import capo_cleanrooms.types.schema_type_properties
    import capo_cleanrooms.types.selected_analysis_methods
    import capo_cleanrooms.types.table_alias
    import capo_cleanrooms.types.table_description
    import capo_cleanrooms.types.uuid


class Schema(TypedDict, closed=True):
    columns: "capo_cleanrooms.types.column_list.ColumnList"
    """<p>The columns for the relation that this schema represents.</p>"""
    partition_keys: "capo_cleanrooms.types.column_list.ColumnList"
    """<p>The partition keys for the dataset underlying this schema.</p>"""
    analysis_rule_types: (
        "capo_cleanrooms.types.analysis_rule_type_list.AnalysisRuleTypeList"
    )
    """<p>The analysis rule types that are associated with the schema. Currently, only one entry is present.</p>"""
    analysis_method: NotRequired["capo_cleanrooms.types.analysis_method.AnalysisMethod"]
    """<p>The analysis method for the schema. </p> <p> <code>DIRECT_QUERY</code> allows SQL queries to be run directly on this table.</p> <p> <code>DIRECT_JOB</code> allows PySpark jobs to be run directly on this table.</p> <p> <code>MULTIPLE</code> allows both SQL queries and PySpark jobs to be run directly on this table.</p>"""
    selected_analysis_methods: NotRequired[
        "capo_cleanrooms.types.selected_analysis_methods.SelectedAnalysisMethods"
    ]
    """<p> The selected analysis methods for the schema.</p>"""
    creator_account_id: "capo_cleanrooms.types.account_id.AccountId"
    """<p>The unique account ID for the Amazon Web Services account that owns the schema.</p>"""
    name: "capo_cleanrooms.types.table_alias.TableAlias"
    """<p>A name for the schema. The schema relation is referred to by this name when queried by a protected query.</p>"""
    collaboration_id: "capo_cleanrooms.types.uuid.UUID"
    """<p>The unique ID for the collaboration that the schema belongs to.</p>"""
    collaboration_arn: "capo_cleanrooms.types.collaboration_arn.CollaborationArn"
    """<p>The unique Amazon Resource Name (ARN) for the collaboration that the schema belongs to.</p>"""
    description: "capo_cleanrooms.types.table_description.TableDescription"
    """<p>A description for the schema.</p>"""
    create_time: "datetime.datetime"
    """<p>The time at which the schema was created.</p>"""
    update_time: "datetime.datetime"
    """<p>The most recent time at which the schema was updated.</p>"""
    type: "capo_cleanrooms.types.schema_type.SchemaType"
    """<p>The type of schema.</p>"""
    schema_status_details: (
        "capo_cleanrooms.types.schema_status_detail_list.SchemaStatusDetailList"
    )
    """<p>Details about the status of the schema. Currently, only one entry is present.</p>"""
    resource_arn: NotRequired[
        "capo_cleanrooms.types.schema_resource_arn.SchemaResourceArn"
    ]
    """<p>The Amazon Resource Name (ARN) of the schema resource.</p>"""
    schema_type_properties: NotRequired[
        "capo_cleanrooms.types.schema_type_properties.SchemaTypeProperties"
    ]
    """<p>The schema type properties.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: Schema) -> dict:
    out: dict = {}
    import capo_cleanrooms.types.column_list

    out["columns"] = capo_cleanrooms.types.column_list.serialize_json(value["columns"])
    import capo_cleanrooms.types.column_list

    out["partitionKeys"] = capo_cleanrooms.types.column_list.serialize_json(
        value["partition_keys"]
    )
    import capo_cleanrooms.types.analysis_rule_type_list

    out["analysisRuleTypes"] = (
        capo_cleanrooms.types.analysis_rule_type_list.serialize_json(
            value["analysis_rule_types"]
        )
    )
    if "analysis_method" in value:
        import capo_cleanrooms.types.analysis_method

        out["analysisMethod"] = capo_cleanrooms.types.analysis_method.serialize_json(
            value["analysis_method"]
        )
    if "selected_analysis_methods" in value:
        import capo_cleanrooms.types.selected_analysis_methods

        out["selectedAnalysisMethods"] = (
            capo_cleanrooms.types.selected_analysis_methods.serialize_json(
                value["selected_analysis_methods"]
            )
        )
    out["creatorAccountId"] = value["creator_account_id"]
    out["name"] = value["name"]
    out["collaborationId"] = value["collaboration_id"]
    out["collaborationArn"] = value["collaboration_arn"]
    out["description"] = value["description"]
    import capo_cleanrooms.types._prelude.timestamp

    out["createTime"] = capo_cleanrooms.types._prelude.timestamp.serialize_json(
        value["create_time"]
    )
    import capo_cleanrooms.types._prelude.timestamp

    out["updateTime"] = capo_cleanrooms.types._prelude.timestamp.serialize_json(
        value["update_time"]
    )
    import capo_cleanrooms.types.schema_type

    out["type"] = capo_cleanrooms.types.schema_type.serialize_json(value["type"])
    import capo_cleanrooms.types.schema_status_detail_list

    out["schemaStatusDetails"] = (
        capo_cleanrooms.types.schema_status_detail_list.serialize_json(
            value.get("schema_status_details", [])
        )
    )
    if "resource_arn" in value:
        out["resourceArn"] = value["resource_arn"]
    if "schema_type_properties" in value:
        import capo_cleanrooms.types.schema_type_properties

        out["schemaTypeProperties"] = (
            capo_cleanrooms.types.schema_type_properties.serialize_json(
                value["schema_type_properties"]
            )
        )
    return out


def deserialize_json(data: dict) -> Schema:
    out: Schema = {}  # type: ignore[typeddict-item]
    if data.get("columns") is not None:
        import capo_cleanrooms.types.column_list

        out["columns"] = capo_cleanrooms.types.column_list.deserialize_json(
            data["columns"]
        )
    else:
        out["columns"] = []
    if data.get("partitionKeys") is not None:
        import capo_cleanrooms.types.column_list

        out["partition_keys"] = capo_cleanrooms.types.column_list.deserialize_json(
            data["partitionKeys"]
        )
    else:
        out["partition_keys"] = []
    if data.get("analysisRuleTypes") is not None:
        import capo_cleanrooms.types.analysis_rule_type_list

        out["analysis_rule_types"] = (
            capo_cleanrooms.types.analysis_rule_type_list.deserialize_json(
                data["analysisRuleTypes"]
            )
        )
    else:
        out["analysis_rule_types"] = []
    if data.get("analysisMethod") is not None:
        import capo_cleanrooms.types.analysis_method

        out["analysis_method"] = capo_cleanrooms.types.analysis_method.deserialize_json(
            data["analysisMethod"]
        )
    if data.get("selectedAnalysisMethods") is not None:
        import capo_cleanrooms.types.selected_analysis_methods

        out["selected_analysis_methods"] = (
            capo_cleanrooms.types.selected_analysis_methods.deserialize_json(
                data["selectedAnalysisMethods"]
            )
        )
    if data.get("creatorAccountId") is not None:
        out["creator_account_id"] = data["creatorAccountId"]
    else:
        out["creator_account_id"] = ""
    if data.get("name") is not None:
        out["name"] = data["name"]
    else:
        out["name"] = ""
    if data.get("collaborationId") is not None:
        out["collaboration_id"] = data["collaborationId"]
    else:
        out["collaboration_id"] = ""
    if data.get("collaborationArn") is not None:
        out["collaboration_arn"] = data["collaborationArn"]
    else:
        out["collaboration_arn"] = ""
    if data.get("description") is not None:
        out["description"] = data["description"]
    else:
        out["description"] = ""
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
    if data.get("type") is not None:
        import capo_cleanrooms.types.schema_type

        out["type"] = capo_cleanrooms.types.schema_type.deserialize_json(data["type"])
    else:
        import typing

        out["type"] = typing.cast("capo_cleanrooms.types.schema_type.SchemaType", "")
    if data.get("schemaStatusDetails") is not None:
        import capo_cleanrooms.types.schema_status_detail_list

        out["schema_status_details"] = (
            capo_cleanrooms.types.schema_status_detail_list.deserialize_json(
                data["schemaStatusDetails"]
            )
        )
    else:
        out["schema_status_details"] = []
    if data.get("resourceArn") is not None:
        out["resource_arn"] = data["resourceArn"]
    if data.get("schemaTypeProperties") is not None:
        import capo_cleanrooms.types.schema_type_properties

        out["schema_type_properties"] = (
            capo_cleanrooms.types.schema_type_properties.deserialize_json(
                data["schemaTypeProperties"]
            )
        )
    return out
