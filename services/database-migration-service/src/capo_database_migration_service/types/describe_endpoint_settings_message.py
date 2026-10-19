"""Generated from Smithy shape ``com.amazonaws.databasemigrationservice#DescribeEndpointSettingsMessage``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_database_migration_service.types.integer_optional
    import capo_database_migration_service.types.string


class DescribeEndpointSettingsMessage(TypedDict, closed=True):
    engine_name: "capo_database_migration_service.types.string.String"
    """<p>The database engine used for your source or target endpoint.</p>"""
    max_records: NotRequired[
        "capo_database_migration_service.types.integer_optional.IntegerOptional"
    ]
    """<p>The maximum number of records to include in the response. If more records exist than the specified <code>MaxRecords</code> value, a pagination token called a marker is included in the response so that the remaining results can be retrieved.</p>"""
    marker: NotRequired["capo_database_migration_service.types.string.String"]
    """<p>An optional pagination token provided by a previous request. If this parameter is specified, the response includes only records beyond the marker, up to the value specified by <code>MaxRecords</code>.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: DescribeEndpointSettingsMessage) -> dict:
    out: dict = {}
    out["EngineName"] = value["engine_name"]
    if "max_records" in value:
        out["MaxRecords"] = value["max_records"]
    if "marker" in value:
        out["Marker"] = value["marker"]
    return out


def deserialize_aws_json_1_1(data: dict) -> DescribeEndpointSettingsMessage:
    out: DescribeEndpointSettingsMessage = {}  # type: ignore[typeddict-item]
    if data.get("EngineName") is not None:
        out["engine_name"] = data["EngineName"]
    else:
        out["engine_name"] = ""
    if data.get("MaxRecords") is not None:
        out["max_records"] = data["MaxRecords"]
    if data.get("Marker") is not None:
        out["marker"] = data["Marker"]
    return out
