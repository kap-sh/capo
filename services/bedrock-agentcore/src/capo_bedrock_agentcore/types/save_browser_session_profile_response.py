"""Generated from Smithy shape ``com.amazonaws.bedrockagentcore#SaveBrowserSessionProfileResponse``."""

from typing import TYPE_CHECKING

from typing_extensions import TypedDict

if TYPE_CHECKING:
    import capo_bedrock_agentcore.types.browser_profile_id
    import capo_bedrock_agentcore.types.browser_session_id
    import capo_bedrock_agentcore.types.date_timestamp


class SaveBrowserSessionProfileResponse(TypedDict, closed=True):
    profile_identifier: (
        "capo_bedrock_agentcore.types.browser_profile_id.BrowserProfileId"
    )
    """<p>The unique identifier of the saved browser profile.</p>"""
    browser_identifier: "str"
    """<p>The unique identifier of the browser associated with the session from which the profile was saved.</p>"""
    session_id: "capo_bedrock_agentcore.types.browser_session_id.BrowserSessionId"
    """<p>The unique identifier of the browser session from which the profile was saved.</p>"""
    last_updated_at: "capo_bedrock_agentcore.types.date_timestamp.DateTimestamp"
    """<p>The timestamp when the browser profile was last updated. This value is in ISO 8601 format.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: SaveBrowserSessionProfileResponse) -> dict:
    out: dict = {}
    out["profileIdentifier"] = value["profile_identifier"]
    out["browserIdentifier"] = value["browser_identifier"]
    out["sessionId"] = value["session_id"]
    import capo_bedrock_agentcore.types.date_timestamp

    out["lastUpdatedAt"] = capo_bedrock_agentcore.types.date_timestamp.serialize_json(
        value["last_updated_at"]
    )
    return out


def deserialize_json(data: dict) -> SaveBrowserSessionProfileResponse:
    out: SaveBrowserSessionProfileResponse = {}  # type: ignore[typeddict-item]
    if data.get("profileIdentifier") is not None:
        out["profile_identifier"] = data["profileIdentifier"]
    else:
        out["profile_identifier"] = ""
    if data.get("browserIdentifier") is not None:
        out["browser_identifier"] = data["browserIdentifier"]
    else:
        out["browser_identifier"] = ""
    if data.get("sessionId") is not None:
        out["session_id"] = data["sessionId"]
    else:
        out["session_id"] = ""
    if data.get("lastUpdatedAt") is not None:
        import capo_bedrock_agentcore.types.date_timestamp

        out["last_updated_at"] = (
            capo_bedrock_agentcore.types.date_timestamp.deserialize_json(
                data["lastUpdatedAt"]
            )
        )
    else:
        import datetime

        out["last_updated_at"] = datetime.datetime.fromtimestamp(
            0, tz=datetime.timezone.utc
        )
    return out
