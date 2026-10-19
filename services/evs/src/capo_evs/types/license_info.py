"""Generated from Smithy shape ``com.amazonaws.evs#LicenseInfo``."""

from typing import TYPE_CHECKING, Any

from typing_extensions import TypedDict

if TYPE_CHECKING:
    import capo_evs.types.solution_key
    import capo_evs.types.v_san_license_key


class LicenseInfo(TypedDict, closed=True):
    solution_key: "capo_evs.types.solution_key.SolutionKey"
    """<p> The VCF solution key. This license unlocks VMware VCF product features, including vSphere, NSX, SDDC Manager, and vCenter Server. The VCF solution key must meet the instance-type-specific minimum core requirements.</p>"""
    vsan_key: "capo_evs.types.v_san_license_key.VSanLicenseKey"
    """<p> The VSAN license key. This license unlocks vSAN features. The vSAN license key must meet the instance-type-specific minimum capacity requirements.</p>"""


# --- awsJson1_0 ser/de ---
def serialize_aws_json_1_0(value: LicenseInfo) -> dict:
    out: dict = {}
    out["solutionKey"] = value["solution_key"]
    out["vsanKey"] = value["vsan_key"]
    return out


def deserialize_aws_json_1_0(data: dict) -> LicenseInfo:
    out: LicenseInfo = {}  # type: ignore[typeddict-item]
    if data.get("solutionKey") is not None:
        out["solution_key"] = data["solutionKey"]
    else:
        out["solution_key"] = ""
    if data.get("vsanKey") is not None:
        out["vsan_key"] = data["vsanKey"]
    else:
        out["vsan_key"] = ""
    return out


def redact_sensitive(value: LicenseInfo) -> dict[str, Any]:
    out: dict[str, Any] = dict(value)
    if "solution_key" in value:
        out["solution_key"] = "*** Sensitive Data Redacted ***"
    if "vsan_key" in value:
        out["vsan_key"] = "*** Sensitive Data Redacted ***"
    return out
