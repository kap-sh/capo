"""Generated from Smithy shape ``com.amazonaws.inspector2#CodeSecurityResource``."""

from typing import TYPE_CHECKING, TypeAlias

from typing_extensions import TypedDict

from capo_inspector2.errors import DeserializationError, SerializationError
from capo_inspector2.types._unknown import UnknownUnionMember

if TYPE_CHECKING:
    import capo_inspector2.types.project_id


class CodeSecurityResourceProjectIdMember(TypedDict, closed=True):
    projectId: "capo_inspector2.types.project_id.ProjectId"


CodeSecurityResource: TypeAlias = (
    CodeSecurityResourceProjectIdMember | UnknownUnionMember
)


# --- restJson1 ser/de ---
def serialize_json(value: CodeSecurityResource) -> dict:
    if "$unknown" in value:
        raise SerializationError(
            f"CodeSecurityResource: cannot serialize unknown variant {value['$unknown']['name']!r}"
        )
    elif "projectId" in value:
        return {"projectId": value["projectId"]}
    else:
        raise SerializationError("CodeSecurityResource: no variant present")


def deserialize_json(data: dict) -> CodeSecurityResource:
    if data.get("projectId") is not None:
        return {"projectId": data["projectId"]}
    else:
        name = next(
            (k for k, v in data.items() if v is not None and k != "__type"), None
        )
        if name is not None:
            return {"$unknown": {"name": name}}
        raise DeserializationError("CodeSecurityResource: no recognized variant key")
