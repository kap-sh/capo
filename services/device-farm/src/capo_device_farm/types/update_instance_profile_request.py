"""Generated from Smithy shape ``com.amazonaws.devicefarm#UpdateInstanceProfileRequest``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_device_farm.types.amazon_resource_name
    import capo_device_farm.types.boolean
    import capo_device_farm.types.message
    import capo_device_farm.types.name
    import capo_device_farm.types.package_ids


class UpdateInstanceProfileRequest(TypedDict, closed=True):
    arn: "capo_device_farm.types.amazon_resource_name.AmazonResourceName"
    """<p>The Amazon Resource Name (ARN) of the instance profile.</p>"""
    name: NotRequired["capo_device_farm.types.name.Name"]
    """<p>The updated name for your instance profile.</p>"""
    description: NotRequired["capo_device_farm.types.message.Message"]
    """<p>The updated description for your instance profile.</p>"""
    package_cleanup: NotRequired["capo_device_farm.types.boolean.Boolean"]
    """<p>The updated choice for whether you want to specify package cleanup. The default value is <code>false</code> for private devices.</p>"""
    exclude_app_packages_from_cleanup: NotRequired[
        "capo_device_farm.types.package_ids.PackageIds"
    ]
    """<p>An array of strings that specifies the list of app packages that should not be cleaned up from the device after a test run is over.</p> <p>The list of packages is only considered if you set <code>packageCleanup</code> to <code>true</code>.</p>"""
    reboot_after_use: NotRequired["capo_device_farm.types.boolean.Boolean"]
    """<p>The updated choice for whether you want to reboot the device after use. The default value is <code>true</code>.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: UpdateInstanceProfileRequest) -> dict:
    out: dict = {}
    out["arn"] = value["arn"]
    if "name" in value:
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


def deserialize_aws_json_1_1(data: dict) -> UpdateInstanceProfileRequest:
    out: UpdateInstanceProfileRequest = {}  # type: ignore[typeddict-item]
    if data.get("arn") is not None:
        out["arn"] = data["arn"]
    else:
        out["arn"] = ""
    if data.get("name") is not None:
        out["name"] = data["name"]
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
