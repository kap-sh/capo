"""Generated from Smithy shape ``com.amazonaws.glue#GetPartitionsRequest``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

from capo_glue.errors import DeserializationError

if TYPE_CHECKING:
    import capo_glue.types.audit_context
    import capo_glue.types.boolean_nullable
    import capo_glue.types.catalog_id_string
    import capo_glue.types.name_string
    import capo_glue.types.page_size
    import capo_glue.types.predicate_string
    import capo_glue.types.segment
    import capo_glue.types.timestamp
    import capo_glue.types.token
    import capo_glue.types.transaction_id_string


class GetPartitionsRequest(TypedDict, closed=True):
    catalog_id: NotRequired["capo_glue.types.catalog_id_string.CatalogIdString"]
    """<p>The ID of the Data Catalog where the partitions in question reside. If none is provided, the Amazon Web Services account ID is used by default.</p>"""
    database_name: "capo_glue.types.name_string.NameString"
    """<p>The name of the catalog database where the partitions reside.</p>"""
    table_name: "capo_glue.types.name_string.NameString"
    """<p>The name of the partitions' table.</p>"""
    expression: NotRequired["capo_glue.types.predicate_string.PredicateString"]
    """<p>An expression that filters the partitions to be returned.</p> <p>The expression uses SQL syntax similar to the SQL <code>WHERE</code> filter clause. The SQL statement parser <a href="http://jsqlparser.sourceforge.net/home.php">JSQLParser</a> parses the expression. </p> <p> <i>Operators</i>: The following are the operators that you can use in the <code>Expression</code> API call:</p> <dl> <dt>=</dt> <dd> <p>Checks whether the values of the two operands are equal; if yes, then the condition becomes true.</p> <p>Example: Assume 'variable a' holds 10 and 'variable b' holds 20. </p> <p>(a = b) is not true.</p> </dd> <dt>< ></dt> <dd> <p>Checks whether the values of two operands are equal; if the values are not equal, then the condition becomes true.</p> <p>Example: (a < > b) is true.</p> </dd> <dt>></dt> <dd> <p>Checks whether the value of the left operand is greater than the value of the right operand; if yes, then the condition becomes true.</p> <p>Example: (a > b) is not true.</p> </dd> <dt><</dt> <dd> <p>Checks whether the value of the left operand is less than the value of the right operand; if yes, then the condition becomes true.</p> <p>Example: (a < b) is true.</p> </dd> <dt>>=</dt> <dd> <p>Checks whether the value of the left operand is greater than or equal to the value of the right operand; if yes, then the condition becomes true.</p> <p>Example: (a >= b) is not true.</p> </dd> <dt><=</dt> <dd> <p>Checks whether the value of the left operand is less than or equal to the value of the right operand; if yes, then the condition becomes true.</p> <p>Example: (a <= b) is true.</p> </dd> <dt>AND, OR, IN, BETWEEN, LIKE, NOT, IS NULL</dt> <dd> <p>Logical operators.</p> </dd> </dl> <p> <i>Supported Partition Key Types</i>: The following are the supported partition keys.</p> <ul> <li> <p> <code>string</code> </p> </li> <li> <p> <code>date</code> </p> </li> <li> <p> <code>timestamp</code> </p> </li> <li> <p> <code>int</code> </p> </li> <li> <p> <code>bigint</code> </p> </li> <li> <p> <code>long</code> </p> </li> <li> <p> <code>tinyint</code> </p> </li> <li> <p> <code>smallint</code> </p> </li> <li> <p> <code>decimal</code> </p> </li> </ul> <p>If an type is encountered that is not valid, an exception is thrown. </p> <p>The following list shows the valid operators on each type. When you define a crawler, the <code>partitionKey</code> type is created as a <code>STRING</code>, to be compatible with the catalog partitions. </p> <p> <i>Sample API Call</i>: </p>"""
    next_token: NotRequired["capo_glue.types.token.Token"]
    """<p>A continuation token, if this is not the first call to retrieve these partitions.</p>"""
    segment: NotRequired["capo_glue.types.segment.Segment"]
    """<p>The segment of the table's partitions to scan in this request.</p>"""
    max_results: NotRequired["capo_glue.types.page_size.PageSize"]
    """<p>The maximum number of partitions to return in a single response.</p>"""
    exclude_column_schema: NotRequired[
        "capo_glue.types.boolean_nullable.BooleanNullable"
    ]
    """<p>When true, specifies not returning the partition column schema. Useful when you are interested only in other partition attributes such as partition values or location. This approach avoids the problem of a large response by not returning duplicate data.</p>"""
    transaction_id: NotRequired[
        "capo_glue.types.transaction_id_string.TransactionIdString"
    ]
    """<p>The transaction ID at which to read the partition contents.</p>"""
    query_as_of_time: NotRequired["capo_glue.types.timestamp.Timestamp"]
    """<p>The time as of when to read the partition contents. If not set, the most recent transaction commit time will be used. Cannot be specified along with <code>TransactionId</code>.</p>"""
    audit_context: NotRequired["capo_glue.types.audit_context.AuditContext"]


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: GetPartitionsRequest) -> dict:
    out: dict = {}
    if "catalog_id" in value:
        out["CatalogId"] = value["catalog_id"]
    out["DatabaseName"] = value["database_name"]
    out["TableName"] = value["table_name"]
    if "expression" in value:
        out["Expression"] = value["expression"]
    if "next_token" in value:
        out["NextToken"] = value["next_token"]
    if "segment" in value:
        import capo_glue.types.segment

        out["Segment"] = capo_glue.types.segment.serialize_aws_json_1_1(
            value["segment"]
        )
    if "max_results" in value:
        out["MaxResults"] = value["max_results"]
    if "exclude_column_schema" in value:
        out["ExcludeColumnSchema"] = value["exclude_column_schema"]
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
    return out


def deserialize_aws_json_1_1(data: dict) -> GetPartitionsRequest:
    out: GetPartitionsRequest = {}  # type: ignore[typeddict-item]
    if data.get("CatalogId") is not None:
        out["catalog_id"] = data["CatalogId"]
    if data.get("DatabaseName") is not None:
        out["database_name"] = data["DatabaseName"]
    else:
        raise DeserializationError("GetPartitionsRequest.database_name required")
    if data.get("TableName") is not None:
        out["table_name"] = data["TableName"]
    else:
        raise DeserializationError("GetPartitionsRequest.table_name required")
    if data.get("Expression") is not None:
        out["expression"] = data["Expression"]
    if data.get("NextToken") is not None:
        out["next_token"] = data["NextToken"]
    if data.get("Segment") is not None:
        import capo_glue.types.segment

        out["segment"] = capo_glue.types.segment.deserialize_aws_json_1_1(
            data["Segment"]
        )
    if data.get("MaxResults") is not None:
        out["max_results"] = data["MaxResults"]
    if data.get("ExcludeColumnSchema") is not None:
        out["exclude_column_schema"] = data["ExcludeColumnSchema"]
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
    return out
