"""Generated from Smithy shape ``com.amazonaws.continuum#StartIntegrationAuthorizationOutput``."""

from typing import TYPE_CHECKING, Any

from typing_extensions import TypedDict

if TYPE_CHECKING:
    import datetime

    import capo_continuum.types.o_auth_code_challenge
    import capo_continuum.types.o_auth_code_challenge_method
    import capo_continuum.types.o_auth_state


class StartIntegrationAuthorizationOutput(TypedDict, closed=True):
    state: "capo_continuum.types.o_auth_state.OAuthState"
    """An opaque value to send as the OAuth `state` parameter. Pass the value the provider returns in its callback to CreateIntegration as `authorization.state`."""
    code_challenge: "capo_continuum.types.o_auth_code_challenge.OAuthCodeChallenge"
    """The PKCE code challenge to send as the OAuth `code_challenge` parameter."""
    code_challenge_method: (
        "capo_continuum.types.o_auth_code_challenge_method.OAuthCodeChallengeMethod"
    )
    """The PKCE challenge method to send as the OAuth `code_challenge_method` parameter."""
    expires_at: "datetime.datetime"
    """The time after which CreateIntegration no longer accepts this authorization."""


# --- restJson1 ser/de ---
def serialize_json(value: StartIntegrationAuthorizationOutput) -> dict:
    out: dict = {}
    out["state"] = value["state"]
    out["codeChallenge"] = value["code_challenge"]
    import capo_continuum.types.o_auth_code_challenge_method

    out["codeChallengeMethod"] = (
        capo_continuum.types.o_auth_code_challenge_method.serialize_json(
            value["code_challenge_method"]
        )
    )
    import capo_continuum._protocol.serialize

    out["expiresAt"] = capo_continuum._protocol.serialize.fmt_date_time(
        value["expires_at"]
    )
    return out


def deserialize_json(data: dict) -> StartIntegrationAuthorizationOutput:
    out: StartIntegrationAuthorizationOutput = {}  # type: ignore[typeddict-item]
    if data.get("state") is not None:
        out["state"] = data["state"]
    else:
        out["state"] = ""
    if data.get("codeChallenge") is not None:
        out["code_challenge"] = data["codeChallenge"]
    else:
        out["code_challenge"] = ""
    if data.get("codeChallengeMethod") is not None:
        import capo_continuum.types.o_auth_code_challenge_method

        out["code_challenge_method"] = (
            capo_continuum.types.o_auth_code_challenge_method.deserialize_json(
                data["codeChallengeMethod"]
            )
        )
    else:
        import typing

        out["code_challenge_method"] = typing.cast(
            "capo_continuum.types.o_auth_code_challenge_method.OAuthCodeChallengeMethod",
            "",
        )
    if data.get("expiresAt") is not None:
        import datetime

        out["expires_at"] = datetime.datetime.fromisoformat(
            data["expiresAt"].replace("Z", "+00:00")
        )
    else:
        import datetime

        out["expires_at"] = datetime.datetime.fromtimestamp(0, tz=datetime.timezone.utc)
    return out


def redact_sensitive(value: StartIntegrationAuthorizationOutput) -> dict[str, Any]:
    out: dict[str, Any] = dict(value)
    if "state" in value:
        out["state"] = "*** Sensitive Data Redacted ***"
    return out
