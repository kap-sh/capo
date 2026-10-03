"""Generated from Smithy shape ``com.amazonaws.mediaconvert#DashAdditionalManifest``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_mediaconvert.types.__list_of__string_min1
    import capo_mediaconvert.types.__string_min1


class DashAdditionalManifest(TypedDict, closed=True):
    manifest_name_modifier: NotRequired[
        "capo_mediaconvert.types.__string_min1.__stringMin1"
    ]
    """Specify a name modifier that the service adds to the name of this manifest to make it different from the file names of the other main manifests in the output group. For example, say that the default main manifest for your DASH group is film-name.mpd. If you enter "-no-premium" for this setting, then the file name the service generates for this top-level manifest is film-name-no-premium.mpd."""
    selected_outputs: NotRequired[
        "capo_mediaconvert.types.__list_of__string_min1.__listOf__stringMin1"
    ]
    """Specify the outputs that you want this additional top-level manifest to reference."""


# --- restJson1 ser/de ---
def serialize_json(value: DashAdditionalManifest) -> dict:
    out: dict = {}
    if "manifest_name_modifier" in value:
        out["manifestNameModifier"] = value["manifest_name_modifier"]
    if "selected_outputs" in value:
        import capo_mediaconvert.types.__list_of__string_min1

        out["selectedOutputs"] = (
            capo_mediaconvert.types.__list_of__string_min1.serialize_json(
                value["selected_outputs"]
            )
        )
    return out


def deserialize_json(data: dict) -> DashAdditionalManifest:
    out: DashAdditionalManifest = {}  # type: ignore[typeddict-item]
    if data.get("manifestNameModifier") is not None:
        out["manifest_name_modifier"] = data["manifestNameModifier"]
    if data.get("selectedOutputs") is not None:
        import capo_mediaconvert.types.__list_of__string_min1

        out["selected_outputs"] = (
            capo_mediaconvert.types.__list_of__string_min1.deserialize_json(
                data["selectedOutputs"]
            )
        )
    return out
