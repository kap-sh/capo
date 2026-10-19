"""Generated from Smithy shape ``com.amazonaws.detective#DeleteGraphRequest``."""

from typing import TYPE_CHECKING

from typing_extensions import TypedDict

if TYPE_CHECKING:
    import capo_detective.types.graph_arn


class DeleteGraphRequest(TypedDict, closed=True):
    graph_arn: "capo_detective.types.graph_arn.GraphArn"
    """<p>The ARN of the behavior graph to disable.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: DeleteGraphRequest) -> dict:
    out: dict = {}
    out["GraphArn"] = value["graph_arn"]
    return out


def deserialize_json(data: dict) -> DeleteGraphRequest:
    out: DeleteGraphRequest = {}  # type: ignore[typeddict-item]
    if data.get("GraphArn") is not None:
        out["graph_arn"] = data["GraphArn"]
    else:
        out["graph_arn"] = ""
    return out
