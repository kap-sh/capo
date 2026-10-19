"""Generated from Smithy shape ``com.amazonaws.route53globalresolver#DisableDNSViewOutput``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_route53globalresolver.types.client_token
    import capo_route53globalresolver.types.dns_sec_validation_type
    import capo_route53globalresolver.types.edns_client_subnet_type
    import capo_route53globalresolver.types.firewall_rules_fail_open_type
    import capo_route53globalresolver.types.iso8601_time_string
    import capo_route53globalresolver.types.profile_resource_status
    import capo_route53globalresolver.types.resource_arn
    import capo_route53globalresolver.types.resource_description
    import capo_route53globalresolver.types.resource_id
    import capo_route53globalresolver.types.resource_name


class DisableDNSViewOutput(TypedDict, closed=True):
    id: "capo_route53globalresolver.types.resource_id.ResourceId"
    """<p>The unique identifier of the disabled DNS view.</p>"""
    arn: "capo_route53globalresolver.types.resource_arn.ResourceArn"
    """<p>The Amazon Resource Name (ARN) of the disabled DNS view.</p>"""
    client_token: NotRequired[
        "capo_route53globalresolver.types.client_token.ClientToken"
    ]
    """<p>The unique string that identifies the request and ensures idempotency.</p>"""
    dnssec_validation: (
        "capo_route53globalresolver.types.dns_sec_validation_type.DnsSecValidationType"
    )
    """<p>Whether DNSSEC validation is enabled for the disabled DNS view.</p>"""
    edns_client_subnet: (
        "capo_route53globalresolver.types.edns_client_subnet_type.EdnsClientSubnetType"
    )
    """<p>Whether EDNS Client Subnet injection is enabled for the disabled DNS view.</p>"""
    firewall_rules_fail_open: "capo_route53globalresolver.types.firewall_rules_fail_open_type.FirewallRulesFailOpenType"
    """<p>The firewall rules fail-open behavior configured for the disabled DNS view.</p>"""
    name: "capo_route53globalresolver.types.resource_name.ResourceName"
    """<p>The name of the disabled DNS view.</p>"""
    description: NotRequired[
        "capo_route53globalresolver.types.resource_description.ResourceDescription"
    ]
    """<p>The description of the disabled DNS view.</p>"""
    global_resolver_id: "capo_route53globalresolver.types.resource_id.ResourceId"
    """<p>The ID of the Route 53 Global Resolver that the disabled DNS view is associated with.</p>"""
    created_at: "capo_route53globalresolver.types.iso8601_time_string.ISO8601TimeString"
    """<p>The date and time when the DNS view was originally created.</p>"""
    updated_at: "capo_route53globalresolver.types.iso8601_time_string.ISO8601TimeString"
    """<p>The date and time when the DNS view was last updated.</p>"""
    status: (
        "capo_route53globalresolver.types.profile_resource_status.ProfileResourceStatus"
    )
    """<p>The current status of the disabled DNS view.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: DisableDNSViewOutput) -> dict:
    out: dict = {}
    out["id"] = value["id"]
    out["arn"] = value["arn"]
    if "client_token" in value:
        out["clientToken"] = value["client_token"]
    import capo_route53globalresolver.types.dns_sec_validation_type

    out["dnssecValidation"] = (
        capo_route53globalresolver.types.dns_sec_validation_type.serialize_json(
            value["dnssec_validation"]
        )
    )
    import capo_route53globalresolver.types.edns_client_subnet_type

    out["ednsClientSubnet"] = (
        capo_route53globalresolver.types.edns_client_subnet_type.serialize_json(
            value["edns_client_subnet"]
        )
    )
    import capo_route53globalresolver.types.firewall_rules_fail_open_type

    out["firewallRulesFailOpen"] = (
        capo_route53globalresolver.types.firewall_rules_fail_open_type.serialize_json(
            value["firewall_rules_fail_open"]
        )
    )
    out["name"] = value["name"]
    if "description" in value:
        out["description"] = value["description"]
    out["globalResolverId"] = value["global_resolver_id"]
    import capo_route53globalresolver.types.iso8601_time_string

    out["createdAt"] = (
        capo_route53globalresolver.types.iso8601_time_string.serialize_json(
            value["created_at"]
        )
    )
    import capo_route53globalresolver.types.iso8601_time_string

    out["updatedAt"] = (
        capo_route53globalresolver.types.iso8601_time_string.serialize_json(
            value["updated_at"]
        )
    )
    import capo_route53globalresolver.types.profile_resource_status

    out["status"] = (
        capo_route53globalresolver.types.profile_resource_status.serialize_json(
            value["status"]
        )
    )
    return out


def deserialize_json(data: dict) -> DisableDNSViewOutput:
    out: DisableDNSViewOutput = {}  # type: ignore[typeddict-item]
    if data.get("id") is not None:
        out["id"] = data["id"]
    else:
        out["id"] = ""
    if data.get("arn") is not None:
        out["arn"] = data["arn"]
    else:
        out["arn"] = ""
    if data.get("clientToken") is not None:
        out["client_token"] = data["clientToken"]
    if data.get("dnssecValidation") is not None:
        import capo_route53globalresolver.types.dns_sec_validation_type

        out["dnssec_validation"] = (
            capo_route53globalresolver.types.dns_sec_validation_type.deserialize_json(
                data["dnssecValidation"]
            )
        )
    else:
        import typing

        out["dnssec_validation"] = typing.cast(
            "capo_route53globalresolver.types.dns_sec_validation_type.DnsSecValidationType",
            "",
        )
    if data.get("ednsClientSubnet") is not None:
        import capo_route53globalresolver.types.edns_client_subnet_type

        out["edns_client_subnet"] = (
            capo_route53globalresolver.types.edns_client_subnet_type.deserialize_json(
                data["ednsClientSubnet"]
            )
        )
    else:
        import typing

        out["edns_client_subnet"] = typing.cast(
            "capo_route53globalresolver.types.edns_client_subnet_type.EdnsClientSubnetType",
            "",
        )
    if data.get("firewallRulesFailOpen") is not None:
        import capo_route53globalresolver.types.firewall_rules_fail_open_type

        out["firewall_rules_fail_open"] = (
            capo_route53globalresolver.types.firewall_rules_fail_open_type.deserialize_json(
                data["firewallRulesFailOpen"]
            )
        )
    else:
        import typing

        out["firewall_rules_fail_open"] = typing.cast(
            "capo_route53globalresolver.types.firewall_rules_fail_open_type.FirewallRulesFailOpenType",
            "",
        )
    if data.get("name") is not None:
        out["name"] = data["name"]
    else:
        out["name"] = ""
    if data.get("description") is not None:
        out["description"] = data["description"]
    if data.get("globalResolverId") is not None:
        out["global_resolver_id"] = data["globalResolverId"]
    else:
        out["global_resolver_id"] = ""
    if data.get("createdAt") is not None:
        import capo_route53globalresolver.types.iso8601_time_string

        out["created_at"] = (
            capo_route53globalresolver.types.iso8601_time_string.deserialize_json(
                data["createdAt"]
            )
        )
    else:
        import datetime

        out["created_at"] = datetime.datetime.fromtimestamp(0, tz=datetime.timezone.utc)
    if data.get("updatedAt") is not None:
        import capo_route53globalresolver.types.iso8601_time_string

        out["updated_at"] = (
            capo_route53globalresolver.types.iso8601_time_string.deserialize_json(
                data["updatedAt"]
            )
        )
    else:
        import datetime

        out["updated_at"] = datetime.datetime.fromtimestamp(0, tz=datetime.timezone.utc)
    if data.get("status") is not None:
        import capo_route53globalresolver.types.profile_resource_status

        out["status"] = (
            capo_route53globalresolver.types.profile_resource_status.deserialize_json(
                data["status"]
            )
        )
    else:
        import typing

        out["status"] = typing.cast(
            "capo_route53globalresolver.types.profile_resource_status.ProfileResourceStatus",
            "",
        )
    return out
