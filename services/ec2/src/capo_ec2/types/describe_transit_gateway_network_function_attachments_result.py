"""Generated from Smithy shape ``com.amazonaws.ec2#DescribeTransitGatewayNetworkFunctionAttachmentsResult``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

from capo_ec2._protocol.xml import Element

if TYPE_CHECKING:
    import capo_ec2.types.string
    import capo_ec2.types.transit_gateway_network_function_attachment_list


class DescribeTransitGatewayNetworkFunctionAttachmentsResult(TypedDict, closed=True):
    transit_gateway_network_function_attachments: NotRequired[
        "capo_ec2.types.transit_gateway_network_function_attachment_list.TransitGatewayNetworkFunctionAttachmentList"
    ]
    """<p>Information about the network function attachments.</p>"""
    next_token: NotRequired["capo_ec2.types.string.String"]
    """<p>The token to use to retrieve the next page of results. This value is <code>null</code> when there are no more results to return.</p>"""


# --- ec2Query ser/de ---
def serialize_ec2_query(
    value: DescribeTransitGatewayNetworkFunctionAttachmentsResult,
    pairs: list[tuple[str, str]],
    prefix: str,
) -> None:
    key_prefix = f"{prefix}." if prefix else ""
    if "transit_gateway_network_function_attachments" in value:
        import capo_ec2.types.transit_gateway_network_function_attachment_list

        capo_ec2.types.transit_gateway_network_function_attachment_list.serialize_ec2_query(
            value["transit_gateway_network_function_attachments"],
            pairs,
            f"{key_prefix}TransitGatewayNetworkFunctionAttachmentSet",
        )
    if "next_token" in value:
        pairs.append((f"{key_prefix}NextToken", str(value["next_token"])))


def deserialize_ec2_query(
    el: Element,
) -> DescribeTransitGatewayNetworkFunctionAttachmentsResult:
    out: DescribeTransitGatewayNetworkFunctionAttachmentsResult = {}  # type: ignore[typeddict-item]
    child_transit_gateway_network_function_attachments = el.find(
        "transitGatewayNetworkFunctionAttachmentSet"
    )
    if child_transit_gateway_network_function_attachments is not None:
        import capo_ec2.types.transit_gateway_network_function_attachment_list

        out["transit_gateway_network_function_attachments"] = (
            capo_ec2.types.transit_gateway_network_function_attachment_list.deserialize_ec2_query(
                child_transit_gateway_network_function_attachments
            )
        )
    child_next_token = el.find("nextToken")
    if child_next_token is not None:
        out["next_token"] = str(child_next_token.text or "")
    return out
