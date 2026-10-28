"""Generated from Smithy shape ``com.amazonaws.groundstation#KmsKey``."""

from typing import TYPE_CHECKING, TypeAlias

from typing_extensions import TypedDict

from capo_groundstation.errors import DeserializationError, SerializationError
from capo_groundstation.types._unknown import UnknownUnionMember

if TYPE_CHECKING:
    import capo_groundstation.types.key_alias_arn
    import capo_groundstation.types.key_alias_name
    import capo_groundstation.types.key_arn


class KmsKeyKmsKeyArnMember(TypedDict, closed=True):
    kmsKeyArn: "capo_groundstation.types.key_arn.KeyArn"


class KmsKeyKmsAliasArnMember(TypedDict, closed=True):
    kmsAliasArn: "capo_groundstation.types.key_alias_arn.KeyAliasArn"


class KmsKeyKmsAliasNameMember(TypedDict, closed=True):
    kmsAliasName: "capo_groundstation.types.key_alias_name.KeyAliasName"


KmsKey: TypeAlias = (
    KmsKeyKmsKeyArnMember
    | KmsKeyKmsAliasArnMember
    | KmsKeyKmsAliasNameMember
    | UnknownUnionMember
)


# --- restJson1 ser/de ---
def serialize_json(value: KmsKey) -> dict:
    if "$unknown" in value:
        raise SerializationError(
            f"KmsKey: cannot serialize unknown variant {value['$unknown']['name']!r}"
        )
    elif "kmsKeyArn" in value:
        return {"kmsKeyArn": value["kmsKeyArn"]}
    elif "kmsAliasArn" in value:
        return {"kmsAliasArn": value["kmsAliasArn"]}
    elif "kmsAliasName" in value:
        return {"kmsAliasName": value["kmsAliasName"]}
    else:
        raise SerializationError("KmsKey: no variant present")


def deserialize_json(data: dict) -> KmsKey:
    if data.get("kmsKeyArn") is not None:
        return {"kmsKeyArn": data["kmsKeyArn"]}
    elif data.get("kmsAliasArn") is not None:
        return {"kmsAliasArn": data["kmsAliasArn"]}
    elif data.get("kmsAliasName") is not None:
        return {"kmsAliasName": data["kmsAliasName"]}
    else:
        name = next(
            (k for k, v in data.items() if v is not None and k != "__type"), None
        )
        if name is not None:
            return {"$unknown": {"name": name}}
        raise DeserializationError("KmsKey: no recognized variant key")
