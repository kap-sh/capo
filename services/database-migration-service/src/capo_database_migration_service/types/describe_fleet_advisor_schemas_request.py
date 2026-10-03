"""Generated from Smithy shape ``com.amazonaws.databasemigrationservice#DescribeFleetAdvisorSchemasRequest``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_database_migration_service.types.filter_list
    import capo_database_migration_service.types.integer_optional
    import capo_database_migration_service.types.string


class DescribeFleetAdvisorSchemasRequest(TypedDict, closed=True):
    filters: NotRequired["capo_database_migration_service.types.filter_list.FilterList"]
    """<p> If you specify any of the following filters, the output includes information for only those schemas that meet the filter criteria:</p> <ul> <li> <p> <code>complexity</code> – The schema's complexity, for example <code>Simple</code>.</p> </li> <li> <p> <code>database-id</code> – The ID of the schema's database.</p> </li> <li> <p> <code>database-ip-address</code> – The IP address of the schema's database.</p> </li> <li> <p> <code>database-name</code> – The name of the schema's database.</p> </li> <li> <p> <code>database-engine</code> – The name of the schema database's engine.</p> </li> <li> <p> <code>original-schema-name</code> – The name of the schema's database's main schema.</p> </li> <li> <p> <code>schema-id</code> – The ID of the schema, for example <code>15</code>.</p> </li> <li> <p> <code>schema-name</code> – The name of the schema.</p> </li> <li> <p> <code>server-ip-address</code> – The IP address of the schema database's server.</p> </li> </ul> <p>An example is: <code>describe-fleet-advisor-schemas --filter Name="schema-id",Values="50"</code> </p>"""
    max_records: NotRequired[
        "capo_database_migration_service.types.integer_optional.IntegerOptional"
    ]
    """<p>Sets the maximum number of records returned in the response.</p>"""
    next_token: NotRequired["capo_database_migration_service.types.string.String"]
    """<p>If <code>NextToken</code> is returned by a previous response, there are more results available. The value of <code>NextToken</code> is a unique pagination token for each page. Make the call again using the returned token to retrieve the next page. Keep all other arguments unchanged. </p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: DescribeFleetAdvisorSchemasRequest) -> dict:
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


def deserialize_aws_json_1_1(data: dict) -> DescribeFleetAdvisorSchemasRequest:
    out: DescribeFleetAdvisorSchemasRequest = {}  # type: ignore[typeddict-item]
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
