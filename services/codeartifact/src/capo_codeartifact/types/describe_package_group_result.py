"""Generated from Smithy shape ``com.amazonaws.codeartifact#DescribePackageGroupResult``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_codeartifact.types.package_group_description


class DescribePackageGroupResult(TypedDict, closed=True):
    package_group: NotRequired[
        "capo_codeartifact.types.package_group_description.PackageGroupDescription"
    ]
    """<p>A <a href="https://docs.aws.amazon.com/codeartifact/latest/APIReference/API_PackageGroupDescription.html">PackageGroupDescription</a> object that contains information about the requested package group.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: DescribePackageGroupResult) -> dict:
    out: dict = {}
    if "package_group" in value:
        import capo_codeartifact.types.package_group_description

        out["packageGroup"] = (
            capo_codeartifact.types.package_group_description.serialize_json(
                value["package_group"]
            )
        )
    return out


def deserialize_json(data: dict) -> DescribePackageGroupResult:
    out: DescribePackageGroupResult = {}  # type: ignore[typeddict-item]
    if data.get("packageGroup") is not None:
        import capo_codeartifact.types.package_group_description

        out["package_group"] = (
            capo_codeartifact.types.package_group_description.deserialize_json(
                data["packageGroup"]
            )
        )
    return out
