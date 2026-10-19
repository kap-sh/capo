"""Generated from Smithy shape ``com.amazonaws.detective#BatchGetMembershipDatasourcesRequest``."""

from typing import TYPE_CHECKING

from typing_extensions import TypedDict

if TYPE_CHECKING:
    import capo_detective.types.graph_arn_list


class BatchGetMembershipDatasourcesRequest(TypedDict, closed=True):
    graph_arns: "capo_detective.types.graph_arn_list.GraphArnList"
    """<p>The ARN of the behavior graph.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: BatchGetMembershipDatasourcesRequest) -> dict:
    out: dict = {}
    import capo_detective.types.graph_arn_list

    out["GraphArns"] = capo_detective.types.graph_arn_list.serialize_json(
        value["graph_arns"]
    )
    return out


def deserialize_json(data: dict) -> BatchGetMembershipDatasourcesRequest:
    out: BatchGetMembershipDatasourcesRequest = {}  # type: ignore[typeddict-item]
    if data.get("GraphArns") is not None:
        import capo_detective.types.graph_arn_list

        out["graph_arns"] = capo_detective.types.graph_arn_list.deserialize_json(
            data["GraphArns"]
        )
    else:
        out["graph_arns"] = []
    return out
