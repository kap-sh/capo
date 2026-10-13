"""Generated from Smithy shape ``com.amazonaws.sesv2#EmailSubjectFilterList``."""

from typing import TYPE_CHECKING, Any, TypeAlias

if TYPE_CHECKING:
    import capo_sesv2.types.email_subject

EmailSubjectFilterList: TypeAlias = list["capo_sesv2.types.email_subject.EmailSubject"]


# --- restJson1 ser/de ---
def serialize_json(value: EmailSubjectFilterList) -> list:
    return list(value)


def deserialize_json(data: list) -> EmailSubjectFilterList:
    return [item for item in data if item is not None]


def redact_sensitive(value: EmailSubjectFilterList) -> list[Any]:
    return ["*** Sensitive Data Redacted ***"] * len(value)
