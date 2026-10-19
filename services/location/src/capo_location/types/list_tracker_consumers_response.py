"""Generated from Smithy shape ``com.amazonaws.location#ListTrackerConsumersResponse``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_location.types.arn_list
    import capo_location.types.token


class ListTrackerConsumersResponse(TypedDict, closed=True):
    consumer_arns: "capo_location.types.arn_list.ArnList"
    """<p>Contains the list of geofence collection ARNs associated to the tracker resource.</p>"""
    next_token: NotRequired["capo_location.types.token.Token"]
    """<p>A pagination token indicating there are additional pages available. You can use the token in a following request to fetch the next set of results. </p>"""


# --- restJson1 ser/de ---
def serialize_json(value: ListTrackerConsumersResponse) -> dict:
    out: dict = {}
    import capo_location.types.arn_list

    out["ConsumerArns"] = capo_location.types.arn_list.serialize_json(
        value["consumer_arns"]
    )
    if "next_token" in value:
        out["NextToken"] = value["next_token"]
    return out


def deserialize_json(data: dict) -> ListTrackerConsumersResponse:
    out: ListTrackerConsumersResponse = {}  # type: ignore[typeddict-item]
    if data.get("ConsumerArns") is not None:
        import capo_location.types.arn_list

        out["consumer_arns"] = capo_location.types.arn_list.deserialize_json(
            data["ConsumerArns"]
        )
    else:
        out["consumer_arns"] = []
    if data.get("NextToken") is not None:
        out["next_token"] = data["NextToken"]
    return out
