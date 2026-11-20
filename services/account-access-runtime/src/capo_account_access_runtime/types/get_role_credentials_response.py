"""Generated from Smithy shape ``com.amazonaws.accountaccessruntime#GetRoleCredentialsResponse``."""

from typing import TYPE_CHECKING, Any

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_account_access_runtime.types.credentials_details


class GetRoleCredentialsResponse(TypedDict, closed=True):
    credentials_details: NotRequired[
        "capo_account_access_runtime.types.credentials_details.CredentialsDetails"
    ]
    """<p>The temporary credentials that the service returns for the requested role.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: GetRoleCredentialsResponse) -> dict:
    out: dict = {}
    if "credentials_details" in value:
        import capo_account_access_runtime.types.credentials_details

        out["credentialsDetails"] = (
            capo_account_access_runtime.types.credentials_details.serialize_json(
                value["credentials_details"]
            )
        )
    return out


def deserialize_json(data: dict) -> GetRoleCredentialsResponse:
    out: GetRoleCredentialsResponse = {}  # type: ignore[typeddict-item]
    if data.get("credentialsDetails") is not None:
        import capo_account_access_runtime.types.credentials_details

        out["credentials_details"] = (
            capo_account_access_runtime.types.credentials_details.deserialize_json(
                data["credentialsDetails"]
            )
        )
    return out


def redact_sensitive(value: GetRoleCredentialsResponse) -> dict[str, Any]:
    out: dict[str, Any] = dict(value)
    if "credentials_details" in value:
        out["credentials_details"] = "*** Sensitive Data Redacted ***"
    return out
