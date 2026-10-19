"""Generated from Smithy shape ``com.amazonaws.paymentcryptographydata#IncomingKeyMaterial``."""

from typing import TYPE_CHECKING, Any, TypeAlias

from typing_extensions import TypedDict

from capo_payment_cryptography_data.errors import (
    DeserializationError,
    SerializationError,
)
from capo_payment_cryptography_data.types._unknown import UnknownUnionMember

if TYPE_CHECKING:
    import capo_payment_cryptography_data.types.incoming_diffie_hellman_tr31_key_block


class _IncomingKeyMaterial_DiffieHellmanTr31KeyBlock(TypedDict, closed=True):
    DiffieHellmanTr31KeyBlock: "capo_payment_cryptography_data.types.incoming_diffie_hellman_tr31_key_block.IncomingDiffieHellmanTr31KeyBlock"


IncomingKeyMaterial: TypeAlias = (
    _IncomingKeyMaterial_DiffieHellmanTr31KeyBlock | UnknownUnionMember
)


# --- restJson1 ser/de ---
def serialize_json(value: IncomingKeyMaterial) -> dict:
    if isinstance(value, UnknownUnionMember):
        raise SerializationError(
            f"IncomingKeyMaterial: cannot serialize unknown variant {value.name!r}"
        )
    elif "DiffieHellmanTr31KeyBlock" in value:
        import capo_payment_cryptography_data.types.incoming_diffie_hellman_tr31_key_block

        return {
            "DiffieHellmanTr31KeyBlock": capo_payment_cryptography_data.types.incoming_diffie_hellman_tr31_key_block.serialize_json(
                value["DiffieHellmanTr31KeyBlock"]
            )
        }
    else:
        raise SerializationError("IncomingKeyMaterial: no variant present")


def deserialize_json(data: dict) -> IncomingKeyMaterial:
    if data.get("DiffieHellmanTr31KeyBlock") is not None:
        import capo_payment_cryptography_data.types.incoming_diffie_hellman_tr31_key_block

        return {
            "DiffieHellmanTr31KeyBlock": capo_payment_cryptography_data.types.incoming_diffie_hellman_tr31_key_block.deserialize_json(
                data["DiffieHellmanTr31KeyBlock"]
            )
        }
    else:
        name = next(
            (k for k, v in data.items() if v is not None and k != "__type"), None
        )
        if name is not None:
            return UnknownUnionMember(name)
        raise DeserializationError("IncomingKeyMaterial: no recognized variant key")


def redact_sensitive(value: IncomingKeyMaterial) -> dict[str, Any] | UnknownUnionMember:
    if isinstance(value, UnknownUnionMember):
        return value
    out: dict[str, Any] = dict(value)
    if "DiffieHellmanTr31KeyBlock" in value:
        import capo_payment_cryptography_data.types.incoming_diffie_hellman_tr31_key_block

        out["DiffieHellmanTr31KeyBlock"] = (
            capo_payment_cryptography_data.types.incoming_diffie_hellman_tr31_key_block.redact_sensitive(
                value["DiffieHellmanTr31KeyBlock"]
            )
        )
    return out
