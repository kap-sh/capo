"""Generated from Smithy shape ``com.amazonaws.datazone#OwnerPropertiesOutput``."""

from typing import TYPE_CHECKING, TypeAlias

from typing_extensions import TypedDict

from capo_datazone.errors import DeserializationError, SerializationError
from capo_datazone.types._unknown import UnknownUnionMember

if TYPE_CHECKING:
    import capo_datazone.types.owner_group_properties_output
    import capo_datazone.types.owner_user_properties_output


class _OwnerPropertiesOutput_user(TypedDict, closed=True):
    user: "capo_datazone.types.owner_user_properties_output.OwnerUserPropertiesOutput"


class _OwnerPropertiesOutput_group(TypedDict, closed=True):
    group: (
        "capo_datazone.types.owner_group_properties_output.OwnerGroupPropertiesOutput"
    )


OwnerPropertiesOutput: TypeAlias = (
    _OwnerPropertiesOutput_user | _OwnerPropertiesOutput_group | UnknownUnionMember
)


# --- restJson1 ser/de ---
def serialize_json(value: OwnerPropertiesOutput) -> dict:
    if isinstance(value, UnknownUnionMember):
        raise SerializationError(
            f"OwnerPropertiesOutput: cannot serialize unknown variant {value.name!r}"
        )
    elif "user" in value:
        import capo_datazone.types.owner_user_properties_output

        return {
            "user": capo_datazone.types.owner_user_properties_output.serialize_json(
                value["user"]
            )
        }
    elif "group" in value:
        import capo_datazone.types.owner_group_properties_output

        return {
            "group": capo_datazone.types.owner_group_properties_output.serialize_json(
                value["group"]
            )
        }
    else:
        raise SerializationError("OwnerPropertiesOutput: no variant present")


def deserialize_json(data: dict) -> OwnerPropertiesOutput:
    if data.get("user") is not None:
        import capo_datazone.types.owner_user_properties_output

        return {
            "user": capo_datazone.types.owner_user_properties_output.deserialize_json(
                data["user"]
            )
        }
    elif data.get("group") is not None:
        import capo_datazone.types.owner_group_properties_output

        return {
            "group": capo_datazone.types.owner_group_properties_output.deserialize_json(
                data["group"]
            )
        }
    else:
        name = next(
            (k for k, v in data.items() if v is not None and k != "__type"), None
        )
        if name is not None:
            return UnknownUnionMember(name)
        raise DeserializationError("OwnerPropertiesOutput: no recognized variant key")
