"""Generated from Smithy shape ``com.amazonaws.paymentcryptographydata#VerifyCardValidationDataInput``."""

from typing import TYPE_CHECKING, Any

from typing_extensions import TypedDict

from capo_payment_cryptography_data.errors import DeserializationError

if TYPE_CHECKING:
    import capo_payment_cryptography_data.types.card_verification_attributes
    import capo_payment_cryptography_data.types.key_arn_or_key_alias_type
    import capo_payment_cryptography_data.types.primary_account_number_type
    import capo_payment_cryptography_data.types.validation_data_type


class VerifyCardValidationDataInput(TypedDict, closed=True):
    key_identifier: "capo_payment_cryptography_data.types.key_arn_or_key_alias_type.KeyArnOrKeyAliasType"
    """<p>The <code>keyARN</code> of the CVK encryption key that Amazon Web Services Payment Cryptography uses to verify card data.</p>"""
    primary_account_number: "capo_payment_cryptography_data.types.primary_account_number_type.PrimaryAccountNumberType"
    """<p>The Primary Account Number (PAN), a unique identifier for a payment credit or debit card that associates the card with a specific account holder.</p>"""
    verification_attributes: "capo_payment_cryptography_data.types.card_verification_attributes.CardVerificationAttributes"
    """<p>The algorithm to use for verification of card data within Amazon Web Services Payment Cryptography.</p>"""
    validation_data: (
        "capo_payment_cryptography_data.types.validation_data_type.ValidationDataType"
    )
    """<p>The CVV or CSC value for use for card data verification within Amazon Web Services Payment Cryptography.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: VerifyCardValidationDataInput) -> dict:
    out: dict = {}
    out["KeyIdentifier"] = value["key_identifier"]
    out["PrimaryAccountNumber"] = value["primary_account_number"]
    import capo_payment_cryptography_data.types.card_verification_attributes

    out["VerificationAttributes"] = (
        capo_payment_cryptography_data.types.card_verification_attributes.serialize_json(
            value["verification_attributes"]
        )
    )
    out["ValidationData"] = value["validation_data"]
    return out


def deserialize_json(data: dict) -> VerifyCardValidationDataInput:
    out: VerifyCardValidationDataInput = {}  # type: ignore[typeddict-item]
    if data.get("KeyIdentifier") is not None:
        out["key_identifier"] = data["KeyIdentifier"]
    else:
        raise DeserializationError(
            "VerifyCardValidationDataInput.key_identifier required"
        )
    if data.get("PrimaryAccountNumber") is not None:
        out["primary_account_number"] = data["PrimaryAccountNumber"]
    else:
        raise DeserializationError(
            "VerifyCardValidationDataInput.primary_account_number required"
        )
    if data.get("VerificationAttributes") is not None:
        import capo_payment_cryptography_data.types.card_verification_attributes

        out["verification_attributes"] = (
            capo_payment_cryptography_data.types.card_verification_attributes.deserialize_json(
                data["VerificationAttributes"]
            )
        )
    else:
        raise DeserializationError(
            "VerifyCardValidationDataInput.verification_attributes required"
        )
    if data.get("ValidationData") is not None:
        out["validation_data"] = data["ValidationData"]
    else:
        raise DeserializationError(
            "VerifyCardValidationDataInput.validation_data required"
        )
    return out


def redact_sensitive(value: VerifyCardValidationDataInput) -> dict[str, Any]:
    out: dict[str, Any] = dict(value)
    if "primary_account_number" in value:
        out["primary_account_number"] = "*** Sensitive Data Redacted ***"
    if "verification_attributes" in value:
        import capo_payment_cryptography_data.types.card_verification_attributes

        out["verification_attributes"] = (
            capo_payment_cryptography_data.types.card_verification_attributes.redact_sensitive(
                value["verification_attributes"]
            )
        )
    if "validation_data" in value:
        out["validation_data"] = "*** Sensitive Data Redacted ***"
    return out
