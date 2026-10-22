"""Generated from Smithy shape ``com.amazonaws.ec2#AnalysisTransitGatewayPolicyTableEntry``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

from capo_ec2._protocol.xml import Element

if TYPE_CHECKING:
    import capo_ec2.types.integer
    import capo_ec2.types.port_range
    import capo_ec2.types.string


class AnalysisTransitGatewayPolicyTableEntry(TypedDict, closed=True):
    rule_number: NotRequired["capo_ec2.types.integer.Integer"]
    """<p>The rule number for the policy table entry. Entries are evaluated in ascending order of rule number.</p>"""
    protocol: NotRequired["capo_ec2.types.string.String"]
    """<p>The protocol number. A value of <code>-1</code> means that the entry matches all protocols.</p>"""
    source_cidr: NotRequired["capo_ec2.types.string.String"]
    """<p>The source CIDR block. If this value is not present, the entry matches any source address.</p>"""
    destination_cidr: NotRequired["capo_ec2.types.string.String"]
    """<p>The destination CIDR block. If this value is not present, the entry matches any destination address.</p>"""
    source_port_range: NotRequired["capo_ec2.types.port_range.PortRange"]
    """<p>The source port range. If this value is not present, the entry matches any source port.</p>"""
    destination_port_range: NotRequired["capo_ec2.types.port_range.PortRange"]
    """<p>The destination port range. If this value is not present, the entry matches any destination port.</p>"""
    target_route_table_id: NotRequired["capo_ec2.types.string.String"]
    """<p>The ID of the transit gateway route table to which the entry routes matching traffic.</p>"""


# --- ec2Query ser/de ---
def serialize_ec2_query(
    value: AnalysisTransitGatewayPolicyTableEntry,
    pairs: list[tuple[str, str]],
    prefix: str,
) -> None:
    key_prefix = f"{prefix}." if prefix else ""
    if "rule_number" in value:
        pairs.append((f"{key_prefix}RuleNumber", str(value["rule_number"])))
    if "protocol" in value:
        pairs.append((f"{key_prefix}Protocol", str(value["protocol"])))
    if "source_cidr" in value:
        pairs.append((f"{key_prefix}SourceCidr", str(value["source_cidr"])))
    if "destination_cidr" in value:
        pairs.append((f"{key_prefix}DestinationCidr", str(value["destination_cidr"])))
    if "source_port_range" in value:
        import capo_ec2.types.port_range

        capo_ec2.types.port_range.serialize_ec2_query(
            value["source_port_range"], pairs, f"{key_prefix}SourcePortRange"
        )
    if "destination_port_range" in value:
        import capo_ec2.types.port_range

        capo_ec2.types.port_range.serialize_ec2_query(
            value["destination_port_range"], pairs, f"{key_prefix}DestinationPortRange"
        )
    if "target_route_table_id" in value:
        pairs.append(
            (f"{key_prefix}TargetRouteTableId", str(value["target_route_table_id"]))
        )


def deserialize_ec2_query(el: Element) -> AnalysisTransitGatewayPolicyTableEntry:
    out: AnalysisTransitGatewayPolicyTableEntry = {}  # type: ignore[typeddict-item]
    child_rule_number = el.find("ruleNumber")
    if child_rule_number is not None:
        out["rule_number"] = int(child_rule_number.text or "")
    child_protocol = el.find("protocol")
    if child_protocol is not None:
        out["protocol"] = str(child_protocol.text or "")
    child_source_cidr = el.find("sourceCidr")
    if child_source_cidr is not None:
        out["source_cidr"] = str(child_source_cidr.text or "")
    child_destination_cidr = el.find("destinationCidr")
    if child_destination_cidr is not None:
        out["destination_cidr"] = str(child_destination_cidr.text or "")
    child_source_port_range = el.find("sourcePortRange")
    if child_source_port_range is not None:
        import capo_ec2.types.port_range

        out["source_port_range"] = capo_ec2.types.port_range.deserialize_ec2_query(
            child_source_port_range
        )
    child_destination_port_range = el.find("destinationPortRange")
    if child_destination_port_range is not None:
        import capo_ec2.types.port_range

        out["destination_port_range"] = capo_ec2.types.port_range.deserialize_ec2_query(
            child_destination_port_range
        )
    child_target_route_table_id = el.find("targetRouteTableId")
    if child_target_route_table_id is not None:
        out["target_route_table_id"] = str(child_target_route_table_id.text or "")
    return out
