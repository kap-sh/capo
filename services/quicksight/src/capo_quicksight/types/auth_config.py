"""Generated from Smithy shape ``com.amazonaws.quicksight#AuthConfig``."""

from typing import TYPE_CHECKING, Any

from typing_extensions import TypedDict

if TYPE_CHECKING:
    import capo_quicksight.types.authentication_metadata
    import capo_quicksight.types.connection_auth_type


class AuthConfig(TypedDict, closed=True):
    authentication_type: "capo_quicksight.types.connection_auth_type.ConnectionAuthType"
    """<p>The type of authentication method.</p>"""
    authentication_metadata: (
        "capo_quicksight.types.authentication_metadata.AuthenticationMetadata"
    )
    """<p>The authentication metadata containing the specific configuration for the chosen authentication type.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: AuthConfig) -> dict:
    out: dict = {}
    import capo_quicksight.types.connection_auth_type

    out["AuthenticationType"] = (
        capo_quicksight.types.connection_auth_type.serialize_json(
            value["authentication_type"]
        )
    )
    import capo_quicksight.types.authentication_metadata

    out["AuthenticationMetadata"] = (
        capo_quicksight.types.authentication_metadata.serialize_json(
            value["authentication_metadata"]
        )
    )
    return out


def deserialize_json(data: dict) -> AuthConfig:
    out: AuthConfig = {}  # type: ignore[typeddict-item]
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
        import capo_quicksight.types.authentication_metadata

        out["authentication_metadata"] = (
            capo_quicksight.types.authentication_metadata.deserialize_json(
                data["AuthenticationMetadata"]
            )
        )
    else:
        out["authentication_metadata"] = {"$unknown": {"name": ""}}
    return out


def redact_sensitive(value: AuthConfig) -> dict[str, Any]:
    out: dict[str, Any] = dict(value)
    if "authentication_metadata" in value:
        import capo_quicksight.types.authentication_metadata

        out["authentication_metadata"] = (
            capo_quicksight.types.authentication_metadata.redact_sensitive(
                value["authentication_metadata"]
            )
        )
    return out
