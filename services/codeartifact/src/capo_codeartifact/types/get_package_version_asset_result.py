"""Generated from Smithy shape ``com.amazonaws.codeartifact#GetPackageVersionAssetResult``."""

from typing import TYPE_CHECKING, Any

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_codeartifact.types.asset
    import capo_codeartifact.types.asset_name
    import capo_codeartifact.types.package_version
    import capo_codeartifact.types.package_version_revision


class GetPackageVersionAssetResult(TypedDict, closed=True):
    asset: "capo_codeartifact.types.asset.Asset"
    """<p> The binary file, or asset, that is downloaded.</p>"""
    asset_name: NotRequired["capo_codeartifact.types.asset_name.AssetName"]
    """<p> The name of the asset that is downloaded. </p>"""
    package_version: NotRequired[
        "capo_codeartifact.types.package_version.PackageVersion"
    ]
    """<p> A string that contains the package version (for example, <code>3.5.2</code>). </p>"""
    package_version_revision: NotRequired[
        "capo_codeartifact.types.package_version_revision.PackageVersionRevision"
    ]
    """<p> The name of the package version revision that contains the downloaded asset. </p>"""


def redact_sensitive(value: GetPackageVersionAssetResult) -> dict[str, Any]:
    out: dict[str, Any] = dict(value)
    if "asset" in value:
        out["asset"] = "*** Streaming Data Redacted ***"
    return out
