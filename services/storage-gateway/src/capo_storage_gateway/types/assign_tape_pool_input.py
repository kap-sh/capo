"""Generated from Smithy shape ``com.amazonaws.storagegateway#AssignTapePoolInput``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_storage_gateway.types.boolean2
    import capo_storage_gateway.types.pool_id
    import capo_storage_gateway.types.tape_arn


class AssignTapePoolInput(TypedDict, closed=True):
    tape_arn: "capo_storage_gateway.types.tape_arn.TapeARN"
    """<p>The unique Amazon Resource Name (ARN) of the virtual tape that you want to add to the tape pool.</p>"""
    pool_id: "capo_storage_gateway.types.pool_id.PoolId"
    """<p>The ID of the pool that you want to add your tape to for archiving. The tape in this pool is archived in the S3 storage class that is associated with the pool. When you use your backup application to eject the tape, the tape is archived directly into the storage class (S3 Glacier or S3 Glacier Deep Archive) that corresponds to the pool.</p>"""
    bypass_governance_retention: NotRequired[
        "capo_storage_gateway.types.boolean2.Boolean2"
    ]
    """<p>Set permissions to bypass governance retention. If the lock type of the archived tape is <code>Governance</code>, the tape's archived age is not older than <code>RetentionLockInDays</code>, and the user does not already have <code>BypassGovernanceRetention</code>, setting this to TRUE enables the user to bypass the retention lock. This parameter is set to true by default for calls from the console.</p> <p>Valid values: <code>TRUE</code> | <code>FALSE</code> </p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: AssignTapePoolInput) -> dict:
    out: dict = {}
    out["TapeARN"] = value["tape_arn"]
    out["PoolId"] = value["pool_id"]
    if "bypass_governance_retention" in value:
        out["BypassGovernanceRetention"] = value["bypass_governance_retention"]
    return out


def deserialize_aws_json_1_1(data: dict) -> AssignTapePoolInput:
    out: AssignTapePoolInput = {}  # type: ignore[typeddict-item]
    if data.get("TapeARN") is not None:
        out["tape_arn"] = data["TapeARN"]
    else:
        out["tape_arn"] = ""
    if data.get("PoolId") is not None:
        out["pool_id"] = data["PoolId"]
    else:
        out["pool_id"] = ""
    if data.get("BypassGovernanceRetention") is not None:
        out["bypass_governance_retention"] = data["BypassGovernanceRetention"]
    return out
