"""Generated from Smithy shape ``com.amazonaws.geoplaces#Contacts``."""

from typing import TYPE_CHECKING, Any

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_geo_places.types.contact_details_list


class Contacts(TypedDict, closed=True):
    phones: NotRequired["capo_geo_places.types.contact_details_list.ContactDetailsList"]
    """<p>List of phone numbers for the results contact. </p>"""
    faxes: NotRequired["capo_geo_places.types.contact_details_list.ContactDetailsList"]
    """<p>List of fax addresses for the result contact. </p>"""
    websites: NotRequired[
        "capo_geo_places.types.contact_details_list.ContactDetailsList"
    ]
    """<p>List of website URLs that belong to the result. </p>"""
    emails: NotRequired["capo_geo_places.types.contact_details_list.ContactDetailsList"]
    """<p>List of emails for contacts of the result. </p>"""


# --- restJson1 ser/de ---
def serialize_json(value: Contacts) -> dict:
    out: dict = {}
    if "phones" in value:
        import capo_geo_places.types.contact_details_list

        out["Phones"] = capo_geo_places.types.contact_details_list.serialize_json(
            value["phones"]
        )
    if "faxes" in value:
        import capo_geo_places.types.contact_details_list

        out["Faxes"] = capo_geo_places.types.contact_details_list.serialize_json(
            value["faxes"]
        )
    if "websites" in value:
        import capo_geo_places.types.contact_details_list

        out["Websites"] = capo_geo_places.types.contact_details_list.serialize_json(
            value["websites"]
        )
    if "emails" in value:
        import capo_geo_places.types.contact_details_list

        out["Emails"] = capo_geo_places.types.contact_details_list.serialize_json(
            value["emails"]
        )
    return out


def deserialize_json(data: dict) -> Contacts:
    out: Contacts = {}  # type: ignore[typeddict-item]
    if data.get("Phones") is not None:
        import capo_geo_places.types.contact_details_list

        out["phones"] = capo_geo_places.types.contact_details_list.deserialize_json(
            data["Phones"]
        )
    if data.get("Faxes") is not None:
        import capo_geo_places.types.contact_details_list

        out["faxes"] = capo_geo_places.types.contact_details_list.deserialize_json(
            data["Faxes"]
        )
    if data.get("Websites") is not None:
        import capo_geo_places.types.contact_details_list

        out["websites"] = capo_geo_places.types.contact_details_list.deserialize_json(
            data["Websites"]
        )
    if data.get("Emails") is not None:
        import capo_geo_places.types.contact_details_list

        out["emails"] = capo_geo_places.types.contact_details_list.deserialize_json(
            data["Emails"]
        )
    return out


def redact_sensitive(value: Contacts) -> dict[str, Any]:
    out: dict[str, Any] = dict(value)
    if "phones" in value:
        import capo_geo_places.types.contact_details_list

        out["phones"] = capo_geo_places.types.contact_details_list.redact_sensitive(
            value["phones"]
        )
    if "faxes" in value:
        import capo_geo_places.types.contact_details_list

        out["faxes"] = capo_geo_places.types.contact_details_list.redact_sensitive(
            value["faxes"]
        )
    if "websites" in value:
        import capo_geo_places.types.contact_details_list

        out["websites"] = capo_geo_places.types.contact_details_list.redact_sensitive(
            value["websites"]
        )
    if "emails" in value:
        import capo_geo_places.types.contact_details_list

        out["emails"] = capo_geo_places.types.contact_details_list.redact_sensitive(
            value["emails"]
        )
    return out
