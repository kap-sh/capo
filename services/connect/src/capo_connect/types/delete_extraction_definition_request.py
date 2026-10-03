"""Generated from Smithy shape ``com.amazonaws.connect#DeleteExtractionDefinitionRequest``."""

from typing import TYPE_CHECKING

from typing_extensions import TypedDict

if TYPE_CHECKING:
    import capo_connect.types.extraction_definition_id
    import capo_connect.types.instance_id


class DeleteExtractionDefinitionRequest(TypedDict, closed=True):
    instance_id: "capo_connect.types.instance_id.InstanceId"
    """<p>The identifier of the Connect Customer instance. You can <a href="https://docs.aws.amazon.com/connect/latest/adminguide/find-instance-arn.html">find the instance ID</a> in the Amazon Resource Name (ARN) of the instance.</p>"""
    extraction_definition_id: (
        "capo_connect.types.extraction_definition_id.ExtractionDefinitionId"
    )
    """<p>The identifier of the extraction definition to delete.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: DeleteExtractionDefinitionRequest) -> dict:
    out: dict = {}
    return out


def deserialize_json(data: dict) -> DeleteExtractionDefinitionRequest:
    out: DeleteExtractionDefinitionRequest = {}  # type: ignore[typeddict-item]
    return out
