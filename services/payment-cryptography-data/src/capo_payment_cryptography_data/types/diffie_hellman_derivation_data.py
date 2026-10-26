"""Generated from Smithy shape ``com.amazonaws.paymentcryptographydata#DiffieHellmanDerivationData``."""

from typing import TYPE_CHECKING, TypeAlias

from typing_extensions import TypedDict

from capo_payment_cryptography_data.errors import (
    DeserializationError,
    SerializationError,
)
from capo_payment_cryptography_data.types._unknown import UnknownUnionMember

if TYPE_CHECKING:
    import capo_payment_cryptography_data.types.shared_information


class _DiffieHellmanDerivationData_SharedInformation(TypedDict, closed=True):
    SharedInformation: (
        "capo_payment_cryptography_data.types.shared_information.SharedInformation"
    )


DiffieHellmanDerivationData: TypeAlias = (
    _DiffieHellmanDerivationData_SharedInformation | UnknownUnionMember
)


# --- restJson1 ser/de ---
def serialize_json(value: DiffieHellmanDerivationData) -> dict:
    if "$unknown" in value:
        raise SerializationError(
            f"DiffieHellmanDerivationData: cannot serialize unknown variant {value['$unknown']['name']!r}"
        )
    elif "SharedInformation" in value:
        return {"SharedInformation": value["SharedInformation"]}
    else:
        raise SerializationError("DiffieHellmanDerivationData: no variant present")


def deserialize_json(data: dict) -> DiffieHellmanDerivationData:
    if data.get("SharedInformation") is not None:
        return {"SharedInformation": data["SharedInformation"]}
    else:
        name = next(
            (k for k, v in data.items() if v is not None and k != "__type"), None
        )
        if name is not None:
            return {"$unknown": {"name": name}}
        raise DeserializationError(
            "DiffieHellmanDerivationData: no recognized variant key"
        )
