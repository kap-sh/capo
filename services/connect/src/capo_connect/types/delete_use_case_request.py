"""Generated from Smithy shape ``com.amazonaws.connect#DeleteUseCaseRequest``."""

from typing import TYPE_CHECKING

from typing_extensions import TypedDict

if TYPE_CHECKING:
    import capo_connect.types.instance_id
    import capo_connect.types.integration_association_id
    import capo_connect.types.use_case_id


class DeleteUseCaseRequest(TypedDict, closed=True):
    instance_id: "capo_connect.types.instance_id.InstanceId"
    """<p>The identifier of the Connect Customer instance. You can <a href="https://docs.aws.amazon.com/connect/latest/adminguide/find-instance-arn.html">find the instance ID</a> in the Amazon Resource Name (ARN) of the instance.</p>"""
    integration_association_id: (
        "capo_connect.types.integration_association_id.IntegrationAssociationId"
    )
    """<p>The identifier for the integration association.</p>"""
    use_case_id: "capo_connect.types.use_case_id.UseCaseId"
    """<p>The identifier for the use case.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: DeleteUseCaseRequest) -> dict:
    out: dict = {}
    return out


def deserialize_json(data: dict) -> DeleteUseCaseRequest:
    out: DeleteUseCaseRequest = {}  # type: ignore[typeddict-item]
    return out
