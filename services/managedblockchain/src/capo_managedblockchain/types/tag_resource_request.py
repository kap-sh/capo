"""Generated from Smithy shape ``com.amazonaws.managedblockchain#TagResourceRequest``."""

from typing import TYPE_CHECKING

from typing_extensions import TypedDict

from capo_managedblockchain.errors import DeserializationError

if TYPE_CHECKING:
    import capo_managedblockchain.types.arn_string
    import capo_managedblockchain.types.input_tag_map


class TagResourceRequest(TypedDict, closed=True):
    resource_arn: "capo_managedblockchain.types.arn_string.ArnString"
    """<p>The Amazon Resource Name (ARN) of the resource. For more information about ARNs and their format, see <a href="https://docs.aws.amazon.com/general/latest/gr/aws-arns-and-namespaces.html">Amazon Resource Names (ARNs)</a> in the <i>Amazon Web Services General Reference</i>.</p>"""
    tags: "capo_managedblockchain.types.input_tag_map.InputTagMap"
    """<p>The tags to assign to the specified resource. Tag values can be empty, for example, <code>"MyTagKey" : ""</code>. You can specify multiple key-value pairs in a single request, with an overall maximum of 50 tags added to each resource.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: TagResourceRequest) -> dict:
    out: dict = {}
    import capo_managedblockchain.types.input_tag_map

    out["Tags"] = capo_managedblockchain.types.input_tag_map.serialize_json(
        value["tags"]
    )
    return out


def deserialize_json(data: dict) -> TagResourceRequest:
    out: TagResourceRequest = {}  # type: ignore[typeddict-item]
    if data.get("Tags") is not None:
        import capo_managedblockchain.types.input_tag_map

        out["tags"] = capo_managedblockchain.types.input_tag_map.deserialize_json(
            data["Tags"]
        )
    else:
        raise DeserializationError("TagResourceRequest.tags required")
    return out
