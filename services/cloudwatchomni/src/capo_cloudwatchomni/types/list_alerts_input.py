"""Generated from Smithy shape ``com.amazonaws.cloudwatchomni#ListAlertsInput``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_cloudwatchomni.types.alert_filter_criteria
    import capo_cloudwatchomni.types.alert_sort_field
    import capo_cloudwatchomni.types.alert_sort_order
    import capo_cloudwatchomni.types.next_token
    import capo_cloudwatchomni.types.space_id


class ListAlertsInput(TypedDict, closed=True):
    space_id: "capo_cloudwatchomni.types.space_id.SpaceId"
    """The unique ID of the space."""
    filter_criteria: NotRequired[
        "capo_cloudwatchomni.types.alert_filter_criteria.AlertFilterCriteria"
    ]
    """Filter criteria narrowing which alerts are returned. All members are optional; the three name/id filters are mutually exclusive."""
    sort_by: NotRequired["capo_cloudwatchomni.types.alert_sort_field.AlertSortField"]
    """The field to sort results by."""
    sort_order: NotRequired["capo_cloudwatchomni.types.alert_sort_order.AlertSortOrder"]
    """The order in which to sort results."""
    next_token: NotRequired["capo_cloudwatchomni.types.next_token.NextToken"]
    """A token to retrieve the next page of results."""
    max_results: NotRequired["int"]
    """The maximum number of alerts to return per page."""


# --- rpcv2Cbor ser/de ---
def serialize_cbor(value: ListAlertsInput) -> dict:
    out: dict = {}
    out["spaceId"] = value["space_id"]
    if "filter_criteria" in value:
        import capo_cloudwatchomni.types.alert_filter_criteria

        out["filterCriteria"] = (
            capo_cloudwatchomni.types.alert_filter_criteria.serialize_cbor(
                value["filter_criteria"]
            )
        )
    if "sort_by" in value:
        import capo_cloudwatchomni.types.alert_sort_field

        out["sortBy"] = capo_cloudwatchomni.types.alert_sort_field.serialize_cbor(
            value["sort_by"]
        )
    if "sort_order" in value:
        import capo_cloudwatchomni.types.alert_sort_order

        out["sortOrder"] = capo_cloudwatchomni.types.alert_sort_order.serialize_cbor(
            value["sort_order"]
        )
    if "next_token" in value:
        out["nextToken"] = value["next_token"]
    if "max_results" in value:
        out["maxResults"] = value["max_results"]
    return out


def deserialize_cbor(data: dict) -> ListAlertsInput:
    out: ListAlertsInput = {}  # type: ignore[typeddict-item]
    if data.get("spaceId") is not None:
        out["space_id"] = data["spaceId"]
    else:
        out["space_id"] = ""
    if data.get("filterCriteria") is not None:
        import capo_cloudwatchomni.types.alert_filter_criteria

        out["filter_criteria"] = (
            capo_cloudwatchomni.types.alert_filter_criteria.deserialize_cbor(
                data["filterCriteria"]
            )
        )
    if data.get("sortBy") is not None:
        import capo_cloudwatchomni.types.alert_sort_field

        out["sort_by"] = capo_cloudwatchomni.types.alert_sort_field.deserialize_cbor(
            data["sortBy"]
        )
    if data.get("sortOrder") is not None:
        import capo_cloudwatchomni.types.alert_sort_order

        out["sort_order"] = capo_cloudwatchomni.types.alert_sort_order.deserialize_cbor(
            data["sortOrder"]
        )
    if data.get("nextToken") is not None:
        out["next_token"] = data["nextToken"]
    if data.get("maxResults") is not None:
        out["max_results"] = data["maxResults"]
    return out
