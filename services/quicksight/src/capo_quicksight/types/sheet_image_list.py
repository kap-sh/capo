"""Generated from Smithy shape ``com.amazonaws.quicksight#SheetImageList``."""

from typing import TYPE_CHECKING, Any, TypeAlias

if TYPE_CHECKING:
    import capo_quicksight.types.sheet_image

SheetImageList: TypeAlias = list["capo_quicksight.types.sheet_image.SheetImage"]


# --- restJson1 ser/de ---
def serialize_json(value: SheetImageList) -> list:
    import capo_quicksight.types.sheet_image

    out: list = []
    for item in value:
        out.append(capo_quicksight.types.sheet_image.serialize_json(item))
    return out


def deserialize_json(data: list) -> SheetImageList:
    import capo_quicksight.types.sheet_image

    out: SheetImageList = []
    for item in data:
        if item is None:
            continue
        out.append(capo_quicksight.types.sheet_image.deserialize_json(item))
    return out


def redact_sensitive(value: SheetImageList) -> list[Any]:
    import capo_quicksight.types.sheet_image

    return [capo_quicksight.types.sheet_image.redact_sensitive(item) for item in value]
