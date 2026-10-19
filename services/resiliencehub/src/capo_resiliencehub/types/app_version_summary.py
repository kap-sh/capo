"""Generated from Smithy shape ``com.amazonaws.resiliencehub#AppVersionSummary``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_resiliencehub.types.entity_version
    import capo_resiliencehub.types.long_optional
    import capo_resiliencehub.types.time_stamp


class AppVersionSummary(TypedDict, closed=True):
    app_version: "capo_resiliencehub.types.entity_version.EntityVersion"
    """<p>Version of an application.</p>"""
    identifier: NotRequired["capo_resiliencehub.types.long_optional.LongOptional"]
    """<p>Identifier of the application version.</p>"""
    creation_time: NotRequired["capo_resiliencehub.types.time_stamp.TimeStamp"]
    """<p>Creation time of the application version.</p>"""
    version_name: NotRequired["capo_resiliencehub.types.entity_version.EntityVersion"]
    """<p>Name of the application version.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: AppVersionSummary) -> dict:
    out: dict = {}
    out["appVersion"] = value["app_version"]
    if "identifier" in value:
        out["identifier"] = value["identifier"]
    if "creation_time" in value:
        import capo_resiliencehub.types.time_stamp

        out["creationTime"] = capo_resiliencehub.types.time_stamp.serialize_json(
            value["creation_time"]
        )
    if "version_name" in value:
        out["versionName"] = value["version_name"]
    return out


def deserialize_json(data: dict) -> AppVersionSummary:
    out: AppVersionSummary = {}  # type: ignore[typeddict-item]
    if data.get("appVersion") is not None:
        out["app_version"] = data["appVersion"]
    else:
        out["app_version"] = ""
    if data.get("identifier") is not None:
        out["identifier"] = data["identifier"]
    if data.get("creationTime") is not None:
        import capo_resiliencehub.types.time_stamp

        out["creation_time"] = capo_resiliencehub.types.time_stamp.deserialize_json(
            data["creationTime"]
        )
    if data.get("versionName") is not None:
        out["version_name"] = data["versionName"]
    return out
