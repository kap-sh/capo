"""Generated from Smithy shape ``com.amazonaws.glue#GetUnfilteredPartitionMetadataRequest``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_glue.types.audit_context
    import capo_glue.types.catalog_id_string
    import capo_glue.types.name_string
    import capo_glue.types.permission_type_list
    import capo_glue.types.query_session_context
    import capo_glue.types.value_string
    import capo_glue.types.value_string_list


class GetUnfilteredPartitionMetadataRequest(TypedDict, closed=True):
    region: NotRequired["capo_glue.types.value_string.ValueString"]
    """<p>Specified only if the base tables belong to a different Amazon Web Services Region.</p>"""
    catalog_id: "capo_glue.types.catalog_id_string.CatalogIdString"
    """<p>The catalog ID where the partition resides.</p>"""
    database_name: "capo_glue.types.name_string.NameString"
    """<p>(Required) Specifies the name of a database that contains the partition.</p>"""
    table_name: "capo_glue.types.name_string.NameString"
    """<p>(Required) Specifies the name of a table that contains the partition.</p>"""
    partition_values: "capo_glue.types.value_string_list.ValueStringList"
    """<p>(Required) A list of partition key values.</p>"""
    audit_context: NotRequired["capo_glue.types.audit_context.AuditContext"]
    """<p>A structure containing Lake Formation audit context information.</p>"""
    supported_permission_types: (
        "capo_glue.types.permission_type_list.PermissionTypeList"
    )
    """<p>(Required) A list of supported permission types. </p>"""
    query_session_context: NotRequired[
        "capo_glue.types.query_session_context.QuerySessionContext"
    ]
    """<p>A structure used as a protocol between query engines and Lake Formation or Glue. Contains both a Lake Formation generated authorization identifier and information from the request's authorization context.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: GetUnfilteredPartitionMetadataRequest) -> dict:
    out: dict = {}
    if "region" in value:
        out["Region"] = value["region"]
    out["CatalogId"] = value["catalog_id"]
    out["DatabaseName"] = value["database_name"]
    out["TableName"] = value["table_name"]
    import capo_glue.types.value_string_list

    out["PartitionValues"] = capo_glue.types.value_string_list.serialize_aws_json_1_1(
        value["partition_values"]
    )
    if "audit_context" in value:
        import capo_glue.types.audit_context

        out["AuditContext"] = capo_glue.types.audit_context.serialize_aws_json_1_1(
            value["audit_context"]
        )
    import capo_glue.types.permission_type_list

    out["SupportedPermissionTypes"] = (
        capo_glue.types.permission_type_list.serialize_aws_json_1_1(
            value["supported_permission_types"]
        )
    )
    if "query_session_context" in value:
        import capo_glue.types.query_session_context

        out["QuerySessionContext"] = (
            capo_glue.types.query_session_context.serialize_aws_json_1_1(
                value["query_session_context"]
            )
        )
    return out


def deserialize_aws_json_1_1(data: dict) -> GetUnfilteredPartitionMetadataRequest:
    out: GetUnfilteredPartitionMetadataRequest = {}  # type: ignore[typeddict-item]
    if data.get("Region") is not None:
        out["region"] = data["Region"]
    if data.get("CatalogId") is not None:
        out["catalog_id"] = data["CatalogId"]
    else:
        out["catalog_id"] = ""
    if data.get("DatabaseName") is not None:
        out["database_name"] = data["DatabaseName"]
    else:
        out["database_name"] = ""
    if data.get("TableName") is not None:
        out["table_name"] = data["TableName"]
    else:
        out["table_name"] = ""
    if data.get("PartitionValues") is not None:
        import capo_glue.types.value_string_list

        out["partition_values"] = (
            capo_glue.types.value_string_list.deserialize_aws_json_1_1(
                data["PartitionValues"]
            )
        )
    else:
        out["partition_values"] = []
    if data.get("AuditContext") is not None:
        import capo_glue.types.audit_context

        out["audit_context"] = capo_glue.types.audit_context.deserialize_aws_json_1_1(
            data["AuditContext"]
        )
    if data.get("SupportedPermissionTypes") is not None:
        import capo_glue.types.permission_type_list

        out["supported_permission_types"] = (
            capo_glue.types.permission_type_list.deserialize_aws_json_1_1(
                data["SupportedPermissionTypes"]
            )
        )
    else:
        out["supported_permission_types"] = []
    if data.get("QuerySessionContext") is not None:
        import capo_glue.types.query_session_context

        out["query_session_context"] = (
            capo_glue.types.query_session_context.deserialize_aws_json_1_1(
                data["QuerySessionContext"]
            )
        )
    return out
