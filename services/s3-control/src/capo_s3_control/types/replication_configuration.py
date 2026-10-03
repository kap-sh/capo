"""Generated from Smithy shape ``com.amazonaws.s3control#ReplicationConfiguration``."""

from typing import TYPE_CHECKING

from typing_extensions import TypedDict

from capo_s3_control._protocol.xml import Element, SubElement
from capo_s3_control.errors import DeserializationError

if TYPE_CHECKING:
    import capo_s3_control.types.replication_rules
    import capo_s3_control.types.role


class ReplicationConfiguration(TypedDict, closed=True):
    role: "capo_s3_control.types.role.Role"
    """<p>The Amazon Resource Name (ARN) of the Identity and Access Management (IAM) role that S3 on Outposts assumes when replicating objects. For information about S3 replication on Outposts configuration, see <a href="https://docs.aws.amazon.com/AmazonS3/latest/userguide/outposts-replication-how-setup.html">Setting up replication</a> in the <i>Amazon S3 User Guide</i>.</p>"""
    rules: "capo_s3_control.types.replication_rules.ReplicationRules"
    """<p>A container for one or more replication rules. A replication configuration must have at least one rule and can contain an array of 100 rules at the most. </p>"""


# --- restXml ser/de ---
def serialize_xml(value: ReplicationConfiguration, parent: Element, tag: str) -> None:
    el = SubElement(parent, tag)
    SubElement(el, "Role").text = str(value["role"])
    import capo_s3_control.types.replication_rules

    capo_s3_control.types.replication_rules.serialize_xml(value["rules"], el, "Rules")


def deserialize_xml(el: Element) -> ReplicationConfiguration:
    out: ReplicationConfiguration = {}  # type: ignore[typeddict-item]
    child_role = el.find("Role")
    if child_role is not None:
        out["role"] = str(child_role.text or "")
    else:
        raise DeserializationError("ReplicationConfiguration.role required")
    child_rules = el.find("Rules")
    if child_rules is not None:
        import capo_s3_control.types.replication_rules

        out["rules"] = capo_s3_control.types.replication_rules.deserialize_xml(
            child_rules
        )
    else:
        raise DeserializationError("ReplicationConfiguration.rules required")
    return out
