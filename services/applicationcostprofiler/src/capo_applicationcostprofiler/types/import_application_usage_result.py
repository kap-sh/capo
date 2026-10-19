"""Generated from Smithy shape ``com.amazonaws.applicationcostprofiler#ImportApplicationUsageResult``."""

from typing import TYPE_CHECKING

from typing_extensions import TypedDict

if TYPE_CHECKING:
    import capo_applicationcostprofiler.types.import_id


class ImportApplicationUsageResult(TypedDict, closed=True):
    import_id: "capo_applicationcostprofiler.types.import_id.ImportId"
    """<p>ID of the import request.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: ImportApplicationUsageResult) -> dict:
    out: dict = {}
    out["importId"] = value["import_id"]
    return out


def deserialize_json(data: dict) -> ImportApplicationUsageResult:
    out: ImportApplicationUsageResult = {}  # type: ignore[typeddict-item]
    if data.get("importId") is not None:
        out["import_id"] = data["importId"]
    else:
        out["import_id"] = ""
    return out
