"""Generated from Smithy shape ``com.amazonaws.verifiedpermissions#EntitiesDefinition``."""

from typing import TYPE_CHECKING, Any, TypeAlias

from typing_extensions import TypedDict

from capo_verifiedpermissions.errors import DeserializationError, SerializationError
from capo_verifiedpermissions.types._unknown import UnknownUnionMember

if TYPE_CHECKING:
    import capo_verifiedpermissions.types.cedar_json
    import capo_verifiedpermissions.types.entity_list


class EntitiesDefinitionEntityListMember(TypedDict, closed=True):
    entityList: "capo_verifiedpermissions.types.entity_list.EntityList"


class EntitiesDefinitionCedarJsonMember(TypedDict, closed=True):
    cedarJson: "capo_verifiedpermissions.types.cedar_json.CedarJson"


EntitiesDefinition: TypeAlias = (
    EntitiesDefinitionEntityListMember
    | EntitiesDefinitionCedarJsonMember
    | UnknownUnionMember
)


# --- awsJson1_0 ser/de ---
def serialize_aws_json_1_0(value: EntitiesDefinition) -> dict:
    if "$unknown" in value:
        raise SerializationError(
            f"EntitiesDefinition: cannot serialize unknown variant {value['$unknown']['name']!r}"
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
            return {"$unknown": {"name": name}}
        raise DeserializationError("EntitiesDefinition: no recognized variant key")


def redact_sensitive(value: EntitiesDefinition) -> dict[str, Any]:
    out: dict[str, Any] = dict(value)
    if "entityList" in value:
        import capo_verifiedpermissions.types.entity_list

        out["entityList"] = capo_verifiedpermissions.types.entity_list.redact_sensitive(
            value["entityList"]
        )
    if "cedarJson" in value:
        out["cedarJson"] = "*** Sensitive Data Redacted ***"
    return out
