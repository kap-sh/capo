"""Generated from Smithy shape ``com.amazonaws.paymentcryptography#TagResourceInput``."""

from typing import TYPE_CHECKING

from typing_extensions import TypedDict

from capo_payment_cryptography.errors import DeserializationError

if TYPE_CHECKING:
    import capo_payment_cryptography.types.resource_arn
    import capo_payment_cryptography.types.tags


class TagResourceInput(TypedDict, closed=True):
    resource_arn: "capo_payment_cryptography.types.resource_arn.ResourceArn"
    """<p>The <code>KeyARN</code> of the key whose tags are being updated.</p>"""
    tags: "capo_payment_cryptography.types.tags.Tags"
    """<p>One or more tags. Each tag consists of a tag key and a tag value. The tag value can be an empty (null) string. You can't have more than one tag on an Amazon Web Services Payment Cryptography key with the same tag key. If you specify an existing tag key with a different tag value, Amazon Web Services Payment Cryptography replaces the current tag value with the new one.</p> <important> <p>Don't include personal, confidential or sensitive information in this field. This field may be displayed in plaintext in CloudTrail logs and other output.</p> </important> <p>To use this parameter, you must have <a href="https://docs.aws.amazon.com/payment-cryptography/latest/APIReference/API_TagResource.html">TagResource</a> permission in an IAM policy.</p> <important> <p>Don't include personal, confidential or sensitive information in this field. This field may be displayed in plaintext in CloudTrail logs and other output.</p> </important>"""


# --- awsJson1_0 ser/de ---
def serialize_aws_json_1_0(value: TagResourceInput) -> dict:
    out: dict = {}
    out["ResourceArn"] = value["resource_arn"]
    import capo_payment_cryptography.types.tags

    out["Tags"] = capo_payment_cryptography.types.tags.serialize_aws_json_1_0(
        value["tags"]
    )
    return out


def deserialize_aws_json_1_0(data: dict) -> TagResourceInput:
    out: TagResourceInput = {}  # type: ignore[typeddict-item]
    if data.get("ResourceArn") is not None:
        out["resource_arn"] = data["ResourceArn"]
    else:
        raise DeserializationError("TagResourceInput.resource_arn required")
    if data.get("Tags") is not None:
        import capo_payment_cryptography.types.tags

        out["tags"] = capo_payment_cryptography.types.tags.deserialize_aws_json_1_0(
            data["Tags"]
        )
    else:
        raise DeserializationError("TagResourceInput.tags required")
    return out
