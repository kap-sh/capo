"""Generated from Smithy shape ``com.amazonaws.securityir#ListCasesItems``."""

from typing import TYPE_CHECKING, Any, TypeAlias

if TYPE_CHECKING:
    import capo_security_ir.types.list_cases_item

ListCasesItems: TypeAlias = list["capo_security_ir.types.list_cases_item.ListCasesItem"]


# --- restJson1 ser/de ---
def serialize_json(value: ListCasesItems) -> list:
    import capo_security_ir.types.list_cases_item

    out: list = []
    for item in value:
        out.append(capo_security_ir.types.list_cases_item.serialize_json(item))
    return out


def deserialize_json(data: list) -> ListCasesItems:
    import capo_security_ir.types.list_cases_item

    out: ListCasesItems = []
    for item in data:
        if item is None:
            continue
        out.append(capo_security_ir.types.list_cases_item.deserialize_json(item))
    return out


def redact_sensitive(value: ListCasesItems) -> list[Any]:
    import capo_security_ir.types.list_cases_item

    return [
        capo_security_ir.types.list_cases_item.redact_sensitive(item) for item in value
    ]
