"""Generated from Smithy shape ``com.amazonaws.mediapackagev2#MultiviewFilterConfiguration``."""

from typing import TYPE_CHECKING

from typing_extensions import TypedDict

from capo_mediapackagev2.errors import DeserializationError

if TYPE_CHECKING:
    import capo_mediapackagev2.types.multiview_layout_type
    import capo_mediapackagev2.types.multiview_source_list


class MultiviewFilterConfiguration(TypedDict, closed=True):
    layout: "capo_mediapackagev2.types.multiview_layout_type.MultiviewLayoutType"
    """<p>The layout that MediaPackage uses to composite the tiles into a single output. This layout must be one of the <code>AvailableLayouts</code> of the channel that this origin endpoint is on.</p>"""
    sources: "capo_mediapackagev2.types.multiview_source_list.MultiviewSourceList"
    """<p>The source channels to composite, in tile order. Each channel must be one of the <code>AvailableSources</code> of the channel that this origin endpoint is on, and the number of channels must equal the number of tiles in <code>Layout</code>.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: MultiviewFilterConfiguration) -> dict:
    out: dict = {}
    import capo_mediapackagev2.types.multiview_layout_type

    out["Layout"] = capo_mediapackagev2.types.multiview_layout_type.serialize_json(
        value["layout"]
    )
    import capo_mediapackagev2.types.multiview_source_list

    out["Sources"] = capo_mediapackagev2.types.multiview_source_list.serialize_json(
        value["sources"]
    )
    return out


def deserialize_json(data: dict) -> MultiviewFilterConfiguration:
    out: MultiviewFilterConfiguration = {}  # type: ignore[typeddict-item]
    if data.get("Layout") is not None:
        import capo_mediapackagev2.types.multiview_layout_type

        out["layout"] = (
            capo_mediapackagev2.types.multiview_layout_type.deserialize_json(
                data["Layout"]
            )
        )
    else:
        raise DeserializationError("MultiviewFilterConfiguration.layout required")
    if data.get("Sources") is not None:
        import capo_mediapackagev2.types.multiview_source_list

        out["sources"] = (
            capo_mediapackagev2.types.multiview_source_list.deserialize_json(
                data["Sources"]
            )
        )
    else:
        raise DeserializationError("MultiviewFilterConfiguration.sources required")
    return out
