"""Generated from Smithy shape ``com.amazonaws.codegurusecurity#ResourceId``."""

from typing import TYPE_CHECKING, TypeAlias

from typing_extensions import TypedDict

from capo_codeguru_security.errors import DeserializationError, SerializationError
from capo_codeguru_security.types._unknown import UnknownUnionMember

if TYPE_CHECKING:
    import capo_codeguru_security.types.uuid


class ResourceIdCodeArtifactIdMember(TypedDict, closed=True):
    codeArtifactId: "capo_codeguru_security.types.uuid.Uuid"


ResourceId: TypeAlias = ResourceIdCodeArtifactIdMember | UnknownUnionMember


# --- restJson1 ser/de ---
def serialize_json(value: ResourceId) -> dict:
    if "$unknown" in value:
        raise SerializationError(
            f"ResourceId: cannot serialize unknown variant {value['$unknown']['name']!r}"
        )
    elif "codeArtifactId" in value:
        return {"codeArtifactId": value["codeArtifactId"]}
    else:
        raise SerializationError("ResourceId: no variant present")


def deserialize_json(data: dict) -> ResourceId:
    if data.get("codeArtifactId") is not None:
        return {"codeArtifactId": data["codeArtifactId"]}
    else:
        name = next(
            (k for k, v in data.items() if v is not None and k != "__type"), None
        )
        if name is not None:
            return {"$unknown": {"name": name}}
        raise DeserializationError("ResourceId: no recognized variant key")
