"""Generated from Smithy shape ``com.amazonaws.iottwinmaker#IotTwinMakerSourceConfigurationFilter``."""

from typing import TYPE_CHECKING, TypeAlias

from typing_extensions import TypedDict

from capo_iottwinmaker.errors import DeserializationError, SerializationError
from capo_iottwinmaker.types._unknown import UnknownUnionMember

if TYPE_CHECKING:
    import capo_iottwinmaker.types.filter_by_component_type
    import capo_iottwinmaker.types.filter_by_entity


class _IotTwinMakerSourceConfigurationFilter_filterByComponentType(
    TypedDict, closed=True
):
    filterByComponentType: (
        "capo_iottwinmaker.types.filter_by_component_type.FilterByComponentType"
    )


class _IotTwinMakerSourceConfigurationFilter_filterByEntity(TypedDict, closed=True):
    filterByEntity: "capo_iottwinmaker.types.filter_by_entity.FilterByEntity"


IotTwinMakerSourceConfigurationFilter: TypeAlias = (
    _IotTwinMakerSourceConfigurationFilter_filterByComponentType
    | _IotTwinMakerSourceConfigurationFilter_filterByEntity
    | UnknownUnionMember
)


# --- restJson1 ser/de ---
def serialize_json(value: IotTwinMakerSourceConfigurationFilter) -> dict:
    if isinstance(value, UnknownUnionMember):
        raise SerializationError(
            f"IotTwinMakerSourceConfigurationFilter: cannot serialize unknown variant {value.name!r}"
        )
    elif "filterByComponentType" in value:
        import capo_iottwinmaker.types.filter_by_component_type

        return {
            "filterByComponentType": capo_iottwinmaker.types.filter_by_component_type.serialize_json(
                value["filterByComponentType"]
            )
        }
    elif "filterByEntity" in value:
        import capo_iottwinmaker.types.filter_by_entity

        return {
            "filterByEntity": capo_iottwinmaker.types.filter_by_entity.serialize_json(
                value["filterByEntity"]
            )
        }
    else:
        raise SerializationError(
            "IotTwinMakerSourceConfigurationFilter: no variant present"
        )


def deserialize_json(data: dict) -> IotTwinMakerSourceConfigurationFilter:
    if data.get("filterByComponentType") is not None:
        import capo_iottwinmaker.types.filter_by_component_type

        return {
            "filterByComponentType": capo_iottwinmaker.types.filter_by_component_type.deserialize_json(
                data["filterByComponentType"]
            )
        }
    elif data.get("filterByEntity") is not None:
        import capo_iottwinmaker.types.filter_by_entity

        return {
            "filterByEntity": capo_iottwinmaker.types.filter_by_entity.deserialize_json(
                data["filterByEntity"]
            )
        }
    else:
        name = next(
            (k for k, v in data.items() if v is not None and k != "__type"), None
        )
        if name is not None:
            return UnknownUnionMember(name)
        raise DeserializationError(
            "IotTwinMakerSourceConfigurationFilter: no recognized variant key"
        )
