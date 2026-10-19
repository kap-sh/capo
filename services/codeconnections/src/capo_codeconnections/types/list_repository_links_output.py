"""Generated from Smithy shape ``com.amazonaws.codeconnections#ListRepositoryLinksOutput``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_codeconnections.types.repository_link_list
    import capo_codeconnections.types.sharp_next_token


class ListRepositoryLinksOutput(TypedDict, closed=True):
    repository_links: (
        "capo_codeconnections.types.repository_link_list.RepositoryLinkList"
    )
    """<p>Lists the repository links called by the list repository links operation.</p>"""
    next_token: NotRequired[
        "capo_codeconnections.types.sharp_next_token.SharpNextToken"
    ]
    """<p>An enumeration token that allows the operation to batch the results of the operation. </p>"""


# --- awsJson1_0 ser/de ---
def serialize_aws_json_1_0(value: ListRepositoryLinksOutput) -> dict:
    out: dict = {}
    import capo_codeconnections.types.repository_link_list

    out["RepositoryLinks"] = (
        capo_codeconnections.types.repository_link_list.serialize_aws_json_1_0(
            value["repository_links"]
        )
    )
    if "next_token" in value:
        out["NextToken"] = value["next_token"]
    return out


def deserialize_aws_json_1_0(data: dict) -> ListRepositoryLinksOutput:
    out: ListRepositoryLinksOutput = {}  # type: ignore[typeddict-item]
    if data.get("RepositoryLinks") is not None:
        import capo_codeconnections.types.repository_link_list

        out["repository_links"] = (
            capo_codeconnections.types.repository_link_list.deserialize_aws_json_1_0(
                data["RepositoryLinks"]
            )
        )
    else:
        out["repository_links"] = []
    if data.get("NextToken") is not None:
        out["next_token"] = data["NextToken"]
    return out
