"""Generated from Smithy shape ``com.amazonaws.transcribe#ToxicityDetectionSettings``."""

from typing import TYPE_CHECKING

from typing_extensions import TypedDict

if TYPE_CHECKING:
    import capo_transcribe.types.toxicity_categories


class ToxicityDetectionSettings(TypedDict, closed=True):
    toxicity_categories: "capo_transcribe.types.toxicity_categories.ToxicityCategories"
    """<p> If you include <code>ToxicityDetection</code> in your transcription request, you must also include <code>ToxicityCategories</code>. The only accepted value for this parameter is <code>ALL</code>.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: ToxicityDetectionSettings) -> dict:
    out: dict = {}
    import capo_transcribe.types.toxicity_categories

    out["ToxicityCategories"] = (
        capo_transcribe.types.toxicity_categories.serialize_aws_json_1_1(
            value["toxicity_categories"]
        )
    )
    return out


def deserialize_aws_json_1_1(data: dict) -> ToxicityDetectionSettings:
    out: ToxicityDetectionSettings = {}  # type: ignore[typeddict-item]
    if data.get("ToxicityCategories") is not None:
        import capo_transcribe.types.toxicity_categories

        out["toxicity_categories"] = (
            capo_transcribe.types.toxicity_categories.deserialize_aws_json_1_1(
                data["ToxicityCategories"]
            )
        )
    else:
        out["toxicity_categories"] = []
    return out
