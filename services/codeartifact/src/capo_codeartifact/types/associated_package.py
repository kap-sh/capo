"""Generated from Smithy shape ``com.amazonaws.codeartifact#AssociatedPackage``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_codeartifact.types.package_format
    import capo_codeartifact.types.package_group_association_type
    import capo_codeartifact.types.package_name
    import capo_codeartifact.types.package_namespace


class AssociatedPackage(TypedDict, closed=True):
    format: NotRequired["capo_codeartifact.types.package_format.PackageFormat"]
    """<p>A format that specifies the type of the associated package.</p>"""
    namespace: NotRequired["capo_codeartifact.types.package_namespace.PackageNamespace"]
    """<p>The namespace of the associated package. The package component that specifies its namespace depends on its type. For example:</p> <ul> <li> <p> The namespace of a Maven package version is its <code>groupId</code>. </p> </li> <li> <p> The namespace of an npm or Swift package version is its <code>scope</code>. </p> </li> <li> <p>The namespace of a generic package is its <code>namespace</code>.</p> </li> <li> <p> Python, NuGet, Ruby, and Cargo package versions do not contain a corresponding component, package versions of those formats do not have a namespace. </p> </li> </ul>"""
    package: NotRequired["capo_codeartifact.types.package_name.PackageName"]
    """<p> The name of the associated package. </p>"""
    association_type: NotRequired[
        "capo_codeartifact.types.package_group_association_type.PackageGroupAssociationType"
    ]
    """<p>Describes the strength of the association between the package and package group. A strong match can be thought of as an exact match, and a weak match can be thought of as a variation match, for example, the package name matches a variation of the package group pattern. For more information about package group pattern matching, including strong and weak matches, see <a href="https://docs.aws.amazon.com/codeartifact/latest/ug/package-group-definition-syntax-matching-behavior.html">Package group definition syntax and matching behavior</a> in the <i>CodeArtifact User Guide</i>.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: AssociatedPackage) -> dict:
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
    if "association_type" in value:
        import capo_codeartifact.types.package_group_association_type

        out["associationType"] = (
            capo_codeartifact.types.package_group_association_type.serialize_json(
                value["association_type"]
            )
        )
    return out


def deserialize_json(data: dict) -> AssociatedPackage:
    out: AssociatedPackage = {}  # type: ignore[typeddict-item]
    if data.get("format") is not None:
        import capo_codeartifact.types.package_format

        out["format"] = capo_codeartifact.types.package_format.deserialize_json(
            data["format"]
        )
    if data.get("namespace") is not None:
        out["namespace"] = data["namespace"]
    if data.get("package") is not None:
        out["package"] = data["package"]
    if data.get("associationType") is not None:
        import capo_codeartifact.types.package_group_association_type

        out["association_type"] = (
            capo_codeartifact.types.package_group_association_type.deserialize_json(
                data["associationType"]
            )
        )
    return out
