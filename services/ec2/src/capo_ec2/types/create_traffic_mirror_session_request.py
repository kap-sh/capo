"""Generated from Smithy shape ``com.amazonaws.ec2#CreateTrafficMirrorSessionRequest``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

from capo_ec2._protocol.xml import Element

if TYPE_CHECKING:
    import capo_ec2.types.boolean
    import capo_ec2.types.integer
    import capo_ec2.types.network_interface_id
    import capo_ec2.types.string
    import capo_ec2.types.tag_specification_list
    import capo_ec2.types.traffic_mirror_filter_id
    import capo_ec2.types.traffic_mirror_target_id


class CreateTrafficMirrorSessionRequest(TypedDict, closed=True):
    network_interface_id: NotRequired[
        "capo_ec2.types.network_interface_id.NetworkInterfaceId"
    ]
    """<p>The ID of the source network interface.</p>"""
    traffic_mirror_target_id: NotRequired[
        "capo_ec2.types.traffic_mirror_target_id.TrafficMirrorTargetId"
    ]
    """<p>The ID of the Traffic Mirror target.</p>"""
    traffic_mirror_filter_id: NotRequired[
        "capo_ec2.types.traffic_mirror_filter_id.TrafficMirrorFilterId"
    ]
    """<p>The ID of the Traffic Mirror filter.</p>"""
    packet_length: NotRequired["capo_ec2.types.integer.Integer"]
    """<p>The number of bytes in each packet to mirror. These are bytes after the VXLAN header. Do not specify this parameter when you want to mirror the entire packet. To mirror a subset of the packet, set this to the length (in bytes) that you want to mirror. For example, if you set this value to 100, then the first 100 bytes that meet the filter criteria are copied to the target.</p> <p>If you do not want to mirror the entire packet, use the <code>PacketLength</code> parameter to specify the number of bytes in each packet to mirror.</p> <p>For sessions with Network Load Balancer (NLB) Traffic Mirror targets the default <code>PacketLength</code> will be set to 8500. Valid values are 1-8500. Setting a <code>PacketLength</code> greater than 8500 will result in an error response.</p>"""
    session_number: NotRequired["capo_ec2.types.integer.Integer"]
    """<p>The session number determines the order in which sessions are evaluated when an interface is used by multiple sessions. The first session with a matching filter is the one that mirrors the packets.</p> <p>Valid values are 1-32766.</p>"""
    virtual_network_id: NotRequired["capo_ec2.types.integer.Integer"]
    """<p>The VXLAN ID for the Traffic Mirror session. For more information about the VXLAN protocol, see <a href="https://datatracker.ietf.org/doc/html/rfc7348">RFC 7348</a>. If you do not specify a <code>VirtualNetworkId</code>, an account-wide unique ID is chosen at random.</p>"""
    description: NotRequired["capo_ec2.types.string.String"]
    """<p>The description of the Traffic Mirror session.</p>"""
    tag_specifications: NotRequired[
        "capo_ec2.types.tag_specification_list.TagSpecificationList"
    ]
    """<p>The tags to assign to a Traffic Mirror session.</p>"""
    dry_run: NotRequired["capo_ec2.types.boolean.Boolean"]
    """<p>Checks whether you have the required permissions for the action, without actually making the request, and provides an error response. If you have the required permissions, the error response is <code>DryRunOperation</code>. Otherwise, it is <code>UnauthorizedOperation</code>.</p>"""
    client_token: NotRequired["capo_ec2.types.string.String"]
    """<p>Unique, case-sensitive identifier that you provide to ensure the idempotency of the request. For more information, see <a href="https://docs.aws.amazon.com/ec2/latest/devguide/ec2-api-idempotency.html">How to ensure idempotency</a>.</p>"""


# --- ec2Query ser/de ---
def serialize_ec2_query(
    value: CreateTrafficMirrorSessionRequest, pairs: list[tuple[str, str]], prefix: str
) -> None:
    key_prefix = f"{prefix}." if prefix else ""
    if "network_interface_id" in value:
        pairs.append(
            (f"{key_prefix}NetworkInterfaceId", str(value["network_interface_id"]))
        )
    if "traffic_mirror_target_id" in value:
        pairs.append(
            (
                f"{key_prefix}TrafficMirrorTargetId",
                str(value["traffic_mirror_target_id"]),
            )
        )
    if "traffic_mirror_filter_id" in value:
        pairs.append(
            (
                f"{key_prefix}TrafficMirrorFilterId",
                str(value["traffic_mirror_filter_id"]),
            )
        )
    if "packet_length" in value:
        pairs.append((f"{key_prefix}PacketLength", str(value["packet_length"])))
    if "session_number" in value:
        pairs.append((f"{key_prefix}SessionNumber", str(value["session_number"])))
    if "virtual_network_id" in value:
        pairs.append(
            (f"{key_prefix}VirtualNetworkId", str(value["virtual_network_id"]))
        )
    if "description" in value:
        pairs.append((f"{key_prefix}Description", str(value["description"])))
    if "tag_specifications" in value:
        import capo_ec2.types.tag_specification_list

        capo_ec2.types.tag_specification_list.serialize_ec2_query(
            value["tag_specifications"], pairs, f"{key_prefix}TagSpecification"
        )
    if "dry_run" in value:
        pairs.append((f"{key_prefix}DryRun", "true" if value["dry_run"] else "false"))
    if "client_token" in value:
        pairs.append((f"{key_prefix}ClientToken", str(value["client_token"])))


def deserialize_ec2_query(el: Element) -> CreateTrafficMirrorSessionRequest:
    out: CreateTrafficMirrorSessionRequest = {}  # type: ignore[typeddict-item]
    child_network_interface_id = el.find("NetworkInterfaceId")
    if child_network_interface_id is not None:
        out["network_interface_id"] = str(child_network_interface_id.text or "")
    child_traffic_mirror_target_id = el.find("TrafficMirrorTargetId")
    if child_traffic_mirror_target_id is not None:
        out["traffic_mirror_target_id"] = str(child_traffic_mirror_target_id.text or "")
    child_traffic_mirror_filter_id = el.find("TrafficMirrorFilterId")
    if child_traffic_mirror_filter_id is not None:
        out["traffic_mirror_filter_id"] = str(child_traffic_mirror_filter_id.text or "")
    child_packet_length = el.find("PacketLength")
    if child_packet_length is not None:
        out["packet_length"] = int(child_packet_length.text or "")
    child_session_number = el.find("SessionNumber")
    if child_session_number is not None:
        out["session_number"] = int(child_session_number.text or "")
    child_virtual_network_id = el.find("VirtualNetworkId")
    if child_virtual_network_id is not None:
        out["virtual_network_id"] = int(child_virtual_network_id.text or "")
    child_description = el.find("Description")
    if child_description is not None:
        out["description"] = str(child_description.text or "")
    child_tag_specifications = el.find("TagSpecification")
    if child_tag_specifications is not None:
        import capo_ec2.types.tag_specification_list

        out["tag_specifications"] = (
            capo_ec2.types.tag_specification_list.deserialize_ec2_query(
                child_tag_specifications
            )
        )
    child_dry_run = el.find("DryRun")
    if child_dry_run is not None:
        out["dry_run"] = (child_dry_run.text or "").lower() == "true"
    child_client_token = el.find("ClientToken")
    if child_client_token is not None:
        out["client_token"] = str(child_client_token.text or "")
    return out
