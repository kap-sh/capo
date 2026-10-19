"""Generated from Smithy shape ``com.amazonaws.lakeformation#WorkUnitRange``."""

from typing import TYPE_CHECKING

from typing_extensions import TypedDict

if TYPE_CHECKING:
    import capo_lakeformation.types.work_unit_id_long
    import capo_lakeformation.types.work_unit_token_string


class WorkUnitRange(TypedDict, closed=True):
    work_unit_id_max: "capo_lakeformation.types.work_unit_id_long.WorkUnitIdLong"
    """<p>Defines the maximum work unit ID in the range. The maximum value is inclusive.</p>"""
    work_unit_id_min: "capo_lakeformation.types.work_unit_id_long.WorkUnitIdLong"
    """<p>Defines the minimum work unit ID in the range.</p>"""
    work_unit_token: (
        "capo_lakeformation.types.work_unit_token_string.WorkUnitTokenString"
    )
    """<p>A work token used to query the execution service.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: WorkUnitRange) -> dict:
    out: dict = {}
    out["WorkUnitIdMax"] = value.get("work_unit_id_max", 0)
    out["WorkUnitIdMin"] = value.get("work_unit_id_min", 0)
    out["WorkUnitToken"] = value["work_unit_token"]
    return out


def deserialize_json(data: dict) -> WorkUnitRange:
    out: WorkUnitRange = {}  # type: ignore[typeddict-item]
    if data.get("WorkUnitIdMax") is not None:
        out["work_unit_id_max"] = data["WorkUnitIdMax"]
    else:
        out["work_unit_id_max"] = 0
    if data.get("WorkUnitIdMin") is not None:
        out["work_unit_id_min"] = data["WorkUnitIdMin"]
    else:
        out["work_unit_id_min"] = 0
    if data.get("WorkUnitToken") is not None:
        out["work_unit_token"] = data["WorkUnitToken"]
    else:
        out["work_unit_token"] = ""
    return out
