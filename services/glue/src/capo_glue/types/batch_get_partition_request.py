"""Generated from Smithy shape ``com.amazonaws.glue#BatchGetPartitionRequest``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_glue.types.audit_context
    import capo_glue.types.batch_get_partition_value_list
    import capo_glue.types.catalog_id_string
    import capo_glue.types.name_string
    import capo_glue.types.query_session_context


class BatchGetPartitionRequest(TypedDict, closed=True):
    catalog_id: NotRequired["capo_glue.types.catalog_id_string.CatalogIdString"]
    """<p>The ID of the Data Catalog where the partitions in question reside. If none is supplied, the Amazon Web Services account ID is used by default.</p>"""
    database_name: "capo_glue.types.name_string.NameString"
    """<p>The name of the catalog database where the partitions reside.</p>"""
    table_name: "capo_glue.types.name_string.NameString"
    """<p>The name of the partitions' table.</p>"""
    partitions_to_get: (
        "capo_glue.types.batch_get_partition_value_list.BatchGetPartitionValueList"
    )
    """<p>A list of partition values identifying the partitions to retrieve.</p>"""
    audit_context: NotRequired["capo_glue.types.audit_context.AuditContext"]
    query_session_context: NotRequired[
        "capo_glue.types.query_session_context.QuerySessionContext"
    ]


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: BatchGetPartitionRequest) -> dict:
    out: dict = {}
    if "catalog_id" in value:
        out["CatalogId"] = value["catalog_id"]
    out["DatabaseName"] = value["database_name"]
    out["TableName"] = value["table_name"]
    import capo_glue.types.batch_get_partition_value_list

    out["PartitionsToGet"] = (
        capo_glue.types.batch_get_partition_value_list.serialize_aws_json_1_1(
            value["partitions_to_get"]
        )
    )
    if "audit_context" in value:
        import capo_glue.types.audit_context

        out["AuditContext"] = capo_glue.types.audit_context.serialize_aws_json_1_1(
            value["audit_context"]
        )
    if "query_session_context" in value:
        import capo_glue.types.query_session_context

        out["QuerySessionContext"] = (
            capo_glue.types.query_session_context.serialize_aws_json_1_1(
                value["query_session_context"]
            )
        )
    return out


def deserialize_aws_json_1_1(data: dict) -> BatchGetPartitionRequest:
    out: BatchGetPartitionRequest = {}  # type: ignore[typeddict-item]
    if data.get("CatalogId") is not None:
        out["catalog_id"] = data["CatalogId"]
    if data.get("DatabaseName") is not None:
        out["database_name"] = data["DatabaseName"]
    else:
        out["database_name"] = ""
    if data.get("TableName") is not None:
        out["table_name"] = data["TableName"]
    else:
        out["table_name"] = ""
    if data.get("PartitionsToGet") is not None:
        import capo_glue.types.batch_get_partition_value_list

        out["partitions_to_get"] = (
            capo_glue.types.batch_get_partition_value_list.deserialize_aws_json_1_1(
                data["PartitionsToGet"]
            )
        )
    else:
        out["partitions_to_get"] = []
    if data.get("AuditContext") is not None:
        import capo_glue.types.audit_context

        out["audit_context"] = capo_glue.types.audit_context.deserialize_aws_json_1_1(
            data["AuditContext"]
        )
    if data.get("QuerySessionContext") is not None:
        import capo_glue.types.query_session_context

        out["query_session_context"] = (
            capo_glue.types.query_session_context.deserialize_aws_json_1_1(
                data["QuerySessionContext"]
            )
        )
    return out
