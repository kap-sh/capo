"""Generated from Smithy shape ``com.amazonaws.codedeploy#DeleteGitHubAccountTokenInput``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_codedeploy.types.git_hub_account_token_name


class DeleteGitHubAccountTokenInput(TypedDict, closed=True):
    token_name: NotRequired[
        "capo_codedeploy.types.git_hub_account_token_name.GitHubAccountTokenName"
    ]
    """<p>The name of the GitHub account connection to delete.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: DeleteGitHubAccountTokenInput) -> dict:
    out: dict = {}
    if "token_name" in value:
        out["tokenName"] = value["token_name"]
    return out


def deserialize_aws_json_1_1(data: dict) -> DeleteGitHubAccountTokenInput:
    out: DeleteGitHubAccountTokenInput = {}  # type: ignore[typeddict-item]
    if data.get("tokenName") is not None:
        out["token_name"] = data["tokenName"]
    return out


# --- rpcv2Cbor ser/de ---
def serialize_cbor(value: DeleteGitHubAccountTokenInput) -> dict:
    out: dict = {}
    if "token_name" in value:
        out["tokenName"] = value["token_name"]
    return out


def deserialize_cbor(data: dict) -> DeleteGitHubAccountTokenInput:
    out: DeleteGitHubAccountTokenInput = {}  # type: ignore[typeddict-item]
    if data.get("tokenName") is not None:
        out["token_name"] = data["tokenName"]
    return out
