"""Generated from Smithy shape ``com.amazonaws.s3#LifecycleRule``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

from capo_s3._protocol.xml import Element, SubElement
from capo_s3.errors import DeserializationError

if TYPE_CHECKING:
    import capo_s3.types.abort_incomplete_multipart_upload
    import capo_s3.types.expiration_status
    import capo_s3.types.id
    import capo_s3.types.lifecycle_expiration
    import capo_s3.types.lifecycle_rule_filter
    import capo_s3.types.noncurrent_version_expiration
    import capo_s3.types.noncurrent_version_transition_list
    import capo_s3.types.prefix
    import capo_s3.types.transition_list


class LifecycleRule(TypedDict, closed=True):
    expiration: NotRequired["capo_s3.types.lifecycle_expiration.LifecycleExpiration"]
    """<p>Specifies the expiration for the lifecycle of the object in the form of date, days and, whether the object has a delete marker.</p>"""
    id: NotRequired["capo_s3.types.id.ID"]
    """<p>Unique identifier for the rule. The value cannot be longer than 255 characters.</p>"""
    prefix: NotRequired["capo_s3.types.prefix.Prefix"]
    """<p> The general purpose bucket prefix that identifies one or more objects to which the rule applies. We recommend using <code>Filter</code> instead of <code>Prefix</code> for new PUTs. Previous configurations where a prefix is defined will continue to operate as before.</p> <important> <p>Replacement must be made for object keys containing special characters (such as carriage returns) when using XML requests. For more information, see <a href="https://docs.aws.amazon.com/AmazonS3/latest/userguide/object-keys.html#object-key-xml-related-constraints"> XML related object key constraints</a>.</p> </important>"""
    filter: NotRequired["capo_s3.types.lifecycle_rule_filter.LifecycleRuleFilter"]
    """<p>The <code>Filter</code> is used to identify objects that a Lifecycle Rule applies to. A <code>Filter</code> must have exactly one of <code>Prefix</code>, <code>Tag</code>, <code>ObjectSizeGreaterThan</code>, <code>ObjectSizeLessThan</code>, or <code>And</code> specified. <code>Filter</code> is required if the <code>LifecycleRule</code> does not contain a <code>Prefix</code> element.</p> <p>For more information about <code>Tag</code> filters, see <a href="https://docs.aws.amazon.com/AmazonS3/latest/userguide/intro-lifecycle-filters.html">Adding filters to Lifecycle rules</a> in the <i>Amazon S3 User Guide</i>.</p> <note> <p> <code>Tag</code> filters are not supported for directory buckets.</p> </note>"""
    status: "capo_s3.types.expiration_status.ExpirationStatus"
    """<p>If 'Enabled', the rule is currently being applied. If 'Disabled', the rule is not currently being applied.</p>"""
    transitions: NotRequired["capo_s3.types.transition_list.TransitionList"]
    """<p>Specifies when an Amazon S3 object transitions to a specified storage class.</p> <note> <p>This parameter applies to general purpose buckets only. It is not supported for directory bucket lifecycle configurations.</p> </note>"""
    noncurrent_version_transitions: NotRequired[
        "capo_s3.types.noncurrent_version_transition_list.NoncurrentVersionTransitionList"
    ]
    """<p>Specifies the transition rule for the lifecycle rule that describes when noncurrent objects transition to a specific storage class. If your bucket is versioning-enabled (or versioning is suspended), you can set this action to request that Amazon S3 transition noncurrent object versions to a specific storage class at a set period in the object's lifetime.</p> <note> <p>This parameter applies to general purpose buckets only. It is not supported for directory bucket lifecycle configurations.</p> </note>"""
    noncurrent_version_expiration: NotRequired[
        "capo_s3.types.noncurrent_version_expiration.NoncurrentVersionExpiration"
    ]
    abort_incomplete_multipart_upload: NotRequired[
        "capo_s3.types.abort_incomplete_multipart_upload.AbortIncompleteMultipartUpload"
    ]


# --- restXml ser/de ---
def serialize_xml(value: LifecycleRule, parent: Element, tag: str) -> None:
    el = SubElement(parent, tag)
    if "expiration" in value:
        import capo_s3.types.lifecycle_expiration

        capo_s3.types.lifecycle_expiration.serialize_xml(
            value["expiration"], el, "Expiration"
        )
    if "id" in value:
        SubElement(el, "ID").text = str(value["id"])
    if "prefix" in value:
        SubElement(el, "Prefix").text = str(value["prefix"])
    if "filter" in value:
        import capo_s3.types.lifecycle_rule_filter

        capo_s3.types.lifecycle_rule_filter.serialize_xml(value["filter"], el, "Filter")
    import capo_s3.types.expiration_status

    capo_s3.types.expiration_status.serialize_xml(value["status"], el, "Status")
    if "transitions" in value:
        import capo_s3.types.transition_list

        capo_s3.types.transition_list.serialize_xml_flat(
            value["transitions"], el, "Transition"
        )
    if "noncurrent_version_transitions" in value:
        import capo_s3.types.noncurrent_version_transition_list

        capo_s3.types.noncurrent_version_transition_list.serialize_xml_flat(
            value["noncurrent_version_transitions"], el, "NoncurrentVersionTransition"
        )
    if "noncurrent_version_expiration" in value:
        import capo_s3.types.noncurrent_version_expiration

        capo_s3.types.noncurrent_version_expiration.serialize_xml(
            value["noncurrent_version_expiration"], el, "NoncurrentVersionExpiration"
        )
    if "abort_incomplete_multipart_upload" in value:
        import capo_s3.types.abort_incomplete_multipart_upload

        capo_s3.types.abort_incomplete_multipart_upload.serialize_xml(
            value["abort_incomplete_multipart_upload"],
            el,
            "AbortIncompleteMultipartUpload",
        )


def deserialize_xml(el: Element) -> LifecycleRule:
    out: LifecycleRule = {}  # type: ignore[typeddict-item]
    child_expiration = el.find("Expiration")
    if child_expiration is not None:
        import capo_s3.types.lifecycle_expiration

        out["expiration"] = capo_s3.types.lifecycle_expiration.deserialize_xml(
            child_expiration
        )
    child_id = el.find("ID")
    if child_id is not None:
        out["id"] = str(child_id.text or "")
    child_prefix = el.find("Prefix")
    if child_prefix is not None:
        out["prefix"] = str(child_prefix.text or "")
    child_filter = el.find("Filter")
    if child_filter is not None:
        import capo_s3.types.lifecycle_rule_filter

        out["filter"] = capo_s3.types.lifecycle_rule_filter.deserialize_xml(
            child_filter
        )
    child_status = el.find("Status")
    if child_status is not None:
        import capo_s3.types.expiration_status

        out["status"] = capo_s3.types.expiration_status.deserialize_xml(child_status)
    else:
        raise DeserializationError("LifecycleRule.status required")
    if el.find("Transition") is not None:
        import capo_s3.types.transition_list

        out["transitions"] = capo_s3.types.transition_list.deserialize_xml_flat(
            el, "Transition"
        )
    if el.find("NoncurrentVersionTransition") is not None:
        import capo_s3.types.noncurrent_version_transition_list

        out["noncurrent_version_transitions"] = (
            capo_s3.types.noncurrent_version_transition_list.deserialize_xml_flat(
                el, "NoncurrentVersionTransition"
            )
        )
    child_noncurrent_version_expiration = el.find("NoncurrentVersionExpiration")
    if child_noncurrent_version_expiration is not None:
        import capo_s3.types.noncurrent_version_expiration

        out["noncurrent_version_expiration"] = (
            capo_s3.types.noncurrent_version_expiration.deserialize_xml(
                child_noncurrent_version_expiration
            )
        )
    child_abort_incomplete_multipart_upload = el.find("AbortIncompleteMultipartUpload")
    if child_abort_incomplete_multipart_upload is not None:
        import capo_s3.types.abort_incomplete_multipart_upload

        out["abort_incomplete_multipart_upload"] = (
            capo_s3.types.abort_incomplete_multipart_upload.deserialize_xml(
                child_abort_incomplete_multipart_upload
            )
        )
    return out
