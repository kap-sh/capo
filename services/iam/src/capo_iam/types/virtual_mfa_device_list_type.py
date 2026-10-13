"""Generated from Smithy shape ``com.amazonaws.iam#virtualMFADeviceListType``."""

from typing import TYPE_CHECKING, Any, TypeAlias

from capo_iam._protocol.xml import Element

if TYPE_CHECKING:
    import capo_iam.types.virtual_mfa_device

virtualMFADeviceListType: TypeAlias = list[
    "capo_iam.types.virtual_mfa_device.VirtualMFADevice"
]


# --- awsQuery ser/de ---
def serialize_query(
    value: virtualMFADeviceListType, pairs: list[tuple[str, str]], prefix: str
) -> None:
    import capo_iam.types.virtual_mfa_device

    if not value:
        pairs.append((prefix, ""))
        return
    for n, item in enumerate(value, 1):
        capo_iam.types.virtual_mfa_device.serialize_query(
            item, pairs, f"{prefix}.member.{n}"
        )


def deserialize_query(el: Element) -> virtualMFADeviceListType:
    import capo_iam.types.virtual_mfa_device

    out: virtualMFADeviceListType = []
    for child in el.findall("member"):
        out.append(capo_iam.types.virtual_mfa_device.deserialize_query(child))
    return out


def serialize_query_flat(
    value: virtualMFADeviceListType, pairs: list[tuple[str, str]], prefix: str
) -> None:
    import capo_iam.types.virtual_mfa_device

    if not value:
        pairs.append((prefix, ""))
        return
    for n, item in enumerate(value, 1):
        capo_iam.types.virtual_mfa_device.serialize_query(item, pairs, f"{prefix}.{n}")


def deserialize_query_flat(parent: Element, tag: str) -> virtualMFADeviceListType:
    import capo_iam.types.virtual_mfa_device

    out: virtualMFADeviceListType = []
    for child in parent.findall(tag):
        out.append(capo_iam.types.virtual_mfa_device.deserialize_query(child))
    return out


def redact_sensitive(value: virtualMFADeviceListType) -> list[Any]:
    import capo_iam.types.virtual_mfa_device

    return [capo_iam.types.virtual_mfa_device.redact_sensitive(item) for item in value]
