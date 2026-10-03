"""Generated from Smithy shape ``com.amazonaws.rdsdata#ExecuteStatementResponse``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_rds_data.types.field_list
    import capo_rds_data.types.formatted_sql_records
    import capo_rds_data.types.metadata
    import capo_rds_data.types.records_updated
    import capo_rds_data.types.sql_records


class ExecuteStatementResponse(TypedDict, closed=True):
    records: NotRequired["capo_rds_data.types.sql_records.SqlRecords"]
    """<p>The records returned by the SQL statement. This field is blank if the <code>formatRecordsAs</code> parameter is set to <code>JSON</code>.</p>"""
    column_metadata: NotRequired["capo_rds_data.types.metadata.Metadata"]
    """<p>Metadata for the columns included in the results. This field is blank if the <code>formatRecordsAs</code> parameter is set to <code>JSON</code>.</p>"""
    number_of_records_updated: "capo_rds_data.types.records_updated.RecordsUpdated"
    """<p>The number of records updated by the request.</p>"""
    generated_fields: NotRequired["capo_rds_data.types.field_list.FieldList"]
    """<p>Values for fields generated during a DML request.</p> <note> <p>The <code>generatedFields</code> data isn't supported by Aurora PostgreSQL. To get the values of generated fields, use the <code>RETURNING</code> clause. For more information, see <a href="https://www.postgresql.org/docs/10/dml-returning.html">Returning Data From Modified Rows</a> in the PostgreSQL documentation.</p> </note>"""
    formatted_records: NotRequired[
        "capo_rds_data.types.formatted_sql_records.FormattedSqlRecords"
    ]
    """<p>A string value that represents the result set of a <code>SELECT</code> statement in JSON format. This value is only present when the <code>formatRecordsAs</code> parameter is set to <code>JSON</code>.</p> <p>The size limit for this field is currently 10 MB. If the JSON-formatted string representing the result set requires more than 10 MB, the call returns an error.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: ExecuteStatementResponse) -> dict:
    out: dict = {}
    if "records" in value:
        import capo_rds_data.types.sql_records

        out["records"] = capo_rds_data.types.sql_records.serialize_json(
            value["records"]
        )
    if "column_metadata" in value:
        import capo_rds_data.types.metadata

        out["columnMetadata"] = capo_rds_data.types.metadata.serialize_json(
            value["column_metadata"]
        )
    out["numberOfRecordsUpdated"] = value.get("number_of_records_updated", 0)
    if "generated_fields" in value:
        import capo_rds_data.types.field_list

        out["generatedFields"] = capo_rds_data.types.field_list.serialize_json(
            value["generated_fields"]
        )
    if "formatted_records" in value:
        out["formattedRecords"] = value["formatted_records"]
    return out


def deserialize_json(data: dict) -> ExecuteStatementResponse:
    out: ExecuteStatementResponse = {}  # type: ignore[typeddict-item]
    if data.get("records") is not None:
        import capo_rds_data.types.sql_records

        out["records"] = capo_rds_data.types.sql_records.deserialize_json(
            data["records"]
        )
    if data.get("columnMetadata") is not None:
        import capo_rds_data.types.metadata

        out["column_metadata"] = capo_rds_data.types.metadata.deserialize_json(
            data["columnMetadata"]
        )
    if data.get("numberOfRecordsUpdated") is not None:
        out["number_of_records_updated"] = data["numberOfRecordsUpdated"]
    else:
        out["number_of_records_updated"] = 0
    if data.get("generatedFields") is not None:
        import capo_rds_data.types.field_list

        out["generated_fields"] = capo_rds_data.types.field_list.deserialize_json(
            data["generatedFields"]
        )
    if data.get("formattedRecords") is not None:
        out["formatted_records"] = data["formattedRecords"]
    return out
