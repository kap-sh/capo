"""Generated from Smithy shape ``com.amazonaws.partnercentralselling#ListOpportunityFromEngagementTasksRequest``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_partnercentral_selling.types.catalog_identifier
    import capo_partnercentral_selling.types.context_identifiers
    import capo_partnercentral_selling.types.engagement_identifiers
    import capo_partnercentral_selling.types.list_tasks_sort_base
    import capo_partnercentral_selling.types.opportunity_identifiers
    import capo_partnercentral_selling.types.task_identifiers
    import capo_partnercentral_selling.types.task_statuses


class ListOpportunityFromEngagementTasksRequest(TypedDict, closed=True):
    max_results: NotRequired["int"]
    """<p>Specifies the maximum number of results to return in a single page of the response. Use this parameter to control the number of items returned in each request, which can be useful for performance tuning and managing large result sets.</p>"""
    next_token: NotRequired["str"]
    """<p>The token for requesting the next page of results. This value is obtained from the NextToken field in the response of a previous call to this API. Use this parameter for pagination when the result set spans multiple pages.</p>"""
    sort: NotRequired[
        "capo_partnercentral_selling.types.list_tasks_sort_base.ListTasksSortBase"
    ]
    catalog: "capo_partnercentral_selling.types.catalog_identifier.CatalogIdentifier"
    """<p>Specifies the catalog related to the request. Valid values are <code>AWS</code> for production environments and <code>Sandbox</code> for testing or development purposes. The catalog determines which environment the task data is retrieved from.</p>"""
    task_status: NotRequired[
        "capo_partnercentral_selling.types.task_statuses.TaskStatuses"
    ]
    """<p>Filters the tasks based on their current status. This allows you to focus on tasks in specific states. Valid values are <code>COMPLETE</code> for tasks that have finished successfully, <code>INPROGRESS</code> for tasks that are currently running, and <code>FAILED</code> for tasks that have encountered an error and failed to complete.</p>"""
    task_identifier: NotRequired[
        "capo_partnercentral_selling.types.task_identifiers.TaskIdentifiers"
    ]
    """<p>Filters tasks by their unique identifiers. Use this when you want to retrieve information about specific tasks. Provide the task ID to get details about a particular opportunity creation task.</p>"""
    opportunity_identifier: NotRequired[
        "capo_partnercentral_selling.types.opportunity_identifiers.OpportunityIdentifiers"
    ]
    """<p>Filters tasks by the identifiers of the opportunities they created or are associated with. Use this to find tasks related to specific opportunity creation processes.</p>"""
    engagement_identifier: NotRequired[
        "capo_partnercentral_selling.types.engagement_identifiers.EngagementIdentifiers"
    ]
    """<p>Filters tasks by the identifiers of the engagements from which opportunities are being created. Use this to find all opportunity creation tasks associated with a specific engagement.</p>"""
    context_identifier: NotRequired[
        "capo_partnercentral_selling.types.context_identifiers.ContextIdentifiers"
    ]
    """<p>Filters tasks by the identifiers of the engagement contexts associated with the opportunity creation. Use this to find tasks related to specific contextual information within engagements that are being converted to opportunities.</p>"""


# --- awsJson1_0 ser/de ---
def serialize_aws_json_1_0(value: ListOpportunityFromEngagementTasksRequest) -> dict:
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
    if "context_identifier" in value:
        import capo_partnercentral_selling.types.context_identifiers

        out["ContextIdentifier"] = (
            capo_partnercentral_selling.types.context_identifiers.serialize_aws_json_1_0(
                value["context_identifier"]
            )
        )
    return out


def deserialize_aws_json_1_0(data: dict) -> ListOpportunityFromEngagementTasksRequest:
    out: ListOpportunityFromEngagementTasksRequest = {}  # type: ignore[typeddict-item]
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
    if data.get("ContextIdentifier") is not None:
        import capo_partnercentral_selling.types.context_identifiers

        out["context_identifier"] = (
            capo_partnercentral_selling.types.context_identifiers.deserialize_aws_json_1_0(
                data["ContextIdentifier"]
            )
        )
    return out
