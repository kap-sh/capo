"""Generated from Smithy shape ``com.amazonaws.cleanrooms#ProtectedJobOutputConfigurationInput``."""

from typing import TYPE_CHECKING, TypeAlias

from typing_extensions import TypedDict

from capo_cleanrooms.errors import DeserializationError, SerializationError
from capo_cleanrooms.types._unknown import UnknownUnionMember

if TYPE_CHECKING:
    import capo_cleanrooms.types.protected_job_member_output_configuration_input


class _ProtectedJobOutputConfigurationInput_member(TypedDict, closed=True):
    member: "capo_cleanrooms.types.protected_job_member_output_configuration_input.ProtectedJobMemberOutputConfigurationInput"


ProtectedJobOutputConfigurationInput: TypeAlias = (
    _ProtectedJobOutputConfigurationInput_member | UnknownUnionMember
)


# --- restJson1 ser/de ---
def serialize_json(value: ProtectedJobOutputConfigurationInput) -> dict:
    if "$unknown" in value:
        raise SerializationError(
            f"ProtectedJobOutputConfigurationInput: cannot serialize unknown variant {value['$unknown']['name']!r}"
        )
    elif "member" in value:
        import capo_cleanrooms.types.protected_job_member_output_configuration_input

        return {
            "member": capo_cleanrooms.types.protected_job_member_output_configuration_input.serialize_json(
                value["member"]
            )
        }
    else:
        raise SerializationError(
            "ProtectedJobOutputConfigurationInput: no variant present"
        )


def deserialize_json(data: dict) -> ProtectedJobOutputConfigurationInput:
    if data.get("member") is not None:
        import capo_cleanrooms.types.protected_job_member_output_configuration_input

        return {
            "member": capo_cleanrooms.types.protected_job_member_output_configuration_input.deserialize_json(
                data["member"]
            )
        }
    else:
        name = next(
            (k for k, v in data.items() if v is not None and k != "__type"), None
        )
        if name is not None:
            return {"$unknown": {"name": name}}
        raise DeserializationError(
            "ProtectedJobOutputConfigurationInput: no recognized variant key"
        )
