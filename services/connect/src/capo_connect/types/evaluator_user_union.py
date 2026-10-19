"""Generated from Smithy shape ``com.amazonaws.connect#EvaluatorUserUnion``."""

from typing import TYPE_CHECKING, TypeAlias

from typing_extensions import TypedDict

from capo_connect.errors import DeserializationError, SerializationError
from capo_connect.types._unknown import UnknownUnionMember

if TYPE_CHECKING:
    import capo_connect.types.arn


class _EvaluatorUserUnion_ConnectUserArn(TypedDict, closed=True):
    ConnectUserArn: "capo_connect.types.arn.ARN"


EvaluatorUserUnion: TypeAlias = _EvaluatorUserUnion_ConnectUserArn | UnknownUnionMember


# --- restJson1 ser/de ---
def serialize_json(value: EvaluatorUserUnion) -> dict:
    if isinstance(value, UnknownUnionMember):
        raise SerializationError(
            f"EvaluatorUserUnion: cannot serialize unknown variant {value.name!r}"
        )
    elif "ConnectUserArn" in value:
        return {"ConnectUserArn": value["ConnectUserArn"]}
    else:
        raise SerializationError("EvaluatorUserUnion: no variant present")


def deserialize_json(data: dict) -> EvaluatorUserUnion:
    if data.get("ConnectUserArn") is not None:
        return {"ConnectUserArn": data["ConnectUserArn"]}
    else:
        name = next(
            (k for k, v in data.items() if v is not None and k != "__type"), None
        )
        if name is not None:
            return UnknownUnionMember(name)
        raise DeserializationError("EvaluatorUserUnion: no recognized variant key")
