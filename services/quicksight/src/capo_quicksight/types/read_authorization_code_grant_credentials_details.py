"""Generated from Smithy shape ``com.amazonaws.quicksight#ReadAuthorizationCodeGrantCredentialsDetails``."""

from typing import TYPE_CHECKING, TypeAlias

from typing_extensions import TypedDict

from capo_quicksight.errors import DeserializationError, SerializationError
from capo_quicksight.types._unknown import UnknownUnionMember

if TYPE_CHECKING:
    import capo_quicksight.types.read_authorization_code_grant_details


class ReadAuthorizationCodeGrantCredentialsDetailsReadAuthorizationCodeGrantDetailsMember(
    TypedDict, closed=True
):
    ReadAuthorizationCodeGrantDetails: "capo_quicksight.types.read_authorization_code_grant_details.ReadAuthorizationCodeGrantDetails"


ReadAuthorizationCodeGrantCredentialsDetails: TypeAlias = (
    ReadAuthorizationCodeGrantCredentialsDetailsReadAuthorizationCodeGrantDetailsMember
    | UnknownUnionMember
)


# --- restJson1 ser/de ---
def serialize_json(value: ReadAuthorizationCodeGrantCredentialsDetails) -> dict:
    if "$unknown" in value:
        raise SerializationError(
            f"ReadAuthorizationCodeGrantCredentialsDetails: cannot serialize unknown variant {value['$unknown']['name']!r}"
        )
    elif "ReadAuthorizationCodeGrantDetails" in value:
        import capo_quicksight.types.read_authorization_code_grant_details

        return {
            "ReadAuthorizationCodeGrantDetails": capo_quicksight.types.read_authorization_code_grant_details.serialize_json(
                value["ReadAuthorizationCodeGrantDetails"]
            )
        }
    else:
        raise SerializationError(
            "ReadAuthorizationCodeGrantCredentialsDetails: no variant present"
        )


def deserialize_json(data: dict) -> ReadAuthorizationCodeGrantCredentialsDetails:
    if data.get("ReadAuthorizationCodeGrantDetails") is not None:
        import capo_quicksight.types.read_authorization_code_grant_details

        return {
            "ReadAuthorizationCodeGrantDetails": capo_quicksight.types.read_authorization_code_grant_details.deserialize_json(
                data["ReadAuthorizationCodeGrantDetails"]
            )
        }
    else:
        name = next(
            (k for k, v in data.items() if v is not None and k != "__type"), None
        )
        if name is not None:
            return {"$unknown": {"name": name}}
        raise DeserializationError(
            "ReadAuthorizationCodeGrantCredentialsDetails: no recognized variant key"
        )
