"""Generated from Smithy shape ``com.amazonaws.bedrockagentcore#OAuth2Authentication``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_bedrock_agentcore.types.email


class OAuth2Authentication(TypedDict, closed=True):
    sub: "str"
    """<p>The subject (sub) claim from the OAuth2 provider. Uniquely identifies the user at the provider.</p>"""
    email_address: NotRequired["capo_bedrock_agentcore.types.email.Email"]
    """<p>The email address from the OAuth2 provider.</p>"""
    name: NotRequired["str"]
    """<p>The user's name from the OAuth2 provider.</p>"""
    username: NotRequired["str"]
    """<p>The username from the OAuth2 provider.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: OAuth2Authentication) -> dict:
    out: dict = {}
    out["sub"] = value["sub"]
    if "email_address" in value:
        out["emailAddress"] = value["email_address"]
    if "name" in value:
        out["name"] = value["name"]
    if "username" in value:
        out["username"] = value["username"]
    return out


def deserialize_json(data: dict) -> OAuth2Authentication:
    out: OAuth2Authentication = {}  # type: ignore[typeddict-item]
    if data.get("sub") is not None:
        out["sub"] = data["sub"]
    else:
        out["sub"] = ""
    if data.get("emailAddress") is not None:
        out["email_address"] = data["emailAddress"]
    if data.get("name") is not None:
        out["name"] = data["name"]
    if data.get("username") is not None:
        out["username"] = data["username"]
    return out
