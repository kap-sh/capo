"""Generated from Smithy shape ``com.amazonaws.paymentcryptographydata#PinGenerationAttributes``."""

from typing import TYPE_CHECKING, Any, TypeAlias

from typing_extensions import TypedDict

from capo_payment_cryptography_data.errors import (
    DeserializationError,
    SerializationError,
)

if TYPE_CHECKING:
    import capo_payment_cryptography_data.types.ibm3624_natural_pin
    import capo_payment_cryptography_data.types.ibm3624_pin_from_offset
    import capo_payment_cryptography_data.types.ibm3624_pin_offset
    import capo_payment_cryptography_data.types.ibm3624_random_pin
    import capo_payment_cryptography_data.types.visa_pin
    import capo_payment_cryptography_data.types.visa_pin_verification_value


class _PinGenerationAttributes_VisaPin(TypedDict, closed=True):
    VisaPin: "capo_payment_cryptography_data.types.visa_pin.VisaPin"


class _PinGenerationAttributes_VisaPinVerificationValue(TypedDict, closed=True):
    VisaPinVerificationValue: "capo_payment_cryptography_data.types.visa_pin_verification_value.VisaPinVerificationValue"


class _PinGenerationAttributes_Ibm3624PinOffset(TypedDict, closed=True):
    Ibm3624PinOffset: (
        "capo_payment_cryptography_data.types.ibm3624_pin_offset.Ibm3624PinOffset"
    )


class _PinGenerationAttributes_Ibm3624NaturalPin(TypedDict, closed=True):
    Ibm3624NaturalPin: (
        "capo_payment_cryptography_data.types.ibm3624_natural_pin.Ibm3624NaturalPin"
    )


class _PinGenerationAttributes_Ibm3624RandomPin(TypedDict, closed=True):
    Ibm3624RandomPin: (
        "capo_payment_cryptography_data.types.ibm3624_random_pin.Ibm3624RandomPin"
    )


class _PinGenerationAttributes_Ibm3624PinFromOffset(TypedDict, closed=True):
    Ibm3624PinFromOffset: "capo_payment_cryptography_data.types.ibm3624_pin_from_offset.Ibm3624PinFromOffset"


PinGenerationAttributes: TypeAlias = (
    _PinGenerationAttributes_VisaPin
    | _PinGenerationAttributes_VisaPinVerificationValue
    | _PinGenerationAttributes_Ibm3624PinOffset
    | _PinGenerationAttributes_Ibm3624NaturalPin
    | _PinGenerationAttributes_Ibm3624RandomPin
    | _PinGenerationAttributes_Ibm3624PinFromOffset
)


# --- restJson1 ser/de ---
def serialize_json(value: PinGenerationAttributes) -> dict:
    if "VisaPin" in value:
        import capo_payment_cryptography_data.types.visa_pin

        return {
            "VisaPin": capo_payment_cryptography_data.types.visa_pin.serialize_json(
                value["VisaPin"]
            )
        }
    elif "VisaPinVerificationValue" in value:
        import capo_payment_cryptography_data.types.visa_pin_verification_value

        return {
            "VisaPinVerificationValue": capo_payment_cryptography_data.types.visa_pin_verification_value.serialize_json(
                value["VisaPinVerificationValue"]
            )
        }
    elif "Ibm3624PinOffset" in value:
        import capo_payment_cryptography_data.types.ibm3624_pin_offset

        return {
            "Ibm3624PinOffset": capo_payment_cryptography_data.types.ibm3624_pin_offset.serialize_json(
                value["Ibm3624PinOffset"]
            )
        }
    elif "Ibm3624NaturalPin" in value:
        import capo_payment_cryptography_data.types.ibm3624_natural_pin

        return {
            "Ibm3624NaturalPin": capo_payment_cryptography_data.types.ibm3624_natural_pin.serialize_json(
                value["Ibm3624NaturalPin"]
            )
        }
    elif "Ibm3624RandomPin" in value:
        import capo_payment_cryptography_data.types.ibm3624_random_pin

        return {
            "Ibm3624RandomPin": capo_payment_cryptography_data.types.ibm3624_random_pin.serialize_json(
                value["Ibm3624RandomPin"]
            )
        }
    elif "Ibm3624PinFromOffset" in value:
        import capo_payment_cryptography_data.types.ibm3624_pin_from_offset

        return {
            "Ibm3624PinFromOffset": capo_payment_cryptography_data.types.ibm3624_pin_from_offset.serialize_json(
                value["Ibm3624PinFromOffset"]
            )
        }
    else:
        raise SerializationError("PinGenerationAttributes: no variant present")


def deserialize_json(data: dict) -> PinGenerationAttributes:
    if data.get("VisaPin") is not None:
        import capo_payment_cryptography_data.types.visa_pin

        return {
            "VisaPin": capo_payment_cryptography_data.types.visa_pin.deserialize_json(
                data["VisaPin"]
            )
        }
    elif data.get("VisaPinVerificationValue") is not None:
        import capo_payment_cryptography_data.types.visa_pin_verification_value

        return {
            "VisaPinVerificationValue": capo_payment_cryptography_data.types.visa_pin_verification_value.deserialize_json(
                data["VisaPinVerificationValue"]
            )
        }
    elif data.get("Ibm3624PinOffset") is not None:
        import capo_payment_cryptography_data.types.ibm3624_pin_offset

        return {
            "Ibm3624PinOffset": capo_payment_cryptography_data.types.ibm3624_pin_offset.deserialize_json(
                data["Ibm3624PinOffset"]
            )
        }
    elif data.get("Ibm3624NaturalPin") is not None:
        import capo_payment_cryptography_data.types.ibm3624_natural_pin

        return {
            "Ibm3624NaturalPin": capo_payment_cryptography_data.types.ibm3624_natural_pin.deserialize_json(
                data["Ibm3624NaturalPin"]
            )
        }
    elif data.get("Ibm3624RandomPin") is not None:
        import capo_payment_cryptography_data.types.ibm3624_random_pin

        return {
            "Ibm3624RandomPin": capo_payment_cryptography_data.types.ibm3624_random_pin.deserialize_json(
                data["Ibm3624RandomPin"]
            )
        }
    elif data.get("Ibm3624PinFromOffset") is not None:
        import capo_payment_cryptography_data.types.ibm3624_pin_from_offset

        return {
            "Ibm3624PinFromOffset": capo_payment_cryptography_data.types.ibm3624_pin_from_offset.deserialize_json(
                data["Ibm3624PinFromOffset"]
            )
        }
    else:
        raise DeserializationError("PinGenerationAttributes: no recognized variant key")


def redact_sensitive(value: PinGenerationAttributes) -> dict[str, Any]:
    out: dict[str, Any] = dict(value)
    if "VisaPinVerificationValue" in value:
        import capo_payment_cryptography_data.types.visa_pin_verification_value

        out["VisaPinVerificationValue"] = (
            capo_payment_cryptography_data.types.visa_pin_verification_value.redact_sensitive(
                value["VisaPinVerificationValue"]
            )
        )
    if "Ibm3624PinOffset" in value:
        import capo_payment_cryptography_data.types.ibm3624_pin_offset

        out["Ibm3624PinOffset"] = (
            capo_payment_cryptography_data.types.ibm3624_pin_offset.redact_sensitive(
                value["Ibm3624PinOffset"]
            )
        )
    if "Ibm3624NaturalPin" in value:
        import capo_payment_cryptography_data.types.ibm3624_natural_pin

        out["Ibm3624NaturalPin"] = (
            capo_payment_cryptography_data.types.ibm3624_natural_pin.redact_sensitive(
                value["Ibm3624NaturalPin"]
            )
        )
    if "Ibm3624RandomPin" in value:
        import capo_payment_cryptography_data.types.ibm3624_random_pin

        out["Ibm3624RandomPin"] = (
            capo_payment_cryptography_data.types.ibm3624_random_pin.redact_sensitive(
                value["Ibm3624RandomPin"]
            )
        )
    if "Ibm3624PinFromOffset" in value:
        import capo_payment_cryptography_data.types.ibm3624_pin_from_offset

        out["Ibm3624PinFromOffset"] = (
            capo_payment_cryptography_data.types.ibm3624_pin_from_offset.redact_sensitive(
                value["Ibm3624PinFromOffset"]
            )
        )
    return out
