"""Generated from Smithy shape ``com.amazonaws.bedrockagentcorecontrol#UpdateHarnessResponse``."""

from typing import TYPE_CHECKING, Any

from typing_extensions import TypedDict

from capo_bedrock_agentcore_control.errors import DeserializationError

if TYPE_CHECKING:
    import capo_bedrock_agentcore_control.types.harness


class UpdateHarnessResponse(TypedDict, closed=True):
    harness: "capo_bedrock_agentcore_control.types.harness.Harness"
    """<p>The updated harness.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: UpdateHarnessResponse) -> dict:
    out: dict = {}
    import capo_bedrock_agentcore_control.types.harness

    out["harness"] = capo_bedrock_agentcore_control.types.harness.serialize_json(
        value["harness"]
    )
    return out


def deserialize_json(data: dict) -> UpdateHarnessResponse:
    out: UpdateHarnessResponse = {}  # type: ignore[typeddict-item]
    if data.get("harness") is not None:
        import capo_bedrock_agentcore_control.types.harness

        out["harness"] = capo_bedrock_agentcore_control.types.harness.deserialize_json(
            data["harness"]
        )
    else:
        raise DeserializationError("UpdateHarnessResponse.harness required")
    return out


def redact_sensitive(value: UpdateHarnessResponse) -> dict[str, Any]:
    out: dict[str, Any] = dict(value)
    if "harness" in value:
        import capo_bedrock_agentcore_control.types.harness

        out["harness"] = capo_bedrock_agentcore_control.types.harness.redact_sensitive(
            value["harness"]
        )
    return out
