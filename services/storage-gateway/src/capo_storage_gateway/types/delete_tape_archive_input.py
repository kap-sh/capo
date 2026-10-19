"""Generated from Smithy shape ``com.amazonaws.storagegateway#DeleteTapeArchiveInput``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_storage_gateway.types.boolean2
    import capo_storage_gateway.types.tape_arn


class DeleteTapeArchiveInput(TypedDict, closed=True):
    tape_arn: "capo_storage_gateway.types.tape_arn.TapeARN"
    """<p>The Amazon Resource Name (ARN) of the virtual tape to delete from the virtual tape shelf (VTS).</p>"""
    bypass_governance_retention: NotRequired[
        "capo_storage_gateway.types.boolean2.Boolean2"
    ]
    """<p>Set to <code>TRUE</code> to delete an archived tape that belongs to a custom pool with tape retention lock. Only archived tapes with tape retention lock set to <code>governance</code> can be deleted. Archived tapes with tape retention lock set to <code>compliance</code> can't be deleted.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: DeleteTapeArchiveInput) -> dict:
    out: dict = {}
    out["TapeARN"] = value["tape_arn"]
    if "bypass_governance_retention" in value:
        out["BypassGovernanceRetention"] = value["bypass_governance_retention"]
    return out


def deserialize_aws_json_1_1(data: dict) -> DeleteTapeArchiveInput:
    out: DeleteTapeArchiveInput = {}  # type: ignore[typeddict-item]
    if data.get("TapeARN") is not None:
        out["tape_arn"] = data["TapeARN"]
    else:
        out["tape_arn"] = ""
    if data.get("BypassGovernanceRetention") is not None:
        out["bypass_governance_retention"] = data["BypassGovernanceRetention"]
    return out
