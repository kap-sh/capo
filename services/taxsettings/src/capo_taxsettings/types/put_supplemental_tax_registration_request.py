"""Generated from Smithy shape ``com.amazonaws.taxsettings#PutSupplementalTaxRegistrationRequest``."""

from typing import TYPE_CHECKING, Any

from typing_extensions import TypedDict

from capo_taxsettings.errors import DeserializationError

if TYPE_CHECKING:
    import capo_taxsettings.types.supplemental_tax_registration_entry


class PutSupplementalTaxRegistrationRequest(TypedDict, closed=True):
    tax_registration_entry: "capo_taxsettings.types.supplemental_tax_registration_entry.SupplementalTaxRegistrationEntry"
    """<p> The supplemental TRN information that will be stored for the caller account ID. </p>"""


# --- restJson1 ser/de ---
def serialize_json(value: PutSupplementalTaxRegistrationRequest) -> dict:
    out: dict = {}
    import capo_taxsettings.types.supplemental_tax_registration_entry

    out["taxRegistrationEntry"] = (
        capo_taxsettings.types.supplemental_tax_registration_entry.serialize_json(
            value["tax_registration_entry"]
        )
    )
    return out


def deserialize_json(data: dict) -> PutSupplementalTaxRegistrationRequest:
    out: PutSupplementalTaxRegistrationRequest = {}  # type: ignore[typeddict-item]
    if data.get("taxRegistrationEntry") is not None:
        import capo_taxsettings.types.supplemental_tax_registration_entry

        out["tax_registration_entry"] = (
            capo_taxsettings.types.supplemental_tax_registration_entry.deserialize_json(
                data["taxRegistrationEntry"]
            )
        )
    else:
        raise DeserializationError(
            "PutSupplementalTaxRegistrationRequest.tax_registration_entry required"
        )
    return out


def redact_sensitive(value: PutSupplementalTaxRegistrationRequest) -> dict[str, Any]:
    out: dict[str, Any] = dict(value)
    if "tax_registration_entry" in value:
        out["tax_registration_entry"] = "*** Sensitive Data Redacted ***"
    return out
