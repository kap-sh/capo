"""Generated from Smithy shape ``com.amazonaws.cloudcontrol#ResourceDescription``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_cloudcontrol.types.identifier
    import capo_cloudcontrol.types.properties


class ResourceDescription(TypedDict, closed=True):
    identifier: NotRequired["capo_cloudcontrol.types.identifier.Identifier"]
    """<p>The primary identifier for the resource.</p> <p>For more information, see <a href="https://docs.aws.amazon.com/cloudcontrolapi/latest/userguide/resource-identifier.html">Identifying resources</a> in the <i>Amazon Web Services Cloud Control API User Guide</i>.</p>"""
    properties: NotRequired["capo_cloudcontrol.types.properties.Properties"]
    """<p>A list of the resource properties and their current values.</p>"""


# --- awsJson1_0 ser/de ---
def serialize_aws_json_1_0(value: ResourceDescription) -> dict:
    out: dict = {}
    if "identifier" in value:
        out["Identifier"] = value["identifier"]
    if "properties" in value:
        out["Properties"] = value["properties"]
    return out


def deserialize_aws_json_1_0(data: dict) -> ResourceDescription:
    out: ResourceDescription = {}  # type: ignore[typeddict-item]
    if data.get("Identifier") is not None:
        out["identifier"] = data["Identifier"]
    if data.get("Properties") is not None:
        out["properties"] = data["Properties"]
    return out
