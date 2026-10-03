"""Generated from Smithy shape ``com.amazonaws.codecatalyst#ListSourceRepositoryBranchesItem``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_codecatalyst.types.source_repository_branch_ref_string
    import capo_codecatalyst.types.source_repository_branch_string
    import capo_codecatalyst.types.timestamp


class ListSourceRepositoryBranchesItem(TypedDict, closed=True):
    ref: NotRequired[
        "capo_codecatalyst.types.source_repository_branch_ref_string.SourceRepositoryBranchRefString"
    ]
    """<p>The Git reference name of the branch.</p>"""
    name: NotRequired[
        "capo_codecatalyst.types.source_repository_branch_string.SourceRepositoryBranchString"
    ]
    """<p>The name of the branch.</p>"""
    last_updated_time: NotRequired["capo_codecatalyst.types.timestamp.Timestamp"]
    """<p>The time the branch was last updated, in coordinated universal time (UTC) timestamp format as specified in <a href="https://www.rfc-editor.org/rfc/rfc3339#section-5.6">RFC 3339</a>.</p>"""
    head_commit_id: NotRequired["str"]
    """<p>The commit ID of the tip of the branch at the time of the request, also known as the head commit.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: ListSourceRepositoryBranchesItem) -> dict:
    out: dict = {}
    if "ref" in value:
        out["ref"] = value["ref"]
    if "name" in value:
        out["name"] = value["name"]
    if "last_updated_time" in value:
        import capo_codecatalyst._protocol.serialize

        out["lastUpdatedTime"] = capo_codecatalyst._protocol.serialize.fmt_date_time(
            value["last_updated_time"]
        )
    if "head_commit_id" in value:
        out["headCommitId"] = value["head_commit_id"]
    return out


def deserialize_json(data: dict) -> ListSourceRepositoryBranchesItem:
    out: ListSourceRepositoryBranchesItem = {}  # type: ignore[typeddict-item]
    if data.get("ref") is not None:
        out["ref"] = data["ref"]
    if data.get("name") is not None:
        out["name"] = data["name"]
    if data.get("lastUpdatedTime") is not None:
        import datetime

        out["last_updated_time"] = datetime.datetime.fromisoformat(
            data["lastUpdatedTime"].replace("Z", "+00:00")
        )
    if data.get("headCommitId") is not None:
        out["head_commit_id"] = data["headCommitId"]
    return out
