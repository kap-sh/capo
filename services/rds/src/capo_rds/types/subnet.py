"""Generated from Smithy shape ``com.amazonaws.rds#Subnet``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

from capo_rds._protocol.xml import Element

if TYPE_CHECKING:
    import capo_rds.types.availability_zone
    import capo_rds.types.outpost
    import capo_rds.types.string


class Subnet(TypedDict, closed=True):
    subnet_identifier: NotRequired["capo_rds.types.string.String"]
    """<p>The identifier of the subnet.</p>"""
    subnet_availability_zone: NotRequired[
        "capo_rds.types.availability_zone.AvailabilityZone"
    ]
    subnet_outpost: NotRequired["capo_rds.types.outpost.Outpost"]
    """<p>If the subnet is associated with an Outpost, this value specifies the Outpost.</p> <p>For more information about RDS on Outposts, see <a href="https://docs.aws.amazon.com/AmazonRDS/latest/UserGuide/rds-on-outposts.html">Amazon RDS on Amazon Web Services Outposts</a> in the <i>Amazon RDS User Guide.</i> </p>"""
    subnet_status: NotRequired["capo_rds.types.string.String"]
    """<p>The status of the subnet.</p>"""


# --- awsQuery ser/de ---
def serialize_query(value: Subnet, pairs: list[tuple[str, str]], prefix: str) -> None:
    key_prefix = f"{prefix}." if prefix else ""
    if "subnet_identifier" in value:
        pairs.append((f"{key_prefix}SubnetIdentifier", str(value["subnet_identifier"])))
    if "subnet_availability_zone" in value:
        import capo_rds.types.availability_zone

        capo_rds.types.availability_zone.serialize_query(
            value["subnet_availability_zone"],
            pairs,
            f"{key_prefix}SubnetAvailabilityZone",
        )
    if "subnet_outpost" in value:
        import capo_rds.types.outpost

        capo_rds.types.outpost.serialize_query(
            value["subnet_outpost"], pairs, f"{key_prefix}SubnetOutpost"
        )
    if "subnet_status" in value:
        pairs.append((f"{key_prefix}SubnetStatus", str(value["subnet_status"])))


def deserialize_query(el: Element) -> Subnet:
    out: Subnet = {}  # type: ignore[typeddict-item]
    child_subnet_identifier = el.find("SubnetIdentifier")
    if child_subnet_identifier is not None:
        out["subnet_identifier"] = str(child_subnet_identifier.text or "")
    child_subnet_availability_zone = el.find("SubnetAvailabilityZone")
    if child_subnet_availability_zone is not None:
        import capo_rds.types.availability_zone

        out["subnet_availability_zone"] = (
            capo_rds.types.availability_zone.deserialize_query(
                child_subnet_availability_zone
            )
        )
    child_subnet_outpost = el.find("SubnetOutpost")
    if child_subnet_outpost is not None:
        import capo_rds.types.outpost

        out["subnet_outpost"] = capo_rds.types.outpost.deserialize_query(
            child_subnet_outpost
        )
    child_subnet_status = el.find("SubnetStatus")
    if child_subnet_status is not None:
        out["subnet_status"] = str(child_subnet_status.text or "")
    return out
