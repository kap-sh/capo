"""Generated from Smithy shape ``com.amazonaws.workspaces#ImportClientBrandingRequest``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_workspaces.types.default_import_client_branding_attributes
    import capo_workspaces.types.directory_id
    import capo_workspaces.types.ios_import_client_branding_attributes


class ImportClientBrandingRequest(TypedDict, closed=True):
    resource_id: "capo_workspaces.types.directory_id.DirectoryId"
    """<p>The directory identifier of the WorkSpace for which you want to import client branding.</p>"""
    device_type_windows: NotRequired[
        "capo_workspaces.types.default_import_client_branding_attributes.DefaultImportClientBrandingAttributes"
    ]
    """<p>The branding information to import for Windows devices.</p>"""
    device_type_osx: NotRequired[
        "capo_workspaces.types.default_import_client_branding_attributes.DefaultImportClientBrandingAttributes"
    ]
    """<p>The branding information to import for macOS devices.</p>"""
    device_type_android: NotRequired[
        "capo_workspaces.types.default_import_client_branding_attributes.DefaultImportClientBrandingAttributes"
    ]
    """<p>The branding information to import for Android devices.</p>"""
    device_type_ios: NotRequired[
        "capo_workspaces.types.ios_import_client_branding_attributes.IosImportClientBrandingAttributes"
    ]
    """<p>The branding information to import for iOS devices.</p>"""
    device_type_linux: NotRequired[
        "capo_workspaces.types.default_import_client_branding_attributes.DefaultImportClientBrandingAttributes"
    ]
    """<p>The branding information to import for Linux devices.</p>"""
    device_type_web: NotRequired[
        "capo_workspaces.types.default_import_client_branding_attributes.DefaultImportClientBrandingAttributes"
    ]
    """<p>The branding information to import for web access.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: ImportClientBrandingRequest) -> dict:
    out: dict = {}
    out["ResourceId"] = value["resource_id"]
    if "device_type_windows" in value:
        import capo_workspaces.types.default_import_client_branding_attributes

        out["DeviceTypeWindows"] = (
            capo_workspaces.types.default_import_client_branding_attributes.serialize_aws_json_1_1(
                value["device_type_windows"]
            )
        )
    if "device_type_osx" in value:
        import capo_workspaces.types.default_import_client_branding_attributes

        out["DeviceTypeOsx"] = (
            capo_workspaces.types.default_import_client_branding_attributes.serialize_aws_json_1_1(
                value["device_type_osx"]
            )
        )
    if "device_type_android" in value:
        import capo_workspaces.types.default_import_client_branding_attributes

        out["DeviceTypeAndroid"] = (
            capo_workspaces.types.default_import_client_branding_attributes.serialize_aws_json_1_1(
                value["device_type_android"]
            )
        )
    if "device_type_ios" in value:
        import capo_workspaces.types.ios_import_client_branding_attributes

        out["DeviceTypeIos"] = (
            capo_workspaces.types.ios_import_client_branding_attributes.serialize_aws_json_1_1(
                value["device_type_ios"]
            )
        )
    if "device_type_linux" in value:
        import capo_workspaces.types.default_import_client_branding_attributes

        out["DeviceTypeLinux"] = (
            capo_workspaces.types.default_import_client_branding_attributes.serialize_aws_json_1_1(
                value["device_type_linux"]
            )
        )
    if "device_type_web" in value:
        import capo_workspaces.types.default_import_client_branding_attributes

        out["DeviceTypeWeb"] = (
            capo_workspaces.types.default_import_client_branding_attributes.serialize_aws_json_1_1(
                value["device_type_web"]
            )
        )
    return out


def deserialize_aws_json_1_1(data: dict) -> ImportClientBrandingRequest:
    out: ImportClientBrandingRequest = {}  # type: ignore[typeddict-item]
    if data.get("ResourceId") is not None:
        out["resource_id"] = data["ResourceId"]
    else:
        out["resource_id"] = ""
    if data.get("DeviceTypeWindows") is not None:
        import capo_workspaces.types.default_import_client_branding_attributes

        out["device_type_windows"] = (
            capo_workspaces.types.default_import_client_branding_attributes.deserialize_aws_json_1_1(
                data["DeviceTypeWindows"]
            )
        )
    if data.get("DeviceTypeOsx") is not None:
        import capo_workspaces.types.default_import_client_branding_attributes

        out["device_type_osx"] = (
            capo_workspaces.types.default_import_client_branding_attributes.deserialize_aws_json_1_1(
                data["DeviceTypeOsx"]
            )
        )
    if data.get("DeviceTypeAndroid") is not None:
        import capo_workspaces.types.default_import_client_branding_attributes

        out["device_type_android"] = (
            capo_workspaces.types.default_import_client_branding_attributes.deserialize_aws_json_1_1(
                data["DeviceTypeAndroid"]
            )
        )
    if data.get("DeviceTypeIos") is not None:
        import capo_workspaces.types.ios_import_client_branding_attributes

        out["device_type_ios"] = (
            capo_workspaces.types.ios_import_client_branding_attributes.deserialize_aws_json_1_1(
                data["DeviceTypeIos"]
            )
        )
    if data.get("DeviceTypeLinux") is not None:
        import capo_workspaces.types.default_import_client_branding_attributes

        out["device_type_linux"] = (
            capo_workspaces.types.default_import_client_branding_attributes.deserialize_aws_json_1_1(
                data["DeviceTypeLinux"]
            )
        )
    if data.get("DeviceTypeWeb") is not None:
        import capo_workspaces.types.default_import_client_branding_attributes

        out["device_type_web"] = (
            capo_workspaces.types.default_import_client_branding_attributes.deserialize_aws_json_1_1(
                data["DeviceTypeWeb"]
            )
        )
    return out
