"""Generated from Smithy shape ``com.amazonaws.comprehend#DescribeEntityRecognizerResponse``."""

from typing import TYPE_CHECKING, Any

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_comprehend.types.entity_recognizer_properties


class DescribeEntityRecognizerResponse(TypedDict, closed=True):
    entity_recognizer_properties: NotRequired[
        "capo_comprehend.types.entity_recognizer_properties.EntityRecognizerProperties"
    ]
    """<p>Describes information associated with an entity recognizer.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: DescribeEntityRecognizerResponse) -> dict:
    out: dict = {}
    if "entity_recognizer_properties" in value:
        import capo_comprehend.types.entity_recognizer_properties

        out["EntityRecognizerProperties"] = (
            capo_comprehend.types.entity_recognizer_properties.serialize_aws_json_1_1(
                value["entity_recognizer_properties"]
            )
        )
    return out


def deserialize_aws_json_1_1(data: dict) -> DescribeEntityRecognizerResponse:
    out: DescribeEntityRecognizerResponse = {}  # type: ignore[typeddict-item]
    if data.get("EntityRecognizerProperties") is not None:
        import capo_comprehend.types.entity_recognizer_properties

        out["entity_recognizer_properties"] = (
            capo_comprehend.types.entity_recognizer_properties.deserialize_aws_json_1_1(
                data["EntityRecognizerProperties"]
            )
        )
    return out


def redact_sensitive(value: DescribeEntityRecognizerResponse) -> dict[str, Any]:
    out: dict[str, Any] = dict(value)
    if "entity_recognizer_properties" in value:
        import capo_comprehend.types.entity_recognizer_properties

        out["entity_recognizer_properties"] = (
            capo_comprehend.types.entity_recognizer_properties.redact_sensitive(
                value["entity_recognizer_properties"]
            )
        )
    return out
