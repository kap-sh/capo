"""Generated from Smithy shape ``com.amazonaws.codepipeline#GitConfiguration``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_codepipeline.types.action_name
    import capo_codepipeline.types.git_pull_request_filter_list
    import capo_codepipeline.types.git_push_filter_list


class GitConfiguration(TypedDict, closed=True):
    source_action_name: "capo_codepipeline.types.action_name.ActionName"
    """<p>The name of the pipeline source action where the trigger configuration, such as Git tags, is specified. The trigger configuration will start the pipeline upon the specified change only.</p> <note> <p>You can only specify one trigger configuration per source action.</p> </note>"""
    push: NotRequired["capo_codepipeline.types.git_push_filter_list.GitPushFilterList"]
    """<p>The field where the repository event that will start the pipeline, such as pushing Git tags, is specified with details.</p>"""
    pull_request: NotRequired[
        "capo_codepipeline.types.git_pull_request_filter_list.GitPullRequestFilterList"
    ]
    """<p>The field where the repository event that will start the pipeline is specified as pull requests.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: GitConfiguration) -> dict:
    out: dict = {}
    out["sourceActionName"] = value["source_action_name"]
    if "push" in value:
        import capo_codepipeline.types.git_push_filter_list

        out["push"] = (
            capo_codepipeline.types.git_push_filter_list.serialize_aws_json_1_1(
                value["push"]
            )
        )
    if "pull_request" in value:
        import capo_codepipeline.types.git_pull_request_filter_list

        out["pullRequest"] = (
            capo_codepipeline.types.git_pull_request_filter_list.serialize_aws_json_1_1(
                value["pull_request"]
            )
        )
    return out


def deserialize_aws_json_1_1(data: dict) -> GitConfiguration:
    out: GitConfiguration = {}  # type: ignore[typeddict-item]
    if data.get("sourceActionName") is not None:
        out["source_action_name"] = data["sourceActionName"]
    else:
        out["source_action_name"] = ""
    if data.get("push") is not None:
        import capo_codepipeline.types.git_push_filter_list

        out["push"] = (
            capo_codepipeline.types.git_push_filter_list.deserialize_aws_json_1_1(
                data["push"]
            )
        )
    if data.get("pullRequest") is not None:
        import capo_codepipeline.types.git_pull_request_filter_list

        out["pull_request"] = (
            capo_codepipeline.types.git_pull_request_filter_list.deserialize_aws_json_1_1(
                data["pullRequest"]
            )
        )
    return out
