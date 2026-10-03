"""Generated from Smithy shape ``com.amazonaws.bedrock#CustomMetricDefinition``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

from capo_bedrock.errors import DeserializationError

if TYPE_CHECKING:
    import capo_bedrock.types.custom_metric_instructions
    import capo_bedrock.types.metric_name
    import capo_bedrock.types.rating_scale


class CustomMetricDefinition(TypedDict, closed=True):
    name: "capo_bedrock.types.metric_name.MetricName"
    """<p>The name for a custom metric. Names must be unique in your Amazon Web Services region.</p>"""
    instructions: (
        "capo_bedrock.types.custom_metric_instructions.CustomMetricInstructions"
    )
    """<p>The prompt for a custom metric that instructs the evaluator model how to rate the model or RAG source under evaluation.</p>"""
    rating_scale: NotRequired["capo_bedrock.types.rating_scale.RatingScale"]
    """<p>Defines the rating scale to be used for a custom metric. We recommend that you always define a ratings scale when creating a custom metric. If you don't define a scale, Amazon Bedrock won't be able to visually display the results of the evaluation in the console or calculate average values of numerical scores. For more information on specifying a rating scale, see <a href="https://docs.aws.amazon.com/bedrock/latest/userguide/model-evaluation-custom-metrics-prompt-formats.html#model-evaluation-custom-metrics-prompt-formats-schema">Specifying an output schema (rating scale)</a>.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: CustomMetricDefinition) -> dict:
    out: dict = {}
    out["name"] = value["name"]
    out["instructions"] = value["instructions"]
    if "rating_scale" in value:
        import capo_bedrock.types.rating_scale

        out["ratingScale"] = capo_bedrock.types.rating_scale.serialize_json(
            value["rating_scale"]
        )
    return out


def deserialize_json(data: dict) -> CustomMetricDefinition:
    out: CustomMetricDefinition = {}  # type: ignore[typeddict-item]
    if data.get("name") is not None:
        out["name"] = data["name"]
    else:
        raise DeserializationError("CustomMetricDefinition.name required")
    if data.get("instructions") is not None:
        out["instructions"] = data["instructions"]
    else:
        raise DeserializationError("CustomMetricDefinition.instructions required")
    if data.get("ratingScale") is not None:
        import capo_bedrock.types.rating_scale

        out["rating_scale"] = capo_bedrock.types.rating_scale.deserialize_json(
            data["ratingScale"]
        )
    return out
