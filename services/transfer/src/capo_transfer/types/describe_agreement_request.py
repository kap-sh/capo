"""Generated from Smithy shape ``com.amazonaws.transfer#DescribeAgreementRequest``."""

from typing import TYPE_CHECKING

from typing_extensions import TypedDict

if TYPE_CHECKING:
    import capo_transfer.types.agreement_id
    import capo_transfer.types.server_id


class DescribeAgreementRequest(TypedDict, closed=True):
    agreement_id: "capo_transfer.types.agreement_id.AgreementId"
    """<p>A unique identifier for the agreement. This identifier is returned when you create an agreement.</p>"""
    server_id: "capo_transfer.types.server_id.ServerId"
    """<p>The server identifier that's associated with the agreement.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: DescribeAgreementRequest) -> dict:
    out: dict = {}
    out["AgreementId"] = value["agreement_id"]
    out["ServerId"] = value["server_id"]
    return out


def deserialize_aws_json_1_1(data: dict) -> DescribeAgreementRequest:
    out: DescribeAgreementRequest = {}  # type: ignore[typeddict-item]
    if data.get("AgreementId") is not None:
        out["agreement_id"] = data["AgreementId"]
    else:
        out["agreement_id"] = ""
    if data.get("ServerId") is not None:
        out["server_id"] = data["ServerId"]
    else:
        out["server_id"] = ""
    return out
