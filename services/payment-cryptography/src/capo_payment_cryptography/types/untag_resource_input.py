"""Generated from Smithy shape ``com.amazonaws.paymentcryptography#UntagResourceInput``."""

from typing import TYPE_CHECKING

from typing_extensions import TypedDict

from capo_payment_cryptography.errors import DeserializationError

if TYPE_CHECKING:
    import capo_payment_cryptography.types.resource_arn
    import capo_payment_cryptography.types.tag_keys


class UntagResourceInput(TypedDict, closed=True):
    resource_arn: "capo_payment_cryptography.types.resource_arn.ResourceArn"
    """<p>The <code>KeyARN</code> of the key whose tags are being removed.</p>"""
    tag_keys: "capo_payment_cryptography.types.tag_keys.TagKeys"
    """<p>One or more tag keys. Don't include the tag values.</p> <p>If the Amazon Web Services Payment Cryptography key doesn't have the specified tag key, Amazon Web Services Payment Cryptography doesn't throw an exception or return a response. To confirm that the operation succeeded, use the <a href="https://docs.aws.amazon.com/payment-cryptography/latest/APIReference/API_ListTagsForResource.html">ListTagsForResource</a> operation.</p>"""


# --- awsJson1_0 ser/de ---
def serialize_aws_json_1_0(value: UntagResourceInput) -> dict:
    out: dict = {}
    out["ResourceArn"] = value["resource_arn"]
    import capo_payment_cryptography.types.tag_keys

    out["TagKeys"] = capo_payment_cryptography.types.tag_keys.serialize_aws_json_1_0(
        value["tag_keys"]
    )
    return out


def deserialize_aws_json_1_0(data: dict) -> UntagResourceInput:
    out: UntagResourceInput = {}  # type: ignore[typeddict-item]
    if data.get("ResourceArn") is not None:
        out["resource_arn"] = data["ResourceArn"]
    else:
        raise DeserializationError("UntagResourceInput.resource_arn required")
    if data.get("TagKeys") is not None:
        import capo_payment_cryptography.types.tag_keys

        out["tag_keys"] = (
            capo_payment_cryptography.types.tag_keys.deserialize_aws_json_1_0(
                data["TagKeys"]
            )
        )
    else:
        raise DeserializationError("UntagResourceInput.tag_keys required")
    return out
