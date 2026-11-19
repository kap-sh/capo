"""Generated from Smithy shape ``com.amazonaws.ec2#DeleteTransitGatewayNetworkFunctionAttachmentResult``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

from capo_ec2._protocol.xml import Element

if TYPE_CHECKING:
    import capo_ec2.types.transit_gateway_network_function_attachment


class DeleteTransitGatewayNetworkFunctionAttachmentResult(TypedDict, closed=True):
    transit_gateway_network_function_attachment: NotRequired[
        "capo_ec2.types.transit_gateway_network_function_attachment.TransitGatewayNetworkFunctionAttachment"
    ]
    """<p>Information about the deleted network function attachment.</p>"""


# --- ec2Query ser/de ---
def serialize_ec2_query(
    value: DeleteTransitGatewayNetworkFunctionAttachmentResult,
    pairs: list[tuple[str, str]],
    prefix: str,
) -> None:
    key_prefix = f"{prefix}." if prefix else ""
    if "transit_gateway_network_function_attachment" in value:
        import capo_ec2.types.transit_gateway_network_function_attachment

        capo_ec2.types.transit_gateway_network_function_attachment.serialize_ec2_query(
            value["transit_gateway_network_function_attachment"],
            pairs,
            f"{key_prefix}TransitGatewayNetworkFunctionAttachment",
        )


def deserialize_ec2_query(
    el: Element,
) -> DeleteTransitGatewayNetworkFunctionAttachmentResult:
    out: DeleteTransitGatewayNetworkFunctionAttachmentResult = {}  # type: ignore[typeddict-item]
    child_transit_gateway_network_function_attachment = el.find(
        "transitGatewayNetworkFunctionAttachment"
    )
    if child_transit_gateway_network_function_attachment is not None:
        import capo_ec2.types.transit_gateway_network_function_attachment

        out["transit_gateway_network_function_attachment"] = (
            capo_ec2.types.transit_gateway_network_function_attachment.deserialize_ec2_query(
                child_transit_gateway_network_function_attachment
            )
        )
    return out
