"""Generated from Smithy shape ``com.amazonaws.codeartifact#PackageSummary``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_codeartifact.types.package_format
    import capo_codeartifact.types.package_name
    import capo_codeartifact.types.package_namespace
    import capo_codeartifact.types.package_origin_configuration


class PackageSummary(TypedDict, closed=True):
    format: NotRequired["capo_codeartifact.types.package_format.PackageFormat"]
    """<p> The format of the package. </p>"""
    namespace: NotRequired["capo_codeartifact.types.package_namespace.PackageNamespace"]
    """<p>The namespace of the package. The package component that specifies its namespace depends on its type. For example:</p> <ul> <li> <p> The namespace of a Maven package version is its <code>groupId</code>. </p> </li> <li> <p> The namespace of an npm or Swift package version is its <code>scope</code>. </p> </li> <li> <p>The namespace of a generic package is its <code>namespace</code>.</p> </li> <li> <p> Python, NuGet, Ruby, and Cargo package versions do not contain a corresponding component, package versions of those formats do not have a namespace. </p> </li> </ul>"""
    package: NotRequired["capo_codeartifact.types.package_name.PackageName"]
    """<p> The name of the package. </p>"""
    origin_configuration: NotRequired[
        "capo_codeartifact.types.package_origin_configuration.PackageOriginConfiguration"
    ]
    """<p>A <a href="https://docs.aws.amazon.com/codeartifact/latest/APIReference/API_PackageOriginConfiguration.html">PackageOriginConfiguration</a> object that contains a <a href="https://docs.aws.amazon.com/codeartifact/latest/APIReference/API_PackageOriginRestrictions.html">PackageOriginRestrictions</a> object that contains information about the upstream and publish package origin restrictions.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: PackageSummary) -> dict:
    out: dict = {}
    if "format" in value:
        import capo_codeartifact.types.package_format

        out["format"] = capo_codeartifact.types.package_format.serialize_json(
            value["format"]
        )
    if "namespace" in value:
        out["namespace"] = value["namespace"]
    if "package" in value:
        out["package"] = value["package"]
    if "origin_configuration" in value:
        import capo_codeartifact.types.package_origin_configuration

        out["originConfiguration"] = (
            capo_codeartifact.types.package_origin_configuration.serialize_json(
                value["origin_configuration"]
            )
        )
    return out


def deserialize_json(data: dict) -> PackageSummary:
    out: PackageSummary = {}  # type: ignore[typeddict-item]
    if data.get("format") is not None:
        import capo_codeartifact.types.package_format

        out["format"] = capo_codeartifact.types.package_format.deserialize_json(
            data["format"]
        )
    if data.get("namespace") is not None:
        out["namespace"] = data["namespace"]
    if data.get("package") is not None:
        out["package"] = data["package"]
    if data.get("originConfiguration") is not None:
        import capo_codeartifact.types.package_origin_configuration

        out["origin_configuration"] = (
            capo_codeartifact.types.package_origin_configuration.deserialize_json(
                data["originConfiguration"]
            )
        )
    return out
