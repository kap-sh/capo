"""Generated from Smithy shape ``com.amazonaws.managedblockchain#NetworkSummary``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_managedblockchain.types.arn_string
    import capo_managedblockchain.types.description_string
    import capo_managedblockchain.types.framework
    import capo_managedblockchain.types.framework_version_string
    import capo_managedblockchain.types.name_string
    import capo_managedblockchain.types.network_status
    import capo_managedblockchain.types.resource_id_string
    import capo_managedblockchain.types.timestamp


class NetworkSummary(TypedDict, closed=True):
    id: NotRequired["capo_managedblockchain.types.resource_id_string.ResourceIdString"]
    """<p>The unique identifier of the network.</p>"""
    name: NotRequired["capo_managedblockchain.types.name_string.NameString"]
    """<p>The name of the network.</p>"""
    description: NotRequired[
        "capo_managedblockchain.types.description_string.DescriptionString"
    ]
    """<p>An optional description of the network.</p>"""
    framework: NotRequired["capo_managedblockchain.types.framework.Framework"]
    """<p>The blockchain framework that the network uses.</p>"""
    framework_version: NotRequired[
        "capo_managedblockchain.types.framework_version_string.FrameworkVersionString"
    ]
    """<p>The version of the blockchain framework that the network uses.</p>"""
    status: NotRequired["capo_managedblockchain.types.network_status.NetworkStatus"]
    """<p>The current status of the network.</p>"""
    creation_date: NotRequired["capo_managedblockchain.types.timestamp.Timestamp"]
    """<p>The date and time that the network was created.</p>"""
    arn: NotRequired["capo_managedblockchain.types.arn_string.ArnString"]
    """<p>The Amazon Resource Name (ARN) of the network. For more information about ARNs and their format, see <a href="https://docs.aws.amazon.com/general/latest/gr/aws-arns-and-namespaces.html">Amazon Resource Names (ARNs)</a> in the <i>Amazon Web Services General Reference</i>.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: NetworkSummary) -> dict:
    out: dict = {}
    if "id" in value:
        out["Id"] = value["id"]
    if "name" in value:
        out["Name"] = value["name"]
    if "description" in value:
        out["Description"] = value["description"]
    if "framework" in value:
        import capo_managedblockchain.types.framework

        out["Framework"] = capo_managedblockchain.types.framework.serialize_json(
            value["framework"]
        )
    if "framework_version" in value:
        out["FrameworkVersion"] = value["framework_version"]
    if "status" in value:
        import capo_managedblockchain.types.network_status

        out["Status"] = capo_managedblockchain.types.network_status.serialize_json(
            value["status"]
        )
    if "creation_date" in value:
        import capo_managedblockchain.types.timestamp

        out["CreationDate"] = capo_managedblockchain.types.timestamp.serialize_json(
            value["creation_date"]
        )
    if "arn" in value:
        out["Arn"] = value["arn"]
    return out


def deserialize_json(data: dict) -> NetworkSummary:
    out: NetworkSummary = {}  # type: ignore[typeddict-item]
    if data.get("Id") is not None:
        out["id"] = data["Id"]
    if data.get("Name") is not None:
        out["name"] = data["Name"]
    if data.get("Description") is not None:
        out["description"] = data["Description"]
    if data.get("Framework") is not None:
        import capo_managedblockchain.types.framework

        out["framework"] = capo_managedblockchain.types.framework.deserialize_json(
            data["Framework"]
        )
    if data.get("FrameworkVersion") is not None:
        out["framework_version"] = data["FrameworkVersion"]
    if data.get("Status") is not None:
        import capo_managedblockchain.types.network_status

        out["status"] = capo_managedblockchain.types.network_status.deserialize_json(
            data["Status"]
        )
    if data.get("CreationDate") is not None:
        import capo_managedblockchain.types.timestamp

        out["creation_date"] = capo_managedblockchain.types.timestamp.deserialize_json(
            data["CreationDate"]
        )
    if data.get("Arn") is not None:
        out["arn"] = data["Arn"]
    return out
