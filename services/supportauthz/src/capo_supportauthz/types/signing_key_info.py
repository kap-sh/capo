"""Generated from Smithy shape ``com.amazonaws.supportauthz#SigningKeyInfo``."""

from typing import TYPE_CHECKING, TypeAlias

from typing_extensions import TypedDict

from capo_supportauthz.errors import DeserializationError, SerializationError

if TYPE_CHECKING:
    import capo_supportauthz.types.kms_key_arn


class _SigningKeyInfo_kmsKey(TypedDict, closed=True):
    kmsKey: "capo_supportauthz.types.kms_key_arn.KmsKeyArn"


SigningKeyInfo: TypeAlias = _SigningKeyInfo_kmsKey


# --- restJson1 ser/de ---
def serialize_json(value: SigningKeyInfo) -> dict:
    if "kmsKey" in value:
        return {"kmsKey": value["kmsKey"]}
    else:
        raise SerializationError("SigningKeyInfo: no variant present")


def deserialize_json(data: dict) -> SigningKeyInfo:
    if data.get("kmsKey") is not None:
        return {"kmsKey": data["kmsKey"]}
    else:
        raise DeserializationError("SigningKeyInfo: no recognized variant key")
