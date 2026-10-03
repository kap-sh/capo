"""Generated from Smithy shape ``com.amazonaws.ivs#RenditionConfiguration``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_ivs.types.rendition_configuration_rendition_list
    import capo_ivs.types.rendition_configuration_rendition_selection


class RenditionConfiguration(TypedDict, closed=True):
    rendition_selection: NotRequired[
        "capo_ivs.types.rendition_configuration_rendition_selection.RenditionConfigurationRenditionSelection"
    ]
    """<p>Indicates which set of renditions are recorded for a stream. For <code>BASIC</code> channels, the <code>CUSTOM</code> value has no effect. If <code>CUSTOM</code> is specified, a set of renditions must be specified in the <code>renditions</code> field. Default: <code>ALL</code>.</p>"""
    renditions: NotRequired[
        "capo_ivs.types.rendition_configuration_rendition_list.RenditionConfigurationRenditionList"
    ]
    """<p>Indicates which renditions are recorded for a stream, if <code>renditionSelection</code> is <code>CUSTOM</code>; otherwise, this field is irrelevant. The selected renditions are recorded if they are available during the stream. If a selected rendition is unavailable, the best available rendition is recorded. For details on the resolution dimensions of each rendition, see <a href="https://docs.aws.amazon.com/ivs/latest/userguide/record-to-s3.html">Auto-Record to Amazon S3</a>.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: RenditionConfiguration) -> dict:
    out: dict = {}
    if "rendition_selection" in value:
        out["renditionSelection"] = value["rendition_selection"]
    if "renditions" in value:
        import capo_ivs.types.rendition_configuration_rendition_list

        out["renditions"] = (
            capo_ivs.types.rendition_configuration_rendition_list.serialize_json(
                value["renditions"]
            )
        )
    return out


def deserialize_json(data: dict) -> RenditionConfiguration:
    out: RenditionConfiguration = {}  # type: ignore[typeddict-item]
    if data.get("renditionSelection") is not None:
        out["rendition_selection"] = data["renditionSelection"]
    if data.get("renditions") is not None:
        import capo_ivs.types.rendition_configuration_rendition_list

        out["renditions"] = (
            capo_ivs.types.rendition_configuration_rendition_list.deserialize_json(
                data["renditions"]
            )
        )
    return out
