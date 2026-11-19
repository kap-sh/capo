"""Generated from Smithy shape ``com.amazonaws.observabilityadmin#GetConnectorTelemetrySetupOutput``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_observabilityadmin.types.connector_provider
    import capo_observabilityadmin.types.permission_list
    import capo_observabilityadmin.types.setup_artifact_list
    import capo_observabilityadmin.types.setup_format


class GetConnectorTelemetrySetupOutput(TypedDict, closed=True):
    artifacts: "capo_observabilityadmin.types.setup_artifact_list.SetupArtifactList"
    """<p>The setup artifacts to apply in your cloud provider.</p>"""
    required_permissions_to_apply: NotRequired[
        "capo_observabilityadmin.types.permission_list.PermissionList"
    ]
    """<p>The permissions or roles in your cloud provider that you need to apply the artifacts, for example Azure Contributor and User Access Administrator.</p>"""
    format: "capo_observabilityadmin.types.setup_format.SetupFormat"
    """<p>The format of the setup artifacts.</p>"""
    provider: NotRequired[
        "capo_observabilityadmin.types.connector_provider.ConnectorProvider"
    ]
    """<p>The cloud provider that the setup artifacts are for.</p>"""
    manifest_version: NotRequired["int"]
    """<p>The version of the telemetry manifest that the service generated the setup artifacts from.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: GetConnectorTelemetrySetupOutput) -> dict:
    out: dict = {}
    import capo_observabilityadmin.types.setup_artifact_list

    out["Artifacts"] = capo_observabilityadmin.types.setup_artifact_list.serialize_json(
        value["artifacts"]
    )
    if "required_permissions_to_apply" in value:
        import capo_observabilityadmin.types.permission_list

        out["RequiredPermissionsToApply"] = (
            capo_observabilityadmin.types.permission_list.serialize_json(
                value["required_permissions_to_apply"]
            )
        )
    import capo_observabilityadmin.types.setup_format

    out["Format"] = capo_observabilityadmin.types.setup_format.serialize_json(
        value["format"]
    )
    if "provider" in value:
        import capo_observabilityadmin.types.connector_provider

        out["Provider"] = (
            capo_observabilityadmin.types.connector_provider.serialize_json(
                value["provider"]
            )
        )
    if "manifest_version" in value:
        out["ManifestVersion"] = value["manifest_version"]
    return out


def deserialize_json(data: dict) -> GetConnectorTelemetrySetupOutput:
    out: GetConnectorTelemetrySetupOutput = {}  # type: ignore[typeddict-item]
    if data.get("Artifacts") is not None:
        import capo_observabilityadmin.types.setup_artifact_list

        out["artifacts"] = (
            capo_observabilityadmin.types.setup_artifact_list.deserialize_json(
                data["Artifacts"]
            )
        )
    else:
        out["artifacts"] = []
    if data.get("RequiredPermissionsToApply") is not None:
        import capo_observabilityadmin.types.permission_list

        out["required_permissions_to_apply"] = (
            capo_observabilityadmin.types.permission_list.deserialize_json(
                data["RequiredPermissionsToApply"]
            )
        )
    if data.get("Format") is not None:
        import capo_observabilityadmin.types.setup_format

        out["format"] = capo_observabilityadmin.types.setup_format.deserialize_json(
            data["Format"]
        )
    else:
        import typing

        out["format"] = typing.cast(
            "capo_observabilityadmin.types.setup_format.SetupFormat", ""
        )
    if data.get("Provider") is not None:
        import capo_observabilityadmin.types.connector_provider

        out["provider"] = (
            capo_observabilityadmin.types.connector_provider.deserialize_json(
                data["Provider"]
            )
        )
    if data.get("ManifestVersion") is not None:
        out["manifest_version"] = data["ManifestVersion"]
    return out
