"""Generated from Smithy shape ``com.amazonaws.codecommit#Commit``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_codecommit.types.additional_data
    import capo_codecommit.types.message
    import capo_codecommit.types.object_id
    import capo_codecommit.types.parent_list
    import capo_codecommit.types.user_info


class Commit(TypedDict, closed=True):
    commit_id: NotRequired["capo_codecommit.types.object_id.ObjectId"]
    """<p>The full SHA ID of the specified commit. </p>"""
    tree_id: NotRequired["capo_codecommit.types.object_id.ObjectId"]
    """<p>Tree information for the specified commit.</p>"""
    parents: NotRequired["capo_codecommit.types.parent_list.ParentList"]
    """<p>A list of parent commits for the specified commit. Each parent commit ID is the full commit ID.</p>"""
    message: NotRequired["capo_codecommit.types.message.Message"]
    """<p>The commit message associated with the specified commit.</p>"""
    author: NotRequired["capo_codecommit.types.user_info.UserInfo"]
    """<p>Information about the author of the specified commit. Information includes the date in timestamp format with GMT offset, the name of the author, and the email address for the author, as configured in Git.</p>"""
    committer: NotRequired["capo_codecommit.types.user_info.UserInfo"]
    """<p>Information about the person who committed the specified commit, also known as the committer. Information includes the date in timestamp format with GMT offset, the name of the committer, and the email address for the committer, as configured in Git.</p> <p>For more information about the difference between an author and a committer in Git, see <a href="http://git-scm.com/book/ch2-3.html">Viewing the Commit History</a> in Pro Git by Scott Chacon and Ben Straub.</p>"""
    additional_data: NotRequired["capo_codecommit.types.additional_data.AdditionalData"]
    """<p>Any other data associated with the specified commit.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: Commit) -> dict:
    out: dict = {}
    if "commit_id" in value:
        out["commitId"] = value["commit_id"]
    if "tree_id" in value:
        out["treeId"] = value["tree_id"]
    if "parents" in value:
        import capo_codecommit.types.parent_list

        out["parents"] = capo_codecommit.types.parent_list.serialize_aws_json_1_1(
            value["parents"]
        )
    if "message" in value:
        out["message"] = value["message"]
    if "author" in value:
        import capo_codecommit.types.user_info

        out["author"] = capo_codecommit.types.user_info.serialize_aws_json_1_1(
            value["author"]
        )
    if "committer" in value:
        import capo_codecommit.types.user_info

        out["committer"] = capo_codecommit.types.user_info.serialize_aws_json_1_1(
            value["committer"]
        )
    if "additional_data" in value:
        out["additionalData"] = value["additional_data"]
    return out


def deserialize_aws_json_1_1(data: dict) -> Commit:
    out: Commit = {}  # type: ignore[typeddict-item]
    if data.get("commitId") is not None:
        out["commit_id"] = data["commitId"]
    if data.get("treeId") is not None:
        out["tree_id"] = data["treeId"]
    if data.get("parents") is not None:
        import capo_codecommit.types.parent_list

        out["parents"] = capo_codecommit.types.parent_list.deserialize_aws_json_1_1(
            data["parents"]
        )
    if data.get("message") is not None:
        out["message"] = data["message"]
    if data.get("author") is not None:
        import capo_codecommit.types.user_info

        out["author"] = capo_codecommit.types.user_info.deserialize_aws_json_1_1(
            data["author"]
        )
    if data.get("committer") is not None:
        import capo_codecommit.types.user_info

        out["committer"] = capo_codecommit.types.user_info.deserialize_aws_json_1_1(
            data["committer"]
        )
    if data.get("additionalData") is not None:
        out["additional_data"] = data["additionalData"]
    return out
