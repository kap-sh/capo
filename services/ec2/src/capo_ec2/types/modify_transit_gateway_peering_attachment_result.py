"""Generated from Smithy shape ``com.amazonaws.ec2#ModifyTransitGatewayPeeringAttachmentResult``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

from capo_ec2._protocol.xml import Element

if TYPE_CHECKING:
    import capo_ec2.types.transit_gateway_peering_attachment


class ModifyTransitGatewayPeeringAttachmentResult(TypedDict, closed=True):
    transit_gateway_peering_attachment: NotRequired[
        "capo_ec2.types.transit_gateway_peering_attachment.TransitGatewayPeeringAttachment"
    ]
    """<p>Information about the transit gateway peering attachment.</p>"""


# --- ec2Query ser/de ---
def serialize_ec2_query(
    value: ModifyTransitGatewayPeeringAttachmentResult,
    pairs: list[tuple[str, str]],
    prefix: str,
) -> None:
    key_prefix = f"{prefix}." if prefix else ""
    if "transit_gateway_peering_attachment" in value:
        import capo_ec2.types.transit_gateway_peering_attachment

        capo_ec2.types.transit_gateway_peering_attachment.serialize_ec2_query(
            value["transit_gateway_peering_attachment"],
            pairs,
            f"{key_prefix}TransitGatewayPeeringAttachment",
        )


def deserialize_ec2_query(el: Element) -> ModifyTransitGatewayPeeringAttachmentResult:
    out: ModifyTransitGatewayPeeringAttachmentResult = {}  # type: ignore[typeddict-item]
    child_transit_gateway_peering_attachment = el.find(
        "transitGatewayPeeringAttachment"
    )
    if child_transit_gateway_peering_attachment is not None:
        import capo_ec2.types.transit_gateway_peering_attachment

        out["transit_gateway_peering_attachment"] = (
            capo_ec2.types.transit_gateway_peering_attachment.deserialize_ec2_query(
                child_transit_gateway_peering_attachment
            )
        )
    return out
