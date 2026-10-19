"""Generated from Smithy shape ``com.amazonaws.quicksight#VpcConnectionProperties``."""

from typing import TYPE_CHECKING

from typing_extensions import TypedDict

if TYPE_CHECKING:
    import capo_quicksight.types.arn


class VpcConnectionProperties(TypedDict, closed=True):
    vpc_connection_arn: "capo_quicksight.types.arn.Arn"
    """<p>The Amazon Resource Name (ARN) for the VPC connection.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: VpcConnectionProperties) -> dict:
    out: dict = {}
    out["VpcConnectionArn"] = value["vpc_connection_arn"]
    return out


def deserialize_json(data: dict) -> VpcConnectionProperties:
    out: VpcConnectionProperties = {}  # type: ignore[typeddict-item]
    if data.get("VpcConnectionArn") is not None:
        out["vpc_connection_arn"] = data["VpcConnectionArn"]
    else:
        out["vpc_connection_arn"] = ""
    return out
