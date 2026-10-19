"""Generated from Smithy shape ``com.amazonaws.shield#ProtectionLimits``."""

from typing import TYPE_CHECKING

from typing_extensions import TypedDict

if TYPE_CHECKING:
    import capo_shield.types.limits


class ProtectionLimits(TypedDict, closed=True):
    protected_resource_type_limits: "capo_shield.types.limits.Limits"
    """<p>The maximum number of resource types that you can specify in a protection.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: ProtectionLimits) -> dict:
    out: dict = {}
    import capo_shield.types.limits

    out["ProtectedResourceTypeLimits"] = (
        capo_shield.types.limits.serialize_aws_json_1_1(
            value["protected_resource_type_limits"]
        )
    )
    return out


def deserialize_aws_json_1_1(data: dict) -> ProtectionLimits:
    out: ProtectionLimits = {}  # type: ignore[typeddict-item]
    if data.get("ProtectedResourceTypeLimits") is not None:
        import capo_shield.types.limits

        out["protected_resource_type_limits"] = (
            capo_shield.types.limits.deserialize_aws_json_1_1(
                data["ProtectedResourceTypeLimits"]
            )
        )
    else:
        out["protected_resource_type_limits"] = []
    return out
