"""Generated from Smithy shape ``com.amazonaws.quicksight#WordCloudFieldWells``."""

from typing import TYPE_CHECKING, Any

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_quicksight.types.word_cloud_aggregated_field_wells


class WordCloudFieldWells(TypedDict, closed=True):
    word_cloud_aggregated_field_wells: NotRequired[
        "capo_quicksight.types.word_cloud_aggregated_field_wells.WordCloudAggregatedFieldWells"
    ]
    """<p>The aggregated field wells of a word cloud.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: WordCloudFieldWells) -> dict:
    out: dict = {}
    if "word_cloud_aggregated_field_wells" in value:
        import capo_quicksight.types.word_cloud_aggregated_field_wells

        out["WordCloudAggregatedFieldWells"] = (
            capo_quicksight.types.word_cloud_aggregated_field_wells.serialize_json(
                value["word_cloud_aggregated_field_wells"]
            )
        )
    return out


def deserialize_json(data: dict) -> WordCloudFieldWells:
    out: WordCloudFieldWells = {}  # type: ignore[typeddict-item]
    if data.get("WordCloudAggregatedFieldWells") is not None:
        import capo_quicksight.types.word_cloud_aggregated_field_wells

        out["word_cloud_aggregated_field_wells"] = (
            capo_quicksight.types.word_cloud_aggregated_field_wells.deserialize_json(
                data["WordCloudAggregatedFieldWells"]
            )
        )
    return out


def redact_sensitive(value: WordCloudFieldWells) -> dict[str, Any]:
    out: dict[str, Any] = dict(value)
    if "word_cloud_aggregated_field_wells" in value:
        import capo_quicksight.types.word_cloud_aggregated_field_wells

        out["word_cloud_aggregated_field_wells"] = (
            capo_quicksight.types.word_cloud_aggregated_field_wells.redact_sensitive(
                value["word_cloud_aggregated_field_wells"]
            )
        )
    return out
