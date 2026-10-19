"""Generated from Smithy shape ``com.amazonaws.route53resolver#UpdateFirewallConfigRequest``."""

from typing import TYPE_CHECKING

from typing_extensions import TypedDict

if TYPE_CHECKING:
    import capo_route53resolver.types.firewall_fail_open_status
    import capo_route53resolver.types.resource_id


class UpdateFirewallConfigRequest(TypedDict, closed=True):
    resource_id: "capo_route53resolver.types.resource_id.ResourceId"
    """<p>The ID of the VPC that the configuration is for.</p>"""
    firewall_fail_open: (
        "capo_route53resolver.types.firewall_fail_open_status.FirewallFailOpenStatus"
    )
    """<p>Determines how Route 53 Resolver handles queries during failures, for example when all traffic that is sent to DNS Firewall fails to receive a reply. </p> <ul> <li> <p>By default, fail open is disabled, which means the failure mode is closed. This approach favors security over availability. DNS Firewall blocks queries that it is unable to evaluate properly. </p> </li> <li> <p>If you enable this option, the failure mode is open. This approach favors availability over security. DNS Firewall allows queries to proceed if it is unable to properly evaluate them. </p> </li> </ul> <p>This behavior is only enforced for VPCs that have at least one DNS Firewall rule group association. </p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: UpdateFirewallConfigRequest) -> dict:
    out: dict = {}
    out["ResourceId"] = value["resource_id"]
    import capo_route53resolver.types.firewall_fail_open_status

    out["FirewallFailOpen"] = (
        capo_route53resolver.types.firewall_fail_open_status.serialize_aws_json_1_1(
            value["firewall_fail_open"]
        )
    )
    return out


def deserialize_aws_json_1_1(data: dict) -> UpdateFirewallConfigRequest:
    out: UpdateFirewallConfigRequest = {}  # type: ignore[typeddict-item]
    if data.get("ResourceId") is not None:
        out["resource_id"] = data["ResourceId"]
    else:
        out["resource_id"] = ""
    if data.get("FirewallFailOpen") is not None:
        import capo_route53resolver.types.firewall_fail_open_status

        out["firewall_fail_open"] = (
            capo_route53resolver.types.firewall_fail_open_status.deserialize_aws_json_1_1(
                data["FirewallFailOpen"]
            )
        )
    else:
        import typing

        out["firewall_fail_open"] = typing.cast(
            "capo_route53resolver.types.firewall_fail_open_status.FirewallFailOpenStatus",
            "",
        )
    return out
