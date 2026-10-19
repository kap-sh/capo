"""Generated from Smithy shape ``com.amazonaws.bedrockagentcore#LinkedAccountEmail``."""

from typing import TYPE_CHECKING

from typing_extensions import TypedDict

if TYPE_CHECKING:
    import capo_bedrock_agentcore.types.email


class LinkedAccountEmail(TypedDict, closed=True):
    email_address: "capo_bedrock_agentcore.types.email.Email"
    """<p>The email address used for the linked account. Must be a valid email format.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: LinkedAccountEmail) -> dict:
    out: dict = {}
    out["emailAddress"] = value["email_address"]
    return out


def deserialize_json(data: dict) -> LinkedAccountEmail:
    out: LinkedAccountEmail = {}  # type: ignore[typeddict-item]
    if data.get("emailAddress") is not None:
        out["email_address"] = data["emailAddress"]
    else:
        out["email_address"] = ""
    return out
