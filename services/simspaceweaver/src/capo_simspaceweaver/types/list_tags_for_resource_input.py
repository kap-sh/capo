"""Generated from Smithy shape ``com.amazonaws.simspaceweaver#ListTagsForResourceInput``."""

from typing import TYPE_CHECKING

from typing_extensions import TypedDict

if TYPE_CHECKING:
    import capo_simspaceweaver.types.sim_space_weaver_arn


class ListTagsForResourceInput(TypedDict, closed=True):
    resource_arn: "capo_simspaceweaver.types.sim_space_weaver_arn.SimSpaceWeaverArn"
    """<p>The Amazon Resource Name (ARN) of the resource. For more information about ARNs, see <a href="https://docs.aws.amazon.com/general/latest/gr/aws-arns-and-namespaces.html">Amazon Resource Names (ARNs)</a> in the <i>Amazon Web Services General Reference</i>.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: ListTagsForResourceInput) -> dict:
    out: dict = {}
    return out


def deserialize_json(data: dict) -> ListTagsForResourceInput:
    out: ListTagsForResourceInput = {}  # type: ignore[typeddict-item]
    return out
