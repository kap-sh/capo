"""Generated from Smithy shape ``com.amazonaws.quicksight#AuthorizationCodeGrantCredentialsDetails``."""

from typing import TYPE_CHECKING, Any, TypeAlias

from typing_extensions import TypedDict

from capo_quicksight.errors import DeserializationError, SerializationError
from capo_quicksight.types._unknown import UnknownUnionMember

if TYPE_CHECKING:
    import capo_quicksight.types.authorization_code_grant_details


class _AuthorizationCodeGrantCredentialsDetails_AuthorizationCodeGrantDetails(
    TypedDict, closed=True
):
    AuthorizationCodeGrantDetails: "capo_quicksight.types.authorization_code_grant_details.AuthorizationCodeGrantDetails"


AuthorizationCodeGrantCredentialsDetails: TypeAlias = (
    _AuthorizationCodeGrantCredentialsDetails_AuthorizationCodeGrantDetails
    | UnknownUnionMember
)


# --- restJson1 ser/de ---
def serialize_json(value: AuthorizationCodeGrantCredentialsDetails) -> dict:
    if "$unknown" in value:
        raise SerializationError(
            f"AuthorizationCodeGrantCredentialsDetails: cannot serialize unknown variant {value['$unknown']['name']!r}"
        )
    elif "AuthorizationCodeGrantDetails" in value:
        import capo_quicksight.types.authorization_code_grant_details

        return {
            "AuthorizationCodeGrantDetails": capo_quicksight.types.authorization_code_grant_details.serialize_json(
                value["AuthorizationCodeGrantDetails"]
            )
        }
    else:
        raise SerializationError(
            "AuthorizationCodeGrantCredentialsDetails: no variant present"
        )


def deserialize_json(data: dict) -> AuthorizationCodeGrantCredentialsDetails:
    if data.get("AuthorizationCodeGrantDetails") is not None:
        import capo_quicksight.types.authorization_code_grant_details

        return {
            "AuthorizationCodeGrantDetails": capo_quicksight.types.authorization_code_grant_details.deserialize_json(
                data["AuthorizationCodeGrantDetails"]
            )
        }
    else:
        name = next(
            (k for k, v in data.items() if v is not None and k != "__type"), None
        )
        if name is not None:
            return {"$unknown": {"name": name}}
        raise DeserializationError(
            "AuthorizationCodeGrantCredentialsDetails: no recognized variant key"
        )


def redact_sensitive(value: AuthorizationCodeGrantCredentialsDetails) -> dict[str, Any]:
    out: dict[str, Any] = dict(value)
    if "AuthorizationCodeGrantDetails" in value:
        import capo_quicksight.types.authorization_code_grant_details

        out["AuthorizationCodeGrantDetails"] = (
            capo_quicksight.types.authorization_code_grant_details.redact_sensitive(
                value["AuthorizationCodeGrantDetails"]
            )
        )
    return out
