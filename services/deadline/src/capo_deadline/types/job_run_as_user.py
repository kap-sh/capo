"""Generated from Smithy shape ``com.amazonaws.deadline#JobRunAsUser``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_deadline.types.posix_user
    import capo_deadline.types.run_as
    import capo_deadline.types.windows_user


class JobRunAsUser(TypedDict, closed=True):
    posix: NotRequired["capo_deadline.types.posix_user.PosixUser"]
    """<p>The user and group that the jobs in the queue run as.</p>"""
    windows: NotRequired["capo_deadline.types.windows_user.WindowsUser"]
    """<p>Identifies a Microsoft Windows user.</p>"""
    run_as: "capo_deadline.types.run_as.RunAs"
    """<p>Specifies whether the job should run using the queue's system user or if the job should run using the worker agent system user.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: JobRunAsUser) -> dict:
    out: dict = {}
    if "posix" in value:
        import capo_deadline.types.posix_user

        out["posix"] = capo_deadline.types.posix_user.serialize_json(value["posix"])
    if "windows" in value:
        import capo_deadline.types.windows_user

        out["windows"] = capo_deadline.types.windows_user.serialize_json(
            value["windows"]
        )
    import capo_deadline.types.run_as

    out["runAs"] = capo_deadline.types.run_as.serialize_json(value["run_as"])
    return out


def deserialize_json(data: dict) -> JobRunAsUser:
    out: JobRunAsUser = {}  # type: ignore[typeddict-item]
    if data.get("posix") is not None:
        import capo_deadline.types.posix_user

        out["posix"] = capo_deadline.types.posix_user.deserialize_json(data["posix"])
    if data.get("windows") is not None:
        import capo_deadline.types.windows_user

        out["windows"] = capo_deadline.types.windows_user.deserialize_json(
            data["windows"]
        )
    if data.get("runAs") is not None:
        import capo_deadline.types.run_as

        out["run_as"] = capo_deadline.types.run_as.deserialize_json(data["runAs"])
    else:
        import typing

        out["run_as"] = typing.cast("capo_deadline.types.run_as.RunAs", "")
    return out
