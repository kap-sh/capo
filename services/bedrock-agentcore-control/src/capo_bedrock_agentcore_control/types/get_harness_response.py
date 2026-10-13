"""Generated from Smithy shape ``com.amazonaws.bedrockagentcorecontrol#GetHarnessResponse``."""

from typing import TYPE_CHECKING, Any

from typing_extensions import TypedDict

from capo_bedrock_agentcore_control.errors import DeserializationError

if TYPE_CHECKING:
    import capo_bedrock_agentcore_control.types.harness


class GetHarnessResponse(TypedDict, closed=True):
    harness: "capo_bedrock_agentcore_control.types.harness.Harness"
    """<p>The harness resource.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: GetHarnessResponse) -> dict:
    out: dict = {}
    import capo_bedrock_agentcore_control.types.harness

    out["harness"] = capo_bedrock_agentcore_control.types.harness.serialize_json(
        value["harness"]
    )
    return out


def deserialize_json(data: dict) -> GetHarnessResponse:
    out: GetHarnessResponse = {}  # type: ignore[typeddict-item]
    if data.get("harness") is not None:
        import capo_bedrock_agentcore_control.types.harness

        out["harness"] = capo_bedrock_agentcore_control.types.harness.deserialize_json(
            data["harness"]
        )
    else:
        raise DeserializationError("GetHarnessResponse.harness required")
    return out


def redact_sensitive(value: GetHarnessResponse) -> dict[str, Any]:
    out: dict[str, Any] = dict(value)
    if "harness" in value:
        import capo_bedrock_agentcore_control.types.harness

        out["harness"] = capo_bedrock_agentcore_control.types.harness.redact_sensitive(
            value["harness"]
        )
    return out
