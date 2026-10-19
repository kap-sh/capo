"""Generated from Smithy shape ``com.amazonaws.codecommit#GetDifferencesInput``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_codecommit.types.commit_name
    import capo_codecommit.types.limit
    import capo_codecommit.types.next_token
    import capo_codecommit.types.path
    import capo_codecommit.types.repository_name


class GetDifferencesInput(TypedDict, closed=True):
    repository_name: "capo_codecommit.types.repository_name.RepositoryName"
    """<p>The name of the repository where you want to get differences.</p>"""
    before_commit_specifier: NotRequired["capo_codecommit.types.commit_name.CommitName"]
    """<p>The branch, tag, HEAD, or other fully qualified reference used to identify a commit (for example, the full commit ID). Optional. If not specified, all changes before the <code>afterCommitSpecifier</code> value are shown. If you do not use <code>beforeCommitSpecifier</code> in your request, consider limiting the results with <code>maxResults</code>.</p>"""
    after_commit_specifier: "capo_codecommit.types.commit_name.CommitName"
    """<p>The branch, tag, HEAD, or other fully qualified reference used to identify a commit.</p>"""
    before_path: NotRequired["capo_codecommit.types.path.Path"]
    """<p>The file path in which to check for differences. Limits the results to this path. Can also be used to specify the previous name of a directory or folder. If <code>beforePath</code> and <code>afterPath</code> are not specified, differences are shown for all paths.</p>"""
    after_path: NotRequired["capo_codecommit.types.path.Path"]
    """<p>The file path in which to check differences. Limits the results to this path. Can also be used to specify the changed name of a directory or folder, if it has changed. If not specified, differences are shown for all paths.</p>"""
    max_results: NotRequired["capo_codecommit.types.limit.Limit"]
    """<p>A non-zero, non-negative integer used to limit the number of returned results.</p>"""
    next_token: NotRequired["capo_codecommit.types.next_token.NextToken"]
    """<p>An enumeration token that, when provided in a request, returns the next batch of the results.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: GetDifferencesInput) -> dict:
    out: dict = {}
    out["repositoryName"] = value["repository_name"]
    if "before_commit_specifier" in value:
        out["beforeCommitSpecifier"] = value["before_commit_specifier"]
    out["afterCommitSpecifier"] = value["after_commit_specifier"]
    if "before_path" in value:
        out["beforePath"] = value["before_path"]
    if "after_path" in value:
        out["afterPath"] = value["after_path"]
    if "max_results" in value:
        out["MaxResults"] = value["max_results"]
    if "next_token" in value:
        out["NextToken"] = value["next_token"]
    return out


def deserialize_aws_json_1_1(data: dict) -> GetDifferencesInput:
    out: GetDifferencesInput = {}  # type: ignore[typeddict-item]
    if data.get("repositoryName") is not None:
        out["repository_name"] = data["repositoryName"]
    else:
        out["repository_name"] = ""
    if data.get("beforeCommitSpecifier") is not None:
        out["before_commit_specifier"] = data["beforeCommitSpecifier"]
    if data.get("afterCommitSpecifier") is not None:
        out["after_commit_specifier"] = data["afterCommitSpecifier"]
    else:
        out["after_commit_specifier"] = ""
    if data.get("beforePath") is not None:
        out["before_path"] = data["beforePath"]
    if data.get("afterPath") is not None:
        out["after_path"] = data["afterPath"]
    if data.get("MaxResults") is not None:
        out["max_results"] = data["MaxResults"]
    if data.get("NextToken") is not None:
        out["next_token"] = data["NextToken"]
    return out
