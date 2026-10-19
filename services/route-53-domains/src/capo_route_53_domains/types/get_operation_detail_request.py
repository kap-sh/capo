"""Generated from Smithy shape ``com.amazonaws.route53domains#GetOperationDetailRequest``."""

from typing import TYPE_CHECKING

from typing_extensions import TypedDict

if TYPE_CHECKING:
    import capo_route_53_domains.types.operation_id


class GetOperationDetailRequest(TypedDict, closed=True):
    operation_id: "capo_route_53_domains.types.operation_id.OperationId"
    """<p>The identifier for the operation for which you want to get the status. Route 53 returned the identifier in the response to the original request.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: GetOperationDetailRequest) -> dict:
    out: dict = {}
    out["OperationId"] = value["operation_id"]
    return out


def deserialize_aws_json_1_1(data: dict) -> GetOperationDetailRequest:
    out: GetOperationDetailRequest = {}  # type: ignore[typeddict-item]
    if data.get("OperationId") is not None:
        out["operation_id"] = data["OperationId"]
    else:
        out["operation_id"] = ""
    return out
