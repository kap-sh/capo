"""Generated from Smithy shape ``com.amazonaws.partnercentralselling#ListEngagementFromOpportunityTasksRequest``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_partnercentral_selling.types.catalog_identifier
    import capo_partnercentral_selling.types.engagement_identifiers
    import capo_partnercentral_selling.types.list_tasks_sort_base
    import capo_partnercentral_selling.types.opportunity_identifiers
    import capo_partnercentral_selling.types.task_identifiers
    import capo_partnercentral_selling.types.task_statuses


class ListEngagementFromOpportunityTasksRequest(TypedDict, closed=True):
    max_results: NotRequired["int"]
    """<p> Specifies the maximum number of results to return in a single page of the response.Use this parameter to control the number of items returned in each request, which can be useful for performance tuning and managing large result sets. </p>"""
    next_token: NotRequired["str"]
    """<p> The token for requesting the next page of results. This value is obtained from the NextToken field in the response of a previous call to this API. Use this parameter for pagination when the result set spans multiple pages. </p>"""
    sort: NotRequired[
        "capo_partnercentral_selling.types.list_tasks_sort_base.ListTasksSortBase"
    ]
    """<p> Specifies the sorting criteria for the returned results. This allows you to order the tasks based on specific attributes. </p>"""
    catalog: "capo_partnercentral_selling.types.catalog_identifier.CatalogIdentifier"
    """<p> Specifies the catalog related to the request. Valid values are: </p> <ul> <li> <p> AWS: Retrieves the request from the production AWS environment. </p> </li> <li> <p> Sandbox: Retrieves the request from a sandbox environment used for testing or development purposes. </p> </li> </ul>"""
    task_status: NotRequired[
        "capo_partnercentral_selling.types.task_statuses.TaskStatuses"
    ]
    """<p> Filters the tasks based on their current status. This allows you to focus on tasks in specific states. </p>"""
    task_identifier: NotRequired[
        "capo_partnercentral_selling.types.task_identifiers.TaskIdentifiers"
    ]
    """<p> Filters tasks by their unique identifiers. Use this when you want to retrieve information about specific tasks. </p>"""
    opportunity_identifier: NotRequired[
        "capo_partnercentral_selling.types.opportunity_identifiers.OpportunityIdentifiers"
    ]
    """<p> The identifier of the original opportunity associated with this task. </p>"""
    engagement_identifier: NotRequired[
        "capo_partnercentral_selling.types.engagement_identifiers.EngagementIdentifiers"
    ]
    """<p> Filters tasks by the identifiers of the engagements they created or are associated with. </p>"""


# --- awsJson1_0 ser/de ---
def serialize_aws_json_1_0(value: ListEngagementFromOpportunityTasksRequest) -> dict:
    out: dict = {}
    if "max_results" in value:
        out["MaxResults"] = value["max_results"]
    if "next_token" in value:
        out["NextToken"] = value["next_token"]
    if "sort" in value:
        import capo_partnercentral_selling.types.list_tasks_sort_base

        out["Sort"] = (
            capo_partnercentral_selling.types.list_tasks_sort_base.serialize_aws_json_1_0(
                value["sort"]
            )
        )
    out["Catalog"] = value["catalog"]
    if "task_status" in value:
        import capo_partnercentral_selling.types.task_statuses

        out["TaskStatus"] = (
            capo_partnercentral_selling.types.task_statuses.serialize_aws_json_1_0(
                value["task_status"]
            )
        )
    if "task_identifier" in value:
        import capo_partnercentral_selling.types.task_identifiers

        out["TaskIdentifier"] = (
            capo_partnercentral_selling.types.task_identifiers.serialize_aws_json_1_0(
                value["task_identifier"]
            )
        )
    if "opportunity_identifier" in value:
        import capo_partnercentral_selling.types.opportunity_identifiers

        out["OpportunityIdentifier"] = (
            capo_partnercentral_selling.types.opportunity_identifiers.serialize_aws_json_1_0(
                value["opportunity_identifier"]
            )
        )
    if "engagement_identifier" in value:
        import capo_partnercentral_selling.types.engagement_identifiers

        out["EngagementIdentifier"] = (
            capo_partnercentral_selling.types.engagement_identifiers.serialize_aws_json_1_0(
                value["engagement_identifier"]
            )
        )
    return out


def deserialize_aws_json_1_0(data: dict) -> ListEngagementFromOpportunityTasksRequest:
    out: ListEngagementFromOpportunityTasksRequest = {}  # type: ignore[typeddict-item]
    if data.get("MaxResults") is not None:
        out["max_results"] = data["MaxResults"]
    if data.get("NextToken") is not None:
        out["next_token"] = data["NextToken"]
    if data.get("Sort") is not None:
        import capo_partnercentral_selling.types.list_tasks_sort_base

        out["sort"] = (
            capo_partnercentral_selling.types.list_tasks_sort_base.deserialize_aws_json_1_0(
                data["Sort"]
            )
        )
    if data.get("Catalog") is not None:
        out["catalog"] = data["Catalog"]
    else:
        out["catalog"] = ""
    if data.get("TaskStatus") is not None:
        import capo_partnercentral_selling.types.task_statuses

        out["task_status"] = (
            capo_partnercentral_selling.types.task_statuses.deserialize_aws_json_1_0(
                data["TaskStatus"]
            )
        )
    if data.get("TaskIdentifier") is not None:
        import capo_partnercentral_selling.types.task_identifiers

        out["task_identifier"] = (
            capo_partnercentral_selling.types.task_identifiers.deserialize_aws_json_1_0(
                data["TaskIdentifier"]
            )
        )
    if data.get("OpportunityIdentifier") is not None:
        import capo_partnercentral_selling.types.opportunity_identifiers

        out["opportunity_identifier"] = (
            capo_partnercentral_selling.types.opportunity_identifiers.deserialize_aws_json_1_0(
                data["OpportunityIdentifier"]
            )
        )
    if data.get("EngagementIdentifier") is not None:
        import capo_partnercentral_selling.types.engagement_identifiers

        out["engagement_identifier"] = (
            capo_partnercentral_selling.types.engagement_identifiers.deserialize_aws_json_1_0(
                data["EngagementIdentifier"]
            )
        )
    return out
