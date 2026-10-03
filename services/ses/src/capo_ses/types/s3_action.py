"""Generated from Smithy shape ``com.amazonaws.ses#S3Action``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

from capo_ses._protocol.xml import Element
from capo_ses.errors import DeserializationError

if TYPE_CHECKING:
    import capo_ses.types.amazon_resource_name
    import capo_ses.types.iam_role_arn
    import capo_ses.types.s3_bucket_name
    import capo_ses.types.s3_key_prefix


class S3Action(TypedDict, closed=True):
    topic_arn: NotRequired["capo_ses.types.amazon_resource_name.AmazonResourceName"]
    """<p>The ARN of the Amazon SNS topic to notify when the message is saved to the Amazon S3 bucket. You can find the ARN of a topic by using the <a href="https://docs.aws.amazon.com/sns/latest/api/API_ListTopics.html">ListTopics</a> operation in Amazon SNS.</p> <p>For more information about Amazon SNS topics, see the <a href="https://docs.aws.amazon.com/sns/latest/dg/CreateTopic.html">Amazon SNS Developer Guide</a>.</p>"""
    bucket_name: "capo_ses.types.s3_bucket_name.S3BucketName"
    """<p>The name of the Amazon S3 bucket for incoming email.</p>"""
    object_key_prefix: NotRequired["capo_ses.types.s3_key_prefix.S3KeyPrefix"]
    """<p>The key prefix of the Amazon S3 bucket. The key prefix is similar to a directory name that enables you to store similar data under the same directory in a bucket.</p>"""
    kms_key_arn: NotRequired["capo_ses.types.amazon_resource_name.AmazonResourceName"]
    """<p>The customer managed key that Amazon SES should use to encrypt your emails before saving them to the Amazon S3 bucket. You can use the Amazon Web Services managed key or a customer managed key that you created in Amazon Web Services KMS as follows:</p> <ul> <li> <p>To use the Amazon Web Services managed key, provide an ARN in the form of <code>arn:aws:kms:REGION:ACCOUNT-ID-WITHOUT-HYPHENS:alias/aws/ses</code>. For example, if your Amazon Web Services account ID is 123456789012 and you want to use the Amazon Web Services managed key in the US West (Oregon) Region, the ARN of the Amazon Web Services managed key would be <code>arn:aws:kms:us-west-2:123456789012:alias/aws/ses</code>. If you use the Amazon Web Services managed key, you don't need to perform any extra steps to give Amazon SES permission to use the key.</p> </li> <li> <p>To use a customer managed key that you created in Amazon Web Services KMS, provide the ARN of the customer managed key and ensure that you add a statement to your key's policy to give Amazon SES permission to use it. For more information about giving permissions, see the <a href="https://docs.aws.amazon.com/ses/latest/dg/receiving-email-permissions.html">Amazon SES Developer Guide</a>.</p> </li> </ul> <p>For more information about key policies, see the <a href="https://docs.aws.amazon.com/kms/latest/developerguide/concepts.html">Amazon Web Services KMS Developer Guide</a>. If you do not specify an Amazon Web Services KMS key, Amazon SES does not encrypt your emails.</p> <important> <p>Your mail is encrypted by Amazon SES using the Amazon S3 encryption client before the mail is submitted to Amazon S3 for storage. It is not encrypted using Amazon S3 server-side encryption. This means that you must use the Amazon S3 encryption client to decrypt the email after retrieving it from Amazon S3, as the service has no access to use your Amazon Web Services KMS keys for decryption. This encryption client is currently available with the <a href="http://aws.amazon.com/sdk-for-java/">Amazon Web Services SDK for Java</a> and <a href="http://aws.amazon.com/sdk-for-ruby/">Amazon Web Services SDK for Ruby</a> only. For more information about client-side encryption using Amazon Web Services KMS managed keys, see the <a href="https://docs.aws.amazon.com/AmazonS3/latest/dev/UsingClientSideEncryption.html">Amazon S3 Developer Guide</a>.</p> </important>"""
    iam_role_arn: NotRequired["capo_ses.types.iam_role_arn.IAMRoleARN"]
    """<p> The ARN of the IAM role to be used by Amazon Simple Email Service while writing to the Amazon S3 bucket, optionally encrypting your mail via the provided customer managed key, and publishing to the Amazon SNS topic. This role should have access to the following APIs: </p> <ul> <li> <p> <code>s3:PutObject</code>, <code>kms:Encrypt</code> and <code>kms:GenerateDataKey</code> for the given Amazon S3 bucket.</p> </li> <li> <p> <code>kms:GenerateDataKey</code> for the given Amazon Web Services KMS customer managed key. </p> </li> <li> <p> <code>sns:Publish</code> for the given Amazon SNS topic.</p> </li> </ul> <note> <p>If an IAM role ARN is provided, the role (and only the role) is used to access all the given resources (Amazon S3 bucket, Amazon Web Services KMS customer managed key and Amazon SNS topic). Therefore, setting up individual resource access permissions is not required.</p> </note>"""


# --- awsQuery ser/de ---
def serialize_query(value: S3Action, pairs: list[tuple[str, str]], prefix: str) -> None:
    key_prefix = f"{prefix}." if prefix else ""
    if "topic_arn" in value:
        pairs.append((f"{key_prefix}TopicArn", str(value["topic_arn"])))
    pairs.append((f"{key_prefix}BucketName", str(value["bucket_name"])))
    if "object_key_prefix" in value:
        pairs.append((f"{key_prefix}ObjectKeyPrefix", str(value["object_key_prefix"])))
    if "kms_key_arn" in value:
        pairs.append((f"{key_prefix}KmsKeyArn", str(value["kms_key_arn"])))
    if "iam_role_arn" in value:
        pairs.append((f"{key_prefix}IamRoleArn", str(value["iam_role_arn"])))


def deserialize_query(el: Element) -> S3Action:
    out: S3Action = {}  # type: ignore[typeddict-item]
    child_topic_arn = el.find("TopicArn")
    if child_topic_arn is not None:
        out["topic_arn"] = str(child_topic_arn.text or "")
    child_bucket_name = el.find("BucketName")
    if child_bucket_name is not None:
        out["bucket_name"] = str(child_bucket_name.text or "")
    else:
        raise DeserializationError("S3Action.bucket_name required")
    child_object_key_prefix = el.find("ObjectKeyPrefix")
    if child_object_key_prefix is not None:
        out["object_key_prefix"] = str(child_object_key_prefix.text or "")
    child_kms_key_arn = el.find("KmsKeyArn")
    if child_kms_key_arn is not None:
        out["kms_key_arn"] = str(child_kms_key_arn.text or "")
    child_iam_role_arn = el.find("IamRoleArn")
    if child_iam_role_arn is not None:
        out["iam_role_arn"] = str(child_iam_role_arn.text or "")
    return out
