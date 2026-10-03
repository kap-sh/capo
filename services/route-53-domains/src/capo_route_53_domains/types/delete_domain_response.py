"""Generated from Smithy shape ``com.amazonaws.route53domains#DeleteDomainResponse``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_route_53_domains.types.operation_id


class DeleteDomainResponse(TypedDict, closed=True):
    operation_id: NotRequired["capo_route_53_domains.types.operation_id.OperationId"]
    """<p>Identifier for tracking the progress of the request. To query the operation status, use <a href="https://docs.aws.amazon.com/Route53/latest/APIReference/API_domains_GetOperationDetail.html">GetOperationDetail</a>.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: DeleteDomainResponse) -> dict:
    out: dict = {}
    if "operation_id" in value:
        out["OperationId"] = value["operation_id"]
    return out


def deserialize_aws_json_1_1(data: dict) -> DeleteDomainResponse:
    out: DeleteDomainResponse = {}  # type: ignore[typeddict-item]
    if data.get("OperationId") is not None:
        out["operation_id"] = data["OperationId"]
    return out
