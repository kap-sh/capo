"""Generated from Smithy shape ``com.amazonaws.odb#DeleteOdbPeeringConnectionInput``."""

from typing import TYPE_CHECKING

from typing_extensions import TypedDict

if TYPE_CHECKING:
    import capo_odb.types.resource_id_or_arn


class DeleteOdbPeeringConnectionInput(TypedDict, closed=True):
    odb_peering_connection_id: "capo_odb.types.resource_id_or_arn.ResourceIdOrArn"
    """<p>The unique identifier of the ODB peering connection to delete.</p>"""


# --- awsJson1_0 ser/de ---
def serialize_aws_json_1_0(value: DeleteOdbPeeringConnectionInput) -> dict:
    out: dict = {}
    out["odbPeeringConnectionId"] = value["odb_peering_connection_id"]
    return out


def deserialize_aws_json_1_0(data: dict) -> DeleteOdbPeeringConnectionInput:
    out: DeleteOdbPeeringConnectionInput = {}  # type: ignore[typeddict-item]
    if data.get("odbPeeringConnectionId") is not None:
        out["odb_peering_connection_id"] = data["odbPeeringConnectionId"]
    else:
        out["odb_peering_connection_id"] = ""
    return out
