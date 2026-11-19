"""Generated from Smithy shape ``com.amazonaws.directconnect#DescribeDirectConnectGatewayAttachmentsResult``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_direct_connect.types.direct_connect_gateway_attachment_list
    import capo_direct_connect.types.pagination_token


class DescribeDirectConnectGatewayAttachmentsResult(TypedDict, closed=True):
    direct_connect_gateway_attachments: NotRequired[
        "capo_direct_connect.types.direct_connect_gateway_attachment_list.DirectConnectGatewayAttachmentList"
    ]
    """<p>The attachments.</p>"""
    next_token: NotRequired[
        "capo_direct_connect.types.pagination_token.PaginationToken"
    ]
    """<p>The token to retrieve the next page.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(
    value: DescribeDirectConnectGatewayAttachmentsResult,
) -> dict:
    out: dict = {}
    if "direct_connect_gateway_attachments" in value:
        import capo_direct_connect.types.direct_connect_gateway_attachment_list

        out["directConnectGatewayAttachments"] = (
            capo_direct_connect.types.direct_connect_gateway_attachment_list.serialize_aws_json_1_1(
                value["direct_connect_gateway_attachments"]
            )
        )
    if "next_token" in value:
        out["nextToken"] = value["next_token"]
    return out


def deserialize_aws_json_1_1(
    data: dict,
) -> DescribeDirectConnectGatewayAttachmentsResult:
    out: DescribeDirectConnectGatewayAttachmentsResult = {}  # type: ignore[typeddict-item]
    if data.get("directConnectGatewayAttachments") is not None:
        import capo_direct_connect.types.direct_connect_gateway_attachment_list

        out["direct_connect_gateway_attachments"] = (
            capo_direct_connect.types.direct_connect_gateway_attachment_list.deserialize_aws_json_1_1(
                data["directConnectGatewayAttachments"]
            )
        )
    if data.get("nextToken") is not None:
        out["next_token"] = data["nextToken"]
    return out


# --- rpcv2Cbor ser/de ---
def serialize_cbor(value: DescribeDirectConnectGatewayAttachmentsResult) -> dict:
    out: dict = {}
    if "direct_connect_gateway_attachments" in value:
        import capo_direct_connect.types.direct_connect_gateway_attachment_list

        out["directConnectGatewayAttachments"] = (
            capo_direct_connect.types.direct_connect_gateway_attachment_list.serialize_cbor(
                value["direct_connect_gateway_attachments"]
            )
        )
    if "next_token" in value:
        out["nextToken"] = value["next_token"]
    return out


def deserialize_cbor(data: dict) -> DescribeDirectConnectGatewayAttachmentsResult:
    out: DescribeDirectConnectGatewayAttachmentsResult = {}  # type: ignore[typeddict-item]
    if data.get("directConnectGatewayAttachments") is not None:
        import capo_direct_connect.types.direct_connect_gateway_attachment_list

        out["direct_connect_gateway_attachments"] = (
            capo_direct_connect.types.direct_connect_gateway_attachment_list.deserialize_cbor(
                data["directConnectGatewayAttachments"]
            )
        )
    if data.get("nextToken") is not None:
        out["next_token"] = data["nextToken"]
    return out
