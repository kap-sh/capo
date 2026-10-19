"""Generated from Smithy shape ``com.amazonaws.supportauthz#SigningKeyInfo``."""

from typing import TYPE_CHECKING, TypeAlias

from typing_extensions import TypedDict

from capo_supportauthz.errors import DeserializationError, SerializationError
from capo_supportauthz.types._unknown import UnknownUnionMember

if TYPE_CHECKING:
    import capo_supportauthz.types.kms_key_arn


class _SigningKeyInfo_kmsKey(TypedDict, closed=True):
    kmsKey: "capo_supportauthz.types.kms_key_arn.KmsKeyArn"


SigningKeyInfo: TypeAlias = _SigningKeyInfo_kmsKey | UnknownUnionMember


# --- restJson1 ser/de ---
def serialize_json(value: SigningKeyInfo) -> dict:
    if isinstance(value, UnknownUnionMember):
        raise SerializationError(
            f"SigningKeyInfo: cannot serialize unknown variant {value.name!r}"
        )
    elif "kmsKey" in value:
        return {"kmsKey": value["kmsKey"]}
    else:
        raise SerializationError("SigningKeyInfo: no variant present")


def deserialize_json(data: dict) -> SigningKeyInfo:
    if data.get("kmsKey") is not None:
        return {"kmsKey": data["kmsKey"]}
    else:
        name = next(
            (k for k, v in data.items() if v is not None and k != "__type"), None
        )
        if name is not None:
            return UnknownUnionMember(name)
        raise DeserializationError("SigningKeyInfo: no recognized variant key")
