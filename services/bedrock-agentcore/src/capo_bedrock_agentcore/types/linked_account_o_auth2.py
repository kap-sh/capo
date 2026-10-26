"""Generated from Smithy shape ``com.amazonaws.bedrockagentcore#LinkedAccountOAuth2``."""

from typing import TYPE_CHECKING, Any, TypeAlias

from typing_extensions import TypedDict

from capo_bedrock_agentcore.errors import DeserializationError, SerializationError
from capo_bedrock_agentcore.types._unknown import UnknownUnionMember

if TYPE_CHECKING:
    import capo_bedrock_agentcore.types.o_auth2_authentication


class _LinkedAccountOAuth2_google(TypedDict, closed=True):
    google: "capo_bedrock_agentcore.types.o_auth2_authentication.OAuth2Authentication"


class _LinkedAccountOAuth2_apple(TypedDict, closed=True):
    apple: "capo_bedrock_agentcore.types.o_auth2_authentication.OAuth2Authentication"


class _LinkedAccountOAuth2_x(TypedDict, closed=True):
    x: "capo_bedrock_agentcore.types.o_auth2_authentication.OAuth2Authentication"


class _LinkedAccountOAuth2_telegram(TypedDict, closed=True):
    telegram: "capo_bedrock_agentcore.types.o_auth2_authentication.OAuth2Authentication"


class _LinkedAccountOAuth2_github(TypedDict, closed=True):
    github: "capo_bedrock_agentcore.types.o_auth2_authentication.OAuth2Authentication"


LinkedAccountOAuth2: TypeAlias = (
    _LinkedAccountOAuth2_google
    | _LinkedAccountOAuth2_apple
    | _LinkedAccountOAuth2_x
    | _LinkedAccountOAuth2_telegram
    | _LinkedAccountOAuth2_github
    | UnknownUnionMember
)


# --- restJson1 ser/de ---
def serialize_json(value: LinkedAccountOAuth2) -> dict:
    if "$unknown" in value:
        raise SerializationError(
            f"LinkedAccountOAuth2: cannot serialize unknown variant {value['$unknown']['name']!r}"
        )
    elif "google" in value:
        import capo_bedrock_agentcore.types.o_auth2_authentication

        return {
            "google": capo_bedrock_agentcore.types.o_auth2_authentication.serialize_json(
                value["google"]
            )
        }
    elif "apple" in value:
        import capo_bedrock_agentcore.types.o_auth2_authentication

        return {
            "apple": capo_bedrock_agentcore.types.o_auth2_authentication.serialize_json(
                value["apple"]
            )
        }
    elif "x" in value:
        import capo_bedrock_agentcore.types.o_auth2_authentication

        return {
            "x": capo_bedrock_agentcore.types.o_auth2_authentication.serialize_json(
                value["x"]
            )
        }
    elif "telegram" in value:
        import capo_bedrock_agentcore.types.o_auth2_authentication

        return {
            "telegram": capo_bedrock_agentcore.types.o_auth2_authentication.serialize_json(
                value["telegram"]
            )
        }
    elif "github" in value:
        import capo_bedrock_agentcore.types.o_auth2_authentication

        return {
            "github": capo_bedrock_agentcore.types.o_auth2_authentication.serialize_json(
                value["github"]
            )
        }
    else:
        raise SerializationError("LinkedAccountOAuth2: no variant present")


def deserialize_json(data: dict) -> LinkedAccountOAuth2:
    if data.get("google") is not None:
        import capo_bedrock_agentcore.types.o_auth2_authentication

        return {
            "google": capo_bedrock_agentcore.types.o_auth2_authentication.deserialize_json(
                data["google"]
            )
        }
    elif data.get("apple") is not None:
        import capo_bedrock_agentcore.types.o_auth2_authentication

        return {
            "apple": capo_bedrock_agentcore.types.o_auth2_authentication.deserialize_json(
                data["apple"]
            )
        }
    elif data.get("x") is not None:
        import capo_bedrock_agentcore.types.o_auth2_authentication

        return {
            "x": capo_bedrock_agentcore.types.o_auth2_authentication.deserialize_json(
                data["x"]
            )
        }
    elif data.get("telegram") is not None:
        import capo_bedrock_agentcore.types.o_auth2_authentication

        return {
            "telegram": capo_bedrock_agentcore.types.o_auth2_authentication.deserialize_json(
                data["telegram"]
            )
        }
    elif data.get("github") is not None:
        import capo_bedrock_agentcore.types.o_auth2_authentication

        return {
            "github": capo_bedrock_agentcore.types.o_auth2_authentication.deserialize_json(
                data["github"]
            )
        }
    else:
        name = next(
            (k for k, v in data.items() if v is not None and k != "__type"), None
        )
        if name is not None:
            return {"$unknown": {"name": name}}
        raise DeserializationError("LinkedAccountOAuth2: no recognized variant key")


def redact_sensitive(value: LinkedAccountOAuth2) -> dict[str, Any]:
    out: dict[str, Any] = dict(value)
    if "google" in value:
        out["google"] = "*** Sensitive Data Redacted ***"
    if "apple" in value:
        out["apple"] = "*** Sensitive Data Redacted ***"
    if "x" in value:
        out["x"] = "*** Sensitive Data Redacted ***"
    if "telegram" in value:
        out["telegram"] = "*** Sensitive Data Redacted ***"
    if "github" in value:
        out["github"] = "*** Sensitive Data Redacted ***"
    return out
