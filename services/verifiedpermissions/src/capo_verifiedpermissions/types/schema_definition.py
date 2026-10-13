"""Generated from Smithy shape ``com.amazonaws.verifiedpermissions#SchemaDefinition``."""

from typing import TYPE_CHECKING, Any, TypeAlias

from typing_extensions import TypedDict

from capo_verifiedpermissions.errors import DeserializationError, SerializationError

if TYPE_CHECKING:
    import capo_verifiedpermissions.types.schema_json


class _SchemaDefinition_cedarJson(TypedDict, closed=True):
    cedarJson: "capo_verifiedpermissions.types.schema_json.SchemaJson"


SchemaDefinition: TypeAlias = _SchemaDefinition_cedarJson


# --- awsJson1_0 ser/de ---
def serialize_aws_json_1_0(value: SchemaDefinition) -> dict:
    if "cedarJson" in value:
        return {"cedarJson": value["cedarJson"]}
    else:
        raise SerializationError("SchemaDefinition: no variant present")


def deserialize_aws_json_1_0(data: dict) -> SchemaDefinition:
    if data.get("cedarJson") is not None:
        return {"cedarJson": data["cedarJson"]}
    else:
        raise DeserializationError("SchemaDefinition: no recognized variant key")


def redact_sensitive(value: SchemaDefinition) -> dict[str, Any]:
    out: dict[str, Any] = dict(value)
    if "cedarJson" in value:
        out["cedarJson"] = "*** Sensitive Data Redacted ***"
    return out
