"""Generated from Smithy shape ``com.amazonaws.connect#ListNotificationsResponse``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_connect.types.next_token
    import capo_connect.types.notification_summary_list


class ListNotificationsResponse(TypedDict, closed=True):
    next_token: NotRequired["capo_connect.types.next_token.NextToken"]
    """<p>The token for the next set of results. If present, there are more results available.</p>"""
    notification_summary_list: (
        "capo_connect.types.notification_summary_list.NotificationSummaryList"
    )
    """<p>A list of notification summaries.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: ListNotificationsResponse) -> dict:
    out: dict = {}
    if "next_token" in value:
        out["NextToken"] = value["next_token"]
    import capo_connect.types.notification_summary_list

    out["NotificationSummaryList"] = (
        capo_connect.types.notification_summary_list.serialize_json(
            value["notification_summary_list"]
        )
    )
    return out


def deserialize_json(data: dict) -> ListNotificationsResponse:
    out: ListNotificationsResponse = {}  # type: ignore[typeddict-item]
    if data.get("NextToken") is not None:
        out["next_token"] = data["NextToken"]
    if data.get("NotificationSummaryList") is not None:
        import capo_connect.types.notification_summary_list

        out["notification_summary_list"] = (
            capo_connect.types.notification_summary_list.deserialize_json(
                data["NotificationSummaryList"]
            )
        )
    else:
        out["notification_summary_list"] = []
    return out
