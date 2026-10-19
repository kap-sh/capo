"""Generated from Smithy shape ``com.amazonaws.devicefarm#CreateInstanceProfileRequest``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_device_farm.types.boolean
    import capo_device_farm.types.message
    import capo_device_farm.types.name
    import capo_device_farm.types.package_ids


class CreateInstanceProfileRequest(TypedDict, closed=True):
    name: "capo_device_farm.types.name.Name"
    """<p>The name of your instance profile.</p>"""
    description: NotRequired["capo_device_farm.types.message.Message"]
    """<p>The description of your instance profile.</p>"""
    package_cleanup: NotRequired["capo_device_farm.types.boolean.Boolean"]
    """<p>When set to <code>true</code>, Device Farm removes app packages after a test run. The default value is <code>false</code> for private devices.</p>"""
    exclude_app_packages_from_cleanup: NotRequired[
        "capo_device_farm.types.package_ids.PackageIds"
    ]
    """<p>An array of strings that specifies the list of app packages that should not be cleaned up from the device after a test run.</p> <p>The list of packages is considered only if you set <code>packageCleanup</code> to <code>true</code>.</p>"""
    reboot_after_use: NotRequired["capo_device_farm.types.boolean.Boolean"]
    """<p>When set to <code>true</code>, Device Farm reboots the instance after a test run. The default value is <code>true</code>.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: CreateInstanceProfileRequest) -> dict:
    out: dict = {}
    out["name"] = value["name"]
    if "description" in value:
        out["description"] = value["description"]
    if "package_cleanup" in value:
        out["packageCleanup"] = value["package_cleanup"]
    if "exclude_app_packages_from_cleanup" in value:
        import capo_device_farm.types.package_ids

        out["excludeAppPackagesFromCleanup"] = (
            capo_device_farm.types.package_ids.serialize_aws_json_1_1(
                value["exclude_app_packages_from_cleanup"]
            )
        )
    if "reboot_after_use" in value:
        out["rebootAfterUse"] = value["reboot_after_use"]
    return out


def deserialize_aws_json_1_1(data: dict) -> CreateInstanceProfileRequest:
    out: CreateInstanceProfileRequest = {}  # type: ignore[typeddict-item]
    if data.get("name") is not None:
        out["name"] = data["name"]
    else:
        out["name"] = ""
    if data.get("description") is not None:
        out["description"] = data["description"]
    if data.get("packageCleanup") is not None:
        out["package_cleanup"] = data["packageCleanup"]
    if data.get("excludeAppPackagesFromCleanup") is not None:
        import capo_device_farm.types.package_ids

        out["exclude_app_packages_from_cleanup"] = (
            capo_device_farm.types.package_ids.deserialize_aws_json_1_1(
                data["excludeAppPackagesFromCleanup"]
            )
        )
    if data.get("rebootAfterUse") is not None:
        out["reboot_after_use"] = data["rebootAfterUse"]
    return out
