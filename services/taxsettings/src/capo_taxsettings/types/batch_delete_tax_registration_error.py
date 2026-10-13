"""Generated from Smithy shape ``com.amazonaws.taxsettings#BatchDeleteTaxRegistrationError``."""

from typing import TYPE_CHECKING, Any

from typing_extensions import NotRequired, TypedDict

from capo_taxsettings.errors import DeserializationError

if TYPE_CHECKING:
    import capo_taxsettings.types.account_id
    import capo_taxsettings.types.error_code
    import capo_taxsettings.types.error_message


class BatchDeleteTaxRegistrationError(TypedDict, closed=True):
    account_id: "capo_taxsettings.types.account_id.AccountId"
    """<p> The unique account identifier for the account whose tax registration couldn't be deleted during the <code>BatchDeleteTaxRegistration</code> operation. </p>"""
    message: "capo_taxsettings.types.error_message.ErrorMessage"
    """<p> The error message for an individual failure in the <code>BatchDeleteTaxRegistration</code> operation. </p>"""
    code: NotRequired["capo_taxsettings.types.error_code.ErrorCode"]
    """<p> The error code for an individual failure in BatchDeleteTaxRegistration operation. </p>"""


# --- restJson1 ser/de ---
def serialize_json(value: BatchDeleteTaxRegistrationError) -> dict:
    out: dict = {}
    out["accountId"] = value["account_id"]
    out["message"] = value["message"]
    if "code" in value:
        out["code"] = value["code"]
    return out


def deserialize_json(data: dict) -> BatchDeleteTaxRegistrationError:
    out: BatchDeleteTaxRegistrationError = {}  # type: ignore[typeddict-item]
    if data.get("accountId") is not None:
        out["account_id"] = data["accountId"]
    else:
        raise DeserializationError(
            "BatchDeleteTaxRegistrationError.account_id required"
        )
    if data.get("message") is not None:
        out["message"] = data["message"]
    else:
        raise DeserializationError("BatchDeleteTaxRegistrationError.message required")
    if data.get("code") is not None:
        out["code"] = data["code"]
    return out


def redact_sensitive(value: BatchDeleteTaxRegistrationError) -> dict[str, Any]:
    out: dict[str, Any] = dict(value)
    if "message" in value:
        out["message"] = "*** Sensitive Data Redacted ***"
    return out
