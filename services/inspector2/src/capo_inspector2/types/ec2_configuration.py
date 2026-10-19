"""Generated from Smithy shape ``com.amazonaws.inspector2#Ec2Configuration``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_inspector2.types.ec2_scan_mode


class Ec2Configuration(TypedDict, closed=True):
    scan_mode: "capo_inspector2.types.ec2_scan_mode.Ec2ScanMode"
    """<p>The scan method that is applied to the instance.</p>"""
    activate_vm_scanner: NotRequired["bool"]
    """<p>Whether to activate Amazon Inspector VM scanner for Amazon EC2 scanning.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: Ec2Configuration) -> dict:
    out: dict = {}
    out["scanMode"] = value["scan_mode"]
    if "activate_vm_scanner" in value:
        out["activateVMScanner"] = value["activate_vm_scanner"]
    return out


def deserialize_json(data: dict) -> Ec2Configuration:
    out: Ec2Configuration = {}  # type: ignore[typeddict-item]
    if data.get("scanMode") is not None:
        out["scan_mode"] = data["scanMode"]
    else:
        out["scan_mode"] = ""
    if data.get("activateVMScanner") is not None:
        out["activate_vm_scanner"] = data["activateVMScanner"]
    return out
