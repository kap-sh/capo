"""Generated from Smithy shape ``com.amazonaws.codedeploy#DeleteGitHubAccountTokenOutput``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_codedeploy.types.git_hub_account_token_name


class DeleteGitHubAccountTokenOutput(TypedDict, closed=True):
    token_name: NotRequired[
        "capo_codedeploy.types.git_hub_account_token_name.GitHubAccountTokenName"
    ]
    """<p>The name of the GitHub account connection that was deleted.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: DeleteGitHubAccountTokenOutput) -> dict:
    out: dict = {}
    if "token_name" in value:
        out["tokenName"] = value["token_name"]
    return out


def deserialize_aws_json_1_1(data: dict) -> DeleteGitHubAccountTokenOutput:
    out: DeleteGitHubAccountTokenOutput = {}  # type: ignore[typeddict-item]
    if data.get("tokenName") is not None:
        out["token_name"] = data["tokenName"]
    return out


# --- rpcv2Cbor ser/de ---
def serialize_cbor(value: DeleteGitHubAccountTokenOutput) -> dict:
    out: dict = {}
    if "token_name" in value:
        out["tokenName"] = value["token_name"]
    return out


def deserialize_cbor(data: dict) -> DeleteGitHubAccountTokenOutput:
    out: DeleteGitHubAccountTokenOutput = {}  # type: ignore[typeddict-item]
    if data.get("tokenName") is not None:
        out["token_name"] = data["tokenName"]
    return out
