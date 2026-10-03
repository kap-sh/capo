"""Generated from Smithy shape ``com.amazonaws.lambda#FunctionCodeLocation``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_lambda.types.function_code_location_error
    import capo_lambda.types.kms_key_arn
    import capo_lambda.types.resolved_s3_object
    import capo_lambda.types.sensitive_string_on_server_only
    import capo_lambda.types.string


class FunctionCodeLocation(TypedDict, closed=True):
    repository_type: NotRequired["capo_lambda.types.string.String"]
    """<p>The service that's hosting the file.</p>"""
    location: NotRequired[
        "capo_lambda.types.sensitive_string_on_server_only.SensitiveStringOnServerOnly"
    ]
    """<p>A presigned URL that you can use to download the deployment package.</p>"""
    image_uri: NotRequired["capo_lambda.types.string.String"]
    """<p>URI of a container image in the Amazon ECR registry.</p>"""
    resolved_image_uri: NotRequired["capo_lambda.types.string.String"]
    """<p>The resolved URI for the image.</p>"""
    resolved_s3_object: NotRequired[
        "capo_lambda.types.resolved_s3_object.ResolvedS3Object"
    ]
    """<p>The resolved Amazon S3 object that contains the deployment package.</p>"""
    source_kms_key_arn: NotRequired["capo_lambda.types.kms_key_arn.KMSKeyArn"]
    """<p>The ARN of the Key Management Service (KMS) customer managed key that's used to encrypt your function's .zip deployment package. If you don't provide a customer managed key, Lambda uses an <a href="https://docs.aws.amazon.com/kms/latest/developerguide/concepts.html#aws-owned-cmk">Amazon Web Services owned key</a>.</p>"""
    error: NotRequired[
        "capo_lambda.types.function_code_location_error.FunctionCodeLocationError"
    ]
    """<p>An object that contains details about an error related to function deployment package retrieval.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: FunctionCodeLocation) -> dict:
    out: dict = {}
    if "repository_type" in value:
        out["RepositoryType"] = value["repository_type"]
    if "location" in value:
        out["Location"] = value["location"]
    if "image_uri" in value:
        out["ImageUri"] = value["image_uri"]
    if "resolved_image_uri" in value:
        out["ResolvedImageUri"] = value["resolved_image_uri"]
    if "resolved_s3_object" in value:
        import capo_lambda.types.resolved_s3_object

        out["ResolvedS3Object"] = capo_lambda.types.resolved_s3_object.serialize_json(
            value["resolved_s3_object"]
        )
    if "source_kms_key_arn" in value:
        out["SourceKMSKeyArn"] = value["source_kms_key_arn"]
    if "error" in value:
        import capo_lambda.types.function_code_location_error

        out["Error"] = capo_lambda.types.function_code_location_error.serialize_json(
            value["error"]
        )
    return out


def deserialize_json(data: dict) -> FunctionCodeLocation:
    out: FunctionCodeLocation = {}  # type: ignore[typeddict-item]
    if data.get("RepositoryType") is not None:
        out["repository_type"] = data["RepositoryType"]
    if data.get("Location") is not None:
        out["location"] = data["Location"]
    if data.get("ImageUri") is not None:
        out["image_uri"] = data["ImageUri"]
    if data.get("ResolvedImageUri") is not None:
        out["resolved_image_uri"] = data["ResolvedImageUri"]
    if data.get("ResolvedS3Object") is not None:
        import capo_lambda.types.resolved_s3_object

        out["resolved_s3_object"] = (
            capo_lambda.types.resolved_s3_object.deserialize_json(
                data["ResolvedS3Object"]
            )
        )
    if data.get("SourceKMSKeyArn") is not None:
        out["source_kms_key_arn"] = data["SourceKMSKeyArn"]
    if data.get("Error") is not None:
        import capo_lambda.types.function_code_location_error

        out["error"] = capo_lambda.types.function_code_location_error.deserialize_json(
            data["Error"]
        )
    return out
