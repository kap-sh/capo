"""Generated from Smithy shape ``com.amazonaws.ec2#ModifyTransitGatewayPeeringAttachmentRequest``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

from capo_ec2._protocol.xml import Element

if TYPE_CHECKING:
    import capo_ec2.types.boolean
    import capo_ec2.types.modify_transit_gateway_peering_attachment_request_options
    import capo_ec2.types.transit_gateway_attachment_id


class ModifyTransitGatewayPeeringAttachmentRequest(TypedDict, closed=True):
    transit_gateway_attachment_id: NotRequired[
        "capo_ec2.types.transit_gateway_attachment_id.TransitGatewayAttachmentId"
    ]
    """<p>The ID of the transit gateway peering attachment.</p>"""
    options: NotRequired[
        "capo_ec2.types.modify_transit_gateway_peering_attachment_request_options.ModifyTransitGatewayPeeringAttachmentRequestOptions"
    ]
    """<p>The options to modify for the transit gateway peering attachment.</p>"""
    dry_run: NotRequired["capo_ec2.types.boolean.Boolean"]
    """<p>Checks whether you have the required permissions for the action, without actually making the request, and provides an error response. If you have the required permissions, the error response is <code>DryRunOperation</code>. Otherwise, it is <code>UnauthorizedOperation</code>.</p>"""


# --- ec2Query ser/de ---
def serialize_ec2_query(
    value: ModifyTransitGatewayPeeringAttachmentRequest,
    pairs: list[tuple[str, str]],
    prefix: str,
) -> None:
    key_prefix = f"{prefix}." if prefix else ""
    if "transit_gateway_attachment_id" in value:
        pairs.append(
            (
                f"{key_prefix}TransitGatewayAttachmentId",
                str(value["transit_gateway_attachment_id"]),
            )
        )
    if "options" in value:
        import capo_ec2.types.modify_transit_gateway_peering_attachment_request_options

        capo_ec2.types.modify_transit_gateway_peering_attachment_request_options.serialize_ec2_query(
            value["options"], pairs, f"{key_prefix}Options"
        )
    if "dry_run" in value:
        pairs.append((f"{key_prefix}DryRun", "true" if value["dry_run"] else "false"))


def deserialize_ec2_query(el: Element) -> ModifyTransitGatewayPeeringAttachmentRequest:
    out: ModifyTransitGatewayPeeringAttachmentRequest = {}  # type: ignore[typeddict-item]
    child_transit_gateway_attachment_id = el.find("TransitGatewayAttachmentId")
    if child_transit_gateway_attachment_id is not None:
        out["transit_gateway_attachment_id"] = str(
            child_transit_gateway_attachment_id.text or ""
        )
    child_options = el.find("Options")
    if child_options is not None:
        import capo_ec2.types.modify_transit_gateway_peering_attachment_request_options

        out["options"] = (
            capo_ec2.types.modify_transit_gateway_peering_attachment_request_options.deserialize_ec2_query(
                child_options
            )
        )
    child_dry_run = el.find("DryRun")
    if child_dry_run is not None:
        out["dry_run"] = (child_dry_run.text or "").lower() == "true"
    return out
