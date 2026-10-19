"""Generated from Smithy shape ``com.amazonaws.devopsagent#OAuthAdditionalStepDetails``."""

from typing_extensions import TypedDict


class OAuthAdditionalStepDetails(TypedDict, closed=True):
    authorization_url: "str"
    """<p>The URL to redirect the user to for OAuth authorization.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: OAuthAdditionalStepDetails) -> dict:
    out: dict = {}
    out["authorizationUrl"] = value["authorization_url"]
    return out


def deserialize_json(data: dict) -> OAuthAdditionalStepDetails:
    out: OAuthAdditionalStepDetails = {}  # type: ignore[typeddict-item]
    if data.get("authorizationUrl") is not None:
        out["authorization_url"] = data["authorizationUrl"]
    else:
        out["authorization_url"] = ""
    return out
