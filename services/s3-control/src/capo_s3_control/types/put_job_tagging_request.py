"""Generated from Smithy shape ``com.amazonaws.s3control#PutJobTaggingRequest``."""

from typing import TYPE_CHECKING

from typing_extensions import TypedDict

from capo_s3_control._protocol.xml import Element, SubElement

if TYPE_CHECKING:
    import capo_s3_control.types.account_id
    import capo_s3_control.types.job_id
    import capo_s3_control.types.s3_tag_set


class PutJobTaggingRequest(TypedDict, closed=True):
    account_id: "capo_s3_control.types.account_id.AccountId"
    """<p>The Amazon Web Services account ID associated with the S3 Batch Operations job.</p>"""
    job_id: "capo_s3_control.types.job_id.JobId"
    """<p>The ID for the S3 Batch Operations job whose tags you want to replace.</p>"""
    tags: "capo_s3_control.types.s3_tag_set.S3TagSet"
    """<p>The set of tags to associate with the S3 Batch Operations job.</p>"""


# --- restXml ser/de ---
def serialize_xml(value: PutJobTaggingRequest, parent: Element, tag: str) -> None:
    el = SubElement(parent, tag)
    import capo_s3_control.types.s3_tag_set

    capo_s3_control.types.s3_tag_set.serialize_xml(value["tags"], el, "Tags")


def deserialize_xml(el: Element) -> PutJobTaggingRequest:
    out: PutJobTaggingRequest = {}  # type: ignore[typeddict-item]
    child_tags = el.find("Tags")
    if child_tags is not None:
        import capo_s3_control.types.s3_tag_set

        out["tags"] = capo_s3_control.types.s3_tag_set.deserialize_xml(child_tags)
    else:
        out["tags"] = []
    return out
