"""Generated from Smithy shape ``com.amazonaws.s3control#S3SetObjectRetentionOperation``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

from capo_s3_control._protocol.xml import Element, SubElement
from capo_s3_control.errors import DeserializationError

if TYPE_CHECKING:
    import capo_s3_control.types.boolean
    import capo_s3_control.types.s3_retention


class S3SetObjectRetentionOperation(TypedDict, closed=True):
    bypass_governance_retention: NotRequired["capo_s3_control.types.boolean.Boolean"]
    """<p>Indicates if the action should be applied to objects in the Batch Operations job even if they have Object Lock <code> GOVERNANCE</code> type in place.</p>"""
    retention: "capo_s3_control.types.s3_retention.S3Retention"
    """<p>Contains the Object Lock retention mode to be applied to all objects in the Batch Operations job. For more information, see <a href="https://docs.aws.amazon.com/AmazonS3/latest/dev/batch-ops-retention-date.html">Using S3 Object Lock retention with S3 Batch Operations</a> in the <i>Amazon S3 User Guide</i>.</p>"""


# --- restXml ser/de ---
def serialize_xml(
    value: S3SetObjectRetentionOperation, parent: Element, tag: str
) -> None:
    el = SubElement(parent, tag)
    if "bypass_governance_retention" in value:
        SubElement(el, "BypassGovernanceRetention").text = (
            "true" if value["bypass_governance_retention"] else "false"
        )
    import capo_s3_control.types.s3_retention

    capo_s3_control.types.s3_retention.serialize_xml(
        value["retention"], el, "Retention"
    )


def deserialize_xml(el: Element) -> S3SetObjectRetentionOperation:
    out: S3SetObjectRetentionOperation = {}  # type: ignore[typeddict-item]
    child_bypass_governance_retention = el.find("BypassGovernanceRetention")
    if child_bypass_governance_retention is not None:
        out["bypass_governance_retention"] = (
            child_bypass_governance_retention.text or ""
        ).lower() == "true"
    child_retention = el.find("Retention")
    if child_retention is not None:
        import capo_s3_control.types.s3_retention

        out["retention"] = capo_s3_control.types.s3_retention.deserialize_xml(
            child_retention
        )
    else:
        raise DeserializationError("S3SetObjectRetentionOperation.retention required")
    return out
