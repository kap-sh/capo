"""Generated from Smithy shape ``com.amazonaws.firehose#KMSEncryptionConfig``."""

from typing import TYPE_CHECKING

from typing_extensions import TypedDict

from capo_firehose.errors import DeserializationError

if TYPE_CHECKING:
    import capo_firehose.types.awskms_key_arn


class KMSEncryptionConfig(TypedDict, closed=True):
    awskms_key_arn: "capo_firehose.types.awskms_key_arn.AWSKMSKeyARN"
    """<p>The Amazon Resource Name (ARN) of the encryption key. Must belong to the same Amazon Web Services Region as the destination Amazon S3 bucket. For more information, see <a href="https://docs.aws.amazon.com/general/latest/gr/aws-arns-and-namespaces.html">Amazon Resource Names (ARNs) and Amazon Web Services Service Namespaces</a>.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: KMSEncryptionConfig) -> dict:
    out: dict = {}
    out["AWSKMSKeyARN"] = value["awskms_key_arn"]
    return out


def deserialize_aws_json_1_1(data: dict) -> KMSEncryptionConfig:
    out: KMSEncryptionConfig = {}  # type: ignore[typeddict-item]
    if data.get("AWSKMSKeyARN") is not None:
        out["awskms_key_arn"] = data["AWSKMSKeyARN"]
    else:
        raise DeserializationError("KMSEncryptionConfig.awskms_key_arn required")
    return out
