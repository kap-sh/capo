"""Generated from Smithy shape ``com.amazonaws.ses#MessageTag``."""

from typing import TYPE_CHECKING

from typing_extensions import TypedDict

from capo_ses._protocol.xml import Element

if TYPE_CHECKING:
    import capo_ses.types.message_tag_name
    import capo_ses.types.message_tag_value


class MessageTag(TypedDict, closed=True):
    name: "capo_ses.types.message_tag_name.MessageTagName"
    """<p>The name of the tag. The name must meet the following requirements:</p> <ul> <li> <p>Contain only ASCII letters (a-z, A-Z), numbers (0-9), underscores (_), or dashes (-).</p> </li> <li> <p>Contain 256 characters or fewer.</p> </li> </ul>"""
    value: "capo_ses.types.message_tag_value.MessageTagValue"
    """<p>The value of the tag. The value must meet the following requirements:</p> <ul> <li> <p>Contain only ASCII letters (a-z, A-Z), numbers (0-9), underscores (_), or dashes (-).</p> </li> <li> <p>Contain 256 characters or fewer.</p> </li> </ul>"""


# --- awsQuery ser/de ---
def serialize_query(
    value: MessageTag, pairs: list[tuple[str, str]], prefix: str
) -> None:
    key_prefix = f"{prefix}." if prefix else ""
    pairs.append((f"{key_prefix}Name", str(value["name"])))
    pairs.append((f"{key_prefix}Value", str(value["value"])))


def deserialize_query(el: Element) -> MessageTag:
    out: MessageTag = {}  # type: ignore[typeddict-item]
    child_name = el.find("Name")
    if child_name is not None:
        out["name"] = str(child_name.text or "")
    else:
        out["name"] = ""
    child_value = el.find("Value")
    if child_value is not None:
        out["value"] = str(child_value.text or "")
    else:
        out["value"] = ""
    return out
