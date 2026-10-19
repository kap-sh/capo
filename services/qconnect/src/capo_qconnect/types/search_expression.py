"""Generated from Smithy shape ``com.amazonaws.qconnect#SearchExpression``."""

from typing import TYPE_CHECKING

from typing_extensions import TypedDict

if TYPE_CHECKING:
    import capo_qconnect.types.filter_list


class SearchExpression(TypedDict, closed=True):
    filters: "capo_qconnect.types.filter_list.FilterList"
    """<p>The search expression filters.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: SearchExpression) -> dict:
    out: dict = {}
    import capo_qconnect.types.filter_list

    out["filters"] = capo_qconnect.types.filter_list.serialize_json(value["filters"])
    return out


def deserialize_json(data: dict) -> SearchExpression:
    out: SearchExpression = {}  # type: ignore[typeddict-item]
    if data.get("filters") is not None:
        import capo_qconnect.types.filter_list

        out["filters"] = capo_qconnect.types.filter_list.deserialize_json(
            data["filters"]
        )
    else:
        out["filters"] = []
    return out
