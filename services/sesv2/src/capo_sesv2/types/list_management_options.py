"""Generated from Smithy shape ``com.amazonaws.sesv2#ListManagementOptions``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_sesv2.types.contact_list_name
    import capo_sesv2.types.topic_name


class ListManagementOptions(TypedDict, closed=True):
    contact_list_name: "capo_sesv2.types.contact_list_name.ContactListName"
    """<p>The name of the contact list.</p>"""
    topic_name: NotRequired["capo_sesv2.types.topic_name.TopicName"]
    """<p>The name of the topic.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: ListManagementOptions) -> dict:
    out: dict = {}
    out["ContactListName"] = value["contact_list_name"]
    if "topic_name" in value:
        out["TopicName"] = value["topic_name"]
    return out


def deserialize_json(data: dict) -> ListManagementOptions:
    out: ListManagementOptions = {}  # type: ignore[typeddict-item]
    if data.get("ContactListName") is not None:
        out["contact_list_name"] = data["ContactListName"]
    else:
        out["contact_list_name"] = ""
    if data.get("TopicName") is not None:
        out["topic_name"] = data["TopicName"]
    return out
