"""Generated from Smithy shape ``com.amazonaws.guardduty#TacticCoverages``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import capo_guardduty.types.tactic_coverage

TacticCoverages: TypeAlias = list["capo_guardduty.types.tactic_coverage.TacticCoverage"]


# --- restJson1 ser/de ---
def serialize_json(value: TacticCoverages) -> list:
    import capo_guardduty.types.tactic_coverage

    out: list = []
    for item in value:
        out.append(capo_guardduty.types.tactic_coverage.serialize_json(item))
    return out


def deserialize_json(data: list) -> TacticCoverages:
    import capo_guardduty.types.tactic_coverage

    out: TacticCoverages = []
    for item in data:
        if item is None:
            continue
        out.append(capo_guardduty.types.tactic_coverage.deserialize_json(item))
    return out
