"""Generated from Smithy shape ``com.amazonaws.lambdamicrovms#MicrovmItemList``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import capo_lambda_microvms.types.microvm_item

MicrovmItemList: TypeAlias = list["capo_lambda_microvms.types.microvm_item.MicrovmItem"]


# --- restJson1 ser/de ---
def serialize_json(value: MicrovmItemList) -> list:
    import capo_lambda_microvms.types.microvm_item

    out: list = []
    for item in value:
        out.append(capo_lambda_microvms.types.microvm_item.serialize_json(item))
    return out


def deserialize_json(data: list) -> MicrovmItemList:
    import capo_lambda_microvms.types.microvm_item

    out: MicrovmItemList = []
    for item in data:
        if item is None:
            continue
        out.append(capo_lambda_microvms.types.microvm_item.deserialize_json(item))
    return out
