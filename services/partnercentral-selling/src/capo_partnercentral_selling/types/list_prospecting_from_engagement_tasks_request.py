"""Generated from Smithy shape ``com.amazonaws.partnercentralselling#ListProspectingFromEngagementTasksRequest``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_partnercentral_selling.types.catalog_identifier
    import capo_partnercentral_selling.types.date_time
    import capo_partnercentral_selling.types.page_size
    import capo_partnercentral_selling.types.prospecting_from_engagement_task_sort
    import capo_partnercentral_selling.types.task_identifier_list
    import capo_partnercentral_selling.types.task_name_list


class ListProspectingFromEngagementTasksRequest(TypedDict, closed=True):
    catalog: "capo_partnercentral_selling.types.catalog_identifier.CatalogIdentifier"
    """<p>Specifies the catalog to list tasks from. Specify <code>AWS</code> for production environments and <code>Sandbox</code> for testing and development purposes.</p>"""
    max_results: NotRequired["capo_partnercentral_selling.types.page_size.PageSize"]
    """<p>The maximum number of results to return in a single page. If additional results exist, the response includes a <code>NextToken</code> value for retrieving the next page. If omitted, the API uses a service-defined default page size.</p>"""
    next_token: NotRequired["str"]
    """<p>The pagination token from a previous call to this API. Include this value to retrieve the next page of results. If omitted, the first page is returned.</p>"""
    task_identifier: NotRequired[
        "capo_partnercentral_selling.types.task_identifier_list.TaskIdentifierList"
    ]
    """<p>Filters the results to include only the tasks with the specified identifiers. Provide up to 10 task IDs to narrow the list to specific tasks. If omitted, tasks are not filtered by identifier.</p>"""
    task_name: NotRequired[
        "capo_partnercentral_selling.types.task_name_list.TaskNameList"
    ]
    """<p>Filters the results to include only tasks with the specified names. Provide up to 10 task names to narrow the list. If omitted, tasks are not filtered by name.</p>"""
    start_after: NotRequired["capo_partnercentral_selling.types.date_time.DateTime"]
    """<p>Filters tasks to include only those that started after the specified timestamp. Use this with <code>StartBefore</code> to define a start-time range for your query. The format follows ISO 8601 date-time notation.</p>"""
    start_before: NotRequired["capo_partnercentral_selling.types.date_time.DateTime"]
    """<p>Filters tasks to include only those that started before the specified timestamp. Use this with <code>StartAfter</code> to define a start-time range for your query. The format follows ISO 8601 date-time notation.</p>"""
    sort: NotRequired[
        "capo_partnercentral_selling.types.prospecting_from_engagement_task_sort.ProspectingFromEngagementTaskSort"
    ]
    """<p>Specifies the field and order used to sort the returned tasks. If omitted, tasks are returned in the default sort order.</p>"""


# --- awsJson1_0 ser/de ---
def serialize_aws_json_1_0(value: ListProspectingFromEngagementTasksRequest) -> dict:
    out: dict = {}
    out["Catalog"] = value["catalog"]
    if "max_results" in value:
        out["MaxResults"] = value["max_results"]
    if "next_token" in value:
        out["NextToken"] = value["next_token"]
    if "task_identifier" in value:
        import capo_partnercentral_selling.types.task_identifier_list

        out["TaskIdentifier"] = (
            capo_partnercentral_selling.types.task_identifier_list.serialize_aws_json_1_0(
                value["task_identifier"]
            )
        )
    if "task_name" in value:
        import capo_partnercentral_selling.types.task_name_list

        out["TaskName"] = (
            capo_partnercentral_selling.types.task_name_list.serialize_aws_json_1_0(
                value["task_name"]
            )
        )
    if "start_after" in value:
        import capo_partnercentral_selling.types.date_time

        out["StartAfter"] = (
            capo_partnercentral_selling.types.date_time.serialize_aws_json_1_0(
                value["start_after"]
            )
        )
    if "start_before" in value:
        import capo_partnercentral_selling.types.date_time

        out["StartBefore"] = (
            capo_partnercentral_selling.types.date_time.serialize_aws_json_1_0(
                value["start_before"]
            )
        )
    if "sort" in value:
        import capo_partnercentral_selling.types.prospecting_from_engagement_task_sort

        out["Sort"] = (
            capo_partnercentral_selling.types.prospecting_from_engagement_task_sort.serialize_aws_json_1_0(
                value["sort"]
            )
        )
    return out


def deserialize_aws_json_1_0(data: dict) -> ListProspectingFromEngagementTasksRequest:
    out: ListProspectingFromEngagementTasksRequest = {}  # type: ignore[typeddict-item]
    if data.get("Catalog") is not None:
        out["catalog"] = data["Catalog"]
    else:
        out["catalog"] = ""
    if data.get("MaxResults") is not None:
        out["max_results"] = data["MaxResults"]
    if data.get("NextToken") is not None:
        out["next_token"] = data["NextToken"]
    if data.get("TaskIdentifier") is not None:
        import capo_partnercentral_selling.types.task_identifier_list

        out["task_identifier"] = (
            capo_partnercentral_selling.types.task_identifier_list.deserialize_aws_json_1_0(
                data["TaskIdentifier"]
            )
        )
    if data.get("TaskName") is not None:
        import capo_partnercentral_selling.types.task_name_list

        out["task_name"] = (
            capo_partnercentral_selling.types.task_name_list.deserialize_aws_json_1_0(
                data["TaskName"]
            )
        )
    if data.get("StartAfter") is not None:
        import capo_partnercentral_selling.types.date_time

        out["start_after"] = (
            capo_partnercentral_selling.types.date_time.deserialize_aws_json_1_0(
                data["StartAfter"]
            )
        )
    if data.get("StartBefore") is not None:
        import capo_partnercentral_selling.types.date_time

        out["start_before"] = (
            capo_partnercentral_selling.types.date_time.deserialize_aws_json_1_0(
                data["StartBefore"]
            )
        )
    if data.get("Sort") is not None:
        import capo_partnercentral_selling.types.prospecting_from_engagement_task_sort

        out["sort"] = (
            capo_partnercentral_selling.types.prospecting_from_engagement_task_sort.deserialize_aws_json_1_0(
                data["Sort"]
            )
        )
    return out
