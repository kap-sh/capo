"""Generated from Smithy shape ``com.amazonaws.lakeformation#AnyResource``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_lakeformation.types.any_resource_supported_types
    import capo_lakeformation.types.catalog_id_string


class AnyResource(TypedDict, closed=True):
    catalog_id: NotRequired[
        "capo_lakeformation.types.catalog_id_string.CatalogIdString"
    ]
    """<p>The ID of the Data Catalog. By default, it's your account ID.</p>"""
    resource_type: "capo_lakeformation.types.any_resource_supported_types.AnyResourceSupportedTypes"
    """<p>The type of resource that the grant covers. The only supported value is <code>TABLE</code>.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: AnyResource) -> dict:
    out: dict = {}
    if "catalog_id" in value:
        out["CatalogId"] = value["catalog_id"]
    import capo_lakeformation.types.any_resource_supported_types

    out["ResourceType"] = (
        capo_lakeformation.types.any_resource_supported_types.serialize_json(
            value["resource_type"]
        )
    )
    return out


def deserialize_json(data: dict) -> AnyResource:
    out: AnyResource = {}  # type: ignore[typeddict-item]
    if data.get("CatalogId") is not None:
        out["catalog_id"] = data["CatalogId"]
    if data.get("ResourceType") is not None:
        import capo_lakeformation.types.any_resource_supported_types

        out["resource_type"] = (
            capo_lakeformation.types.any_resource_supported_types.deserialize_json(
                data["ResourceType"]
            )
        )
    else:
        import typing

        out["resource_type"] = typing.cast(
            "capo_lakeformation.types.any_resource_supported_types.AnyResourceSupportedTypes",
            "",
        )
    return out
