"""Generated from Smithy shape ``com.amazonaws.ec2#PeeringConnectionOptions``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

from capo_ec2._protocol.xml import Element

if TYPE_CHECKING:
    import capo_ec2.types.boolean
    import capo_ec2.types.multipath_resilience_mode


class PeeringConnectionOptions(TypedDict, closed=True):
    allow_dns_resolution_from_remote_vpc: NotRequired["capo_ec2.types.boolean.Boolean"]
    """<p>If true, the public DNS hostnames of instances in the specified VPC resolve to private IP addresses when queried from instances in the peer VPC.</p>"""
    allow_egress_from_local_classic_link_to_remote_vpc: NotRequired[
        "capo_ec2.types.boolean.Boolean"
    ]
    """<p>Deprecated.</p>"""
    allow_egress_from_local_vpc_to_remote_classic_link: NotRequired[
        "capo_ec2.types.boolean.Boolean"
    ]
    """<p>Deprecated.</p>"""
    allow_multipath_resilience: NotRequired["capo_ec2.types.boolean.Boolean"]
    """<p>Indicates whether this side of the VPC peering connection allows multipath resilience.</p>"""
    multipath_resilience_mode: NotRequired[
        "capo_ec2.types.multipath_resilience_mode.MultipathResilienceMode"
    ]
    """<p>The multipath resilience mode for this side of the VPC peering connection. This value is present only when this side allows multipath resilience.</p>"""


# --- ec2Query ser/de ---
def serialize_ec2_query(
    value: PeeringConnectionOptions, pairs: list[tuple[str, str]], prefix: str
) -> None:
    key_prefix = f"{prefix}." if prefix else ""
    if "allow_dns_resolution_from_remote_vpc" in value:
        pairs.append(
            (
                f"{key_prefix}AllowDnsResolutionFromRemoteVpc",
                "true" if value["allow_dns_resolution_from_remote_vpc"] else "false",
            )
        )
    if "allow_egress_from_local_classic_link_to_remote_vpc" in value:
        pairs.append(
            (
                f"{key_prefix}AllowEgressFromLocalClassicLinkToRemoteVpc",
                "true"
                if value["allow_egress_from_local_classic_link_to_remote_vpc"]
                else "false",
            )
        )
    if "allow_egress_from_local_vpc_to_remote_classic_link" in value:
        pairs.append(
            (
                f"{key_prefix}AllowEgressFromLocalVpcToRemoteClassicLink",
                "true"
                if value["allow_egress_from_local_vpc_to_remote_classic_link"]
                else "false",
            )
        )
    if "allow_multipath_resilience" in value:
        pairs.append(
            (
                f"{key_prefix}AllowMultipathResilience",
                "true" if value["allow_multipath_resilience"] else "false",
            )
        )
    if "multipath_resilience_mode" in value:
        import capo_ec2.types.multipath_resilience_mode

        capo_ec2.types.multipath_resilience_mode.serialize_ec2_query(
            value["multipath_resilience_mode"],
            pairs,
            f"{key_prefix}MultipathResilienceMode",
        )


def deserialize_ec2_query(el: Element) -> PeeringConnectionOptions:
    out: PeeringConnectionOptions = {}  # type: ignore[typeddict-item]
    child_allow_dns_resolution_from_remote_vpc = el.find(
        "allowDnsResolutionFromRemoteVpc"
    )
    if child_allow_dns_resolution_from_remote_vpc is not None:
        out["allow_dns_resolution_from_remote_vpc"] = (
            child_allow_dns_resolution_from_remote_vpc.text or ""
        ).lower() == "true"
    child_allow_egress_from_local_classic_link_to_remote_vpc = el.find(
        "allowEgressFromLocalClassicLinkToRemoteVpc"
    )
    if child_allow_egress_from_local_classic_link_to_remote_vpc is not None:
        out["allow_egress_from_local_classic_link_to_remote_vpc"] = (
            child_allow_egress_from_local_classic_link_to_remote_vpc.text or ""
        ).lower() == "true"
    child_allow_egress_from_local_vpc_to_remote_classic_link = el.find(
        "allowEgressFromLocalVpcToRemoteClassicLink"
    )
    if child_allow_egress_from_local_vpc_to_remote_classic_link is not None:
        out["allow_egress_from_local_vpc_to_remote_classic_link"] = (
            child_allow_egress_from_local_vpc_to_remote_classic_link.text or ""
        ).lower() == "true"
    child_allow_multipath_resilience = el.find("allowMultipathResilience")
    if child_allow_multipath_resilience is not None:
        out["allow_multipath_resilience"] = (
            child_allow_multipath_resilience.text or ""
        ).lower() == "true"
    child_multipath_resilience_mode = el.find("multipathResilienceMode")
    if child_multipath_resilience_mode is not None:
        import capo_ec2.types.multipath_resilience_mode

        out["multipath_resilience_mode"] = (
            capo_ec2.types.multipath_resilience_mode.deserialize_ec2_query(
                child_multipath_resilience_mode
            )
        )
    return out
