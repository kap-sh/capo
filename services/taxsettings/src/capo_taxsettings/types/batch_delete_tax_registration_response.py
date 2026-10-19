"""Generated from Smithy shape ``com.amazonaws.taxsettings#BatchDeleteTaxRegistrationResponse``."""

from typing import TYPE_CHECKING, Any

from typing_extensions import TypedDict

if TYPE_CHECKING:
    import capo_taxsettings.types.batch_delete_tax_registration_errors


class BatchDeleteTaxRegistrationResponse(TypedDict, closed=True):
    errors: "capo_taxsettings.types.batch_delete_tax_registration_errors.BatchDeleteTaxRegistrationErrors"
    """<p>The list of errors for the accounts the TRN information could not be deleted for. </p>"""


# --- restJson1 ser/de ---
def serialize_json(value: BatchDeleteTaxRegistrationResponse) -> dict:
    out: dict = {}
    import capo_taxsettings.types.batch_delete_tax_registration_errors

    out["errors"] = (
        capo_taxsettings.types.batch_delete_tax_registration_errors.serialize_json(
            value["errors"]
        )
    )
    return out


def deserialize_json(data: dict) -> BatchDeleteTaxRegistrationResponse:
    out: BatchDeleteTaxRegistrationResponse = {}  # type: ignore[typeddict-item]
    if data.get("errors") is not None:
        import capo_taxsettings.types.batch_delete_tax_registration_errors

        out["errors"] = (
            capo_taxsettings.types.batch_delete_tax_registration_errors.deserialize_json(
                data["errors"]
            )
        )
    else:
        out["errors"] = []
    return out


def redact_sensitive(value: BatchDeleteTaxRegistrationResponse) -> dict[str, Any]:
    out: dict[str, Any] = dict(value)
    if "errors" in value:
        import capo_taxsettings.types.batch_delete_tax_registration_errors

        out["errors"] = (
            capo_taxsettings.types.batch_delete_tax_registration_errors.redact_sensitive(
                value["errors"]
            )
        )
    return out
