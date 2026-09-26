"""Generated from Smithy shape ``com.amazonaws.supportauthz#SupportPermitSummaries``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import capo_supportauthz.types.support_permit_summary

SupportPermitSummaries: TypeAlias = list[
    "capo_supportauthz.types.support_permit_summary.SupportPermitSummary"
]


# --- restJson1 ser/de ---
def serialize_json(value: SupportPermitSummaries) -> list:
    import capo_supportauthz.types.support_permit_summary

    out: list = []
    for item in value:
        out.append(capo_supportauthz.types.support_permit_summary.serialize_json(item))
    return out


def deserialize_json(data: list) -> SupportPermitSummaries:
    import capo_supportauthz.types.support_permit_summary

    out: SupportPermitSummaries = []
    for item in data:
        if item is None:
            continue
        out.append(
            capo_supportauthz.types.support_permit_summary.deserialize_json(item)
        )
    return out
