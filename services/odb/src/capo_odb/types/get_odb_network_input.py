"""Generated from Smithy shape ``com.amazonaws.odb#GetOdbNetworkInput``."""

from typing import TYPE_CHECKING

from typing_extensions import TypedDict

if TYPE_CHECKING:
    import capo_odb.types.resource_id_or_arn


class GetOdbNetworkInput(TypedDict, closed=True):
    odb_network_id: "capo_odb.types.resource_id_or_arn.ResourceIdOrArn"
    """<p>The unique identifier of the ODB network.</p>"""


# --- awsJson1_0 ser/de ---
def serialize_aws_json_1_0(value: GetOdbNetworkInput) -> dict:
    out: dict = {}
    out["odbNetworkId"] = value["odb_network_id"]
    return out


def deserialize_aws_json_1_0(data: dict) -> GetOdbNetworkInput:
    out: GetOdbNetworkInput = {}  # type: ignore[typeddict-item]
    if data.get("odbNetworkId") is not None:
        out["odb_network_id"] = data["odbNetworkId"]
    else:
        out["odb_network_id"] = ""
    return out
