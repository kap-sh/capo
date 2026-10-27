"""Generated from Smithy shape ``com.amazonaws.bedrockagentcorecontrol#Fallback``."""

from typing import TYPE_CHECKING, Any

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_bedrock_agentcore_control.types.circuit_breaker_configuration
    import capo_bedrock_agentcore_control.types.fallback_triggers
    import capo_bedrock_agentcore_control.types.target_fallbacks


class Fallback(TypedDict, closed=True):
    trigger_on: NotRequired[
        "capo_bedrock_agentcore_control.types.fallback_triggers.FallbackTriggers"
    ]
    """<p>The status codes and errors from the route's target that cause the gateway to send the request to the first fallback target. If you omit <code>triggerOn</code>, the gateway falls back on <code>5XX</code> status codes and on the <code>CONNECTION_ERROR</code>, <code>FIRST_BYTE_TIMEOUT</code>, and <code>UNROUTABLE</code> errors. If you specify <code>triggerOn</code>, only the status codes and errors that you list trigger a fallback.</p>"""
    first_byte_timeout_milliseconds: NotRequired["int"]
    """<p>The maximum time, in milliseconds, from sending the request to the route's target until the first byte of the response body arrives. If the time expires, the gateway abandons the request and treats it as a <code>FIRST_BYTE_TIMEOUT</code> error. If you don't specify a value, no timeout is enforced.</p>"""
    circuit_breaker: NotRequired[
        "capo_bedrock_agentcore_control.types.circuit_breaker_configuration.CircuitBreakerConfiguration"
    ]
    """<p>Specifies whether the gateway temporarily stops sending your requests to a failing target. The circuit breaker tracks each combination of target and model separately. With the circuit breaker enabled, the gateway skips one or more targets and models that fail repeatedly, and your requests go to the next target in the chain. The gateway always tries the last remaining target in the chain. The gateway enables the circuit breaker by default.</p>"""
    target_fallback: (
        "capo_bedrock_agentcore_control.types.target_fallbacks.TargetFallbacks"
    )
    """<p>The ordered list of fallback targets. The gateway tries each target in order until a response doesn't match that target's triggers, and returns that response to the caller. If every target fails, the gateway returns the last response. You can specify up to two fallback targets. Each combination of target and model, including the route's target, can appear only once.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: Fallback) -> dict:
    out: dict = {}
    if "trigger_on" in value:
        import capo_bedrock_agentcore_control.types.fallback_triggers

        out["triggerOn"] = (
            capo_bedrock_agentcore_control.types.fallback_triggers.serialize_json(
                value["trigger_on"]
            )
        )
    if "first_byte_timeout_milliseconds" in value:
        out["firstByteTimeoutMilliseconds"] = value["first_byte_timeout_milliseconds"]
    if "circuit_breaker" in value:
        import capo_bedrock_agentcore_control.types.circuit_breaker_configuration

        out["circuitBreaker"] = (
            capo_bedrock_agentcore_control.types.circuit_breaker_configuration.serialize_json(
                value["circuit_breaker"]
            )
        )
    import capo_bedrock_agentcore_control.types.target_fallbacks

    out["targetFallback"] = (
        capo_bedrock_agentcore_control.types.target_fallbacks.serialize_json(
            value["target_fallback"]
        )
    )
    return out


def deserialize_json(data: dict) -> Fallback:
    out: Fallback = {}  # type: ignore[typeddict-item]
    if data.get("triggerOn") is not None:
        import capo_bedrock_agentcore_control.types.fallback_triggers

        out["trigger_on"] = (
            capo_bedrock_agentcore_control.types.fallback_triggers.deserialize_json(
                data["triggerOn"]
            )
        )
    if data.get("firstByteTimeoutMilliseconds") is not None:
        out["first_byte_timeout_milliseconds"] = data["firstByteTimeoutMilliseconds"]
    if data.get("circuitBreaker") is not None:
        import capo_bedrock_agentcore_control.types.circuit_breaker_configuration

        out["circuit_breaker"] = (
            capo_bedrock_agentcore_control.types.circuit_breaker_configuration.deserialize_json(
                data["circuitBreaker"]
            )
        )
    if data.get("targetFallback") is not None:
        import capo_bedrock_agentcore_control.types.target_fallbacks

        out["target_fallback"] = (
            capo_bedrock_agentcore_control.types.target_fallbacks.deserialize_json(
                data["targetFallback"]
            )
        )
    else:
        out["target_fallback"] = []
    return out


def redact_sensitive(value: Fallback) -> dict[str, Any]:
    out: dict[str, Any] = dict(value)
    if "target_fallback" in value:
        import capo_bedrock_agentcore_control.types.target_fallbacks

        out["target_fallback"] = (
            capo_bedrock_agentcore_control.types.target_fallbacks.redact_sensitive(
                value["target_fallback"]
            )
        )
    return out
