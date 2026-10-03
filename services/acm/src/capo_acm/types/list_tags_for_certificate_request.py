"""Generated from Smithy shape ``com.amazonaws.acm#ListTagsForCertificateRequest``."""

from typing import TYPE_CHECKING

from typing_extensions import TypedDict

from capo_acm.errors import DeserializationError

if TYPE_CHECKING:
    import capo_acm.types.arn


class ListTagsForCertificateRequest(TypedDict, closed=True):
    certificate_arn: "capo_acm.types.arn.Arn"
    """<p>String that contains the ARN of the ACM certificate for which you want to list the tags. This must have the following form:</p> <p> <code>arn:aws:acm:region:123456789012:certificate/12345678-1234-1234-1234-123456789012</code> </p> <p>For more information about ARNs, see <a href="https://docs.aws.amazon.com/general/latest/gr/aws-arns-and-namespaces.html">Amazon Resource Names (ARNs)</a>.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: ListTagsForCertificateRequest) -> dict:
    out: dict = {}
    out["CertificateArn"] = value["certificate_arn"]
    return out


def deserialize_aws_json_1_1(data: dict) -> ListTagsForCertificateRequest:
    out: ListTagsForCertificateRequest = {}  # type: ignore[typeddict-item]
    if data.get("CertificateArn") is not None:
        out["certificate_arn"] = data["CertificateArn"]
    else:
        raise DeserializationError(
            "ListTagsForCertificateRequest.certificate_arn required"
        )
    return out
