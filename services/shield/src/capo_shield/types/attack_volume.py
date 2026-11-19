"""Generated from Smithy shape ``com.amazonaws.shield#AttackVolume``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_shield.types.attack_volume_statistics


class AttackVolume(TypedDict, closed=True):
    bits_per_second: NotRequired[
        "capo_shield.types.attack_volume_statistics.AttackVolumeStatistics"
    ]
    """<p>A statistics object that uses bits per second as the unit. This is included for network level attacks. </p>"""
    packets_per_second: NotRequired[
        "capo_shield.types.attack_volume_statistics.AttackVolumeStatistics"
    ]
    """<p>A statistics object that uses packets per second as the unit. This is included for network level attacks. </p>"""
    requests_per_second: NotRequired[
        "capo_shield.types.attack_volume_statistics.AttackVolumeStatistics"
    ]
    """<p>A statistics object that uses requests per second as the unit. This is included for application level attacks, and is only available for accounts that are subscribed to Shield Advanced.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: AttackVolume) -> dict:
    out: dict = {}
    if "bits_per_second" in value:
        import capo_shield.types.attack_volume_statistics

        out["BitsPerSecond"] = (
            capo_shield.types.attack_volume_statistics.serialize_aws_json_1_1(
                value["bits_per_second"]
            )
        )
    if "packets_per_second" in value:
        import capo_shield.types.attack_volume_statistics

        out["PacketsPerSecond"] = (
            capo_shield.types.attack_volume_statistics.serialize_aws_json_1_1(
                value["packets_per_second"]
            )
        )
    if "requests_per_second" in value:
        import capo_shield.types.attack_volume_statistics

        out["RequestsPerSecond"] = (
            capo_shield.types.attack_volume_statistics.serialize_aws_json_1_1(
                value["requests_per_second"]
            )
        )
    return out


def deserialize_aws_json_1_1(data: dict) -> AttackVolume:
    out: AttackVolume = {}  # type: ignore[typeddict-item]
    if data.get("BitsPerSecond") is not None:
        import capo_shield.types.attack_volume_statistics

        out["bits_per_second"] = (
            capo_shield.types.attack_volume_statistics.deserialize_aws_json_1_1(
                data["BitsPerSecond"]
            )
        )
    if data.get("PacketsPerSecond") is not None:
        import capo_shield.types.attack_volume_statistics

        out["packets_per_second"] = (
            capo_shield.types.attack_volume_statistics.deserialize_aws_json_1_1(
                data["PacketsPerSecond"]
            )
        )
    if data.get("RequestsPerSecond") is not None:
        import capo_shield.types.attack_volume_statistics

        out["requests_per_second"] = (
            capo_shield.types.attack_volume_statistics.deserialize_aws_json_1_1(
                data["RequestsPerSecond"]
            )
        )
    return out


# --- rpcv2Cbor ser/de ---
def serialize_cbor(value: AttackVolume) -> dict:
    out: dict = {}
    if "bits_per_second" in value:
        import capo_shield.types.attack_volume_statistics

        out["BitsPerSecond"] = (
            capo_shield.types.attack_volume_statistics.serialize_cbor(
                value["bits_per_second"]
            )
        )
    if "packets_per_second" in value:
        import capo_shield.types.attack_volume_statistics

        out["PacketsPerSecond"] = (
            capo_shield.types.attack_volume_statistics.serialize_cbor(
                value["packets_per_second"]
            )
        )
    if "requests_per_second" in value:
        import capo_shield.types.attack_volume_statistics

        out["RequestsPerSecond"] = (
            capo_shield.types.attack_volume_statistics.serialize_cbor(
                value["requests_per_second"]
            )
        )
    return out


def deserialize_cbor(data: dict) -> AttackVolume:
    out: AttackVolume = {}  # type: ignore[typeddict-item]
    if data.get("BitsPerSecond") is not None:
        import capo_shield.types.attack_volume_statistics

        out["bits_per_second"] = (
            capo_shield.types.attack_volume_statistics.deserialize_cbor(
                data["BitsPerSecond"]
            )
        )
    if data.get("PacketsPerSecond") is not None:
        import capo_shield.types.attack_volume_statistics

        out["packets_per_second"] = (
            capo_shield.types.attack_volume_statistics.deserialize_cbor(
                data["PacketsPerSecond"]
            )
        )
    if data.get("RequestsPerSecond") is not None:
        import capo_shield.types.attack_volume_statistics

        out["requests_per_second"] = (
            capo_shield.types.attack_volume_statistics.deserialize_cbor(
                data["RequestsPerSecond"]
            )
        )
    return out
