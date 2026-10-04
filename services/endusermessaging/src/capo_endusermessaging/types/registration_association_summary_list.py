"""Generated from Smithy shape ``com.amazonaws.endusermessaging#RegistrationAssociationSummaryList``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import capo_endusermessaging.types.registration_association_summary

RegistrationAssociationSummaryList: TypeAlias = list[
    "capo_endusermessaging.types.registration_association_summary.RegistrationAssociationSummary"
]


# --- restJson1 ser/de ---
def serialize_json(value: RegistrationAssociationSummaryList) -> list:
    import capo_endusermessaging.types.registration_association_summary

    out: list = []
    for item in value:
        out.append(
            capo_endusermessaging.types.registration_association_summary.serialize_json(
                item
            )
        )
    return out


def deserialize_json(data: list) -> RegistrationAssociationSummaryList:
    import capo_endusermessaging.types.registration_association_summary

    out: RegistrationAssociationSummaryList = []
    for item in data:
        if item is None:
            continue
        out.append(
            capo_endusermessaging.types.registration_association_summary.deserialize_json(
                item
            )
        )
    return out
