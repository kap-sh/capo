"""Generated from Smithy shape ``com.amazonaws.apprunner#SourceConfiguration``."""

from typing import TYPE_CHECKING, Any

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_apprunner.types.authentication_configuration
    import capo_apprunner.types.code_repository
    import capo_apprunner.types.image_repository
    import capo_apprunner.types.nullable_boolean


class SourceConfiguration(TypedDict, closed=True):
    code_repository: NotRequired["capo_apprunner.types.code_repository.CodeRepository"]
    """<p>The description of a source code repository.</p> <p>You must provide either this member or <code>ImageRepository</code> (but not both).</p>"""
    image_repository: NotRequired[
        "capo_apprunner.types.image_repository.ImageRepository"
    ]
    """<p>The description of a source image repository.</p> <p>You must provide either this member or <code>CodeRepository</code> (but not both).</p>"""
    auto_deployments_enabled: NotRequired[
        "capo_apprunner.types.nullable_boolean.NullableBoolean"
    ]
    """<p>If <code>true</code>, continuous integration from the source repository is enabled for the App Runner service. Each repository change (including any source code commit or new image version) starts a deployment.</p> <p>Default: App Runner sets to <code>false</code> for a source image that uses an ECR Public repository or an ECR repository that's in an Amazon Web Services account other than the one that the service is in. App Runner sets to <code>true</code> in all other cases (which currently include a source code repository or a source image using a same-account ECR repository).</p>"""
    authentication_configuration: NotRequired[
        "capo_apprunner.types.authentication_configuration.AuthenticationConfiguration"
    ]
    """<p>Describes the resources that are needed to authenticate access to some source repositories.</p>"""


# --- awsJson1_0 ser/de ---
def serialize_aws_json_1_0(value: SourceConfiguration) -> dict:
    out: dict = {}
    if "code_repository" in value:
        import capo_apprunner.types.code_repository

        out["CodeRepository"] = (
            capo_apprunner.types.code_repository.serialize_aws_json_1_0(
                value["code_repository"]
            )
        )
    if "image_repository" in value:
        import capo_apprunner.types.image_repository

        out["ImageRepository"] = (
            capo_apprunner.types.image_repository.serialize_aws_json_1_0(
                value["image_repository"]
            )
        )
    if "auto_deployments_enabled" in value:
        out["AutoDeploymentsEnabled"] = value["auto_deployments_enabled"]
    if "authentication_configuration" in value:
        import capo_apprunner.types.authentication_configuration

        out["AuthenticationConfiguration"] = (
            capo_apprunner.types.authentication_configuration.serialize_aws_json_1_0(
                value["authentication_configuration"]
            )
        )
    return out


def deserialize_aws_json_1_0(data: dict) -> SourceConfiguration:
    out: SourceConfiguration = {}  # type: ignore[typeddict-item]
    if data.get("CodeRepository") is not None:
        import capo_apprunner.types.code_repository

        out["code_repository"] = (
            capo_apprunner.types.code_repository.deserialize_aws_json_1_0(
                data["CodeRepository"]
            )
        )
    if data.get("ImageRepository") is not None:
        import capo_apprunner.types.image_repository

        out["image_repository"] = (
            capo_apprunner.types.image_repository.deserialize_aws_json_1_0(
                data["ImageRepository"]
            )
        )
    if data.get("AutoDeploymentsEnabled") is not None:
        out["auto_deployments_enabled"] = data["AutoDeploymentsEnabled"]
    if data.get("AuthenticationConfiguration") is not None:
        import capo_apprunner.types.authentication_configuration

        out["authentication_configuration"] = (
            capo_apprunner.types.authentication_configuration.deserialize_aws_json_1_0(
                data["AuthenticationConfiguration"]
            )
        )
    return out


def redact_sensitive(value: SourceConfiguration) -> dict[str, Any]:
    out: dict[str, Any] = dict(value)
    if "code_repository" in value:
        import capo_apprunner.types.code_repository

        out["code_repository"] = capo_apprunner.types.code_repository.redact_sensitive(
            value["code_repository"]
        )
    if "image_repository" in value:
        import capo_apprunner.types.image_repository

        out["image_repository"] = (
            capo_apprunner.types.image_repository.redact_sensitive(
                value["image_repository"]
            )
        )
    return out
