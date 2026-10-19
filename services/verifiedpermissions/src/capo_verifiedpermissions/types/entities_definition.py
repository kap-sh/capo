"""Generated from Smithy shape ``com.amazonaws.verifiedpermissions#EntitiesDefinition``."""

from typing import TYPE_CHECKING, Any, TypeAlias

from typing_extensions import TypedDict

from capo_verifiedpermissions.errors import DeserializationError, SerializationError
from capo_verifiedpermissions.types._unknown import UnknownUnionMember

if TYPE_CHECKING:
    import capo_verifiedpermissions.types.cedar_json
    import capo_verifiedpermissions.types.entity_list


class _EntitiesDefinition_entityList(TypedDict, closed=True):
    entityList: "capo_verifiedpermissions.types.entity_list.EntityList"


class _EntitiesDefinition_cedarJson(TypedDict, closed=True):
    cedarJson: "capo_verifiedpermissions.types.cedar_json.CedarJson"


EntitiesDefinition: TypeAlias = (
    _EntitiesDefinition_entityList | _EntitiesDefinition_cedarJson | UnknownUnionMember
)


# --- awsJson1_0 ser/de ---
def serialize_aws_json_1_0(value: EntitiesDefinition) -> dict:
    if isinstance(value, UnknownUnionMember):
        raise SerializationError(
            f"EntitiesDefinition: cannot serialize unknown variant {value.name!r}"
        )
    elif "entityList" in value:
        import capo_verifiedpermissions.types.entity_list

        return {
            "entityList": capo_verifiedpermissions.types.entity_list.serialize_aws_json_1_0(
                value["entityList"]
            )
        }
    elif "cedarJson" in value:
        return {"cedarJson": value["cedarJson"]}
    else:
        raise SerializationError("EntitiesDefinition: no variant present")


def deserialize_aws_json_1_0(data: dict) -> EntitiesDefinition:
    if data.get("entityList") is not None:
        import capo_verifiedpermissions.types.entity_list

        return {
            "entityList": capo_verifiedpermissions.types.entity_list.deserialize_aws_json_1_0(
                data["entityList"]
            )
        }
    elif data.get("cedarJson") is not None:
        return {"cedarJson": data["cedarJson"]}
    else:
        name = next(
            (k for k, v in data.items() if v is not None and k != "__type"), None
        )
        if name is not None:
            return UnknownUnionMember(name)
        raise DeserializationError("EntitiesDefinition: no recognized variant key")


def redact_sensitive(value: EntitiesDefinition) -> dict[str, Any] | UnknownUnionMember:
    if isinstance(value, UnknownUnionMember):
        return value
    out: dict[str, Any] = dict(value)
    if "entityList" in value:
        import capo_verifiedpermissions.types.entity_list

        out["entityList"] = capo_verifiedpermissions.types.entity_list.redact_sensitive(
            value["entityList"]
        )
    if "cedarJson" in value:
        out["cedarJson"] = "*** Sensitive Data Redacted ***"
    return out
