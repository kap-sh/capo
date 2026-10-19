"""Generated from Smithy shape ``com.amazonaws.opensearch#UpdatePackageRequest``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

from capo_opensearch.errors import DeserializationError

if TYPE_CHECKING:
    import capo_opensearch.types.commit_message
    import capo_opensearch.types.package_configuration
    import capo_opensearch.types.package_description
    import capo_opensearch.types.package_encryption_options
    import capo_opensearch.types.package_id
    import capo_opensearch.types.package_source


class UpdatePackageRequest(TypedDict, closed=True):
    package_id: "capo_opensearch.types.package_id.PackageID"
    """<p>The unique identifier for the package.</p>"""
    package_source: "capo_opensearch.types.package_source.PackageSource"
    """<p>Amazon S3 bucket and key for the package.</p>"""
    package_description: NotRequired[
        "capo_opensearch.types.package_description.PackageDescription"
    ]
    """<p>A new description of the package.</p>"""
    commit_message: NotRequired["capo_opensearch.types.commit_message.CommitMessage"]
    """<p>Commit message for the updated file, which is shown as part of <code>GetPackageVersionHistoryResponse</code>.</p>"""
    package_configuration: NotRequired[
        "capo_opensearch.types.package_configuration.PackageConfiguration"
    ]
    """<p>The updated configuration details for a package.</p>"""
    package_encryption_options: NotRequired[
        "capo_opensearch.types.package_encryption_options.PackageEncryptionOptions"
    ]
    """<p>Encryption options for a package.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: UpdatePackageRequest) -> dict:
    out: dict = {}
    out["PackageID"] = value["package_id"]
    import capo_opensearch.types.package_source

    out["PackageSource"] = capo_opensearch.types.package_source.serialize_json(
        value["package_source"]
    )
    if "package_description" in value:
        out["PackageDescription"] = value["package_description"]
    if "commit_message" in value:
        out["CommitMessage"] = value["commit_message"]
    if "package_configuration" in value:
        import capo_opensearch.types.package_configuration

        out["PackageConfiguration"] = (
            capo_opensearch.types.package_configuration.serialize_json(
                value["package_configuration"]
            )
        )
    if "package_encryption_options" in value:
        import capo_opensearch.types.package_encryption_options

        out["PackageEncryptionOptions"] = (
            capo_opensearch.types.package_encryption_options.serialize_json(
                value["package_encryption_options"]
            )
        )
    return out


def deserialize_json(data: dict) -> UpdatePackageRequest:
    out: UpdatePackageRequest = {}  # type: ignore[typeddict-item]
    if data.get("PackageID") is not None:
        out["package_id"] = data["PackageID"]
    else:
        out["package_id"] = ""
    if data.get("PackageSource") is not None:
        import capo_opensearch.types.package_source

        out["package_source"] = capo_opensearch.types.package_source.deserialize_json(
            data["PackageSource"]
        )
    else:
        raise DeserializationError("UpdatePackageRequest.package_source required")
    if data.get("PackageDescription") is not None:
        out["package_description"] = data["PackageDescription"]
    if data.get("CommitMessage") is not None:
        out["commit_message"] = data["CommitMessage"]
    if data.get("PackageConfiguration") is not None:
        import capo_opensearch.types.package_configuration

        out["package_configuration"] = (
            capo_opensearch.types.package_configuration.deserialize_json(
                data["PackageConfiguration"]
            )
        )
    if data.get("PackageEncryptionOptions") is not None:
        import capo_opensearch.types.package_encryption_options

        out["package_encryption_options"] = (
            capo_opensearch.types.package_encryption_options.deserialize_json(
                data["PackageEncryptionOptions"]
            )
        )
    return out
