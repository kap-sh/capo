"""Generated from Smithy shape ``com.amazonaws.inspector2#StopCisSessionMessage``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

from capo_inspector2.errors import DeserializationError

if TYPE_CHECKING:
    import capo_inspector2.types.benchmark_profile
    import capo_inspector2.types.benchmark_version
    import capo_inspector2.types.compute_platform
    import capo_inspector2.types.reason
    import capo_inspector2.types.stop_cis_message_progress
    import capo_inspector2.types.stop_cis_session_status


class StopCisSessionMessage(TypedDict, closed=True):
    status: "capo_inspector2.types.stop_cis_session_status.StopCisSessionStatus"
    """<p>The status of the message.</p>"""
    reason: NotRequired["capo_inspector2.types.reason.Reason"]
    """<p>The reason for the message.</p>"""
    progress: "capo_inspector2.types.stop_cis_message_progress.StopCisMessageProgress"
    """<p>The progress of the message.</p>"""
    compute_platform: NotRequired[
        "capo_inspector2.types.compute_platform.ComputePlatform"
    ]
    """<p>The message compute platform.</p>"""
    benchmark_version: NotRequired[
        "capo_inspector2.types.benchmark_version.BenchmarkVersion"
    ]
    """<p>The message benchmark version.</p>"""
    benchmark_profile: NotRequired[
        "capo_inspector2.types.benchmark_profile.BenchmarkProfile"
    ]
    """<p>The message benchmark profile.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: StopCisSessionMessage) -> dict:
    out: dict = {}
    import capo_inspector2.types.stop_cis_session_status

    out["status"] = capo_inspector2.types.stop_cis_session_status.serialize_json(
        value["status"]
    )
    if "reason" in value:
        out["reason"] = value["reason"]
    import capo_inspector2.types.stop_cis_message_progress

    out["progress"] = capo_inspector2.types.stop_cis_message_progress.serialize_json(
        value["progress"]
    )
    if "compute_platform" in value:
        import capo_inspector2.types.compute_platform

        out["computePlatform"] = capo_inspector2.types.compute_platform.serialize_json(
            value["compute_platform"]
        )
    if "benchmark_version" in value:
        out["benchmarkVersion"] = value["benchmark_version"]
    if "benchmark_profile" in value:
        out["benchmarkProfile"] = value["benchmark_profile"]
    return out


def deserialize_json(data: dict) -> StopCisSessionMessage:
    out: StopCisSessionMessage = {}  # type: ignore[typeddict-item]
    if data.get("status") is not None:
        import capo_inspector2.types.stop_cis_session_status

        out["status"] = capo_inspector2.types.stop_cis_session_status.deserialize_json(
            data["status"]
        )
    else:
        import typing

        out["status"] = typing.cast(
            "capo_inspector2.types.stop_cis_session_status.StopCisSessionStatus", ""
        )
    if data.get("reason") is not None:
        out["reason"] = data["reason"]
    if data.get("progress") is not None:
        import capo_inspector2.types.stop_cis_message_progress

        out["progress"] = (
            capo_inspector2.types.stop_cis_message_progress.deserialize_json(
                data["progress"]
            )
        )
    else:
        raise DeserializationError("StopCisSessionMessage.progress required")
    if data.get("computePlatform") is not None:
        import capo_inspector2.types.compute_platform

        out["compute_platform"] = (
            capo_inspector2.types.compute_platform.deserialize_json(
                data["computePlatform"]
            )
        )
    if data.get("benchmarkVersion") is not None:
        out["benchmark_version"] = data["benchmarkVersion"]
    if data.get("benchmarkProfile") is not None:
        out["benchmark_profile"] = data["benchmarkProfile"]
    return out
