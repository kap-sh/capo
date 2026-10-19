"""Generated from Smithy shape ``com.amazonaws.shield#DescribeAttackRequest``."""

from typing import TYPE_CHECKING

from typing_extensions import TypedDict

if TYPE_CHECKING:
    import capo_shield.types.attack_id


class DescribeAttackRequest(TypedDict, closed=True):
    attack_id: "capo_shield.types.attack_id.AttackId"
    """<p>The unique identifier (ID) for the attack.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: DescribeAttackRequest) -> dict:
    out: dict = {}
    out["AttackId"] = value["attack_id"]
    return out


def deserialize_aws_json_1_1(data: dict) -> DescribeAttackRequest:
    out: DescribeAttackRequest = {}  # type: ignore[typeddict-item]
    if data.get("AttackId") is not None:
        out["attack_id"] = data["AttackId"]
    else:
        out["attack_id"] = ""
    return out
