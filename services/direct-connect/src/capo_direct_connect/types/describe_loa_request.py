"""Generated from Smithy shape ``com.amazonaws.directconnect#DescribeLoaRequest``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_direct_connect.types.connection_id
    import capo_direct_connect.types.loa_content_type
    import capo_direct_connect.types.provider_name


class DescribeLoaRequest(TypedDict, closed=True):
    connection_id: "capo_direct_connect.types.connection_id.ConnectionId"
    """<p>The ID of a connection, LAG, or interconnect.</p>"""
    provider_name: NotRequired["capo_direct_connect.types.provider_name.ProviderName"]
    """<p>The name of the service provider who establishes connectivity on your behalf. If you specify this parameter, the LOA-CFA lists the provider name alongside your company name as the requester of the cross connect.</p>"""
    loa_content_type: NotRequired[
        "capo_direct_connect.types.loa_content_type.LoaContentType"
    ]
    """<p>The standard media type for the LOA-CFA document. The only supported value is application/pdf.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: DescribeLoaRequest) -> dict:
    out: dict = {}
    out["connectionId"] = value["connection_id"]
    if "provider_name" in value:
        out["providerName"] = value["provider_name"]
    if "loa_content_type" in value:
        import capo_direct_connect.types.loa_content_type

        out["loaContentType"] = (
            capo_direct_connect.types.loa_content_type.serialize_aws_json_1_1(
                value["loa_content_type"]
            )
        )
    return out


def deserialize_aws_json_1_1(data: dict) -> DescribeLoaRequest:
    out: DescribeLoaRequest = {}  # type: ignore[typeddict-item]
    if data.get("connectionId") is not None:
        out["connection_id"] = data["connectionId"]
    else:
        out["connection_id"] = ""
    if data.get("providerName") is not None:
        out["provider_name"] = data["providerName"]
    if data.get("loaContentType") is not None:
        import capo_direct_connect.types.loa_content_type

        out["loa_content_type"] = (
            capo_direct_connect.types.loa_content_type.deserialize_aws_json_1_1(
                data["loaContentType"]
            )
        )
    return out
