"""Generated from Smithy shape ``com.amazonaws.comprehend#DeleteEntityRecognizerRequest``."""

from typing import TYPE_CHECKING

from typing_extensions import TypedDict

if TYPE_CHECKING:
    import capo_comprehend.types.entity_recognizer_arn


class DeleteEntityRecognizerRequest(TypedDict, closed=True):
    entity_recognizer_arn: (
        "capo_comprehend.types.entity_recognizer_arn.EntityRecognizerArn"
    )
    """<p>The Amazon Resource Name (ARN) that identifies the entity recognizer.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: DeleteEntityRecognizerRequest) -> dict:
    out: dict = {}
    out["EntityRecognizerArn"] = value["entity_recognizer_arn"]
    return out


def deserialize_aws_json_1_1(data: dict) -> DeleteEntityRecognizerRequest:
    out: DeleteEntityRecognizerRequest = {}  # type: ignore[typeddict-item]
    if data.get("EntityRecognizerArn") is not None:
        out["entity_recognizer_arn"] = data["EntityRecognizerArn"]
    else:
        out["entity_recognizer_arn"] = ""
    return out
