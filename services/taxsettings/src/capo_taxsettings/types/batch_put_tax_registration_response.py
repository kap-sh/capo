"""Generated from Smithy shape ``com.amazonaws.taxsettings#BatchPutTaxRegistrationResponse``."""

from typing import TYPE_CHECKING, Any

from typing_extensions import NotRequired, TypedDict

from capo_taxsettings.errors import DeserializationError

if TYPE_CHECKING:
    import capo_taxsettings.types.batch_put_tax_registration_errors
    import capo_taxsettings.types.tax_registration_status


class BatchPutTaxRegistrationResponse(TypedDict, closed=True):
    status: NotRequired[
        "capo_taxsettings.types.tax_registration_status.TaxRegistrationStatus"
    ]
    """<p>The status of your TRN stored in the system after processing. Based on the validation occurring on the TRN, the status can be <code>Verified</code>, <code>Pending</code> or <code>Rejected</code>. </p>"""
    errors: "capo_taxsettings.types.batch_put_tax_registration_errors.BatchPutTaxRegistrationErrors"
    """<p>List of errors for the accounts the TRN information could not be added or updated to. </p>"""


# --- restJson1 ser/de ---
def serialize_json(value: BatchPutTaxRegistrationResponse) -> dict:
    out: dict = {}
    if "status" in value:
        import capo_taxsettings.types.tax_registration_status

        out["status"] = capo_taxsettings.types.tax_registration_status.serialize_json(
            value["status"]
        )
    import capo_taxsettings.types.batch_put_tax_registration_errors

    out["errors"] = (
        capo_taxsettings.types.batch_put_tax_registration_errors.serialize_json(
            value["errors"]
        )
    )
    return out


def deserialize_json(data: dict) -> BatchPutTaxRegistrationResponse:
    out: BatchPutTaxRegistrationResponse = {}  # type: ignore[typeddict-item]
    if data.get("status") is not None:
        import capo_taxsettings.types.tax_registration_status

        out["status"] = capo_taxsettings.types.tax_registration_status.deserialize_json(
            data["status"]
        )
    if data.get("errors") is not None:
        import capo_taxsettings.types.batch_put_tax_registration_errors

        out["errors"] = (
            capo_taxsettings.types.batch_put_tax_registration_errors.deserialize_json(
                data["errors"]
            )
        )
    else:
        raise DeserializationError("BatchPutTaxRegistrationResponse.errors required")
    return out


def redact_sensitive(value: BatchPutTaxRegistrationResponse) -> dict[str, Any]:
    out: dict[str, Any] = dict(value)
    if "errors" in value:
        import capo_taxsettings.types.batch_put_tax_registration_errors

        out["errors"] = (
            capo_taxsettings.types.batch_put_tax_registration_errors.redact_sensitive(
                value["errors"]
            )
        )
    return out
