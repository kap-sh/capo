"""Generated from Smithy shape ``com.amazonaws.paymentcryptographydata#VerifyAuthRequestCryptogramInput``."""

from typing import TYPE_CHECKING, Any

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_payment_cryptography_data.types.auth_request_cryptogram_type
    import capo_payment_cryptography_data.types.cryptogram_auth_response
    import capo_payment_cryptography_data.types.key_arn_or_key_alias_type
    import capo_payment_cryptography_data.types.major_key_derivation_mode
    import capo_payment_cryptography_data.types.session_key_derivation
    import capo_payment_cryptography_data.types.transaction_data_type


class VerifyAuthRequestCryptogramInput(TypedDict, closed=True):
    key_identifier: "capo_payment_cryptography_data.types.key_arn_or_key_alias_type.KeyArnOrKeyAliasType"
    """<p>The <code>keyARN</code> of the major encryption key that Amazon Web Services Payment Cryptography uses for ARQC verification.</p>"""
    transaction_data: (
        "capo_payment_cryptography_data.types.transaction_data_type.TransactionDataType"
    )
    """<p>The transaction data that Amazon Web Services Payment Cryptography uses for ARQC verification. The same transaction is used for ARQC generation outside of Amazon Web Services Payment Cryptography.</p>"""
    auth_request_cryptogram: "capo_payment_cryptography_data.types.auth_request_cryptogram_type.AuthRequestCryptogramType"
    """<p>The auth request cryptogram imported into Amazon Web Services Payment Cryptography for ARQC verification using a major encryption key and transaction data.</p>"""
    major_key_derivation_mode: "capo_payment_cryptography_data.types.major_key_derivation_mode.MajorKeyDerivationMode"
    """<p>The method to use when deriving the major encryption key for ARQC verification within Amazon Web Services Payment Cryptography. The same key derivation mode was used for ARQC generation outside of Amazon Web Services Payment Cryptography.</p>"""
    session_key_derivation_attributes: "capo_payment_cryptography_data.types.session_key_derivation.SessionKeyDerivation"
    """<p>The attributes and values to use for deriving a session key for ARQC verification within Amazon Web Services Payment Cryptography. The same attributes were used for ARQC generation outside of Amazon Web Services Payment Cryptography.</p>"""
    auth_response_attributes: NotRequired[
        "capo_payment_cryptography_data.types.cryptogram_auth_response.CryptogramAuthResponse"
    ]
    """<p>The attributes and values for auth request cryptogram verification. These parameters are required in case using ARPC Method 1 or Method 2 for ARQC verification.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: VerifyAuthRequestCryptogramInput) -> dict:
    out: dict = {}
    out["KeyIdentifier"] = value["key_identifier"]
    out["TransactionData"] = value["transaction_data"]
    out["AuthRequestCryptogram"] = value["auth_request_cryptogram"]
    import capo_payment_cryptography_data.types.major_key_derivation_mode

    out["MajorKeyDerivationMode"] = (
        capo_payment_cryptography_data.types.major_key_derivation_mode.serialize_json(
            value["major_key_derivation_mode"]
        )
    )
    import capo_payment_cryptography_data.types.session_key_derivation

    out["SessionKeyDerivationAttributes"] = (
        capo_payment_cryptography_data.types.session_key_derivation.serialize_json(
            value["session_key_derivation_attributes"]
        )
    )
    if "auth_response_attributes" in value:
        import capo_payment_cryptography_data.types.cryptogram_auth_response

        out["AuthResponseAttributes"] = (
            capo_payment_cryptography_data.types.cryptogram_auth_response.serialize_json(
                value["auth_response_attributes"]
            )
        )
    return out


def deserialize_json(data: dict) -> VerifyAuthRequestCryptogramInput:
    out: VerifyAuthRequestCryptogramInput = {}  # type: ignore[typeddict-item]
    if data.get("KeyIdentifier") is not None:
        out["key_identifier"] = data["KeyIdentifier"]
    else:
        out["key_identifier"] = ""
    if data.get("TransactionData") is not None:
        out["transaction_data"] = data["TransactionData"]
    else:
        out["transaction_data"] = ""
    if data.get("AuthRequestCryptogram") is not None:
        out["auth_request_cryptogram"] = data["AuthRequestCryptogram"]
    else:
        out["auth_request_cryptogram"] = ""
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
    if data.get("SessionKeyDerivationAttributes") is not None:
        import capo_payment_cryptography_data.types.session_key_derivation

        out["session_key_derivation_attributes"] = (
            capo_payment_cryptography_data.types.session_key_derivation.deserialize_json(
                data["SessionKeyDerivationAttributes"]
            )
        )
    else:
        out["session_key_derivation_attributes"] = {"$unknown": {"name": ""}}
    if data.get("AuthResponseAttributes") is not None:
        import capo_payment_cryptography_data.types.cryptogram_auth_response

        out["auth_response_attributes"] = (
            capo_payment_cryptography_data.types.cryptogram_auth_response.deserialize_json(
                data["AuthResponseAttributes"]
            )
        )
    return out


def redact_sensitive(value: VerifyAuthRequestCryptogramInput) -> dict[str, Any]:
    out: dict[str, Any] = dict(value)
    if "transaction_data" in value:
        out["transaction_data"] = "*** Sensitive Data Redacted ***"
    if "auth_request_cryptogram" in value:
        out["auth_request_cryptogram"] = "*** Sensitive Data Redacted ***"
    if "session_key_derivation_attributes" in value:
        import capo_payment_cryptography_data.types.session_key_derivation

        out["session_key_derivation_attributes"] = (
            capo_payment_cryptography_data.types.session_key_derivation.redact_sensitive(
                value["session_key_derivation_attributes"]
            )
        )
    if "auth_response_attributes" in value:
        import capo_payment_cryptography_data.types.cryptogram_auth_response

        out["auth_response_attributes"] = (
            capo_payment_cryptography_data.types.cryptogram_auth_response.redact_sensitive(
                value["auth_response_attributes"]
            )
        )
    return out
