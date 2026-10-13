"""Generated from Smithy shape ``com.amazonaws.sns#SMSSandboxPhoneNumberList``."""

from typing import TYPE_CHECKING, Any, TypeAlias

from capo_sns._protocol.xml import Element

if TYPE_CHECKING:
    import capo_sns.types.sms_sandbox_phone_number

SMSSandboxPhoneNumberList: TypeAlias = list[
    "capo_sns.types.sms_sandbox_phone_number.SMSSandboxPhoneNumber"
]


# --- awsQuery ser/de ---
def serialize_query(
    value: SMSSandboxPhoneNumberList, pairs: list[tuple[str, str]], prefix: str
) -> None:
    import capo_sns.types.sms_sandbox_phone_number

    if not value:
        pairs.append((prefix, ""))
        return
    for n, item in enumerate(value, 1):
        capo_sns.types.sms_sandbox_phone_number.serialize_query(
            item, pairs, f"{prefix}.member.{n}"
        )


def deserialize_query(el: Element) -> SMSSandboxPhoneNumberList:
    import capo_sns.types.sms_sandbox_phone_number

    out: SMSSandboxPhoneNumberList = []
    for child in el.findall("member"):
        out.append(capo_sns.types.sms_sandbox_phone_number.deserialize_query(child))
    return out


def serialize_query_flat(
    value: SMSSandboxPhoneNumberList, pairs: list[tuple[str, str]], prefix: str
) -> None:
    import capo_sns.types.sms_sandbox_phone_number

    if not value:
        pairs.append((prefix, ""))
        return
    for n, item in enumerate(value, 1):
        capo_sns.types.sms_sandbox_phone_number.serialize_query(
            item, pairs, f"{prefix}.{n}"
        )


def deserialize_query_flat(parent: Element, tag: str) -> SMSSandboxPhoneNumberList:
    import capo_sns.types.sms_sandbox_phone_number

    out: SMSSandboxPhoneNumberList = []
    for child in parent.findall(tag):
        out.append(capo_sns.types.sms_sandbox_phone_number.deserialize_query(child))
    return out


def redact_sensitive(value: SMSSandboxPhoneNumberList) -> list[Any]:
    import capo_sns.types.sms_sandbox_phone_number

    return [
        capo_sns.types.sms_sandbox_phone_number.redact_sensitive(item) for item in value
    ]
