"""Generated from Smithy shape ``com.amazonaws.directconnect#AssociateMacSecKeyRequest``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_direct_connect.types.cak
    import capo_direct_connect.types.ckn
    import capo_direct_connect.types.connection_id
    import capo_direct_connect.types.secret_arn


class AssociateMacSecKeyRequest(TypedDict, closed=True):
    connection_id: "capo_direct_connect.types.connection_id.ConnectionId"
    """<p>The ID of the dedicated connection (dxcon-xxxx), interconnect (dxcon-xxxx), or LAG (dxlag-xxxx).</p> <p>You can use <a>DescribeConnections</a>, <a>DescribeInterconnects</a>, or <a>DescribeLags</a> to retrieve connection ID.</p>"""
    secret_arn: NotRequired["capo_direct_connect.types.secret_arn.SecretARN"]
    """<p>The Amazon Resource Name (ARN) of the MAC Security (MACsec) secret key to associate with the connection.</p> <p>You can use <a>DescribeConnections</a> or <a>DescribeLags</a> to retrieve the MAC Security (MACsec) secret key.</p> <p>If you use this request parameter, you do not use the <code>ckn</code> and <code>cak</code> request parameters.</p>"""
    ckn: NotRequired["capo_direct_connect.types.ckn.Ckn"]
    """<p>The MAC Security (MACsec) CKN to associate with the connection.</p> <p>You can create the CKN/CAK pair using an industry standard tool.</p> <p> The valid values are 64 hexadecimal characters (0-9, A-E).</p> <p>If you use this request parameter, you must use the <code>cak</code> request parameter and not use the <code>secretARN</code> request parameter.</p>"""
    cak: NotRequired["capo_direct_connect.types.cak.Cak"]
    """<p>The MAC Security (MACsec) CAK to associate with the connection.</p> <p>You can create the CKN/CAK pair using an industry standard tool.</p> <p> The valid values are 64 hexadecimal characters (0-9, A-E).</p> <p>If you use this request parameter, you must use the <code>ckn</code> request parameter and not use the <code>secretARN</code> request parameter.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: AssociateMacSecKeyRequest) -> dict:
    out: dict = {}
    out["connectionId"] = value["connection_id"]
    if "secret_arn" in value:
        out["secretARN"] = value["secret_arn"]
    if "ckn" in value:
        out["ckn"] = value["ckn"]
    if "cak" in value:
        out["cak"] = value["cak"]
    return out


def deserialize_aws_json_1_1(data: dict) -> AssociateMacSecKeyRequest:
    out: AssociateMacSecKeyRequest = {}  # type: ignore[typeddict-item]
    if data.get("connectionId") is not None:
        out["connection_id"] = data["connectionId"]
    else:
        out["connection_id"] = ""
    if data.get("secretARN") is not None:
        out["secret_arn"] = data["secretARN"]
    if data.get("ckn") is not None:
        out["ckn"] = data["ckn"]
    if data.get("cak") is not None:
        out["cak"] = data["cak"]
    return out
