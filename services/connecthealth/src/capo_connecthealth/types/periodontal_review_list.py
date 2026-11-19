"""Generated from Smithy shape ``com.amazonaws.connecthealth#PeriodontalReviewList``."""

from typing import TYPE_CHECKING, Any, TypeAlias

if TYPE_CHECKING:
    import capo_connecthealth.types.periodontal_review

PeriodontalReviewList: TypeAlias = list[
    "capo_connecthealth.types.periodontal_review.PeriodontalReview"
]


# --- restJson1 ser/de ---
def serialize_json(value: PeriodontalReviewList) -> list:
    import capo_connecthealth.types.periodontal_review

    out: list = []
    for item in value:
        out.append(capo_connecthealth.types.periodontal_review.serialize_json(item))
    return out


def deserialize_json(data: list) -> PeriodontalReviewList:
    import capo_connecthealth.types.periodontal_review

    out: PeriodontalReviewList = []
    for item in data:
        if item is None:
            continue
        out.append(capo_connecthealth.types.periodontal_review.deserialize_json(item))
    return out


def redact_sensitive(value: PeriodontalReviewList) -> list[Any]:
    return ["*** Sensitive Data Redacted ***"] * len(value)
