"""Generated from Smithy shape ``com.amazonaws.simspaceweaver#UntagResourceInput``."""

from typing import TYPE_CHECKING

from typing_extensions import TypedDict

if TYPE_CHECKING:
    import capo_simspaceweaver.types.sim_space_weaver_arn
    import capo_simspaceweaver.types.tag_key_list


class UntagResourceInput(TypedDict, closed=True):
    resource_arn: "capo_simspaceweaver.types.sim_space_weaver_arn.SimSpaceWeaverArn"
    """<p>The Amazon Resource Name (ARN) of the resource that you want to remove tags from. For more information about ARNs, see <a href="https://docs.aws.amazon.com/general/latest/gr/aws-arns-and-namespaces.html">Amazon Resource Names (ARNs)</a> in the <i>Amazon Web Services General Reference</i>.</p>"""
    tag_keys: "capo_simspaceweaver.types.tag_key_list.TagKeyList"
    """<p>A list of tag keys to remove from the resource.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: UntagResourceInput) -> dict:
    out: dict = {}
    return out


def deserialize_json(data: dict) -> UntagResourceInput:
    out: UntagResourceInput = {}  # type: ignore[typeddict-item]
    return out
