"""Generated from Smithy shape ``com.amazonaws.iottwinmaker#SyncResourceFilter``."""

from typing import TYPE_CHECKING, TypeAlias

from typing_extensions import TypedDict

from capo_iottwinmaker.errors import DeserializationError, SerializationError
from capo_iottwinmaker.types._unknown import UnknownUnionMember

if TYPE_CHECKING:
    import capo_iottwinmaker.types.id
    import capo_iottwinmaker.types.sync_resource_state
    import capo_iottwinmaker.types.sync_resource_type


class SyncResourceFilterStateMember(TypedDict, closed=True):
    state: "capo_iottwinmaker.types.sync_resource_state.SyncResourceState"


class SyncResourceFilterResourceTypeMember(TypedDict, closed=True):
    resourceType: "capo_iottwinmaker.types.sync_resource_type.SyncResourceType"


class SyncResourceFilterResourceIdMember(TypedDict, closed=True):
    resourceId: "capo_iottwinmaker.types.id.Id"


class SyncResourceFilterExternalIdMember(TypedDict, closed=True):
    externalId: "capo_iottwinmaker.types.id.Id"


SyncResourceFilter: TypeAlias = (
    SyncResourceFilterStateMember
    | SyncResourceFilterResourceTypeMember
    | SyncResourceFilterResourceIdMember
    | SyncResourceFilterExternalIdMember
    | UnknownUnionMember
)


# --- restJson1 ser/de ---
def serialize_json(value: SyncResourceFilter) -> dict:
    if "$unknown" in value:
        raise SerializationError(
            f"SyncResourceFilter: cannot serialize unknown variant {value['$unknown']['name']!r}"
        )
    elif "state" in value:
        return {"state": value["state"]}
    elif "resourceType" in value:
        return {"resourceType": value["resourceType"]}
    elif "resourceId" in value:
        return {"resourceId": value["resourceId"]}
    elif "externalId" in value:
        return {"externalId": value["externalId"]}
    else:
        raise SerializationError("SyncResourceFilter: no variant present")


def deserialize_json(data: dict) -> SyncResourceFilter:
    if data.get("state") is not None:
        return {"state": data["state"]}
    elif data.get("resourceType") is not None:
        return {"resourceType": data["resourceType"]}
    elif data.get("resourceId") is not None:
        return {"resourceId": data["resourceId"]}
    elif data.get("externalId") is not None:
        return {"externalId": data["externalId"]}
    else:
        name = next(
            (k for k, v in data.items() if v is not None and k != "__type"), None
        )
        if name is not None:
            return {"$unknown": {"name": name}}
        raise DeserializationError("SyncResourceFilter: no recognized variant key")
