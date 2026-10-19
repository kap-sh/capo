"""Generated from Smithy shape ``com.amazonaws.paymentcryptographydata#WrappedKeyMaterial``."""

from typing import TYPE_CHECKING, Any, TypeAlias

from typing_extensions import TypedDict

from capo_payment_cryptography_data.errors import (
    DeserializationError,
    SerializationError,
)
from capo_payment_cryptography_data.types._unknown import UnknownUnionMember

if TYPE_CHECKING:
    import capo_payment_cryptography_data.types.ecdh_derivation_attributes
    import capo_payment_cryptography_data.types.tr31_wrapped_key_block


class _WrappedKeyMaterial_Tr31KeyBlock(TypedDict, closed=True):
    Tr31KeyBlock: "capo_payment_cryptography_data.types.tr31_wrapped_key_block.Tr31WrappedKeyBlock"


class _WrappedKeyMaterial_DiffieHellmanSymmetricKey(TypedDict, closed=True):
    DiffieHellmanSymmetricKey: "capo_payment_cryptography_data.types.ecdh_derivation_attributes.EcdhDerivationAttributes"


WrappedKeyMaterial: TypeAlias = (
    _WrappedKeyMaterial_Tr31KeyBlock
    | _WrappedKeyMaterial_DiffieHellmanSymmetricKey
    | UnknownUnionMember
)


# --- restJson1 ser/de ---
def serialize_json(value: WrappedKeyMaterial) -> dict:
    if isinstance(value, UnknownUnionMember):
        raise SerializationError(
            f"WrappedKeyMaterial: cannot serialize unknown variant {value.name!r}"
        )
    elif "Tr31KeyBlock" in value:
        return {"Tr31KeyBlock": value["Tr31KeyBlock"]}
    elif "DiffieHellmanSymmetricKey" in value:
        import capo_payment_cryptography_data.types.ecdh_derivation_attributes

        return {
            "DiffieHellmanSymmetricKey": capo_payment_cryptography_data.types.ecdh_derivation_attributes.serialize_json(
                value["DiffieHellmanSymmetricKey"]
            )
        }
    else:
        raise SerializationError("WrappedKeyMaterial: no variant present")


def deserialize_json(data: dict) -> WrappedKeyMaterial:
    if data.get("Tr31KeyBlock") is not None:
        return {"Tr31KeyBlock": data["Tr31KeyBlock"]}
    elif data.get("DiffieHellmanSymmetricKey") is not None:
        import capo_payment_cryptography_data.types.ecdh_derivation_attributes

        return {
            "DiffieHellmanSymmetricKey": capo_payment_cryptography_data.types.ecdh_derivation_attributes.deserialize_json(
                data["DiffieHellmanSymmetricKey"]
            )
        }
    else:
        name = next(
            (k for k, v in data.items() if v is not None and k != "__type"), None
        )
        if name is not None:
            return UnknownUnionMember(name)
        raise DeserializationError("WrappedKeyMaterial: no recognized variant key")


def redact_sensitive(value: WrappedKeyMaterial) -> dict[str, Any] | UnknownUnionMember:
    if isinstance(value, UnknownUnionMember):
        return value
    out: dict[str, Any] = dict(value)
    if "Tr31KeyBlock" in value:
        out["Tr31KeyBlock"] = "*** Sensitive Data Redacted ***"
    return out
