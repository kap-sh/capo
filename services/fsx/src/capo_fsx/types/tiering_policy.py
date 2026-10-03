"""Generated from Smithy shape ``com.amazonaws.fsx#TieringPolicy``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_fsx.types.cooling_period
    import capo_fsx.types.tiering_policy_name


class TieringPolicy(TypedDict, closed=True):
    cooling_period: NotRequired["capo_fsx.types.cooling_period.CoolingPeriod"]
    """<p>Specifies the number of days that user data in a volume must remain inactive before it is considered "cold" and moved to the capacity pool. Used with the <code>AUTO</code> and <code>SNAPSHOT_ONLY</code> tiering policies. Enter a whole number between 2 and 183. Default values are 31 days for <code>AUTO</code> and 2 days for <code>SNAPSHOT_ONLY</code>.</p>"""
    name: NotRequired["capo_fsx.types.tiering_policy_name.TieringPolicyName"]
    """<p>Specifies the tiering policy used to transition data. Default value is <code>SNAPSHOT_ONLY</code>.</p> <ul> <li> <p> <code>SNAPSHOT_ONLY</code> - moves cold snapshots to the capacity pool storage tier.</p> </li> <li> <p> <code>AUTO</code> - moves cold user data and snapshots to the capacity pool storage tier based on your access patterns.</p> </li> <li> <p> <code>ALL</code> - moves all user data blocks in both the active file system and Snapshot copies to the storage pool tier.</p> </li> <li> <p> <code>NONE</code> - keeps a volume's data in the primary storage tier, preventing it from being moved to the capacity pool tier.</p> </li> </ul>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: TieringPolicy) -> dict:
    out: dict = {}
    if "cooling_period" in value:
        out["CoolingPeriod"] = value["cooling_period"]
    if "name" in value:
        import capo_fsx.types.tiering_policy_name

        out["Name"] = capo_fsx.types.tiering_policy_name.serialize_aws_json_1_1(
            value["name"]
        )
    return out


def deserialize_aws_json_1_1(data: dict) -> TieringPolicy:
    out: TieringPolicy = {}  # type: ignore[typeddict-item]
    if data.get("CoolingPeriod") is not None:
        out["cooling_period"] = data["CoolingPeriod"]
    if data.get("Name") is not None:
        import capo_fsx.types.tiering_policy_name

        out["name"] = capo_fsx.types.tiering_policy_name.deserialize_aws_json_1_1(
            data["Name"]
        )
    return out
