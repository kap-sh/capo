"""Generated from Smithy shape ``com.amazonaws.applicationinsights#ListProblemsRequest``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_application_insights.types.account_id
    import capo_application_insights.types.component_name
    import capo_application_insights.types.end_time
    import capo_application_insights.types.max_entities
    import capo_application_insights.types.pagination_token
    import capo_application_insights.types.resource_group_name
    import capo_application_insights.types.start_time
    import capo_application_insights.types.visibility


class ListProblemsRequest(TypedDict, closed=True):
    account_id: NotRequired["capo_application_insights.types.account_id.AccountId"]
    """<p>The Amazon Web Services account ID for the resource group owner.</p>"""
    resource_group_name: NotRequired[
        "capo_application_insights.types.resource_group_name.ResourceGroupName"
    ]
    """<p>The name of the resource group.</p>"""
    start_time: NotRequired["capo_application_insights.types.start_time.StartTime"]
    """<p>The time when the problem was detected, in epoch seconds. If you don't specify a time frame for the request, problems within the past seven days are returned.</p>"""
    end_time: NotRequired["capo_application_insights.types.end_time.EndTime"]
    """<p>The time when the problem ended, in epoch seconds. If not specified, problems within the past seven days are returned.</p>"""
    max_results: NotRequired["capo_application_insights.types.max_entities.MaxEntities"]
    """<p>The maximum number of results to return in a single call. To retrieve the remaining results, make another call with the returned <code>NextToken</code> value.</p>"""
    next_token: NotRequired[
        "capo_application_insights.types.pagination_token.PaginationToken"
    ]
    """<p>The token to request the next page of results.</p>"""
    component_name: NotRequired[
        "capo_application_insights.types.component_name.ComponentName"
    ]
    """<p> The name of the component. </p>"""
    visibility: NotRequired["capo_application_insights.types.visibility.Visibility"]
    """<p>Specifies whether or not you can view the problem. If not specified, visible and ignored problems are returned.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: ListProblemsRequest) -> dict:
    out: dict = {}
    if "account_id" in value:
        out["AccountId"] = value["account_id"]
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
    if "max_results" in value:
        out["MaxResults"] = value["max_results"]
    if "next_token" in value:
        out["NextToken"] = value["next_token"]
    if "component_name" in value:
        out["ComponentName"] = value["component_name"]
    if "visibility" in value:
        import capo_application_insights.types.visibility

        out["Visibility"] = (
            capo_application_insights.types.visibility.serialize_aws_json_1_1(
                value["visibility"]
            )
        )
    return out


def deserialize_aws_json_1_1(data: dict) -> ListProblemsRequest:
    out: ListProblemsRequest = {}  # type: ignore[typeddict-item]
    if data.get("AccountId") is not None:
        out["account_id"] = data["AccountId"]
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
    if data.get("MaxResults") is not None:
        out["max_results"] = data["MaxResults"]
    if data.get("NextToken") is not None:
        out["next_token"] = data["NextToken"]
    if data.get("ComponentName") is not None:
        out["component_name"] = data["ComponentName"]
    if data.get("Visibility") is not None:
        import capo_application_insights.types.visibility

        out["visibility"] = (
            capo_application_insights.types.visibility.deserialize_aws_json_1_1(
                data["Visibility"]
            )
        )
    return out


# --- rpcv2Cbor ser/de ---
def serialize_cbor(value: ListProblemsRequest) -> dict:
    out: dict = {}
    if "account_id" in value:
        out["AccountId"] = value["account_id"]
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
    if "max_results" in value:
        out["MaxResults"] = value["max_results"]
    if "next_token" in value:
        out["NextToken"] = value["next_token"]
    if "component_name" in value:
        out["ComponentName"] = value["component_name"]
    if "visibility" in value:
        import capo_application_insights.types.visibility

        out["Visibility"] = capo_application_insights.types.visibility.serialize_cbor(
            value["visibility"]
        )
    return out


def deserialize_cbor(data: dict) -> ListProblemsRequest:
    out: ListProblemsRequest = {}  # type: ignore[typeddict-item]
    if data.get("AccountId") is not None:
        out["account_id"] = data["AccountId"]
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
    if data.get("MaxResults") is not None:
        out["max_results"] = data["MaxResults"]
    if data.get("NextToken") is not None:
        out["next_token"] = data["NextToken"]
    if data.get("ComponentName") is not None:
        out["component_name"] = data["ComponentName"]
    if data.get("Visibility") is not None:
        import capo_application_insights.types.visibility

        out["visibility"] = capo_application_insights.types.visibility.deserialize_cbor(
            data["Visibility"]
        )
    return out
