"""Generated from Smithy shape ``com.amazonaws.appintegrations#AuthConfig``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_appintegrations.types.arn
    import capo_appintegrations.types.auth_type


class AuthConfig(TypedDict, closed=True):
    auth_type: NotRequired["capo_appintegrations.types.auth_type.AuthType"]
    """<p>The type of authentication used when calling the external application.</p>"""
    credential_provider_identifier: NotRequired["capo_appintegrations.types.arn.Arn"]
    """<p>The ARN of the Secrets Manager secret that stores the credentials. The secret must be accessible to Connect Customer.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: AuthConfig) -> dict:
    out: dict = {}
    if "auth_type" in value:
        import capo_appintegrations.types.auth_type

        out["AuthType"] = capo_appintegrations.types.auth_type.serialize_json(
            value["auth_type"]
        )
    if "credential_provider_identifier" in value:
        out["CredentialProviderIdentifier"] = value["credential_provider_identifier"]
    return out


def deserialize_json(data: dict) -> AuthConfig:
    out: AuthConfig = {}  # type: ignore[typeddict-item]
    if data.get("AuthType") is not None:
        import capo_appintegrations.types.auth_type

        out["auth_type"] = capo_appintegrations.types.auth_type.deserialize_json(
            data["AuthType"]
        )
    if data.get("CredentialProviderIdentifier") is not None:
        out["credential_provider_identifier"] = data["CredentialProviderIdentifier"]
    return out
