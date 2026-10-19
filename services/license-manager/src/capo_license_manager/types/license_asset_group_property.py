"""Generated from Smithy shape ``com.amazonaws.licensemanager#LicenseAssetGroupProperty``."""

from typing import TYPE_CHECKING

from typing_extensions import TypedDict

if TYPE_CHECKING:
    import capo_license_manager.types.string


class LicenseAssetGroupProperty(TypedDict, closed=True):
    key: "capo_license_manager.types.string.String"
    """<p>Property key.</p>"""
    value: "capo_license_manager.types.string.String"
    """<p>Property value.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: LicenseAssetGroupProperty) -> dict:
    out: dict = {}
    out["Key"] = value["key"]
    out["Value"] = value["value"]
    return out


def deserialize_aws_json_1_1(data: dict) -> LicenseAssetGroupProperty:
    out: LicenseAssetGroupProperty = {}  # type: ignore[typeddict-item]
    if data.get("Key") is not None:
        out["key"] = data["Key"]
    else:
        out["key"] = ""
    if data.get("Value") is not None:
        out["value"] = data["Value"]
    else:
        out["value"] = ""
    return out
