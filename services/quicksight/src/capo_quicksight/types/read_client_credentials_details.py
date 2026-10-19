"""Generated from Smithy shape ``com.amazonaws.quicksight#ReadClientCredentialsDetails``."""

from typing import TYPE_CHECKING, TypeAlias

from typing_extensions import TypedDict

from capo_quicksight.errors import DeserializationError, SerializationError
from capo_quicksight.types._unknown import UnknownUnionMember

if TYPE_CHECKING:
    import capo_quicksight.types.read_client_credentials_grant_details


class _ReadClientCredentialsDetails_ReadClientCredentialsGrantDetails(
    TypedDict, closed=True
):
    ReadClientCredentialsGrantDetails: "capo_quicksight.types.read_client_credentials_grant_details.ReadClientCredentialsGrantDetails"


ReadClientCredentialsDetails: TypeAlias = (
    _ReadClientCredentialsDetails_ReadClientCredentialsGrantDetails | UnknownUnionMember
)


# --- restJson1 ser/de ---
def serialize_json(value: ReadClientCredentialsDetails) -> dict:
    if isinstance(value, UnknownUnionMember):
        raise SerializationError(
            f"ReadClientCredentialsDetails: cannot serialize unknown variant {value.name!r}"
        )
    elif "ReadClientCredentialsGrantDetails" in value:
        import capo_quicksight.types.read_client_credentials_grant_details

        return {
            "ReadClientCredentialsGrantDetails": capo_quicksight.types.read_client_credentials_grant_details.serialize_json(
                value["ReadClientCredentialsGrantDetails"]
            )
        }
    else:
        raise SerializationError("ReadClientCredentialsDetails: no variant present")


def deserialize_json(data: dict) -> ReadClientCredentialsDetails:
    if data.get("ReadClientCredentialsGrantDetails") is not None:
        import capo_quicksight.types.read_client_credentials_grant_details

        return {
            "ReadClientCredentialsGrantDetails": capo_quicksight.types.read_client_credentials_grant_details.deserialize_json(
                data["ReadClientCredentialsGrantDetails"]
            )
        }
    else:
        name = next(
            (k for k, v in data.items() if v is not None and k != "__type"), None
        )
        if name is not None:
            return UnknownUnionMember(name)
        raise DeserializationError(
            "ReadClientCredentialsDetails: no recognized variant key"
        )
