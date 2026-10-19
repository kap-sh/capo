"""Generated from Smithy shape ``com.amazonaws.dsql#ListClustersOutput``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_dsql.types.cluster_list
    import capo_dsql.types.next_token


class ListClustersOutput(TypedDict, closed=True):
    next_token: NotRequired["capo_dsql.types.next_token.NextToken"]
    """<p>If nextToken is returned, there are more results available. The value of nextToken is a unique pagination token for each page. To retrieve the next page, make the call again using the returned token.</p>"""
    clusters: "capo_dsql.types.cluster_list.ClusterList"
    """<p>An array of the returned clusters.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: ListClustersOutput) -> dict:
    out: dict = {}
    if "next_token" in value:
        out["nextToken"] = value["next_token"]
    import capo_dsql.types.cluster_list

    out["clusters"] = capo_dsql.types.cluster_list.serialize_json(value["clusters"])
    return out


def deserialize_json(data: dict) -> ListClustersOutput:
    out: ListClustersOutput = {}  # type: ignore[typeddict-item]
    if data.get("nextToken") is not None:
        out["next_token"] = data["nextToken"]
    if data.get("clusters") is not None:
        import capo_dsql.types.cluster_list

        out["clusters"] = capo_dsql.types.cluster_list.deserialize_json(
            data["clusters"]
        )
    else:
        out["clusters"] = []
    return out
