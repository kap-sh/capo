"""Generated from Smithy shape ``com.amazonaws.databasemigrationservice#DescribeFleetAdvisorDatabasesRequest``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_database_migration_service.types.filter_list
    import capo_database_migration_service.types.integer_optional
    import capo_database_migration_service.types.string


class DescribeFleetAdvisorDatabasesRequest(TypedDict, closed=True):
    filters: NotRequired["capo_database_migration_service.types.filter_list.FilterList"]
    """<p> If you specify any of the following filters, the output includes information for only those databases that meet the filter criteria: </p> <ul> <li> <p> <code>database-id</code> – The ID of the database.</p> </li> <li> <p> <code>database-name</code> – The name of the database.</p> </li> <li> <p> <code>database-engine</code> – The name of the database engine.</p> </li> <li> <p> <code>server-ip-address</code> – The IP address of the database server.</p> </li> <li> <p> <code>database-ip-address</code> – The IP address of the database.</p> </li> <li> <p> <code>collector-name</code> – The name of the associated Fleet Advisor collector.</p> </li> </ul> <p>An example is: <code>describe-fleet-advisor-databases --filter Name="database-id",Values="45"</code> </p>"""
    max_records: NotRequired[
        "capo_database_migration_service.types.integer_optional.IntegerOptional"
    ]
    """<p>Sets the maximum number of records returned in the response.</p>"""
    next_token: NotRequired["capo_database_migration_service.types.string.String"]
    """<p>If <code>NextToken</code> is returned by a previous response, there are more results available. The value of <code>NextToken</code> is a unique pagination token for each page. Make the call again using the returned token to retrieve the next page. Keep all other arguments unchanged. </p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: DescribeFleetAdvisorDatabasesRequest) -> dict:
    out: dict = {}
    if "filters" in value:
        import capo_database_migration_service.types.filter_list

        out["Filters"] = (
            capo_database_migration_service.types.filter_list.serialize_aws_json_1_1(
                value["filters"]
            )
        )
    if "max_records" in value:
        out["MaxRecords"] = value["max_records"]
    if "next_token" in value:
        out["NextToken"] = value["next_token"]
    return out


def deserialize_aws_json_1_1(data: dict) -> DescribeFleetAdvisorDatabasesRequest:
    out: DescribeFleetAdvisorDatabasesRequest = {}  # type: ignore[typeddict-item]
    if data.get("Filters") is not None:
        import capo_database_migration_service.types.filter_list

        out["filters"] = (
            capo_database_migration_service.types.filter_list.deserialize_aws_json_1_1(
                data["Filters"]
            )
        )
    if data.get("MaxRecords") is not None:
        out["max_records"] = data["MaxRecords"]
    if data.get("NextToken") is not None:
        out["next_token"] = data["NextToken"]
    return out
