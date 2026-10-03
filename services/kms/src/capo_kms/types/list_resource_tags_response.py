"""Generated from Smithy shape ``com.amazonaws.kms#ListResourceTagsResponse``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_kms.types.boolean_type
    import capo_kms.types.marker_type
    import capo_kms.types.tag_list


class ListResourceTagsResponse(TypedDict, closed=True):
    tags: NotRequired["capo_kms.types.tag_list.TagList"]
    """<p>A list of tags. Each tag consists of a tag key and a tag value.</p> <note> <p>Tagging or untagging a KMS key can allow or deny permission to the KMS key. For details, see <a href="https://docs.aws.amazon.com/kms/latest/developerguide/abac.html">ABAC for KMS</a> in the <i>Key Management Service Developer Guide</i>.</p> </note>"""
    next_marker: NotRequired["capo_kms.types.marker_type.MarkerType"]
    """<p>When <code>Truncated</code> is true, this element is present and contains the value to use for the <code>Marker</code> parameter in a subsequent request.</p> <p>Do not assume or infer any information from this value.</p>"""
    truncated: "capo_kms.types.boolean_type.BooleanType"
    """<p>A flag that indicates whether there are more items in the list. When this value is true, the list in this response is truncated. To get more items, pass the value of the <code>NextMarker</code> element in this response to the <code>Marker</code> parameter in a subsequent request.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: ListResourceTagsResponse) -> dict:
    out: dict = {}
    if "tags" in value:
        import capo_kms.types.tag_list

        out["Tags"] = capo_kms.types.tag_list.serialize_aws_json_1_1(value["tags"])
    if "next_marker" in value:
        out["NextMarker"] = value["next_marker"]
    out["Truncated"] = value.get("truncated", False)
    return out


def deserialize_aws_json_1_1(data: dict) -> ListResourceTagsResponse:
    out: ListResourceTagsResponse = {}  # type: ignore[typeddict-item]
    if data.get("Tags") is not None:
        import capo_kms.types.tag_list

        out["tags"] = capo_kms.types.tag_list.deserialize_aws_json_1_1(data["Tags"])
    if data.get("NextMarker") is not None:
        out["next_marker"] = data["NextMarker"]
    if data.get("Truncated") is not None:
        out["truncated"] = data["Truncated"]
    else:
        out["truncated"] = False
    return out
