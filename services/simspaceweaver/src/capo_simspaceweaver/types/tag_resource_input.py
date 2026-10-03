"""Generated from Smithy shape ``com.amazonaws.simspaceweaver#TagResourceInput``."""

from typing import TYPE_CHECKING

from typing_extensions import TypedDict

from capo_simspaceweaver.errors import DeserializationError

if TYPE_CHECKING:
    import capo_simspaceweaver.types.sim_space_weaver_arn
    import capo_simspaceweaver.types.tag_map


class TagResourceInput(TypedDict, closed=True):
    resource_arn: "capo_simspaceweaver.types.sim_space_weaver_arn.SimSpaceWeaverArn"
    """<p>The Amazon Resource Name (ARN) of the resource that you want to add tags to. For more information about ARNs, see <a href="https://docs.aws.amazon.com/general/latest/gr/aws-arns-and-namespaces.html">Amazon Resource Names (ARNs)</a> in the <i>Amazon Web Services General Reference</i>.</p>"""
    tags: "capo_simspaceweaver.types.tag_map.TagMap"
    """<p>A list of tags to apply to the resource.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: TagResourceInput) -> dict:
    out: dict = {}
    import capo_simspaceweaver.types.tag_map

    out["Tags"] = capo_simspaceweaver.types.tag_map.serialize_json(value["tags"])
    return out


def deserialize_json(data: dict) -> TagResourceInput:
    out: TagResourceInput = {}  # type: ignore[typeddict-item]
    if data.get("Tags") is not None:
        import capo_simspaceweaver.types.tag_map

        out["tags"] = capo_simspaceweaver.types.tag_map.deserialize_json(data["Tags"])
    else:
        raise DeserializationError("TagResourceInput.tags required")
    return out
