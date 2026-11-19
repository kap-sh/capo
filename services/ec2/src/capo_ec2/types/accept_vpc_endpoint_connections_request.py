"""Generated from Smithy shape ``com.amazonaws.ec2#AcceptVpcEndpointConnectionsRequest``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

from capo_ec2._protocol.xml import Element

if TYPE_CHECKING:
    import capo_ec2.types.boolean
    import capo_ec2.types.transit_gateway_attachment_id_list
    import capo_ec2.types.vpc_endpoint_id_list
    import capo_ec2.types.vpc_endpoint_service_id


class AcceptVpcEndpointConnectionsRequest(TypedDict, closed=True):
    dry_run: NotRequired["capo_ec2.types.boolean.Boolean"]
    """<p>Checks whether you have the required permissions for the action, without actually making the request, and provides an error response. If you have the required permissions, the error response is <code>DryRunOperation</code>. Otherwise, it is <code>UnauthorizedOperation</code>.</p>"""
    service_id: NotRequired[
        "capo_ec2.types.vpc_endpoint_service_id.VpcEndpointServiceId"
    ]
    """<p>The ID of the VPC endpoint service.</p>"""
    vpc_endpoint_ids: NotRequired[
        "capo_ec2.types.vpc_endpoint_id_list.VpcEndpointIdList"
    ]
    """<p>The IDs of the interface VPC endpoints.</p> <p>You must specify either <code>VpcEndpointIds</code> or <code>TransitGatewayAttachmentIds</code>, but not both.</p>"""
    transit_gateway_attachment_ids: NotRequired[
        "capo_ec2.types.transit_gateway_attachment_id_list.TransitGatewayAttachmentIdList"
    ]
    """<p>The IDs of the transit gateway attachments to accept. This parameter is supported only for Gateway Load Balancer endpoint services.</p> <p>You must specify either <code>VpcEndpointIds</code> or <code>TransitGatewayAttachmentIds</code>, but not both.</p>"""


# --- ec2Query ser/de ---
def serialize_ec2_query(
    value: AcceptVpcEndpointConnectionsRequest,
    pairs: list[tuple[str, str]],
    prefix: str,
) -> None:
    key_prefix = f"{prefix}." if prefix else ""
    if "dry_run" in value:
        pairs.append((f"{key_prefix}DryRun", "true" if value["dry_run"] else "false"))
    if "service_id" in value:
        pairs.append((f"{key_prefix}ServiceId", str(value["service_id"])))
    if "vpc_endpoint_ids" in value:
        import capo_ec2.types.vpc_endpoint_id_list

        capo_ec2.types.vpc_endpoint_id_list.serialize_ec2_query(
            value["vpc_endpoint_ids"], pairs, f"{key_prefix}VpcEndpointId"
        )
    if "transit_gateway_attachment_ids" in value:
        import capo_ec2.types.transit_gateway_attachment_id_list

        capo_ec2.types.transit_gateway_attachment_id_list.serialize_ec2_query(
            value["transit_gateway_attachment_ids"],
            pairs,
            f"{key_prefix}TransitGatewayAttachmentId",
        )


def deserialize_ec2_query(el: Element) -> AcceptVpcEndpointConnectionsRequest:
    out: AcceptVpcEndpointConnectionsRequest = {}  # type: ignore[typeddict-item]
    child_dry_run = el.find("DryRun")
    if child_dry_run is not None:
        out["dry_run"] = (child_dry_run.text or "").lower() == "true"
    child_service_id = el.find("ServiceId")
    if child_service_id is not None:
        out["service_id"] = str(child_service_id.text or "")
    child_vpc_endpoint_ids = el.find("VpcEndpointId")
    if child_vpc_endpoint_ids is not None:
        import capo_ec2.types.vpc_endpoint_id_list

        out["vpc_endpoint_ids"] = (
            capo_ec2.types.vpc_endpoint_id_list.deserialize_ec2_query(
                child_vpc_endpoint_ids
            )
        )
    child_transit_gateway_attachment_ids = el.find("TransitGatewayAttachmentId")
    if child_transit_gateway_attachment_ids is not None:
        import capo_ec2.types.transit_gateway_attachment_id_list

        out["transit_gateway_attachment_ids"] = (
            capo_ec2.types.transit_gateway_attachment_id_list.deserialize_ec2_query(
                child_transit_gateway_attachment_ids
            )
        )
    return out
