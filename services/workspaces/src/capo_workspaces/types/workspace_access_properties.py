"""Generated from Smithy shape ``com.amazonaws.workspaces#WorkspaceAccessProperties``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_workspaces.types.access_endpoint_config
    import capo_workspaces.types.access_property_value


class WorkspaceAccessProperties(TypedDict, closed=True):
    device_type_windows: NotRequired[
        "capo_workspaces.types.access_property_value.AccessPropertyValue"
    ]
    """<p>Indicates whether users can use Windows clients to access their WorkSpaces.</p>"""
    device_type_osx: NotRequired[
        "capo_workspaces.types.access_property_value.AccessPropertyValue"
    ]
    """<p>Indicates whether users can use macOS clients to access their WorkSpaces.</p>"""
    device_type_web: NotRequired[
        "capo_workspaces.types.access_property_value.AccessPropertyValue"
    ]
    """<p>Indicates whether users can access their WorkSpaces through a web browser.</p>"""
    device_type_ios: NotRequired[
        "capo_workspaces.types.access_property_value.AccessPropertyValue"
    ]
    """<p>Indicates whether users can use iOS devices to access their WorkSpaces.</p>"""
    device_type_android: NotRequired[
        "capo_workspaces.types.access_property_value.AccessPropertyValue"
    ]
    """<p>Indicates whether users can use Android and Android-compatible Chrome OS devices to access their WorkSpaces.</p>"""
    device_type_chrome_os: NotRequired[
        "capo_workspaces.types.access_property_value.AccessPropertyValue"
    ]
    """<p>Indicates whether users can use Chromebooks to access their WorkSpaces.</p>"""
    device_type_zero_client: NotRequired[
        "capo_workspaces.types.access_property_value.AccessPropertyValue"
    ]
    """<p>Indicates whether users can use zero client devices to access their WorkSpaces.</p>"""
    device_type_linux: NotRequired[
        "capo_workspaces.types.access_property_value.AccessPropertyValue"
    ]
    """<p>Indicates whether users can use Linux clients to access their WorkSpaces.</p>"""
    device_type_work_spaces_thin_client: NotRequired[
        "capo_workspaces.types.access_property_value.AccessPropertyValue"
    ]
    """<p>Indicates whether users can access their WorkSpaces through a WorkSpaces Thin Client.</p>"""
    access_endpoint_config: NotRequired[
        "capo_workspaces.types.access_endpoint_config.AccessEndpointConfig"
    ]
    """<p>Specifies the configuration for accessing the WorkSpace.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: WorkspaceAccessProperties) -> dict:
    out: dict = {}
    if "device_type_windows" in value:
        import capo_workspaces.types.access_property_value

        out["DeviceTypeWindows"] = (
            capo_workspaces.types.access_property_value.serialize_aws_json_1_1(
                value["device_type_windows"]
            )
        )
    if "device_type_osx" in value:
        import capo_workspaces.types.access_property_value

        out["DeviceTypeOsx"] = (
            capo_workspaces.types.access_property_value.serialize_aws_json_1_1(
                value["device_type_osx"]
            )
        )
    if "device_type_web" in value:
        import capo_workspaces.types.access_property_value

        out["DeviceTypeWeb"] = (
            capo_workspaces.types.access_property_value.serialize_aws_json_1_1(
                value["device_type_web"]
            )
        )
    if "device_type_ios" in value:
        import capo_workspaces.types.access_property_value

        out["DeviceTypeIos"] = (
            capo_workspaces.types.access_property_value.serialize_aws_json_1_1(
                value["device_type_ios"]
            )
        )
    if "device_type_android" in value:
        import capo_workspaces.types.access_property_value

        out["DeviceTypeAndroid"] = (
            capo_workspaces.types.access_property_value.serialize_aws_json_1_1(
                value["device_type_android"]
            )
        )
    if "device_type_chrome_os" in value:
        import capo_workspaces.types.access_property_value

        out["DeviceTypeChromeOs"] = (
            capo_workspaces.types.access_property_value.serialize_aws_json_1_1(
                value["device_type_chrome_os"]
            )
        )
    if "device_type_zero_client" in value:
        import capo_workspaces.types.access_property_value

        out["DeviceTypeZeroClient"] = (
            capo_workspaces.types.access_property_value.serialize_aws_json_1_1(
                value["device_type_zero_client"]
            )
        )
    if "device_type_linux" in value:
        import capo_workspaces.types.access_property_value

        out["DeviceTypeLinux"] = (
            capo_workspaces.types.access_property_value.serialize_aws_json_1_1(
                value["device_type_linux"]
            )
        )
    if "device_type_work_spaces_thin_client" in value:
        import capo_workspaces.types.access_property_value

        out["DeviceTypeWorkSpacesThinClient"] = (
            capo_workspaces.types.access_property_value.serialize_aws_json_1_1(
                value["device_type_work_spaces_thin_client"]
            )
        )
    if "access_endpoint_config" in value:
        import capo_workspaces.types.access_endpoint_config

        out["AccessEndpointConfig"] = (
            capo_workspaces.types.access_endpoint_config.serialize_aws_json_1_1(
                value["access_endpoint_config"]
            )
        )
    return out


def deserialize_aws_json_1_1(data: dict) -> WorkspaceAccessProperties:
    out: WorkspaceAccessProperties = {}  # type: ignore[typeddict-item]
    if data.get("DeviceTypeWindows") is not None:
        import capo_workspaces.types.access_property_value

        out["device_type_windows"] = (
            capo_workspaces.types.access_property_value.deserialize_aws_json_1_1(
                data["DeviceTypeWindows"]
            )
        )
    if data.get("DeviceTypeOsx") is not None:
        import capo_workspaces.types.access_property_value

        out["device_type_osx"] = (
            capo_workspaces.types.access_property_value.deserialize_aws_json_1_1(
                data["DeviceTypeOsx"]
            )
        )
    if data.get("DeviceTypeWeb") is not None:
        import capo_workspaces.types.access_property_value

        out["device_type_web"] = (
            capo_workspaces.types.access_property_value.deserialize_aws_json_1_1(
                data["DeviceTypeWeb"]
            )
        )
    if data.get("DeviceTypeIos") is not None:
        import capo_workspaces.types.access_property_value

        out["device_type_ios"] = (
            capo_workspaces.types.access_property_value.deserialize_aws_json_1_1(
                data["DeviceTypeIos"]
            )
        )
    if data.get("DeviceTypeAndroid") is not None:
        import capo_workspaces.types.access_property_value

        out["device_type_android"] = (
            capo_workspaces.types.access_property_value.deserialize_aws_json_1_1(
                data["DeviceTypeAndroid"]
            )
        )
    if data.get("DeviceTypeChromeOs") is not None:
        import capo_workspaces.types.access_property_value

        out["device_type_chrome_os"] = (
            capo_workspaces.types.access_property_value.deserialize_aws_json_1_1(
                data["DeviceTypeChromeOs"]
            )
        )
    if data.get("DeviceTypeZeroClient") is not None:
        import capo_workspaces.types.access_property_value

        out["device_type_zero_client"] = (
            capo_workspaces.types.access_property_value.deserialize_aws_json_1_1(
                data["DeviceTypeZeroClient"]
            )
        )
    if data.get("DeviceTypeLinux") is not None:
        import capo_workspaces.types.access_property_value

        out["device_type_linux"] = (
            capo_workspaces.types.access_property_value.deserialize_aws_json_1_1(
                data["DeviceTypeLinux"]
            )
        )
    if data.get("DeviceTypeWorkSpacesThinClient") is not None:
        import capo_workspaces.types.access_property_value

        out["device_type_work_spaces_thin_client"] = (
            capo_workspaces.types.access_property_value.deserialize_aws_json_1_1(
                data["DeviceTypeWorkSpacesThinClient"]
            )
        )
    if data.get("AccessEndpointConfig") is not None:
        import capo_workspaces.types.access_endpoint_config

        out["access_endpoint_config"] = (
            capo_workspaces.types.access_endpoint_config.deserialize_aws_json_1_1(
                data["AccessEndpointConfig"]
            )
        )
    return out


# --- rpcv2Cbor ser/de ---
def serialize_cbor(value: WorkspaceAccessProperties) -> dict:
    out: dict = {}
    if "device_type_windows" in value:
        import capo_workspaces.types.access_property_value

        out["DeviceTypeWindows"] = (
            capo_workspaces.types.access_property_value.serialize_cbor(
                value["device_type_windows"]
            )
        )
    if "device_type_osx" in value:
        import capo_workspaces.types.access_property_value

        out["DeviceTypeOsx"] = (
            capo_workspaces.types.access_property_value.serialize_cbor(
                value["device_type_osx"]
            )
        )
    if "device_type_web" in value:
        import capo_workspaces.types.access_property_value

        out["DeviceTypeWeb"] = (
            capo_workspaces.types.access_property_value.serialize_cbor(
                value["device_type_web"]
            )
        )
    if "device_type_ios" in value:
        import capo_workspaces.types.access_property_value

        out["DeviceTypeIos"] = (
            capo_workspaces.types.access_property_value.serialize_cbor(
                value["device_type_ios"]
            )
        )
    if "device_type_android" in value:
        import capo_workspaces.types.access_property_value

        out["DeviceTypeAndroid"] = (
            capo_workspaces.types.access_property_value.serialize_cbor(
                value["device_type_android"]
            )
        )
    if "device_type_chrome_os" in value:
        import capo_workspaces.types.access_property_value

        out["DeviceTypeChromeOs"] = (
            capo_workspaces.types.access_property_value.serialize_cbor(
                value["device_type_chrome_os"]
            )
        )
    if "device_type_zero_client" in value:
        import capo_workspaces.types.access_property_value

        out["DeviceTypeZeroClient"] = (
            capo_workspaces.types.access_property_value.serialize_cbor(
                value["device_type_zero_client"]
            )
        )
    if "device_type_linux" in value:
        import capo_workspaces.types.access_property_value

        out["DeviceTypeLinux"] = (
            capo_workspaces.types.access_property_value.serialize_cbor(
                value["device_type_linux"]
            )
        )
    if "device_type_work_spaces_thin_client" in value:
        import capo_workspaces.types.access_property_value

        out["DeviceTypeWorkSpacesThinClient"] = (
            capo_workspaces.types.access_property_value.serialize_cbor(
                value["device_type_work_spaces_thin_client"]
            )
        )
    if "access_endpoint_config" in value:
        import capo_workspaces.types.access_endpoint_config

        out["AccessEndpointConfig"] = (
            capo_workspaces.types.access_endpoint_config.serialize_cbor(
                value["access_endpoint_config"]
            )
        )
    return out


def deserialize_cbor(data: dict) -> WorkspaceAccessProperties:
    out: WorkspaceAccessProperties = {}  # type: ignore[typeddict-item]
    if data.get("DeviceTypeWindows") is not None:
        import capo_workspaces.types.access_property_value

        out["device_type_windows"] = (
            capo_workspaces.types.access_property_value.deserialize_cbor(
                data["DeviceTypeWindows"]
            )
        )
    if data.get("DeviceTypeOsx") is not None:
        import capo_workspaces.types.access_property_value

        out["device_type_osx"] = (
            capo_workspaces.types.access_property_value.deserialize_cbor(
                data["DeviceTypeOsx"]
            )
        )
    if data.get("DeviceTypeWeb") is not None:
        import capo_workspaces.types.access_property_value

        out["device_type_web"] = (
            capo_workspaces.types.access_property_value.deserialize_cbor(
                data["DeviceTypeWeb"]
            )
        )
    if data.get("DeviceTypeIos") is not None:
        import capo_workspaces.types.access_property_value

        out["device_type_ios"] = (
            capo_workspaces.types.access_property_value.deserialize_cbor(
                data["DeviceTypeIos"]
            )
        )
    if data.get("DeviceTypeAndroid") is not None:
        import capo_workspaces.types.access_property_value

        out["device_type_android"] = (
            capo_workspaces.types.access_property_value.deserialize_cbor(
                data["DeviceTypeAndroid"]
            )
        )
    if data.get("DeviceTypeChromeOs") is not None:
        import capo_workspaces.types.access_property_value

        out["device_type_chrome_os"] = (
            capo_workspaces.types.access_property_value.deserialize_cbor(
                data["DeviceTypeChromeOs"]
            )
        )
    if data.get("DeviceTypeZeroClient") is not None:
        import capo_workspaces.types.access_property_value

        out["device_type_zero_client"] = (
            capo_workspaces.types.access_property_value.deserialize_cbor(
                data["DeviceTypeZeroClient"]
            )
        )
    if data.get("DeviceTypeLinux") is not None:
        import capo_workspaces.types.access_property_value

        out["device_type_linux"] = (
            capo_workspaces.types.access_property_value.deserialize_cbor(
                data["DeviceTypeLinux"]
            )
        )
    if data.get("DeviceTypeWorkSpacesThinClient") is not None:
        import capo_workspaces.types.access_property_value

        out["device_type_work_spaces_thin_client"] = (
            capo_workspaces.types.access_property_value.deserialize_cbor(
                data["DeviceTypeWorkSpacesThinClient"]
            )
        )
    if data.get("AccessEndpointConfig") is not None:
        import capo_workspaces.types.access_endpoint_config

        out["access_endpoint_config"] = (
            capo_workspaces.types.access_endpoint_config.deserialize_cbor(
                data["AccessEndpointConfig"]
            )
        )
    return out
