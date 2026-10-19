"""Generated from Smithy shape ``com.amazonaws.connect#CreatedByInfo``."""

from typing import TYPE_CHECKING, TypeAlias

from typing_extensions import TypedDict

from capo_connect.errors import DeserializationError, SerializationError
from capo_connect.types._unknown import UnknownUnionMember

if TYPE_CHECKING:
    import capo_connect.types.arn


class _CreatedByInfo_ConnectUserArn(TypedDict, closed=True):
    ConnectUserArn: "capo_connect.types.arn.ARN"


class _CreatedByInfo_AWSIdentityArn(TypedDict, closed=True):
    AWSIdentityArn: "capo_connect.types.arn.ARN"


CreatedByInfo: TypeAlias = (
    _CreatedByInfo_ConnectUserArn | _CreatedByInfo_AWSIdentityArn | UnknownUnionMember
)


# --- restJson1 ser/de ---
def serialize_json(value: CreatedByInfo) -> dict:
    if isinstance(value, UnknownUnionMember):
        raise SerializationError(
            f"CreatedByInfo: cannot serialize unknown variant {value.name!r}"
        )
    elif "ConnectUserArn" in value:
        return {"ConnectUserArn": value["ConnectUserArn"]}
    elif "AWSIdentityArn" in value:
        return {"AWSIdentityArn": value["AWSIdentityArn"]}
    else:
        raise SerializationError("CreatedByInfo: no variant present")


def deserialize_json(data: dict) -> CreatedByInfo:
    if data.get("ConnectUserArn") is not None:
        return {"ConnectUserArn": data["ConnectUserArn"]}
    elif data.get("AWSIdentityArn") is not None:
        return {"AWSIdentityArn": data["AWSIdentityArn"]}
    else:
        name = next(
            (k for k, v in data.items() if v is not None and k != "__type"), None
        )
        if name is not None:
            return UnknownUnionMember(name)
        raise DeserializationError("CreatedByInfo: no recognized variant key")
