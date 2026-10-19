"""Generated from Smithy shape ``com.amazonaws.cleanrooms#ProtectedJobOutput``."""

from typing import TYPE_CHECKING, TypeAlias

from typing_extensions import TypedDict

from capo_cleanrooms.errors import DeserializationError, SerializationError
from capo_cleanrooms.types._unknown import UnknownUnionMember

if TYPE_CHECKING:
    import capo_cleanrooms.types.protected_job_member_output_list
    import capo_cleanrooms.types.protected_job_s3_output


class _ProtectedJobOutput_s3(TypedDict, closed=True):
    s3: "capo_cleanrooms.types.protected_job_s3_output.ProtectedJobS3Output"


class _ProtectedJobOutput_memberList(TypedDict, closed=True):
    memberList: "capo_cleanrooms.types.protected_job_member_output_list.ProtectedJobMemberOutputList"


ProtectedJobOutput: TypeAlias = (
    _ProtectedJobOutput_s3 | _ProtectedJobOutput_memberList | UnknownUnionMember
)


# --- restJson1 ser/de ---
def serialize_json(value: ProtectedJobOutput) -> dict:
    if isinstance(value, UnknownUnionMember):
        raise SerializationError(
            f"ProtectedJobOutput: cannot serialize unknown variant {value.name!r}"
        )
    elif "s3" in value:
        import capo_cleanrooms.types.protected_job_s3_output

        return {
            "s3": capo_cleanrooms.types.protected_job_s3_output.serialize_json(
                value["s3"]
            )
        }
    elif "memberList" in value:
        import capo_cleanrooms.types.protected_job_member_output_list

        return {
            "memberList": capo_cleanrooms.types.protected_job_member_output_list.serialize_json(
                value["memberList"]
            )
        }
    else:
        raise SerializationError("ProtectedJobOutput: no variant present")


def deserialize_json(data: dict) -> ProtectedJobOutput:
    if data.get("s3") is not None:
        import capo_cleanrooms.types.protected_job_s3_output

        return {
            "s3": capo_cleanrooms.types.protected_job_s3_output.deserialize_json(
                data["s3"]
            )
        }
    elif data.get("memberList") is not None:
        import capo_cleanrooms.types.protected_job_member_output_list

        return {
            "memberList": capo_cleanrooms.types.protected_job_member_output_list.deserialize_json(
                data["memberList"]
            )
        }
    else:
        name = next(
            (k for k, v in data.items() if v is not None and k != "__type"), None
        )
        if name is not None:
            return UnknownUnionMember(name)
        raise DeserializationError("ProtectedJobOutput: no recognized variant key")
