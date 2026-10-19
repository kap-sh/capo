"""Generated from Smithy shape ``com.amazonaws.taxsettings#BatchPutTaxRegistrationRequest``."""

from typing import TYPE_CHECKING, Any

from typing_extensions import TypedDict

from capo_taxsettings.errors import DeserializationError

if TYPE_CHECKING:
    import capo_taxsettings.types.account_ids
    import capo_taxsettings.types.tax_registration_entry


class BatchPutTaxRegistrationRequest(TypedDict, closed=True):
    account_ids: "capo_taxsettings.types.account_ids.AccountIds"
    """<p> List of unique account identifiers.</p>"""
    tax_registration_entry: (
        "capo_taxsettings.types.tax_registration_entry.TaxRegistrationEntry"
    )
    """<p>Your TRN information that will be stored to the accounts mentioned in <code>putEntries</code>. </p>"""


# --- restJson1 ser/de ---
def serialize_json(value: BatchPutTaxRegistrationRequest) -> dict:
    out: dict = {}
    import capo_taxsettings.types.account_ids

    out["accountIds"] = capo_taxsettings.types.account_ids.serialize_json(
        value["account_ids"]
    )
    import capo_taxsettings.types.tax_registration_entry

    out["taxRegistrationEntry"] = (
        capo_taxsettings.types.tax_registration_entry.serialize_json(
            value["tax_registration_entry"]
        )
    )
    return out


def deserialize_json(data: dict) -> BatchPutTaxRegistrationRequest:
    out: BatchPutTaxRegistrationRequest = {}  # type: ignore[typeddict-item]
    if data.get("accountIds") is not None:
        import capo_taxsettings.types.account_ids

        out["account_ids"] = capo_taxsettings.types.account_ids.deserialize_json(
            data["accountIds"]
        )
    else:
        out["account_ids"] = []
    if data.get("taxRegistrationEntry") is not None:
        import capo_taxsettings.types.tax_registration_entry

        out["tax_registration_entry"] = (
            capo_taxsettings.types.tax_registration_entry.deserialize_json(
                data["taxRegistrationEntry"]
            )
        )
    else:
        raise DeserializationError(
            "BatchPutTaxRegistrationRequest.tax_registration_entry required"
        )
    return out


def redact_sensitive(value: BatchPutTaxRegistrationRequest) -> dict[str, Any]:
    out: dict[str, Any] = dict(value)
    if "tax_registration_entry" in value:
        out["tax_registration_entry"] = "*** Sensitive Data Redacted ***"
    return out
