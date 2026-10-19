"""Generated from Smithy shape ``com.amazonaws.frauddetector#DeleteExternalModelRequest``."""

from typing import TYPE_CHECKING

from typing_extensions import TypedDict

if TYPE_CHECKING:
    import capo_frauddetector.types.sage_maker_endpoint_identifier


class DeleteExternalModelRequest(TypedDict, closed=True):
    model_endpoint: "capo_frauddetector.types.sage_maker_endpoint_identifier.sageMakerEndpointIdentifier"
    """<p>The endpoint of the Amazon Sagemaker model to delete.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: DeleteExternalModelRequest) -> dict:
    out: dict = {}
    out["modelEndpoint"] = value["model_endpoint"]
    return out


def deserialize_aws_json_1_1(data: dict) -> DeleteExternalModelRequest:
    out: DeleteExternalModelRequest = {}  # type: ignore[typeddict-item]
    if data.get("modelEndpoint") is not None:
        out["model_endpoint"] = data["modelEndpoint"]
    else:
        out["model_endpoint"] = ""
    return out
