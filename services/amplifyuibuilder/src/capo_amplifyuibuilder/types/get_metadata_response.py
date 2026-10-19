"""Generated from Smithy shape ``com.amazonaws.amplifyuibuilder#GetMetadataResponse``."""

from typing import TYPE_CHECKING

from typing_extensions import TypedDict

if TYPE_CHECKING:
    import capo_amplifyuibuilder.types.features_map


class GetMetadataResponse(TypedDict, closed=True):
    features: "capo_amplifyuibuilder.types.features_map.FeaturesMap"
    """<p>Represents the configuration settings for the features metadata.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: GetMetadataResponse) -> dict:
    out: dict = {}
    import capo_amplifyuibuilder.types.features_map

    out["features"] = capo_amplifyuibuilder.types.features_map.serialize_json(
        value["features"]
    )
    return out


def deserialize_json(data: dict) -> GetMetadataResponse:
    out: GetMetadataResponse = {}  # type: ignore[typeddict-item]
    if data.get("features") is not None:
        import capo_amplifyuibuilder.types.features_map

        out["features"] = capo_amplifyuibuilder.types.features_map.deserialize_json(
            data["features"]
        )
    else:
        out["features"] = {}
    return out
