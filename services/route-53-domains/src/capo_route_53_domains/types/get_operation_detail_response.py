"""Generated from Smithy shape ``com.amazonaws.route53domains#GetOperationDetailResponse``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_route_53_domains.types.domain_name
    import capo_route_53_domains.types.error_message
    import capo_route_53_domains.types.operation_id
    import capo_route_53_domains.types.operation_status
    import capo_route_53_domains.types.operation_type
    import capo_route_53_domains.types.status_flag
    import capo_route_53_domains.types.timestamp


class GetOperationDetailResponse(TypedDict, closed=True):
    operation_id: NotRequired["capo_route_53_domains.types.operation_id.OperationId"]
    """<p>The identifier for the operation.</p>"""
    status: NotRequired["capo_route_53_domains.types.operation_status.OperationStatus"]
    """<p>The current status of the requested operation in the system.</p>"""
    message: NotRequired["capo_route_53_domains.types.error_message.ErrorMessage"]
    """<p>Detailed information on the status including possible errors.</p>"""
    domain_name: NotRequired["capo_route_53_domains.types.domain_name.DomainName"]
    """<p>The name of a domain.</p>"""
    type: NotRequired["capo_route_53_domains.types.operation_type.OperationType"]
    """<p>The type of operation that was requested.</p>"""
    submitted_date: NotRequired["capo_route_53_domains.types.timestamp.Timestamp"]
    """<p>The date when the request was submitted.</p>"""
    last_updated_date: NotRequired["capo_route_53_domains.types.timestamp.Timestamp"]
    """<p> The date when the operation was last updated. </p>"""
    status_flag: NotRequired["capo_route_53_domains.types.status_flag.StatusFlag"]
    """<p> Lists any outstanding operations that require customer action. Valid values are:</p> <ul> <li> <p> <code>PENDING_ACCEPTANCE</code>: The operation is waiting for acceptance from the account that is receiving the domain.</p> </li> <li> <p> <code>PENDING_CUSTOMER_ACTION</code>: The operation is waiting for customer action, for example, returning an email.</p> </li> <li> <p> <code>PENDING_AUTHORIZATION</code>: The operation is waiting for the form of authorization. For more information, see <a href="https://docs.aws.amazon.com/Route53/latest/APIReference/API_domains_ResendOperationAuthorization.html">ResendOperationAuthorization</a>.</p> </li> <li> <p> <code>PENDING_PAYMENT_VERIFICATION</code>: The operation is waiting for the payment method to validate.</p> </li> <li> <p> <code>PENDING_SUPPORT_CASE</code>: The operation includes a support case and is waiting for its resolution.</p> </li> </ul>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: GetOperationDetailResponse) -> dict:
    out: dict = {}
    if "operation_id" in value:
        out["OperationId"] = value["operation_id"]
    if "status" in value:
        import capo_route_53_domains.types.operation_status

        out["Status"] = (
            capo_route_53_domains.types.operation_status.serialize_aws_json_1_1(
                value["status"]
            )
        )
    if "message" in value:
        out["Message"] = value["message"]
    if "domain_name" in value:
        out["DomainName"] = value["domain_name"]
    if "type" in value:
        import capo_route_53_domains.types.operation_type

        out["Type"] = capo_route_53_domains.types.operation_type.serialize_aws_json_1_1(
            value["type"]
        )
    if "submitted_date" in value:
        import capo_route_53_domains.types.timestamp

        out["SubmittedDate"] = (
            capo_route_53_domains.types.timestamp.serialize_aws_json_1_1(
                value["submitted_date"]
            )
        )
    if "last_updated_date" in value:
        import capo_route_53_domains.types.timestamp

        out["LastUpdatedDate"] = (
            capo_route_53_domains.types.timestamp.serialize_aws_json_1_1(
                value["last_updated_date"]
            )
        )
    if "status_flag" in value:
        import capo_route_53_domains.types.status_flag

        out["StatusFlag"] = (
            capo_route_53_domains.types.status_flag.serialize_aws_json_1_1(
                value["status_flag"]
            )
        )
    return out


def deserialize_aws_json_1_1(data: dict) -> GetOperationDetailResponse:
    out: GetOperationDetailResponse = {}  # type: ignore[typeddict-item]
    if data.get("OperationId") is not None:
        out["operation_id"] = data["OperationId"]
    if data.get("Status") is not None:
        import capo_route_53_domains.types.operation_status

        out["status"] = (
            capo_route_53_domains.types.operation_status.deserialize_aws_json_1_1(
                data["Status"]
            )
        )
    if data.get("Message") is not None:
        out["message"] = data["Message"]
    if data.get("DomainName") is not None:
        out["domain_name"] = data["DomainName"]
    if data.get("Type") is not None:
        import capo_route_53_domains.types.operation_type

        out["type"] = (
            capo_route_53_domains.types.operation_type.deserialize_aws_json_1_1(
                data["Type"]
            )
        )
    if data.get("SubmittedDate") is not None:
        import capo_route_53_domains.types.timestamp

        out["submitted_date"] = (
            capo_route_53_domains.types.timestamp.deserialize_aws_json_1_1(
                data["SubmittedDate"]
            )
        )
    if data.get("LastUpdatedDate") is not None:
        import capo_route_53_domains.types.timestamp

        out["last_updated_date"] = (
            capo_route_53_domains.types.timestamp.deserialize_aws_json_1_1(
                data["LastUpdatedDate"]
            )
        )
    if data.get("StatusFlag") is not None:
        import capo_route_53_domains.types.status_flag

        out["status_flag"] = (
            capo_route_53_domains.types.status_flag.deserialize_aws_json_1_1(
                data["StatusFlag"]
            )
        )
    return out
