"""Generated from Smithy shape ``com.amazonaws.cloudformation#TestTypeInput``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

from capo_cloudformation._protocol.xml import Element

if TYPE_CHECKING:
    import capo_cloudformation.types.s3_bucket
    import capo_cloudformation.types.third_party_type
    import capo_cloudformation.types.type_arn
    import capo_cloudformation.types.type_name
    import capo_cloudformation.types.type_version_id


class TestTypeInput(TypedDict, closed=True):
    arn: NotRequired["capo_cloudformation.types.type_arn.TypeArn"]
    """<p>The Amazon Resource Name (ARN) of the extension.</p> <p>Conditional: You must specify <code>Arn</code>, or <code>TypeName</code> and <code>Type</code>.</p>"""
    type: NotRequired["capo_cloudformation.types.third_party_type.ThirdPartyType"]
    """<p>The type of the extension to test.</p> <p>Conditional: You must specify <code>Arn</code>, or <code>TypeName</code> and <code>Type</code>.</p>"""
    type_name: NotRequired["capo_cloudformation.types.type_name.TypeName"]
    """<p>The name of the extension to test.</p> <p>Conditional: You must specify <code>Arn</code>, or <code>TypeName</code> and <code>Type</code>.</p>"""
    version_id: NotRequired["capo_cloudformation.types.type_version_id.TypeVersionId"]
    """<p>The version of the extension to test.</p> <p>You can specify the version id with either <code>Arn</code>, or with <code>TypeName</code> and <code>Type</code>.</p> <p>If you don't specify a version, CloudFormation uses the default version of the extension in this account and Region for testing.</p>"""
    log_delivery_bucket: NotRequired["capo_cloudformation.types.s3_bucket.S3Bucket"]
    """<p>The S3 bucket to which CloudFormation delivers the contract test execution logs.</p> <p>CloudFormation delivers the logs by the time contract testing has completed and the extension has been assigned a test type status of <code>PASSED</code> or <code>FAILED</code>.</p> <p>The user calling <code>TestType</code> must be able to access items in the specified S3 bucket. Specifically, the user needs the following permissions:</p> <ul> <li> <p> <code>GetObject</code> </p> </li> <li> <p> <code>PutObject</code> </p> </li> </ul> <p>For more information, see <a href="https://docs.aws.amazon.com/service-authorization/latest/reference/list_amazons3.html">Actions, Resources, and Condition Keys for Amazon S3</a> in the <i>Identity and Access Management User Guide</i>.</p>"""


# --- awsQuery ser/de ---
def serialize_query(
    value: TestTypeInput, pairs: list[tuple[str, str]], prefix: str
) -> None:
    key_prefix = f"{prefix}." if prefix else ""
    if "arn" in value:
        pairs.append((f"{key_prefix}Arn", str(value["arn"])))
    if "type" in value:
        import capo_cloudformation.types.third_party_type

        capo_cloudformation.types.third_party_type.serialize_query(
            value["type"], pairs, f"{key_prefix}Type"
        )
    if "type_name" in value:
        pairs.append((f"{key_prefix}TypeName", str(value["type_name"])))
    if "version_id" in value:
        pairs.append((f"{key_prefix}VersionId", str(value["version_id"])))
    if "log_delivery_bucket" in value:
        pairs.append(
            (f"{key_prefix}LogDeliveryBucket", str(value["log_delivery_bucket"]))
        )


def deserialize_query(el: Element) -> TestTypeInput:
    out: TestTypeInput = {}  # type: ignore[typeddict-item]
    child_arn = el.find("Arn")
    if child_arn is not None:
        out["arn"] = str(child_arn.text or "")
    child_type = el.find("Type")
    if child_type is not None:
        import capo_cloudformation.types.third_party_type

        out["type"] = capo_cloudformation.types.third_party_type.deserialize_query(
            child_type
        )
    child_type_name = el.find("TypeName")
    if child_type_name is not None:
        out["type_name"] = str(child_type_name.text or "")
    child_version_id = el.find("VersionId")
    if child_version_id is not None:
        out["version_id"] = str(child_version_id.text or "")
    child_log_delivery_bucket = el.find("LogDeliveryBucket")
    if child_log_delivery_bucket is not None:
        out["log_delivery_bucket"] = str(child_log_delivery_bucket.text or "")
    return out
