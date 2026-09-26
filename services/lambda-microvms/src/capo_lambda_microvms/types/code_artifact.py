"""Generated from Smithy shape ``com.amazonaws.lambdamicrovms#CodeArtifact``."""

from typing import TYPE_CHECKING, TypeAlias

from typing_extensions import TypedDict

from capo_lambda_microvms.errors import DeserializationError, SerializationError

if TYPE_CHECKING:
    import capo_lambda_microvms.types.non_blank_string


class _CodeArtifact_uri(TypedDict, closed=True):
    uri: "capo_lambda_microvms.types.non_blank_string.NonBlankString"


CodeArtifact: TypeAlias = _CodeArtifact_uri


# --- restJson1 ser/de ---
def serialize_json(value: CodeArtifact) -> dict:
    if "uri" in value:
        return {"uri": value["uri"]}
    else:
        raise SerializationError("CodeArtifact: no variant present")


def deserialize_json(data: dict) -> CodeArtifact:
    if data.get("uri") is not None:
        return {"uri": data["uri"]}
    else:
        raise DeserializationError("CodeArtifact: no recognized variant key")
