"""Generated from Smithy shape ``com.amazonaws.bedrockagentcore#BrowserProfileConfiguration``."""

from typing import TYPE_CHECKING

from typing_extensions import TypedDict

if TYPE_CHECKING:
    import capo_bedrock_agentcore.types.browser_profile_id


class BrowserProfileConfiguration(TypedDict, closed=True):
    profile_identifier: (
        "capo_bedrock_agentcore.types.browser_profile_id.BrowserProfileId"
    )
    """<p>The unique identifier of the browser profile. This identifier is used to reference the profile when starting new browser sessions or saving session data to the profile.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: BrowserProfileConfiguration) -> dict:
    out: dict = {}
    out["profileIdentifier"] = value["profile_identifier"]
    return out


def deserialize_json(data: dict) -> BrowserProfileConfiguration:
    out: BrowserProfileConfiguration = {}  # type: ignore[typeddict-item]
    if data.get("profileIdentifier") is not None:
        out["profile_identifier"] = data["profileIdentifier"]
    else:
        out["profile_identifier"] = ""
    return out
