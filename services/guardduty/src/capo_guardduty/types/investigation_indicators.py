"""Generated from Smithy shape ``com.amazonaws.guardduty#InvestigationIndicators``."""

from typing import TYPE_CHECKING, Any, TypeAlias

if TYPE_CHECKING:
    import capo_guardduty.types.investigation_indicator

InvestigationIndicators: TypeAlias = list[
    "capo_guardduty.types.investigation_indicator.InvestigationIndicator"
]


# --- restJson1 ser/de ---
def serialize_json(value: InvestigationIndicators) -> list:
    import capo_guardduty.types.investigation_indicator

    out: list = []
    for item in value:
        out.append(capo_guardduty.types.investigation_indicator.serialize_json(item))
    return out


def deserialize_json(data: list) -> InvestigationIndicators:
    import capo_guardduty.types.investigation_indicator

    out: InvestigationIndicators = []
    for item in data:
        if item is None:
            continue
        out.append(capo_guardduty.types.investigation_indicator.deserialize_json(item))
    return out


def redact_sensitive(value: InvestigationIndicators) -> list[Any]:
    import capo_guardduty.types.investigation_indicator

    return [
        capo_guardduty.types.investigation_indicator.redact_sensitive(item)
        for item in value
    ]
