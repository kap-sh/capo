"""Generated from Smithy shape ``com.amazonaws.repostspace#AllowedDomainsList``."""

from typing import TYPE_CHECKING, Any, TypeAlias

if TYPE_CHECKING:
    import capo_repostspace.types.email_domain

AllowedDomainsList: TypeAlias = list["capo_repostspace.types.email_domain.EmailDomain"]


# --- restJson1 ser/de ---
def serialize_json(value: AllowedDomainsList) -> list:
    return list(value)


def deserialize_json(data: list) -> AllowedDomainsList:
    return [item for item in data if item is not None]


def redact_sensitive(value: AllowedDomainsList) -> list[Any]:
    return ["*** Sensitive Data Redacted ***"] * len(value)
