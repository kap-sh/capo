"""Generated from Smithy shape ``com.amazonaws.acm#ListCertificateDomainValidationsRequest``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_acm.types.certificate_arn
    import capo_acm.types.max_items
    import capo_acm.types.next_token


class ListCertificateDomainValidationsRequest(TypedDict, closed=True):
    certificate_arn: "capo_acm.types.certificate_arn.CertificateArn"
    """<p>The Amazon Resource Name (ARN) of the certificate for which to list domain validation summaries.</p>"""
    next_token: NotRequired["capo_acm.types.next_token.NextToken"]
    """<p>A token returned by a previous call to <code>ListCertificateDomainValidations</code>. If the number of results exceeds <code>MaxItems</code>, use this token to retrieve the next page of results.</p>"""
    max_items: NotRequired["capo_acm.types.max_items.MaxItems"]
    """<p>The maximum number of domain validation summaries to return. If you don't specify a value, the default is 1000.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: ListCertificateDomainValidationsRequest) -> dict:
    out: dict = {}
    out["CertificateArn"] = value["certificate_arn"]
    if "next_token" in value:
        out["NextToken"] = value["next_token"]
    if "max_items" in value:
        out["MaxItems"] = value["max_items"]
    return out


def deserialize_aws_json_1_1(data: dict) -> ListCertificateDomainValidationsRequest:
    out: ListCertificateDomainValidationsRequest = {}  # type: ignore[typeddict-item]
    if data.get("CertificateArn") is not None:
        out["certificate_arn"] = data["CertificateArn"]
    else:
        out["certificate_arn"] = ""
    if data.get("NextToken") is not None:
        out["next_token"] = data["NextToken"]
    if data.get("MaxItems") is not None:
        out["max_items"] = data["MaxItems"]
    return out
