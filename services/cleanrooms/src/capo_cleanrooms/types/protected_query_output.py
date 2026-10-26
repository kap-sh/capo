"""Generated from Smithy shape ``com.amazonaws.cleanrooms#ProtectedQueryOutput``."""

from typing import TYPE_CHECKING, TypeAlias

from typing_extensions import TypedDict

from capo_cleanrooms.errors import DeserializationError, SerializationError
from capo_cleanrooms.types._unknown import UnknownUnionMember

if TYPE_CHECKING:
    import capo_cleanrooms.types.protected_query_distribute_output
    import capo_cleanrooms.types.protected_query_member_output_list
    import capo_cleanrooms.types.protected_query_s3_output


class _ProtectedQueryOutput_s3(TypedDict, closed=True):
    s3: "capo_cleanrooms.types.protected_query_s3_output.ProtectedQueryS3Output"


class _ProtectedQueryOutput_memberList(TypedDict, closed=True):
    memberList: "capo_cleanrooms.types.protected_query_member_output_list.ProtectedQueryMemberOutputList"


class _ProtectedQueryOutput_distribute(TypedDict, closed=True):
    distribute: "capo_cleanrooms.types.protected_query_distribute_output.ProtectedQueryDistributeOutput"


ProtectedQueryOutput: TypeAlias = (
    _ProtectedQueryOutput_s3
    | _ProtectedQueryOutput_memberList
    | _ProtectedQueryOutput_distribute
    | UnknownUnionMember
)


# --- restJson1 ser/de ---
def serialize_json(value: ProtectedQueryOutput) -> dict:
    if "$unknown" in value:
        raise SerializationError(
            f"ProtectedQueryOutput: cannot serialize unknown variant {value['$unknown']['name']!r}"
        )
    elif "s3" in value:
        import capo_cleanrooms.types.protected_query_s3_output

        return {
            "s3": capo_cleanrooms.types.protected_query_s3_output.serialize_json(
                value["s3"]
            )
        }
    elif "memberList" in value:
        import capo_cleanrooms.types.protected_query_member_output_list

        return {
            "memberList": capo_cleanrooms.types.protected_query_member_output_list.serialize_json(
                value["memberList"]
            )
        }
    elif "distribute" in value:
        import capo_cleanrooms.types.protected_query_distribute_output

        return {
            "distribute": capo_cleanrooms.types.protected_query_distribute_output.serialize_json(
                value["distribute"]
            )
        }
    else:
        raise SerializationError("ProtectedQueryOutput: no variant present")


def deserialize_json(data: dict) -> ProtectedQueryOutput:
    if data.get("s3") is not None:
        import capo_cleanrooms.types.protected_query_s3_output

        return {
            "s3": capo_cleanrooms.types.protected_query_s3_output.deserialize_json(
                data["s3"]
            )
        }
    elif data.get("memberList") is not None:
        import capo_cleanrooms.types.protected_query_member_output_list

        return {
            "memberList": capo_cleanrooms.types.protected_query_member_output_list.deserialize_json(
                data["memberList"]
            )
        }
    elif data.get("distribute") is not None:
        import capo_cleanrooms.types.protected_query_distribute_output

        return {
            "distribute": capo_cleanrooms.types.protected_query_distribute_output.deserialize_json(
                data["distribute"]
            )
        }
    else:
        name = next(
            (k for k, v in data.items() if v is not None and k != "__type"), None
        )
        if name is not None:
            return {"$unknown": {"name": name}}
        raise DeserializationError("ProtectedQueryOutput: no recognized variant key")
