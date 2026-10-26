"""Generated from Smithy shape ``com.amazonaws.workspacesweb#EventFilter``."""

from typing import TYPE_CHECKING, TypeAlias

from typing_extensions import TypedDict

from capo_workspaces_web.errors import DeserializationError, SerializationError
from capo_workspaces_web.types._unknown import UnknownUnionMember

if TYPE_CHECKING:
    import capo_workspaces_web.types.events


class _EventFilter_all(TypedDict, closed=True):
    all: "None"


class _EventFilter_include(TypedDict, closed=True):
    include: "capo_workspaces_web.types.events.Events"


EventFilter: TypeAlias = _EventFilter_all | _EventFilter_include | UnknownUnionMember


# --- restJson1 ser/de ---
def serialize_json(value: EventFilter) -> dict:
    if "$unknown" in value:
        raise SerializationError(
            f"EventFilter: cannot serialize unknown variant {value['$unknown']['name']!r}"
        )
    elif "all" in value:
        return {"all": {}}
    elif "include" in value:
        import capo_workspaces_web.types.events

        return {
            "include": capo_workspaces_web.types.events.serialize_json(value["include"])
        }
    else:
        raise SerializationError("EventFilter: no variant present")


def deserialize_json(data: dict) -> EventFilter:
    if data.get("all") is not None:
        return {"all": None}
    elif data.get("include") is not None:
        import capo_workspaces_web.types.events

        return {
            "include": capo_workspaces_web.types.events.deserialize_json(
                data["include"]
            )
        }
    else:
        name = next(
            (k for k, v in data.items() if v is not None and k != "__type"), None
        )
        if name is not None:
            return {"$unknown": {"name": name}}
        raise DeserializationError("EventFilter: no recognized variant key")
