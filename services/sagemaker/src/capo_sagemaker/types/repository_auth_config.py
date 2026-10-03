"""Generated from Smithy shape ``com.amazonaws.sagemaker#RepositoryAuthConfig``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_sagemaker.types.repository_credentials_provider_arn


class RepositoryAuthConfig(TypedDict, closed=True):
    repository_credentials_provider_arn: NotRequired[
        "capo_sagemaker.types.repository_credentials_provider_arn.RepositoryCredentialsProviderArn"
    ]
    """<p>The Amazon Resource Name (ARN) of an Amazon Web Services Lambda function that provides credentials to authenticate to the private Docker registry where your model image is hosted. For information about how to create an Amazon Web Services Lambda function, see <a href="https://docs.aws.amazon.com/lambda/latest/dg/getting-started-create-function.html">Create a Lambda function with the console</a> in the <i>Amazon Web Services Lambda Developer Guide</i>.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: RepositoryAuthConfig) -> dict:
    out: dict = {}
    if "repository_credentials_provider_arn" in value:
        out["RepositoryCredentialsProviderArn"] = value[
            "repository_credentials_provider_arn"
        ]
    return out


def deserialize_aws_json_1_1(data: dict) -> RepositoryAuthConfig:
    out: RepositoryAuthConfig = {}  # type: ignore[typeddict-item]
    if data.get("RepositoryCredentialsProviderArn") is not None:
        out["repository_credentials_provider_arn"] = data[
            "RepositoryCredentialsProviderArn"
        ]
    return out
