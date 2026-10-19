"""Generated from Smithy shape ``com.amazonaws.proton#Repository``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_proton.types.arn
    import capo_proton.types.repository_arn
    import capo_proton.types.repository_name
    import capo_proton.types.repository_provider


class Repository(TypedDict, closed=True):
    arn: "capo_proton.types.repository_arn.RepositoryArn"
    """<p>The Amazon Resource Name (ARN) of the linked repository.</p>"""
    provider: "capo_proton.types.repository_provider.RepositoryProvider"
    """<p>The repository provider.</p>"""
    name: "capo_proton.types.repository_name.RepositoryName"
    """<p>The repository name.</p>"""
    connection_arn: "capo_proton.types.arn.Arn"
    """<p>The Amazon Resource Name (ARN) of your AWS CodeStar connection that connects Proton to your repository provider account.</p>"""
    encryption_key: NotRequired["capo_proton.types.arn.Arn"]
    """<p>Your customer Amazon Web Services KMS encryption key.</p>"""


# --- awsJson1_0 ser/de ---
def serialize_aws_json_1_0(value: Repository) -> dict:
    out: dict = {}
    out["arn"] = value["arn"]
    out["provider"] = value["provider"]
    out["name"] = value["name"]
    out["connectionArn"] = value["connection_arn"]
    if "encryption_key" in value:
        out["encryptionKey"] = value["encryption_key"]
    return out


def deserialize_aws_json_1_0(data: dict) -> Repository:
    out: Repository = {}  # type: ignore[typeddict-item]
    if data.get("arn") is not None:
        out["arn"] = data["arn"]
    else:
        out["arn"] = ""
    if data.get("provider") is not None:
        out["provider"] = data["provider"]
    else:
        out["provider"] = ""
    if data.get("name") is not None:
        out["name"] = data["name"]
    else:
        out["name"] = ""
    if data.get("connectionArn") is not None:
        out["connection_arn"] = data["connectionArn"]
    else:
        out["connection_arn"] = ""
    if data.get("encryptionKey") is not None:
        out["encryption_key"] = data["encryptionKey"]
    return out
