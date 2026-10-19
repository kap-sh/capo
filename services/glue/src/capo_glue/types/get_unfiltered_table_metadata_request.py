"""Generated from Smithy shape ``com.amazonaws.glue#GetUnfilteredTableMetadataRequest``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_glue.types.arn_string
    import capo_glue.types.audit_context
    import capo_glue.types.catalog_id_string
    import capo_glue.types.name_string
    import capo_glue.types.permission_list
    import capo_glue.types.permission_type_list
    import capo_glue.types.query_session_context
    import capo_glue.types.supported_dialect
    import capo_glue.types.value_string


class GetUnfilteredTableMetadataRequest(TypedDict, closed=True):
    region: NotRequired["capo_glue.types.value_string.ValueString"]
    """<p>Specified only if the base tables belong to a different Amazon Web Services Region.</p>"""
    catalog_id: "capo_glue.types.catalog_id_string.CatalogIdString"
    """<p>The catalog ID where the table resides.</p>"""
    database_name: "capo_glue.types.name_string.NameString"
    """<p>(Required) Specifies the name of a database that contains the table.</p>"""
    name: "capo_glue.types.name_string.NameString"
    """<p>(Required) Specifies the name of a table for which you are requesting metadata.</p>"""
    audit_context: NotRequired["capo_glue.types.audit_context.AuditContext"]
    """<p>A structure containing Lake Formation audit context information.</p>"""
    supported_permission_types: (
        "capo_glue.types.permission_type_list.PermissionTypeList"
    )
    """<p>Indicates the level of filtering a third-party analytical engine is capable of enforcing when calling the <code>GetUnfilteredTableMetadata</code> API operation. Accepted values are:</p> <ul> <li> <p> <code>COLUMN_PERMISSION</code> - Column permissions ensure that users can access only specific columns in the table. If there are particular columns contain sensitive data, data lake administrators can define column filters that exclude access to specific columns.</p> </li> <li> <p> <code>CELL_FILTER_PERMISSION</code> - Cell-level filtering combines column filtering (include or exclude columns) and row filter expressions to restrict access to individual elements in the table.</p> </li> <li> <p> <code>NESTED_PERMISSION</code> - Nested permissions combines cell-level filtering and nested column filtering to restrict access to columns and/or nested columns in specific rows based on row filter expressions.</p> </li> <li> <p> <code>NESTED_CELL_PERMISSION</code> - Nested cell permissions combines nested permission with nested cell-level filtering. This allows different subsets of nested columns to be restricted based on an array of row filter expressions. </p> </li> </ul> <p>Note: Each of these permission types follows a hierarchical order where each subsequent permission type includes all permission of the previous type.</p> <p>Important: If you provide a supported permission type that doesn't match the user's level of permissions on the table, then Lake Formation raises an exception. For example, if the third-party engine calling the <code>GetUnfilteredTableMetadata</code> operation can enforce only column-level filtering, and the user has nested cell filtering applied on the table, Lake Formation throws an exception, and will not return unfiltered table metadata and data access credentials.</p>"""
    parent_resource_arn: NotRequired["capo_glue.types.arn_string.ArnString"]
    """<p>The resource ARN of the view.</p>"""
    root_resource_arn: NotRequired["capo_glue.types.arn_string.ArnString"]
    """<p>The resource ARN of the root view in a chain of nested views.</p>"""
    supported_dialect: NotRequired["capo_glue.types.supported_dialect.SupportedDialect"]
    """<p>A structure specifying the dialect and dialect version used by the query engine.</p>"""
    permissions: NotRequired["capo_glue.types.permission_list.PermissionList"]
    """<p>The Lake Formation data permissions of the caller on the table. Used to authorize the call when no view context is found.</p>"""
    query_session_context: NotRequired[
        "capo_glue.types.query_session_context.QuerySessionContext"
    ]
    """<p>A structure used as a protocol between query engines and Lake Formation or Glue. Contains both a Lake Formation generated authorization identifier and information from the request's authorization context.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: GetUnfilteredTableMetadataRequest) -> dict:
    out: dict = {}
    if "region" in value:
        out["Region"] = value["region"]
    out["CatalogId"] = value["catalog_id"]
    out["DatabaseName"] = value["database_name"]
    out["Name"] = value["name"]
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
    if "parent_resource_arn" in value:
        out["ParentResourceArn"] = value["parent_resource_arn"]
    if "root_resource_arn" in value:
        out["RootResourceArn"] = value["root_resource_arn"]
    if "supported_dialect" in value:
        import capo_glue.types.supported_dialect

        out["SupportedDialect"] = (
            capo_glue.types.supported_dialect.serialize_aws_json_1_1(
                value["supported_dialect"]
            )
        )
    if "permissions" in value:
        import capo_glue.types.permission_list

        out["Permissions"] = capo_glue.types.permission_list.serialize_aws_json_1_1(
            value["permissions"]
        )
    if "query_session_context" in value:
        import capo_glue.types.query_session_context

        out["QuerySessionContext"] = (
            capo_glue.types.query_session_context.serialize_aws_json_1_1(
                value["query_session_context"]
            )
        )
    return out


def deserialize_aws_json_1_1(data: dict) -> GetUnfilteredTableMetadataRequest:
    out: GetUnfilteredTableMetadataRequest = {}  # type: ignore[typeddict-item]
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
    if data.get("Name") is not None:
        out["name"] = data["Name"]
    else:
        out["name"] = ""
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
    if data.get("ParentResourceArn") is not None:
        out["parent_resource_arn"] = data["ParentResourceArn"]
    if data.get("RootResourceArn") is not None:
        out["root_resource_arn"] = data["RootResourceArn"]
    if data.get("SupportedDialect") is not None:
        import capo_glue.types.supported_dialect

        out["supported_dialect"] = (
            capo_glue.types.supported_dialect.deserialize_aws_json_1_1(
                data["SupportedDialect"]
            )
        )
    if data.get("Permissions") is not None:
        import capo_glue.types.permission_list

        out["permissions"] = capo_glue.types.permission_list.deserialize_aws_json_1_1(
            data["Permissions"]
        )
    if data.get("QuerySessionContext") is not None:
        import capo_glue.types.query_session_context

        out["query_session_context"] = (
            capo_glue.types.query_session_context.deserialize_aws_json_1_1(
                data["QuerySessionContext"]
            )
        )
    return out
