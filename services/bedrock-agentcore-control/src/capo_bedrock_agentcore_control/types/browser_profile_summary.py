"""Generated from Smithy shape ``com.amazonaws.bedrockagentcorecontrol#BrowserProfileSummary``."""

from typing import TYPE_CHECKING, Any

from typing_extensions import NotRequired, TypedDict

from capo_bedrock_agentcore_control.errors import DeserializationError

if TYPE_CHECKING:
    import capo_bedrock_agentcore_control.types.browser_id
    import capo_bedrock_agentcore_control.types.browser_profile_arn
    import capo_bedrock_agentcore_control.types.browser_profile_id
    import capo_bedrock_agentcore_control.types.browser_profile_name
    import capo_bedrock_agentcore_control.types.browser_profile_status
    import capo_bedrock_agentcore_control.types.browser_session_id
    import capo_bedrock_agentcore_control.types.date_timestamp
    import capo_bedrock_agentcore_control.types.description


class BrowserProfileSummary(TypedDict, closed=True):
    profile_id: (
        "capo_bedrock_agentcore_control.types.browser_profile_id.BrowserProfileId"
    )
    """<p>The unique identifier of the browser profile.</p>"""
    profile_arn: (
        "capo_bedrock_agentcore_control.types.browser_profile_arn.BrowserProfileArn"
    )
    """<p>The Amazon Resource Name (ARN) of the browser profile.</p>"""
    name: "capo_bedrock_agentcore_control.types.browser_profile_name.BrowserProfileName"
    """<p>The name of the browser profile.</p>"""
    description: NotRequired[
        "capo_bedrock_agentcore_control.types.description.Description"
    ]
    """<p>The description of the browser profile.</p>"""
    status: "capo_bedrock_agentcore_control.types.browser_profile_status.BrowserProfileStatus"
    """<p>The current status of the browser profile. Possible values include READY, SAVING, DELETING, and DELETED.</p>"""
    created_at: "capo_bedrock_agentcore_control.types.date_timestamp.DateTimestamp"
    """<p>The timestamp when the browser profile was created.</p>"""
    last_updated_at: "capo_bedrock_agentcore_control.types.date_timestamp.DateTimestamp"
    """<p>The timestamp when the browser profile was last updated.</p>"""
    last_saved_at: NotRequired[
        "capo_bedrock_agentcore_control.types.date_timestamp.DateTimestamp"
    ]
    """<p>The timestamp when browser session data was last saved to this profile.</p>"""
    last_saved_browser_session_id: NotRequired[
        "capo_bedrock_agentcore_control.types.browser_session_id.BrowserSessionId"
    ]
    """<p>The identifier of the browser session from which data was last saved to this profile.</p>"""
    last_saved_browser_id: NotRequired[
        "capo_bedrock_agentcore_control.types.browser_id.BrowserId"
    ]
    """<p>The identifier of the browser from which data was last saved to this profile.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: BrowserProfileSummary) -> dict:
    out: dict = {}
    out["profileId"] = value["profile_id"]
    out["profileArn"] = value["profile_arn"]
    out["name"] = value["name"]
    if "description" in value:
        out["description"] = value["description"]
    import capo_bedrock_agentcore_control.types.browser_profile_status

    out["status"] = (
        capo_bedrock_agentcore_control.types.browser_profile_status.serialize_json(
            value["status"]
        )
    )
    import capo_bedrock_agentcore_control.types.date_timestamp

    out["createdAt"] = (
        capo_bedrock_agentcore_control.types.date_timestamp.serialize_json(
            value["created_at"]
        )
    )
    import capo_bedrock_agentcore_control.types.date_timestamp

    out["lastUpdatedAt"] = (
        capo_bedrock_agentcore_control.types.date_timestamp.serialize_json(
            value["last_updated_at"]
        )
    )
    if "last_saved_at" in value:
        import capo_bedrock_agentcore_control.types.date_timestamp

        out["lastSavedAt"] = (
            capo_bedrock_agentcore_control.types.date_timestamp.serialize_json(
                value["last_saved_at"]
            )
        )
    if "last_saved_browser_session_id" in value:
        out["lastSavedBrowserSessionId"] = value["last_saved_browser_session_id"]
    if "last_saved_browser_id" in value:
        out["lastSavedBrowserId"] = value["last_saved_browser_id"]
    return out


def deserialize_json(data: dict) -> BrowserProfileSummary:
    out: BrowserProfileSummary = {}  # type: ignore[typeddict-item]
    if data.get("profileId") is not None:
        out["profile_id"] = data["profileId"]
    else:
        raise DeserializationError("BrowserProfileSummary.profile_id required")
    if data.get("profileArn") is not None:
        out["profile_arn"] = data["profileArn"]
    else:
        raise DeserializationError("BrowserProfileSummary.profile_arn required")
    if data.get("name") is not None:
        out["name"] = data["name"]
    else:
        raise DeserializationError("BrowserProfileSummary.name required")
    if data.get("description") is not None:
        out["description"] = data["description"]
    if data.get("status") is not None:
        import capo_bedrock_agentcore_control.types.browser_profile_status

        out["status"] = (
            capo_bedrock_agentcore_control.types.browser_profile_status.deserialize_json(
                data["status"]
            )
        )
    else:
        raise DeserializationError("BrowserProfileSummary.status required")
    if data.get("createdAt") is not None:
        import capo_bedrock_agentcore_control.types.date_timestamp

        out["created_at"] = (
            capo_bedrock_agentcore_control.types.date_timestamp.deserialize_json(
                data["createdAt"]
            )
        )
    else:
        raise DeserializationError("BrowserProfileSummary.created_at required")
    if data.get("lastUpdatedAt") is not None:
        import capo_bedrock_agentcore_control.types.date_timestamp

        out["last_updated_at"] = (
            capo_bedrock_agentcore_control.types.date_timestamp.deserialize_json(
                data["lastUpdatedAt"]
            )
        )
    else:
        raise DeserializationError("BrowserProfileSummary.last_updated_at required")
    if data.get("lastSavedAt") is not None:
        import capo_bedrock_agentcore_control.types.date_timestamp

        out["last_saved_at"] = (
            capo_bedrock_agentcore_control.types.date_timestamp.deserialize_json(
                data["lastSavedAt"]
            )
        )
    if data.get("lastSavedBrowserSessionId") is not None:
        out["last_saved_browser_session_id"] = data["lastSavedBrowserSessionId"]
    if data.get("lastSavedBrowserId") is not None:
        out["last_saved_browser_id"] = data["lastSavedBrowserId"]
    return out


def redact_sensitive(value: BrowserProfileSummary) -> dict[str, Any]:
    out: dict[str, Any] = dict(value)
    if "description" in value:
        out["description"] = "*** Sensitive Data Redacted ***"
    return out
