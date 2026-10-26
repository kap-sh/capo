"""Generated from Smithy shape ``com.amazonaws.deadline#SessionsStatisticsResources``."""

from typing import TYPE_CHECKING, TypeAlias

from typing_extensions import TypedDict

from capo_deadline.errors import DeserializationError, SerializationError
from capo_deadline.types._unknown import UnknownUnionMember

if TYPE_CHECKING:
    import capo_deadline.types.fleet_ids
    import capo_deadline.types.queue_ids


class _SessionsStatisticsResources_queueIds(TypedDict, closed=True):
    queueIds: "capo_deadline.types.queue_ids.QueueIds"


class _SessionsStatisticsResources_fleetIds(TypedDict, closed=True):
    fleetIds: "capo_deadline.types.fleet_ids.FleetIds"


SessionsStatisticsResources: TypeAlias = (
    _SessionsStatisticsResources_queueIds
    | _SessionsStatisticsResources_fleetIds
    | UnknownUnionMember
)


# --- restJson1 ser/de ---
def serialize_json(value: SessionsStatisticsResources) -> dict:
    if "$unknown" in value:
        raise SerializationError(
            f"SessionsStatisticsResources: cannot serialize unknown variant {value['$unknown']['name']!r}"
        )
    elif "queueIds" in value:
        import capo_deadline.types.queue_ids

        return {
            "queueIds": capo_deadline.types.queue_ids.serialize_json(value["queueIds"])
        }
    elif "fleetIds" in value:
        import capo_deadline.types.fleet_ids

        return {
            "fleetIds": capo_deadline.types.fleet_ids.serialize_json(value["fleetIds"])
        }
    else:
        raise SerializationError("SessionsStatisticsResources: no variant present")


def deserialize_json(data: dict) -> SessionsStatisticsResources:
    if data.get("queueIds") is not None:
        import capo_deadline.types.queue_ids

        return {
            "queueIds": capo_deadline.types.queue_ids.deserialize_json(data["queueIds"])
        }
    elif data.get("fleetIds") is not None:
        import capo_deadline.types.fleet_ids

        return {
            "fleetIds": capo_deadline.types.fleet_ids.deserialize_json(data["fleetIds"])
        }
    else:
        name = next(
            (k for k, v in data.items() if v is not None and k != "__type"), None
        )
        if name is not None:
            return {"$unknown": {"name": name}}
        raise DeserializationError(
            "SessionsStatisticsResources: no recognized variant key"
        )
