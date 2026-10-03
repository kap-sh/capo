"""Generated from Smithy shape ``com.amazonaws.s3#ReplicationRule``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

from capo_s3._protocol.xml import Element, SubElement
from capo_s3.errors import DeserializationError

if TYPE_CHECKING:
    import capo_s3.types.delete_marker_replication
    import capo_s3.types.destination
    import capo_s3.types.existing_object_replication
    import capo_s3.types.id
    import capo_s3.types.prefix
    import capo_s3.types.priority
    import capo_s3.types.replication_rule_filter
    import capo_s3.types.replication_rule_status
    import capo_s3.types.source_selection_criteria


class ReplicationRule(TypedDict, closed=True):
    id: NotRequired["capo_s3.types.id.ID"]
    """<p>A unique identifier for the rule. The maximum value is 255 characters.</p>"""
    priority: NotRequired["capo_s3.types.priority.Priority"]
    """<p>The priority indicates which rule has precedence whenever two or more replication rules conflict. Amazon S3 will attempt to replicate objects according to all replication rules. However, if there are two or more rules with the same destination bucket, then objects will be replicated according to the rule with the highest priority. The higher the number, the higher the priority. </p> <p>For more information, see <a href="https://docs.aws.amazon.com/AmazonS3/latest/dev/replication.html">Replication</a> in the <i>Amazon S3 User Guide</i>.</p>"""
    prefix: NotRequired["capo_s3.types.prefix.Prefix"]
    """<p>An object key name prefix that identifies the object or objects to which the rule applies. The maximum prefix length is 1,024 characters. To include all objects in a bucket, specify an empty string. </p> <important> <p>Replacement must be made for object keys containing special characters (such as carriage returns) when using XML requests. For more information, see <a href="https://docs.aws.amazon.com/AmazonS3/latest/userguide/object-keys.html#object-key-xml-related-constraints"> XML related object key constraints</a>.</p> </important>"""
    filter: NotRequired["capo_s3.types.replication_rule_filter.ReplicationRuleFilter"]
    status: "capo_s3.types.replication_rule_status.ReplicationRuleStatus"
    """<p>Specifies whether the rule is enabled.</p>"""
    source_selection_criteria: NotRequired[
        "capo_s3.types.source_selection_criteria.SourceSelectionCriteria"
    ]
    """<p>A container that describes additional filters for identifying the source objects that you want to replicate. You can choose to enable or disable the replication of these objects. Currently, Amazon S3 supports only the filter that you can specify for objects created with server-side encryption using a customer managed key stored in Amazon Web Services Key Management Service (SSE-KMS).</p>"""
    existing_object_replication: NotRequired[
        "capo_s3.types.existing_object_replication.ExistingObjectReplication"
    ]
    """<p>Optional configuration to replicate existing source bucket objects. </p> <note> <p>This parameter is no longer supported. To replicate existing objects, see <a href="https://docs.aws.amazon.com/AmazonS3/latest/userguide/s3-batch-replication-batch.html">Replicating existing objects with S3 Batch Replication</a> in the <i>Amazon S3 User Guide</i>.</p> </note>"""
    destination: "capo_s3.types.destination.Destination"
    """<p>A container for information about the replication destination and its configurations including enabling the S3 Replication Time Control (S3 RTC).</p>"""
    delete_marker_replication: NotRequired[
        "capo_s3.types.delete_marker_replication.DeleteMarkerReplication"
    ]


# --- restXml ser/de ---
def serialize_xml(value: ReplicationRule, parent: Element, tag: str) -> None:
    el = SubElement(parent, tag)
    if "id" in value:
        SubElement(el, "ID").text = str(value["id"])
    if "priority" in value:
        SubElement(el, "Priority").text = str(value["priority"])
    if "prefix" in value:
        SubElement(el, "Prefix").text = str(value["prefix"])
    if "filter" in value:
        import capo_s3.types.replication_rule_filter

        capo_s3.types.replication_rule_filter.serialize_xml(
            value["filter"], el, "Filter"
        )
    import capo_s3.types.replication_rule_status

    capo_s3.types.replication_rule_status.serialize_xml(value["status"], el, "Status")
    if "source_selection_criteria" in value:
        import capo_s3.types.source_selection_criteria

        capo_s3.types.source_selection_criteria.serialize_xml(
            value["source_selection_criteria"], el, "SourceSelectionCriteria"
        )
    if "existing_object_replication" in value:
        import capo_s3.types.existing_object_replication

        capo_s3.types.existing_object_replication.serialize_xml(
            value["existing_object_replication"], el, "ExistingObjectReplication"
        )
    import capo_s3.types.destination

    capo_s3.types.destination.serialize_xml(value["destination"], el, "Destination")
    if "delete_marker_replication" in value:
        import capo_s3.types.delete_marker_replication

        capo_s3.types.delete_marker_replication.serialize_xml(
            value["delete_marker_replication"], el, "DeleteMarkerReplication"
        )


def deserialize_xml(el: Element) -> ReplicationRule:
    out: ReplicationRule = {}  # type: ignore[typeddict-item]
    child_id = el.find("ID")
    if child_id is not None:
        out["id"] = str(child_id.text or "")
    child_priority = el.find("Priority")
    if child_priority is not None:
        out["priority"] = int(child_priority.text or "")
    child_prefix = el.find("Prefix")
    if child_prefix is not None:
        out["prefix"] = str(child_prefix.text or "")
    child_filter = el.find("Filter")
    if child_filter is not None:
        import capo_s3.types.replication_rule_filter

        out["filter"] = capo_s3.types.replication_rule_filter.deserialize_xml(
            child_filter
        )
    child_status = el.find("Status")
    if child_status is not None:
        import capo_s3.types.replication_rule_status

        out["status"] = capo_s3.types.replication_rule_status.deserialize_xml(
            child_status
        )
    else:
        raise DeserializationError("ReplicationRule.status required")
    child_source_selection_criteria = el.find("SourceSelectionCriteria")
    if child_source_selection_criteria is not None:
        import capo_s3.types.source_selection_criteria

        out["source_selection_criteria"] = (
            capo_s3.types.source_selection_criteria.deserialize_xml(
                child_source_selection_criteria
            )
        )
    child_existing_object_replication = el.find("ExistingObjectReplication")
    if child_existing_object_replication is not None:
        import capo_s3.types.existing_object_replication

        out["existing_object_replication"] = (
            capo_s3.types.existing_object_replication.deserialize_xml(
                child_existing_object_replication
            )
        )
    child_destination = el.find("Destination")
    if child_destination is not None:
        import capo_s3.types.destination

        out["destination"] = capo_s3.types.destination.deserialize_xml(
            child_destination
        )
    else:
        raise DeserializationError("ReplicationRule.destination required")
    child_delete_marker_replication = el.find("DeleteMarkerReplication")
    if child_delete_marker_replication is not None:
        import capo_s3.types.delete_marker_replication

        out["delete_marker_replication"] = (
            capo_s3.types.delete_marker_replication.deserialize_xml(
                child_delete_marker_replication
            )
        )
    return out
