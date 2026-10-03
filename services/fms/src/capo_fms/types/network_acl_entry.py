"""Generated from Smithy shape ``com.amazonaws.fms#NetworkAclEntry``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

from capo_fms.errors import DeserializationError

if TYPE_CHECKING:
    import capo_fms.types.boolean_object
    import capo_fms.types.length_bounded_non_empty_string
    import capo_fms.types.length_bounded_string
    import capo_fms.types.network_acl_icmp_type_code
    import capo_fms.types.network_acl_port_range
    import capo_fms.types.network_acl_rule_action


class NetworkAclEntry(TypedDict, closed=True):
    icmp_type_code: NotRequired[
        "capo_fms.types.network_acl_icmp_type_code.NetworkAclIcmpTypeCode"
    ]
    """<p>ICMP protocol: The ICMP type and code.</p>"""
    protocol: "capo_fms.types.length_bounded_string.LengthBoundedString"
    """<p>The protocol number. A value of "-1" means all protocols. </p>"""
    port_range: NotRequired["capo_fms.types.network_acl_port_range.NetworkAclPortRange"]
    """<p>TCP or UDP protocols: The range of ports the rule applies to.</p>"""
    cidr_block: NotRequired[
        "capo_fms.types.length_bounded_non_empty_string.LengthBoundedNonEmptyString"
    ]
    """<p>The IPv4 network range to allow or deny, in CIDR notation.</p>"""
    ipv6_cidr_block: NotRequired[
        "capo_fms.types.length_bounded_non_empty_string.LengthBoundedNonEmptyString"
    ]
    """<p>The IPv6 network range to allow or deny, in CIDR notation.</p>"""
    rule_action: "capo_fms.types.network_acl_rule_action.NetworkAclRuleAction"
    """<p>Indicates whether to allow or deny the traffic that matches the rule.</p>"""
    egress: "capo_fms.types.boolean_object.BooleanObject"
    """<p>Indicates whether the rule is an egress, or outbound, rule (applied to traffic leaving the subnet). If it's not an egress rule, then it's an ingress, or inbound, rule.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: NetworkAclEntry) -> dict:
    out: dict = {}
    if "icmp_type_code" in value:
        import capo_fms.types.network_acl_icmp_type_code

        out["IcmpTypeCode"] = (
            capo_fms.types.network_acl_icmp_type_code.serialize_aws_json_1_1(
                value["icmp_type_code"]
            )
        )
    out["Protocol"] = value["protocol"]
    if "port_range" in value:
        import capo_fms.types.network_acl_port_range

        out["PortRange"] = capo_fms.types.network_acl_port_range.serialize_aws_json_1_1(
            value["port_range"]
        )
    if "cidr_block" in value:
        out["CidrBlock"] = value["cidr_block"]
    if "ipv6_cidr_block" in value:
        out["Ipv6CidrBlock"] = value["ipv6_cidr_block"]
    import capo_fms.types.network_acl_rule_action

    out["RuleAction"] = capo_fms.types.network_acl_rule_action.serialize_aws_json_1_1(
        value["rule_action"]
    )
    out["Egress"] = value["egress"]
    return out


def deserialize_aws_json_1_1(data: dict) -> NetworkAclEntry:
    out: NetworkAclEntry = {}  # type: ignore[typeddict-item]
    if data.get("IcmpTypeCode") is not None:
        import capo_fms.types.network_acl_icmp_type_code

        out["icmp_type_code"] = (
            capo_fms.types.network_acl_icmp_type_code.deserialize_aws_json_1_1(
                data["IcmpTypeCode"]
            )
        )
    if data.get("Protocol") is not None:
        out["protocol"] = data["Protocol"]
    else:
        raise DeserializationError("NetworkAclEntry.protocol required")
    if data.get("PortRange") is not None:
        import capo_fms.types.network_acl_port_range

        out["port_range"] = (
            capo_fms.types.network_acl_port_range.deserialize_aws_json_1_1(
                data["PortRange"]
            )
        )
    if data.get("CidrBlock") is not None:
        out["cidr_block"] = data["CidrBlock"]
    if data.get("Ipv6CidrBlock") is not None:
        out["ipv6_cidr_block"] = data["Ipv6CidrBlock"]
    if data.get("RuleAction") is not None:
        import capo_fms.types.network_acl_rule_action

        out["rule_action"] = (
            capo_fms.types.network_acl_rule_action.deserialize_aws_json_1_1(
                data["RuleAction"]
            )
        )
    else:
        raise DeserializationError("NetworkAclEntry.rule_action required")
    if data.get("Egress") is not None:
        out["egress"] = data["Egress"]
    else:
        raise DeserializationError("NetworkAclEntry.egress required")
    return out
