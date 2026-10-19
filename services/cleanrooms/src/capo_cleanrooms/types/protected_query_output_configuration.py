"""Generated from Smithy shape ``com.amazonaws.cleanrooms#ProtectedQueryOutputConfiguration``."""

from typing import TYPE_CHECKING, TypeAlias

from typing_extensions import TypedDict

from capo_cleanrooms.errors import DeserializationError, SerializationError
from capo_cleanrooms.types._unknown import UnknownUnionMember

if TYPE_CHECKING:
    import capo_cleanrooms.types.intermediate_table_output_configuration
    import capo_cleanrooms.types.protected_query_distribute_output_configuration
    import capo_cleanrooms.types.protected_query_member_output_configuration
    import capo_cleanrooms.types.protected_query_s3_output_configuration


class _ProtectedQueryOutputConfiguration_s3(TypedDict, closed=True):
    s3: "capo_cleanrooms.types.protected_query_s3_output_configuration.ProtectedQueryS3OutputConfiguration"


class _ProtectedQueryOutputConfiguration_member(TypedDict, closed=True):
    member: "capo_cleanrooms.types.protected_query_member_output_configuration.ProtectedQueryMemberOutputConfiguration"


class _ProtectedQueryOutputConfiguration_distribute(TypedDict, closed=True):
    distribute: "capo_cleanrooms.types.protected_query_distribute_output_configuration.ProtectedQueryDistributeOutputConfiguration"


class _ProtectedQueryOutputConfiguration_intermediateTable(TypedDict, closed=True):
    intermediateTable: "capo_cleanrooms.types.intermediate_table_output_configuration.IntermediateTableOutputConfiguration"


ProtectedQueryOutputConfiguration: TypeAlias = (
    _ProtectedQueryOutputConfiguration_s3
    | _ProtectedQueryOutputConfiguration_member
    | _ProtectedQueryOutputConfiguration_distribute
    | _ProtectedQueryOutputConfiguration_intermediateTable
    | UnknownUnionMember
)


# --- restJson1 ser/de ---
def serialize_json(value: ProtectedQueryOutputConfiguration) -> dict:
    if isinstance(value, UnknownUnionMember):
        raise SerializationError(
            f"ProtectedQueryOutputConfiguration: cannot serialize unknown variant {value.name!r}"
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
    elif "distribute" in value:
        import capo_cleanrooms.types.protected_query_distribute_output_configuration

        return {
            "distribute": capo_cleanrooms.types.protected_query_distribute_output_configuration.serialize_json(
                value["distribute"]
            )
        }
    elif "intermediateTable" in value:
        import capo_cleanrooms.types.intermediate_table_output_configuration

        return {
            "intermediateTable": capo_cleanrooms.types.intermediate_table_output_configuration.serialize_json(
                value["intermediateTable"]
            )
        }
    else:
        raise SerializationError(
            "ProtectedQueryOutputConfiguration: no variant present"
        )


def deserialize_json(data: dict) -> ProtectedQueryOutputConfiguration:
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
    elif data.get("distribute") is not None:
        import capo_cleanrooms.types.protected_query_distribute_output_configuration

        return {
            "distribute": capo_cleanrooms.types.protected_query_distribute_output_configuration.deserialize_json(
                data["distribute"]
            )
        }
    elif data.get("intermediateTable") is not None:
        import capo_cleanrooms.types.intermediate_table_output_configuration

        return {
            "intermediateTable": capo_cleanrooms.types.intermediate_table_output_configuration.deserialize_json(
                data["intermediateTable"]
            )
        }
    else:
        name = next(
            (k for k, v in data.items() if v is not None and k != "__type"), None
        )
        if name is not None:
            return UnknownUnionMember(name)
        raise DeserializationError(
            "ProtectedQueryOutputConfiguration: no recognized variant key"
        )
