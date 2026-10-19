"""Generated from Smithy shape ``com.amazonaws.iotthingsgraph#AssociateEntityToThingRequest``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_iotthingsgraph.types.thing_name
    import capo_iotthingsgraph.types.urn
    import capo_iotthingsgraph.types.version


class AssociateEntityToThingRequest(TypedDict, closed=True):
    thing_name: "capo_iotthingsgraph.types.thing_name.ThingName"
    """<p>The name of the thing to which the entity is to be associated.</p>"""
    entity_id: "capo_iotthingsgraph.types.urn.Urn"
    """<p>The ID of the device to be associated with the thing.</p> <p>The ID should be in the following format.</p> <p> <code>urn:tdm:REGION/ACCOUNT ID/default:device:DEVICENAME</code> </p>"""
    namespace_version: NotRequired["capo_iotthingsgraph.types.version.Version"]
    """<p>The version of the user's namespace. Defaults to the latest version of the user's namespace.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: AssociateEntityToThingRequest) -> dict:
    out: dict = {}
    out["thingName"] = value["thing_name"]
    out["entityId"] = value["entity_id"]
    if "namespace_version" in value:
        out["namespaceVersion"] = value["namespace_version"]
    return out


def deserialize_aws_json_1_1(data: dict) -> AssociateEntityToThingRequest:
    out: AssociateEntityToThingRequest = {}  # type: ignore[typeddict-item]
    if data.get("thingName") is not None:
        out["thing_name"] = data["thingName"]
    else:
        out["thing_name"] = ""
    if data.get("entityId") is not None:
        out["entity_id"] = data["entityId"]
    else:
        out["entity_id"] = ""
    if data.get("namespaceVersion") is not None:
        out["namespace_version"] = data["namespaceVersion"]
    return out
