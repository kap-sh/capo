"""Generated from Smithy shape ``com.amazonaws.quicksight#Sheet``."""

from typing import TYPE_CHECKING, Any

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_quicksight.types.sheet_image_list
    import capo_quicksight.types.sheet_name
    import capo_quicksight.types.short_restrictive_resource_id


class Sheet(TypedDict, closed=True):
    sheet_id: NotRequired[
        "capo_quicksight.types.short_restrictive_resource_id.ShortRestrictiveResourceId"
    ]
    """<p>The unique identifier associated with a sheet.</p>"""
    name: NotRequired["capo_quicksight.types.sheet_name.SheetName"]
    """<p>The name of a sheet. This name is displayed on the sheet's tab in the Quick Sight console.</p>"""
    images: NotRequired["capo_quicksight.types.sheet_image_list.SheetImageList"]
    """<p>A list of images on a sheet.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: Sheet) -> dict:
    out: dict = {}
    if "sheet_id" in value:
        out["SheetId"] = value["sheet_id"]
    if "name" in value:
        out["Name"] = value["name"]
    if "images" in value:
        import capo_quicksight.types.sheet_image_list

        out["Images"] = capo_quicksight.types.sheet_image_list.serialize_json(
            value["images"]
        )
    return out


def deserialize_json(data: dict) -> Sheet:
    out: Sheet = {}  # type: ignore[typeddict-item]
    if data.get("SheetId") is not None:
        out["sheet_id"] = data["SheetId"]
    if data.get("Name") is not None:
        out["name"] = data["Name"]
    if data.get("Images") is not None:
        import capo_quicksight.types.sheet_image_list

        out["images"] = capo_quicksight.types.sheet_image_list.deserialize_json(
            data["Images"]
        )
    return out


def redact_sensitive(value: Sheet) -> dict[str, Any]:
    out: dict[str, Any] = dict(value)
    if "images" in value:
        import capo_quicksight.types.sheet_image_list

        out["images"] = capo_quicksight.types.sheet_image_list.redact_sensitive(
            value["images"]
        )
    return out
