"""Generated from Smithy shape ``com.amazonaws.mgn#SsmExternalParameter``."""

from typing import TYPE_CHECKING, TypeAlias

from typing_extensions import TypedDict

from capo_mgn.errors import DeserializationError, SerializationError
from capo_mgn.types._unknown import UnknownUnionMember

if TYPE_CHECKING:
    import capo_mgn.types.jmes_path_string


class SsmExternalParameterDynamicPathMember(TypedDict, closed=True):
    dynamicPath: "capo_mgn.types.jmes_path_string.JmesPathString"


SsmExternalParameter: TypeAlias = (
    SsmExternalParameterDynamicPathMember | UnknownUnionMember
)


# --- restJson1 ser/de ---
def serialize_json(value: SsmExternalParameter) -> dict:
    if "$unknown" in value:
        raise SerializationError(
            f"SsmExternalParameter: cannot serialize unknown variant {value['$unknown']['name']!r}"
        )
    elif "dynamicPath" in value:
        return {"dynamicPath": value["dynamicPath"]}
    else:
        raise SerializationError("SsmExternalParameter: no variant present")


def deserialize_json(data: dict) -> SsmExternalParameter:
    if data.get("dynamicPath") is not None:
        return {"dynamicPath": data["dynamicPath"]}
    else:
        name = next(
            (k for k, v in data.items() if v is not None and k != "__type"), None
        )
        if name is not None:
            return {"$unknown": {"name": name}}
        raise DeserializationError("SsmExternalParameter: no recognized variant key")
