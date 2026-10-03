"""Generated from Smithy shape ``com.amazonaws.s3control#LambdaInvokeOperation``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

from capo_s3_control._protocol.xml import Element, SubElement

if TYPE_CHECKING:
    import capo_s3_control.types.function_arn_string
    import capo_s3_control.types.non_empty_max_length64_string
    import capo_s3_control.types.user_arguments


class LambdaInvokeOperation(TypedDict, closed=True):
    function_arn: NotRequired[
        "capo_s3_control.types.function_arn_string.FunctionArnString"
    ]
    """<p>The Amazon Resource Name (ARN) for the Lambda function that the specified job will invoke on every object in the manifest.</p>"""
    invocation_schema_version: NotRequired[
        "capo_s3_control.types.non_empty_max_length64_string.NonEmptyMaxLength64String"
    ]
    """<p>Specifies the schema version for the payload that Batch Operations sends when invoking an Lambda function. Version <code>1.0</code> is the default. Version <code>2.0</code> is required when you use Batch Operations to invoke Lambda functions that act on directory buckets, or if you need to specify <code>UserArguments</code>. For more information, see <a href="https://aws.amazon.com/blogs/storage/automate-object-processing-in-amazon-s3-directory-buckets-with-s3-batch-operations-and-aws-lambda/">Automate object processing in Amazon S3 directory buckets with S3 Batch Operations and Lambda</a> in the <i>Amazon Web Services Storage Blog</i>.</p> <important> <p>Ensure that your Lambda function code expects <code>InvocationSchemaVersion</code> <b>2.0</b> and uses bucket name rather than bucket ARN. If the <code>InvocationSchemaVersion</code> does not match what your Lambda function expects, your function might not work as expected.</p> </important> <note> <p> <b>Directory buckets</b> - To initiate Amazon Web Services Lambda function to perform custom actions on objects in directory buckets, you must specify <code>2.0</code>.</p> </note>"""
    user_arguments: NotRequired["capo_s3_control.types.user_arguments.UserArguments"]
    """<p>Key-value pairs that are passed in the payload that Batch Operations sends when invoking an Lambda function. You must specify <code>InvocationSchemaVersion</code> <b>2.0</b> for <code>LambdaInvoke</code> operations that include <code>UserArguments</code>. For more information, see <a href="https://aws.amazon.com/blogs/storage/automate-object-processing-in-amazon-s3-directory-buckets-with-s3-batch-operations-and-aws-lambda/">Automate object processing in Amazon S3 directory buckets with S3 Batch Operations and Lambda</a> in the <i>Amazon Web Services Storage Blog</i>.</p>"""


# --- restXml ser/de ---
def serialize_xml(value: LambdaInvokeOperation, parent: Element, tag: str) -> None:
    el = SubElement(parent, tag)
    if "function_arn" in value:
        SubElement(el, "FunctionArn").text = str(value["function_arn"])
    if "invocation_schema_version" in value:
        SubElement(el, "InvocationSchemaVersion").text = str(
            value["invocation_schema_version"]
        )
    if "user_arguments" in value:
        import capo_s3_control.types.user_arguments

        capo_s3_control.types.user_arguments.serialize_xml(
            value["user_arguments"], el, "UserArguments"
        )


def deserialize_xml(el: Element) -> LambdaInvokeOperation:
    out: LambdaInvokeOperation = {}  # type: ignore[typeddict-item]
    child_function_arn = el.find("FunctionArn")
    if child_function_arn is not None:
        out["function_arn"] = str(child_function_arn.text or "")
    child_invocation_schema_version = el.find("InvocationSchemaVersion")
    if child_invocation_schema_version is not None:
        out["invocation_schema_version"] = str(
            child_invocation_schema_version.text or ""
        )
    child_user_arguments = el.find("UserArguments")
    if child_user_arguments is not None:
        import capo_s3_control.types.user_arguments

        out["user_arguments"] = capo_s3_control.types.user_arguments.deserialize_xml(
            child_user_arguments
        )
    return out
