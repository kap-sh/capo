"""Generated from Smithy shape ``com.amazonaws.accountaccess#ApplicationList``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import capo_account_access.types.application_summary

ApplicationList: TypeAlias = list[
    "capo_account_access.types.application_summary.ApplicationSummary"
]


# --- restJson1 ser/de ---
def serialize_json(value: ApplicationList) -> list:
    import capo_account_access.types.application_summary

    out: list = []
    for item in value:
        out.append(capo_account_access.types.application_summary.serialize_json(item))
    return out


def deserialize_json(data: list) -> ApplicationList:
    import capo_account_access.types.application_summary

    out: ApplicationList = []
    for item in data:
        if item is None:
            continue
        out.append(capo_account_access.types.application_summary.deserialize_json(item))
    return out
