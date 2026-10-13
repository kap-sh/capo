"""Generated from Smithy shape ``com.amazonaws.sns#PhoneNumberInformationList``."""

from typing import TYPE_CHECKING, Any, TypeAlias

from capo_sns._protocol.xml import Element

if TYPE_CHECKING:
    import capo_sns.types.phone_number_information

PhoneNumberInformationList: TypeAlias = list[
    "capo_sns.types.phone_number_information.PhoneNumberInformation"
]


# --- awsQuery ser/de ---
def serialize_query(
    value: PhoneNumberInformationList, pairs: list[tuple[str, str]], prefix: str
) -> None:
    import capo_sns.types.phone_number_information

    if not value:
        pairs.append((prefix, ""))
        return
    for n, item in enumerate(value, 1):
        capo_sns.types.phone_number_information.serialize_query(
            item, pairs, f"{prefix}.member.{n}"
        )


def deserialize_query(el: Element) -> PhoneNumberInformationList:
    import capo_sns.types.phone_number_information

    out: PhoneNumberInformationList = []
    for child in el.findall("member"):
        out.append(capo_sns.types.phone_number_information.deserialize_query(child))
    return out


def serialize_query_flat(
    value: PhoneNumberInformationList, pairs: list[tuple[str, str]], prefix: str
) -> None:
    import capo_sns.types.phone_number_information

    if not value:
        pairs.append((prefix, ""))
        return
    for n, item in enumerate(value, 1):
        capo_sns.types.phone_number_information.serialize_query(
            item, pairs, f"{prefix}.{n}"
        )


def deserialize_query_flat(parent: Element, tag: str) -> PhoneNumberInformationList:
    import capo_sns.types.phone_number_information

    out: PhoneNumberInformationList = []
    for child in parent.findall(tag):
        out.append(capo_sns.types.phone_number_information.deserialize_query(child))
    return out


def redact_sensitive(value: PhoneNumberInformationList) -> list[Any]:
    import capo_sns.types.phone_number_information

    return [
        capo_sns.types.phone_number_information.redact_sensitive(item) for item in value
    ]
