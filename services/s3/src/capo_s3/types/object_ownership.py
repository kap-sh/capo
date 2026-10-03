"""Generated from Smithy shape ``com.amazonaws.s3#ObjectOwnership``."""

from typing import Literal, TypeAlias, cast

from capo_s3._protocol.xml import Element, SubElement

"""<p>The container element for object ownership for a bucket's ownership controls.</p> <p> <code>BucketOwnerPreferred</code> - Objects uploaded to the bucket change ownership to the bucket owner if the objects are uploaded with the <code>bucket-owner-full-control</code> canned ACL.</p> <p> <code>ObjectWriter</code> - The uploading account will own the object if the object is uploaded with the <code>bucket-owner-full-control</code> canned ACL.</p> <p> <code>BucketOwnerEnforced</code> - Access control lists (ACLs) are disabled and no longer affect permissions. The bucket owner automatically owns and has full control over every object in the bucket. The bucket only accepts PUT requests that don't specify an ACL or specify bucket owner full control ACLs (such as the predefined <code>bucket-owner-full-control</code> canned ACL or a custom ACL in XML format that grants the same permissions).</p> <p>By default, <code>ObjectOwnership</code> is set to <code>BucketOwnerEnforced</code> and ACLs are disabled. We recommend keeping ACLs disabled, except in uncommon use cases where you must control access for each object individually. For more information about S3 Object Ownership, see <a href="https://docs.aws.amazon.com/AmazonS3/latest/userguide/about-object-ownership.html">Controlling ownership of objects and disabling ACLs for your bucket</a> in the <i>Amazon S3 User Guide</i>. </p> <note> <p>This functionality is not supported for directory buckets. Directory buckets use the bucket owner enforced setting for S3 Object Ownership.</p> </note>"""
ObjectOwnership: TypeAlias = Literal[
    "BucketOwnerPreferred",
    "ObjectWriter",
    "BucketOwnerEnforced",
]


# --- restXml ser/de ---
def to_xml_text(value: ObjectOwnership) -> str:
    return value


def from_xml_text(text: str) -> ObjectOwnership:
    return cast(ObjectOwnership, text)


def serialize_xml(value: ObjectOwnership, parent: Element, tag: str) -> None:
    SubElement(parent, tag).text = to_xml_text(value)


def deserialize_xml(el: Element) -> ObjectOwnership:
    return from_xml_text(el.text or "")
