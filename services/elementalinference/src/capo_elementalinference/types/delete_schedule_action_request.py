"""Generated from Smithy shape ``com.amazonaws.elementalinference#DeleteScheduleActionRequest``."""

from typing import TYPE_CHECKING

from typing_extensions import TypedDict

if TYPE_CHECKING:
    import capo_elementalinference.types.feed_id
    import capo_elementalinference.types.resource_name


class DeleteScheduleActionRequest(TypedDict, closed=True):
    id: "capo_elementalinference.types.feed_id.FeedId"
    """<p>The ID of the feed that holds the schedule action.</p>"""
    action_name: "capo_elementalinference.types.resource_name.ResourceName"
    """<p>The name of the schedule action that you want to delete.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: DeleteScheduleActionRequest) -> dict:
    out: dict = {}
    return out


def deserialize_json(data: dict) -> DeleteScheduleActionRequest:
    out: DeleteScheduleActionRequest = {}  # type: ignore[typeddict-item]
    return out
