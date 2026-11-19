"""Generated from Smithy shape ``com.amazonaws.codedeploy#ListGitHubAccountTokenNamesInput``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_codedeploy.types.next_token


class ListGitHubAccountTokenNamesInput(TypedDict, closed=True):
    next_token: NotRequired["capo_codedeploy.types.next_token.NextToken"]
    """<p>An identifier returned from the previous <code>ListGitHubAccountTokenNames</code> call. It can be used to return the next set of names in the list. </p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: ListGitHubAccountTokenNamesInput) -> dict:
    out: dict = {}
    if "next_token" in value:
        out["nextToken"] = value["next_token"]
    return out


def deserialize_aws_json_1_1(data: dict) -> ListGitHubAccountTokenNamesInput:
    out: ListGitHubAccountTokenNamesInput = {}  # type: ignore[typeddict-item]
    if data.get("nextToken") is not None:
        out["next_token"] = data["nextToken"]
    return out


# --- rpcv2Cbor ser/de ---
def serialize_cbor(value: ListGitHubAccountTokenNamesInput) -> dict:
    out: dict = {}
    if "next_token" in value:
        out["nextToken"] = value["next_token"]
    return out


def deserialize_cbor(data: dict) -> ListGitHubAccountTokenNamesInput:
    out: ListGitHubAccountTokenNamesInput = {}  # type: ignore[typeddict-item]
    if data.get("nextToken") is not None:
        out["next_token"] = data["nextToken"]
    return out
