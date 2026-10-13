"""Generated from Smithy shape ``com.amazonaws.bedrockagentcore#CreateEventOutput``."""

from typing import TYPE_CHECKING, Any

from typing_extensions import TypedDict

from capo_bedrock_agentcore.errors import DeserializationError

if TYPE_CHECKING:
    import capo_bedrock_agentcore.types.event


class CreateEventOutput(TypedDict, closed=True):
    event: "capo_bedrock_agentcore.types.event.Event"
    """<p>The event that was created.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: CreateEventOutput) -> dict:
    out: dict = {}
    import capo_bedrock_agentcore.types.event

    out["event"] = capo_bedrock_agentcore.types.event.serialize_json(value["event"])
    return out


def deserialize_json(data: dict) -> CreateEventOutput:
    out: CreateEventOutput = {}  # type: ignore[typeddict-item]
    if data.get("event") is not None:
        import capo_bedrock_agentcore.types.event

        out["event"] = capo_bedrock_agentcore.types.event.deserialize_json(
            data["event"]
        )
    else:
        raise DeserializationError("CreateEventOutput.event required")
    return out


def redact_sensitive(value: CreateEventOutput) -> dict[str, Any]:
    out: dict[str, Any] = dict(value)
    if "event" in value:
        import capo_bedrock_agentcore.types.event

        out["event"] = capo_bedrock_agentcore.types.event.redact_sensitive(
            value["event"]
        )
    return out
