"""Generated from Smithy shape ``com.amazonaws.databasemigrationservice#DescribeReplicationTableStatisticsMessage``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_database_migration_service.types.filter_list
    import capo_database_migration_service.types.integer_optional
    import capo_database_migration_service.types.string


class DescribeReplicationTableStatisticsMessage(TypedDict, closed=True):
    replication_config_arn: "capo_database_migration_service.types.string.String"
    """<p>The replication config to describe.</p>"""
    max_records: NotRequired[
        "capo_database_migration_service.types.integer_optional.IntegerOptional"
    ]
    """<p>The maximum number of records to include in the response. If more records exist than the specified <code>MaxRecords</code> value, a pagination token called a marker is included in the response so that the remaining results can be retrieved. </p>"""
    marker: NotRequired["capo_database_migration_service.types.string.String"]
    """<p>An optional pagination token provided by a previous request. If this parameter is specified, the response includes only records beyond the marker, up to the value specified by <code>MaxRecords</code>. </p>"""
    filters: NotRequired["capo_database_migration_service.types.filter_list.FilterList"]
    """<p>Filters applied to the replication table statistics.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: DescribeReplicationTableStatisticsMessage) -> dict:
    out: dict = {}
    out["ReplicationConfigArn"] = value["replication_config_arn"]
    if "max_records" in value:
        out["MaxRecords"] = value["max_records"]
    if "marker" in value:
        out["Marker"] = value["marker"]
    if "filters" in value:
        import capo_database_migration_service.types.filter_list

        out["Filters"] = (
            capo_database_migration_service.types.filter_list.serialize_aws_json_1_1(
                value["filters"]
            )
        )
    return out


def deserialize_aws_json_1_1(data: dict) -> DescribeReplicationTableStatisticsMessage:
    out: DescribeReplicationTableStatisticsMessage = {}  # type: ignore[typeddict-item]
    if data.get("ReplicationConfigArn") is not None:
        out["replication_config_arn"] = data["ReplicationConfigArn"]
    else:
        out["replication_config_arn"] = ""
    if data.get("MaxRecords") is not None:
        out["max_records"] = data["MaxRecords"]
    if data.get("Marker") is not None:
        out["marker"] = data["Marker"]
    if data.get("Filters") is not None:
        import capo_database_migration_service.types.filter_list

        out["filters"] = (
            capo_database_migration_service.types.filter_list.deserialize_aws_json_1_1(
                data["Filters"]
            )
        )
    return out
