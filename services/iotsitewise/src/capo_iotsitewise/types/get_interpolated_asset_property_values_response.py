"""Generated from Smithy shape ``com.amazonaws.iotsitewise#GetInterpolatedAssetPropertyValuesResponse``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_iotsitewise.types.interpolated_asset_property_values
    import capo_iotsitewise.types.next_token


class GetInterpolatedAssetPropertyValuesResponse(TypedDict, closed=True):
    interpolated_asset_property_values: "capo_iotsitewise.types.interpolated_asset_property_values.InterpolatedAssetPropertyValues"
    """<p>The requested interpolated values.</p>"""
    next_token: NotRequired["capo_iotsitewise.types.next_token.NextToken"]
    """<p>The token for the next set of results, or null if there are no additional results.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: GetInterpolatedAssetPropertyValuesResponse) -> dict:
    out: dict = {}
    import capo_iotsitewise.types.interpolated_asset_property_values

    out["interpolatedAssetPropertyValues"] = (
        capo_iotsitewise.types.interpolated_asset_property_values.serialize_json(
            value["interpolated_asset_property_values"]
        )
    )
    if "next_token" in value:
        out["nextToken"] = value["next_token"]
    return out


def deserialize_json(data: dict) -> GetInterpolatedAssetPropertyValuesResponse:
    out: GetInterpolatedAssetPropertyValuesResponse = {}  # type: ignore[typeddict-item]
    if data.get("interpolatedAssetPropertyValues") is not None:
        import capo_iotsitewise.types.interpolated_asset_property_values

        out["interpolated_asset_property_values"] = (
            capo_iotsitewise.types.interpolated_asset_property_values.deserialize_json(
                data["interpolatedAssetPropertyValues"]
            )
        )
    else:
        out["interpolated_asset_property_values"] = []
    if data.get("nextToken") is not None:
        out["next_token"] = data["nextToken"]
    return out
