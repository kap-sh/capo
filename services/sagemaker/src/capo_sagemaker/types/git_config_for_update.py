"""Generated from Smithy shape ``com.amazonaws.sagemaker#GitConfigForUpdate``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_sagemaker.types.secret_arn


class GitConfigForUpdate(TypedDict, closed=True):
    secret_arn: NotRequired["capo_sagemaker.types.secret_arn.SecretArn"]
    """<p>The Amazon Resource Name (ARN) of the Amazon Web Services Secrets Manager secret that contains the credentials used to access the git repository. The secret must have a staging label of <code>AWSCURRENT</code> and must be in the following format:</p> <p> <code>{"username": <i>UserName</i>, "password": <i>Password</i>}</code> </p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: GitConfigForUpdate) -> dict:
    out: dict = {}
    if "secret_arn" in value:
        out["SecretArn"] = value["secret_arn"]
    return out


def deserialize_aws_json_1_1(data: dict) -> GitConfigForUpdate:
    out: GitConfigForUpdate = {}  # type: ignore[typeddict-item]
    if data.get("SecretArn") is not None:
        out["secret_arn"] = data["SecretArn"]
    return out
