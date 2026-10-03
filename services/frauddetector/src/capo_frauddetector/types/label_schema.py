"""Generated from Smithy shape ``com.amazonaws.frauddetector#LabelSchema``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_frauddetector.types.label_mapper
    import capo_frauddetector.types.unlabeled_events_treatment


class LabelSchema(TypedDict, closed=True):
    label_mapper: NotRequired["capo_frauddetector.types.label_mapper.labelMapper"]
    """<p>The label mapper maps the Amazon Fraud Detector supported model classification labels (<code>FRAUD</code>, <code>LEGIT</code>) to the appropriate event type labels. For example, if "<code>FRAUD</code>" and "<code>LEGIT</code>" are Amazon Fraud Detector supported labels, this mapper could be: <code>{"FRAUD" => ["0"]</code>, <code>"LEGIT" => ["1"]}</code> or <code>{"FRAUD" => ["false"]</code>, <code>"LEGIT" => ["true"]}</code> or <code>{"FRAUD" => ["fraud", "abuse"]</code>, <code>"LEGIT" => ["legit", "safe"]}</code>. The value part of the mapper is a list, because you may have multiple label variants from your event type for a single Amazon Fraud Detector label. </p>"""
    unlabeled_events_treatment: NotRequired[
        "capo_frauddetector.types.unlabeled_events_treatment.UnlabeledEventsTreatment"
    ]
    """<p>The action to take for unlabeled events.</p> <ul> <li> <p>Use <code>IGNORE</code> if you want the unlabeled events to be ignored. This is recommended when the majority of the events in the dataset are labeled.</p> </li> <li> <p>Use <code>FRAUD</code> if you want to categorize all unlabeled events as “Fraud”. This is recommended when most of the events in your dataset are fraudulent.</p> </li> <li> <p>Use <code>LEGIT</code> if you want to categorize all unlabeled events as “Legit”. This is recommended when most of the events in your dataset are legitimate.</p> </li> <li> <p>Use <code>AUTO</code> if you want Amazon Fraud Detector to decide how to use the unlabeled data. This is recommended when there is significant unlabeled events in the dataset.</p> </li> </ul> <p>By default, Amazon Fraud Detector ignores the unlabeled data.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: LabelSchema) -> dict:
    out: dict = {}
    if "label_mapper" in value:
        import capo_frauddetector.types.label_mapper

        out["labelMapper"] = (
            capo_frauddetector.types.label_mapper.serialize_aws_json_1_1(
                value["label_mapper"]
            )
        )
    if "unlabeled_events_treatment" in value:
        import capo_frauddetector.types.unlabeled_events_treatment

        out["unlabeledEventsTreatment"] = (
            capo_frauddetector.types.unlabeled_events_treatment.serialize_aws_json_1_1(
                value["unlabeled_events_treatment"]
            )
        )
    return out


def deserialize_aws_json_1_1(data: dict) -> LabelSchema:
    out: LabelSchema = {}  # type: ignore[typeddict-item]
    if data.get("labelMapper") is not None:
        import capo_frauddetector.types.label_mapper

        out["label_mapper"] = (
            capo_frauddetector.types.label_mapper.deserialize_aws_json_1_1(
                data["labelMapper"]
            )
        )
    if data.get("unlabeledEventsTreatment") is not None:
        import capo_frauddetector.types.unlabeled_events_treatment

        out["unlabeled_events_treatment"] = (
            capo_frauddetector.types.unlabeled_events_treatment.deserialize_aws_json_1_1(
                data["unlabeledEventsTreatment"]
            )
        )
    return out
