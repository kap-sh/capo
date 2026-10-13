"""Generated from Smithy shape ``com.amazonaws.appflow#CustomAuthCredentials``."""

from typing import TYPE_CHECKING, Any

from typing_extensions import NotRequired, TypedDict

from capo_appflow.errors import DeserializationError

if TYPE_CHECKING:
    import capo_appflow.types.credentials_map
    import capo_appflow.types.custom_authentication_type


class CustomAuthCredentials(TypedDict, closed=True):
    custom_authentication_type: (
        "capo_appflow.types.custom_authentication_type.CustomAuthenticationType"
    )
    """<p>The custom authentication type that the connector uses.</p>"""
    credentials_map: NotRequired["capo_appflow.types.credentials_map.CredentialsMap"]
    """<p>A map that holds custom authentication credentials.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: CustomAuthCredentials) -> dict:
    out: dict = {}
    out["customAuthenticationType"] = value["custom_authentication_type"]
    if "credentials_map" in value:
        import capo_appflow.types.credentials_map

        out["credentialsMap"] = capo_appflow.types.credentials_map.serialize_json(
            value["credentials_map"]
        )
    return out


def deserialize_json(data: dict) -> CustomAuthCredentials:
    out: CustomAuthCredentials = {}  # type: ignore[typeddict-item]
    if data.get("customAuthenticationType") is not None:
        out["custom_authentication_type"] = data["customAuthenticationType"]
    else:
        raise DeserializationError(
            "CustomAuthCredentials.custom_authentication_type required"
        )
    if data.get("credentialsMap") is not None:
        import capo_appflow.types.credentials_map

        out["credentials_map"] = capo_appflow.types.credentials_map.deserialize_json(
            data["credentialsMap"]
        )
    return out


def redact_sensitive(value: CustomAuthCredentials) -> dict[str, Any]:
    out: dict[str, Any] = dict(value)
    if "credentials_map" in value:
        out["credentials_map"] = "*** Sensitive Data Redacted ***"
    return out
