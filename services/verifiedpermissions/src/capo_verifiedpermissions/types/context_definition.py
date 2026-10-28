"""Generated from Smithy shape ``com.amazonaws.verifiedpermissions#ContextDefinition``."""

from typing import TYPE_CHECKING, Any, TypeAlias

from typing_extensions import TypedDict

from capo_verifiedpermissions.errors import DeserializationError, SerializationError
from capo_verifiedpermissions.types._unknown import UnknownUnionMember

if TYPE_CHECKING:
    import capo_verifiedpermissions.types.cedar_json
    import capo_verifiedpermissions.types.context_map


class ContextDefinitionContextMapMember(TypedDict, closed=True):
    contextMap: "capo_verifiedpermissions.types.context_map.ContextMap"


class ContextDefinitionCedarJsonMember(TypedDict, closed=True):
    cedarJson: "capo_verifiedpermissions.types.cedar_json.CedarJson"


ContextDefinition: TypeAlias = (
    ContextDefinitionContextMapMember
    | ContextDefinitionCedarJsonMember
    | UnknownUnionMember
)


# --- awsJson1_0 ser/de ---
def serialize_aws_json_1_0(value: ContextDefinition) -> dict:
    if "$unknown" in value:
        raise SerializationError(
            f"ContextDefinition: cannot serialize unknown variant {value['$unknown']['name']!r}"
        )
    elif "contextMap" in value:
        import capo_verifiedpermissions.types.context_map

        return {
            "contextMap": capo_verifiedpermissions.types.context_map.serialize_aws_json_1_0(
                value["contextMap"]
            )
        }
    elif "cedarJson" in value:
        return {"cedarJson": value["cedarJson"]}
    else:
        raise SerializationError("ContextDefinition: no variant present")


def deserialize_aws_json_1_0(data: dict) -> ContextDefinition:
    if data.get("contextMap") is not None:
        import capo_verifiedpermissions.types.context_map

        return {
            "contextMap": capo_verifiedpermissions.types.context_map.deserialize_aws_json_1_0(
                data["contextMap"]
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
        raise DeserializationError("ContextDefinition: no recognized variant key")


def redact_sensitive(value: ContextDefinition) -> dict[str, Any]:
    out: dict[str, Any] = dict(value)
    if "contextMap" in value:
        out["contextMap"] = "*** Sensitive Data Redacted ***"
    if "cedarJson" in value:
        out["cedarJson"] = "*** Sensitive Data Redacted ***"
    return out
