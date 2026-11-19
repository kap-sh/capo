"""Generated from Smithy shape ``com.amazonaws.shield#AttackStatisticsDataItem``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_shield.types.attack_volume
    import capo_shield.types.long


class AttackStatisticsDataItem(TypedDict, closed=True):
    attack_volume: NotRequired["capo_shield.types.attack_volume.AttackVolume"]
    """<p>Information about the volume of attacks during the time period. If the accompanying <code>AttackCount</code> is zero, this setting might be empty.</p>"""
    attack_count: "capo_shield.types.long.Long"
    """<p>The number of attacks detected during the time period. This is always present, but might be zero. </p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: AttackStatisticsDataItem) -> dict:
    out: dict = {}
    if "attack_volume" in value:
        import capo_shield.types.attack_volume

        out["AttackVolume"] = capo_shield.types.attack_volume.serialize_aws_json_1_1(
            value["attack_volume"]
        )
    out["AttackCount"] = value.get("attack_count", 0)
    return out


def deserialize_aws_json_1_1(data: dict) -> AttackStatisticsDataItem:
    out: AttackStatisticsDataItem = {}  # type: ignore[typeddict-item]
    if data.get("AttackVolume") is not None:
        import capo_shield.types.attack_volume

        out["attack_volume"] = capo_shield.types.attack_volume.deserialize_aws_json_1_1(
            data["AttackVolume"]
        )
    if data.get("AttackCount") is not None:
        out["attack_count"] = data["AttackCount"]
    else:
        out["attack_count"] = 0
    return out


# --- rpcv2Cbor ser/de ---
def serialize_cbor(value: AttackStatisticsDataItem) -> dict:
    out: dict = {}
    if "attack_volume" in value:
        import capo_shield.types.attack_volume

        out["AttackVolume"] = capo_shield.types.attack_volume.serialize_cbor(
            value["attack_volume"]
        )
    out["AttackCount"] = value.get("attack_count", 0)
    return out


def deserialize_cbor(data: dict) -> AttackStatisticsDataItem:
    out: AttackStatisticsDataItem = {}  # type: ignore[typeddict-item]
    if data.get("AttackVolume") is not None:
        import capo_shield.types.attack_volume

        out["attack_volume"] = capo_shield.types.attack_volume.deserialize_cbor(
            data["AttackVolume"]
        )
    if data.get("AttackCount") is not None:
        out["attack_count"] = data["AttackCount"]
    else:
        out["attack_count"] = 0
    return out
