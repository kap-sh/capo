"""Generated from Smithy shape ``com.amazonaws.apprunner#CodeRepository``."""

from typing import TYPE_CHECKING, Any

from typing_extensions import NotRequired, TypedDict

from capo_apprunner.errors import DeserializationError

if TYPE_CHECKING:
    import capo_apprunner.types.code_configuration
    import capo_apprunner.types.source_code_version
    import capo_apprunner.types.source_directory
    import capo_apprunner.types.string


class CodeRepository(TypedDict, closed=True):
    repository_url: "capo_apprunner.types.string.String"
    """<p>The location of the repository that contains the source code.</p>"""
    source_code_version: "capo_apprunner.types.source_code_version.SourceCodeVersion"
    """<p>The version that should be used within the source code repository.</p>"""
    code_configuration: NotRequired[
        "capo_apprunner.types.code_configuration.CodeConfiguration"
    ]
    """<p>Configuration for building and running the service from a source code repository.</p> <note> <p> <code>CodeConfiguration</code> is required only for <code>CreateService</code> request.</p> </note>"""
    source_directory: NotRequired[
        "capo_apprunner.types.source_directory.SourceDirectory"
    ]
    """<p>The path of the directory that stores source code and configuration files. The build and start commands also execute from here. The path is absolute from root and, if not specified, defaults to the repository root.</p>"""


# --- awsJson1_0 ser/de ---
def serialize_aws_json_1_0(value: CodeRepository) -> dict:
    out: dict = {}
    out["RepositoryUrl"] = value["repository_url"]
    import capo_apprunner.types.source_code_version

    out["SourceCodeVersion"] = (
        capo_apprunner.types.source_code_version.serialize_aws_json_1_0(
            value["source_code_version"]
        )
    )
    if "code_configuration" in value:
        import capo_apprunner.types.code_configuration

        out["CodeConfiguration"] = (
            capo_apprunner.types.code_configuration.serialize_aws_json_1_0(
                value["code_configuration"]
            )
        )
    if "source_directory" in value:
        out["SourceDirectory"] = value["source_directory"]
    return out


def deserialize_aws_json_1_0(data: dict) -> CodeRepository:
    out: CodeRepository = {}  # type: ignore[typeddict-item]
    if data.get("RepositoryUrl") is not None:
        out["repository_url"] = data["RepositoryUrl"]
    else:
        out["repository_url"] = ""
    if data.get("SourceCodeVersion") is not None:
        import capo_apprunner.types.source_code_version

        out["source_code_version"] = (
            capo_apprunner.types.source_code_version.deserialize_aws_json_1_0(
                data["SourceCodeVersion"]
            )
        )
    else:
        raise DeserializationError("CodeRepository.source_code_version required")
    if data.get("CodeConfiguration") is not None:
        import capo_apprunner.types.code_configuration

        out["code_configuration"] = (
            capo_apprunner.types.code_configuration.deserialize_aws_json_1_0(
                data["CodeConfiguration"]
            )
        )
    if data.get("SourceDirectory") is not None:
        out["source_directory"] = data["SourceDirectory"]
    return out


def redact_sensitive(value: CodeRepository) -> dict[str, Any]:
    out: dict[str, Any] = dict(value)
    if "code_configuration" in value:
        import capo_apprunner.types.code_configuration

        out["code_configuration"] = (
            capo_apprunner.types.code_configuration.redact_sensitive(
                value["code_configuration"]
            )
        )
    return out
