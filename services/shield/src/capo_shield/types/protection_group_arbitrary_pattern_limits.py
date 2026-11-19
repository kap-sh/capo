"""Generated from Smithy shape ``com.amazonaws.shield#ProtectionGroupArbitraryPatternLimits``."""

from typing import TYPE_CHECKING

from typing_extensions import TypedDict

if TYPE_CHECKING:
    import capo_shield.types.long


class ProtectionGroupArbitraryPatternLimits(TypedDict, closed=True):
    max_members: "capo_shield.types.long.Long"
    """<p>The maximum number of resources you can specify for a single arbitrary pattern in a protection group.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: ProtectionGroupArbitraryPatternLimits) -> dict:
    out: dict = {}
    out["MaxMembers"] = value.get("max_members", 0)
    return out


def deserialize_aws_json_1_1(data: dict) -> ProtectionGroupArbitraryPatternLimits:
    out: ProtectionGroupArbitraryPatternLimits = {}  # type: ignore[typeddict-item]
    if data.get("MaxMembers") is not None:
        out["max_members"] = data["MaxMembers"]
    else:
        out["max_members"] = 0
    return out


# --- rpcv2Cbor ser/de ---
def serialize_cbor(value: ProtectionGroupArbitraryPatternLimits) -> dict:
    out: dict = {}
    out["MaxMembers"] = value.get("max_members", 0)
    return out


def deserialize_cbor(data: dict) -> ProtectionGroupArbitraryPatternLimits:
    out: ProtectionGroupArbitraryPatternLimits = {}  # type: ignore[typeddict-item]
    if data.get("MaxMembers") is not None:
        out["max_members"] = data["MaxMembers"]
    else:
        out["max_members"] = 0
    return out
