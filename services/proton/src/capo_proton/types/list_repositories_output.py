"""Generated from Smithy shape ``com.amazonaws.proton#ListRepositoriesOutput``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_proton.types.next_token
    import capo_proton.types.repository_summary_list


class ListRepositoriesOutput(TypedDict, closed=True):
    next_token: NotRequired["capo_proton.types.next_token.NextToken"]
    """<p>A token that indicates the location of the next repository in the array of repositories, after the current requested list of repositories. </p>"""
    repositories: "capo_proton.types.repository_summary_list.RepositorySummaryList"
    """<p>An array of repository links.</p>"""


# --- awsJson1_0 ser/de ---
def serialize_aws_json_1_0(value: ListRepositoriesOutput) -> dict:
    out: dict = {}
    if "next_token" in value:
        out["nextToken"] = value["next_token"]
    import capo_proton.types.repository_summary_list

    out["repositories"] = (
        capo_proton.types.repository_summary_list.serialize_aws_json_1_0(
            value["repositories"]
        )
    )
    return out


def deserialize_aws_json_1_0(data: dict) -> ListRepositoriesOutput:
    out: ListRepositoriesOutput = {}  # type: ignore[typeddict-item]
    if data.get("nextToken") is not None:
        out["next_token"] = data["nextToken"]
    if data.get("repositories") is not None:
        import capo_proton.types.repository_summary_list

        out["repositories"] = (
            capo_proton.types.repository_summary_list.deserialize_aws_json_1_0(
                data["repositories"]
            )
        )
    else:
        out["repositories"] = []
    return out
