"""Generated from Smithy shape ``com.amazonaws.sso#GetRoleCredentialsResponse``."""

from typing import TYPE_CHECKING, Any

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_sso.types.role_credentials


class GetRoleCredentialsResponse(TypedDict, closed=True):
    role_credentials: NotRequired["capo_sso.types.role_credentials.RoleCredentials"]
    """<p>The credentials for the role that is assigned to the user.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: GetRoleCredentialsResponse) -> dict:
    out: dict = {}
    if "role_credentials" in value:
        import capo_sso.types.role_credentials

        out["roleCredentials"] = capo_sso.types.role_credentials.serialize_json(
            value["role_credentials"]
        )
    return out


def deserialize_json(data: dict) -> GetRoleCredentialsResponse:
    out: GetRoleCredentialsResponse = {}  # type: ignore[typeddict-item]
    if data.get("roleCredentials") is not None:
        import capo_sso.types.role_credentials

        out["role_credentials"] = capo_sso.types.role_credentials.deserialize_json(
            data["roleCredentials"]
        )
    return out


def redact_sensitive(value: GetRoleCredentialsResponse) -> dict[str, Any]:
    out: dict[str, Any] = dict(value)
    if "role_credentials" in value:
        import capo_sso.types.role_credentials

        out["role_credentials"] = capo_sso.types.role_credentials.redact_sensitive(
            value["role_credentials"]
        )
    return out
