"""Generated from Smithy shape ``com.amazonaws.iottwinmaker#ListComponentTypesFilter``."""

from typing import TYPE_CHECKING, TypeAlias

from typing_extensions import TypedDict

from capo_iottwinmaker.errors import DeserializationError, SerializationError
from capo_iottwinmaker.types._unknown import UnknownUnionMember

if TYPE_CHECKING:
    import capo_iottwinmaker.types.boolean
    import capo_iottwinmaker.types.component_type_id
    import capo_iottwinmaker.types.string


class ListComponentTypesFilterExtendsFromMember(TypedDict, closed=True):
    extendsFrom: "capo_iottwinmaker.types.component_type_id.ComponentTypeId"


class ListComponentTypesFilterNamespaceMember(TypedDict, closed=True):
    namespace: "capo_iottwinmaker.types.string.String"


class ListComponentTypesFilterIsAbstractMember(TypedDict, closed=True):
    isAbstract: "capo_iottwinmaker.types.boolean.Boolean"


ListComponentTypesFilter: TypeAlias = (
    ListComponentTypesFilterExtendsFromMember
    | ListComponentTypesFilterNamespaceMember
    | ListComponentTypesFilterIsAbstractMember
    | UnknownUnionMember
)


# --- restJson1 ser/de ---
def serialize_json(value: ListComponentTypesFilter) -> dict:
    if "$unknown" in value:
        raise SerializationError(
            f"ListComponentTypesFilter: cannot serialize unknown variant {value['$unknown']['name']!r}"
        )
    elif "extendsFrom" in value:
        return {"extendsFrom": value["extendsFrom"]}
    elif "namespace" in value:
        return {"namespace": value["namespace"]}
    elif "isAbstract" in value:
        return {"isAbstract": value["isAbstract"]}
    else:
        raise SerializationError("ListComponentTypesFilter: no variant present")


def deserialize_json(data: dict) -> ListComponentTypesFilter:
    if data.get("extendsFrom") is not None:
        return {"extendsFrom": data["extendsFrom"]}
    elif data.get("namespace") is not None:
        return {"namespace": data["namespace"]}
    elif data.get("isAbstract") is not None:
        return {"isAbstract": data["isAbstract"]}
    else:
        name = next(
            (k for k, v in data.items() if v is not None and k != "__type"), None
        )
        if name is not None:
            return {"$unknown": {"name": name}}
        raise DeserializationError(
            "ListComponentTypesFilter: no recognized variant key"
        )
