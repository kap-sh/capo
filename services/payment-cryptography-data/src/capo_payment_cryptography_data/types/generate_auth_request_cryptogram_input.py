"""Generated from Smithy shape ``com.amazonaws.paymentcryptographydata#GenerateAuthRequestCryptogramInput``."""

from typing import TYPE_CHECKING, Any

from typing_extensions import TypedDict

if TYPE_CHECKING:
    import capo_payment_cryptography_data.types.key_arn_or_key_alias_type
    import capo_payment_cryptography_data.types.major_key_derivation_mode
    import capo_payment_cryptography_data.types.session_key_derivation
    import capo_payment_cryptography_data.types.transaction_data_type


class GenerateAuthRequestCryptogramInput(TypedDict, closed=True):
    key_identifier: "capo_payment_cryptography_data.types.key_arn_or_key_alias_type.KeyArnOrKeyAliasType"
    """<p>The <code>keyARN</code> of the IMK-AC (TR31_E0_EMV_MKEY_APP_CRYPTOGRAMS) that Amazon Web Services Payment Cryptography uses to generate the ARQC.</p>"""
    transaction_data: (
        "capo_payment_cryptography_data.types.transaction_data_type.TransactionDataType"
    )
    """<p>The transaction data that Amazon Web Services Payment Cryptography uses for ARQC generation. The same transaction data is used for ARQC verification by the issuer using <a>VerifyAuthRequestCryptogram</a>.</p>"""
    major_key_derivation_mode: "capo_payment_cryptography_data.types.major_key_derivation_mode.MajorKeyDerivationMode"
    """<p>The method to use when deriving the major encryption key for ARQC generation within Amazon Web Services Payment Cryptography.</p>"""
    session_key_derivation_attributes: "capo_payment_cryptography_data.types.session_key_derivation.SessionKeyDerivation"
    """<p>The attributes and values to use for deriving a session key for ARQC generation within Amazon Web Services Payment Cryptography.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: GenerateAuthRequestCryptogramInput) -> dict:
    out: dict = {}
    out["KeyIdentifier"] = value["key_identifier"]
    out["TransactionData"] = value["transaction_data"]
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
    return out


def deserialize_json(data: dict) -> GenerateAuthRequestCryptogramInput:
    out: GenerateAuthRequestCryptogramInput = {}  # type: ignore[typeddict-item]
    if data.get("KeyIdentifier") is not None:
        out["key_identifier"] = data["KeyIdentifier"]
    else:
        out["key_identifier"] = ""
    if data.get("TransactionData") is not None:
        out["transaction_data"] = data["TransactionData"]
    else:
        out["transaction_data"] = ""
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
    return out


def redact_sensitive(value: GenerateAuthRequestCryptogramInput) -> dict[str, Any]:
    out: dict[str, Any] = dict(value)
    if "transaction_data" in value:
        out["transaction_data"] = "*** Sensitive Data Redacted ***"
    if "session_key_derivation_attributes" in value:
        import capo_payment_cryptography_data.types.session_key_derivation

        out["session_key_derivation_attributes"] = (
            capo_payment_cryptography_data.types.session_key_derivation.redact_sensitive(
                value["session_key_derivation_attributes"]
            )
        )
    return out
