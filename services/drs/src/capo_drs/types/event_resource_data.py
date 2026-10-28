"""Generated from Smithy shape ``com.amazonaws.drs#EventResourceData``."""

from typing import TYPE_CHECKING, TypeAlias

from typing_extensions import TypedDict

from capo_drs.errors import DeserializationError, SerializationError
from capo_drs.types._unknown import UnknownUnionMember

if TYPE_CHECKING:
    import capo_drs.types.source_network_data


class EventResourceDataSourceNetworkDataMember(TypedDict, closed=True):
    sourceNetworkData: "capo_drs.types.source_network_data.SourceNetworkData"


EventResourceData: TypeAlias = (
    EventResourceDataSourceNetworkDataMember | UnknownUnionMember
)


# --- restJson1 ser/de ---
def serialize_json(value: EventResourceData) -> dict:
    if "$unknown" in value:
        raise SerializationError(
            f"EventResourceData: cannot serialize unknown variant {value['$unknown']['name']!r}"
        )
    elif "sourceNetworkData" in value:
        import capo_drs.types.source_network_data

        return {
            "sourceNetworkData": capo_drs.types.source_network_data.serialize_json(
                value["sourceNetworkData"]
            )
        }
    else:
        raise SerializationError("EventResourceData: no variant present")


def deserialize_json(data: dict) -> EventResourceData:
    if data.get("sourceNetworkData") is not None:
        import capo_drs.types.source_network_data

        return {
            "sourceNetworkData": capo_drs.types.source_network_data.deserialize_json(
                data["sourceNetworkData"]
            )
        }
    else:
        name = next(
            (k for k, v in data.items() if v is not None and k != "__type"), None
        )
        if name is not None:
            return {"$unknown": {"name": name}}
        raise DeserializationError("EventResourceData: no recognized variant key")
