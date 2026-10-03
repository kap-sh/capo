"""Generated from Smithy shape ``com.amazonaws.ec2#CreateTrafficMirrorFilterRuleRequest``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

from capo_ec2._protocol.xml import Element

if TYPE_CHECKING:
    import capo_ec2.types.boolean
    import capo_ec2.types.integer
    import capo_ec2.types.string
    import capo_ec2.types.tag_specification_list
    import capo_ec2.types.traffic_direction
    import capo_ec2.types.traffic_mirror_filter_id
    import capo_ec2.types.traffic_mirror_port_range_request
    import capo_ec2.types.traffic_mirror_rule_action


class CreateTrafficMirrorFilterRuleRequest(TypedDict, closed=True):
    traffic_mirror_filter_id: NotRequired[
        "capo_ec2.types.traffic_mirror_filter_id.TrafficMirrorFilterId"
    ]
    """<p>The ID of the filter that this rule is associated with.</p>"""
    traffic_direction: NotRequired["capo_ec2.types.traffic_direction.TrafficDirection"]
    """<p>The type of traffic.</p>"""
    rule_number: NotRequired["capo_ec2.types.integer.Integer"]
    """<p>The number of the Traffic Mirror rule. This number must be unique for each Traffic Mirror rule in a given direction. The rules are processed in ascending order by rule number.</p>"""
    rule_action: NotRequired[
        "capo_ec2.types.traffic_mirror_rule_action.TrafficMirrorRuleAction"
    ]
    """<p>The action to take on the filtered traffic.</p>"""
    destination_port_range: NotRequired[
        "capo_ec2.types.traffic_mirror_port_range_request.TrafficMirrorPortRangeRequest"
    ]
    """<p>The destination port range.</p>"""
    source_port_range: NotRequired[
        "capo_ec2.types.traffic_mirror_port_range_request.TrafficMirrorPortRangeRequest"
    ]
    """<p>The source port range.</p>"""
    protocol: NotRequired["capo_ec2.types.integer.Integer"]
    """<p>The protocol, for example UDP, to assign to the Traffic Mirror rule.</p> <p>For information about the protocol value, see <a href="https://www.iana.org/assignments/protocol-numbers/protocol-numbers.xhtml">Protocol Numbers</a> on the Internet Assigned Numbers Authority (IANA) website.</p>"""
    destination_cidr_block: NotRequired["capo_ec2.types.string.String"]
    """<p>The destination CIDR block to assign to the Traffic Mirror rule.</p>"""
    source_cidr_block: NotRequired["capo_ec2.types.string.String"]
    """<p>The source CIDR block to assign to the Traffic Mirror rule.</p>"""
    description: NotRequired["capo_ec2.types.string.String"]
    """<p>The description of the Traffic Mirror rule.</p>"""
    dry_run: NotRequired["capo_ec2.types.boolean.Boolean"]
    """<p>Checks whether you have the required permissions for the action, without actually making the request, and provides an error response. If you have the required permissions, the error response is <code>DryRunOperation</code>. Otherwise, it is <code>UnauthorizedOperation</code>.</p>"""
    client_token: NotRequired["capo_ec2.types.string.String"]
    """<p>Unique, case-sensitive identifier that you provide to ensure the idempotency of the request. For more information, see <a href="https://docs.aws.amazon.com/ec2/latest/devguide/ec2-api-idempotency.html">How to ensure idempotency</a>.</p>"""
    tag_specifications: NotRequired[
        "capo_ec2.types.tag_specification_list.TagSpecificationList"
    ]
    """<p>Traffic Mirroring tags specifications.</p>"""


# --- ec2Query ser/de ---
def serialize_ec2_query(
    value: CreateTrafficMirrorFilterRuleRequest,
    pairs: list[tuple[str, str]],
    prefix: str,
) -> None:
    key_prefix = f"{prefix}." if prefix else ""
    if "traffic_mirror_filter_id" in value:
        pairs.append(
            (
                f"{key_prefix}TrafficMirrorFilterId",
                str(value["traffic_mirror_filter_id"]),
            )
        )
    if "traffic_direction" in value:
        import capo_ec2.types.traffic_direction

        capo_ec2.types.traffic_direction.serialize_ec2_query(
            value["traffic_direction"], pairs, f"{key_prefix}TrafficDirection"
        )
    if "rule_number" in value:
        pairs.append((f"{key_prefix}RuleNumber", str(value["rule_number"])))
    if "rule_action" in value:
        import capo_ec2.types.traffic_mirror_rule_action

        capo_ec2.types.traffic_mirror_rule_action.serialize_ec2_query(
            value["rule_action"], pairs, f"{key_prefix}RuleAction"
        )
    if "destination_port_range" in value:
        import capo_ec2.types.traffic_mirror_port_range_request

        capo_ec2.types.traffic_mirror_port_range_request.serialize_ec2_query(
            value["destination_port_range"], pairs, f"{key_prefix}DestinationPortRange"
        )
    if "source_port_range" in value:
        import capo_ec2.types.traffic_mirror_port_range_request

        capo_ec2.types.traffic_mirror_port_range_request.serialize_ec2_query(
            value["source_port_range"], pairs, f"{key_prefix}SourcePortRange"
        )
    if "protocol" in value:
        pairs.append((f"{key_prefix}Protocol", str(value["protocol"])))
    if "destination_cidr_block" in value:
        pairs.append(
            (f"{key_prefix}DestinationCidrBlock", str(value["destination_cidr_block"]))
        )
    if "source_cidr_block" in value:
        pairs.append((f"{key_prefix}SourceCidrBlock", str(value["source_cidr_block"])))
    if "description" in value:
        pairs.append((f"{key_prefix}Description", str(value["description"])))
    if "dry_run" in value:
        pairs.append((f"{key_prefix}DryRun", "true" if value["dry_run"] else "false"))
    if "client_token" in value:
        pairs.append((f"{key_prefix}ClientToken", str(value["client_token"])))
    if "tag_specifications" in value:
        import capo_ec2.types.tag_specification_list

        capo_ec2.types.tag_specification_list.serialize_ec2_query(
            value["tag_specifications"], pairs, f"{key_prefix}TagSpecification"
        )


def deserialize_ec2_query(el: Element) -> CreateTrafficMirrorFilterRuleRequest:
    out: CreateTrafficMirrorFilterRuleRequest = {}  # type: ignore[typeddict-item]
    child_traffic_mirror_filter_id = el.find("TrafficMirrorFilterId")
    if child_traffic_mirror_filter_id is not None:
        out["traffic_mirror_filter_id"] = str(child_traffic_mirror_filter_id.text or "")
    child_traffic_direction = el.find("TrafficDirection")
    if child_traffic_direction is not None:
        import capo_ec2.types.traffic_direction

        out["traffic_direction"] = (
            capo_ec2.types.traffic_direction.deserialize_ec2_query(
                child_traffic_direction
            )
        )
    child_rule_number = el.find("RuleNumber")
    if child_rule_number is not None:
        out["rule_number"] = int(child_rule_number.text or "")
    child_rule_action = el.find("RuleAction")
    if child_rule_action is not None:
        import capo_ec2.types.traffic_mirror_rule_action

        out["rule_action"] = (
            capo_ec2.types.traffic_mirror_rule_action.deserialize_ec2_query(
                child_rule_action
            )
        )
    child_destination_port_range = el.find("DestinationPortRange")
    if child_destination_port_range is not None:
        import capo_ec2.types.traffic_mirror_port_range_request

        out["destination_port_range"] = (
            capo_ec2.types.traffic_mirror_port_range_request.deserialize_ec2_query(
                child_destination_port_range
            )
        )
    child_source_port_range = el.find("SourcePortRange")
    if child_source_port_range is not None:
        import capo_ec2.types.traffic_mirror_port_range_request

        out["source_port_range"] = (
            capo_ec2.types.traffic_mirror_port_range_request.deserialize_ec2_query(
                child_source_port_range
            )
        )
    child_protocol = el.find("Protocol")
    if child_protocol is not None:
        out["protocol"] = int(child_protocol.text or "")
    child_destination_cidr_block = el.find("DestinationCidrBlock")
    if child_destination_cidr_block is not None:
        out["destination_cidr_block"] = str(child_destination_cidr_block.text or "")
    child_source_cidr_block = el.find("SourceCidrBlock")
    if child_source_cidr_block is not None:
        out["source_cidr_block"] = str(child_source_cidr_block.text or "")
    child_description = el.find("Description")
    if child_description is not None:
        out["description"] = str(child_description.text or "")
    child_dry_run = el.find("DryRun")
    if child_dry_run is not None:
        out["dry_run"] = (child_dry_run.text or "").lower() == "true"
    child_client_token = el.find("ClientToken")
    if child_client_token is not None:
        out["client_token"] = str(child_client_token.text or "")
    child_tag_specifications = el.find("TagSpecification")
    if child_tag_specifications is not None:
        import capo_ec2.types.tag_specification_list

        out["tag_specifications"] = (
            capo_ec2.types.tag_specification_list.deserialize_ec2_query(
                child_tag_specifications
            )
        )
    return out
