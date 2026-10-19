"""Generated from Smithy shape ``com.amazonaws.quicksight#LocalNavigationConfiguration``."""

from typing import TYPE_CHECKING

from typing_extensions import TypedDict

if TYPE_CHECKING:
    import capo_quicksight.types.short_restrictive_resource_id


class LocalNavigationConfiguration(TypedDict, closed=True):
    target_sheet_id: (
        "capo_quicksight.types.short_restrictive_resource_id.ShortRestrictiveResourceId"
    )
    """<p>The sheet that is targeted for navigation in the same analysis.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: LocalNavigationConfiguration) -> dict:
    out: dict = {}
    out["TargetSheetId"] = value["target_sheet_id"]
    return out


def deserialize_json(data: dict) -> LocalNavigationConfiguration:
    out: LocalNavigationConfiguration = {}  # type: ignore[typeddict-item]
    if data.get("TargetSheetId") is not None:
        out["target_sheet_id"] = data["TargetSheetId"]
    else:
        out["target_sheet_id"] = ""
    return out
