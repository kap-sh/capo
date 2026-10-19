"""Generated from Smithy shape ``com.amazonaws.mediapackagev2#MultiviewConfiguration``."""

from typing import TYPE_CHECKING

from typing_extensions import TypedDict

if TYPE_CHECKING:
    import capo_mediapackagev2.types.multiview_layout_list
    import capo_mediapackagev2.types.multiview_source_list


class MultiviewConfiguration(TypedDict, closed=True):
    available_sources: (
        "capo_mediapackagev2.types.multiview_source_list.MultiviewSourceList"
    )
    """<p>The channels that players can use as tiles in this multiview channel's output. Each source channel must be in the same channel group as the multiview channel, and must have an <code>InputType</code> of <code>CMAF</code>. Only the channels that you list here are available as tiles.</p>"""
    available_layouts: (
        "capo_mediapackagev2.types.multiview_layout_list.MultiviewLayoutList"
    )
    """<p>The tile layouts that players can request from this multiview channel's origin endpoints. Only the layouts that you list here are available. Each layout must appear at most once.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: MultiviewConfiguration) -> dict:
    out: dict = {}
    import capo_mediapackagev2.types.multiview_source_list

    out["AvailableSources"] = (
        capo_mediapackagev2.types.multiview_source_list.serialize_json(
            value["available_sources"]
        )
    )
    import capo_mediapackagev2.types.multiview_layout_list

    out["AvailableLayouts"] = (
        capo_mediapackagev2.types.multiview_layout_list.serialize_json(
            value["available_layouts"]
        )
    )
    return out


def deserialize_json(data: dict) -> MultiviewConfiguration:
    out: MultiviewConfiguration = {}  # type: ignore[typeddict-item]
    if data.get("AvailableSources") is not None:
        import capo_mediapackagev2.types.multiview_source_list

        out["available_sources"] = (
            capo_mediapackagev2.types.multiview_source_list.deserialize_json(
                data["AvailableSources"]
            )
        )
    else:
        out["available_sources"] = []
    if data.get("AvailableLayouts") is not None:
        import capo_mediapackagev2.types.multiview_layout_list

        out["available_layouts"] = (
            capo_mediapackagev2.types.multiview_layout_list.deserialize_json(
                data["AvailableLayouts"]
            )
        )
    else:
        out["available_layouts"] = []
    return out
