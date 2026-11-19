"""Generated from Smithy shape ``com.amazonaws.shield#ProtectionGroupPatternTypeLimits``."""

from typing import TYPE_CHECKING

from typing_extensions import TypedDict

from capo_shield.errors import DeserializationError

if TYPE_CHECKING:
    import capo_shield.types.protection_group_arbitrary_pattern_limits


class ProtectionGroupPatternTypeLimits(TypedDict, closed=True):
    arbitrary_pattern_limits: "capo_shield.types.protection_group_arbitrary_pattern_limits.ProtectionGroupArbitraryPatternLimits"
    """<p>Limits settings on protection groups with arbitrary pattern type. </p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: ProtectionGroupPatternTypeLimits) -> dict:
    out: dict = {}
    import capo_shield.types.protection_group_arbitrary_pattern_limits

    out["ArbitraryPatternLimits"] = (
        capo_shield.types.protection_group_arbitrary_pattern_limits.serialize_aws_json_1_1(
            value["arbitrary_pattern_limits"]
        )
    )
    return out


def deserialize_aws_json_1_1(data: dict) -> ProtectionGroupPatternTypeLimits:
    out: ProtectionGroupPatternTypeLimits = {}  # type: ignore[typeddict-item]
    if data.get("ArbitraryPatternLimits") is not None:
        import capo_shield.types.protection_group_arbitrary_pattern_limits

        out["arbitrary_pattern_limits"] = (
            capo_shield.types.protection_group_arbitrary_pattern_limits.deserialize_aws_json_1_1(
                data["ArbitraryPatternLimits"]
            )
        )
    else:
        raise DeserializationError(
            "ProtectionGroupPatternTypeLimits.arbitrary_pattern_limits required"
        )
    return out


# --- rpcv2Cbor ser/de ---
def serialize_cbor(value: ProtectionGroupPatternTypeLimits) -> dict:
    out: dict = {}
    import capo_shield.types.protection_group_arbitrary_pattern_limits

    out["ArbitraryPatternLimits"] = (
        capo_shield.types.protection_group_arbitrary_pattern_limits.serialize_cbor(
            value["arbitrary_pattern_limits"]
        )
    )
    return out


def deserialize_cbor(data: dict) -> ProtectionGroupPatternTypeLimits:
    out: ProtectionGroupPatternTypeLimits = {}  # type: ignore[typeddict-item]
    if data.get("ArbitraryPatternLimits") is not None:
        import capo_shield.types.protection_group_arbitrary_pattern_limits

        out["arbitrary_pattern_limits"] = (
            capo_shield.types.protection_group_arbitrary_pattern_limits.deserialize_cbor(
                data["ArbitraryPatternLimits"]
            )
        )
    else:
        raise DeserializationError(
            "ProtectionGroupPatternTypeLimits.arbitrary_pattern_limits required"
        )
    return out
