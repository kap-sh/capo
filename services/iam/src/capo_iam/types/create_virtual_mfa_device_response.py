"""Generated from Smithy shape ``com.amazonaws.iam#CreateVirtualMFADeviceResponse``."""

from typing import TYPE_CHECKING, Any

from typing_extensions import TypedDict

from capo_iam._protocol.xml import Element
from capo_iam.errors import DeserializationError

if TYPE_CHECKING:
    import capo_iam.types.virtual_mfa_device


class CreateVirtualMFADeviceResponse(TypedDict, closed=True):
    virtual_mfa_device: "capo_iam.types.virtual_mfa_device.VirtualMFADevice"
    """<p>A structure containing details about the new virtual MFA device.</p>"""


# --- awsQuery ser/de ---
def serialize_query(
    value: CreateVirtualMFADeviceResponse, pairs: list[tuple[str, str]], prefix: str
) -> None:
    key_prefix = f"{prefix}." if prefix else ""
    import capo_iam.types.virtual_mfa_device

    capo_iam.types.virtual_mfa_device.serialize_query(
        value["virtual_mfa_device"], pairs, f"{key_prefix}VirtualMFADevice"
    )


def deserialize_query(el: Element) -> CreateVirtualMFADeviceResponse:
    out: CreateVirtualMFADeviceResponse = {}  # type: ignore[typeddict-item]
    child_virtual_mfa_device = el.find("VirtualMFADevice")
    if child_virtual_mfa_device is not None:
        import capo_iam.types.virtual_mfa_device

        out["virtual_mfa_device"] = capo_iam.types.virtual_mfa_device.deserialize_query(
            child_virtual_mfa_device
        )
    else:
        raise DeserializationError(
            "CreateVirtualMFADeviceResponse.virtual_mfa_device required"
        )
    return out


def redact_sensitive(value: CreateVirtualMFADeviceResponse) -> dict[str, Any]:
    out: dict[str, Any] = dict(value)
    if "virtual_mfa_device" in value:
        import capo_iam.types.virtual_mfa_device

        out["virtual_mfa_device"] = capo_iam.types.virtual_mfa_device.redact_sensitive(
            value["virtual_mfa_device"]
        )
    return out
