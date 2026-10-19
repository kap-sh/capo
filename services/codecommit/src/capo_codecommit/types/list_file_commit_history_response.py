"""Generated from Smithy shape ``com.amazonaws.codecommit#ListFileCommitHistoryResponse``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_codecommit.types.next_token
    import capo_codecommit.types.revision_dag


class ListFileCommitHistoryResponse(TypedDict, closed=True):
    revision_dag: "capo_codecommit.types.revision_dag.RevisionDag"
    """<p>An array of FileVersion objects that form a directed acyclic graph (DAG) of the changes to the file made by the commits that changed the file.</p>"""
    next_token: NotRequired["capo_codecommit.types.next_token.NextToken"]
    """<p>An enumeration token that can be used to return the next batch of results.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: ListFileCommitHistoryResponse) -> dict:
    out: dict = {}
    import capo_codecommit.types.revision_dag

    out["revisionDag"] = capo_codecommit.types.revision_dag.serialize_aws_json_1_1(
        value["revision_dag"]
    )
    if "next_token" in value:
        out["nextToken"] = value["next_token"]
    return out


def deserialize_aws_json_1_1(data: dict) -> ListFileCommitHistoryResponse:
    out: ListFileCommitHistoryResponse = {}  # type: ignore[typeddict-item]
    if data.get("revisionDag") is not None:
        import capo_codecommit.types.revision_dag

        out["revision_dag"] = (
            capo_codecommit.types.revision_dag.deserialize_aws_json_1_1(
                data["revisionDag"]
            )
        )
    else:
        out["revision_dag"] = []
    if data.get("nextToken") is not None:
        out["next_token"] = data["nextToken"]
    return out
