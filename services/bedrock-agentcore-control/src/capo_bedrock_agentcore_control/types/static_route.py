"""Generated from Smithy shape ``com.amazonaws.bedrockagentcorecontrol#StaticRoute``."""

from typing import TYPE_CHECKING, Any

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_bedrock_agentcore_control.types.concrete_model_id
    import capo_bedrock_agentcore_control.types.fallback
    import capo_bedrock_agentcore_control.types.target_name


class StaticRoute(TypedDict, closed=True):
    target_name: "capo_bedrock_agentcore_control.types.target_name.TargetName"
    """<p>The name of the target to route requests to.</p>"""
    model: NotRequired[
        "capo_bedrock_agentcore_control.types.concrete_model_id.ConcreteModelId"
    ]
    """<p>The model ID to send to the target. Supported only for inference targets. If you don't specify a model, the gateway sends the model from the original request.</p>"""
    fallback: NotRequired["capo_bedrock_agentcore_control.types.fallback.Fallback"]
    """<p>The fallback configuration for this route. Supported only for inference targets.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: StaticRoute) -> dict:
    out: dict = {}
    out["targetName"] = value["target_name"]
    if "model" in value:
        out["model"] = value["model"]
    if "fallback" in value:
        import capo_bedrock_agentcore_control.types.fallback

        out["fallback"] = capo_bedrock_agentcore_control.types.fallback.serialize_json(
            value["fallback"]
        )
    return out


def deserialize_json(data: dict) -> StaticRoute:
    out: StaticRoute = {}  # type: ignore[typeddict-item]
    if data.get("targetName") is not None:
        out["target_name"] = data["targetName"]
    else:
        out["target_name"] = ""
    if data.get("model") is not None:
        out["model"] = data["model"]
    if data.get("fallback") is not None:
        import capo_bedrock_agentcore_control.types.fallback

        out["fallback"] = (
            capo_bedrock_agentcore_control.types.fallback.deserialize_json(
                data["fallback"]
            )
        )
    return out


def redact_sensitive(value: StaticRoute) -> dict[str, Any]:
    out: dict[str, Any] = dict(value)
    if "target_name" in value:
        out["target_name"] = "*** Sensitive Data Redacted ***"
    if "fallback" in value:
        import capo_bedrock_agentcore_control.types.fallback

        out["fallback"] = (
            capo_bedrock_agentcore_control.types.fallback.redact_sensitive(
                value["fallback"]
            )
        )
    return out
