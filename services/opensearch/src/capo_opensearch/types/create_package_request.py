"""Generated from Smithy shape ``com.amazonaws.opensearch#CreatePackageRequest``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

from capo_opensearch.errors import DeserializationError

if TYPE_CHECKING:
    import capo_opensearch.types.engine_version
    import capo_opensearch.types.package_configuration
    import capo_opensearch.types.package_description
    import capo_opensearch.types.package_encryption_options
    import capo_opensearch.types.package_name
    import capo_opensearch.types.package_source
    import capo_opensearch.types.package_type
    import capo_opensearch.types.package_vending_options


class CreatePackageRequest(TypedDict, closed=True):
    package_name: "capo_opensearch.types.package_name.PackageName"
    """<p>Unique name for the package.</p>"""
    package_type: "capo_opensearch.types.package_type.PackageType"
    """<p>The type of package.</p>"""
    package_description: NotRequired[
        "capo_opensearch.types.package_description.PackageDescription"
    ]
    """<p>Description of the package.</p>"""
    package_source: "capo_opensearch.types.package_source.PackageSource"
    """<p>The Amazon S3 location from which to import the package.</p>"""
    package_configuration: NotRequired[
        "capo_opensearch.types.package_configuration.PackageConfiguration"
    ]
    """<p> The configuration parameters for the package being created.</p>"""
    engine_version: NotRequired["capo_opensearch.types.engine_version.EngineVersion"]
    """<p>The version of the Amazon OpenSearch Service engine for which is compatible with the package. This can only be specified for package type <code>ZIP-PLUGIN</code> </p>"""
    package_vending_options: NotRequired[
        "capo_opensearch.types.package_vending_options.PackageVendingOptions"
    ]
    """<p> The vending options for the package being created. They determine if the package can be vended to other users.</p>"""
    package_encryption_options: NotRequired[
        "capo_opensearch.types.package_encryption_options.PackageEncryptionOptions"
    ]
    """<p>The encryption parameters for the package being created.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: CreatePackageRequest) -> dict:
    out: dict = {}
    out["PackageName"] = value["package_name"]
    import capo_opensearch.types.package_type

    out["PackageType"] = capo_opensearch.types.package_type.serialize_json(
        value["package_type"]
    )
    if "package_description" in value:
        out["PackageDescription"] = value["package_description"]
    import capo_opensearch.types.package_source

    out["PackageSource"] = capo_opensearch.types.package_source.serialize_json(
        value["package_source"]
    )
    if "package_configuration" in value:
        import capo_opensearch.types.package_configuration

        out["PackageConfiguration"] = (
            capo_opensearch.types.package_configuration.serialize_json(
                value["package_configuration"]
            )
        )
    if "engine_version" in value:
        out["EngineVersion"] = value["engine_version"]
    if "package_vending_options" in value:
        import capo_opensearch.types.package_vending_options

        out["PackageVendingOptions"] = (
            capo_opensearch.types.package_vending_options.serialize_json(
                value["package_vending_options"]
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


def deserialize_json(data: dict) -> CreatePackageRequest:
    out: CreatePackageRequest = {}  # type: ignore[typeddict-item]
    if data.get("PackageName") is not None:
        out["package_name"] = data["PackageName"]
    else:
        out["package_name"] = ""
    if data.get("PackageType") is not None:
        import capo_opensearch.types.package_type

        out["package_type"] = capo_opensearch.types.package_type.deserialize_json(
            data["PackageType"]
        )
    else:
        import typing

        out["package_type"] = typing.cast(
            "capo_opensearch.types.package_type.PackageType", ""
        )
    if data.get("PackageDescription") is not None:
        out["package_description"] = data["PackageDescription"]
    if data.get("PackageSource") is not None:
        import capo_opensearch.types.package_source

        out["package_source"] = capo_opensearch.types.package_source.deserialize_json(
            data["PackageSource"]
        )
    else:
        raise DeserializationError("CreatePackageRequest.package_source required")
    if data.get("PackageConfiguration") is not None:
        import capo_opensearch.types.package_configuration

        out["package_configuration"] = (
            capo_opensearch.types.package_configuration.deserialize_json(
                data["PackageConfiguration"]
            )
        )
    if data.get("EngineVersion") is not None:
        out["engine_version"] = data["EngineVersion"]
    if data.get("PackageVendingOptions") is not None:
        import capo_opensearch.types.package_vending_options

        out["package_vending_options"] = (
            capo_opensearch.types.package_vending_options.deserialize_json(
                data["PackageVendingOptions"]
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
