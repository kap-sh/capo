"""Generated from Smithy shape ``com.amazonaws.sagemaker#SpaceSettings``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_sagemaker.types.app_type
    import capo_sagemaker.types.custom_file_systems
    import capo_sagemaker.types.feature_status
    import capo_sagemaker.types.jupyter_server_app_settings
    import capo_sagemaker.types.kernel_gateway_app_settings
    import capo_sagemaker.types.space_code_editor_app_settings
    import capo_sagemaker.types.space_jupyter_lab_app_settings
    import capo_sagemaker.types.space_storage_settings


class SpaceSettings(TypedDict, closed=True):
    jupyter_server_app_settings: NotRequired[
        "capo_sagemaker.types.jupyter_server_app_settings.JupyterServerAppSettings"
    ]
    kernel_gateway_app_settings: NotRequired[
        "capo_sagemaker.types.kernel_gateway_app_settings.KernelGatewayAppSettings"
    ]
    code_editor_app_settings: NotRequired[
        "capo_sagemaker.types.space_code_editor_app_settings.SpaceCodeEditorAppSettings"
    ]
    """<p>The Code Editor application settings.</p>"""
    jupyter_lab_app_settings: NotRequired[
        "capo_sagemaker.types.space_jupyter_lab_app_settings.SpaceJupyterLabAppSettings"
    ]
    """<p>The settings for the JupyterLab application.</p>"""
    app_type: NotRequired["capo_sagemaker.types.app_type.AppType"]
    """<p>The type of app created within the space.</p> <p>If using the <a href="https://docs.aws.amazon.com/sagemaker/latest/APIReference/API_UpdateSpace.html"> UpdateSpace</a> API, you can't change the app type of your space by specifying a different value for this field.</p>"""
    space_storage_settings: NotRequired[
        "capo_sagemaker.types.space_storage_settings.SpaceStorageSettings"
    ]
    """<p>The storage settings for a space.</p>"""
    space_managed_resources: NotRequired[
        "capo_sagemaker.types.feature_status.FeatureStatus"
    ]
    """<p>If you enable this option, SageMaker AI creates the following resources on your behalf when you create the space:</p> <ul> <li> <p>The user profile that possesses the space.</p> </li> <li> <p>The app that the space contains.</p> </li> </ul>"""
    custom_file_systems: NotRequired[
        "capo_sagemaker.types.custom_file_systems.CustomFileSystems"
    ]
    """<p>A file system, created by you, that you assign to a space for an Amazon SageMaker AI Domain. Permitted users can access this file system in Amazon SageMaker AI Studio.</p>"""
    remote_access: NotRequired["capo_sagemaker.types.feature_status.FeatureStatus"]
    """<p>A setting that enables or disables remote access for a SageMaker space. When enabled, this allows you to connect to the remote space from your local IDE.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: SpaceSettings) -> dict:
    out: dict = {}
    if "jupyter_server_app_settings" in value:
        import capo_sagemaker.types.jupyter_server_app_settings

        out["JupyterServerAppSettings"] = (
            capo_sagemaker.types.jupyter_server_app_settings.serialize_aws_json_1_1(
                value["jupyter_server_app_settings"]
            )
        )
    if "kernel_gateway_app_settings" in value:
        import capo_sagemaker.types.kernel_gateway_app_settings

        out["KernelGatewayAppSettings"] = (
            capo_sagemaker.types.kernel_gateway_app_settings.serialize_aws_json_1_1(
                value["kernel_gateway_app_settings"]
            )
        )
    if "code_editor_app_settings" in value:
        import capo_sagemaker.types.space_code_editor_app_settings

        out["CodeEditorAppSettings"] = (
            capo_sagemaker.types.space_code_editor_app_settings.serialize_aws_json_1_1(
                value["code_editor_app_settings"]
            )
        )
    if "jupyter_lab_app_settings" in value:
        import capo_sagemaker.types.space_jupyter_lab_app_settings

        out["JupyterLabAppSettings"] = (
            capo_sagemaker.types.space_jupyter_lab_app_settings.serialize_aws_json_1_1(
                value["jupyter_lab_app_settings"]
            )
        )
    if "app_type" in value:
        import capo_sagemaker.types.app_type

        out["AppType"] = capo_sagemaker.types.app_type.serialize_aws_json_1_1(
            value["app_type"]
        )
    if "space_storage_settings" in value:
        import capo_sagemaker.types.space_storage_settings

        out["SpaceStorageSettings"] = (
            capo_sagemaker.types.space_storage_settings.serialize_aws_json_1_1(
                value["space_storage_settings"]
            )
        )
    if "space_managed_resources" in value:
        import capo_sagemaker.types.feature_status

        out["SpaceManagedResources"] = (
            capo_sagemaker.types.feature_status.serialize_aws_json_1_1(
                value["space_managed_resources"]
            )
        )
    if "custom_file_systems" in value:
        import capo_sagemaker.types.custom_file_systems

        out["CustomFileSystems"] = (
            capo_sagemaker.types.custom_file_systems.serialize_aws_json_1_1(
                value["custom_file_systems"]
            )
        )
    if "remote_access" in value:
        import capo_sagemaker.types.feature_status

        out["RemoteAccess"] = (
            capo_sagemaker.types.feature_status.serialize_aws_json_1_1(
                value["remote_access"]
            )
        )
    return out


def deserialize_aws_json_1_1(data: dict) -> SpaceSettings:
    out: SpaceSettings = {}  # type: ignore[typeddict-item]
    if data.get("JupyterServerAppSettings") is not None:
        import capo_sagemaker.types.jupyter_server_app_settings

        out["jupyter_server_app_settings"] = (
            capo_sagemaker.types.jupyter_server_app_settings.deserialize_aws_json_1_1(
                data["JupyterServerAppSettings"]
            )
        )
    if data.get("KernelGatewayAppSettings") is not None:
        import capo_sagemaker.types.kernel_gateway_app_settings

        out["kernel_gateway_app_settings"] = (
            capo_sagemaker.types.kernel_gateway_app_settings.deserialize_aws_json_1_1(
                data["KernelGatewayAppSettings"]
            )
        )
    if data.get("CodeEditorAppSettings") is not None:
        import capo_sagemaker.types.space_code_editor_app_settings

        out["code_editor_app_settings"] = (
            capo_sagemaker.types.space_code_editor_app_settings.deserialize_aws_json_1_1(
                data["CodeEditorAppSettings"]
            )
        )
    if data.get("JupyterLabAppSettings") is not None:
        import capo_sagemaker.types.space_jupyter_lab_app_settings

        out["jupyter_lab_app_settings"] = (
            capo_sagemaker.types.space_jupyter_lab_app_settings.deserialize_aws_json_1_1(
                data["JupyterLabAppSettings"]
            )
        )
    if data.get("AppType") is not None:
        import capo_sagemaker.types.app_type

        out["app_type"] = capo_sagemaker.types.app_type.deserialize_aws_json_1_1(
            data["AppType"]
        )
    if data.get("SpaceStorageSettings") is not None:
        import capo_sagemaker.types.space_storage_settings

        out["space_storage_settings"] = (
            capo_sagemaker.types.space_storage_settings.deserialize_aws_json_1_1(
                data["SpaceStorageSettings"]
            )
        )
    if data.get("SpaceManagedResources") is not None:
        import capo_sagemaker.types.feature_status

        out["space_managed_resources"] = (
            capo_sagemaker.types.feature_status.deserialize_aws_json_1_1(
                data["SpaceManagedResources"]
            )
        )
    if data.get("CustomFileSystems") is not None:
        import capo_sagemaker.types.custom_file_systems

        out["custom_file_systems"] = (
            capo_sagemaker.types.custom_file_systems.deserialize_aws_json_1_1(
                data["CustomFileSystems"]
            )
        )
    if data.get("RemoteAccess") is not None:
        import capo_sagemaker.types.feature_status

        out["remote_access"] = (
            capo_sagemaker.types.feature_status.deserialize_aws_json_1_1(
                data["RemoteAccess"]
            )
        )
    return out
