"""Generated from Smithy shape ``com.amazonaws.notificationscontacts#EmailContact``."""

from typing import TYPE_CHECKING, Any

from typing_extensions import TypedDict

from capo_notificationscontacts.errors import DeserializationError

if TYPE_CHECKING:
    import capo_notificationscontacts.types.creation_time
    import capo_notificationscontacts.types.email_contact_arn
    import capo_notificationscontacts.types.email_contact_name
    import capo_notificationscontacts.types.email_contact_status
    import capo_notificationscontacts.types.sensitive_email_contact_address
    import capo_notificationscontacts.types.update_time


class EmailContact(TypedDict, closed=True):
    arn: "capo_notificationscontacts.types.email_contact_arn.EmailContactArn"
    """<p>The Amazon Resource Name (ARN) of the email contact.</p>"""
    name: "capo_notificationscontacts.types.email_contact_name.EmailContactName"
    """<p>The name of the email contact.</p>"""
    address: "capo_notificationscontacts.types.sensitive_email_contact_address.SensitiveEmailContactAddress"
    """<p>The email address this email contact points to. The activation email and any subscribed emails are sent here.</p>"""
    status: "capo_notificationscontacts.types.email_contact_status.EmailContactStatus"
    """<p>The status of the email contact. Only activated email contacts receive emails.</p>"""
    creation_time: "capo_notificationscontacts.types.creation_time.CreationTime"
    """<p>The creation time of the resource.</p>"""
    update_time: "capo_notificationscontacts.types.update_time.UpdateTime"
    """<p>The time the resource was last updated.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: EmailContact) -> dict:
    out: dict = {}
    out["arn"] = value["arn"]
    out["name"] = value["name"]
    out["address"] = value["address"]
    out["status"] = value["status"]
    import capo_notificationscontacts.types.creation_time

    out["creationTime"] = capo_notificationscontacts.types.creation_time.serialize_json(
        value["creation_time"]
    )
    import capo_notificationscontacts.types.update_time

    out["updateTime"] = capo_notificationscontacts.types.update_time.serialize_json(
        value["update_time"]
    )
    return out


def deserialize_json(data: dict) -> EmailContact:
    out: EmailContact = {}  # type: ignore[typeddict-item]
    if data.get("arn") is not None:
        out["arn"] = data["arn"]
    else:
        raise DeserializationError("EmailContact.arn required")
    if data.get("name") is not None:
        out["name"] = data["name"]
    else:
        raise DeserializationError("EmailContact.name required")
    if data.get("address") is not None:
        out["address"] = data["address"]
    else:
        raise DeserializationError("EmailContact.address required")
    if data.get("status") is not None:
        out["status"] = data["status"]
    else:
        raise DeserializationError("EmailContact.status required")
    if data.get("creationTime") is not None:
        import capo_notificationscontacts.types.creation_time

        out["creation_time"] = (
            capo_notificationscontacts.types.creation_time.deserialize_json(
                data["creationTime"]
            )
        )
    else:
        raise DeserializationError("EmailContact.creation_time required")
    if data.get("updateTime") is not None:
        import capo_notificationscontacts.types.update_time

        out["update_time"] = (
            capo_notificationscontacts.types.update_time.deserialize_json(
                data["updateTime"]
            )
        )
    else:
        raise DeserializationError("EmailContact.update_time required")
    return out


def redact_sensitive(value: EmailContact) -> dict[str, Any]:
    out: dict[str, Any] = dict(value)
    if "name" in value:
        out["name"] = "*** Sensitive Data Redacted ***"
    if "address" in value:
        out["address"] = "*** Sensitive Data Redacted ***"
    return out
