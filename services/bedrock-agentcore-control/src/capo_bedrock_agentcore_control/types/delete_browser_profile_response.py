"""Generated from Smithy shape ``com.amazonaws.bedrockagentcorecontrol#DeleteBrowserProfileResponse``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_bedrock_agentcore_control.types.browser_profile_arn
    import capo_bedrock_agentcore_control.types.browser_profile_id
    import capo_bedrock_agentcore_control.types.browser_profile_status
    import capo_bedrock_agentcore_control.types.date_timestamp


class DeleteBrowserProfileResponse(TypedDict, closed=True):
    profile_id: (
        "capo_bedrock_agentcore_control.types.browser_profile_id.BrowserProfileId"
    )
    """<p>The unique identifier of the deleted browser profile.</p>"""
    profile_arn: (
        "capo_bedrock_agentcore_control.types.browser_profile_arn.BrowserProfileArn"
    )
    """<p>The Amazon Resource Name (ARN) of the deleted browser profile.</p>"""
    status: "capo_bedrock_agentcore_control.types.browser_profile_status.BrowserProfileStatus"
    """<p>The current status of the browser profile deletion.</p>"""
    last_updated_at: "capo_bedrock_agentcore_control.types.date_timestamp.DateTimestamp"
    """<p>The timestamp when the browser profile was last updated.</p>"""
    last_saved_at: NotRequired[
        "capo_bedrock_agentcore_control.types.date_timestamp.DateTimestamp"
    ]
    """<p>The timestamp when browser session data was last saved to this profile before deletion.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: DeleteBrowserProfileResponse) -> dict:
    out: dict = {}
    out["profileId"] = value["profile_id"]
    out["profileArn"] = value["profile_arn"]
    import capo_bedrock_agentcore_control.types.browser_profile_status

    out["status"] = (
        capo_bedrock_agentcore_control.types.browser_profile_status.serialize_json(
            value["status"]
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
    return out


def deserialize_json(data: dict) -> DeleteBrowserProfileResponse:
    out: DeleteBrowserProfileResponse = {}  # type: ignore[typeddict-item]
    if data.get("profileId") is not None:
        out["profile_id"] = data["profileId"]
    else:
        out["profile_id"] = ""
    if data.get("profileArn") is not None:
        out["profile_arn"] = data["profileArn"]
    else:
        out["profile_arn"] = ""
    if data.get("status") is not None:
        import capo_bedrock_agentcore_control.types.browser_profile_status

        out["status"] = (
            capo_bedrock_agentcore_control.types.browser_profile_status.deserialize_json(
                data["status"]
            )
        )
    else:
        import typing

        out["status"] = typing.cast(
            "capo_bedrock_agentcore_control.types.browser_profile_status.BrowserProfileStatus",
            "",
        )
    if data.get("lastUpdatedAt") is not None:
        import capo_bedrock_agentcore_control.types.date_timestamp

        out["last_updated_at"] = (
            capo_bedrock_agentcore_control.types.date_timestamp.deserialize_json(
                data["lastUpdatedAt"]
            )
        )
    else:
        import datetime

        out["last_updated_at"] = datetime.datetime.fromtimestamp(
            0, tz=datetime.timezone.utc
        )
    if data.get("lastSavedAt") is not None:
        import capo_bedrock_agentcore_control.types.date_timestamp

        out["last_saved_at"] = (
            capo_bedrock_agentcore_control.types.date_timestamp.deserialize_json(
                data["lastSavedAt"]
            )
        )
    return out
