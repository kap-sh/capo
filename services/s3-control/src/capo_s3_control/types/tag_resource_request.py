"""Generated from Smithy shape ``com.amazonaws.s3control#TagResourceRequest``."""

from typing import TYPE_CHECKING

from typing_extensions import TypedDict

from capo_s3_control._protocol.xml import Element, SubElement

if TYPE_CHECKING:
    import capo_s3_control.types.account_id
    import capo_s3_control.types.s3_resource_arn
    import capo_s3_control.types.tag_list


class TagResourceRequest(TypedDict, closed=True):
    account_id: "capo_s3_control.types.account_id.AccountId"
    """<p> The Amazon Web Services account ID that created the S3 resource that you're trying to add tags to or the requester's account ID. </p>"""
    resource_arn: "capo_s3_control.types.s3_resource_arn.S3ResourceArn"
    """<p>The Amazon Resource Name (ARN) of the S3 resource that you're applying tags to. The tagged resource can be a directory bucket, S3 Storage Lens group or S3 Access Grants instance, registered location, or grant.</p>"""
    tags: "capo_s3_control.types.tag_list.TagList"
    """<p> The Amazon Web Services resource tags that you want to add to the specified S3 resource. </p>"""


# --- restXml ser/de ---
def serialize_xml(value: TagResourceRequest, parent: Element, tag: str) -> None:
    el = SubElement(parent, tag)
    import capo_s3_control.types.tag_list

    capo_s3_control.types.tag_list.serialize_xml(value["tags"], el, "Tags")


def deserialize_xml(el: Element) -> TagResourceRequest:
    out: TagResourceRequest = {}  # type: ignore[typeddict-item]
    child_tags = el.find("Tags")
    if child_tags is not None:
        import capo_s3_control.types.tag_list

        out["tags"] = capo_s3_control.types.tag_list.deserialize_xml(child_tags)
    else:
        out["tags"] = []
    return out
