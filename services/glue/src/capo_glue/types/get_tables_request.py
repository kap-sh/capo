"""Generated from Smithy shape ``com.amazonaws.glue#GetTablesRequest``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

from capo_glue.errors import DeserializationError

if TYPE_CHECKING:
    import capo_glue.types.audit_context
    import capo_glue.types.boolean_nullable
    import capo_glue.types.catalog_getter_page_size
    import capo_glue.types.catalog_id_string
    import capo_glue.types.filter_string
    import capo_glue.types.name_string
    import capo_glue.types.table_attributes_list
    import capo_glue.types.table_resource_share_type
    import capo_glue.types.timestamp
    import capo_glue.types.token
    import capo_glue.types.transaction_id_string


class GetTablesRequest(TypedDict, closed=True):
    catalog_id: NotRequired["capo_glue.types.catalog_id_string.CatalogIdString"]
    """<p>The ID of the Data Catalog where the tables reside. If none is provided, the Amazon Web Services account ID is used by default.</p>"""
    database_name: "capo_glue.types.name_string.NameString"
    """<p>The database in the catalog whose tables to list. For Hive compatibility, this name is entirely lowercase.</p>"""
    expression: NotRequired["capo_glue.types.filter_string.FilterString"]
    """<p>A regular expression pattern. If present, only those tables whose names match the pattern are returned.</p>"""
    next_token: NotRequired["capo_glue.types.token.Token"]
    """<p>A continuation token, included if this is a continuation call.</p>"""
    max_results: NotRequired[
        "capo_glue.types.catalog_getter_page_size.CatalogGetterPageSize"
    ]
    """<p>The maximum number of tables to return in a single response.</p>"""
    transaction_id: NotRequired[
        "capo_glue.types.transaction_id_string.TransactionIdString"
    ]
    """<p>The transaction ID at which to read the table contents.</p>"""
    query_as_of_time: NotRequired["capo_glue.types.timestamp.Timestamp"]
    """<p>The time as of when to read the table contents. If not set, the most recent transaction commit time will be used. Cannot be specified along with <code>TransactionId</code>.</p>"""
    audit_context: NotRequired["capo_glue.types.audit_context.AuditContext"]
    """<p>A structure containing the Lake Formation <a href="https://docs.aws.amazon.com/glue/latest/webapi/API_AuditContext.html">audit context</a>.</p>"""
    resource_share_type: NotRequired[
        "capo_glue.types.table_resource_share_type.TableResourceShareType"
    ]
    """<p>Specifies which tables the <code>GetTables</code> call returns. The allowable values are <code>FEDERATED</code> or <code>ALL</code>. </p> <ul> <li> <p>If set to <code>FEDERATED</code>, returns only federated tables, which reference an entity outside the Glue Data Catalog.</p> </li> <li> <p>If set to <code>ALL</code>, returns all tables in the database, both federated and non-federated. </p> </li> </ul>"""
    include_status_details: NotRequired[
        "capo_glue.types.boolean_nullable.BooleanNullable"
    ]
    """<p>Specifies whether to include status details related to a request to create or update an Glue Data Catalog view.</p>"""
    attributes_to_get: NotRequired[
        "capo_glue.types.table_attributes_list.TableAttributesList"
    ]
    """<p> Specifies the table fields returned by the <code>GetTables</code> call. This parameter doesn’t accept an empty list. The request must include <code>NAME</code>.</p> <p>The following are the valid combinations of values:</p> <ul> <li> <p> <code>NAME</code> - Names of all tables in the database.</p> </li> <li> <p> <code>NAME</code>, <code>TABLE_TYPE</code> - Names of all tables and the table types.</p> </li> </ul>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: GetTablesRequest) -> dict:
    out: dict = {}
    if "catalog_id" in value:
        out["CatalogId"] = value["catalog_id"]
    out["DatabaseName"] = value["database_name"]
    if "expression" in value:
        out["Expression"] = value["expression"]
    if "next_token" in value:
        out["NextToken"] = value["next_token"]
    if "max_results" in value:
        out["MaxResults"] = value["max_results"]
    if "transaction_id" in value:
        out["TransactionId"] = value["transaction_id"]
    if "query_as_of_time" in value:
        import capo_glue.types.timestamp

        out["QueryAsOfTime"] = capo_glue.types.timestamp.serialize_aws_json_1_1(
            value["query_as_of_time"]
        )
    if "audit_context" in value:
        import capo_glue.types.audit_context

        out["AuditContext"] = capo_glue.types.audit_context.serialize_aws_json_1_1(
            value["audit_context"]
        )
    if "resource_share_type" in value:
        import capo_glue.types.table_resource_share_type

        out["ResourceShareType"] = (
            capo_glue.types.table_resource_share_type.serialize_aws_json_1_1(
                value["resource_share_type"]
            )
        )
    if "include_status_details" in value:
        out["IncludeStatusDetails"] = value["include_status_details"]
    if "attributes_to_get" in value:
        import capo_glue.types.table_attributes_list

        out["AttributesToGet"] = (
            capo_glue.types.table_attributes_list.serialize_aws_json_1_1(
                value["attributes_to_get"]
            )
        )
    return out


def deserialize_aws_json_1_1(data: dict) -> GetTablesRequest:
    out: GetTablesRequest = {}  # type: ignore[typeddict-item]
    if data.get("CatalogId") is not None:
        out["catalog_id"] = data["CatalogId"]
    if data.get("DatabaseName") is not None:
        out["database_name"] = data["DatabaseName"]
    else:
        raise DeserializationError("GetTablesRequest.database_name required")
    if data.get("Expression") is not None:
        out["expression"] = data["Expression"]
    if data.get("NextToken") is not None:
        out["next_token"] = data["NextToken"]
    if data.get("MaxResults") is not None:
        out["max_results"] = data["MaxResults"]
    if data.get("TransactionId") is not None:
        out["transaction_id"] = data["TransactionId"]
    if data.get("QueryAsOfTime") is not None:
        import capo_glue.types.timestamp

        out["query_as_of_time"] = capo_glue.types.timestamp.deserialize_aws_json_1_1(
            data["QueryAsOfTime"]
        )
    if data.get("AuditContext") is not None:
        import capo_glue.types.audit_context

        out["audit_context"] = capo_glue.types.audit_context.deserialize_aws_json_1_1(
            data["AuditContext"]
        )
    if data.get("ResourceShareType") is not None:
        import capo_glue.types.table_resource_share_type

        out["resource_share_type"] = (
            capo_glue.types.table_resource_share_type.deserialize_aws_json_1_1(
                data["ResourceShareType"]
            )
        )
    if data.get("IncludeStatusDetails") is not None:
        out["include_status_details"] = data["IncludeStatusDetails"]
    if data.get("AttributesToGet") is not None:
        import capo_glue.types.table_attributes_list

        out["attributes_to_get"] = (
            capo_glue.types.table_attributes_list.deserialize_aws_json_1_1(
                data["AttributesToGet"]
            )
        )
    return out
