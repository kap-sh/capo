"""Generated from Smithy shape ``com.amazonaws.bedrockagentcorecontrol#InterceptorPayloadFilter``."""

from typing import TYPE_CHECKING

from typing_extensions import TypedDict

if TYPE_CHECKING:
    import capo_bedrock_agentcore_control.types.interceptor_payload_exclusion_selector_list


class InterceptorPayloadFilter(TypedDict, closed=True):
    exclude: "capo_bedrock_agentcore_control.types.interceptor_payload_exclusion_selector_list.InterceptorPayloadExclusionSelectorList"
    """<p>The list of selectors that identify payload fields to exclude from the interceptor input.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: InterceptorPayloadFilter) -> dict:
    out: dict = {}
    import capo_bedrock_agentcore_control.types.interceptor_payload_exclusion_selector_list

    out["exclude"] = (
        capo_bedrock_agentcore_control.types.interceptor_payload_exclusion_selector_list.serialize_json(
            value["exclude"]
        )
    )
    return out


def deserialize_json(data: dict) -> InterceptorPayloadFilter:
    out: InterceptorPayloadFilter = {}  # type: ignore[typeddict-item]
    if data.get("exclude") is not None:
        import capo_bedrock_agentcore_control.types.interceptor_payload_exclusion_selector_list

        out["exclude"] = (
            capo_bedrock_agentcore_control.types.interceptor_payload_exclusion_selector_list.deserialize_json(
                data["exclude"]
            )
        )
    else:
        out["exclude"] = []
    return out
