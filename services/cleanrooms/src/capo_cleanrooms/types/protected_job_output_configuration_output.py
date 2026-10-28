"""Generated from Smithy shape ``com.amazonaws.cleanrooms#ProtectedJobOutputConfigurationOutput``."""

from typing import TYPE_CHECKING, TypeAlias

from typing_extensions import TypedDict

from capo_cleanrooms.errors import DeserializationError, SerializationError
from capo_cleanrooms.types._unknown import UnknownUnionMember

if TYPE_CHECKING:
    import capo_cleanrooms.types.protected_job_member_output_configuration_output
    import capo_cleanrooms.types.protected_job_s3_output_configuration_output


class ProtectedJobOutputConfigurationOutputS3Member(TypedDict, closed=True):
    s3: "capo_cleanrooms.types.protected_job_s3_output_configuration_output.ProtectedJobS3OutputConfigurationOutput"


class ProtectedJobOutputConfigurationOutputMemberMember(TypedDict, closed=True):
    member: "capo_cleanrooms.types.protected_job_member_output_configuration_output.ProtectedJobMemberOutputConfigurationOutput"


ProtectedJobOutputConfigurationOutput: TypeAlias = (
    ProtectedJobOutputConfigurationOutputS3Member
    | ProtectedJobOutputConfigurationOutputMemberMember
    | UnknownUnionMember
)


# --- restJson1 ser/de ---
def serialize_json(value: ProtectedJobOutputConfigurationOutput) -> dict:
    if "$unknown" in value:
        raise SerializationError(
            f"ProtectedJobOutputConfigurationOutput: cannot serialize unknown variant {value['$unknown']['name']!r}"
        )
    elif "s3" in value:
        import capo_cleanrooms.types.protected_job_s3_output_configuration_output

        return {
            "s3": capo_cleanrooms.types.protected_job_s3_output_configuration_output.serialize_json(
                value["s3"]
            )
        }
    elif "member" in value:
        import capo_cleanrooms.types.protected_job_member_output_configuration_output

        return {
            "member": capo_cleanrooms.types.protected_job_member_output_configuration_output.serialize_json(
                value["member"]
            )
        }
    else:
        raise SerializationError(
            "ProtectedJobOutputConfigurationOutput: no variant present"
        )


def deserialize_json(data: dict) -> ProtectedJobOutputConfigurationOutput:
    if data.get("s3") is not None:
        import capo_cleanrooms.types.protected_job_s3_output_configuration_output

        return {
            "s3": capo_cleanrooms.types.protected_job_s3_output_configuration_output.deserialize_json(
                data["s3"]
            )
        }
    elif data.get("member") is not None:
        import capo_cleanrooms.types.protected_job_member_output_configuration_output

        return {
            "member": capo_cleanrooms.types.protected_job_member_output_configuration_output.deserialize_json(
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
            "ProtectedJobOutputConfigurationOutput: no recognized variant key"
        )
