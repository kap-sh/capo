"""Generated from Smithy shape ``com.amazonaws.bedrockagentcorecontrol#CircuitBreakerConfiguration``."""

from typing import TYPE_CHECKING

from typing_extensions import TypedDict

if TYPE_CHECKING:
    import capo_bedrock_agentcore_control.types.circuit_breaker_mode


class CircuitBreakerConfiguration(TypedDict, closed=True):
    mode: "capo_bedrock_agentcore_control.types.circuit_breaker_mode.CircuitBreakerMode"
    """<p>Specifies whether you want the circuit breaker turned on. To turn it off, set this value to <code>DISABLED</code>. The default is <code>ENABLED</code>.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: CircuitBreakerConfiguration) -> dict:
    out: dict = {}
    import capo_bedrock_agentcore_control.types.circuit_breaker_mode

    out["mode"] = (
        capo_bedrock_agentcore_control.types.circuit_breaker_mode.serialize_json(
            value.get("mode", "ENABLED")
        )
    )
    return out


def deserialize_json(data: dict) -> CircuitBreakerConfiguration:
    out: CircuitBreakerConfiguration = {}  # type: ignore[typeddict-item]
    if data.get("mode") is not None:
        import capo_bedrock_agentcore_control.types.circuit_breaker_mode

        out["mode"] = (
            capo_bedrock_agentcore_control.types.circuit_breaker_mode.deserialize_json(
                data["mode"]
            )
        )
    else:
        out["mode"] = "ENABLED"
    return out
