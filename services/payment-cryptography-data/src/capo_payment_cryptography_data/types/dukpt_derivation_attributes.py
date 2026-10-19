"""Generated from Smithy shape ``com.amazonaws.paymentcryptographydata#DukptDerivationAttributes``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_payment_cryptography_data.types.dukpt_derivation_type
    import capo_payment_cryptography_data.types.dukpt_key_variant
    import capo_payment_cryptography_data.types.hex_length16_or20_or24


class DukptDerivationAttributes(TypedDict, closed=True):
    key_serial_number: "capo_payment_cryptography_data.types.hex_length16_or20_or24.HexLength16Or20Or24"
    """<p>The unique identifier known as Key Serial Number (KSN) that comes from an encrypting device using DUKPT encryption method. The KSN is derived from the encrypting device unique identifier and an internal transaction counter.</p>"""
    dukpt_key_derivation_type: NotRequired[
        "capo_payment_cryptography_data.types.dukpt_derivation_type.DukptDerivationType"
    ]
    """<p>The key type derived using DUKPT from a Base Derivation Key (BDK) and Key Serial Number (KSN). This must be less than or equal to the strength of the BDK. For example, you can't use <code>AES_128</code> as a derivation type for a BDK of <code>AES_128</code> or <code>TDES_2KEY</code> </p>"""
    dukpt_key_variant: NotRequired[
        "capo_payment_cryptography_data.types.dukpt_key_variant.DukptKeyVariant"
    ]
    """<p>The type of use of DUKPT, which can be for incoming data decryption, outgoing data encryption, or both.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: DukptDerivationAttributes) -> dict:
    out: dict = {}
    out["KeySerialNumber"] = value["key_serial_number"]
    if "dukpt_key_derivation_type" in value:
        import capo_payment_cryptography_data.types.dukpt_derivation_type

        out["DukptKeyDerivationType"] = (
            capo_payment_cryptography_data.types.dukpt_derivation_type.serialize_json(
                value["dukpt_key_derivation_type"]
            )
        )
    if "dukpt_key_variant" in value:
        import capo_payment_cryptography_data.types.dukpt_key_variant

        out["DukptKeyVariant"] = (
            capo_payment_cryptography_data.types.dukpt_key_variant.serialize_json(
                value["dukpt_key_variant"]
            )
        )
    return out


def deserialize_json(data: dict) -> DukptDerivationAttributes:
    out: DukptDerivationAttributes = {}  # type: ignore[typeddict-item]
    if data.get("KeySerialNumber") is not None:
        out["key_serial_number"] = data["KeySerialNumber"]
    else:
        out["key_serial_number"] = ""
    if data.get("DukptKeyDerivationType") is not None:
        import capo_payment_cryptography_data.types.dukpt_derivation_type

        out["dukpt_key_derivation_type"] = (
            capo_payment_cryptography_data.types.dukpt_derivation_type.deserialize_json(
                data["DukptKeyDerivationType"]
            )
        )
    if data.get("DukptKeyVariant") is not None:
        import capo_payment_cryptography_data.types.dukpt_key_variant

        out["dukpt_key_variant"] = (
            capo_payment_cryptography_data.types.dukpt_key_variant.deserialize_json(
                data["DukptKeyVariant"]
            )
        )
    return out
