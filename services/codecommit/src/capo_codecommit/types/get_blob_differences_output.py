"""Generated from Smithy shape ``com.amazonaws.codecommit#GetBlobDifferencesOutput``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_codecommit.types.capital_boolean
    import capo_codecommit.types.diff_hunk_list
    import capo_codecommit.types.next_token
    import capo_codecommit.types.object_size


class GetBlobDifferencesOutput(TypedDict, closed=True):
    hunks: "capo_codecommit.types.diff_hunk_list.DiffHunkList"
    """<p>An ordered list of diff hunks. Each hunk represents a contiguous run of changed and adjacent context lines. The list is empty when the blobs are identical or when the content is binary. The list is also empty when a paginated request has already returned all hunks in earlier pages, in which case <code>NextToken</code> is also <code>null</code>.</p>"""
    is_binary: "capo_codecommit.types.capital_boolean.CapitalBoolean"
    """<p>Specifies whether the operation treated the diff content as binary. When <code>true</code>, the operation does not compute a line-level diff and <code>hunks</code> is empty.</p>"""
    before_blob_size: "capo_codecommit.types.object_size.ObjectSize"
    """<p>The size, in bytes, of the blob identified by <code>beforeBlobId</code>. Returns <code>0</code> when you do not specify <code>beforeBlobId</code>.</p>"""
    after_blob_size: "capo_codecommit.types.object_size.ObjectSize"
    """<p>The size, in bytes, of the blob identified by <code>afterBlobId</code>.</p>"""
    next_token: NotRequired["capo_codecommit.types.next_token.NextToken"]
    """<p>An enumeration token that can be used in a request to return the next batch of <code>DiffHunk</code> entries. <code>null</code> when the response contains the final page of the diff.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: GetBlobDifferencesOutput) -> dict:
    out: dict = {}
    import capo_codecommit.types.diff_hunk_list

    out["hunks"] = capo_codecommit.types.diff_hunk_list.serialize_aws_json_1_1(
        value["hunks"]
    )
    out["isBinary"] = value["is_binary"]
    out["beforeBlobSize"] = value.get("before_blob_size", 0)
    out["afterBlobSize"] = value.get("after_blob_size", 0)
    if "next_token" in value:
        out["NextToken"] = value["next_token"]
    return out


def deserialize_aws_json_1_1(data: dict) -> GetBlobDifferencesOutput:
    out: GetBlobDifferencesOutput = {}  # type: ignore[typeddict-item]
    if data.get("hunks") is not None:
        import capo_codecommit.types.diff_hunk_list

        out["hunks"] = capo_codecommit.types.diff_hunk_list.deserialize_aws_json_1_1(
            data["hunks"]
        )
    else:
        out["hunks"] = []
    if data.get("isBinary") is not None:
        out["is_binary"] = data["isBinary"]
    else:
        out["is_binary"] = False
    if data.get("beforeBlobSize") is not None:
        out["before_blob_size"] = data["beforeBlobSize"]
    else:
        out["before_blob_size"] = 0
    if data.get("afterBlobSize") is not None:
        out["after_blob_size"] = data["afterBlobSize"]
    else:
        out["after_blob_size"] = 0
    if data.get("NextToken") is not None:
        out["next_token"] = data["NextToken"]
    return out
