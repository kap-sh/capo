"""Generated from Smithy shape ``com.amazonaws.connectcases#LayoutSummary``."""

from typing import TYPE_CHECKING

from typing_extensions import TypedDict

if TYPE_CHECKING:
    import capo_connectcases.types.layout_arn
    import capo_connectcases.types.layout_id
    import capo_connectcases.types.layout_name


class LayoutSummary(TypedDict, closed=True):
    layout_id: "capo_connectcases.types.layout_id.LayoutId"
    """<p>The unique identifier for of the layout.</p>"""
    layout_arn: "capo_connectcases.types.layout_arn.LayoutArn"
    """<p>The Amazon Resource Name (ARN) of the layout.</p>"""
    name: "capo_connectcases.types.layout_name.LayoutName"
    """<p>The name of the layout.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: LayoutSummary) -> dict:
    out: dict = {}
    out["layoutId"] = value["layout_id"]
    out["layoutArn"] = value["layout_arn"]
    out["name"] = value["name"]
    return out


def deserialize_json(data: dict) -> LayoutSummary:
    out: LayoutSummary = {}  # type: ignore[typeddict-item]
    if data.get("layoutId") is not None:
        out["layout_id"] = data["layoutId"]
    else:
        out["layout_id"] = ""
    if data.get("layoutArn") is not None:
        out["layout_arn"] = data["layoutArn"]
    else:
        out["layout_arn"] = ""
    if data.get("name") is not None:
        out["name"] = data["name"]
    else:
        out["name"] = ""
    return out
