"""Generated from Smithy shape ``com.amazonaws.quicksight#AnonymousUserGenerativeQnAEmbeddingConfiguration``."""

from typing import TYPE_CHECKING

from typing_extensions import TypedDict

if TYPE_CHECKING:
    import capo_quicksight.types.restrictive_resource_id


class AnonymousUserGenerativeQnAEmbeddingConfiguration(TypedDict, closed=True):
    initial_topic_id: (
        "capo_quicksight.types.restrictive_resource_id.RestrictiveResourceId"
    )
    """<p>The Quick Sight Q topic ID of the new reader experience topic that you want the anonymous user to see first. This ID is included in the output URL. When the URL in response is accessed, Quick Sight renders the Generative Q&A experience with this new reader experience topic pre selected.</p> <p>The Amazon Resource Name (ARN) of this Q new reader experience topic must be included in the <code>AuthorizedResourceArns</code> parameter. Otherwise, the request fails with an <code>InvalidParameterValueException</code> error.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: AnonymousUserGenerativeQnAEmbeddingConfiguration) -> dict:
    out: dict = {}
    out["InitialTopicId"] = value["initial_topic_id"]
    return out


def deserialize_json(data: dict) -> AnonymousUserGenerativeQnAEmbeddingConfiguration:
    out: AnonymousUserGenerativeQnAEmbeddingConfiguration = {}  # type: ignore[typeddict-item]
    if data.get("InitialTopicId") is not None:
        out["initial_topic_id"] = data["InitialTopicId"]
    else:
        out["initial_topic_id"] = ""
    return out
