"""Generated from Smithy shape ``com.amazonaws.amp#UpdateQueryLoggingConfigurationRequest``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_amp.types.idempotency_token
    import capo_amp.types.logging_destinations
    import capo_amp.types.workspace_id


class UpdateQueryLoggingConfigurationRequest(TypedDict, closed=True):
    workspace_id: "capo_amp.types.workspace_id.WorkspaceId"
    """<p>The ID of the workspace for which to update the query logging configuration.</p>"""
    destinations: "capo_amp.types.logging_destinations.LoggingDestinations"
    """<p>The destinations where query logs will be sent. Only CloudWatch Logs destination is supported. The list must contain exactly one element.</p>"""
    client_token: NotRequired["capo_amp.types.idempotency_token.IdempotencyToken"]
    """<p>(Optional) A unique, case-sensitive identifier that you can provide to ensure the idempotency of the request.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: UpdateQueryLoggingConfigurationRequest) -> dict:
    out: dict = {}
    import capo_amp.types.logging_destinations

    out["destinations"] = capo_amp.types.logging_destinations.serialize_json(
        value["destinations"]
    )
    if "client_token" in value:
        out["clientToken"] = value["client_token"]
    return out


def deserialize_json(data: dict) -> UpdateQueryLoggingConfigurationRequest:
    out: UpdateQueryLoggingConfigurationRequest = {}  # type: ignore[typeddict-item]
    if data.get("destinations") is not None:
        import capo_amp.types.logging_destinations

        out["destinations"] = capo_amp.types.logging_destinations.deserialize_json(
            data["destinations"]
        )
    else:
        out["destinations"] = []
    if data.get("clientToken") is not None:
        out["client_token"] = data["clientToken"]
    return out
