"""Generated from Smithy shape ``com.amazonaws.sesv2#DedicatedIpPool``."""

from typing import TYPE_CHECKING

from typing_extensions import TypedDict

if TYPE_CHECKING:
    import capo_sesv2.types.pool_name
    import capo_sesv2.types.scaling_mode


class DedicatedIpPool(TypedDict, closed=True):
    pool_name: "capo_sesv2.types.pool_name.PoolName"
    """<p>The name of the dedicated IP pool.</p>"""
    scaling_mode: "capo_sesv2.types.scaling_mode.ScalingMode"
    """<p>The type of the dedicated IP pool.</p> <ul> <li> <p> <code>STANDARD</code> – A dedicated IP pool where you can control which IPs are part of the pool.</p> </li> <li> <p> <code>MANAGED</code> – A dedicated IP pool where the reputation and number of IPs are automatically managed by Amazon SES.</p> </li> </ul>"""


# --- restJson1 ser/de ---
def serialize_json(value: DedicatedIpPool) -> dict:
    out: dict = {}
    out["PoolName"] = value["pool_name"]
    import capo_sesv2.types.scaling_mode

    out["ScalingMode"] = capo_sesv2.types.scaling_mode.serialize_json(
        value["scaling_mode"]
    )
    return out


def deserialize_json(data: dict) -> DedicatedIpPool:
    out: DedicatedIpPool = {}  # type: ignore[typeddict-item]
    if data.get("PoolName") is not None:
        out["pool_name"] = data["PoolName"]
    else:
        out["pool_name"] = ""
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
