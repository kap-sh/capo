"""Generated from Smithy shape ``com.amazonaws.cleanrooms#ProtectedQueryDistributeOutputConfigurationLocation``."""

from typing import TYPE_CHECKING, TypeAlias

from typing_extensions import TypedDict

from capo_cleanrooms.errors import DeserializationError, SerializationError
from capo_cleanrooms.types._unknown import UnknownUnionMember

if TYPE_CHECKING:
    import capo_cleanrooms.types.protected_query_member_output_configuration
    import capo_cleanrooms.types.protected_query_s3_output_configuration


class _ProtectedQueryDistributeOutputConfigurationLocation_s3(TypedDict, closed=True):
    s3: "capo_cleanrooms.types.protected_query_s3_output_configuration.ProtectedQueryS3OutputConfiguration"


class _ProtectedQueryDistributeOutputConfigurationLocation_member(
    TypedDict, closed=True
):
    member: "capo_cleanrooms.types.protected_query_member_output_configuration.ProtectedQueryMemberOutputConfiguration"


ProtectedQueryDistributeOutputConfigurationLocation: TypeAlias = (
    _ProtectedQueryDistributeOutputConfigurationLocation_s3
    | _ProtectedQueryDistributeOutputConfigurationLocation_member
    | UnknownUnionMember
)


# --- restJson1 ser/de ---
def serialize_json(value: ProtectedQueryDistributeOutputConfigurationLocation) -> dict:
    if "$unknown" in value:
        raise SerializationError(
            f"ProtectedQueryDistributeOutputConfigurationLocation: cannot serialize unknown variant {value['$unknown']['name']!r}"
        )
    elif "s3" in value:
        import capo_cleanrooms.types.protected_query_s3_output_configuration

        return {
            "s3": capo_cleanrooms.types.protected_query_s3_output_configuration.serialize_json(
                value["s3"]
            )
        }
    elif "member" in value:
        import capo_cleanrooms.types.protected_query_member_output_configuration

        return {
            "member": capo_cleanrooms.types.protected_query_member_output_configuration.serialize_json(
                value["member"]
            )
        }
    else:
        raise SerializationError(
            "ProtectedQueryDistributeOutputConfigurationLocation: no variant present"
        )


def deserialize_json(data: dict) -> ProtectedQueryDistributeOutputConfigurationLocation:
    if data.get("s3") is not None:
        import capo_cleanrooms.types.protected_query_s3_output_configuration

        return {
            "s3": capo_cleanrooms.types.protected_query_s3_output_configuration.deserialize_json(
                data["s3"]
            )
        }
    elif data.get("member") is not None:
        import capo_cleanrooms.types.protected_query_member_output_configuration

        return {
            "member": capo_cleanrooms.types.protected_query_member_output_configuration.deserialize_json(
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
            "ProtectedQueryDistributeOutputConfigurationLocation: no recognized variant key"
        )
