"""Generated from Smithy shape ``com.amazonaws.quicksight#AuthorizationCodeGrantCredentialsDetails``."""

from typing import TYPE_CHECKING, Any, TypeAlias

from typing_extensions import TypedDict

from capo_quicksight.errors import DeserializationError, SerializationError

if TYPE_CHECKING:
    import capo_quicksight.types.authorization_code_grant_details


class _AuthorizationCodeGrantCredentialsDetails_AuthorizationCodeGrantDetails(
    TypedDict, closed=True
):
    AuthorizationCodeGrantDetails: "capo_quicksight.types.authorization_code_grant_details.AuthorizationCodeGrantDetails"


AuthorizationCodeGrantCredentialsDetails: TypeAlias = (
    _AuthorizationCodeGrantCredentialsDetails_AuthorizationCodeGrantDetails
)


# --- restJson1 ser/de ---
def serialize_json(value: AuthorizationCodeGrantCredentialsDetails) -> dict:
    if "AuthorizationCodeGrantDetails" in value:
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
