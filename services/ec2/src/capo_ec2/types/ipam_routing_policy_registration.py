"""Generated from Smithy shape ``com.amazonaws.ec2#IpamRoutingPolicyRegistration``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

from capo_ec2._protocol.xml import Element

if TYPE_CHECKING:
    import capo_ec2.types.asn_list
    import capo_ec2.types.boxed_boolean
    import capo_ec2.types.ipam_routing_policy_registration_max_length
    import capo_ec2.types.ipam_routing_policy_registration_state
    import capo_ec2.types.string


class IpamRoutingPolicyRegistration(TypedDict, closed=True):
    cidr: NotRequired["capo_ec2.types.string.String"]
    """<p>The IP address prefix in CIDR notation authorized by the ROA.</p>"""
    asns: NotRequired["capo_ec2.types.asn_list.AsnList"]
    """<p>The Autonomous System Numbers (ASNs) authorized to originate the prefix.</p>"""
    permit_more_specific_announcements: NotRequired[
        "capo_ec2.types.boxed_boolean.BoxedBoolean"
    ]
    """<p>Specifies whether to permit more specific route announcements than the CIDR prefix. When enabled, ASNs can announce sub-prefixes of the authorized CIDR up to the specified maximum length. Default: <code>false</code>.</p>"""
    max_length: NotRequired[
        "capo_ec2.types.ipam_routing_policy_registration_max_length.IpamRoutingPolicyRegistrationMaxLength"
    ]
    """<p>The maximum prefix length that the ASNs are authorized to announce.</p>"""
    description: NotRequired["capo_ec2.types.string.String"]
    """<p>The description of the routing policy registration.</p>"""
    latest_delta_id: NotRequired["capo_ec2.types.string.String"]
    """<p>The ID of the most recent delta that modified this registration.</p>"""
    state: NotRequired[
        "capo_ec2.types.ipam_routing_policy_registration_state.IpamRoutingPolicyRegistrationState"
    ]
    """<p>The state of the routing policy registration. Valid values: <code>pending-activate</code> | <code>activate-failed</code> | <code>create-in-progress</code> | <code>create-complete</code> | <code>update-in-progress</code> | <code>update-complete</code> | <code>delete-in-progress</code> | <code>delete-complete</code> | <code>disable-complete</code>.</p>"""


# --- ec2Query ser/de ---
def serialize_ec2_query(
    value: IpamRoutingPolicyRegistration, pairs: list[tuple[str, str]], prefix: str
) -> None:
    key_prefix = f"{prefix}." if prefix else ""
    if "cidr" in value:
        pairs.append((f"{key_prefix}Cidr", str(value["cidr"])))
    if "asns" in value:
        import capo_ec2.types.asn_list

        capo_ec2.types.asn_list.serialize_ec2_query(
            value["asns"], pairs, f"{key_prefix}AsnSet"
        )
    if "permit_more_specific_announcements" in value:
        pairs.append(
            (
                f"{key_prefix}PermitMoreSpecificAnnouncements",
                "true" if value["permit_more_specific_announcements"] else "false",
            )
        )
    if "max_length" in value:
        pairs.append((f"{key_prefix}MaxLength", str(value["max_length"])))
    if "description" in value:
        pairs.append((f"{key_prefix}Description", str(value["description"])))
    if "latest_delta_id" in value:
        pairs.append((f"{key_prefix}LatestDeltaId", str(value["latest_delta_id"])))
    if "state" in value:
        import capo_ec2.types.ipam_routing_policy_registration_state

        capo_ec2.types.ipam_routing_policy_registration_state.serialize_ec2_query(
            value["state"], pairs, f"{key_prefix}State"
        )


def deserialize_ec2_query(el: Element) -> IpamRoutingPolicyRegistration:
    out: IpamRoutingPolicyRegistration = {}  # type: ignore[typeddict-item]
    child_cidr = el.find("cidr")
    if child_cidr is not None:
        out["cidr"] = str(child_cidr.text or "")
    child_asns = el.find("asnSet")
    if child_asns is not None:
        import capo_ec2.types.asn_list

        out["asns"] = capo_ec2.types.asn_list.deserialize_ec2_query(child_asns)
    child_permit_more_specific_announcements = el.find(
        "permitMoreSpecificAnnouncements"
    )
    if child_permit_more_specific_announcements is not None:
        out["permit_more_specific_announcements"] = (
            child_permit_more_specific_announcements.text or ""
        ).lower() == "true"
    child_max_length = el.find("maxLength")
    if child_max_length is not None:
        out["max_length"] = int(child_max_length.text or "")
    child_description = el.find("description")
    if child_description is not None:
        out["description"] = str(child_description.text or "")
    child_latest_delta_id = el.find("latestDeltaId")
    if child_latest_delta_id is not None:
        out["latest_delta_id"] = str(child_latest_delta_id.text or "")
    child_state = el.find("state")
    if child_state is not None:
        import capo_ec2.types.ipam_routing_policy_registration_state

        out["state"] = (
            capo_ec2.types.ipam_routing_policy_registration_state.deserialize_ec2_query(
                child_state
            )
        )
    return out
