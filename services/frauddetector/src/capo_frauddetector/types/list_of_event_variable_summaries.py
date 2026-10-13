"""Generated from Smithy shape ``com.amazonaws.frauddetector#ListOfEventVariableSummaries``."""

from typing import TYPE_CHECKING, Any, TypeAlias

if TYPE_CHECKING:
    import capo_frauddetector.types.event_variable_summary

ListOfEventVariableSummaries: TypeAlias = list[
    "capo_frauddetector.types.event_variable_summary.EventVariableSummary"
]


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: ListOfEventVariableSummaries) -> list:
    import capo_frauddetector.types.event_variable_summary

    out: list = []
    for item in value:
        out.append(
            capo_frauddetector.types.event_variable_summary.serialize_aws_json_1_1(item)
        )
    return out


def deserialize_aws_json_1_1(data: list) -> ListOfEventVariableSummaries:
    import capo_frauddetector.types.event_variable_summary

    out: ListOfEventVariableSummaries = []
    for item in data:
        if item is None:
            continue
        out.append(
            capo_frauddetector.types.event_variable_summary.deserialize_aws_json_1_1(
                item
            )
        )
    return out


def redact_sensitive(value: ListOfEventVariableSummaries) -> list[Any]:
    import capo_frauddetector.types.event_variable_summary

    return [
        capo_frauddetector.types.event_variable_summary.redact_sensitive(item)
        for item in value
    ]
