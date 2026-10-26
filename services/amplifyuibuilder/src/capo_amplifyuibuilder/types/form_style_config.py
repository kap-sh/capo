"""Generated from Smithy shape ``com.amazonaws.amplifyuibuilder#FormStyleConfig``."""

from typing import TypeAlias

from typing_extensions import TypedDict

from capo_amplifyuibuilder.errors import DeserializationError, SerializationError
from capo_amplifyuibuilder.types._unknown import UnknownUnionMember


class _FormStyleConfig_tokenReference(TypedDict, closed=True):
    tokenReference: "str"


class _FormStyleConfig_value(TypedDict, closed=True):
    value: "str"


FormStyleConfig: TypeAlias = (
    _FormStyleConfig_tokenReference | _FormStyleConfig_value | UnknownUnionMember
)


# --- restJson1 ser/de ---
def serialize_json(value: FormStyleConfig) -> dict:
    if "$unknown" in value:
        raise SerializationError(
            f"FormStyleConfig: cannot serialize unknown variant {value['$unknown']['name']!r}"
        )
    elif "tokenReference" in value:
        return {"tokenReference": value["tokenReference"]}
    elif "value" in value:
        return {"value": value["value"]}
    else:
        raise SerializationError("FormStyleConfig: no variant present")


def deserialize_json(data: dict) -> FormStyleConfig:
    if data.get("tokenReference") is not None:
        return {"tokenReference": data["tokenReference"]}
    elif data.get("value") is not None:
        return {"value": data["value"]}
    else:
        name = next(
            (k for k, v in data.items() if v is not None and k != "__type"), None
        )
        if name is not None:
            return {"$unknown": {"name": name}}
        raise DeserializationError("FormStyleConfig: no recognized variant key")
