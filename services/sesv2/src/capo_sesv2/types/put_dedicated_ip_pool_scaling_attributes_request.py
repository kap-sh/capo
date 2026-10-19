"""Generated from Smithy shape ``com.amazonaws.sesv2#PutDedicatedIpPoolScalingAttributesRequest``."""

from typing import TYPE_CHECKING

from typing_extensions import TypedDict

if TYPE_CHECKING:
    import capo_sesv2.types.pool_name
    import capo_sesv2.types.scaling_mode


class PutDedicatedIpPoolScalingAttributesRequest(TypedDict, closed=True):
    pool_name: "capo_sesv2.types.pool_name.PoolName"
    """<p>The name of the dedicated IP pool.</p>"""
    scaling_mode: "capo_sesv2.types.scaling_mode.ScalingMode"
    """<p>The scaling mode to apply to the dedicated IP pool.</p> <note> <p>Changing the scaling mode from <code>MANAGED</code> to <code>STANDARD</code> is not supported.</p> </note>"""


# --- restJson1 ser/de ---
def serialize_json(value: PutDedicatedIpPoolScalingAttributesRequest) -> dict:
    out: dict = {}
    import capo_sesv2.types.scaling_mode

    out["ScalingMode"] = capo_sesv2.types.scaling_mode.serialize_json(
        value["scaling_mode"]
    )
    return out


def deserialize_json(data: dict) -> PutDedicatedIpPoolScalingAttributesRequest:
    out: PutDedicatedIpPoolScalingAttributesRequest = {}  # type: ignore[typeddict-item]
    if data.get("ScalingMode") is not None:
        import capo_sesv2.types.scaling_mode

        out["scaling_mode"] = capo_sesv2.types.scaling_mode.deserialize_json(
            data["ScalingMode"]
        )
    else:
        import typing

        out["scaling_mode"] = typing.cast(
            "capo_sesv2.types.scaling_mode.ScalingMode", ""
        )
    return out
