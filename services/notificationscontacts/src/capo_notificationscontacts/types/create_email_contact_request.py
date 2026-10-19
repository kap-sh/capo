"""Generated from Smithy shape ``com.amazonaws.notificationscontacts#CreateEmailContactRequest``."""

from typing import TYPE_CHECKING, Any

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_notificationscontacts.types.email_contact_address
    import capo_notificationscontacts.types.email_contact_name
    import capo_notificationscontacts.types.tag_map


class CreateEmailContactRequest(TypedDict, closed=True):
    name: "capo_notificationscontacts.types.email_contact_name.EmailContactName"
    """<p>The name of the email contact.</p>"""
    email_address: (
        "capo_notificationscontacts.types.email_contact_address.EmailContactAddress"
    )
    """<p>The email address this email contact points to. The activation email and any subscribed emails are sent here.</p> <note> <p>This email address can't receive emails until it's activated.</p> </note>"""
    tags: NotRequired["capo_notificationscontacts.types.tag_map.TagMap"]
    """<p>A map of tags assigned to a resource. A tag is a string-to-string map of key-value pairs.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: CreateEmailContactRequest) -> dict:
    out: dict = {}
    out["name"] = value["name"]
    out["emailAddress"] = value["email_address"]
    if "tags" in value:
        import capo_notificationscontacts.types.tag_map

        out["tags"] = capo_notificationscontacts.types.tag_map.serialize_json(
            value["tags"]
        )
    return out


def deserialize_json(data: dict) -> CreateEmailContactRequest:
    out: CreateEmailContactRequest = {}  # type: ignore[typeddict-item]
    if data.get("name") is not None:
        out["name"] = data["name"]
    else:
        out["name"] = ""
    if data.get("emailAddress") is not None:
        out["email_address"] = data["emailAddress"]
    else:
        out["email_address"] = ""
    if data.get("tags") is not None:
        import capo_notificationscontacts.types.tag_map

        out["tags"] = capo_notificationscontacts.types.tag_map.deserialize_json(
            data["tags"]
        )
    return out


def redact_sensitive(value: CreateEmailContactRequest) -> dict[str, Any]:
    out: dict[str, Any] = dict(value)
    if "name" in value:
        out["name"] = "*** Sensitive Data Redacted ***"
    return out
