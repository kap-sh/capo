"""Generated from Smithy shape ``com.amazonaws.configservice#GetResourceConfigHistoryRequest``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_config_service.types.chronological_order
    import capo_config_service.types.earlier_time
    import capo_config_service.types.later_time
    import capo_config_service.types.limit
    import capo_config_service.types.next_token
    import capo_config_service.types.resource_id
    import capo_config_service.types.resource_type


class GetResourceConfigHistoryRequest(TypedDict, closed=True):
    resource_type: "capo_config_service.types.resource_type.ResourceType"
    """<p>The resource type.</p>"""
    resource_id: "capo_config_service.types.resource_id.ResourceId"
    """<p>The ID of the resource (for example., <code>sg-xxxxxx</code>).</p>"""
    later_time: NotRequired["capo_config_service.types.later_time.LaterTime"]
    """<p>The chronologically latest time in the time range for which the history requested. If not specified, current time is taken.</p>"""
    earlier_time: NotRequired["capo_config_service.types.earlier_time.EarlierTime"]
    """<p>The chronologically earliest time in the time range for which the history requested. If not specified, the action returns paginated results that contain configuration items that start when the first configuration item was recorded.</p>"""
    chronological_order: NotRequired[
        "capo_config_service.types.chronological_order.ChronologicalOrder"
    ]
    """<p>The chronological order for configuration items listed. By default, the results are listed in reverse chronological order.</p>"""
    limit: NotRequired["capo_config_service.types.limit.Limit"]
    """<p>The maximum number of configuration items returned on each page. The default is 10. You cannot specify a number greater than 100. If you specify 0, Config uses the default.</p>"""
    next_token: NotRequired["capo_config_service.types.next_token.NextToken"]
    """<p>The <code>nextToken</code> string returned on a previous page that you use to get the next page of results in a paginated response.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: GetResourceConfigHistoryRequest) -> dict:
    out: dict = {}
    import capo_config_service.types.resource_type

    out["resourceType"] = (
        capo_config_service.types.resource_type.serialize_aws_json_1_1(
            value["resource_type"]
        )
    )
    out["resourceId"] = value["resource_id"]
    if "later_time" in value:
        import capo_config_service.types.later_time

        out["laterTime"] = capo_config_service.types.later_time.serialize_aws_json_1_1(
            value["later_time"]
        )
    if "earlier_time" in value:
        import capo_config_service.types.earlier_time

        out["earlierTime"] = (
            capo_config_service.types.earlier_time.serialize_aws_json_1_1(
                value["earlier_time"]
            )
        )
    if "chronological_order" in value:
        import capo_config_service.types.chronological_order

        out["chronologicalOrder"] = (
            capo_config_service.types.chronological_order.serialize_aws_json_1_1(
                value["chronological_order"]
            )
        )
    if "limit" in value:
        out["limit"] = value["limit"]
    if "next_token" in value:
        out["nextToken"] = value["next_token"]
    return out


def deserialize_aws_json_1_1(data: dict) -> GetResourceConfigHistoryRequest:
    out: GetResourceConfigHistoryRequest = {}  # type: ignore[typeddict-item]
    if data.get("resourceType") is not None:
        import capo_config_service.types.resource_type

        out["resource_type"] = (
            capo_config_service.types.resource_type.deserialize_aws_json_1_1(
                data["resourceType"]
            )
        )
    else:
        import typing

        out["resource_type"] = typing.cast(
            "capo_config_service.types.resource_type.ResourceType", ""
        )
    if data.get("resourceId") is not None:
        out["resource_id"] = data["resourceId"]
    else:
        out["resource_id"] = ""
    if data.get("laterTime") is not None:
        import capo_config_service.types.later_time

        out["later_time"] = (
            capo_config_service.types.later_time.deserialize_aws_json_1_1(
                data["laterTime"]
            )
        )
    if data.get("earlierTime") is not None:
        import capo_config_service.types.earlier_time

        out["earlier_time"] = (
            capo_config_service.types.earlier_time.deserialize_aws_json_1_1(
                data["earlierTime"]
            )
        )
    if data.get("chronologicalOrder") is not None:
        import capo_config_service.types.chronological_order

        out["chronological_order"] = (
            capo_config_service.types.chronological_order.deserialize_aws_json_1_1(
                data["chronologicalOrder"]
            )
        )
    if data.get("limit") is not None:
        out["limit"] = data["limit"]
    if data.get("nextToken") is not None:
        out["next_token"] = data["nextToken"]
    return out
