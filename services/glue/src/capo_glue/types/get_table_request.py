"""Generated from Smithy shape ``com.amazonaws.glue#GetTableRequest``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

from capo_glue.errors import DeserializationError

if TYPE_CHECKING:
    import capo_glue.types.audit_context
    import capo_glue.types.boolean_nullable
    import capo_glue.types.catalog_id_string
    import capo_glue.types.name_string
    import capo_glue.types.table_attributes_list
    import capo_glue.types.timestamp
    import capo_glue.types.transaction_id_string


class GetTableRequest(TypedDict, closed=True):
    catalog_id: NotRequired["capo_glue.types.catalog_id_string.CatalogIdString"]
    """<p>The ID of the Data Catalog where the table resides. If none is provided, the Amazon Web Services account ID is used by default.</p>"""
    database_name: "capo_glue.types.name_string.NameString"
    """<p>The name of the database in the catalog in which the table resides. For Hive compatibility, this name is entirely lowercase.</p>"""
    name: "capo_glue.types.name_string.NameString"
    """<p>The name of the table for which to retrieve the definition. For Hive compatibility, this name is entirely lowercase.</p>"""
    transaction_id: NotRequired[
        "capo_glue.types.transaction_id_string.TransactionIdString"
    ]
    """<p>The transaction ID at which to read the table contents. </p>"""
    query_as_of_time: NotRequired["capo_glue.types.timestamp.Timestamp"]
    """<p>The time as of when to read the table contents. If not set, the most recent transaction commit time will be used. Cannot be specified along with <code>TransactionId</code>.</p>"""
    audit_context: NotRequired["capo_glue.types.audit_context.AuditContext"]
    """<p>A structure containing the Lake Formation <a href="https://docs.aws.amazon.com/glue/latest/webapi/API_AuditContext.html">audit context</a>.</p>"""
    include_status_details: NotRequired[
        "capo_glue.types.boolean_nullable.BooleanNullable"
    ]
    """<p>Specifies whether to include status details related to a request to create or update an Glue Data Catalog view.</p>"""
    attributes_to_get: NotRequired[
        "capo_glue.types.table_attributes_list.TableAttributesList"
    ]
    """<p>Specifies the table fields returned by the <code>GetTable</code> call. This parameter doesn't accept an empty list.</p> <p>The following are the valid combinations of values:</p> <ul> <li> <p> <code>DEFAULT</code> - Returns the Hive-style table definition only.</p> </li> <li> <p> <code>LATEST_ICEBERG_METADATA</code> - Returns only the latest Apache Iceberg table metadata.</p> </li> <li> <p> <code>DEFAULT</code>, <code>LATEST_ICEBERG_METADATA</code> - Returns both the Hive-style table definition and the latest Apache Iceberg table metadata.</p> </li> </ul>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: GetTableRequest) -> dict:
    out: dict = {}
    if "catalog_id" in value:
        out["CatalogId"] = value["catalog_id"]
    out["DatabaseName"] = value["database_name"]
    out["Name"] = value["name"]
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


def deserialize_aws_json_1_1(data: dict) -> GetTableRequest:
    out: GetTableRequest = {}  # type: ignore[typeddict-item]
    if data.get("CatalogId") is not None:
        out["catalog_id"] = data["CatalogId"]
    if data.get("DatabaseName") is not None:
        out["database_name"] = data["DatabaseName"]
    else:
        raise DeserializationError("GetTableRequest.database_name required")
    if data.get("Name") is not None:
        out["name"] = data["Name"]
    else:
        raise DeserializationError("GetTableRequest.name required")
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
