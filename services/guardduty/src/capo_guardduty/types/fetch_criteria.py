"""Generated from Smithy shape ``com.amazonaws.guardduty#FetchCriteria``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import capo_guardduty.types.fetch_criterion

FetchCriteria: TypeAlias = list["capo_guardduty.types.fetch_criterion.FetchCriterion"]


# --- restJson1 ser/de ---
def serialize_json(value: FetchCriteria) -> list:
    import capo_guardduty.types.fetch_criterion

    out: list = []
    for item in value:
        out.append(capo_guardduty.types.fetch_criterion.serialize_json(item))
    return out


def deserialize_json(data: list) -> FetchCriteria:
    import capo_guardduty.types.fetch_criterion

    out: FetchCriteria = []
    for item in data:
        if item is None:
            continue
        out.append(capo_guardduty.types.fetch_criterion.deserialize_json(item))
    return out
