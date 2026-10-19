"""Generated from Smithy shape ``com.amazonaws.connectcases#CreateLayoutResponse``."""

from typing import TYPE_CHECKING

from typing_extensions import TypedDict

if TYPE_CHECKING:
    import capo_connectcases.types.layout_arn
    import capo_connectcases.types.layout_id


class CreateLayoutResponse(TypedDict, closed=True):
    layout_id: "capo_connectcases.types.layout_id.LayoutId"
    """<p>The unique identifier of the layout.</p>"""
    layout_arn: "capo_connectcases.types.layout_arn.LayoutArn"
    """<p>The Amazon Resource Name (ARN) of the newly created layout.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: CreateLayoutResponse) -> dict:
    out: dict = {}
    out["layoutId"] = value["layout_id"]
    out["layoutArn"] = value["layout_arn"]
    return out


def deserialize_json(data: dict) -> CreateLayoutResponse:
    out: CreateLayoutResponse = {}  # type: ignore[typeddict-item]
    if data.get("layoutId") is not None:
        out["layout_id"] = data["layoutId"]
    else:
        out["layout_id"] = ""
    if data.get("layoutArn") is not None:
        out["layout_arn"] = data["layoutArn"]
    else:
        out["layout_arn"] = ""
    return out
