"""Generated from Smithy shape ``com.amazonaws.codeartifact#PackageVersionSummary``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

from capo_codeartifact.errors import DeserializationError

if TYPE_CHECKING:
    import capo_codeartifact.types.package_version
    import capo_codeartifact.types.package_version_origin
    import capo_codeartifact.types.package_version_revision
    import capo_codeartifact.types.package_version_status


class PackageVersionSummary(TypedDict, closed=True):
    version: "capo_codeartifact.types.package_version.PackageVersion"
    """<p> Information about a package version. </p>"""
    revision: NotRequired[
        "capo_codeartifact.types.package_version_revision.PackageVersionRevision"
    ]
    """<p> The revision associated with a package version. </p>"""
    status: "capo_codeartifact.types.package_version_status.PackageVersionStatus"
    """<p> A string that contains the status of the package version. It can be one of the following: </p>"""
    origin: NotRequired[
        "capo_codeartifact.types.package_version_origin.PackageVersionOrigin"
    ]
    """<p>A <a href="https://docs.aws.amazon.com/codeartifact/latest/APIReference/API_PackageVersionOrigin.html">PackageVersionOrigin</a> object that contains information about how the package version was added to the repository.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: PackageVersionSummary) -> dict:
    out: dict = {}
    out["version"] = value["version"]
    if "revision" in value:
        out["revision"] = value["revision"]
    import capo_codeartifact.types.package_version_status

    out["status"] = capo_codeartifact.types.package_version_status.serialize_json(
        value["status"]
    )
    if "origin" in value:
        import capo_codeartifact.types.package_version_origin

        out["origin"] = capo_codeartifact.types.package_version_origin.serialize_json(
            value["origin"]
        )
    return out


def deserialize_json(data: dict) -> PackageVersionSummary:
    out: PackageVersionSummary = {}  # type: ignore[typeddict-item]
    if data.get("version") is not None:
        out["version"] = data["version"]
    else:
        raise DeserializationError("PackageVersionSummary.version required")
    if data.get("revision") is not None:
        out["revision"] = data["revision"]
    if data.get("status") is not None:
        import capo_codeartifact.types.package_version_status

        out["status"] = capo_codeartifact.types.package_version_status.deserialize_json(
            data["status"]
        )
    else:
        raise DeserializationError("PackageVersionSummary.status required")
    if data.get("origin") is not None:
        import capo_codeartifact.types.package_version_origin

        out["origin"] = capo_codeartifact.types.package_version_origin.deserialize_json(
            data["origin"]
        )
    return out
