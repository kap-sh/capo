"""Generated from Smithy shape ``com.amazonaws.lakeformation#GetTableObjectsRequest``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

from capo_lakeformation.errors import DeserializationError

if TYPE_CHECKING:
    import capo_lakeformation.types.catalog_id_string
    import capo_lakeformation.types.name_string
    import capo_lakeformation.types.page_size
    import capo_lakeformation.types.predicate_string
    import capo_lakeformation.types.timestamp
    import capo_lakeformation.types.token_string
    import capo_lakeformation.types.transaction_id_string


class GetTableObjectsRequest(TypedDict, closed=True):
    catalog_id: NotRequired[
        "capo_lakeformation.types.catalog_id_string.CatalogIdString"
    ]
    """<p>The catalog containing the governed table. Defaults to the caller’s account.</p>"""
    database_name: "capo_lakeformation.types.name_string.NameString"
    """<p>The database containing the governed table.</p>"""
    table_name: "capo_lakeformation.types.name_string.NameString"
    """<p>The governed table for which to retrieve objects.</p>"""
    transaction_id: NotRequired[
        "capo_lakeformation.types.transaction_id_string.TransactionIdString"
    ]
    """<p>The transaction ID at which to read the governed table contents. If this transaction has aborted, an error is returned. If not set, defaults to the most recent committed transaction. Cannot be specified along with <code>QueryAsOfTime</code>.</p>"""
    query_as_of_time: NotRequired["capo_lakeformation.types.timestamp.Timestamp"]
    """<p>The time as of when to read the governed table contents. If not set, the most recent transaction commit time is used. Cannot be specified along with <code>TransactionId</code>.</p>"""
    partition_predicate: NotRequired[
        "capo_lakeformation.types.predicate_string.PredicateString"
    ]
    """<p>A predicate to filter the objects returned based on the partition keys defined in the governed table.</p> <ul> <li> <p>The comparison operators supported are: =, >, <, >=, <=</p> </li> <li> <p>The logical operators supported are: AND</p> </li> <li> <p>The data types supported are integer, long, date(yyyy-MM-dd), timestamp(yyyy-MM-dd HH:mm:ssXXX or yyyy-MM-dd HH:mm:ss"), string and decimal.</p> </li> </ul>"""
    max_results: NotRequired["capo_lakeformation.types.page_size.PageSize"]
    """<p>Specifies how many values to return in a page.</p>"""
    next_token: NotRequired["capo_lakeformation.types.token_string.TokenString"]
    """<p>A continuation token if this is not the first call to retrieve these objects.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: GetTableObjectsRequest) -> dict:
    out: dict = {}
    if "catalog_id" in value:
        out["CatalogId"] = value["catalog_id"]
    out["DatabaseName"] = value["database_name"]
    out["TableName"] = value["table_name"]
    if "transaction_id" in value:
        out["TransactionId"] = value["transaction_id"]
    if "query_as_of_time" in value:
        import capo_lakeformation.types.timestamp

        out["QueryAsOfTime"] = capo_lakeformation.types.timestamp.serialize_json(
            value["query_as_of_time"]
        )
    if "partition_predicate" in value:
        out["PartitionPredicate"] = value["partition_predicate"]
    if "max_results" in value:
        out["MaxResults"] = value["max_results"]
    if "next_token" in value:
        out["NextToken"] = value["next_token"]
    return out


def deserialize_json(data: dict) -> GetTableObjectsRequest:
    out: GetTableObjectsRequest = {}  # type: ignore[typeddict-item]
    if data.get("CatalogId") is not None:
        out["catalog_id"] = data["CatalogId"]
    if data.get("DatabaseName") is not None:
        out["database_name"] = data["DatabaseName"]
    else:
        raise DeserializationError("GetTableObjectsRequest.database_name required")
    if data.get("TableName") is not None:
        out["table_name"] = data["TableName"]
    else:
        raise DeserializationError("GetTableObjectsRequest.table_name required")
    if data.get("TransactionId") is not None:
        out["transaction_id"] = data["TransactionId"]
    if data.get("QueryAsOfTime") is not None:
        import capo_lakeformation.types.timestamp

        out["query_as_of_time"] = capo_lakeformation.types.timestamp.deserialize_json(
            data["QueryAsOfTime"]
        )
    if data.get("PartitionPredicate") is not None:
        out["partition_predicate"] = data["PartitionPredicate"]
    if data.get("MaxResults") is not None:
        out["max_results"] = data["MaxResults"]
    if data.get("NextToken") is not None:
        out["next_token"] = data["NextToken"]
    return out
