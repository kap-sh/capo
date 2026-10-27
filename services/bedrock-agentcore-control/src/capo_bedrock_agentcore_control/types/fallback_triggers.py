"""Generated from Smithy shape ``com.amazonaws.bedrockagentcorecontrol#FallbackTriggers``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_bedrock_agentcore_control.types.error_status_code_patterns
    import capo_bedrock_agentcore_control.types.fallback_errors


class FallbackTriggers(TypedDict, closed=True):
    status_codes: NotRequired[
        "capo_bedrock_agentcore_control.types.error_status_code_patterns.ErrorStatusCodePatterns"
    ]
    """<p>The HTTP status codes returned by the target that trigger a fallback. You can specify the following:</p> <ul> <li> <p>An exact status code – A three-digit code, such as <code>429</code>.</p> </li> <li> <p>A class of status codes – The first digit followed by <code>XX</code>, such as <code>5XX</code>, which matches every code from 500 to 599.</p> </li> </ul> <p>Only 4XX and 5XX codes are supported. Throttling by the gateway itself doesn't trigger a fallback.</p>"""
    errors: NotRequired[
        "capo_bedrock_agentcore_control.types.fallback_errors.FallbackErrors"
    ]
    """<p>The errors that trigger a fallback. You can specify the following:</p> <ul> <li> <p> <code>CONNECTION_ERROR</code> – The gateway couldn't connect to the target because the connection was refused, reset, or timed out. The request didn't reach the target.</p> </li> <li> <p> <code>FIRST_BYTE_TIMEOUT</code> – The target accepted the connection but didn't return the first byte of the response within <code>firstByteTimeoutMilliseconds</code>. The gateway abandons the request before any of the response reaches you.</p> </li> <li> <p> <code>UNROUTABLE</code> – The gateway couldn't route the request to the target, for example because the target doesn't exist or doesn't support the request path. These errors don't count toward the circuit breaker.</p> </li> </ul>"""


# --- restJson1 ser/de ---
def serialize_json(value: FallbackTriggers) -> dict:
    out: dict = {}
    if "status_codes" in value:
        import capo_bedrock_agentcore_control.types.error_status_code_patterns

        out["statusCodes"] = (
            capo_bedrock_agentcore_control.types.error_status_code_patterns.serialize_json(
                value["status_codes"]
            )
        )
    if "errors" in value:
        import capo_bedrock_agentcore_control.types.fallback_errors

        out["errors"] = (
            capo_bedrock_agentcore_control.types.fallback_errors.serialize_json(
                value["errors"]
            )
        )
    return out


def deserialize_json(data: dict) -> FallbackTriggers:
    out: FallbackTriggers = {}  # type: ignore[typeddict-item]
    if data.get("statusCodes") is not None:
        import capo_bedrock_agentcore_control.types.error_status_code_patterns

        out["status_codes"] = (
            capo_bedrock_agentcore_control.types.error_status_code_patterns.deserialize_json(
                data["statusCodes"]
            )
        )
    if data.get("errors") is not None:
        import capo_bedrock_agentcore_control.types.fallback_errors

        out["errors"] = (
            capo_bedrock_agentcore_control.types.fallback_errors.deserialize_json(
                data["errors"]
            )
        )
    return out
