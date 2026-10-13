"""Generated from Smithy shape ``com.amazonaws.devopsagent#SendMessageResponse``."""

from typing import TYPE_CHECKING, Any

from typing_extensions import TypedDict

if TYPE_CHECKING:
    import capo_devops_agent.types.send_message_events


class SendMessageResponse(TypedDict, closed=True):
    events: "capo_devops_agent.types.send_message_events.SendMessageEvents"
    """<p>The stream of chat message events</p>"""


def redact_sensitive(value: SendMessageResponse) -> dict[str, Any]:
    out: dict[str, Any] = dict(value)
    if "events" in value:
        out["events"] = "*** Streaming Data Redacted ***"
    return out
