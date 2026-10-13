"""Generated from Smithy shape ``com.amazonaws.paymentcryptographydata#PinVerificationAttributes``."""

from typing import TYPE_CHECKING, Any, TypeAlias

from typing_extensions import TypedDict

from capo_payment_cryptography_data.errors import (
    DeserializationError,
    SerializationError,
)

if TYPE_CHECKING:
    import capo_payment_cryptography_data.types.ibm3624_pin_verification
    import capo_payment_cryptography_data.types.visa_pin_verification


class _PinVerificationAttributes_VisaPin(TypedDict, closed=True):
    VisaPin: (
        "capo_payment_cryptography_data.types.visa_pin_verification.VisaPinVerification"
    )


class _PinVerificationAttributes_Ibm3624Pin(TypedDict, closed=True):
    Ibm3624Pin: "capo_payment_cryptography_data.types.ibm3624_pin_verification.Ibm3624PinVerification"


PinVerificationAttributes: TypeAlias = (
    _PinVerificationAttributes_VisaPin | _PinVerificationAttributes_Ibm3624Pin
)


# --- restJson1 ser/de ---
def serialize_json(value: PinVerificationAttributes) -> dict:
    if "VisaPin" in value:
        import capo_payment_cryptography_data.types.visa_pin_verification

        return {
            "VisaPin": capo_payment_cryptography_data.types.visa_pin_verification.serialize_json(
                value["VisaPin"]
            )
        }
    elif "Ibm3624Pin" in value:
        import capo_payment_cryptography_data.types.ibm3624_pin_verification

        return {
            "Ibm3624Pin": capo_payment_cryptography_data.types.ibm3624_pin_verification.serialize_json(
                value["Ibm3624Pin"]
            )
        }
    else:
        raise SerializationError("PinVerificationAttributes: no variant present")


def deserialize_json(data: dict) -> PinVerificationAttributes:
    if data.get("VisaPin") is not None:
        import capo_payment_cryptography_data.types.visa_pin_verification

        return {
            "VisaPin": capo_payment_cryptography_data.types.visa_pin_verification.deserialize_json(
                data["VisaPin"]
            )
        }
    elif data.get("Ibm3624Pin") is not None:
        import capo_payment_cryptography_data.types.ibm3624_pin_verification

        return {
            "Ibm3624Pin": capo_payment_cryptography_data.types.ibm3624_pin_verification.deserialize_json(
                data["Ibm3624Pin"]
            )
        }
    else:
        raise DeserializationError(
            "PinVerificationAttributes: no recognized variant key"
        )


def redact_sensitive(value: PinVerificationAttributes) -> dict[str, Any]:
    out: dict[str, Any] = dict(value)
    if "VisaPin" in value:
        import capo_payment_cryptography_data.types.visa_pin_verification

        out["VisaPin"] = (
            capo_payment_cryptography_data.types.visa_pin_verification.redact_sensitive(
                value["VisaPin"]
            )
        )
    if "Ibm3624Pin" in value:
        import capo_payment_cryptography_data.types.ibm3624_pin_verification

        out["Ibm3624Pin"] = (
            capo_payment_cryptography_data.types.ibm3624_pin_verification.redact_sensitive(
                value["Ibm3624Pin"]
            )
        )
    return out
