"""Generated from Smithy shape ``com.amazonaws.sesv2#UpdateContactRequest``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_sesv2.types.attributes_data
    import capo_sesv2.types.contact_list_name
    import capo_sesv2.types.email_address
    import capo_sesv2.types.topic_preference_list
    import capo_sesv2.types.unsubscribe_all


class UpdateContactRequest(TypedDict, closed=True):
    contact_list_name: "capo_sesv2.types.contact_list_name.ContactListName"
    """<p>The name of the contact list.</p>"""
    email_address: "capo_sesv2.types.email_address.EmailAddress"
    """<p>The contact's email address.</p>"""
    topic_preferences: NotRequired[
        "capo_sesv2.types.topic_preference_list.TopicPreferenceList"
    ]
    """<p>The contact's preference for being opted-in to or opted-out of a topic.</p>"""
    unsubscribe_all: NotRequired["capo_sesv2.types.unsubscribe_all.UnsubscribeAll"]
    """<p>A boolean value status noting if the contact is unsubscribed from all contact list topics.</p>"""
    attributes_data: NotRequired["capo_sesv2.types.attributes_data.AttributesData"]
    """<p>The attribute data attached to a contact.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: UpdateContactRequest) -> dict:
    out: dict = {}
    if "topic_preferences" in value:
        import capo_sesv2.types.topic_preference_list

        out["TopicPreferences"] = capo_sesv2.types.topic_preference_list.serialize_json(
            value["topic_preferences"]
        )
    if "unsubscribe_all" in value:
        out["UnsubscribeAll"] = value["unsubscribe_all"]
    if "attributes_data" in value:
        out["AttributesData"] = value["attributes_data"]
    return out


def deserialize_json(data: dict) -> UpdateContactRequest:
    out: UpdateContactRequest = {}  # type: ignore[typeddict-item]
    if data.get("TopicPreferences") is not None:
        import capo_sesv2.types.topic_preference_list

        out["topic_preferences"] = (
            capo_sesv2.types.topic_preference_list.deserialize_json(
                data["TopicPreferences"]
            )
        )
    if data.get("UnsubscribeAll") is not None:
        out["unsubscribe_all"] = data["UnsubscribeAll"]
    if data.get("AttributesData") is not None:
        out["attributes_data"] = data["AttributesData"]
    return out
