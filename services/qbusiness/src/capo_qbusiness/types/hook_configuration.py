"""Generated from Smithy shape ``com.amazonaws.qbusiness#HookConfiguration``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_qbusiness.types.document_attribute_condition
    import capo_qbusiness.types.lambda_arn
    import capo_qbusiness.types.role_arn
    import capo_qbusiness.types.s3_bucket_name


class HookConfiguration(TypedDict, closed=True):
    invocation_condition: NotRequired[
        "capo_qbusiness.types.document_attribute_condition.DocumentAttributeCondition"
    ]
    """<p>The condition used for when a Lambda function should be invoked.</p> <p>For example, you can specify a condition that if there are empty date-time values, then Amazon Q Business should invoke a function that inserts the current date-time.</p>"""
    lambda_arn: NotRequired["capo_qbusiness.types.lambda_arn.LambdaArn"]
    """<p>The Amazon Resource Name (ARN) of the Lambda function during ingestion. For more information, see <a href="https://docs.aws.amazon.com/amazonq/latest/qbusiness-ug/cde-lambda-operations.html">Using Lambda functions for Amazon Q Business document enrichment</a>.</p>"""
    s3_bucket_name: NotRequired["capo_qbusiness.types.s3_bucket_name.S3BucketName"]
    """<p>Stores the original, raw documents or the structured, parsed documents before and after altering them. For more information, see <a href="https://docs.aws.amazon.com/amazonq/latest/business-use-dg/cde-lambda-operations.html#cde-lambda-operations-data-contracts">Data contracts for Lambda functions</a>.</p>"""
    role_arn: NotRequired["capo_qbusiness.types.role_arn.RoleArn"]
    """<p>The Amazon Resource Name (ARN) of a role with permission to run <code>PreExtractionHookConfiguration</code> and <code>PostExtractionHookConfiguration</code> for altering document metadata and content during the document ingestion process.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: HookConfiguration) -> dict:
    out: dict = {}
    if "invocation_condition" in value:
        import capo_qbusiness.types.document_attribute_condition

        out["invocationCondition"] = (
            capo_qbusiness.types.document_attribute_condition.serialize_json(
                value["invocation_condition"]
            )
        )
    if "lambda_arn" in value:
        out["lambdaArn"] = value["lambda_arn"]
    if "s3_bucket_name" in value:
        out["s3BucketName"] = value["s3_bucket_name"]
    if "role_arn" in value:
        out["roleArn"] = value["role_arn"]
    return out


def deserialize_json(data: dict) -> HookConfiguration:
    out: HookConfiguration = {}  # type: ignore[typeddict-item]
    if data.get("invocationCondition") is not None:
        import capo_qbusiness.types.document_attribute_condition

        out["invocation_condition"] = (
            capo_qbusiness.types.document_attribute_condition.deserialize_json(
                data["invocationCondition"]
            )
        )
    if data.get("lambdaArn") is not None:
        out["lambda_arn"] = data["lambdaArn"]
    if data.get("s3BucketName") is not None:
        out["s3_bucket_name"] = data["s3BucketName"]
    if data.get("roleArn") is not None:
        out["role_arn"] = data["roleArn"]
    return out
