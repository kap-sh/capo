"""Generated from Smithy shape ``com.amazonaws.pinpointemail#DedicatedIp``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_pinpoint_email.types.ip
    import capo_pinpoint_email.types.percentage100_wrapper
    import capo_pinpoint_email.types.pool_name
    import capo_pinpoint_email.types.warmup_status


class DedicatedIp(TypedDict, closed=True):
    ip: "capo_pinpoint_email.types.ip.Ip"
    """<p>An IP address that is reserved for use by your Amazon Pinpoint account.</p>"""
    warmup_status: "capo_pinpoint_email.types.warmup_status.WarmupStatus"
    """<p>The warm-up status of a dedicated IP address. The status can have one of the following values:</p> <ul> <li> <p> <code>IN_PROGRESS</code> – The IP address isn't ready to use because the dedicated IP warm-up process is ongoing.</p> </li> <li> <p> <code>DONE</code> – The dedicated IP warm-up process is complete, and the IP address is ready to use.</p> </li> </ul>"""
    warmup_percentage: (
        "capo_pinpoint_email.types.percentage100_wrapper.Percentage100Wrapper"
    )
    """<p>Indicates how complete the dedicated IP warm-up process is. When this value equals 1, the address has completed the warm-up process and is ready for use.</p>"""
    pool_name: NotRequired["capo_pinpoint_email.types.pool_name.PoolName"]
    """<p>The name of the dedicated IP pool that the IP address is associated with.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: DedicatedIp) -> dict:
    out: dict = {}
    out["Ip"] = value["ip"]
    import capo_pinpoint_email.types.warmup_status

    out["WarmupStatus"] = capo_pinpoint_email.types.warmup_status.serialize_json(
        value["warmup_status"]
    )
    out["WarmupPercentage"] = value["warmup_percentage"]
    if "pool_name" in value:
        out["PoolName"] = value["pool_name"]
    return out


def deserialize_json(data: dict) -> DedicatedIp:
    out: DedicatedIp = {}  # type: ignore[typeddict-item]
    if data.get("Ip") is not None:
        out["ip"] = data["Ip"]
    else:
        out["ip"] = ""
    if data.get("WarmupStatus") is not None:
        import capo_pinpoint_email.types.warmup_status

        out["warmup_status"] = capo_pinpoint_email.types.warmup_status.deserialize_json(
            data["WarmupStatus"]
        )
    else:
        import typing

        out["warmup_status"] = typing.cast(
            "capo_pinpoint_email.types.warmup_status.WarmupStatus", ""
        )
    if data.get("WarmupPercentage") is not None:
        out["warmup_percentage"] = data["WarmupPercentage"]
    else:
        out["warmup_percentage"] = 0
    if data.get("PoolName") is not None:
        out["pool_name"] = data["PoolName"]
    return out
