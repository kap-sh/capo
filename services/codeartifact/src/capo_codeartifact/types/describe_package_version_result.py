"""Generated from Smithy shape ``com.amazonaws.codeartifact#DescribePackageVersionResult``."""

from typing import TYPE_CHECKING

from typing_extensions import TypedDict

from capo_codeartifact.errors import DeserializationError

if TYPE_CHECKING:
    import capo_codeartifact.types.package_version_description


class DescribePackageVersionResult(TypedDict, closed=True):
    package_version: (
        "capo_codeartifact.types.package_version_description.PackageVersionDescription"
    )
    """<p> A <a href="https://docs.aws.amazon.com/codeartifact/latest/APIReference/API_PackageVersionDescription.html">PackageVersionDescription</a> object that contains information about the requested package version. </p>"""


# --- restJson1 ser/de ---
def serialize_json(value: DescribePackageVersionResult) -> dict:
    out: dict = {}
    import capo_codeartifact.types.package_version_description

    out["packageVersion"] = (
        capo_codeartifact.types.package_version_description.serialize_json(
            value["package_version"]
        )
    )
    return out


def deserialize_json(data: dict) -> DescribePackageVersionResult:
    out: DescribePackageVersionResult = {}  # type: ignore[typeddict-item]
    if data.get("packageVersion") is not None:
        import capo_codeartifact.types.package_version_description

        out["package_version"] = (
            capo_codeartifact.types.package_version_description.deserialize_json(
                data["packageVersion"]
            )
        )
    else:
        raise DeserializationError(
            "DescribePackageVersionResult.package_version required"
        )
    return out
