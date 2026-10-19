"""Generated from Smithy shape ``com.amazonaws.iotthingsgraph#GetEntitiesRequest``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_iotthingsgraph.types.urns
    import capo_iotthingsgraph.types.version


class GetEntitiesRequest(TypedDict, closed=True):
    ids: "capo_iotthingsgraph.types.urns.Urns"
    """<p>An array of entity IDs.</p> <p>The IDs should be in the following format.</p> <p> <code>urn:tdm:REGION/ACCOUNT ID/default:device:DEVICENAME</code> </p>"""
    namespace_version: NotRequired["capo_iotthingsgraph.types.version.Version"]
    """<p>The version of the user's namespace. Defaults to the latest version of the user's namespace.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: GetEntitiesRequest) -> dict:
    out: dict = {}
    import capo_iotthingsgraph.types.urns

    out["ids"] = capo_iotthingsgraph.types.urns.serialize_aws_json_1_1(value["ids"])
    if "namespace_version" in value:
        out["namespaceVersion"] = value["namespace_version"]
    return out


def deserialize_aws_json_1_1(data: dict) -> GetEntitiesRequest:
    out: GetEntitiesRequest = {}  # type: ignore[typeddict-item]
    if data.get("ids") is not None:
        import capo_iotthingsgraph.types.urns

        out["ids"] = capo_iotthingsgraph.types.urns.deserialize_aws_json_1_1(
            data["ids"]
        )
    else:
        out["ids"] = []
    if data.get("namespaceVersion") is not None:
        out["namespace_version"] = data["namespaceVersion"]
    return out
