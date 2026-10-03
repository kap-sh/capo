"""Generated from Smithy shape ``com.amazonaws.acm#AddTagsToCertificateRequest``."""

from typing import TYPE_CHECKING

from typing_extensions import TypedDict

from capo_acm.errors import DeserializationError

if TYPE_CHECKING:
    import capo_acm.types.arn
    import capo_acm.types.tag_list


class AddTagsToCertificateRequest(TypedDict, closed=True):
    certificate_arn: "capo_acm.types.arn.Arn"
    """<p>String that contains the ARN of the ACM certificate to which the tag is to be applied. This must be of the form:</p> <p> <code>arn:aws:acm:region:123456789012:certificate/12345678-1234-1234-1234-123456789012</code> </p> <p>For more information about ARNs, see <a href="https://docs.aws.amazon.com/general/latest/gr/aws-arns-and-namespaces.html">Amazon Resource Names (ARNs)</a>.</p>"""
    tags: "capo_acm.types.tag_list.TagList"
    """<p>The key-value pair that defines the tag. The tag value is optional.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: AddTagsToCertificateRequest) -> dict:
    out: dict = {}
    out["CertificateArn"] = value["certificate_arn"]
    import capo_acm.types.tag_list

    out["Tags"] = capo_acm.types.tag_list.serialize_aws_json_1_1(value["tags"])
    return out


def deserialize_aws_json_1_1(data: dict) -> AddTagsToCertificateRequest:
    out: AddTagsToCertificateRequest = {}  # type: ignore[typeddict-item]
    if data.get("CertificateArn") is not None:
        out["certificate_arn"] = data["CertificateArn"]
    else:
        raise DeserializationError(
            "AddTagsToCertificateRequest.certificate_arn required"
        )
    if data.get("Tags") is not None:
        import capo_acm.types.tag_list

        out["tags"] = capo_acm.types.tag_list.deserialize_aws_json_1_1(data["Tags"])
    else:
        raise DeserializationError("AddTagsToCertificateRequest.tags required")
    return out
