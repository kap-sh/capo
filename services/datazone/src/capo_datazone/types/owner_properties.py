"""Generated from Smithy shape ``com.amazonaws.datazone#OwnerProperties``."""

from typing import TYPE_CHECKING, TypeAlias

from typing_extensions import TypedDict

from capo_datazone.errors import DeserializationError, SerializationError
from capo_datazone.types._unknown import UnknownUnionMember

if TYPE_CHECKING:
    import capo_datazone.types.owner_group_properties
    import capo_datazone.types.owner_user_properties


class _OwnerProperties_user(TypedDict, closed=True):
    user: "capo_datazone.types.owner_user_properties.OwnerUserProperties"


class _OwnerProperties_group(TypedDict, closed=True):
    group: "capo_datazone.types.owner_group_properties.OwnerGroupProperties"


OwnerProperties: TypeAlias = (
    _OwnerProperties_user | _OwnerProperties_group | UnknownUnionMember
)


# --- restJson1 ser/de ---
def serialize_json(value: OwnerProperties) -> dict:
    if "$unknown" in value:
        raise SerializationError(
            f"OwnerProperties: cannot serialize unknown variant {value['$unknown']['name']!r}"
        )
    elif "user" in value:
        import capo_datazone.types.owner_user_properties

        return {
            "user": capo_datazone.types.owner_user_properties.serialize_json(
                value["user"]
            )
        }
    elif "group" in value:
        import capo_datazone.types.owner_group_properties

        return {
            "group": capo_datazone.types.owner_group_properties.serialize_json(
                value["group"]
            )
        }
    else:
        raise SerializationError("OwnerProperties: no variant present")


def deserialize_json(data: dict) -> OwnerProperties:
    if data.get("user") is not None:
        import capo_datazone.types.owner_user_properties

        return {
            "user": capo_datazone.types.owner_user_properties.deserialize_json(
                data["user"]
            )
        }
    elif data.get("group") is not None:
        import capo_datazone.types.owner_group_properties

        return {
            "group": capo_datazone.types.owner_group_properties.deserialize_json(
                data["group"]
            )
        }
    else:
        name = next(
            (k for k, v in data.items() if v is not None and k != "__type"), None
        )
        if name is not None:
            return {"$unknown": {"name": name}}
        raise DeserializationError("OwnerProperties: no recognized variant key")
