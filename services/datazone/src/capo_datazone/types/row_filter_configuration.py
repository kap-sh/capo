"""Generated from Smithy shape ``com.amazonaws.datazone#RowFilterConfiguration``."""

from typing import TYPE_CHECKING

from typing_extensions import TypedDict

if TYPE_CHECKING:
    import capo_datazone.types.row_filter


class RowFilterConfiguration(TypedDict, closed=True):
    row_filter: "capo_datazone.types.row_filter.RowFilter"
    """<p>The row filter.</p>"""
    sensitive: "bool"
    """<p>Specifies whether the row filter is sensitive.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: RowFilterConfiguration) -> dict:
    out: dict = {}
    import capo_datazone.types.row_filter

    out["rowFilter"] = capo_datazone.types.row_filter.serialize_json(
        value["row_filter"]
    )
    out["sensitive"] = value.get("sensitive", True)
    return out


def deserialize_json(data: dict) -> RowFilterConfiguration:
    out: RowFilterConfiguration = {}  # type: ignore[typeddict-item]
    if data.get("rowFilter") is not None:
        import capo_datazone.types.row_filter

        out["row_filter"] = capo_datazone.types.row_filter.deserialize_json(
            data["rowFilter"]
        )
    else:
        out["row_filter"] = {"$unknown": {"name": ""}}
    if data.get("sensitive") is not None:
        out["sensitive"] = data["sensitive"]
    else:
        out["sensitive"] = True
    return out
