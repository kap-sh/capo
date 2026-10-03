"""Generated from Smithy shape ``com.amazonaws.rds#DBSubnetGroup``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

from capo_rds._protocol.xml import Element

if TYPE_CHECKING:
    import capo_rds.types.string
    import capo_rds.types.string_list
    import capo_rds.types.subnet_list


class DBSubnetGroup(TypedDict, closed=True):
    db_subnet_group_name: NotRequired["capo_rds.types.string.String"]
    """<p>The name of the DB subnet group.</p>"""
    db_subnet_group_description: NotRequired["capo_rds.types.string.String"]
    """<p>Provides the description of the DB subnet group.</p>"""
    vpc_id: NotRequired["capo_rds.types.string.String"]
    """<p>Provides the VpcId of the DB subnet group.</p>"""
    subnet_group_status: NotRequired["capo_rds.types.string.String"]
    """<p>Provides the status of the DB subnet group.</p>"""
    subnets: NotRequired["capo_rds.types.subnet_list.SubnetList"]
    """<p>Contains a list of <code>Subnet</code> elements. The list of subnets shown here might not reflect the current state of your VPC. For the most up-to-date information, we recommend checking your VPC configuration directly.</p>"""
    db_subnet_group_arn: NotRequired["capo_rds.types.string.String"]
    """<p>The Amazon Resource Name (ARN) for the DB subnet group.</p>"""
    supported_network_types: NotRequired["capo_rds.types.string_list.StringList"]
    """<p>The network type of the DB subnet group.</p> <p>Valid values:</p> <ul> <li> <p> <code>IPV4</code> </p> </li> <li> <p> <code>DUAL</code> </p> </li> </ul> <p>A <code>DBSubnetGroup</code> can support only the IPv4 protocol or the IPv4 and the IPv6 protocols (<code>DUAL</code>).</p> <p>For more information, see <a href="https://docs.aws.amazon.com/AmazonRDS/latest/UserGuide/USER_VPC.WorkingWithRDSInstanceinaVPC.html"> Working with a DB instance in a VPC</a> in the <i>Amazon RDS User Guide.</i> </p>"""


# --- awsQuery ser/de ---
def serialize_query(
    value: DBSubnetGroup, pairs: list[tuple[str, str]], prefix: str
) -> None:
    key_prefix = f"{prefix}." if prefix else ""
    if "db_subnet_group_name" in value:
        pairs.append(
            (f"{key_prefix}DBSubnetGroupName", str(value["db_subnet_group_name"]))
        )
    if "db_subnet_group_description" in value:
        pairs.append(
            (
                f"{key_prefix}DBSubnetGroupDescription",
                str(value["db_subnet_group_description"]),
            )
        )
    if "vpc_id" in value:
        pairs.append((f"{key_prefix}VpcId", str(value["vpc_id"])))
    if "subnet_group_status" in value:
        pairs.append(
            (f"{key_prefix}SubnetGroupStatus", str(value["subnet_group_status"]))
        )
    if "subnets" in value:
        import capo_rds.types.subnet_list

        capo_rds.types.subnet_list.serialize_query(
            value["subnets"], pairs, f"{key_prefix}Subnets"
        )
    if "db_subnet_group_arn" in value:
        pairs.append(
            (f"{key_prefix}DBSubnetGroupArn", str(value["db_subnet_group_arn"]))
        )
    if "supported_network_types" in value:
        import capo_rds.types.string_list

        capo_rds.types.string_list.serialize_query(
            value["supported_network_types"],
            pairs,
            f"{key_prefix}SupportedNetworkTypes",
        )


def deserialize_query(el: Element) -> DBSubnetGroup:
    out: DBSubnetGroup = {}  # type: ignore[typeddict-item]
    child_db_subnet_group_name = el.find("DBSubnetGroupName")
    if child_db_subnet_group_name is not None:
        out["db_subnet_group_name"] = str(child_db_subnet_group_name.text or "")
    child_db_subnet_group_description = el.find("DBSubnetGroupDescription")
    if child_db_subnet_group_description is not None:
        out["db_subnet_group_description"] = str(
            child_db_subnet_group_description.text or ""
        )
    child_vpc_id = el.find("VpcId")
    if child_vpc_id is not None:
        out["vpc_id"] = str(child_vpc_id.text or "")
    child_subnet_group_status = el.find("SubnetGroupStatus")
    if child_subnet_group_status is not None:
        out["subnet_group_status"] = str(child_subnet_group_status.text or "")
    child_subnets = el.find("Subnets")
    if child_subnets is not None:
        import capo_rds.types.subnet_list

        out["subnets"] = capo_rds.types.subnet_list.deserialize_query(child_subnets)
    child_db_subnet_group_arn = el.find("DBSubnetGroupArn")
    if child_db_subnet_group_arn is not None:
        out["db_subnet_group_arn"] = str(child_db_subnet_group_arn.text or "")
    child_supported_network_types = el.find("SupportedNetworkTypes")
    if child_supported_network_types is not None:
        import capo_rds.types.string_list

        out["supported_network_types"] = capo_rds.types.string_list.deserialize_query(
            child_supported_network_types
        )
    return out
