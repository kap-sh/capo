"""Generated from Smithy shape ``com.amazonaws.bedrockagentcorecontrol#StickinessConfiguration``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_bedrock_agentcore_control.types.composite_identifier_list
    import capo_bedrock_agentcore_control.types.stickiness_timeout


class StickinessConfiguration(TypedDict, closed=True):
    identifier: "str"
    """<p>The expression that identifies where to extract the session identifier from the request (for example, <code>$context.header.x-session-id</code>).</p>"""
    timeout: NotRequired[
        "capo_bedrock_agentcore_control.types.stickiness_timeout.StickinessTimeout"
    ]
    """<p>The session stickiness timeout, in seconds. After this duration of inactivity, the session affinity expires. Valid values range from 1 to 86400.</p>"""
    composite_identifier: NotRequired[
        "capo_bedrock_agentcore_control.types.composite_identifier_list.CompositeIdentifierList"
    ]
    """<p>Additional headers to include in session affinity routing. When set, requests are only considered part of the same session if both the <code>identifier</code> and all composite identifier values match.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: StickinessConfiguration) -> dict:
    out: dict = {}
    out["identifier"] = value["identifier"]
    if "timeout" in value:
        out["timeout"] = value["timeout"]
    if "composite_identifier" in value:
        import capo_bedrock_agentcore_control.types.composite_identifier_list

        out["compositeIdentifier"] = (
            capo_bedrock_agentcore_control.types.composite_identifier_list.serialize_json(
                value["composite_identifier"]
            )
        )
    return out


def deserialize_json(data: dict) -> StickinessConfiguration:
    out: StickinessConfiguration = {}  # type: ignore[typeddict-item]
    if data.get("identifier") is not None:
        out["identifier"] = data["identifier"]
    else:
        out["identifier"] = ""
    if data.get("timeout") is not None:
        out["timeout"] = data["timeout"]
    if data.get("compositeIdentifier") is not None:
        import capo_bedrock_agentcore_control.types.composite_identifier_list

        out["composite_identifier"] = (
            capo_bedrock_agentcore_control.types.composite_identifier_list.deserialize_json(
                data["compositeIdentifier"]
            )
        )
    return out
