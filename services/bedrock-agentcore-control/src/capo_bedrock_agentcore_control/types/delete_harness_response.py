"""Generated from Smithy shape ``com.amazonaws.bedrockagentcorecontrol#DeleteHarnessResponse``."""

from typing import TYPE_CHECKING, Any

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_bedrock_agentcore_control.types.harness


class DeleteHarnessResponse(TypedDict, closed=True):
    harness: NotRequired["capo_bedrock_agentcore_control.types.harness.Harness"]
    """<p>The harness that was deleted.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: DeleteHarnessResponse) -> dict:
    out: dict = {}
    if "harness" in value:
        import capo_bedrock_agentcore_control.types.harness

        out["harness"] = capo_bedrock_agentcore_control.types.harness.serialize_json(
            value["harness"]
        )
    return out


def deserialize_json(data: dict) -> DeleteHarnessResponse:
    out: DeleteHarnessResponse = {}  # type: ignore[typeddict-item]
    if data.get("harness") is not None:
        import capo_bedrock_agentcore_control.types.harness

        out["harness"] = capo_bedrock_agentcore_control.types.harness.deserialize_json(
            data["harness"]
        )
    return out


def redact_sensitive(value: DeleteHarnessResponse) -> dict[str, Any]:
    out: dict[str, Any] = dict(value)
    if "harness" in value:
        import capo_bedrock_agentcore_control.types.harness

        out["harness"] = capo_bedrock_agentcore_control.types.harness.redact_sensitive(
            value["harness"]
        )
    return out
