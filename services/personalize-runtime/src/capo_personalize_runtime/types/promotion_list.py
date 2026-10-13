"""Generated from Smithy shape ``com.amazonaws.personalizeruntime#PromotionList``."""

from typing import TYPE_CHECKING, Any, TypeAlias

if TYPE_CHECKING:
    import capo_personalize_runtime.types.promotion

PromotionList: TypeAlias = list["capo_personalize_runtime.types.promotion.Promotion"]


# --- restJson1 ser/de ---
def serialize_json(value: PromotionList) -> list:
    import capo_personalize_runtime.types.promotion

    out: list = []
    for item in value:
        out.append(capo_personalize_runtime.types.promotion.serialize_json(item))
    return out


def deserialize_json(data: list) -> PromotionList:
    import capo_personalize_runtime.types.promotion

    out: PromotionList = []
    for item in data:
        if item is None:
            continue
        out.append(capo_personalize_runtime.types.promotion.deserialize_json(item))
    return out


def redact_sensitive(value: PromotionList) -> list[Any]:
    import capo_personalize_runtime.types.promotion

    return [
        capo_personalize_runtime.types.promotion.redact_sensitive(item)
        for item in value
    ]
