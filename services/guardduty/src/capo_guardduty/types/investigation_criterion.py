"""Generated from Smithy shape ``com.amazonaws.guardduty#InvestigationCriterion``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import capo_guardduty.types.investigation_filter_condition
    import capo_guardduty.types.investigation_filter_criterion_key

InvestigationCriterion: TypeAlias = dict[
    "capo_guardduty.types.investigation_filter_criterion_key.InvestigationFilterCriterionKey",
    "capo_guardduty.types.investigation_filter_condition.InvestigationFilterCondition",
]


# --- restJson1 ser/de ---
def serialize_json(input_to_serialize: InvestigationCriterion) -> dict:
    out: dict = {}
    for key, value in input_to_serialize.items():
        import capo_guardduty.types.investigation_filter_condition
        import capo_guardduty.types.investigation_filter_criterion_key

        out[
            capo_guardduty.types.investigation_filter_criterion_key.serialize_json(key)
        ] = capo_guardduty.types.investigation_filter_condition.serialize_json(value)
    return out


def deserialize_json(data: dict) -> InvestigationCriterion:
    out: InvestigationCriterion = {}
    for key, value in data.items():
        import capo_guardduty.types.investigation_filter_criterion_key

        if value is None:
            continue
        import capo_guardduty.types.investigation_filter_condition

        out[
            capo_guardduty.types.investigation_filter_criterion_key.deserialize_json(
                key
            )
        ] = capo_guardduty.types.investigation_filter_condition.deserialize_json(value)
    return out
