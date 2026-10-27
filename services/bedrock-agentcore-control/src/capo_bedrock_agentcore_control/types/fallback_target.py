"""Generated from Smithy shape ``com.amazonaws.bedrockagentcorecontrol#FallbackTarget``."""

from typing import TYPE_CHECKING, Any

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_bedrock_agentcore_control.types.concrete_model_id
    import capo_bedrock_agentcore_control.types.fallback_triggers
    import capo_bedrock_agentcore_control.types.target_name


class FallbackTarget(TypedDict, closed=True):
    target_name: "capo_bedrock_agentcore_control.types.target_name.TargetName"
    """<p>The name of the gateway target to fall back to. The target must be an inference target.</p>"""
    model: NotRequired[
        "capo_bedrock_agentcore_control.types.concrete_model_id.ConcreteModelId"
    ]
    """<p>The model ID to send to this fallback target. If you don't specify a model, the gateway sends the model from the original request.</p>"""
    trigger_on: NotRequired[
        "capo_bedrock_agentcore_control.types.fallback_triggers.FallbackTriggers"
    ]
    """<p>The status codes and errors from this target that cause the gateway to send the request to the next fallback target. This setting isn't inherited from the route. If you omit it, the gateway uses the default triggers: <code>5XX</code> status codes and the <code>CONNECTION_ERROR</code>, <code>FIRST_BYTE_TIMEOUT</code>, and <code>UNROUTABLE</code> errors.</p>"""
    first_byte_timeout_milliseconds: NotRequired["int"]
    """<p>The maximum time, in milliseconds, from sending the request to this target until the first byte of the response body arrives. This setting isn't inherited from the route. If you don't specify a value, no timeout is enforced.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: FallbackTarget) -> dict:
    out: dict = {}
    out["targetName"] = value["target_name"]
    if "model" in value:
        out["model"] = value["model"]
    if "trigger_on" in value:
        import capo_bedrock_agentcore_control.types.fallback_triggers

        out["triggerOn"] = (
            capo_bedrock_agentcore_control.types.fallback_triggers.serialize_json(
                value["trigger_on"]
            )
        )
    if "first_byte_timeout_milliseconds" in value:
        out["firstByteTimeoutMilliseconds"] = value["first_byte_timeout_milliseconds"]
    return out


def deserialize_json(data: dict) -> FallbackTarget:
    out: FallbackTarget = {}  # type: ignore[typeddict-item]
    if data.get("targetName") is not None:
        out["target_name"] = data["targetName"]
    else:
        out["target_name"] = ""
    if data.get("model") is not None:
        out["model"] = data["model"]
    if data.get("triggerOn") is not None:
        import capo_bedrock_agentcore_control.types.fallback_triggers

        out["trigger_on"] = (
            capo_bedrock_agentcore_control.types.fallback_triggers.deserialize_json(
                data["triggerOn"]
            )
        )
    if data.get("firstByteTimeoutMilliseconds") is not None:
        out["first_byte_timeout_milliseconds"] = data["firstByteTimeoutMilliseconds"]
    return out


def redact_sensitive(value: FallbackTarget) -> dict[str, Any]:
    out: dict[str, Any] = dict(value)
    if "target_name" in value:
        out["target_name"] = "*** Sensitive Data Redacted ***"
    return out
