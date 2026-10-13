"""Generated from Smithy shape ``com.amazonaws.datazone#GitMetadata``."""

from typing import TYPE_CHECKING, Any

from typing_extensions import NotRequired, TypedDict

from capo_datazone.errors import DeserializationError

if TYPE_CHECKING:
    import datetime

    import capo_datazone.types.commit_hash
    import capo_datazone.types.commit_message
    import capo_datazone.types.file_name
    import capo_datazone.types.git_branch
    import capo_datazone.types.git_connection_id
    import capo_datazone.types.git_repository


class GitMetadata(TypedDict, closed=True):
    connection_id: "capo_datazone.types.git_connection_id.GitConnectionId"
    """<p>The identifier of the Git connection.</p>"""
    repository: "capo_datazone.types.git_repository.GitRepository"
    """<p>The name of the Git repository.</p>"""
    branch: "capo_datazone.types.git_branch.GitBranch"
    """<p>The name of the Git branch.</p>"""
    commit_hash: "capo_datazone.types.commit_hash.CommitHash"
    """<p>The commit hash in the Git repository.</p>"""
    file_name: NotRequired["capo_datazone.types.file_name.FileName"]
    """<p>The name of the file in the Git repository.</p>"""
    committed_at: NotRequired["datetime.datetime"]
    """<p>The timestamp of when the commit was made.</p>"""
    commit_message: NotRequired["capo_datazone.types.commit_message.CommitMessage"]
    """<p>The commit message associated with the Git commit.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: GitMetadata) -> dict:
    out: dict = {}
    out["connectionId"] = value["connection_id"]
    out["repository"] = value["repository"]
    out["branch"] = value["branch"]
    out["commitHash"] = value["commit_hash"]
    if "file_name" in value:
        out["fileName"] = value["file_name"]
    if "committed_at" in value:
        import capo_datazone.types._prelude.timestamp

        out["committedAt"] = capo_datazone.types._prelude.timestamp.serialize_json(
            value["committed_at"]
        )
    if "commit_message" in value:
        out["commitMessage"] = value["commit_message"]
    return out


def deserialize_json(data: dict) -> GitMetadata:
    out: GitMetadata = {}  # type: ignore[typeddict-item]
    if data.get("connectionId") is not None:
        out["connection_id"] = data["connectionId"]
    else:
        raise DeserializationError("GitMetadata.connection_id required")
    if data.get("repository") is not None:
        out["repository"] = data["repository"]
    else:
        raise DeserializationError("GitMetadata.repository required")
    if data.get("branch") is not None:
        out["branch"] = data["branch"]
    else:
        raise DeserializationError("GitMetadata.branch required")
    if data.get("commitHash") is not None:
        out["commit_hash"] = data["commitHash"]
    else:
        raise DeserializationError("GitMetadata.commit_hash required")
    if data.get("fileName") is not None:
        out["file_name"] = data["fileName"]
    if data.get("committedAt") is not None:
        import capo_datazone.types._prelude.timestamp

        out["committed_at"] = capo_datazone.types._prelude.timestamp.deserialize_json(
            data["committedAt"]
        )
    if data.get("commitMessage") is not None:
        out["commit_message"] = data["commitMessage"]
    return out


def redact_sensitive(value: GitMetadata) -> dict[str, Any]:
    out: dict[str, Any] = dict(value)
    if "repository" in value:
        out["repository"] = "*** Sensitive Data Redacted ***"
    if "branch" in value:
        out["branch"] = "*** Sensitive Data Redacted ***"
    if "commit_message" in value:
        out["commit_message"] = "*** Sensitive Data Redacted ***"
    return out
