"""Generated from Smithy shape ``com.amazonaws.paymentcryptographydata#TranslationIsoFormats``."""

from typing import TYPE_CHECKING, Any, TypeAlias

from typing_extensions import TypedDict

from capo_payment_cryptography_data.errors import (
    DeserializationError,
    SerializationError,
)
from capo_payment_cryptography_data.types._unknown import UnknownUnionMember

if TYPE_CHECKING:
    import capo_payment_cryptography_data.types.translation_pin_data_as2805_format0
    import capo_payment_cryptography_data.types.translation_pin_data_iso_format034
    import capo_payment_cryptography_data.types.translation_pin_data_iso_format1


class _TranslationIsoFormats_IsoFormat0(TypedDict, closed=True):
    IsoFormat0: "capo_payment_cryptography_data.types.translation_pin_data_iso_format034.TranslationPinDataIsoFormat034"


class _TranslationIsoFormats_IsoFormat1(TypedDict, closed=True):
    IsoFormat1: "capo_payment_cryptography_data.types.translation_pin_data_iso_format1.TranslationPinDataIsoFormat1"


class _TranslationIsoFormats_IsoFormat3(TypedDict, closed=True):
    IsoFormat3: "capo_payment_cryptography_data.types.translation_pin_data_iso_format034.TranslationPinDataIsoFormat034"


class _TranslationIsoFormats_IsoFormat4(TypedDict, closed=True):
    IsoFormat4: "capo_payment_cryptography_data.types.translation_pin_data_iso_format034.TranslationPinDataIsoFormat034"


class _TranslationIsoFormats_As2805Format0(TypedDict, closed=True):
    As2805Format0: "capo_payment_cryptography_data.types.translation_pin_data_as2805_format0.TranslationPinDataAs2805Format0"


TranslationIsoFormats: TypeAlias = (
    _TranslationIsoFormats_IsoFormat0
    | _TranslationIsoFormats_IsoFormat1
    | _TranslationIsoFormats_IsoFormat3
    | _TranslationIsoFormats_IsoFormat4
    | _TranslationIsoFormats_As2805Format0
    | UnknownUnionMember
)


# --- restJson1 ser/de ---
def serialize_json(value: TranslationIsoFormats) -> dict:
    if "$unknown" in value:
        raise SerializationError(
            f"TranslationIsoFormats: cannot serialize unknown variant {value['$unknown']['name']!r}"
        )
    elif "IsoFormat0" in value:
        import capo_payment_cryptography_data.types.translation_pin_data_iso_format034

        return {
            "IsoFormat0": capo_payment_cryptography_data.types.translation_pin_data_iso_format034.serialize_json(
                value["IsoFormat0"]
            )
        }
    elif "IsoFormat1" in value:
        import capo_payment_cryptography_data.types.translation_pin_data_iso_format1

        return {
            "IsoFormat1": capo_payment_cryptography_data.types.translation_pin_data_iso_format1.serialize_json(
                value["IsoFormat1"]
            )
        }
    elif "IsoFormat3" in value:
        import capo_payment_cryptography_data.types.translation_pin_data_iso_format034

        return {
            "IsoFormat3": capo_payment_cryptography_data.types.translation_pin_data_iso_format034.serialize_json(
                value["IsoFormat3"]
            )
        }
    elif "IsoFormat4" in value:
        import capo_payment_cryptography_data.types.translation_pin_data_iso_format034

        return {
            "IsoFormat4": capo_payment_cryptography_data.types.translation_pin_data_iso_format034.serialize_json(
                value["IsoFormat4"]
            )
        }
    elif "As2805Format0" in value:
        import capo_payment_cryptography_data.types.translation_pin_data_as2805_format0

        return {
            "As2805Format0": capo_payment_cryptography_data.types.translation_pin_data_as2805_format0.serialize_json(
                value["As2805Format0"]
            )
        }
    else:
        raise SerializationError("TranslationIsoFormats: no variant present")


def deserialize_json(data: dict) -> TranslationIsoFormats:
    if data.get("IsoFormat0") is not None:
        import capo_payment_cryptography_data.types.translation_pin_data_iso_format034

        return {
            "IsoFormat0": capo_payment_cryptography_data.types.translation_pin_data_iso_format034.deserialize_json(
                data["IsoFormat0"]
            )
        }
    elif data.get("IsoFormat1") is not None:
        import capo_payment_cryptography_data.types.translation_pin_data_iso_format1

        return {
            "IsoFormat1": capo_payment_cryptography_data.types.translation_pin_data_iso_format1.deserialize_json(
                data["IsoFormat1"]
            )
        }
    elif data.get("IsoFormat3") is not None:
        import capo_payment_cryptography_data.types.translation_pin_data_iso_format034

        return {
            "IsoFormat3": capo_payment_cryptography_data.types.translation_pin_data_iso_format034.deserialize_json(
                data["IsoFormat3"]
            )
        }
    elif data.get("IsoFormat4") is not None:
        import capo_payment_cryptography_data.types.translation_pin_data_iso_format034

        return {
            "IsoFormat4": capo_payment_cryptography_data.types.translation_pin_data_iso_format034.deserialize_json(
                data["IsoFormat4"]
            )
        }
    elif data.get("As2805Format0") is not None:
        import capo_payment_cryptography_data.types.translation_pin_data_as2805_format0

        return {
            "As2805Format0": capo_payment_cryptography_data.types.translation_pin_data_as2805_format0.deserialize_json(
                data["As2805Format0"]
            )
        }
    else:
        name = next(
            (k for k, v in data.items() if v is not None and k != "__type"), None
        )
        if name is not None:
            return {"$unknown": {"name": name}}
        raise DeserializationError("TranslationIsoFormats: no recognized variant key")


def redact_sensitive(value: TranslationIsoFormats) -> dict[str, Any]:
    out: dict[str, Any] = dict(value)
    if "IsoFormat0" in value:
        import capo_payment_cryptography_data.types.translation_pin_data_iso_format034

        out["IsoFormat0"] = (
            capo_payment_cryptography_data.types.translation_pin_data_iso_format034.redact_sensitive(
                value["IsoFormat0"]
            )
        )
    if "IsoFormat3" in value:
        import capo_payment_cryptography_data.types.translation_pin_data_iso_format034

        out["IsoFormat3"] = (
            capo_payment_cryptography_data.types.translation_pin_data_iso_format034.redact_sensitive(
                value["IsoFormat3"]
            )
        )
    if "IsoFormat4" in value:
        import capo_payment_cryptography_data.types.translation_pin_data_iso_format034

        out["IsoFormat4"] = (
            capo_payment_cryptography_data.types.translation_pin_data_iso_format034.redact_sensitive(
                value["IsoFormat4"]
            )
        )
    if "As2805Format0" in value:
        import capo_payment_cryptography_data.types.translation_pin_data_as2805_format0

        out["As2805Format0"] = (
            capo_payment_cryptography_data.types.translation_pin_data_as2805_format0.redact_sensitive(
                value["As2805Format0"]
            )
        )
    return out
