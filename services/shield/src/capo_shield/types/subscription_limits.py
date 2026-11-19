"""Generated from Smithy shape ``com.amazonaws.shield#SubscriptionLimits``."""

from typing import TYPE_CHECKING

from typing_extensions import TypedDict

from capo_shield.errors import DeserializationError

if TYPE_CHECKING:
    import capo_shield.types.protection_group_limits
    import capo_shield.types.protection_limits


class SubscriptionLimits(TypedDict, closed=True):
    protection_limits: "capo_shield.types.protection_limits.ProtectionLimits"
    """<p>Limits settings on protections for your subscription. </p>"""
    protection_group_limits: (
        "capo_shield.types.protection_group_limits.ProtectionGroupLimits"
    )
    """<p>Limits settings on protection groups for your subscription. </p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: SubscriptionLimits) -> dict:
    out: dict = {}
    import capo_shield.types.protection_limits

    out["ProtectionLimits"] = (
        capo_shield.types.protection_limits.serialize_aws_json_1_1(
            value["protection_limits"]
        )
    )
    import capo_shield.types.protection_group_limits

    out["ProtectionGroupLimits"] = (
        capo_shield.types.protection_group_limits.serialize_aws_json_1_1(
            value["protection_group_limits"]
        )
    )
    return out


def deserialize_aws_json_1_1(data: dict) -> SubscriptionLimits:
    out: SubscriptionLimits = {}  # type: ignore[typeddict-item]
    if data.get("ProtectionLimits") is not None:
        import capo_shield.types.protection_limits

        out["protection_limits"] = (
            capo_shield.types.protection_limits.deserialize_aws_json_1_1(
                data["ProtectionLimits"]
            )
        )
    else:
        raise DeserializationError("SubscriptionLimits.protection_limits required")
    if data.get("ProtectionGroupLimits") is not None:
        import capo_shield.types.protection_group_limits

        out["protection_group_limits"] = (
            capo_shield.types.protection_group_limits.deserialize_aws_json_1_1(
                data["ProtectionGroupLimits"]
            )
        )
    else:
        raise DeserializationError(
            "SubscriptionLimits.protection_group_limits required"
        )
    return out


# --- rpcv2Cbor ser/de ---
def serialize_cbor(value: SubscriptionLimits) -> dict:
    out: dict = {}
    import capo_shield.types.protection_limits

    out["ProtectionLimits"] = capo_shield.types.protection_limits.serialize_cbor(
        value["protection_limits"]
    )
    import capo_shield.types.protection_group_limits

    out["ProtectionGroupLimits"] = (
        capo_shield.types.protection_group_limits.serialize_cbor(
            value["protection_group_limits"]
        )
    )
    return out


def deserialize_cbor(data: dict) -> SubscriptionLimits:
    out: SubscriptionLimits = {}  # type: ignore[typeddict-item]
    if data.get("ProtectionLimits") is not None:
        import capo_shield.types.protection_limits

        out["protection_limits"] = capo_shield.types.protection_limits.deserialize_cbor(
            data["ProtectionLimits"]
        )
    else:
        raise DeserializationError("SubscriptionLimits.protection_limits required")
    if data.get("ProtectionGroupLimits") is not None:
        import capo_shield.types.protection_group_limits

        out["protection_group_limits"] = (
            capo_shield.types.protection_group_limits.deserialize_cbor(
                data["ProtectionGroupLimits"]
            )
        )
    else:
        raise DeserializationError(
            "SubscriptionLimits.protection_group_limits required"
        )
    return out
