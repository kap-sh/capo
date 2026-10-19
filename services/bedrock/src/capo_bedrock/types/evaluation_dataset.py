"""Generated from Smithy shape ``com.amazonaws.bedrock#EvaluationDataset``."""

from typing import TYPE_CHECKING, Any

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_bedrock.types.evaluation_dataset_location
    import capo_bedrock.types.evaluation_dataset_name


class EvaluationDataset(TypedDict, closed=True):
    name: "capo_bedrock.types.evaluation_dataset_name.EvaluationDatasetName"
    """<p>Used to specify supported built-in prompt datasets. Valid values are <code>Builtin.Bold</code>, <code>Builtin.BoolQ</code>, <code>Builtin.NaturalQuestions</code>, <code>Builtin.Gigaword</code>, <code>Builtin.RealToxicityPrompts</code>, <code>Builtin.TriviaQA</code>, <code>Builtin.T-Rex</code>, <code>Builtin.WomensEcommerceClothingReviews</code> and <code>Builtin.Wikitext2</code>.</p>"""
    dataset_location: NotRequired[
        "capo_bedrock.types.evaluation_dataset_location.EvaluationDatasetLocation"
    ]
    """<p>For custom prompt datasets, you must specify the location in Amazon S3 where the prompt dataset is saved.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: EvaluationDataset) -> dict:
    out: dict = {}
    out["name"] = value["name"]
    if "dataset_location" in value:
        import capo_bedrock.types.evaluation_dataset_location

        out["datasetLocation"] = (
            capo_bedrock.types.evaluation_dataset_location.serialize_json(
                value["dataset_location"]
            )
        )
    return out


def deserialize_json(data: dict) -> EvaluationDataset:
    out: EvaluationDataset = {}  # type: ignore[typeddict-item]
    if data.get("name") is not None:
        out["name"] = data["name"]
    else:
        out["name"] = ""
    if data.get("datasetLocation") is not None:
        import capo_bedrock.types.evaluation_dataset_location

        out["dataset_location"] = (
            capo_bedrock.types.evaluation_dataset_location.deserialize_json(
                data["datasetLocation"]
            )
        )
    return out


def redact_sensitive(value: EvaluationDataset) -> dict[str, Any]:
    out: dict[str, Any] = dict(value)
    if "name" in value:
        out["name"] = "*** Sensitive Data Redacted ***"
    return out
