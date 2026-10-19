"""Generated from Smithy shape ``com.amazonaws.redshiftdata#GetStatementResultResponse``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_redshift_data.types.column_metadata_list
    import capo_redshift_data.types.long
    import capo_redshift_data.types.sql_records
    import capo_redshift_data.types.string


class GetStatementResultResponse(TypedDict, closed=True):
    records: "capo_redshift_data.types.sql_records.SqlRecords"
    """<p>The results of the SQL statement in JSON format.</p>"""
    column_metadata: NotRequired[
        "capo_redshift_data.types.column_metadata_list.ColumnMetadataList"
    ]
    """<p>The properties (metadata) of a column. </p>"""
    total_num_rows: "capo_redshift_data.types.long.Long"
    """<p>The total number of rows in the result set returned from a query. You can use this number to estimate the number of calls to the <code>GetStatementResult</code> operation needed to page through the results. </p>"""
    next_token: NotRequired["capo_redshift_data.types.string.String"]
    """<p>A value that indicates the starting point for the next set of response records in a subsequent request. If a value is returned in a response, you can retrieve the next set of records by providing this returned NextToken value in the next NextToken parameter and retrying the command. If the NextToken field is empty, all response records have been retrieved for the request. </p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: GetStatementResultResponse) -> dict:
    out: dict = {}
    import capo_redshift_data.types.sql_records

    out["Records"] = capo_redshift_data.types.sql_records.serialize_aws_json_1_1(
        value["records"]
    )
    if "column_metadata" in value:
        import capo_redshift_data.types.column_metadata_list

        out["ColumnMetadata"] = (
            capo_redshift_data.types.column_metadata_list.serialize_aws_json_1_1(
                value["column_metadata"]
            )
        )
    out["TotalNumRows"] = value.get("total_num_rows", 0)
    if "next_token" in value:
        out["NextToken"] = value["next_token"]
    return out


def deserialize_aws_json_1_1(data: dict) -> GetStatementResultResponse:
    out: GetStatementResultResponse = {}  # type: ignore[typeddict-item]
    if data.get("Records") is not None:
        import capo_redshift_data.types.sql_records

        out["records"] = capo_redshift_data.types.sql_records.deserialize_aws_json_1_1(
            data["Records"]
        )
    else:
        out["records"] = []
    if data.get("ColumnMetadata") is not None:
        import capo_redshift_data.types.column_metadata_list

        out["column_metadata"] = (
            capo_redshift_data.types.column_metadata_list.deserialize_aws_json_1_1(
                data["ColumnMetadata"]
            )
        )
    if data.get("TotalNumRows") is not None:
        out["total_num_rows"] = data["TotalNumRows"]
    else:
        out["total_num_rows"] = 0
    if data.get("NextToken") is not None:
        out["next_token"] = data["NextToken"]
    return out
