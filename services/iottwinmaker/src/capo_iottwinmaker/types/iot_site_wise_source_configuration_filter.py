"""Generated from Smithy shape ``com.amazonaws.iottwinmaker#IotSiteWiseSourceConfigurationFilter``."""

from typing import TYPE_CHECKING, TypeAlias

from typing_extensions import TypedDict

from capo_iottwinmaker.errors import DeserializationError, SerializationError
from capo_iottwinmaker.types._unknown import UnknownUnionMember

if TYPE_CHECKING:
    import capo_iottwinmaker.types.filter_by_asset
    import capo_iottwinmaker.types.filter_by_asset_model


class _IotSiteWiseSourceConfigurationFilter_filterByAssetModel(TypedDict, closed=True):
    filterByAssetModel: (
        "capo_iottwinmaker.types.filter_by_asset_model.FilterByAssetModel"
    )


class _IotSiteWiseSourceConfigurationFilter_filterByAsset(TypedDict, closed=True):
    filterByAsset: "capo_iottwinmaker.types.filter_by_asset.FilterByAsset"


IotSiteWiseSourceConfigurationFilter: TypeAlias = (
    _IotSiteWiseSourceConfigurationFilter_filterByAssetModel
    | _IotSiteWiseSourceConfigurationFilter_filterByAsset
    | UnknownUnionMember
)


# --- restJson1 ser/de ---
def serialize_json(value: IotSiteWiseSourceConfigurationFilter) -> dict:
    if "$unknown" in value:
        raise SerializationError(
            f"IotSiteWiseSourceConfigurationFilter: cannot serialize unknown variant {value['$unknown']['name']!r}"
        )
    elif "filterByAssetModel" in value:
        import capo_iottwinmaker.types.filter_by_asset_model

        return {
            "filterByAssetModel": capo_iottwinmaker.types.filter_by_asset_model.serialize_json(
                value["filterByAssetModel"]
            )
        }
    elif "filterByAsset" in value:
        import capo_iottwinmaker.types.filter_by_asset

        return {
            "filterByAsset": capo_iottwinmaker.types.filter_by_asset.serialize_json(
                value["filterByAsset"]
            )
        }
    else:
        raise SerializationError(
            "IotSiteWiseSourceConfigurationFilter: no variant present"
        )


def deserialize_json(data: dict) -> IotSiteWiseSourceConfigurationFilter:
    if data.get("filterByAssetModel") is not None:
        import capo_iottwinmaker.types.filter_by_asset_model

        return {
            "filterByAssetModel": capo_iottwinmaker.types.filter_by_asset_model.deserialize_json(
                data["filterByAssetModel"]
            )
        }
    elif data.get("filterByAsset") is not None:
        import capo_iottwinmaker.types.filter_by_asset

        return {
            "filterByAsset": capo_iottwinmaker.types.filter_by_asset.deserialize_json(
                data["filterByAsset"]
            )
        }
    else:
        name = next(
            (k for k, v in data.items() if v is not None and k != "__type"), None
        )
        if name is not None:
            return {"$unknown": {"name": name}}
        raise DeserializationError(
            "IotSiteWiseSourceConfigurationFilter: no recognized variant key"
        )
