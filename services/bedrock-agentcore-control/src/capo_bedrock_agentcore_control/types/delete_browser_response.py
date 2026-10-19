"""Generated from Smithy shape ``com.amazonaws.bedrockagentcorecontrol#DeleteBrowserResponse``."""

from typing import TYPE_CHECKING

from typing_extensions import TypedDict

if TYPE_CHECKING:
    import capo_bedrock_agentcore_control.types.browser_id
    import capo_bedrock_agentcore_control.types.browser_status
    import capo_bedrock_agentcore_control.types.date_timestamp


class DeleteBrowserResponse(TypedDict, closed=True):
    browser_id: "capo_bedrock_agentcore_control.types.browser_id.BrowserId"
    """<p>The unique identifier of the deleted browser.</p>"""
    status: "capo_bedrock_agentcore_control.types.browser_status.BrowserStatus"
    """<p>The current status of the browser deletion.</p>"""
    last_updated_at: "capo_bedrock_agentcore_control.types.date_timestamp.DateTimestamp"
    """<p>The timestamp when the browser was last updated.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: DeleteBrowserResponse) -> dict:
    out: dict = {}
    out["browserId"] = value["browser_id"]
    import capo_bedrock_agentcore_control.types.browser_status

    out["status"] = capo_bedrock_agentcore_control.types.browser_status.serialize_json(
        value["status"]
    )
    import capo_bedrock_agentcore_control.types.date_timestamp

    out["lastUpdatedAt"] = (
        capo_bedrock_agentcore_control.types.date_timestamp.serialize_json(
            value["last_updated_at"]
        )
    )
    return out


def deserialize_json(data: dict) -> DeleteBrowserResponse:
    out: DeleteBrowserResponse = {}  # type: ignore[typeddict-item]
    if data.get("browserId") is not None:
        out["browser_id"] = data["browserId"]
    else:
        out["browser_id"] = ""
    if data.get("status") is not None:
        import capo_bedrock_agentcore_control.types.browser_status

        out["status"] = (
            capo_bedrock_agentcore_control.types.browser_status.deserialize_json(
                data["status"]
            )
        )
    else:
        import typing

        out["status"] = typing.cast(
            "capo_bedrock_agentcore_control.types.browser_status.BrowserStatus", ""
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
    return out
