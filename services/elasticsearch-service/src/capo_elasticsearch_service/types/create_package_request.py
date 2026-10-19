"""Generated from Smithy shape ``com.amazonaws.elasticsearchservice#CreatePackageRequest``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

from capo_elasticsearch_service.errors import DeserializationError

if TYPE_CHECKING:
    import capo_elasticsearch_service.types.package_description
    import capo_elasticsearch_service.types.package_name
    import capo_elasticsearch_service.types.package_source
    import capo_elasticsearch_service.types.package_type


class CreatePackageRequest(TypedDict, closed=True):
    package_name: "capo_elasticsearch_service.types.package_name.PackageName"
    """<p>Unique identifier for the package.</p>"""
    package_type: "capo_elasticsearch_service.types.package_type.PackageType"
    """<p>Type of package. Currently supports only TXT-DICTIONARY.</p>"""
    package_description: NotRequired[
        "capo_elasticsearch_service.types.package_description.PackageDescription"
    ]
    """<p>Description of the package.</p>"""
    package_source: "capo_elasticsearch_service.types.package_source.PackageSource"
    """<p>The customer S3 location <code>PackageSource</code> for importing the package.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: CreatePackageRequest) -> dict:
    out: dict = {}
    out["PackageName"] = value["package_name"]
    import capo_elasticsearch_service.types.package_type

    out["PackageType"] = capo_elasticsearch_service.types.package_type.serialize_json(
        value["package_type"]
    )
    if "package_description" in value:
        out["PackageDescription"] = value["package_description"]
    import capo_elasticsearch_service.types.package_source

    out["PackageSource"] = (
        capo_elasticsearch_service.types.package_source.serialize_json(
            value["package_source"]
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
        import capo_elasticsearch_service.types.package_type

        out["package_type"] = (
            capo_elasticsearch_service.types.package_type.deserialize_json(
                data["PackageType"]
            )
        )
    else:
        import typing

        out["package_type"] = typing.cast(
            "capo_elasticsearch_service.types.package_type.PackageType", ""
        )
    if data.get("PackageDescription") is not None:
        out["package_description"] = data["PackageDescription"]
    if data.get("PackageSource") is not None:
        import capo_elasticsearch_service.types.package_source

        out["package_source"] = (
            capo_elasticsearch_service.types.package_source.deserialize_json(
                data["PackageSource"]
            )
        )
    else:
        raise DeserializationError("CreatePackageRequest.package_source required")
    return out
