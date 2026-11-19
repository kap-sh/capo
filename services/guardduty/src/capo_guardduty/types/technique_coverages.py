"""Generated from Smithy shape ``com.amazonaws.guardduty#TechniqueCoverages``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import capo_guardduty.types.technique_coverage

TechniqueCoverages: TypeAlias = list[
    "capo_guardduty.types.technique_coverage.TechniqueCoverage"
]


# --- restJson1 ser/de ---
def serialize_json(value: TechniqueCoverages) -> list:
    import capo_guardduty.types.technique_coverage

    out: list = []
    for item in value:
        out.append(capo_guardduty.types.technique_coverage.serialize_json(item))
    return out


def deserialize_json(data: list) -> TechniqueCoverages:
    import capo_guardduty.types.technique_coverage

    out: TechniqueCoverages = []
    for item in data:
        if item is None:
            continue
        out.append(capo_guardduty.types.technique_coverage.deserialize_json(item))
    return out
