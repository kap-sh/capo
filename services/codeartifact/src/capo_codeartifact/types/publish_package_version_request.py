"""Generated from Smithy shape ``com.amazonaws.codeartifact#PublishPackageVersionRequest``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_codeartifact.types.account_id
    import capo_codeartifact.types.asset
    import capo_codeartifact.types.asset_name
    import capo_codeartifact.types.boolean_optional
    import capo_codeartifact.types.domain_name
    import capo_codeartifact.types.package_format
    import capo_codeartifact.types.package_name
    import capo_codeartifact.types.package_namespace
    import capo_codeartifact.types.package_version
    import capo_codeartifact.types.repository_name
    import capo_codeartifact.types.sha256


class PublishPackageVersionRequest(TypedDict, closed=True):
    domain: "capo_codeartifact.types.domain_name.DomainName"
    """<p>The name of the domain that contains the repository that contains the package version to publish.</p>"""
    domain_owner: NotRequired["capo_codeartifact.types.account_id.AccountId"]
    """<p>The 12-digit account number of the AWS account that owns the domain. It does not include dashes or spaces.</p>"""
    repository: "capo_codeartifact.types.repository_name.RepositoryName"
    """<p>The name of the repository that the package version will be published to.</p>"""
    format: "capo_codeartifact.types.package_format.PackageFormat"
    """<p>A format that specifies the type of the package version with the requested asset file.</p> <p>The only supported value is <code>generic</code>.</p>"""
    namespace: NotRequired["capo_codeartifact.types.package_namespace.PackageNamespace"]
    """<p>The namespace of the package version to publish.</p>"""
    package: "capo_codeartifact.types.package_name.PackageName"
    """<p>The name of the package version to publish.</p>"""
    package_version: "capo_codeartifact.types.package_version.PackageVersion"
    """<p>The package version to publish (for example, <code>3.5.2</code>).</p>"""
    asset_content: "capo_codeartifact.types.asset.Asset"
    """<p>The content of the asset to publish.</p>"""
    asset_name: "capo_codeartifact.types.asset_name.AssetName"
    """<p>The name of the asset to publish. Asset names can include Unicode letters and numbers, and the following special characters: <code>~ ! @ ^ & ( ) - ` _ + [ ] { } ; , . `</code> </p>"""
    asset_sha256: "capo_codeartifact.types.sha256.SHA256"
    """<p>The SHA256 hash of the <code>assetContent</code> to publish. This value must be calculated by the caller and provided with the request (see <a href="https://docs.aws.amazon.com/codeartifact/latest/ug/using-generic.html#publishing-generic-packages">Publishing a generic package</a> in the <i>CodeArtifact User Guide</i>).</p> <p>This value is used as an integrity check to verify that the <code>assetContent</code> has not changed after it was originally sent.</p>"""
    unfinished: NotRequired["capo_codeartifact.types.boolean_optional.BooleanOptional"]
    """<p>Specifies whether the package version should remain in the <code>unfinished</code> state. If omitted, the package version status will be set to <code>Published</code> (see <a href="https://docs.aws.amazon.com/codeartifact/latest/ug/packages-overview.html#package-version-status">Package version status</a> in the <i>CodeArtifact User Guide</i>).</p> <p>Valid values: <code>unfinished</code> </p>"""
