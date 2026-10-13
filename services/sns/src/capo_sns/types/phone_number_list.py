"""Generated from Smithy shape ``com.amazonaws.sns#PhoneNumberList``."""

from typing import TYPE_CHECKING, Any, TypeAlias

from capo_sns._protocol.xml import Element

if TYPE_CHECKING:
    import capo_sns.types.phone_number

PhoneNumberList: TypeAlias = list["capo_sns.types.phone_number.PhoneNumber"]


# --- awsQuery ser/de ---
def serialize_query(
    value: PhoneNumberList, pairs: list[tuple[str, str]], prefix: str
) -> None:
    if not value:
        pairs.append((prefix, ""))
        return
    for n, item in enumerate(value, 1):
        pairs.append((f"{prefix}.member.{n}", str(item)))


def deserialize_query(el: Element) -> PhoneNumberList:
    out: PhoneNumberList = []
    for child in el.findall("member"):
        out.append(str(child.text or ""))
    return out


def serialize_query_flat(
    value: PhoneNumberList, pairs: list[tuple[str, str]], prefix: str
) -> None:
    if not value:
        pairs.append((prefix, ""))
        return
    for n, item in enumerate(value, 1):
        pairs.append((f"{prefix}.{n}", str(item)))


def deserialize_query_flat(parent: Element, tag: str) -> PhoneNumberList:
    out: PhoneNumberList = []
    for child in parent.findall(tag):
        out.append(str(child.text or ""))
    return out


def redact_sensitive(value: PhoneNumberList) -> list[Any]:
    return ["*** Sensitive Data Redacted ***"] * len(value)
