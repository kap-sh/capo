"""Generated from Smithy shape ``com.amazonaws.paymentcryptographydata#OutgoingKeyMaterial``."""

from typing import TYPE_CHECKING, TypeAlias

from typing_extensions import TypedDict

from capo_payment_cryptography_data.errors import (
    DeserializationError,
    SerializationError,
)
from capo_payment_cryptography_data.types._unknown import UnknownUnionMember

if TYPE_CHECKING:
    import capo_payment_cryptography_data.types.outgoing_tr31_key_block


class _OutgoingKeyMaterial_Tr31KeyBlock(TypedDict, closed=True):
    Tr31KeyBlock: "capo_payment_cryptography_data.types.outgoing_tr31_key_block.OutgoingTr31KeyBlock"


OutgoingKeyMaterial: TypeAlias = _OutgoingKeyMaterial_Tr31KeyBlock | UnknownUnionMember


# --- restJson1 ser/de ---
def serialize_json(value: OutgoingKeyMaterial) -> dict:
    if isinstance(value, UnknownUnionMember):
        raise SerializationError(
            f"OutgoingKeyMaterial: cannot serialize unknown variant {value.name!r}"
        )
    elif "Tr31KeyBlock" in value:
        import capo_payment_cryptography_data.types.outgoing_tr31_key_block

        return {
            "Tr31KeyBlock": capo_payment_cryptography_data.types.outgoing_tr31_key_block.serialize_json(
                value["Tr31KeyBlock"]
            )
        }
    else:
        raise SerializationError("OutgoingKeyMaterial: no variant present")


def deserialize_json(data: dict) -> OutgoingKeyMaterial:
    if data.get("Tr31KeyBlock") is not None:
        import capo_payment_cryptography_data.types.outgoing_tr31_key_block

        return {
            "Tr31KeyBlock": capo_payment_cryptography_data.types.outgoing_tr31_key_block.deserialize_json(
                data["Tr31KeyBlock"]
            )
        }
    else:
        name = next(
            (k for k, v in data.items() if v is not None and k != "__type"), None
        )
        if name is not None:
            return UnknownUnionMember(name)
        raise DeserializationError("OutgoingKeyMaterial: no recognized variant key")
