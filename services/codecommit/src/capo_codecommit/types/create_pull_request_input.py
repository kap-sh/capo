"""Generated from Smithy shape ``com.amazonaws.codecommit#CreatePullRequestInput``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_codecommit.types.client_request_token
    import capo_codecommit.types.description
    import capo_codecommit.types.target_list
    import capo_codecommit.types.title


class CreatePullRequestInput(TypedDict, closed=True):
    title: "capo_codecommit.types.title.Title"
    """<p>The title of the pull request. This title is used to identify the pull request to other users in the repository.</p>"""
    description: NotRequired["capo_codecommit.types.description.Description"]
    """<p>A description of the pull request.</p>"""
    targets: "capo_codecommit.types.target_list.TargetList"
    """<p>The targets for the pull request, including the source of the code to be reviewed (the source branch) and the destination where the creator of the pull request intends the code to be merged after the pull request is closed (the destination branch).</p>"""
    client_request_token: NotRequired[
        "capo_codecommit.types.client_request_token.ClientRequestToken"
    ]
    """<p>A unique, client-generated idempotency token that, when provided in a request, ensures the request cannot be repeated with a changed parameter. If a request is received with the same parameters and a token is included, the request returns information about the initial request that used that token.</p> <note> <p>The Amazon Web ServicesSDKs prepopulate client request tokens. If you are using an Amazon Web ServicesSDK, an idempotency token is created for you.</p> </note>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: CreatePullRequestInput) -> dict:
    out: dict = {}
    out["title"] = value["title"]
    if "description" in value:
        out["description"] = value["description"]
    import capo_codecommit.types.target_list

    out["targets"] = capo_codecommit.types.target_list.serialize_aws_json_1_1(
        value["targets"]
    )
    if "client_request_token" in value:
        out["clientRequestToken"] = value["client_request_token"]
    return out


def deserialize_aws_json_1_1(data: dict) -> CreatePullRequestInput:
    out: CreatePullRequestInput = {}  # type: ignore[typeddict-item]
    if data.get("title") is not None:
        out["title"] = data["title"]
    else:
        out["title"] = ""
    if data.get("description") is not None:
        out["description"] = data["description"]
    if data.get("targets") is not None:
        import capo_codecommit.types.target_list

        out["targets"] = capo_codecommit.types.target_list.deserialize_aws_json_1_1(
            data["targets"]
        )
    else:
        out["targets"] = []
    if data.get("clientRequestToken") is not None:
        out["client_request_token"] = data["clientRequestToken"]
    return out
