"""Generated from Smithy shape ``com.amazonaws.acm#RenewCertificateRequest``."""

from typing import TYPE_CHECKING

from typing_extensions import TypedDict

from capo_acm.errors import DeserializationError

if TYPE_CHECKING:
    import capo_acm.types.arn


class RenewCertificateRequest(TypedDict, closed=True):
    certificate_arn: "capo_acm.types.arn.Arn"
    """<p>String that contains the ARN of the ACM certificate to be renewed. This must be of the form:</p> <p> <code>arn:aws:acm:region:123456789012:certificate/12345678-1234-1234-1234-123456789012</code> </p> <p>For more information about ARNs, see <a href="https://docs.aws.amazon.com/general/latest/gr/aws-arns-and-namespaces.html">Amazon Resource Names (ARNs)</a>.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: RenewCertificateRequest) -> dict:
    out: dict = {}
    out["CertificateArn"] = value["certificate_arn"]
    return out


def deserialize_aws_json_1_1(data: dict) -> RenewCertificateRequest:
    out: RenewCertificateRequest = {}  # type: ignore[typeddict-item]
    if data.get("CertificateArn") is not None:
        out["certificate_arn"] = data["CertificateArn"]
    else:
        raise DeserializationError("RenewCertificateRequest.certificate_arn required")
    return out
