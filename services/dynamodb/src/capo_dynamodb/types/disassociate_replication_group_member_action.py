"""Generated from Smithy shape ``com.amazonaws.dynamodb#DisassociateReplicationGroupMemberAction``."""

from typing import TYPE_CHECKING

from typing_extensions import TypedDict

if TYPE_CHECKING:
    import capo_dynamodb.types.disassociation_mode
    import capo_dynamodb.types.region_name


class DisassociateReplicationGroupMemberAction(TypedDict, closed=True):
    region_name: "capo_dynamodb.types.region_name.RegionName"
    """<p>The Region of the replica to disassociate. Set this value to the Region where you send the <code>UpdateTable</code> request. You must use credentials for the account that owns the replica.</p>"""
    disassociation_mode: "capo_dynamodb.types.disassociation_mode.DisassociationMode"
    """<p>The mode for handling pending replication before disassociation completes. You must specify <code>WAIT_FOR_REPLICATION</code>. For more information, see <a href="https://docs.aws.amazon.com/amazondynamodb/latest/developerguide/globaltables-disassociate.html">Disassociating a global table replica</a> in the <i>Amazon DynamoDB Developer Guide</i>.</p>"""


# --- awsJson1_0 ser/de ---
def serialize_aws_json_1_0(value: DisassociateReplicationGroupMemberAction) -> dict:
    out: dict = {}
    out["RegionName"] = value["region_name"]
    import capo_dynamodb.types.disassociation_mode

    out["DisassociationMode"] = (
        capo_dynamodb.types.disassociation_mode.serialize_aws_json_1_0(
            value["disassociation_mode"]
        )
    )
    return out


def deserialize_aws_json_1_0(data: dict) -> DisassociateReplicationGroupMemberAction:
    out: DisassociateReplicationGroupMemberAction = {}  # type: ignore[typeddict-item]
    if data.get("RegionName") is not None:
        out["region_name"] = data["RegionName"]
    else:
        out["region_name"] = ""
    if data.get("DisassociationMode") is not None:
        import capo_dynamodb.types.disassociation_mode

        out["disassociation_mode"] = (
            capo_dynamodb.types.disassociation_mode.deserialize_aws_json_1_0(
                data["DisassociationMode"]
            )
        )
    else:
        import typing

        out["disassociation_mode"] = typing.cast(
            "capo_dynamodb.types.disassociation_mode.DisassociationMode", ""
        )
    return out
