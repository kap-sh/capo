"""Generated from Smithy shape ``com.amazonaws.iotsitewise#Greengrass``."""

from typing import TYPE_CHECKING

from typing_extensions import TypedDict

from capo_iotsitewise.errors import DeserializationError

if TYPE_CHECKING:
    import capo_iotsitewise.types.arn


class Greengrass(TypedDict, closed=True):
    group_arn: "capo_iotsitewise.types.arn.ARN"
    """<p>The <a href="https://docs.aws.amazon.com/general/latest/gr/aws-arns-and-namespaces.html">ARN</a> of the Greengrass group. For more information about how to find a group's ARN, see <a href="https://docs.aws.amazon.com/greengrass/v1/apireference/listgroups-get.html">ListGroups</a> and <a href="https://docs.aws.amazon.com/greengrass/v1/apireference/getgroup-get.html">GetGroup</a> in the <i>IoT Greengrass V1 API Reference</i>.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: Greengrass) -> dict:
    out: dict = {}
    out["groupArn"] = value["group_arn"]
    return out


def deserialize_json(data: dict) -> Greengrass:
    out: Greengrass = {}  # type: ignore[typeddict-item]
    if data.get("groupArn") is not None:
        out["group_arn"] = data["groupArn"]
    else:
        raise DeserializationError("Greengrass.group_arn required")
    return out
