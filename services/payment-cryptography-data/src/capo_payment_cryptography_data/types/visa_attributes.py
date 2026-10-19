"""Generated from Smithy shape ``com.amazonaws.paymentcryptographydata#VisaAttributes``."""

from typing import TYPE_CHECKING, Any

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_payment_cryptography_data.types.current_pin_attributes
    import capo_payment_cryptography_data.types.hex_length_equals4
    import capo_payment_cryptography_data.types.key_arn_or_key_alias_type
    import capo_payment_cryptography_data.types.major_key_derivation_mode
    import capo_payment_cryptography_data.types.number_length_equals2
    import capo_payment_cryptography_data.types.primary_account_number_type


class VisaAttributes(TypedDict, closed=True):
    major_key_derivation_mode: "capo_payment_cryptography_data.types.major_key_derivation_mode.MajorKeyDerivationMode"
    """<p>The method to use when deriving the master key for the payment card.</p>"""
    primary_account_number: "capo_payment_cryptography_data.types.primary_account_number_type.PrimaryAccountNumberType"
    """<p>The Primary Account Number (PAN) of the cardholder.</p>"""
    pan_sequence_number: (
        "capo_payment_cryptography_data.types.number_length_equals2.NumberLengthEquals2"
    )
    """<p>A number that identifies and differentiates payment cards with the same Primary Account Number (PAN). Typically 00 is used, if no value is provided by the terminal.</p>"""
    application_transaction_counter: (
        "capo_payment_cryptography_data.types.hex_length_equals4.HexLengthEquals4"
    )
    """<p>The transaction counter of the current transaction that is provided by the terminal during transaction processing.</p>"""
    authorization_request_key_identifier: "capo_payment_cryptography_data.types.key_arn_or_key_alias_type.KeyArnOrKeyAliasType"
    """<p>The <code>keyArn</code> of the issuer master key for cryptogram (IMK-AC) for the payment card.</p>"""
    current_pin_attributes: NotRequired[
        "capo_payment_cryptography_data.types.current_pin_attributes.CurrentPinAttributes"
    ]
    """<p>The encrypted pinblock of the old pin stored on the chip card.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: VisaAttributes) -> dict:
    out: dict = {}
    import capo_payment_cryptography_data.types.major_key_derivation_mode

    out["MajorKeyDerivationMode"] = (
        capo_payment_cryptography_data.types.major_key_derivation_mode.serialize_json(
            value["major_key_derivation_mode"]
        )
    )
    out["PrimaryAccountNumber"] = value["primary_account_number"]
    out["PanSequenceNumber"] = value["pan_sequence_number"]
    out["ApplicationTransactionCounter"] = value["application_transaction_counter"]
    out["AuthorizationRequestKeyIdentifier"] = value[
        "authorization_request_key_identifier"
    ]
    if "current_pin_attributes" in value:
        import capo_payment_cryptography_data.types.current_pin_attributes

        out["CurrentPinAttributes"] = (
            capo_payment_cryptography_data.types.current_pin_attributes.serialize_json(
                value["current_pin_attributes"]
            )
        )
    return out


def deserialize_json(data: dict) -> VisaAttributes:
    out: VisaAttributes = {}  # type: ignore[typeddict-item]
    if data.get("MajorKeyDerivationMode") is not None:
        import capo_payment_cryptography_data.types.major_key_derivation_mode

        out["major_key_derivation_mode"] = (
            capo_payment_cryptography_data.types.major_key_derivation_mode.deserialize_json(
                data["MajorKeyDerivationMode"]
            )
        )
    else:
        import typing

        out["major_key_derivation_mode"] = typing.cast(
            "capo_payment_cryptography_data.types.major_key_derivation_mode.MajorKeyDerivationMode",
            "",
        )
    if data.get("PrimaryAccountNumber") is not None:
        out["primary_account_number"] = data["PrimaryAccountNumber"]
    else:
        out["primary_account_number"] = ""
    if data.get("PanSequenceNumber") is not None:
        out["pan_sequence_number"] = data["PanSequenceNumber"]
    else:
        out["pan_sequence_number"] = ""
    if data.get("ApplicationTransactionCounter") is not None:
        out["application_transaction_counter"] = data["ApplicationTransactionCounter"]
    else:
        out["application_transaction_counter"] = ""
    if data.get("AuthorizationRequestKeyIdentifier") is not None:
        out["authorization_request_key_identifier"] = data[
            "AuthorizationRequestKeyIdentifier"
        ]
    else:
        out["authorization_request_key_identifier"] = ""
    if data.get("CurrentPinAttributes") is not None:
        import capo_payment_cryptography_data.types.current_pin_attributes

        out["current_pin_attributes"] = (
            capo_payment_cryptography_data.types.current_pin_attributes.deserialize_json(
                data["CurrentPinAttributes"]
            )
        )
    return out


def redact_sensitive(value: VisaAttributes) -> dict[str, Any]:
    out: dict[str, Any] = dict(value)
    if "primary_account_number" in value:
        out["primary_account_number"] = "*** Sensitive Data Redacted ***"
    if "current_pin_attributes" in value:
        import capo_payment_cryptography_data.types.current_pin_attributes

        out["current_pin_attributes"] = (
            capo_payment_cryptography_data.types.current_pin_attributes.redact_sensitive(
                value["current_pin_attributes"]
            )
        )
    return out
