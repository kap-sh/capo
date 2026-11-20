"""Generated from Smithy shape ``com.amazonaws.abusesignal#SubmissionRequirementList``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import capo_abuse_signal.types.submission_requirement

SubmissionRequirementList: TypeAlias = list[
    "capo_abuse_signal.types.submission_requirement.SubmissionRequirement"
]


# --- restJson1 ser/de ---
def serialize_json(value: SubmissionRequirementList) -> list:
    import capo_abuse_signal.types.submission_requirement

    out: list = []
    for item in value:
        out.append(capo_abuse_signal.types.submission_requirement.serialize_json(item))
    return out


def deserialize_json(data: list) -> SubmissionRequirementList:
    import capo_abuse_signal.types.submission_requirement

    out: SubmissionRequirementList = []
    for item in data:
        if item is None:
            continue
        out.append(
            capo_abuse_signal.types.submission_requirement.deserialize_json(item)
        )
    return out
