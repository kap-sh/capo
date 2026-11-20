"""Generated from Smithy shape ``com.amazonaws.connectscheduling#ActorInfo``."""

from typing import TYPE_CHECKING, TypeAlias

from typing_extensions import TypedDict

from capo_connectscheduling.errors import DeserializationError, SerializationError
from capo_connectscheduling.types._unknown import UnknownUnionMember

if TYPE_CHECKING:
    import capo_connectscheduling.types.arn


class ActorInfoConnectUserArnMember(TypedDict, closed=True):
    ConnectUserArn: "capo_connectscheduling.types.arn.ARN"


class ActorInfoAWSIdentityArnMember(TypedDict, closed=True):
    AWSIdentityArn: "capo_connectscheduling.types.arn.ARN"


ActorInfo: TypeAlias = (
    ActorInfoConnectUserArnMember | ActorInfoAWSIdentityArnMember | UnknownUnionMember
)


# --- restJson1 ser/de ---
def serialize_json(value: ActorInfo) -> dict:
    if "$unknown" in value:
        raise SerializationError(
            f"ActorInfo: cannot serialize unknown variant {value['$unknown']['name']!r}"
        )
    elif "ConnectUserArn" in value:
        return {"ConnectUserArn": value["ConnectUserArn"]}
    elif "AWSIdentityArn" in value:
        return {"AWSIdentityArn": value["AWSIdentityArn"]}
    else:
        raise SerializationError("ActorInfo: no variant present")


def deserialize_json(data: dict) -> ActorInfo:
    if data.get("ConnectUserArn") is not None:
        return {"ConnectUserArn": data["ConnectUserArn"]}
    elif data.get("AWSIdentityArn") is not None:
        return {"AWSIdentityArn": data["AWSIdentityArn"]}
    else:
        name = next(
            (k for k, v in data.items() if v is not None and k != "__type"), None
        )
        if name is not None:
            return {"$unknown": {"name": name}}
        raise DeserializationError("ActorInfo: no recognized variant key")
