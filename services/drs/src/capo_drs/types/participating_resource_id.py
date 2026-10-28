"""Generated from Smithy shape ``com.amazonaws.drs#ParticipatingResourceID``."""

from typing import TYPE_CHECKING, TypeAlias

from typing_extensions import TypedDict

from capo_drs.errors import DeserializationError, SerializationError
from capo_drs.types._unknown import UnknownUnionMember

if TYPE_CHECKING:
    import capo_drs.types.source_network_id


class ParticipatingResourceIDSourceNetworkIDMember(TypedDict, closed=True):
    sourceNetworkID: "capo_drs.types.source_network_id.SourceNetworkID"


ParticipatingResourceID: TypeAlias = (
    ParticipatingResourceIDSourceNetworkIDMember | UnknownUnionMember
)


# --- restJson1 ser/de ---
def serialize_json(value: ParticipatingResourceID) -> dict:
    if "$unknown" in value:
        raise SerializationError(
            f"ParticipatingResourceID: cannot serialize unknown variant {value['$unknown']['name']!r}"
        )
    elif "sourceNetworkID" in value:
        return {"sourceNetworkID": value["sourceNetworkID"]}
    else:
        raise SerializationError("ParticipatingResourceID: no variant present")


def deserialize_json(data: dict) -> ParticipatingResourceID:
    if data.get("sourceNetworkID") is not None:
        return {"sourceNetworkID": data["sourceNetworkID"]}
    else:
        name = next(
            (k for k, v in data.items() if v is not None and k != "__type"), None
        )
        if name is not None:
            return {"$unknown": {"name": name}}
        raise DeserializationError("ParticipatingResourceID: no recognized variant key")
