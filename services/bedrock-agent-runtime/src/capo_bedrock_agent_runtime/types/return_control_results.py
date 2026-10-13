"""Generated from Smithy shape ``com.amazonaws.bedrockagentruntime#ReturnControlResults``."""

from typing import TYPE_CHECKING, Any

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_bedrock_agent_runtime.types.return_control_invocation_results


class ReturnControlResults(TypedDict, closed=True):
    invocation_id: NotRequired["str"]
    """<p>The action's invocation ID.</p>"""
    return_control_invocation_results: NotRequired[
        "capo_bedrock_agent_runtime.types.return_control_invocation_results.ReturnControlInvocationResults"
    ]
    """<p>The action invocation result.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: ReturnControlResults) -> dict:
    out: dict = {}
    if "invocation_id" in value:
        out["invocationId"] = value["invocation_id"]
    if "return_control_invocation_results" in value:
        import capo_bedrock_agent_runtime.types.return_control_invocation_results

        out["returnControlInvocationResults"] = (
            capo_bedrock_agent_runtime.types.return_control_invocation_results.serialize_json(
                value["return_control_invocation_results"]
            )
        )
    return out


def deserialize_json(data: dict) -> ReturnControlResults:
    out: ReturnControlResults = {}  # type: ignore[typeddict-item]
    if data.get("invocationId") is not None:
        out["invocation_id"] = data["invocationId"]
    if data.get("returnControlInvocationResults") is not None:
        import capo_bedrock_agent_runtime.types.return_control_invocation_results

        out["return_control_invocation_results"] = (
            capo_bedrock_agent_runtime.types.return_control_invocation_results.deserialize_json(
                data["returnControlInvocationResults"]
            )
        )
    return out


def redact_sensitive(value: ReturnControlResults) -> dict[str, Any]:
    out: dict[str, Any] = dict(value)
    if "return_control_invocation_results" in value:
        import capo_bedrock_agent_runtime.types.return_control_invocation_results

        out["return_control_invocation_results"] = (
            capo_bedrock_agent_runtime.types.return_control_invocation_results.redact_sensitive(
                value["return_control_invocation_results"]
            )
        )
    return out
