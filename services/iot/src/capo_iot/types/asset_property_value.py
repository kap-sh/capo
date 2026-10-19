"""Generated from Smithy shape ``com.amazonaws.iot#AssetPropertyValue``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

from capo_iot.errors import DeserializationError

if TYPE_CHECKING:
    import capo_iot.types.asset_property_quality
    import capo_iot.types.asset_property_timestamp
    import capo_iot.types.asset_property_variant


class AssetPropertyValue(TypedDict, closed=True):
    value: "capo_iot.types.asset_property_variant.AssetPropertyVariant"
    """<p>The value of the asset property.</p>"""
    timestamp: "capo_iot.types.asset_property_timestamp.AssetPropertyTimestamp"
    """<p>The asset property value timestamp.</p>"""
    quality: NotRequired["capo_iot.types.asset_property_quality.AssetPropertyQuality"]
    """<p>Optional. A string that describes the quality of the value. Accepts substitution templates. Must be <code>GOOD</code>, <code>BAD</code>, or <code>UNCERTAIN</code>.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: AssetPropertyValue) -> dict:
    out: dict = {}
    import capo_iot.types.asset_property_variant

    out["value"] = capo_iot.types.asset_property_variant.serialize_json(value["value"])
    import capo_iot.types.asset_property_timestamp

    out["timestamp"] = capo_iot.types.asset_property_timestamp.serialize_json(
        value["timestamp"]
    )
    if "quality" in value:
        out["quality"] = value["quality"]
    return out


def deserialize_json(data: dict) -> AssetPropertyValue:
    out: AssetPropertyValue = {}  # type: ignore[typeddict-item]
    if data.get("value") is not None:
        import capo_iot.types.asset_property_variant

        out["value"] = capo_iot.types.asset_property_variant.deserialize_json(
            data["value"]
        )
    else:
        import capo_iot.types._unknown

        out["value"] = capo_iot.types._unknown.UnknownUnionMember("")
    if data.get("timestamp") is not None:
        import capo_iot.types.asset_property_timestamp

        out["timestamp"] = capo_iot.types.asset_property_timestamp.deserialize_json(
            data["timestamp"]
        )
    else:
        raise DeserializationError("AssetPropertyValue.timestamp required")
    if data.get("quality") is not None:
        out["quality"] = data["quality"]
    return out
