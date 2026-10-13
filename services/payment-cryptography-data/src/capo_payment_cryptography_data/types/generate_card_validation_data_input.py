"""Generated from Smithy shape ``com.amazonaws.paymentcryptographydata#GenerateCardValidationDataInput``."""

from typing import TYPE_CHECKING, Any

from typing_extensions import NotRequired, TypedDict

from capo_payment_cryptography_data.errors import DeserializationError

if TYPE_CHECKING:
    import capo_payment_cryptography_data.types.card_generation_attributes
    import capo_payment_cryptography_data.types.integer_range_between3_and5_type
    import capo_payment_cryptography_data.types.key_arn_or_key_alias_type
    import capo_payment_cryptography_data.types.primary_account_number_type


class GenerateCardValidationDataInput(TypedDict, closed=True):
    key_identifier: "capo_payment_cryptography_data.types.key_arn_or_key_alias_type.KeyArnOrKeyAliasType"
    """<p>The <code>keyARN</code> of the CVK encryption key that Amazon Web Services Payment Cryptography uses to generate card data.</p>"""
    primary_account_number: "capo_payment_cryptography_data.types.primary_account_number_type.PrimaryAccountNumberType"
    """<p>The Primary Account Number (PAN), a unique identifier for a payment credit or debit card that associates the card with a specific account holder.</p>"""
    generation_attributes: "capo_payment_cryptography_data.types.card_generation_attributes.CardGenerationAttributes"
    """<p>The algorithm for generating CVV or CSC values for the card within Amazon Web Services Payment Cryptography.</p>"""
    validation_data_length: NotRequired[
        "capo_payment_cryptography_data.types.integer_range_between3_and5_type.IntegerRangeBetween3And5Type"
    ]
    """<p>The length of the CVV or CSC to be generated. The default value is 3.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: GenerateCardValidationDataInput) -> dict:
    out: dict = {}
    out["KeyIdentifier"] = value["key_identifier"]
    out["PrimaryAccountNumber"] = value["primary_account_number"]
    import capo_payment_cryptography_data.types.card_generation_attributes

    out["GenerationAttributes"] = (
        capo_payment_cryptography_data.types.card_generation_attributes.serialize_json(
            value["generation_attributes"]
        )
    )
    if "validation_data_length" in value:
        out["ValidationDataLength"] = value["validation_data_length"]
    return out


def deserialize_json(data: dict) -> GenerateCardValidationDataInput:
    out: GenerateCardValidationDataInput = {}  # type: ignore[typeddict-item]
    if data.get("KeyIdentifier") is not None:
        out["key_identifier"] = data["KeyIdentifier"]
    else:
        raise DeserializationError(
            "GenerateCardValidationDataInput.key_identifier required"
        )
    if data.get("PrimaryAccountNumber") is not None:
        out["primary_account_number"] = data["PrimaryAccountNumber"]
    else:
        raise DeserializationError(
            "GenerateCardValidationDataInput.primary_account_number required"
        )
    if data.get("GenerationAttributes") is not None:
        import capo_payment_cryptography_data.types.card_generation_attributes

        out["generation_attributes"] = (
            capo_payment_cryptography_data.types.card_generation_attributes.deserialize_json(
                data["GenerationAttributes"]
            )
        )
    else:
        raise DeserializationError(
            "GenerateCardValidationDataInput.generation_attributes required"
        )
    if data.get("ValidationDataLength") is not None:
        out["validation_data_length"] = data["ValidationDataLength"]
    return out


def redact_sensitive(value: GenerateCardValidationDataInput) -> dict[str, Any]:
    out: dict[str, Any] = dict(value)
    if "primary_account_number" in value:
        out["primary_account_number"] = "*** Sensitive Data Redacted ***"
    if "generation_attributes" in value:
        import capo_payment_cryptography_data.types.card_generation_attributes

        out["generation_attributes"] = (
            capo_payment_cryptography_data.types.card_generation_attributes.redact_sensitive(
                value["generation_attributes"]
            )
        )
    return out
