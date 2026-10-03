"""Generated from Smithy shape ``com.amazonaws.route53domains#BillingRecord``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_route_53_domains.types.domain_name
    import capo_route_53_domains.types.invoice_id
    import capo_route_53_domains.types.operation_type
    import capo_route_53_domains.types.price
    import capo_route_53_domains.types.timestamp


class BillingRecord(TypedDict, closed=True):
    domain_name: NotRequired["capo_route_53_domains.types.domain_name.DomainName"]
    """<p>The name of the domain that the billing record applies to. If the domain name contains characters other than a-z, 0-9, and - (hyphen), such as an internationalized domain name, then this value is in Punycode. For more information, see <a href="https://docs.aws.amazon.com/Route53/latest/DeveloperGuide/DomainNameFormat.html">DNS Domain Name Format</a> in the <i>Amazon Route 53 Developer Guide</i>.</p>"""
    operation: NotRequired["capo_route_53_domains.types.operation_type.OperationType"]
    """<p>The operation that you were charged for.</p>"""
    invoice_id: NotRequired["capo_route_53_domains.types.invoice_id.InvoiceId"]
    """<p>Deprecated property. This field is retained in report structure for backwards compatibility, but will appear blank.</p>"""
    bill_date: NotRequired["capo_route_53_domains.types.timestamp.Timestamp"]
    """<p>The date that the operation was billed, in Unix format.</p>"""
    price: "capo_route_53_domains.types.price.Price"
    """<p>The price that you were charged for the operation, in US dollars.</p> <p>Example value: 12.0</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: BillingRecord) -> dict:
    out: dict = {}
    if "domain_name" in value:
        out["DomainName"] = value["domain_name"]
    if "operation" in value:
        import capo_route_53_domains.types.operation_type

        out["Operation"] = (
            capo_route_53_domains.types.operation_type.serialize_aws_json_1_1(
                value["operation"]
            )
        )
    if "invoice_id" in value:
        out["InvoiceId"] = value["invoice_id"]
    if "bill_date" in value:
        import capo_route_53_domains.types.timestamp

        out["BillDate"] = capo_route_53_domains.types.timestamp.serialize_aws_json_1_1(
            value["bill_date"]
        )
    out["Price"] = (
        "NaN"
        if value.get("price", 0) != value.get("price", 0)
        else "Infinity"
        if value.get("price", 0) == float("inf")
        else "-Infinity"
        if value.get("price", 0) == float("-inf")
        else value.get("price", 0)
    )
    return out


def deserialize_aws_json_1_1(data: dict) -> BillingRecord:
    out: BillingRecord = {}  # type: ignore[typeddict-item]
    if data.get("DomainName") is not None:
        out["domain_name"] = data["DomainName"]
    if data.get("Operation") is not None:
        import capo_route_53_domains.types.operation_type

        out["operation"] = (
            capo_route_53_domains.types.operation_type.deserialize_aws_json_1_1(
                data["Operation"]
            )
        )
    if data.get("InvoiceId") is not None:
        out["invoice_id"] = data["InvoiceId"]
    if data.get("BillDate") is not None:
        import capo_route_53_domains.types.timestamp

        out["bill_date"] = (
            capo_route_53_domains.types.timestamp.deserialize_aws_json_1_1(
                data["BillDate"]
            )
        )
    if data.get("Price") is not None:
        out["price"] = float(data["Price"])
    else:
        out["price"] = 0
    return out
