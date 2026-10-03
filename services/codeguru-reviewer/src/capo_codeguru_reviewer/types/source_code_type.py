"""Generated from Smithy shape ``com.amazonaws.codegurureviewer#SourceCodeType``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_codeguru_reviewer.types.branch_diff_source_code_type
    import capo_codeguru_reviewer.types.commit_diff_source_code_type
    import capo_codeguru_reviewer.types.repository_head_source_code_type
    import capo_codeguru_reviewer.types.request_metadata
    import capo_codeguru_reviewer.types.s3_bucket_repository


class SourceCodeType(TypedDict, closed=True):
    commit_diff: NotRequired[
        "capo_codeguru_reviewer.types.commit_diff_source_code_type.CommitDiffSourceCodeType"
    ]
    """<p>A <a href="https://docs.aws.amazon.com/codeguru/latest/reviewer-api/API_SourceCodeType">SourceCodeType</a> that specifies a commit diff created by a pull request on an associated repository.</p>"""
    repository_head: NotRequired[
        "capo_codeguru_reviewer.types.repository_head_source_code_type.RepositoryHeadSourceCodeType"
    ]
    branch_diff: NotRequired[
        "capo_codeguru_reviewer.types.branch_diff_source_code_type.BranchDiffSourceCodeType"
    ]
    """<p>A type of <a href="https://docs.aws.amazon.com/codeguru/latest/reviewer-api/API_SourceCodeType">SourceCodeType</a> that specifies a source branch name and a destination branch name in an associated repository.</p>"""
    s3_bucket_repository: NotRequired[
        "capo_codeguru_reviewer.types.s3_bucket_repository.S3BucketRepository"
    ]
    """<p>Information about an associated repository in an S3 bucket that includes its name and an <code>S3RepositoryDetails</code> object. The <code>S3RepositoryDetails</code> object includes the name of an S3 bucket, an S3 key for a source code .zip file, and an S3 key for a build artifacts .zip file. <code>S3BucketRepository</code> is required in <a href="https://docs.aws.amazon.com/codeguru/latest/reviewer-api/API_SourceCodeType">SourceCodeType</a> for <code>S3BucketRepository</code> based code reviews.</p>"""
    request_metadata: NotRequired[
        "capo_codeguru_reviewer.types.request_metadata.RequestMetadata"
    ]
    """<p>Metadata that is associated with a code review. This applies to any type of code review supported by CodeGuru Reviewer. The <code>RequestMetadaa</code> field captures any event metadata. For example, it might capture metadata associated with an event trigger, such as a push or a pull request.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: SourceCodeType) -> dict:
    out: dict = {}
    if "commit_diff" in value:
        import capo_codeguru_reviewer.types.commit_diff_source_code_type

        out["CommitDiff"] = (
            capo_codeguru_reviewer.types.commit_diff_source_code_type.serialize_json(
                value["commit_diff"]
            )
        )
    if "repository_head" in value:
        import capo_codeguru_reviewer.types.repository_head_source_code_type

        out["RepositoryHead"] = (
            capo_codeguru_reviewer.types.repository_head_source_code_type.serialize_json(
                value["repository_head"]
            )
        )
    if "branch_diff" in value:
        import capo_codeguru_reviewer.types.branch_diff_source_code_type

        out["BranchDiff"] = (
            capo_codeguru_reviewer.types.branch_diff_source_code_type.serialize_json(
                value["branch_diff"]
            )
        )
    if "s3_bucket_repository" in value:
        import capo_codeguru_reviewer.types.s3_bucket_repository

        out["S3BucketRepository"] = (
            capo_codeguru_reviewer.types.s3_bucket_repository.serialize_json(
                value["s3_bucket_repository"]
            )
        )
    if "request_metadata" in value:
        import capo_codeguru_reviewer.types.request_metadata

        out["RequestMetadata"] = (
            capo_codeguru_reviewer.types.request_metadata.serialize_json(
                value["request_metadata"]
            )
        )
    return out


def deserialize_json(data: dict) -> SourceCodeType:
    out: SourceCodeType = {}  # type: ignore[typeddict-item]
    if data.get("CommitDiff") is not None:
        import capo_codeguru_reviewer.types.commit_diff_source_code_type

        out["commit_diff"] = (
            capo_codeguru_reviewer.types.commit_diff_source_code_type.deserialize_json(
                data["CommitDiff"]
            )
        )
    if data.get("RepositoryHead") is not None:
        import capo_codeguru_reviewer.types.repository_head_source_code_type

        out["repository_head"] = (
            capo_codeguru_reviewer.types.repository_head_source_code_type.deserialize_json(
                data["RepositoryHead"]
            )
        )
    if data.get("BranchDiff") is not None:
        import capo_codeguru_reviewer.types.branch_diff_source_code_type

        out["branch_diff"] = (
            capo_codeguru_reviewer.types.branch_diff_source_code_type.deserialize_json(
                data["BranchDiff"]
            )
        )
    if data.get("S3BucketRepository") is not None:
        import capo_codeguru_reviewer.types.s3_bucket_repository

        out["s3_bucket_repository"] = (
            capo_codeguru_reviewer.types.s3_bucket_repository.deserialize_json(
                data["S3BucketRepository"]
            )
        )
    if data.get("RequestMetadata") is not None:
        import capo_codeguru_reviewer.types.request_metadata

        out["request_metadata"] = (
            capo_codeguru_reviewer.types.request_metadata.deserialize_json(
                data["RequestMetadata"]
            )
        )
    return out
