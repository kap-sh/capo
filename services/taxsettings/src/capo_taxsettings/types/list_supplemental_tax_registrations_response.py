"""Generated from Smithy shape ``com.amazonaws.taxsettings#ListSupplementalTaxRegistrationsResponse``."""

from typing import TYPE_CHECKING, Any

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_taxsettings.types.pagination_token_string
    import capo_taxsettings.types.supplemental_tax_registration_list


class ListSupplementalTaxRegistrationsResponse(TypedDict, closed=True):
    tax_registrations: "capo_taxsettings.types.supplemental_tax_registration_list.SupplementalTaxRegistrationList"
    """<p> The list of supplemental tax registrations. </p>"""
    next_token: NotRequired[
        "capo_taxsettings.types.pagination_token_string.PaginationTokenString"
    ]
    """<p> The token to retrieve the next set of results. </p>"""


# --- restJson1 ser/de ---
def serialize_json(value: ListSupplementalTaxRegistrationsResponse) -> dict:
    out: dict = {}
    import capo_taxsettings.types.supplemental_tax_registration_list

    out["taxRegistrations"] = (
        capo_taxsettings.types.supplemental_tax_registration_list.serialize_json(
            value["tax_registrations"]
        )
    )
    if "next_token" in value:
        out["nextToken"] = value["next_token"]
    return out


def deserialize_json(data: dict) -> ListSupplementalTaxRegistrationsResponse:
    out: ListSupplementalTaxRegistrationsResponse = {}  # type: ignore[typeddict-item]
    if data.get("taxRegistrations") is not None:
        import capo_taxsettings.types.supplemental_tax_registration_list

        out["tax_registrations"] = (
            capo_taxsettings.types.supplemental_tax_registration_list.deserialize_json(
                data["taxRegistrations"]
            )
        )
    else:
        out["tax_registrations"] = []
    if data.get("nextToken") is not None:
        out["next_token"] = data["nextToken"]
    return out


def redact_sensitive(value: ListSupplementalTaxRegistrationsResponse) -> dict[str, Any]:
    out: dict[str, Any] = dict(value)
    if "tax_registrations" in value:
        import capo_taxsettings.types.supplemental_tax_registration_list

        out["tax_registrations"] = (
            capo_taxsettings.types.supplemental_tax_registration_list.redact_sensitive(
                value["tax_registrations"]
            )
        )
    return out
