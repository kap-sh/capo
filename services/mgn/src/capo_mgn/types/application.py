"""Generated from Smithy shape ``com.amazonaws.mgn#Application``."""

from typing import TYPE_CHECKING, Any

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_mgn.types.application_aggregated_status
    import capo_mgn.types.application_description
    import capo_mgn.types.application_id
    import capo_mgn.types.application_name
    import capo_mgn.types.arn
    import capo_mgn.types.iso8601_datetime_string
    import capo_mgn.types.tags_map
    import capo_mgn.types.wave_id


class Application(TypedDict, closed=True):
    application_id: NotRequired["capo_mgn.types.application_id.ApplicationID"]
    """<p>Application ID.</p>"""
    arn: NotRequired["capo_mgn.types.arn.ARN"]
    """<p>Application ARN.</p>"""
    name: NotRequired["capo_mgn.types.application_name.ApplicationName"]
    """<p>Application name.</p>"""
    description: NotRequired[
        "capo_mgn.types.application_description.ApplicationDescription"
    ]
    """<p>Application description.</p>"""
    is_archived: NotRequired["bool"]
    """<p>Application archival status.</p>"""
    application_aggregated_status: NotRequired[
        "capo_mgn.types.application_aggregated_status.ApplicationAggregatedStatus"
    ]
    """<p>Application aggregated status.</p>"""
    creation_date_time: NotRequired[
        "capo_mgn.types.iso8601_datetime_string.ISO8601DatetimeString"
    ]
    """<p>Application creation dateTime.</p>"""
    last_modified_date_time: NotRequired[
        "capo_mgn.types.iso8601_datetime_string.ISO8601DatetimeString"
    ]
    """<p>Application last modified dateTime.</p>"""
    tags: NotRequired["capo_mgn.types.tags_map.TagsMap"]
    """<p>Application tags.</p>"""
    wave_id: NotRequired["capo_mgn.types.wave_id.WaveID"]
    """<p>Application wave ID.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: Application) -> dict:
    out: dict = {}
    if "application_id" in value:
        out["applicationID"] = value["application_id"]
    if "arn" in value:
        out["arn"] = value["arn"]
    if "name" in value:
        out["name"] = value["name"]
    if "description" in value:
        out["description"] = value["description"]
    if "is_archived" in value:
        out["isArchived"] = value["is_archived"]
    if "application_aggregated_status" in value:
        import capo_mgn.types.application_aggregated_status

        out["applicationAggregatedStatus"] = (
            capo_mgn.types.application_aggregated_status.serialize_json(
                value["application_aggregated_status"]
            )
        )
    if "creation_date_time" in value:
        out["creationDateTime"] = value["creation_date_time"]
    if "last_modified_date_time" in value:
        out["lastModifiedDateTime"] = value["last_modified_date_time"]
    if "tags" in value:
        import capo_mgn.types.tags_map

        out["tags"] = capo_mgn.types.tags_map.serialize_json(value["tags"])
    if "wave_id" in value:
        out["waveID"] = value["wave_id"]
    return out


def deserialize_json(data: dict) -> Application:
    out: Application = {}  # type: ignore[typeddict-item]
    if data.get("applicationID") is not None:
        out["application_id"] = data["applicationID"]
    if data.get("arn") is not None:
        out["arn"] = data["arn"]
    if data.get("name") is not None:
        out["name"] = data["name"]
    if data.get("description") is not None:
        out["description"] = data["description"]
    if data.get("isArchived") is not None:
        out["is_archived"] = data["isArchived"]
    if data.get("applicationAggregatedStatus") is not None:
        import capo_mgn.types.application_aggregated_status

        out["application_aggregated_status"] = (
            capo_mgn.types.application_aggregated_status.deserialize_json(
                data["applicationAggregatedStatus"]
            )
        )
    if data.get("creationDateTime") is not None:
        out["creation_date_time"] = data["creationDateTime"]
    if data.get("lastModifiedDateTime") is not None:
        out["last_modified_date_time"] = data["lastModifiedDateTime"]
    if data.get("tags") is not None:
        import capo_mgn.types.tags_map

        out["tags"] = capo_mgn.types.tags_map.deserialize_json(data["tags"])
    if data.get("waveID") is not None:
        out["wave_id"] = data["waveID"]
    return out


def redact_sensitive(value: Application) -> dict[str, Any]:
    out: dict[str, Any] = dict(value)
    if "tags" in value:
        out["tags"] = "*** Sensitive Data Redacted ***"
    return out
