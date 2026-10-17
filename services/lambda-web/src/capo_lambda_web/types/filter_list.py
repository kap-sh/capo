"""Generated from Smithy shape ``com.amazonaws.lambdaweb#FilterList``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import capo_lambda_web.types.filter

FilterList: TypeAlias = list["capo_lambda_web.types.filter.Filter"]


# --- restJson1 ser/de ---
def serialize_json(value: FilterList) -> list:
    import capo_lambda_web.types.filter

    out: list = []
    for item in value:
        out.append(capo_lambda_web.types.filter.serialize_json(item))
    return out


def deserialize_json(data: list) -> FilterList:
    import capo_lambda_web.types.filter

    out: FilterList = []
    for item in data:
        if item is None:
            continue
        out.append(capo_lambda_web.types.filter.deserialize_json(item))
    return out
