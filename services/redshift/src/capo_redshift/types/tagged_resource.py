"""Generated from Smithy shape ``com.amazonaws.redshift#TaggedResource``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

from capo_redshift._protocol.xml import Element

if TYPE_CHECKING:
    import capo_redshift.types.string
    import capo_redshift.types.tag


class TaggedResource(TypedDict, closed=True):
    tag: NotRequired["capo_redshift.types.tag.Tag"]
    """<p>The tag for the resource.</p>"""
    resource_name: NotRequired["capo_redshift.types.string.String"]
    """<p>The Amazon Resource Name (ARN) with which the tag is associated, for example: <code>arn:aws:redshift:us-east-2:123456789:cluster:t1</code>.</p>"""
    resource_type: NotRequired["capo_redshift.types.string.String"]
    """<p>The type of resource with which the tag is associated. Valid resource types are: </p> <ul> <li> <p>Cluster</p> </li> <li> <p>CIDR/IP</p> </li> <li> <p>EC2 security group</p> </li> <li> <p>Snapshot</p> </li> <li> <p>Cluster security group</p> </li> <li> <p>Subnet group</p> </li> <li> <p>HSM connection</p> </li> <li> <p>HSM certificate</p> </li> <li> <p>Parameter group</p> </li> </ul> <p>For more information about Amazon Redshift resource types and constructing ARNs, go to <a href="https://docs.aws.amazon.com/redshift/latest/mgmt/redshift-iam-access-control-overview.html#redshift-iam-access-control-specify-actions">Constructing an Amazon Redshift Amazon Resource Name (ARN)</a> in the Amazon Redshift Cluster Management Guide. </p>"""


# --- awsQuery ser/de ---
def serialize_query(
    value: TaggedResource, pairs: list[tuple[str, str]], prefix: str
) -> None:
    key_prefix = f"{prefix}." if prefix else ""
    if "tag" in value:
        import capo_redshift.types.tag

        capo_redshift.types.tag.serialize_query(value["tag"], pairs, f"{key_prefix}Tag")
    if "resource_name" in value:
        pairs.append((f"{key_prefix}ResourceName", str(value["resource_name"])))
    if "resource_type" in value:
        pairs.append((f"{key_prefix}ResourceType", str(value["resource_type"])))


def deserialize_query(el: Element) -> TaggedResource:
    out: TaggedResource = {}  # type: ignore[typeddict-item]
    child_tag = el.find("Tag")
    if child_tag is not None:
        import capo_redshift.types.tag

        out["tag"] = capo_redshift.types.tag.deserialize_query(child_tag)
    child_resource_name = el.find("ResourceName")
    if child_resource_name is not None:
        out["resource_name"] = str(child_resource_name.text or "")
    child_resource_type = el.find("ResourceType")
    if child_resource_type is not None:
        out["resource_type"] = str(child_resource_type.text or "")
    return out
