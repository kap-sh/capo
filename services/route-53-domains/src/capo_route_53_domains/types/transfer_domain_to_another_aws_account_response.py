"""Generated from Smithy shape ``com.amazonaws.route53domains#TransferDomainToAnotherAwsAccountResponse``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_route_53_domains.types.operation_id
    import capo_route_53_domains.types.password


class TransferDomainToAnotherAwsAccountResponse(TypedDict, closed=True):
    operation_id: NotRequired["capo_route_53_domains.types.operation_id.OperationId"]
    """<p>Identifier for tracking the progress of the request. To query the operation status, use <a href="https://docs.aws.amazon.com/Route53/latest/APIReference/API_domains_GetOperationDetail.html">GetOperationDetail</a>.</p>"""
    password: NotRequired["capo_route_53_domains.types.password.Password"]
    """<p>To finish transferring a domain to another Amazon Web Services account, the account that the domain is being transferred to must submit an <a href="https://docs.aws.amazon.com/Route53/latest/APIReference/API_domains_AcceptDomainTransferFromAnotherAwsAccount.html">AcceptDomainTransferFromAnotherAwsAccount</a> request. The request must include the value of the <code>Password</code> element that was returned in the <code>TransferDomainToAnotherAwsAccount</code> response.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: TransferDomainToAnotherAwsAccountResponse) -> dict:
    out: dict = {}
    if "operation_id" in value:
        out["OperationId"] = value["operation_id"]
    if "password" in value:
        out["Password"] = value["password"]
    return out


def deserialize_aws_json_1_1(data: dict) -> TransferDomainToAnotherAwsAccountResponse:
    out: TransferDomainToAnotherAwsAccountResponse = {}  # type: ignore[typeddict-item]
    if data.get("OperationId") is not None:
        out["operation_id"] = data["OperationId"]
    if data.get("Password") is not None:
        out["password"] = data["Password"]
    return out
