"""Generated from Smithy shape ``com.amazonaws.omics#RegistryMapping``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_omics.types.aws_account_id
    import capo_omics.types.ecr_repository_prefix
    import capo_omics.types.secret_arn
    import capo_omics.types.upstream_repository_prefix
    import capo_omics.types.uri


class RegistryMapping(TypedDict, closed=True):
    upstream_registry_url: NotRequired["capo_omics.types.uri.Uri"]
    """<p>The URI of the upstream registry.</p>"""
    ecr_repository_prefix: NotRequired[
        "capo_omics.types.ecr_repository_prefix.EcrRepositoryPrefix"
    ]
    """<p>The repository prefix to use in the ECR private repository.</p>"""
    upstream_repository_prefix: NotRequired[
        "capo_omics.types.upstream_repository_prefix.UpstreamRepositoryPrefix"
    ]
    """<p>The repository prefix of the corresponding repository in the upstream registry.</p>"""
    ecr_account_id: NotRequired["capo_omics.types.aws_account_id.AwsAccountId"]
    """<p>Account ID of the account that owns the upstream container image.</p>"""
    credential_arn: NotRequired["capo_omics.types.secret_arn.SecretArn"]
    """<p>The Amazon Resource Name (ARN) of the Amazon Web Services Secrets Manager secret that holds the credentials for the upstream registry. You must specify this value when Amazon Elastic Container Registry (Amazon ECR) doesn't support pull through cache for the upstream registry. HealthOmics supports only some of these registries. The workflow role must have permission to call the <code>secretsmanager:GetSecretValue</code> operation on the secret. For more information about the supported registries, see <a href="https://docs.aws.amazon.com/omics/latest/dev/workflows-ecr.html">Container images</a> in the <i>Amazon Web Services HealthOmics User Guide</i>.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: RegistryMapping) -> dict:
    out: dict = {}
    if "upstream_registry_url" in value:
        out["upstreamRegistryUrl"] = value["upstream_registry_url"]
    if "ecr_repository_prefix" in value:
        out["ecrRepositoryPrefix"] = value["ecr_repository_prefix"]
    if "upstream_repository_prefix" in value:
        out["upstreamRepositoryPrefix"] = value["upstream_repository_prefix"]
    if "ecr_account_id" in value:
        out["ecrAccountId"] = value["ecr_account_id"]
    if "credential_arn" in value:
        out["credentialArn"] = value["credential_arn"]
    return out


def deserialize_json(data: dict) -> RegistryMapping:
    out: RegistryMapping = {}  # type: ignore[typeddict-item]
    if data.get("upstreamRegistryUrl") is not None:
        out["upstream_registry_url"] = data["upstreamRegistryUrl"]
    if data.get("ecrRepositoryPrefix") is not None:
        out["ecr_repository_prefix"] = data["ecrRepositoryPrefix"]
    if data.get("upstreamRepositoryPrefix") is not None:
        out["upstream_repository_prefix"] = data["upstreamRepositoryPrefix"]
    if data.get("ecrAccountId") is not None:
        out["ecr_account_id"] = data["ecrAccountId"]
    if data.get("credentialArn") is not None:
        out["credential_arn"] = data["credentialArn"]
    return out
