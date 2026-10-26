"""Generated from Smithy shape ``com.amazonaws.paymentcryptographydata#MacAlgorithmEmv``."""

from typing import TYPE_CHECKING, Any

from typing_extensions import TypedDict

if TYPE_CHECKING:
    import capo_payment_cryptography_data.types.major_key_derivation_mode
    import capo_payment_cryptography_data.types.number_length_equals2
    import capo_payment_cryptography_data.types.primary_account_number_type
    import capo_payment_cryptography_data.types.session_key_derivation_mode
    import capo_payment_cryptography_data.types.session_key_derivation_value


class MacAlgorithmEmv(TypedDict, closed=True):
    major_key_derivation_mode: "capo_payment_cryptography_data.types.major_key_derivation_mode.MajorKeyDerivationMode"
    """<p>The method to use when deriving the master key for EMV MAC generation or verification.</p>"""
    primary_account_number: "capo_payment_cryptography_data.types.primary_account_number_type.PrimaryAccountNumberType"
    """<p>The Primary Account Number (PAN), a unique identifier for a payment credit or debit card and associates the card to a specific account holder.</p>"""
    pan_sequence_number: (
        "capo_payment_cryptography_data.types.number_length_equals2.NumberLengthEquals2"
    )
    """<p>A number that identifies and differentiates payment cards with the same Primary Account Number (PAN).</p>"""
    session_key_derivation_mode: "capo_payment_cryptography_data.types.session_key_derivation_mode.SessionKeyDerivationMode"
    """<p>The method of deriving a session key for EMV MAC generation or verification.</p>"""
    session_key_derivation_value: "capo_payment_cryptography_data.types.session_key_derivation_value.SessionKeyDerivationValue"
    """<p>Parameters that are required to generate session key for EMV generation and verification.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: MacAlgorithmEmv) -> dict:
    out: dict = {}
    import capo_payment_cryptography_data.types.major_key_derivation_mode

    out["MajorKeyDerivationMode"] = (
        capo_payment_cryptography_data.types.major_key_derivation_mode.serialize_json(
            value["major_key_derivation_mode"]
        )
    )
    out["PrimaryAccountNumber"] = value["primary_account_number"]
    out["PanSequenceNumber"] = value["pan_sequence_number"]
    import capo_payment_cryptography_data.types.session_key_derivation_mode

    out["SessionKeyDerivationMode"] = (
        capo_payment_cryptography_data.types.session_key_derivation_mode.serialize_json(
            value["session_key_derivation_mode"]
        )
    )
    import capo_payment_cryptography_data.types.session_key_derivation_value

    out["SessionKeyDerivationValue"] = (
        capo_payment_cryptography_data.types.session_key_derivation_value.serialize_json(
            value["session_key_derivation_value"]
        )
    )
    return out


def deserialize_json(data: dict) -> MacAlgorithmEmv:
    out: MacAlgorithmEmv = {}  # type: ignore[typeddict-item]
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
    if data.get("SessionKeyDerivationMode") is not None:
        import capo_payment_cryptography_data.types.session_key_derivation_mode

        out["session_key_derivation_mode"] = (
            capo_payment_cryptography_data.types.session_key_derivation_mode.deserialize_json(
                data["SessionKeyDerivationMode"]
            )
        )
    else:
        import typing

        out["session_key_derivation_mode"] = typing.cast(
            "capo_payment_cryptography_data.types.session_key_derivation_mode.SessionKeyDerivationMode",
            "",
        )
    if data.get("SessionKeyDerivationValue") is not None:
        import capo_payment_cryptography_data.types.session_key_derivation_value

        out["session_key_derivation_value"] = (
            capo_payment_cryptography_data.types.session_key_derivation_value.deserialize_json(
                data["SessionKeyDerivationValue"]
            )
        )
    else:
        out["session_key_derivation_value"] = {"$unknown": {"name": ""}}
    return out


def redact_sensitive(value: MacAlgorithmEmv) -> dict[str, Any]:
    out: dict[str, Any] = dict(value)
    if "primary_account_number" in value:
        out["primary_account_number"] = "*** Sensitive Data Redacted ***"
    if "session_key_derivation_value" in value:
        import capo_payment_cryptography_data.types.session_key_derivation_value

        out["session_key_derivation_value"] = (
            capo_payment_cryptography_data.types.session_key_derivation_value.redact_sensitive(
                value["session_key_derivation_value"]
            )
        )
    return out
