"""Generated from Smithy shape ``com.amazonaws.iotsitewise#AssetStatus``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_iotsitewise.types.asset_state
    import capo_iotsitewise.types.error_details


class AssetStatus(TypedDict, closed=True):
    state: "capo_iotsitewise.types.asset_state.AssetState"
    """<p>The current status of the asset.</p>"""
    error: NotRequired["capo_iotsitewise.types.error_details.ErrorDetails"]
    """<p>Contains associated error information, if any.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: AssetStatus) -> dict:
    out: dict = {}
    import capo_iotsitewise.types.asset_state

    out["state"] = capo_iotsitewise.types.asset_state.serialize_json(value["state"])
    if "error" in value:
        import capo_iotsitewise.types.error_details

        out["error"] = capo_iotsitewise.types.error_details.serialize_json(
            value["error"]
        )
    return out


def deserialize_json(data: dict) -> AssetStatus:
    out: AssetStatus = {}  # type: ignore[typeddict-item]
    if data.get("state") is not None:
        import capo_iotsitewise.types.asset_state

        out["state"] = capo_iotsitewise.types.asset_state.deserialize_json(
            data["state"]
        )
    else:
        import typing

        out["state"] = typing.cast("capo_iotsitewise.types.asset_state.AssetState", "")
    if data.get("error") is not None:
        import capo_iotsitewise.types.error_details

        out["error"] = capo_iotsitewise.types.error_details.deserialize_json(
            data["error"]
        )
    return out
