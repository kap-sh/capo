"""Generated from Smithy shape ``com.amazonaws.quicksight#ClientCredentialsDetails``."""

from typing import TYPE_CHECKING, Any, TypeAlias

from typing_extensions import TypedDict

from capo_quicksight.errors import DeserializationError, SerializationError

if TYPE_CHECKING:
    import capo_quicksight.types.client_credentials_grant_details


class _ClientCredentialsDetails_ClientCredentialsGrantDetails(TypedDict, closed=True):
    ClientCredentialsGrantDetails: "capo_quicksight.types.client_credentials_grant_details.ClientCredentialsGrantDetails"


ClientCredentialsDetails: TypeAlias = (
    _ClientCredentialsDetails_ClientCredentialsGrantDetails
)


# --- restJson1 ser/de ---
def serialize_json(value: ClientCredentialsDetails) -> dict:
    if "ClientCredentialsGrantDetails" in value:
        import capo_quicksight.types.client_credentials_grant_details

        return {
            "ClientCredentialsGrantDetails": capo_quicksight.types.client_credentials_grant_details.serialize_json(
                value["ClientCredentialsGrantDetails"]
            )
        }
    else:
        raise SerializationError("ClientCredentialsDetails: no variant present")


def deserialize_json(data: dict) -> ClientCredentialsDetails:
    if data.get("ClientCredentialsGrantDetails") is not None:
        import capo_quicksight.types.client_credentials_grant_details

        return {
            "ClientCredentialsGrantDetails": capo_quicksight.types.client_credentials_grant_details.deserialize_json(
                data["ClientCredentialsGrantDetails"]
            )
        }
    else:
        raise DeserializationError(
            "ClientCredentialsDetails: no recognized variant key"
        )


def redact_sensitive(value: ClientCredentialsDetails) -> dict[str, Any]:
    out: dict[str, Any] = dict(value)
    if "ClientCredentialsGrantDetails" in value:
        import capo_quicksight.types.client_credentials_grant_details

        out["ClientCredentialsGrantDetails"] = (
            capo_quicksight.types.client_credentials_grant_details.redact_sensitive(
                value["ClientCredentialsGrantDetails"]
            )
        )
    return out
