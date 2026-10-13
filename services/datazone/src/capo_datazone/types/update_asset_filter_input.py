"""Generated from Smithy shape ``com.amazonaws.datazone#UpdateAssetFilterInput``."""

from typing import TYPE_CHECKING, Any

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_datazone.types.asset_filter_configuration
    import capo_datazone.types.asset_id
    import capo_datazone.types.description
    import capo_datazone.types.domain_id
    import capo_datazone.types.filter_id


class UpdateAssetFilterInput(TypedDict, closed=True):
    domain_identifier: "capo_datazone.types.domain_id.DomainId"
    """<p>The ID of the domain where you want to update an asset filter.</p>"""
    asset_identifier: "capo_datazone.types.asset_id.AssetId"
    """<p>The ID of the data asset.</p>"""
    identifier: "capo_datazone.types.filter_id.FilterId"
    """<p>The ID of the asset filter.</p>"""
    name: NotRequired["str"]
    """<p>The name of the asset filter.</p>"""
    description: NotRequired["capo_datazone.types.description.Description"]
    """<p>The description of the asset filter.</p>"""
    configuration: NotRequired[
        "capo_datazone.types.asset_filter_configuration.AssetFilterConfiguration"
    ]
    """<p>The configuration of the asset filter.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: UpdateAssetFilterInput) -> dict:
    out: dict = {}
    if "name" in value:
        out["name"] = value["name"]
    if "description" in value:
        out["description"] = value["description"]
    if "configuration" in value:
        import capo_datazone.types.asset_filter_configuration

        out["configuration"] = (
            capo_datazone.types.asset_filter_configuration.serialize_json(
                value["configuration"]
            )
        )
    return out


def deserialize_json(data: dict) -> UpdateAssetFilterInput:
    out: UpdateAssetFilterInput = {}  # type: ignore[typeddict-item]
    if data.get("name") is not None:
        out["name"] = data["name"]
    if data.get("description") is not None:
        out["description"] = data["description"]
    if data.get("configuration") is not None:
        import capo_datazone.types.asset_filter_configuration

        out["configuration"] = (
            capo_datazone.types.asset_filter_configuration.deserialize_json(
                data["configuration"]
            )
        )
    return out


def redact_sensitive(value: UpdateAssetFilterInput) -> dict[str, Any]:
    out: dict[str, Any] = dict(value)
    if "description" in value:
        out["description"] = "*** Sensitive Data Redacted ***"
    return out
