"""Generated from Smithy shape ``com.amazonaws.bedrockagentcorecontrol#CreateBrowserProfileResponse``."""

from typing import TYPE_CHECKING

from typing_extensions import TypedDict

if TYPE_CHECKING:
    import capo_bedrock_agentcore_control.types.browser_profile_arn
    import capo_bedrock_agentcore_control.types.browser_profile_id
    import capo_bedrock_agentcore_control.types.browser_profile_status
    import capo_bedrock_agentcore_control.types.date_timestamp


class CreateBrowserProfileResponse(TypedDict, closed=True):
    profile_id: (
        "capo_bedrock_agentcore_control.types.browser_profile_id.BrowserProfileId"
    )
    """<p>The unique identifier of the created browser profile.</p>"""
    profile_arn: (
        "capo_bedrock_agentcore_control.types.browser_profile_arn.BrowserProfileArn"
    )
    """<p>The Amazon Resource Name (ARN) of the created browser profile.</p>"""
    created_at: "capo_bedrock_agentcore_control.types.date_timestamp.DateTimestamp"
    """<p>The timestamp when the browser profile was created.</p>"""
    status: "capo_bedrock_agentcore_control.types.browser_profile_status.BrowserProfileStatus"
    """<p>The current status of the browser profile.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: CreateBrowserProfileResponse) -> dict:
    out: dict = {}
    out["profileId"] = value["profile_id"]
    out["profileArn"] = value["profile_arn"]
    import capo_bedrock_agentcore_control.types.date_timestamp

    out["createdAt"] = (
        capo_bedrock_agentcore_control.types.date_timestamp.serialize_json(
            value["created_at"]
        )
    )
    import capo_bedrock_agentcore_control.types.browser_profile_status

    out["status"] = (
        capo_bedrock_agentcore_control.types.browser_profile_status.serialize_json(
            value["status"]
        )
    )
    return out


def deserialize_json(data: dict) -> CreateBrowserProfileResponse:
    out: CreateBrowserProfileResponse = {}  # type: ignore[typeddict-item]
    if data.get("profileId") is not None:
        out["profile_id"] = data["profileId"]
    else:
        out["profile_id"] = ""
    if data.get("profileArn") is not None:
        out["profile_arn"] = data["profileArn"]
    else:
        out["profile_arn"] = ""
    if data.get("createdAt") is not None:
        import capo_bedrock_agentcore_control.types.date_timestamp

        out["created_at"] = (
            capo_bedrock_agentcore_control.types.date_timestamp.deserialize_json(
                data["createdAt"]
            )
        )
    else:
        import datetime

        out["created_at"] = datetime.datetime.fromtimestamp(0, tz=datetime.timezone.utc)
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
    return out
