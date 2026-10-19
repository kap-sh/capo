"""Generated from Smithy shape ``com.amazonaws.lambdamicrovms#IdlePolicy``."""

from typing_extensions import TypedDict


class IdlePolicy(TypedDict, closed=True):
    max_idle_duration_seconds: "int"
    """<p>The maximum time in seconds that a MicroVM can remain idle before it is automatically suspended.</p>"""
    suspended_duration_seconds: "int"
    """<p>The maximum time in seconds that a MicroVM can remain suspended before it is automatically terminated.</p>"""
    auto_resume_enabled: "bool"
    """<p>Indicates whether the MicroVM automatically resumes when it receives a request while suspended.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: IdlePolicy) -> dict:
    out: dict = {}
    out["maxIdleDurationSeconds"] = value["max_idle_duration_seconds"]
    out["suspendedDurationSeconds"] = value["suspended_duration_seconds"]
    out["autoResumeEnabled"] = value["auto_resume_enabled"]
    return out


def deserialize_json(data: dict) -> IdlePolicy:
    out: IdlePolicy = {}  # type: ignore[typeddict-item]
    if data.get("maxIdleDurationSeconds") is not None:
        out["max_idle_duration_seconds"] = data["maxIdleDurationSeconds"]
    else:
        out["max_idle_duration_seconds"] = 0
    if data.get("suspendedDurationSeconds") is not None:
        out["suspended_duration_seconds"] = data["suspendedDurationSeconds"]
    else:
        out["suspended_duration_seconds"] = 0
    if data.get("autoResumeEnabled") is not None:
        out["auto_resume_enabled"] = data["autoResumeEnabled"]
    else:
        out["auto_resume_enabled"] = False
    return out
