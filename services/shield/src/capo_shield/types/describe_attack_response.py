"""Generated from Smithy shape ``com.amazonaws.shield#DescribeAttackResponse``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_shield.types.attack_detail


class DescribeAttackResponse(TypedDict, closed=True):
    attack: NotRequired["capo_shield.types.attack_detail.AttackDetail"]
    """<p>The attack that you requested. </p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: DescribeAttackResponse) -> dict:
    out: dict = {}
    if "attack" in value:
        import capo_shield.types.attack_detail

        out["Attack"] = capo_shield.types.attack_detail.serialize_aws_json_1_1(
            value["attack"]
        )
    return out


def deserialize_aws_json_1_1(data: dict) -> DescribeAttackResponse:
    out: DescribeAttackResponse = {}  # type: ignore[typeddict-item]
    if data.get("Attack") is not None:
        import capo_shield.types.attack_detail

        out["attack"] = capo_shield.types.attack_detail.deserialize_aws_json_1_1(
            data["Attack"]
        )
    return out


# --- rpcv2Cbor ser/de ---
def serialize_cbor(value: DescribeAttackResponse) -> dict:
    out: dict = {}
    if "attack" in value:
        import capo_shield.types.attack_detail

        out["Attack"] = capo_shield.types.attack_detail.serialize_cbor(value["attack"])
    return out


def deserialize_cbor(data: dict) -> DescribeAttackResponse:
    out: DescribeAttackResponse = {}  # type: ignore[typeddict-item]
    if data.get("Attack") is not None:
        import capo_shield.types.attack_detail

        out["attack"] = capo_shield.types.attack_detail.deserialize_cbor(data["Attack"])
    return out
