"""Generated from Smithy shape ``com.amazonaws.datazone#GroupPolicyGrantPrincipal``."""

from typing import TYPE_CHECKING, TypeAlias

from typing_extensions import TypedDict

from capo_datazone.errors import DeserializationError, SerializationError
from capo_datazone.types._unknown import UnknownUnionMember

if TYPE_CHECKING:
    import capo_datazone.types.group_identifier


class GroupPolicyGrantPrincipalGroupIdentifierMember(TypedDict, closed=True):
    groupIdentifier: "capo_datazone.types.group_identifier.GroupIdentifier"


GroupPolicyGrantPrincipal: TypeAlias = (
    GroupPolicyGrantPrincipalGroupIdentifierMember | UnknownUnionMember
)


# --- restJson1 ser/de ---
def serialize_json(value: GroupPolicyGrantPrincipal) -> dict:
    if "$unknown" in value:
        raise SerializationError(
            f"GroupPolicyGrantPrincipal: cannot serialize unknown variant {value['$unknown']['name']!r}"
        )
    elif "groupIdentifier" in value:
        return {"groupIdentifier": value["groupIdentifier"]}
    else:
        raise SerializationError("GroupPolicyGrantPrincipal: no variant present")


def deserialize_json(data: dict) -> GroupPolicyGrantPrincipal:
    if data.get("groupIdentifier") is not None:
        return {"groupIdentifier": data["groupIdentifier"]}
    else:
        name = next(
            (k for k, v in data.items() if v is not None and k != "__type"), None
        )
        if name is not None:
            return {"$unknown": {"name": name}}
        raise DeserializationError(
            "GroupPolicyGrantPrincipal: no recognized variant key"
        )
