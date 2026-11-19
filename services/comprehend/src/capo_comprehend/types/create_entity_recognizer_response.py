"""Generated from Smithy shape ``com.amazonaws.comprehend#CreateEntityRecognizerResponse``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_comprehend.types.entity_recognizer_arn


class CreateEntityRecognizerResponse(TypedDict, closed=True):
    entity_recognizer_arn: NotRequired[
        "capo_comprehend.types.entity_recognizer_arn.EntityRecognizerArn"
    ]
    """<p>The Amazon Resource Name (ARN) that identifies the entity recognizer.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: CreateEntityRecognizerResponse) -> dict:
    out: dict = {}
    if "entity_recognizer_arn" in value:
        out["EntityRecognizerArn"] = value["entity_recognizer_arn"]
    return out


def deserialize_aws_json_1_1(data: dict) -> CreateEntityRecognizerResponse:
    out: CreateEntityRecognizerResponse = {}  # type: ignore[typeddict-item]
    if data.get("EntityRecognizerArn") is not None:
        out["entity_recognizer_arn"] = data["EntityRecognizerArn"]
    return out


# --- rpcv2Cbor ser/de ---
def serialize_cbor(value: CreateEntityRecognizerResponse) -> dict:
    out: dict = {}
    if "entity_recognizer_arn" in value:
        out["EntityRecognizerArn"] = value["entity_recognizer_arn"]
    return out


def deserialize_cbor(data: dict) -> CreateEntityRecognizerResponse:
    out: CreateEntityRecognizerResponse = {}  # type: ignore[typeddict-item]
    if data.get("EntityRecognizerArn") is not None:
        out["entity_recognizer_arn"] = data["EntityRecognizerArn"]
    return out
