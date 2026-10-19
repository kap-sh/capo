"""Generated from Smithy shape ``com.amazonaws.iottwinmaker#ListEntitiesFilter``."""

from typing import TYPE_CHECKING, TypeAlias

from typing_extensions import TypedDict

from capo_iottwinmaker.errors import DeserializationError, SerializationError
from capo_iottwinmaker.types._unknown import UnknownUnionMember

if TYPE_CHECKING:
    import capo_iottwinmaker.types.component_type_id
    import capo_iottwinmaker.types.parent_entity_id
    import capo_iottwinmaker.types.string


class _ListEntitiesFilter_parentEntityId(TypedDict, closed=True):
    parentEntityId: "capo_iottwinmaker.types.parent_entity_id.ParentEntityId"


class _ListEntitiesFilter_componentTypeId(TypedDict, closed=True):
    componentTypeId: "capo_iottwinmaker.types.component_type_id.ComponentTypeId"


class _ListEntitiesFilter_externalId(TypedDict, closed=True):
    externalId: "capo_iottwinmaker.types.string.String"


ListEntitiesFilter: TypeAlias = (
    _ListEntitiesFilter_parentEntityId
    | _ListEntitiesFilter_componentTypeId
    | _ListEntitiesFilter_externalId
    | UnknownUnionMember
)


# --- restJson1 ser/de ---
def serialize_json(value: ListEntitiesFilter) -> dict:
    if isinstance(value, UnknownUnionMember):
        raise SerializationError(
            f"ListEntitiesFilter: cannot serialize unknown variant {value.name!r}"
        )
    elif "parentEntityId" in value:
        return {"parentEntityId": value["parentEntityId"]}
    elif "componentTypeId" in value:
        return {"componentTypeId": value["componentTypeId"]}
    elif "externalId" in value:
        return {"externalId": value["externalId"]}
    else:
        raise SerializationError("ListEntitiesFilter: no variant present")


def deserialize_json(data: dict) -> ListEntitiesFilter:
    if data.get("parentEntityId") is not None:
        return {"parentEntityId": data["parentEntityId"]}
    elif data.get("componentTypeId") is not None:
        return {"componentTypeId": data["componentTypeId"]}
    elif data.get("externalId") is not None:
        return {"externalId": data["externalId"]}
    else:
        name = next(
            (k for k, v in data.items() if v is not None and k != "__type"), None
        )
        if name is not None:
            return UnknownUnionMember(name)
        raise DeserializationError("ListEntitiesFilter: no recognized variant key")
