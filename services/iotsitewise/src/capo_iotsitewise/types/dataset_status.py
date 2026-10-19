"""Generated from Smithy shape ``com.amazonaws.iotsitewise#DatasetStatus``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_iotsitewise.types.dataset_state
    import capo_iotsitewise.types.error_details


class DatasetStatus(TypedDict, closed=True):
    state: "capo_iotsitewise.types.dataset_state.DatasetState"
    """<p>The current status of the dataset.</p>"""
    error: NotRequired["capo_iotsitewise.types.error_details.ErrorDetails"]


# --- restJson1 ser/de ---
def serialize_json(value: DatasetStatus) -> dict:
    out: dict = {}
    import capo_iotsitewise.types.dataset_state

    out["state"] = capo_iotsitewise.types.dataset_state.serialize_json(value["state"])
    if "error" in value:
        import capo_iotsitewise.types.error_details

        out["error"] = capo_iotsitewise.types.error_details.serialize_json(
            value["error"]
        )
    return out


def deserialize_json(data: dict) -> DatasetStatus:
    out: DatasetStatus = {}  # type: ignore[typeddict-item]
    if data.get("state") is not None:
        import capo_iotsitewise.types.dataset_state

        out["state"] = capo_iotsitewise.types.dataset_state.deserialize_json(
            data["state"]
        )
    else:
        import typing

        out["state"] = typing.cast(
            "capo_iotsitewise.types.dataset_state.DatasetState", ""
        )
    if data.get("error") is not None:
        import capo_iotsitewise.types.error_details

        out["error"] = capo_iotsitewise.types.error_details.deserialize_json(
            data["error"]
        )
    return out
