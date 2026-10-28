"""Generated from Smithy shape ``com.amazonaws.lambdamicrovms#CodeArtifact``."""

from typing import TYPE_CHECKING, TypeAlias

from typing_extensions import TypedDict

from capo_lambda_microvms.errors import DeserializationError, SerializationError
from capo_lambda_microvms.types._unknown import UnknownUnionMember

if TYPE_CHECKING:
    import capo_lambda_microvms.types.non_blank_string


class CodeArtifactUriMember(TypedDict, closed=True):
    uri: "capo_lambda_microvms.types.non_blank_string.NonBlankString"


CodeArtifact: TypeAlias = CodeArtifactUriMember | UnknownUnionMember


# --- restJson1 ser/de ---
def serialize_json(value: CodeArtifact) -> dict:
    if "$unknown" in value:
        raise SerializationError(
            f"CodeArtifact: cannot serialize unknown variant {value['$unknown']['name']!r}"
        )
    elif "uri" in value:
        return {"uri": value["uri"]}
    else:
        raise SerializationError("CodeArtifact: no variant present")


def deserialize_json(data: dict) -> CodeArtifact:
    if data.get("uri") is not None:
        return {"uri": data["uri"]}
    else:
        name = next(
            (k for k, v in data.items() if v is not None and k != "__type"), None
        )
        if name is not None:
            return {"$unknown": {"name": name}}
        raise DeserializationError("CodeArtifact: no recognized variant key")
