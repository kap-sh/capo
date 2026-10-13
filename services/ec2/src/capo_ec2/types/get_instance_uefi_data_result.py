"""Generated from Smithy shape ``com.amazonaws.ec2#GetInstanceUefiDataResult``."""

from typing import TYPE_CHECKING, Any

from typing_extensions import NotRequired, TypedDict

from capo_ec2._protocol.xml import Element

if TYPE_CHECKING:
    import capo_ec2.types.instance_id
    import capo_ec2.types.sensitive_string


class GetInstanceUefiDataResult(TypedDict, closed=True):
    instance_id: NotRequired["capo_ec2.types.instance_id.InstanceId"]
    """<p>The ID of the instance from which to retrieve the UEFI data.</p>"""
    uefi_data: NotRequired["capo_ec2.types.sensitive_string.SensitiveString"]
    """<p>Base64 representation of the non-volatile UEFI variable store.</p>"""


# --- ec2Query ser/de ---
def serialize_ec2_query(
    value: GetInstanceUefiDataResult, pairs: list[tuple[str, str]], prefix: str
) -> None:
    key_prefix = f"{prefix}." if prefix else ""
    if "instance_id" in value:
        pairs.append((f"{key_prefix}InstanceId", str(value["instance_id"])))
    if "uefi_data" in value:
        pairs.append((f"{key_prefix}UefiData", str(value["uefi_data"])))


def deserialize_ec2_query(el: Element) -> GetInstanceUefiDataResult:
    out: GetInstanceUefiDataResult = {}  # type: ignore[typeddict-item]
    child_instance_id = el.find("instanceId")
    if child_instance_id is not None:
        out["instance_id"] = str(child_instance_id.text or "")
    child_uefi_data = el.find("uefiData")
    if child_uefi_data is not None:
        out["uefi_data"] = str(child_uefi_data.text or "")
    return out


def redact_sensitive(value: GetInstanceUefiDataResult) -> dict[str, Any]:
    out: dict[str, Any] = dict(value)
    if "uefi_data" in value:
        out["uefi_data"] = "*** Sensitive Data Redacted ***"
    return out
