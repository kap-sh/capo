"""Generated from Smithy shape ``com.amazonaws.quicksight#ReadAuthConfig``."""

from typing import TYPE_CHECKING, Any

from typing_extensions import TypedDict

if TYPE_CHECKING:
    import capo_quicksight.types.connection_auth_type
    import capo_quicksight.types.read_authentication_metadata


class ReadAuthConfig(TypedDict, closed=True):
    authentication_type: "capo_quicksight.types.connection_auth_type.ConnectionAuthType"
    """<p>The type of authentication being used (BASIC, API_KEY, OAUTH2_CLIENT_CREDENTIALS, or OAUTH2_AUTHORIZATION_CODE).</p>"""
    authentication_metadata: (
        "capo_quicksight.types.read_authentication_metadata.ReadAuthenticationMetadata"
    )
    """<p>The authentication metadata containing configuration details specific to the authentication type.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: ReadAuthConfig) -> dict:
    out: dict = {}
    import capo_quicksight.types.connection_auth_type

    out["AuthenticationType"] = (
        capo_quicksight.types.connection_auth_type.serialize_json(
            value["authentication_type"]
        )
    )
    import capo_quicksight.types.read_authentication_metadata

    out["AuthenticationMetadata"] = (
        capo_quicksight.types.read_authentication_metadata.serialize_json(
            value["authentication_metadata"]
        )
    )
    return out


def deserialize_json(data: dict) -> ReadAuthConfig:
    out: ReadAuthConfig = {}  # type: ignore[typeddict-item]
    if data.get("AuthenticationType") is not None:
        import capo_quicksight.types.connection_auth_type

        out["authentication_type"] = (
            capo_quicksight.types.connection_auth_type.deserialize_json(
                data["AuthenticationType"]
            )
        )
    else:
        import typing

        out["authentication_type"] = typing.cast(
            "capo_quicksight.types.connection_auth_type.ConnectionAuthType", ""
        )
    if data.get("AuthenticationMetadata") is not None:
        import capo_quicksight.types.read_authentication_metadata

        out["authentication_metadata"] = (
            capo_quicksight.types.read_authentication_metadata.deserialize_json(
                data["AuthenticationMetadata"]
            )
        )
    else:
        out["authentication_metadata"] = {"$unknown": {"name": ""}}
    return out


def redact_sensitive(value: ReadAuthConfig) -> dict[str, Any]:
    out: dict[str, Any] = dict(value)
    if "authentication_metadata" in value:
        import capo_quicksight.types.read_authentication_metadata

        out["authentication_metadata"] = (
            capo_quicksight.types.read_authentication_metadata.redact_sensitive(
                value["authentication_metadata"]
            )
        )
    return out
