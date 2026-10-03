"""Generated from Smithy shape ``com.amazonaws.managedblockchain#AccessorSummary``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_managedblockchain.types.accessor_network_type
    import capo_managedblockchain.types.accessor_status
    import capo_managedblockchain.types.accessor_type
    import capo_managedblockchain.types.arn_string
    import capo_managedblockchain.types.resource_id_string
    import capo_managedblockchain.types.timestamp


class AccessorSummary(TypedDict, closed=True):
    id: NotRequired["capo_managedblockchain.types.resource_id_string.ResourceIdString"]
    """<p>The unique identifier of the accessor.</p>"""
    type: NotRequired["capo_managedblockchain.types.accessor_type.AccessorType"]
    """<p>The type of the accessor.</p> <note> <p>Currently accessor type is restricted to <code>BILLING_TOKEN</code>.</p> </note>"""
    status: NotRequired["capo_managedblockchain.types.accessor_status.AccessorStatus"]
    """<p>The current status of the accessor.</p>"""
    creation_date: NotRequired["capo_managedblockchain.types.timestamp.Timestamp"]
    """<p>The creation date and time of the accessor.</p>"""
    arn: NotRequired["capo_managedblockchain.types.arn_string.ArnString"]
    """<p>The Amazon Resource Name (ARN) of the accessor. For more information about ARNs and their format, see <a href="https://docs.aws.amazon.com/general/latest/gr/aws-arns-and-namespaces.html">Amazon Resource Names (ARNs)</a> in the <i>Amazon Web Services General Reference</i>.</p>"""
    network_type: NotRequired[
        "capo_managedblockchain.types.accessor_network_type.AccessorNetworkType"
    ]
    """<p>The blockchain network that the Accessor token is created for.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: AccessorSummary) -> dict:
    out: dict = {}
    if "id" in value:
        out["Id"] = value["id"]
    if "type" in value:
        import capo_managedblockchain.types.accessor_type

        out["Type"] = capo_managedblockchain.types.accessor_type.serialize_json(
            value["type"]
        )
    if "status" in value:
        import capo_managedblockchain.types.accessor_status

        out["Status"] = capo_managedblockchain.types.accessor_status.serialize_json(
            value["status"]
        )
    if "creation_date" in value:
        import capo_managedblockchain.types.timestamp

        out["CreationDate"] = capo_managedblockchain.types.timestamp.serialize_json(
            value["creation_date"]
        )
    if "arn" in value:
        out["Arn"] = value["arn"]
    if "network_type" in value:
        import capo_managedblockchain.types.accessor_network_type

        out["NetworkType"] = (
            capo_managedblockchain.types.accessor_network_type.serialize_json(
                value["network_type"]
            )
        )
    return out


def deserialize_json(data: dict) -> AccessorSummary:
    out: AccessorSummary = {}  # type: ignore[typeddict-item]
    if data.get("Id") is not None:
        out["id"] = data["Id"]
    if data.get("Type") is not None:
        import capo_managedblockchain.types.accessor_type

        out["type"] = capo_managedblockchain.types.accessor_type.deserialize_json(
            data["Type"]
        )
    if data.get("Status") is not None:
        import capo_managedblockchain.types.accessor_status

        out["status"] = capo_managedblockchain.types.accessor_status.deserialize_json(
            data["Status"]
        )
    if data.get("CreationDate") is not None:
        import capo_managedblockchain.types.timestamp

        out["creation_date"] = capo_managedblockchain.types.timestamp.deserialize_json(
            data["CreationDate"]
        )
    if data.get("Arn") is not None:
        out["arn"] = data["Arn"]
    if data.get("NetworkType") is not None:
        import capo_managedblockchain.types.accessor_network_type

        out["network_type"] = (
            capo_managedblockchain.types.accessor_network_type.deserialize_json(
                data["NetworkType"]
            )
        )
    return out
