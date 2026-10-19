"""Generated from Smithy shape ``com.amazonaws.sesv2#ContactListDestination``."""

from typing import TYPE_CHECKING

from typing_extensions import TypedDict

if TYPE_CHECKING:
    import capo_sesv2.types.contact_list_import_action
    import capo_sesv2.types.contact_list_name


class ContactListDestination(TypedDict, closed=True):
    contact_list_name: "capo_sesv2.types.contact_list_name.ContactListName"
    """<p>The name of the contact list.</p>"""
    contact_list_import_action: (
        "capo_sesv2.types.contact_list_import_action.ContactListImportAction"
    )
    """<p>>The type of action to perform on the addresses. The following are the possible values:</p> <ul> <li> <p>PUT: add the addresses to the contact list. If the record already exists, it will override it with the new value.</p> </li> <li> <p>DELETE: remove the addresses from the contact list.</p> </li> </ul>"""


# --- restJson1 ser/de ---
def serialize_json(value: ContactListDestination) -> dict:
    out: dict = {}
    out["ContactListName"] = value["contact_list_name"]
    import capo_sesv2.types.contact_list_import_action

    out["ContactListImportAction"] = (
        capo_sesv2.types.contact_list_import_action.serialize_json(
            value["contact_list_import_action"]
        )
    )
    return out


def deserialize_json(data: dict) -> ContactListDestination:
    out: ContactListDestination = {}  # type: ignore[typeddict-item]
    if data.get("ContactListName") is not None:
        out["contact_list_name"] = data["ContactListName"]
    else:
        out["contact_list_name"] = ""
    if data.get("ContactListImportAction") is not None:
        import capo_sesv2.types.contact_list_import_action

        out["contact_list_import_action"] = (
            capo_sesv2.types.contact_list_import_action.deserialize_json(
                data["ContactListImportAction"]
            )
        )
    else:
        import typing

        out["contact_list_import_action"] = typing.cast(
            "capo_sesv2.types.contact_list_import_action.ContactListImportAction", ""
        )
    return out
