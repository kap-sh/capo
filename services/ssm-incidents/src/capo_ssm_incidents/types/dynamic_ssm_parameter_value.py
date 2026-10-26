"""Generated from Smithy shape ``com.amazonaws.ssmincidents#DynamicSsmParameterValue``."""

from typing import TYPE_CHECKING, TypeAlias

from typing_extensions import TypedDict

from capo_ssm_incidents.errors import DeserializationError, SerializationError
from capo_ssm_incidents.types._unknown import UnknownUnionMember

if TYPE_CHECKING:
    import capo_ssm_incidents.types.variable_type


class _DynamicSsmParameterValue_variable(TypedDict, closed=True):
    variable: "capo_ssm_incidents.types.variable_type.VariableType"


DynamicSsmParameterValue: TypeAlias = (
    _DynamicSsmParameterValue_variable | UnknownUnionMember
)


# --- restJson1 ser/de ---
def serialize_json(value: DynamicSsmParameterValue) -> dict:
    if "$unknown" in value:
        raise SerializationError(
            f"DynamicSsmParameterValue: cannot serialize unknown variant {value['$unknown']['name']!r}"
        )
    elif "variable" in value:
        return {"variable": value["variable"]}
    else:
        raise SerializationError("DynamicSsmParameterValue: no variant present")


def deserialize_json(data: dict) -> DynamicSsmParameterValue:
    if data.get("variable") is not None:
        return {"variable": data["variable"]}
    else:
        name = next(
            (k for k, v in data.items() if v is not None and k != "__type"), None
        )
        if name is not None:
            return {"$unknown": {"name": name}}
        raise DeserializationError(
            "DynamicSsmParameterValue: no recognized variant key"
        )
