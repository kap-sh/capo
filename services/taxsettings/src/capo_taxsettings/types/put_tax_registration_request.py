"""Generated from Smithy shape ``com.amazonaws.taxsettings#PutTaxRegistrationRequest``."""

from typing import TYPE_CHECKING, Any

from typing_extensions import NotRequired, TypedDict

from capo_taxsettings.errors import DeserializationError

if TYPE_CHECKING:
    import capo_taxsettings.types.account_id
    import capo_taxsettings.types.tax_registration_entry


class PutTaxRegistrationRequest(TypedDict, closed=True):
    account_id: NotRequired["capo_taxsettings.types.account_id.AccountId"]
    """<p>Your unique account identifier. </p>"""
    tax_registration_entry: (
        "capo_taxsettings.types.tax_registration_entry.TaxRegistrationEntry"
    )
    """<p> Your TRN information that will be stored to the account mentioned in <code>accountId</code>. </p>"""


# --- restJson1 ser/de ---
def serialize_json(value: PutTaxRegistrationRequest) -> dict:
    out: dict = {}
    if "account_id" in value:
        out["accountId"] = value["account_id"]
    import capo_taxsettings.types.tax_registration_entry

    out["taxRegistrationEntry"] = (
        capo_taxsettings.types.tax_registration_entry.serialize_json(
            value["tax_registration_entry"]
        )
    )
    return out


def deserialize_json(data: dict) -> PutTaxRegistrationRequest:
    out: PutTaxRegistrationRequest = {}  # type: ignore[typeddict-item]
    if data.get("accountId") is not None:
        out["account_id"] = data["accountId"]
    if data.get("taxRegistrationEntry") is not None:
        import capo_taxsettings.types.tax_registration_entry

        out["tax_registration_entry"] = (
            capo_taxsettings.types.tax_registration_entry.deserialize_json(
                data["taxRegistrationEntry"]
            )
        )
    else:
        raise DeserializationError(
            "PutTaxRegistrationRequest.tax_registration_entry required"
        )
    return out


def redact_sensitive(value: PutTaxRegistrationRequest) -> dict[str, Any]:
    out: dict[str, Any] = dict(value)
    if "tax_registration_entry" in value:
        out["tax_registration_entry"] = "*** Sensitive Data Redacted ***"
    return out
