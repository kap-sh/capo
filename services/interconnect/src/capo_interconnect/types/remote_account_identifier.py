"""Generated from Smithy shape ``com.amazonaws.interconnect#RemoteAccountIdentifier``."""

from typing import TYPE_CHECKING, TypeAlias

from typing_extensions import TypedDict

from capo_interconnect.errors import DeserializationError, SerializationError
from capo_interconnect.types._unknown import UnknownUnionMember

if TYPE_CHECKING:
    import capo_interconnect.types.remote_owner_account


class _RemoteAccountIdentifier_identifier(TypedDict, closed=True):
    identifier: "capo_interconnect.types.remote_owner_account.RemoteOwnerAccount"


RemoteAccountIdentifier: TypeAlias = (
    _RemoteAccountIdentifier_identifier | UnknownUnionMember
)


# --- awsJson1_0 ser/de ---
def serialize_aws_json_1_0(value: RemoteAccountIdentifier) -> dict:
    if "$unknown" in value:
        raise SerializationError(
            f"RemoteAccountIdentifier: cannot serialize unknown variant {value['$unknown']['name']!r}"
        )
    elif "identifier" in value:
        return {"identifier": value["identifier"]}
    else:
        raise SerializationError("RemoteAccountIdentifier: no variant present")


def deserialize_aws_json_1_0(data: dict) -> RemoteAccountIdentifier:
    if data.get("identifier") is not None:
        return {"identifier": data["identifier"]}
    else:
        name = next(
            (k for k, v in data.items() if v is not None and k != "__type"), None
        )
        if name is not None:
            return {"$unknown": {"name": name}}
        raise DeserializationError("RemoteAccountIdentifier: no recognized variant key")
