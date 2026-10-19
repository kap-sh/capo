"""Generated from Smithy shape ``com.amazonaws.sesv2#MessageTag``."""

from typing import TYPE_CHECKING

from typing_extensions import TypedDict

if TYPE_CHECKING:
    import capo_sesv2.types.message_tag_name
    import capo_sesv2.types.message_tag_value


class MessageTag(TypedDict, closed=True):
    name: "capo_sesv2.types.message_tag_name.MessageTagName"
    """<p>The name of the message tag. The message tag name has to meet the following criteria:</p> <ul> <li> <p>It can only contain ASCII letters (a–z, A–Z), numbers (0–9), underscores (_), or dashes (-).</p> </li> <li> <p>It can contain no more than 256 characters.</p> </li> </ul>"""
    value: "capo_sesv2.types.message_tag_value.MessageTagValue"
    """<p>The value of the message tag. The message tag value has to meet the following criteria:</p> <ul> <li> <p>It can only contain ASCII letters (a–z, A–Z), numbers (0–9), underscores (_), or dashes (-).</p> </li> <li> <p>It can contain no more than 256 characters.</p> </li> </ul>"""


# --- restJson1 ser/de ---
def serialize_json(value: MessageTag) -> dict:
    out: dict = {}
    out["Name"] = value["name"]
    out["Value"] = value["value"]
    return out


def deserialize_json(data: dict) -> MessageTag:
    out: MessageTag = {}  # type: ignore[typeddict-item]
    if data.get("Name") is not None:
        out["name"] = data["Name"]
    else:
        out["name"] = ""
    if data.get("Value") is not None:
        out["value"] = data["Value"]
    else:
        out["value"] = ""
    return out
