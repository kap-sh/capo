"""Generated from Smithy shape ``com.amazonaws.qconnect#QuickResponseOrderField``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_qconnect.types.non_empty_string
    import capo_qconnect.types.order


class QuickResponseOrderField(TypedDict, closed=True):
    name: "capo_qconnect.types.non_empty_string.NonEmptyString"
    """<p>The name of the attribute to order the quick response query results by.</p>"""
    order: NotRequired["capo_qconnect.types.order.Order"]
    """<p>The order at which the quick responses are sorted by.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: QuickResponseOrderField) -> dict:
    out: dict = {}
    out["name"] = value["name"]
    if "order" in value:
        out["order"] = value["order"]
    return out


def deserialize_json(data: dict) -> QuickResponseOrderField:
    out: QuickResponseOrderField = {}  # type: ignore[typeddict-item]
    if data.get("name") is not None:
        out["name"] = data["name"]
    else:
        out["name"] = ""
    if data.get("order") is not None:
        out["order"] = data["order"]
    return out
