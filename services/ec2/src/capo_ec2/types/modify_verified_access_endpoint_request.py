"""Generated from Smithy shape ``com.amazonaws.ec2#ModifyVerifiedAccessEndpointRequest``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

from capo_ec2._protocol.xml import Element

if TYPE_CHECKING:
    import capo_ec2.types.boolean
    import capo_ec2.types.modify_verified_access_endpoint_cidr_options
    import capo_ec2.types.modify_verified_access_endpoint_eni_options
    import capo_ec2.types.modify_verified_access_endpoint_load_balancer_options
    import capo_ec2.types.modify_verified_access_endpoint_rds_options
    import capo_ec2.types.string
    import capo_ec2.types.verified_access_endpoint_id
    import capo_ec2.types.verified_access_group_id


class ModifyVerifiedAccessEndpointRequest(TypedDict, closed=True):
    verified_access_endpoint_id: NotRequired[
        "capo_ec2.types.verified_access_endpoint_id.VerifiedAccessEndpointId"
    ]
    """<p>The ID of the Verified Access endpoint.</p>"""
    verified_access_group_id: NotRequired[
        "capo_ec2.types.verified_access_group_id.VerifiedAccessGroupId"
    ]
    """<p>The ID of the Verified Access group.</p>"""
    load_balancer_options: NotRequired[
        "capo_ec2.types.modify_verified_access_endpoint_load_balancer_options.ModifyVerifiedAccessEndpointLoadBalancerOptions"
    ]
    """<p>The load balancer details if creating the Verified Access endpoint as <code>load-balancer</code>type.</p>"""
    network_interface_options: NotRequired[
        "capo_ec2.types.modify_verified_access_endpoint_eni_options.ModifyVerifiedAccessEndpointEniOptions"
    ]
    """<p>The network interface options.</p>"""
    description: NotRequired["capo_ec2.types.string.String"]
    """<p>A description for the Verified Access endpoint.</p>"""
    client_token: NotRequired["capo_ec2.types.string.String"]
    """<p>A unique, case-sensitive token that you provide to ensure idempotency of your modification request. For more information, see <a href="https://docs.aws.amazon.com/ec2/latest/devguide/ec2-api-idempotency.html">Ensuring idempotency</a>.</p>"""
    dry_run: NotRequired["capo_ec2.types.boolean.Boolean"]
    """<p>Checks whether you have the required permissions for the action, without actually making the request, and provides an error response. If you have the required permissions, the error response is <code>DryRunOperation</code>. Otherwise, it is <code>UnauthorizedOperation</code>.</p>"""
    rds_options: NotRequired[
        "capo_ec2.types.modify_verified_access_endpoint_rds_options.ModifyVerifiedAccessEndpointRdsOptions"
    ]
    """<p>The RDS options.</p>"""
    cidr_options: NotRequired[
        "capo_ec2.types.modify_verified_access_endpoint_cidr_options.ModifyVerifiedAccessEndpointCidrOptions"
    ]
    """<p>The CIDR options.</p>"""


# --- ec2Query ser/de ---
def serialize_ec2_query(
    value: ModifyVerifiedAccessEndpointRequest,
    pairs: list[tuple[str, str]],
    prefix: str,
) -> None:
    key_prefix = f"{prefix}." if prefix else ""
    if "verified_access_endpoint_id" in value:
        pairs.append(
            (
                f"{key_prefix}VerifiedAccessEndpointId",
                str(value["verified_access_endpoint_id"]),
            )
        )
    if "verified_access_group_id" in value:
        pairs.append(
            (
                f"{key_prefix}VerifiedAccessGroupId",
                str(value["verified_access_group_id"]),
            )
        )
    if "load_balancer_options" in value:
        import capo_ec2.types.modify_verified_access_endpoint_load_balancer_options

        capo_ec2.types.modify_verified_access_endpoint_load_balancer_options.serialize_ec2_query(
            value["load_balancer_options"], pairs, f"{key_prefix}LoadBalancerOptions"
        )
    if "network_interface_options" in value:
        import capo_ec2.types.modify_verified_access_endpoint_eni_options

        capo_ec2.types.modify_verified_access_endpoint_eni_options.serialize_ec2_query(
            value["network_interface_options"],
            pairs,
            f"{key_prefix}NetworkInterfaceOptions",
        )
    if "description" in value:
        pairs.append((f"{key_prefix}Description", str(value["description"])))
    if "client_token" in value:
        pairs.append((f"{key_prefix}ClientToken", str(value["client_token"])))
    if "dry_run" in value:
        pairs.append((f"{key_prefix}DryRun", "true" if value["dry_run"] else "false"))
    if "rds_options" in value:
        import capo_ec2.types.modify_verified_access_endpoint_rds_options

        capo_ec2.types.modify_verified_access_endpoint_rds_options.serialize_ec2_query(
            value["rds_options"], pairs, f"{key_prefix}RdsOptions"
        )
    if "cidr_options" in value:
        import capo_ec2.types.modify_verified_access_endpoint_cidr_options

        capo_ec2.types.modify_verified_access_endpoint_cidr_options.serialize_ec2_query(
            value["cidr_options"], pairs, f"{key_prefix}CidrOptions"
        )


def deserialize_ec2_query(el: Element) -> ModifyVerifiedAccessEndpointRequest:
    out: ModifyVerifiedAccessEndpointRequest = {}  # type: ignore[typeddict-item]
    child_verified_access_endpoint_id = el.find("VerifiedAccessEndpointId")
    if child_verified_access_endpoint_id is not None:
        out["verified_access_endpoint_id"] = str(
            child_verified_access_endpoint_id.text or ""
        )
    child_verified_access_group_id = el.find("VerifiedAccessGroupId")
    if child_verified_access_group_id is not None:
        out["verified_access_group_id"] = str(child_verified_access_group_id.text or "")
    child_load_balancer_options = el.find("LoadBalancerOptions")
    if child_load_balancer_options is not None:
        import capo_ec2.types.modify_verified_access_endpoint_load_balancer_options

        out["load_balancer_options"] = (
            capo_ec2.types.modify_verified_access_endpoint_load_balancer_options.deserialize_ec2_query(
                child_load_balancer_options
            )
        )
    child_network_interface_options = el.find("NetworkInterfaceOptions")
    if child_network_interface_options is not None:
        import capo_ec2.types.modify_verified_access_endpoint_eni_options

        out["network_interface_options"] = (
            capo_ec2.types.modify_verified_access_endpoint_eni_options.deserialize_ec2_query(
                child_network_interface_options
            )
        )
    child_description = el.find("Description")
    if child_description is not None:
        out["description"] = str(child_description.text or "")
    child_client_token = el.find("ClientToken")
    if child_client_token is not None:
        out["client_token"] = str(child_client_token.text or "")
    child_dry_run = el.find("DryRun")
    if child_dry_run is not None:
        out["dry_run"] = (child_dry_run.text or "").lower() == "true"
    child_rds_options = el.find("RdsOptions")
    if child_rds_options is not None:
        import capo_ec2.types.modify_verified_access_endpoint_rds_options

        out["rds_options"] = (
            capo_ec2.types.modify_verified_access_endpoint_rds_options.deserialize_ec2_query(
                child_rds_options
            )
        )
    child_cidr_options = el.find("CidrOptions")
    if child_cidr_options is not None:
        import capo_ec2.types.modify_verified_access_endpoint_cidr_options

        out["cidr_options"] = (
            capo_ec2.types.modify_verified_access_endpoint_cidr_options.deserialize_ec2_query(
                child_cidr_options
            )
        )
    return out
