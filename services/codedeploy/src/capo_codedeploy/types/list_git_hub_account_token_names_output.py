"""Generated from Smithy shape ``com.amazonaws.codedeploy#ListGitHubAccountTokenNamesOutput``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_codedeploy.types.git_hub_account_token_name_list
    import capo_codedeploy.types.next_token


class ListGitHubAccountTokenNamesOutput(TypedDict, closed=True):
    token_name_list: NotRequired[
        "capo_codedeploy.types.git_hub_account_token_name_list.GitHubAccountTokenNameList"
    ]
    """<p>A list of names of connections to GitHub accounts.</p>"""
    next_token: NotRequired["capo_codedeploy.types.next_token.NextToken"]
    """<p>If a large amount of information is returned, an identifier is also returned. It can be used in a subsequent <code>ListGitHubAccountTokenNames</code> call to return the next set of names in the list. </p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: ListGitHubAccountTokenNamesOutput) -> dict:
    out: dict = {}
    if "token_name_list" in value:
        import capo_codedeploy.types.git_hub_account_token_name_list

        out["tokenNameList"] = (
            capo_codedeploy.types.git_hub_account_token_name_list.serialize_aws_json_1_1(
                value["token_name_list"]
            )
        )
    if "next_token" in value:
        out["nextToken"] = value["next_token"]
    return out


def deserialize_aws_json_1_1(data: dict) -> ListGitHubAccountTokenNamesOutput:
    out: ListGitHubAccountTokenNamesOutput = {}  # type: ignore[typeddict-item]
    if data.get("tokenNameList") is not None:
        import capo_codedeploy.types.git_hub_account_token_name_list

        out["token_name_list"] = (
            capo_codedeploy.types.git_hub_account_token_name_list.deserialize_aws_json_1_1(
                data["tokenNameList"]
            )
        )
    if data.get("nextToken") is not None:
        out["next_token"] = data["nextToken"]
    return out


# --- rpcv2Cbor ser/de ---
def serialize_cbor(value: ListGitHubAccountTokenNamesOutput) -> dict:
    out: dict = {}
    if "token_name_list" in value:
        import capo_codedeploy.types.git_hub_account_token_name_list

        out["tokenNameList"] = (
            capo_codedeploy.types.git_hub_account_token_name_list.serialize_cbor(
                value["token_name_list"]
            )
        )
    if "next_token" in value:
        out["nextToken"] = value["next_token"]
    return out


def deserialize_cbor(data: dict) -> ListGitHubAccountTokenNamesOutput:
    out: ListGitHubAccountTokenNamesOutput = {}  # type: ignore[typeddict-item]
    if data.get("tokenNameList") is not None:
        import capo_codedeploy.types.git_hub_account_token_name_list

        out["token_name_list"] = (
            capo_codedeploy.types.git_hub_account_token_name_list.deserialize_cbor(
                data["tokenNameList"]
            )
        )
    if data.get("nextToken") is not None:
        out["next_token"] = data["nextToken"]
    return out
