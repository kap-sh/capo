"""Generated from Smithy shape ``com.amazonaws.databrew#FilesLimit``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_databrew.types.max_files
    import capo_databrew.types.order
    import capo_databrew.types.ordered_by


class FilesLimit(TypedDict, closed=True):
    max_files: "capo_databrew.types.max_files.MaxFiles"
    """<p>The number of Amazon S3 files to select.</p>"""
    ordered_by: NotRequired["capo_databrew.types.ordered_by.OrderedBy"]
    """<p>A criteria to use for Amazon S3 files sorting before their selection. By default uses LAST_MODIFIED_DATE as a sorting criteria. Currently it's the only allowed value.</p>"""
    order: NotRequired["capo_databrew.types.order.Order"]
    """<p>A criteria to use for Amazon S3 files sorting before their selection. By default uses DESCENDING order, i.e. most recent files are selected first. Another possible value is ASCENDING.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: FilesLimit) -> dict:
    out: dict = {}
    out["MaxFiles"] = value["max_files"]
    if "ordered_by" in value:
        import capo_databrew.types.ordered_by

        out["OrderedBy"] = capo_databrew.types.ordered_by.serialize_json(
            value["ordered_by"]
        )
    if "order" in value:
        import capo_databrew.types.order

        out["Order"] = capo_databrew.types.order.serialize_json(value["order"])
    return out


def deserialize_json(data: dict) -> FilesLimit:
    out: FilesLimit = {}  # type: ignore[typeddict-item]
    if data.get("MaxFiles") is not None:
        out["max_files"] = data["MaxFiles"]
    else:
        out["max_files"] = 0
    if data.get("OrderedBy") is not None:
        import capo_databrew.types.ordered_by

        out["ordered_by"] = capo_databrew.types.ordered_by.deserialize_json(
            data["OrderedBy"]
        )
    if data.get("Order") is not None:
        import capo_databrew.types.order

        out["order"] = capo_databrew.types.order.deserialize_json(data["Order"])
    return out
