"""Generated from Smithy shape ``com.amazonaws.m2#ApplicationVersionSummary``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_m2.types.application_version_lifecycle
    import capo_m2.types.timestamp
    import capo_m2.types.version


class ApplicationVersionSummary(TypedDict, closed=True):
    application_version: "capo_m2.types.version.Version"
    """<p>The application version.</p>"""
    status: "capo_m2.types.application_version_lifecycle.ApplicationVersionLifecycle"
    """<p>The status of the application.</p>"""
    status_reason: NotRequired["str"]
    """<p>The reason for the reported status.</p>"""
    creation_time: "capo_m2.types.timestamp.Timestamp"
    """<p>The timestamp when the application version was created.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: ApplicationVersionSummary) -> dict:
    out: dict = {}
    out["applicationVersion"] = value["application_version"]
    out["status"] = value["status"]
    if "status_reason" in value:
        out["statusReason"] = value["status_reason"]
    import capo_m2.types.timestamp

    out["creationTime"] = capo_m2.types.timestamp.serialize_json(value["creation_time"])
    return out


def deserialize_json(data: dict) -> ApplicationVersionSummary:
    out: ApplicationVersionSummary = {}  # type: ignore[typeddict-item]
    if data.get("applicationVersion") is not None:
        out["application_version"] = data["applicationVersion"]
    else:
        out["application_version"] = 0
    if data.get("status") is not None:
        out["status"] = data["status"]
    else:
        out["status"] = ""
    if data.get("statusReason") is not None:
        out["status_reason"] = data["statusReason"]
    if data.get("creationTime") is not None:
        import capo_m2.types.timestamp

        out["creation_time"] = capo_m2.types.timestamp.deserialize_json(
            data["creationTime"]
        )
    else:
        import datetime

        out["creation_time"] = datetime.datetime.fromtimestamp(
            0, tz=datetime.timezone.utc
        )
    return out
