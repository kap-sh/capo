"""Generated from Smithy shape ``com.amazonaws.frauddetector#EvaluatedExternalModel``."""

from typing import TYPE_CHECKING, Any

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_frauddetector.types.boolean
    import capo_frauddetector.types.map_of_strings
    import capo_frauddetector.types.string


class EvaluatedExternalModel(TypedDict, closed=True):
    model_endpoint: NotRequired["capo_frauddetector.types.string.string"]
    """<p> The endpoint of the external (Amazon Sagemaker) model. </p>"""
    use_event_variables: NotRequired["capo_frauddetector.types.boolean.Boolean"]
    """<p> Indicates whether event variables were used to generate predictions. </p>"""
    input_variables: NotRequired["capo_frauddetector.types.map_of_strings.MapOfStrings"]
    """<p> Input variables use for generating predictions. </p>"""
    output_variables: NotRequired[
        "capo_frauddetector.types.map_of_strings.MapOfStrings"
    ]
    """<p> Output variables. </p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: EvaluatedExternalModel) -> dict:
    out: dict = {}
    if "model_endpoint" in value:
        out["modelEndpoint"] = value["model_endpoint"]
    if "use_event_variables" in value:
        out["useEventVariables"] = value["use_event_variables"]
    if "input_variables" in value:
        import capo_frauddetector.types.map_of_strings

        out["inputVariables"] = (
            capo_frauddetector.types.map_of_strings.serialize_aws_json_1_1(
                value["input_variables"]
            )
        )
    if "output_variables" in value:
        import capo_frauddetector.types.map_of_strings

        out["outputVariables"] = (
            capo_frauddetector.types.map_of_strings.serialize_aws_json_1_1(
                value["output_variables"]
            )
        )
    return out


def deserialize_aws_json_1_1(data: dict) -> EvaluatedExternalModel:
    out: EvaluatedExternalModel = {}  # type: ignore[typeddict-item]
    if data.get("modelEndpoint") is not None:
        out["model_endpoint"] = data["modelEndpoint"]
    if data.get("useEventVariables") is not None:
        out["use_event_variables"] = data["useEventVariables"]
    if data.get("inputVariables") is not None:
        import capo_frauddetector.types.map_of_strings

        out["input_variables"] = (
            capo_frauddetector.types.map_of_strings.deserialize_aws_json_1_1(
                data["inputVariables"]
            )
        )
    if data.get("outputVariables") is not None:
        import capo_frauddetector.types.map_of_strings

        out["output_variables"] = (
            capo_frauddetector.types.map_of_strings.deserialize_aws_json_1_1(
                data["outputVariables"]
            )
        )
    return out


def redact_sensitive(value: EvaluatedExternalModel) -> dict[str, Any]:
    out: dict[str, Any] = dict(value)
    if "input_variables" in value:
        out["input_variables"] = "*** Sensitive Data Redacted ***"
    if "output_variables" in value:
        out["output_variables"] = "*** Sensitive Data Redacted ***"
    return out
