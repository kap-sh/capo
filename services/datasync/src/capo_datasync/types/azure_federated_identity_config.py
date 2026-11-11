"""Generated from Smithy shape ``com.amazonaws.datasync#AzureFederatedIdentityConfig``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_datasync.types.azure_oidc_config
    import capo_datasync.types.iam_role_arn


class AzureFederatedIdentityConfig(TypedDict, closed=True):
    aws_iam_role: NotRequired["capo_datasync.types.iam_role_arn.IamRoleArn"]
    """<p>Specifies the ARN for an Amazon Web Services role that allows DataSync to invoke STS GetWebIdentityToken API on behalf of the customer account and to obtain Amazon Web Services STS JWT (web token).</p>"""
    azure_oidc: NotRequired["capo_datasync.types.azure_oidc_config.AzureOidcConfig"]
    """<p>External identity parameters for Azure Blob Storage.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: AzureFederatedIdentityConfig) -> dict:
    out: dict = {}
    if "aws_iam_role" in value:
        out["AwsIamRole"] = value["aws_iam_role"]
    if "azure_oidc" in value:
        import capo_datasync.types.azure_oidc_config

        out["AzureOidc"] = capo_datasync.types.azure_oidc_config.serialize_aws_json_1_1(
            value["azure_oidc"]
        )
    return out


def deserialize_aws_json_1_1(data: dict) -> AzureFederatedIdentityConfig:
    out: AzureFederatedIdentityConfig = {}  # type: ignore[typeddict-item]
    if data.get("AwsIamRole") is not None:
        out["aws_iam_role"] = data["AwsIamRole"]
    if data.get("AzureOidc") is not None:
        import capo_datasync.types.azure_oidc_config

        out["azure_oidc"] = (
            capo_datasync.types.azure_oidc_config.deserialize_aws_json_1_1(
                data["AzureOidc"]
            )
        )
    return out
