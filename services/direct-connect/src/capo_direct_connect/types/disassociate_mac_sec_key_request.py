"""Generated from Smithy shape ``com.amazonaws.directconnect#DisassociateMacSecKeyRequest``."""

from typing import TYPE_CHECKING

from typing_extensions import TypedDict

if TYPE_CHECKING:
    import capo_direct_connect.types.connection_id
    import capo_direct_connect.types.secret_arn


class DisassociateMacSecKeyRequest(TypedDict, closed=True):
    connection_id: "capo_direct_connect.types.connection_id.ConnectionId"
    """<p>The ID of the dedicated connection (dxcon-xxxx), interconnect (dxcon-xxxx), or LAG (dxlag-xxxx).</p> <p>You can use <a>DescribeConnections</a>, <a>DescribeInterconnects</a>, or <a>DescribeLags</a> to retrieve connection ID.</p>"""
    secret_arn: "capo_direct_connect.types.secret_arn.SecretARN"
    """<p>The Amazon Resource Name (ARN) of the MAC Security (MACsec) secret key.</p> <p>You can use <a>DescribeConnections</a> to retrieve the ARN of the MAC Security (MACsec) secret key.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: DisassociateMacSecKeyRequest) -> dict:
    out: dict = {}
    out["connectionId"] = value["connection_id"]
    out["secretARN"] = value["secret_arn"]
    return out


def deserialize_aws_json_1_1(data: dict) -> DisassociateMacSecKeyRequest:
    out: DisassociateMacSecKeyRequest = {}  # type: ignore[typeddict-item]
    if data.get("connectionId") is not None:
        out["connection_id"] = data["connectionId"]
    else:
        out["connection_id"] = ""
    if data.get("secretARN") is not None:
        out["secret_arn"] = data["secretARN"]
    else:
        out["secret_arn"] = ""
    return out
