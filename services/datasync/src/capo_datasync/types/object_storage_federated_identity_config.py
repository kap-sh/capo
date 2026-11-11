"""Generated from Smithy shape ``com.amazonaws.datasync#ObjectStorageFederatedIdentityConfig``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_datasync.types.iam_role_arn
    import capo_datasync.types.object_storage_external_identity_config


class ObjectStorageFederatedIdentityConfig(TypedDict, closed=True):
    aws_iam_role: NotRequired["capo_datasync.types.iam_role_arn.IamRoleArn"]
    """<p>Specifies the ARN for an Amazon Web Services role that allows DataSync to invoke STS GetWebIdentityToken API on behalf of the customer account and to obtain Amazon Web Services STS JWT (web token).</p>"""
    external_identity: NotRequired[
        "capo_datasync.types.object_storage_external_identity_config.ObjectStorageExternalIdentityConfig"
    ]
    """<p>Specifies cloud-provider-specific external identity parameters used when exchanging the Amazon Web Services web token for an OpenID Connect token at the object storage provider.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: ObjectStorageFederatedIdentityConfig) -> dict:
    out: dict = {}
    if "aws_iam_role" in value:
        out["AwsIamRole"] = value["aws_iam_role"]
    if "external_identity" in value:
        import capo_datasync.types.object_storage_external_identity_config

        out["ExternalIdentity"] = (
            capo_datasync.types.object_storage_external_identity_config.serialize_aws_json_1_1(
                value["external_identity"]
            )
        )
    return out


def deserialize_aws_json_1_1(data: dict) -> ObjectStorageFederatedIdentityConfig:
    out: ObjectStorageFederatedIdentityConfig = {}  # type: ignore[typeddict-item]
    if data.get("AwsIamRole") is not None:
        out["aws_iam_role"] = data["AwsIamRole"]
    if data.get("ExternalIdentity") is not None:
        import capo_datasync.types.object_storage_external_identity_config

        out["external_identity"] = (
            capo_datasync.types.object_storage_external_identity_config.deserialize_aws_json_1_1(
                data["ExternalIdentity"]
            )
        )
    return out
