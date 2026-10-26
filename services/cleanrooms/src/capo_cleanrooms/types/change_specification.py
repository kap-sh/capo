"""Generated from Smithy shape ``com.amazonaws.cleanrooms#ChangeSpecification``."""

from typing import TYPE_CHECKING, TypeAlias

from typing_extensions import TypedDict

from capo_cleanrooms.errors import DeserializationError, SerializationError
from capo_cleanrooms.types._unknown import UnknownUnionMember

if TYPE_CHECKING:
    import capo_cleanrooms.types.collaboration_change_specification
    import capo_cleanrooms.types.member_change_specification


class _ChangeSpecification_member(TypedDict, closed=True):
    member: (
        "capo_cleanrooms.types.member_change_specification.MemberChangeSpecification"
    )


class _ChangeSpecification_collaboration(TypedDict, closed=True):
    collaboration: "capo_cleanrooms.types.collaboration_change_specification.CollaborationChangeSpecification"


ChangeSpecification: TypeAlias = (
    _ChangeSpecification_member
    | _ChangeSpecification_collaboration
    | UnknownUnionMember
)


# --- restJson1 ser/de ---
def serialize_json(value: ChangeSpecification) -> dict:
    if "$unknown" in value:
        raise SerializationError(
            f"ChangeSpecification: cannot serialize unknown variant {value['$unknown']['name']!r}"
        )
    elif "member" in value:
        import capo_cleanrooms.types.member_change_specification

        return {
            "member": capo_cleanrooms.types.member_change_specification.serialize_json(
                value["member"]
            )
        }
    elif "collaboration" in value:
        import capo_cleanrooms.types.collaboration_change_specification

        return {
            "collaboration": capo_cleanrooms.types.collaboration_change_specification.serialize_json(
                value["collaboration"]
            )
        }
    else:
        raise SerializationError("ChangeSpecification: no variant present")


def deserialize_json(data: dict) -> ChangeSpecification:
    if data.get("member") is not None:
        import capo_cleanrooms.types.member_change_specification

        return {
            "member": capo_cleanrooms.types.member_change_specification.deserialize_json(
                data["member"]
            )
        }
    elif data.get("collaboration") is not None:
        import capo_cleanrooms.types.collaboration_change_specification

        return {
            "collaboration": capo_cleanrooms.types.collaboration_change_specification.deserialize_json(
                data["collaboration"]
            )
        }
    else:
        name = next(
            (k for k, v in data.items() if v is not None and k != "__type"), None
        )
        if name is not None:
            return {"$unknown": {"name": name}}
        raise DeserializationError("ChangeSpecification: no recognized variant key")
