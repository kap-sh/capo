"""Generated from Smithy shape ``com.amazonaws.agentregistrycontrol#UntagResourceRequest``."""

from typing import TYPE_CHECKING

from typing_extensions import TypedDict

if TYPE_CHECKING:
    import capo_agent_registry_control.types.resource_arn
    import capo_agent_registry_control.types.tag_key_list


class UntagResourceRequest(TypedDict, closed=True):
    resource_arn: "capo_agent_registry_control.types.resource_arn.ResourceArn"
    """<p>The Amazon Resource Name (ARN) of the resource to remove tags from. Supported resources include registries and registry records.</p>"""
    tag_keys: "capo_agent_registry_control.types.tag_key_list.TagKeyList"
    """<p>The keys of the tags to remove from the resource. Tags with keys not included in this list remain on the resource.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: UntagResourceRequest) -> dict:
    out: dict = {}
    return out


def deserialize_json(data: dict) -> UntagResourceRequest:
    out: UntagResourceRequest = {}  # type: ignore[typeddict-item]
    return out
