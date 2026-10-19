"""Generated from Smithy shape ``com.amazonaws.bedrockagentcorecontrol#InterceptorInputConfiguration``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_bedrock_agentcore_control.types.interceptor_payload_filter


class InterceptorInputConfiguration(TypedDict, closed=True):
    pass_request_headers: "bool"
    """<p>Indicates whether to pass request headers as input into the interceptor. When set to true, request headers will be passed.</p>"""
    payload_filter: NotRequired[
        "capo_bedrock_agentcore_control.types.interceptor_payload_filter.InterceptorPayloadFilter"
    ]
    """<p>The filter that determines which parts of the request or response payload are passed as input to the interceptor.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: InterceptorInputConfiguration) -> dict:
    out: dict = {}
    out["passRequestHeaders"] = value["pass_request_headers"]
    if "payload_filter" in value:
        import capo_bedrock_agentcore_control.types.interceptor_payload_filter

        out["payloadFilter"] = (
            capo_bedrock_agentcore_control.types.interceptor_payload_filter.serialize_json(
                value["payload_filter"]
            )
        )
    return out


def deserialize_json(data: dict) -> InterceptorInputConfiguration:
    out: InterceptorInputConfiguration = {}  # type: ignore[typeddict-item]
    if data.get("passRequestHeaders") is not None:
        out["pass_request_headers"] = data["passRequestHeaders"]
    else:
        out["pass_request_headers"] = False
    if data.get("payloadFilter") is not None:
        import capo_bedrock_agentcore_control.types.interceptor_payload_filter

        out["payload_filter"] = (
            capo_bedrock_agentcore_control.types.interceptor_payload_filter.deserialize_json(
                data["payloadFilter"]
            )
        )
    return out
