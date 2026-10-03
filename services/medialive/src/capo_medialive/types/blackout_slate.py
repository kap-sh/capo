"""Generated from Smithy shape ``com.amazonaws.medialive#BlackoutSlate``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_medialive.types.__string_min34_max34
    import capo_medialive.types.blackout_slate_network_end_blackout
    import capo_medialive.types.blackout_slate_state
    import capo_medialive.types.input_location


class BlackoutSlate(TypedDict, closed=True):
    blackout_slate_image: NotRequired[
        "capo_medialive.types.input_location.InputLocation"
    ]
    """Blackout slate image to be used. Leave empty for solid black. Only bmp and png images are supported."""
    network_end_blackout: NotRequired[
        "capo_medialive.types.blackout_slate_network_end_blackout.BlackoutSlateNetworkEndBlackout"
    ]
    """Setting to enabled causes the encoder to blackout the video, audio, and captions, and raise the "Network Blackout Image" slate when an SCTE104/35 Network End Segmentation Descriptor is encountered. The blackout will be lifted when the Network Start Segmentation Descriptor is encountered. The Network End and Network Start descriptors must contain a network ID that matches the value entered in "Network ID"."""
    network_end_blackout_image: NotRequired[
        "capo_medialive.types.input_location.InputLocation"
    ]
    """Path to local file to use as Network End Blackout image. Image will be scaled to fill the entire output raster."""
    network_id: NotRequired[
        "capo_medialive.types.__string_min34_max34.__stringMin34Max34"
    ]
    """Provides Network ID that matches EIDR ID format (e.g., "10.XXXX/XXXX-XXXX-XXXX-XXXX-XXXX-C")."""
    state: NotRequired["capo_medialive.types.blackout_slate_state.BlackoutSlateState"]
    """When set to enabled, causes video, audio and captions to be blanked when indicated by program metadata."""


# --- restJson1 ser/de ---
def serialize_json(value: BlackoutSlate) -> dict:
    out: dict = {}
    if "blackout_slate_image" in value:
        import capo_medialive.types.input_location

        out["blackoutSlateImage"] = capo_medialive.types.input_location.serialize_json(
            value["blackout_slate_image"]
        )
    if "network_end_blackout" in value:
        import capo_medialive.types.blackout_slate_network_end_blackout

        out["networkEndBlackout"] = (
            capo_medialive.types.blackout_slate_network_end_blackout.serialize_json(
                value["network_end_blackout"]
            )
        )
    if "network_end_blackout_image" in value:
        import capo_medialive.types.input_location

        out["networkEndBlackoutImage"] = (
            capo_medialive.types.input_location.serialize_json(
                value["network_end_blackout_image"]
            )
        )
    if "network_id" in value:
        out["networkId"] = value["network_id"]
    if "state" in value:
        import capo_medialive.types.blackout_slate_state

        out["state"] = capo_medialive.types.blackout_slate_state.serialize_json(
            value["state"]
        )
    return out


def deserialize_json(data: dict) -> BlackoutSlate:
    out: BlackoutSlate = {}  # type: ignore[typeddict-item]
    if data.get("blackoutSlateImage") is not None:
        import capo_medialive.types.input_location

        out["blackout_slate_image"] = (
            capo_medialive.types.input_location.deserialize_json(
                data["blackoutSlateImage"]
            )
        )
    if data.get("networkEndBlackout") is not None:
        import capo_medialive.types.blackout_slate_network_end_blackout

        out["network_end_blackout"] = (
            capo_medialive.types.blackout_slate_network_end_blackout.deserialize_json(
                data["networkEndBlackout"]
            )
        )
    if data.get("networkEndBlackoutImage") is not None:
        import capo_medialive.types.input_location

        out["network_end_blackout_image"] = (
            capo_medialive.types.input_location.deserialize_json(
                data["networkEndBlackoutImage"]
            )
        )
    if data.get("networkId") is not None:
        out["network_id"] = data["networkId"]
    if data.get("state") is not None:
        import capo_medialive.types.blackout_slate_state

        out["state"] = capo_medialive.types.blackout_slate_state.deserialize_json(
            data["state"]
        )
    return out
