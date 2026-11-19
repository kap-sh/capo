"""Generated from Smithy shape ``com.amazonaws.applicationinsights#ListConfigurationHistoryRequest``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_application_insights.types.account_id
    import capo_application_insights.types.configuration_event_status
    import capo_application_insights.types.end_time
    import capo_application_insights.types.max_entities
    import capo_application_insights.types.pagination_token
    import capo_application_insights.types.resource_group_name
    import capo_application_insights.types.start_time


class ListConfigurationHistoryRequest(TypedDict, closed=True):
    resource_group_name: NotRequired[
        "capo_application_insights.types.resource_group_name.ResourceGroupName"
    ]
    """<p>Resource group to which the application belongs. </p>"""
    start_time: NotRequired["capo_application_insights.types.start_time.StartTime"]
    """<p>The start time of the event. </p>"""
    end_time: NotRequired["capo_application_insights.types.end_time.EndTime"]
    """<p>The end time of the event.</p>"""
    event_status: NotRequired[
        "capo_application_insights.types.configuration_event_status.ConfigurationEventStatus"
    ]
    """<p>The status of the configuration update event. Possible values include INFO, WARN, and ERROR.</p>"""
    max_results: NotRequired["capo_application_insights.types.max_entities.MaxEntities"]
    """<p> The maximum number of results returned by <code>ListConfigurationHistory</code> in paginated output. When this parameter is used, <code>ListConfigurationHistory</code> returns only <code>MaxResults</code> in a single page along with a <code>NextToken</code> response element. The remaining results of the initial request can be seen by sending another <code>ListConfigurationHistory</code> request with the returned <code>NextToken</code> value. If this parameter is not used, then <code>ListConfigurationHistory</code> returns all results. </p>"""
    next_token: NotRequired[
        "capo_application_insights.types.pagination_token.PaginationToken"
    ]
    """<p>The <code>NextToken</code> value returned from a previous paginated <code>ListConfigurationHistory</code> request where <code>MaxResults</code> was used and the results exceeded the value of that parameter. Pagination continues from the end of the previous results that returned the <code>NextToken</code> value. This value is <code>null</code> when there are no more results to return.</p>"""
    account_id: NotRequired["capo_application_insights.types.account_id.AccountId"]
    """<p>The Amazon Web Services account ID for the resource group owner.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: ListConfigurationHistoryRequest) -> dict:
    out: dict = {}
    if "resource_group_name" in value:
        out["ResourceGroupName"] = value["resource_group_name"]
    if "start_time" in value:
        import capo_application_insights.types.start_time

        out["StartTime"] = (
            capo_application_insights.types.start_time.serialize_aws_json_1_1(
                value["start_time"]
            )
        )
    if "end_time" in value:
        import capo_application_insights.types.end_time

        out["EndTime"] = (
            capo_application_insights.types.end_time.serialize_aws_json_1_1(
                value["end_time"]
            )
        )
    if "event_status" in value:
        import capo_application_insights.types.configuration_event_status

        out["EventStatus"] = (
            capo_application_insights.types.configuration_event_status.serialize_aws_json_1_1(
                value["event_status"]
            )
        )
    if "max_results" in value:
        out["MaxResults"] = value["max_results"]
    if "next_token" in value:
        out["NextToken"] = value["next_token"]
    if "account_id" in value:
        out["AccountId"] = value["account_id"]
    return out


def deserialize_aws_json_1_1(data: dict) -> ListConfigurationHistoryRequest:
    out: ListConfigurationHistoryRequest = {}  # type: ignore[typeddict-item]
    if data.get("ResourceGroupName") is not None:
        out["resource_group_name"] = data["ResourceGroupName"]
    if data.get("StartTime") is not None:
        import capo_application_insights.types.start_time

        out["start_time"] = (
            capo_application_insights.types.start_time.deserialize_aws_json_1_1(
                data["StartTime"]
            )
        )
    if data.get("EndTime") is not None:
        import capo_application_insights.types.end_time

        out["end_time"] = (
            capo_application_insights.types.end_time.deserialize_aws_json_1_1(
                data["EndTime"]
            )
        )
    if data.get("EventStatus") is not None:
        import capo_application_insights.types.configuration_event_status

        out["event_status"] = (
            capo_application_insights.types.configuration_event_status.deserialize_aws_json_1_1(
                data["EventStatus"]
            )
        )
    if data.get("MaxResults") is not None:
        out["max_results"] = data["MaxResults"]
    if data.get("NextToken") is not None:
        out["next_token"] = data["NextToken"]
    if data.get("AccountId") is not None:
        out["account_id"] = data["AccountId"]
    return out


# --- rpcv2Cbor ser/de ---
def serialize_cbor(value: ListConfigurationHistoryRequest) -> dict:
    out: dict = {}
    if "resource_group_name" in value:
        out["ResourceGroupName"] = value["resource_group_name"]
    if "start_time" in value:
        import capo_application_insights.types.start_time

        out["StartTime"] = capo_application_insights.types.start_time.serialize_cbor(
            value["start_time"]
        )
    if "end_time" in value:
        import capo_application_insights.types.end_time

        out["EndTime"] = capo_application_insights.types.end_time.serialize_cbor(
            value["end_time"]
        )
    if "event_status" in value:
        import capo_application_insights.types.configuration_event_status

        out["EventStatus"] = (
            capo_application_insights.types.configuration_event_status.serialize_cbor(
                value["event_status"]
            )
        )
    if "max_results" in value:
        out["MaxResults"] = value["max_results"]
    if "next_token" in value:
        out["NextToken"] = value["next_token"]
    if "account_id" in value:
        out["AccountId"] = value["account_id"]
    return out


def deserialize_cbor(data: dict) -> ListConfigurationHistoryRequest:
    out: ListConfigurationHistoryRequest = {}  # type: ignore[typeddict-item]
    if data.get("ResourceGroupName") is not None:
        out["resource_group_name"] = data["ResourceGroupName"]
    if data.get("StartTime") is not None:
        import capo_application_insights.types.start_time

        out["start_time"] = capo_application_insights.types.start_time.deserialize_cbor(
            data["StartTime"]
        )
    if data.get("EndTime") is not None:
        import capo_application_insights.types.end_time

        out["end_time"] = capo_application_insights.types.end_time.deserialize_cbor(
            data["EndTime"]
        )
    if data.get("EventStatus") is not None:
        import capo_application_insights.types.configuration_event_status

        out["event_status"] = (
            capo_application_insights.types.configuration_event_status.deserialize_cbor(
                data["EventStatus"]
            )
        )
    if data.get("MaxResults") is not None:
        out["max_results"] = data["MaxResults"]
    if data.get("NextToken") is not None:
        out["next_token"] = data["NextToken"]
    if data.get("AccountId") is not None:
        out["account_id"] = data["AccountId"]
    return out
