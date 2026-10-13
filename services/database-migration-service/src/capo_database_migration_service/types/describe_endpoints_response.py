"""Generated from Smithy shape ``com.amazonaws.databasemigrationservice#DescribeEndpointsResponse``."""

from typing import TYPE_CHECKING, Any

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_database_migration_service.types.endpoint_list
    import capo_database_migration_service.types.string


class DescribeEndpointsResponse(TypedDict, closed=True):
    marker: NotRequired["capo_database_migration_service.types.string.String"]
    """<p> An optional pagination token provided by a previous request. If this parameter is specified, the response includes only records beyond the marker, up to the value specified by <code>MaxRecords</code>. </p>"""
    endpoints: NotRequired[
        "capo_database_migration_service.types.endpoint_list.EndpointList"
    ]
    """<p>Endpoint description.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: DescribeEndpointsResponse) -> dict:
    out: dict = {}
    if "marker" in value:
        out["Marker"] = value["marker"]
    if "endpoints" in value:
        import capo_database_migration_service.types.endpoint_list

        out["Endpoints"] = (
            capo_database_migration_service.types.endpoint_list.serialize_aws_json_1_1(
                value["endpoints"]
            )
        )
    return out


def deserialize_aws_json_1_1(data: dict) -> DescribeEndpointsResponse:
    out: DescribeEndpointsResponse = {}  # type: ignore[typeddict-item]
    if data.get("Marker") is not None:
        out["marker"] = data["Marker"]
    if data.get("Endpoints") is not None:
        import capo_database_migration_service.types.endpoint_list

        out["endpoints"] = (
            capo_database_migration_service.types.endpoint_list.deserialize_aws_json_1_1(
                data["Endpoints"]
            )
        )
    return out


def redact_sensitive(value: DescribeEndpointsResponse) -> dict[str, Any]:
    out: dict[str, Any] = dict(value)
    if "endpoints" in value:
        import capo_database_migration_service.types.endpoint_list

        out["endpoints"] = (
            capo_database_migration_service.types.endpoint_list.redact_sensitive(
                value["endpoints"]
            )
        )
    return out
