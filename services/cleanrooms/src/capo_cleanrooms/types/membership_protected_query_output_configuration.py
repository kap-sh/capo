"""Generated from Smithy shape ``com.amazonaws.cleanrooms#MembershipProtectedQueryOutputConfiguration``."""

from typing import TYPE_CHECKING, TypeAlias

from typing_extensions import TypedDict

from capo_cleanrooms.errors import DeserializationError, SerializationError
from capo_cleanrooms.types._unknown import UnknownUnionMember

if TYPE_CHECKING:
    import capo_cleanrooms.types.protected_query_s3_output_configuration


class MembershipProtectedQueryOutputConfigurationS3Member(TypedDict, closed=True):
    s3: "capo_cleanrooms.types.protected_query_s3_output_configuration.ProtectedQueryS3OutputConfiguration"


MembershipProtectedQueryOutputConfiguration: TypeAlias = (
    MembershipProtectedQueryOutputConfigurationS3Member | UnknownUnionMember
)


# --- restJson1 ser/de ---
def serialize_json(value: MembershipProtectedQueryOutputConfiguration) -> dict:
    if "$unknown" in value:
        raise SerializationError(
            f"MembershipProtectedQueryOutputConfiguration: cannot serialize unknown variant {value['$unknown']['name']!r}"
        )
    elif "s3" in value:
        import capo_cleanrooms.types.protected_query_s3_output_configuration

        return {
            "s3": capo_cleanrooms.types.protected_query_s3_output_configuration.serialize_json(
                value["s3"]
            )
        }
    else:
        raise SerializationError(
            "MembershipProtectedQueryOutputConfiguration: no variant present"
        )


def deserialize_json(data: dict) -> MembershipProtectedQueryOutputConfiguration:
    if data.get("s3") is not None:
        import capo_cleanrooms.types.protected_query_s3_output_configuration

        return {
            "s3": capo_cleanrooms.types.protected_query_s3_output_configuration.deserialize_json(
                data["s3"]
            )
        }
    else:
        name = next(
            (k for k, v in data.items() if v is not None and k != "__type"), None
        )
        if name is not None:
            return {"$unknown": {"name": name}}
        raise DeserializationError(
            "MembershipProtectedQueryOutputConfiguration: no recognized variant key"
        )
