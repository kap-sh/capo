"""Generated from Smithy shape ``com.amazonaws.ec2#RouteServerBgpOptions``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

from capo_ec2._protocol.xml import Element

if TYPE_CHECKING:
    import capo_ec2.types.long
    import capo_ec2.types.route_server_peer_liveness_mode


class RouteServerBgpOptions(TypedDict, closed=True):
    peer_asn: NotRequired["capo_ec2.types.long.Long"]
    """<p>The Border Gateway Protocol (BGP) Autonomous System Number (ASN) for the appliance. Valid values are from 1 to 4294967295. We recommend using a private ASN in the 64512–65534 (16-bit ASN) or 4200000000–4294967294 (32-bit ASN) range.</p>"""
    peer_liveness_detection: NotRequired[
        "capo_ec2.types.route_server_peer_liveness_mode.RouteServerPeerLivenessMode"
    ]
    """<p>The liveness detection protocol used for the BGP peer.</p> <p>The requested liveness detection protocol for the BGP peer.</p> <ul> <li> <p> <code>bgp-keepalive</code>: The standard BGP keep alive mechanism (<a href="https://www.rfc-editor.org/rfc/rfc4271#page-21">RFC4271</a>) that is stable but may take longer to fail-over in cases of network impact or router failure.</p> </li> <li> <p> <code>bfd</code>: An additional Bidirectional Forwarding Detection (BFD) protocol (<a href="https://www.rfc-editor.org/rfc/rfc5880">RFC5880</a>) that enables fast failover by using more sensitive liveness detection.</p> </li> </ul> <p>Defaults to <code>bgp-keepalive</code>.</p>"""


# --- ec2Query ser/de ---
def serialize_ec2_query(
    value: RouteServerBgpOptions, pairs: list[tuple[str, str]], prefix: str
) -> None:
    key_prefix = f"{prefix}." if prefix else ""
    if "peer_asn" in value:
        pairs.append((f"{key_prefix}PeerAsn", str(value["peer_asn"])))
    if "peer_liveness_detection" in value:
        import capo_ec2.types.route_server_peer_liveness_mode

        capo_ec2.types.route_server_peer_liveness_mode.serialize_ec2_query(
            value["peer_liveness_detection"],
            pairs,
            f"{key_prefix}PeerLivenessDetection",
        )


def deserialize_ec2_query(el: Element) -> RouteServerBgpOptions:
    out: RouteServerBgpOptions = {}  # type: ignore[typeddict-item]
    child_peer_asn = el.find("peerAsn")
    if child_peer_asn is not None:
        out["peer_asn"] = int(child_peer_asn.text or "")
    child_peer_liveness_detection = el.find("peerLivenessDetection")
    if child_peer_liveness_detection is not None:
        import capo_ec2.types.route_server_peer_liveness_mode

        out["peer_liveness_detection"] = (
            capo_ec2.types.route_server_peer_liveness_mode.deserialize_ec2_query(
                child_peer_liveness_detection
            )
        )
    return out
