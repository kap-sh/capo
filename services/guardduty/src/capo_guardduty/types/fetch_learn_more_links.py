"""Generated from Smithy shape ``com.amazonaws.guardduty#FetchLearnMoreLinks``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import capo_guardduty.types.fetch_learn_more_link

FetchLearnMoreLinks: TypeAlias = list[
    "capo_guardduty.types.fetch_learn_more_link.FetchLearnMoreLink"
]


# --- restJson1 ser/de ---
def serialize_json(value: FetchLearnMoreLinks) -> list:
    return list(value)


def deserialize_json(data: list) -> FetchLearnMoreLinks:
    return [item for item in data if item is not None]
