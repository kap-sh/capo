"""Generated from Smithy shape ``com.amazonaws.workspaces#ImportClientBrandingResult``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_workspaces.types.default_client_branding_attributes
    import capo_workspaces.types.ios_client_branding_attributes


class ImportClientBrandingResult(TypedDict, closed=True):
    device_type_windows: NotRequired[
        "capo_workspaces.types.default_client_branding_attributes.DefaultClientBrandingAttributes"
    ]
    """<p>The branding information configured for Windows devices.</p>"""
    device_type_osx: NotRequired[
        "capo_workspaces.types.default_client_branding_attributes.DefaultClientBrandingAttributes"
    ]
    """<p>The branding information configured for macOS devices.</p>"""
    device_type_android: NotRequired[
        "capo_workspaces.types.default_client_branding_attributes.DefaultClientBrandingAttributes"
    ]
    """<p>The branding information configured for Android devices.</p>"""
    device_type_ios: NotRequired[
        "capo_workspaces.types.ios_client_branding_attributes.IosClientBrandingAttributes"
    ]
    """<p>The branding information configured for iOS devices.</p>"""
    device_type_linux: NotRequired[
        "capo_workspaces.types.default_client_branding_attributes.DefaultClientBrandingAttributes"
    ]
    """<p>The branding information configured for Linux devices.</p>"""
    device_type_web: NotRequired[
        "capo_workspaces.types.default_client_branding_attributes.DefaultClientBrandingAttributes"
    ]
    """<p>The branding information configured for web access.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: ImportClientBrandingResult) -> dict:
    out: dict = {}
    if "device_type_windows" in value:
        import capo_workspaces.types.default_client_branding_attributes

        out["DeviceTypeWindows"] = (
            capo_workspaces.types.default_client_branding_attributes.serialize_aws_json_1_1(
                value["device_type_windows"]
            )
        )
    if "device_type_osx" in value:
        import capo_workspaces.types.default_client_branding_attributes

        out["DeviceTypeOsx"] = (
            capo_workspaces.types.default_client_branding_attributes.serialize_aws_json_1_1(
                value["device_type_osx"]
            )
        )
    if "device_type_android" in value:
        import capo_workspaces.types.default_client_branding_attributes

        out["DeviceTypeAndroid"] = (
            capo_workspaces.types.default_client_branding_attributes.serialize_aws_json_1_1(
                value["device_type_android"]
            )
        )
    if "device_type_ios" in value:
        import capo_workspaces.types.ios_client_branding_attributes

        out["DeviceTypeIos"] = (
            capo_workspaces.types.ios_client_branding_attributes.serialize_aws_json_1_1(
                value["device_type_ios"]
            )
        )
    if "device_type_linux" in value:
        import capo_workspaces.types.default_client_branding_attributes

        out["DeviceTypeLinux"] = (
            capo_workspaces.types.default_client_branding_attributes.serialize_aws_json_1_1(
                value["device_type_linux"]
            )
        )
    if "device_type_web" in value:
        import capo_workspaces.types.default_client_branding_attributes

        out["DeviceTypeWeb"] = (
            capo_workspaces.types.default_client_branding_attributes.serialize_aws_json_1_1(
                value["device_type_web"]
            )
        )
    return out


def deserialize_aws_json_1_1(data: dict) -> ImportClientBrandingResult:
    out: ImportClientBrandingResult = {}  # type: ignore[typeddict-item]
    if data.get("DeviceTypeWindows") is not None:
        import capo_workspaces.types.default_client_branding_attributes

        out["device_type_windows"] = (
            capo_workspaces.types.default_client_branding_attributes.deserialize_aws_json_1_1(
                data["DeviceTypeWindows"]
            )
        )
    if data.get("DeviceTypeOsx") is not None:
        import capo_workspaces.types.default_client_branding_attributes

        out["device_type_osx"] = (
            capo_workspaces.types.default_client_branding_attributes.deserialize_aws_json_1_1(
                data["DeviceTypeOsx"]
            )
        )
    if data.get("DeviceTypeAndroid") is not None:
        import capo_workspaces.types.default_client_branding_attributes

        out["device_type_android"] = (
            capo_workspaces.types.default_client_branding_attributes.deserialize_aws_json_1_1(
                data["DeviceTypeAndroid"]
            )
        )
    if data.get("DeviceTypeIos") is not None:
        import capo_workspaces.types.ios_client_branding_attributes

        out["device_type_ios"] = (
            capo_workspaces.types.ios_client_branding_attributes.deserialize_aws_json_1_1(
                data["DeviceTypeIos"]
            )
        )
    if data.get("DeviceTypeLinux") is not None:
        import capo_workspaces.types.default_client_branding_attributes

        out["device_type_linux"] = (
            capo_workspaces.types.default_client_branding_attributes.deserialize_aws_json_1_1(
                data["DeviceTypeLinux"]
            )
        )
    if data.get("DeviceTypeWeb") is not None:
        import capo_workspaces.types.default_client_branding_attributes

        out["device_type_web"] = (
            capo_workspaces.types.default_client_branding_attributes.deserialize_aws_json_1_1(
                data["DeviceTypeWeb"]
            )
        )
    return out


# --- rpcv2Cbor ser/de ---
def serialize_cbor(value: ImportClientBrandingResult) -> dict:
    out: dict = {}
    if "device_type_windows" in value:
        import capo_workspaces.types.default_client_branding_attributes

        out["DeviceTypeWindows"] = (
            capo_workspaces.types.default_client_branding_attributes.serialize_cbor(
                value["device_type_windows"]
            )
        )
    if "device_type_osx" in value:
        import capo_workspaces.types.default_client_branding_attributes

        out["DeviceTypeOsx"] = (
            capo_workspaces.types.default_client_branding_attributes.serialize_cbor(
                value["device_type_osx"]
            )
        )
    if "device_type_android" in value:
        import capo_workspaces.types.default_client_branding_attributes

        out["DeviceTypeAndroid"] = (
            capo_workspaces.types.default_client_branding_attributes.serialize_cbor(
                value["device_type_android"]
            )
        )
    if "device_type_ios" in value:
        import capo_workspaces.types.ios_client_branding_attributes

        out["DeviceTypeIos"] = (
            capo_workspaces.types.ios_client_branding_attributes.serialize_cbor(
                value["device_type_ios"]
            )
        )
    if "device_type_linux" in value:
        import capo_workspaces.types.default_client_branding_attributes

        out["DeviceTypeLinux"] = (
            capo_workspaces.types.default_client_branding_attributes.serialize_cbor(
                value["device_type_linux"]
            )
        )
    if "device_type_web" in value:
        import capo_workspaces.types.default_client_branding_attributes

        out["DeviceTypeWeb"] = (
            capo_workspaces.types.default_client_branding_attributes.serialize_cbor(
                value["device_type_web"]
            )
        )
    return out


def deserialize_cbor(data: dict) -> ImportClientBrandingResult:
    out: ImportClientBrandingResult = {}  # type: ignore[typeddict-item]
    if data.get("DeviceTypeWindows") is not None:
        import capo_workspaces.types.default_client_branding_attributes

        out["device_type_windows"] = (
            capo_workspaces.types.default_client_branding_attributes.deserialize_cbor(
                data["DeviceTypeWindows"]
            )
        )
    if data.get("DeviceTypeOsx") is not None:
        import capo_workspaces.types.default_client_branding_attributes

        out["device_type_osx"] = (
            capo_workspaces.types.default_client_branding_attributes.deserialize_cbor(
                data["DeviceTypeOsx"]
            )
        )
    if data.get("DeviceTypeAndroid") is not None:
        import capo_workspaces.types.default_client_branding_attributes

        out["device_type_android"] = (
            capo_workspaces.types.default_client_branding_attributes.deserialize_cbor(
                data["DeviceTypeAndroid"]
            )
        )
    if data.get("DeviceTypeIos") is not None:
        import capo_workspaces.types.ios_client_branding_attributes

        out["device_type_ios"] = (
            capo_workspaces.types.ios_client_branding_attributes.deserialize_cbor(
                data["DeviceTypeIos"]
            )
        )
    if data.get("DeviceTypeLinux") is not None:
        import capo_workspaces.types.default_client_branding_attributes

        out["device_type_linux"] = (
            capo_workspaces.types.default_client_branding_attributes.deserialize_cbor(
                data["DeviceTypeLinux"]
            )
        )
    if data.get("DeviceTypeWeb") is not None:
        import capo_workspaces.types.default_client_branding_attributes

        out["device_type_web"] = (
            capo_workspaces.types.default_client_branding_attributes.deserialize_cbor(
                data["DeviceTypeWeb"]
            )
        )
    return out
