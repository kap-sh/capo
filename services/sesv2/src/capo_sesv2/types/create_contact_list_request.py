"""Generated from Smithy shape ``com.amazonaws.sesv2#CreateContactListRequest``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_sesv2.types.contact_list_name
    import capo_sesv2.types.description
    import capo_sesv2.types.tag_list
    import capo_sesv2.types.topics


class CreateContactListRequest(TypedDict, closed=True):
    contact_list_name: "capo_sesv2.types.contact_list_name.ContactListName"
    """<p>The name of the contact list.</p>"""
    topics: NotRequired["capo_sesv2.types.topics.Topics"]
    """<p>An interest group, theme, or label within a list. A contact list can have multiple topics.</p>"""
    description: NotRequired["capo_sesv2.types.description.Description"]
    """<p>A description of what the contact list is about.</p>"""
    tags: NotRequired["capo_sesv2.types.tag_list.TagList"]
    """<p>The tags associated with a contact list.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: CreateContactListRequest) -> dict:
    out: dict = {}
    out["ContactListName"] = value["contact_list_name"]
    if "topics" in value:
        import capo_sesv2.types.topics

        out["Topics"] = capo_sesv2.types.topics.serialize_json(value["topics"])
    if "description" in value:
        out["Description"] = value["description"]
    if "tags" in value:
        import capo_sesv2.types.tag_list

        out["Tags"] = capo_sesv2.types.tag_list.serialize_json(value["tags"])
    return out


def deserialize_json(data: dict) -> CreateContactListRequest:
    out: CreateContactListRequest = {}  # type: ignore[typeddict-item]
    if data.get("ContactListName") is not None:
        out["contact_list_name"] = data["ContactListName"]
    else:
        out["contact_list_name"] = ""
    if data.get("Topics") is not None:
        import capo_sesv2.types.topics

        out["topics"] = capo_sesv2.types.topics.deserialize_json(data["Topics"])
    if data.get("Description") is not None:
        out["description"] = data["Description"]
    if data.get("Tags") is not None:
        import capo_sesv2.types.tag_list

        out["tags"] = capo_sesv2.types.tag_list.deserialize_json(data["Tags"])
    return out
