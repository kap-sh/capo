"""Generated from Smithy shape ``com.amazonaws.databasemigrationservice#DescribeFleetAdvisorSchemaObjectSummaryRequest``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_database_migration_service.types.filter_list
    import capo_database_migration_service.types.integer_optional
    import capo_database_migration_service.types.string


class DescribeFleetAdvisorSchemaObjectSummaryRequest(TypedDict, closed=True):
    filters: NotRequired["capo_database_migration_service.types.filter_list.FilterList"]
    """<p> If you specify any of the following filters, the output includes information for only those schema objects that meet the filter criteria:</p> <ul> <li> <p> <code>schema-id</code> – The ID of the schema, for example <code>d4610ac5-e323-4ad9-bc50-eaf7249dfe9d</code>.</p> </li> </ul> <p>Example: <code>describe-fleet-advisor-schema-object-summary --filter Name="schema-id",Values="50"</code> </p>"""
    max_records: NotRequired[
        "capo_database_migration_service.types.integer_optional.IntegerOptional"
    ]
    """<important> <p> End of support notice: On May 20, 2026, Amazon Web Services will end support for Amazon Web Services DMS Fleet Advisor;. After May 20, 2026, you will no longer be able to access the Amazon Web Services DMS Fleet Advisor; console or Amazon Web Services DMS Fleet Advisor; resources. For more information, see <a href="https://docs.aws.amazon.com/dms/latest/userguide/dms_fleet.advisor-end-of-support.html">Amazon Web Services DMS Fleet Advisor end of support</a>. </p> </important> <p>Sets the maximum number of records returned in the response.</p>"""
    next_token: NotRequired["capo_database_migration_service.types.string.String"]
    """<p>If <code>NextToken</code> is returned by a previous response, there are more results available. The value of <code>NextToken</code> is a unique pagination token for each page. Make the call again using the returned token to retrieve the next page. Keep all other arguments unchanged. </p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(
    value: DescribeFleetAdvisorSchemaObjectSummaryRequest,
) -> dict:
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


def deserialize_aws_json_1_1(
    data: dict,
) -> DescribeFleetAdvisorSchemaObjectSummaryRequest:
    out: DescribeFleetAdvisorSchemaObjectSummaryRequest = {}  # type: ignore[typeddict-item]
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
