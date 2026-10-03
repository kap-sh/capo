"""Generated from Smithy shape ``com.amazonaws.codecommit#GetBlobDifferencesInput``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

from capo_codecommit.errors import DeserializationError

if TYPE_CHECKING:
    import capo_codecommit.types.diff_context
    import capo_codecommit.types.ignore_white_spaces
    import capo_codecommit.types.limit
    import capo_codecommit.types.next_token
    import capo_codecommit.types.object_id
    import capo_codecommit.types.repository_name


class GetBlobDifferencesInput(TypedDict, closed=True):
    repository_name: "capo_codecommit.types.repository_name.RepositoryName"
    """<p>The name of the repository that contains the blobs to compare.</p>"""
    after_blob_id: "capo_codecommit.types.object_id.ObjectId"
    """<p>The ID of the "after" (destination) blob in the diff. Typically the value of <code>afterBlob.blobId</code> from a <code>Difference</code> object returned by <a>GetDifferences</a>.</p>"""
    before_blob_id: NotRequired["capo_codecommit.types.object_id.ObjectId"]
    """<p>The ID of the "before" (source) blob in the diff. Typically the value of <code>beforeBlob.blobId</code> from a <code>Difference</code> object returned by <a>GetDifferences</a>.</p> <p>If you do not specify a value, the operation returns a diff against an empty before-state. This is equivalent to treating the file as newly added.</p>"""
    context_lines: NotRequired["capo_codecommit.types.diff_context.DiffContext"]
    """<p>The number of unchanged lines of context to include before and after each block of changes in a hunk. Valid values are 0 through 20. Defaults to <code>3</code>.</p>"""
    ignore_whitespace: NotRequired[
        "capo_codecommit.types.ignore_white_spaces.IgnoreWhiteSpaces"
    ]
    """<p>Specifies whether to ignore whitespace-only changes when computing the diff. When <code>true</code>, the operation treats lines that differ only in whitespace as unchanged. Defaults to <code>false</code>.</p>"""
    max_results: NotRequired["capo_codecommit.types.limit.Limit"]
    """<p>The maximum number of <code>DiffHunk</code> entries to return in a single response page. Defaults to <code>100</code>.</p>"""
    next_token: NotRequired["capo_codecommit.types.next_token.NextToken"]
    """<p>An enumeration token that returns the next batch of results when present in a request.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: GetBlobDifferencesInput) -> dict:
    out: dict = {}
    out["repositoryName"] = value["repository_name"]
    out["afterBlobId"] = value["after_blob_id"]
    if "before_blob_id" in value:
        out["beforeBlobId"] = value["before_blob_id"]
    if "context_lines" in value:
        out["contextLines"] = value["context_lines"]
    if "ignore_whitespace" in value:
        out["ignoreWhitespace"] = value["ignore_whitespace"]
    if "max_results" in value:
        out["MaxResults"] = value["max_results"]
    if "next_token" in value:
        out["NextToken"] = value["next_token"]
    return out


def deserialize_aws_json_1_1(data: dict) -> GetBlobDifferencesInput:
    out: GetBlobDifferencesInput = {}  # type: ignore[typeddict-item]
    if data.get("repositoryName") is not None:
        out["repository_name"] = data["repositoryName"]
    else:
        raise DeserializationError("GetBlobDifferencesInput.repository_name required")
    if data.get("afterBlobId") is not None:
        out["after_blob_id"] = data["afterBlobId"]
    else:
        raise DeserializationError("GetBlobDifferencesInput.after_blob_id required")
    if data.get("beforeBlobId") is not None:
        out["before_blob_id"] = data["beforeBlobId"]
    if data.get("contextLines") is not None:
        out["context_lines"] = data["contextLines"]
    if data.get("ignoreWhitespace") is not None:
        out["ignore_whitespace"] = data["ignoreWhitespace"]
    if data.get("MaxResults") is not None:
        out["max_results"] = data["MaxResults"]
    if data.get("NextToken") is not None:
        out["next_token"] = data["NextToken"]
    return out
