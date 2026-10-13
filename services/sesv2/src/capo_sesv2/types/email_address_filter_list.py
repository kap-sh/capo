"""Generated from Smithy shape ``com.amazonaws.sesv2#EmailAddressFilterList``."""

from typing import TYPE_CHECKING, Any, TypeAlias

if TYPE_CHECKING:
    import capo_sesv2.types.insights_email_address

EmailAddressFilterList: TypeAlias = list[
    "capo_sesv2.types.insights_email_address.InsightsEmailAddress"
]


# --- restJson1 ser/de ---
def serialize_json(value: EmailAddressFilterList) -> list:
    return list(value)


def deserialize_json(data: list) -> EmailAddressFilterList:
    return [item for item in data if item is not None]


def redact_sensitive(value: EmailAddressFilterList) -> list[Any]:
    return ["*** Sensitive Data Redacted ***"] * len(value)
