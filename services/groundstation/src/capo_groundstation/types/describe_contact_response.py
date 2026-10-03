"""Generated from Smithy shape ``com.amazonaws.groundstation#DescribeContactResponse``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import datetime

    import capo_groundstation.types.contact_status
    import capo_groundstation.types.contact_version
    import capo_groundstation.types.dataflow_list
    import capo_groundstation.types.elevation
    import capo_groundstation.types.ephemeris_response_data
    import capo_groundstation.types.mission_profile_arn
    import capo_groundstation.types.satellite_arn
    import capo_groundstation.types.tags_map
    import capo_groundstation.types.tracking_overrides
    import capo_groundstation.types.uuid


class DescribeContactResponse(TypedDict, closed=True):
    contact_id: NotRequired["capo_groundstation.types.uuid.Uuid"]
    """<p>UUID of a contact.</p>"""
    mission_profile_arn: NotRequired[
        "capo_groundstation.types.mission_profile_arn.MissionProfileArn"
    ]
    """<p>ARN of a mission profile.</p>"""
    satellite_arn: NotRequired["capo_groundstation.types.satellite_arn.satelliteArn"]
    """<p>ARN of a satellite.</p>"""
    start_time: NotRequired["datetime.datetime"]
    """<p>Start time of a contact in UTC.</p>"""
    end_time: NotRequired["datetime.datetime"]
    """<p>End time of a contact in UTC.</p>"""
    pre_pass_start_time: NotRequired["datetime.datetime"]
    """<p>Start time in UTC of the pre-pass period, at which you receive a CloudWatch event indicating an upcoming pass.</p>"""
    post_pass_end_time: NotRequired["datetime.datetime"]
    """<p>End time in UTC of the post-pass period, at which you receive a CloudWatch event indicating the pass has finished.</p>"""
    ground_station: NotRequired["str"]
    """<p>Ground station for a contact.</p>"""
    contact_status: NotRequired["capo_groundstation.types.contact_status.ContactStatus"]
    """<p>Status of a contact.</p>"""
    error_message: NotRequired["str"]
    """<p>Error message for a contact.</p>"""
    maximum_elevation: NotRequired["capo_groundstation.types.elevation.Elevation"]
    """<p>Maximum elevation angle of a contact.</p>"""
    tags: NotRequired["capo_groundstation.types.tags_map.TagsMap"]
    """<p>Tags assigned to a contact.</p>"""
    region: NotRequired["str"]
    """<p>Region where the <code>ReserveContact</code> API was called to schedule this contact.</p>"""
    dataflow_list: NotRequired["capo_groundstation.types.dataflow_list.DataflowList"]
    """<p>List describing source and destination details for each dataflow edge.</p>"""
    visibility_start_time: NotRequired["datetime.datetime"]
    """<p> Projected time in UTC your satellite will rise above the <a href="https://docs.aws.amazon.com/ground-station/latest/ug/site-masks.html">receive mask</a>. This time is based on the satellite's current active ephemeris for future contacts and the ephemeris that was active during contact execution for completed contacts.</p>"""
    visibility_end_time: NotRequired["datetime.datetime"]
    """<p> Projected time in UTC your satellite will set below the <a href="https://docs.aws.amazon.com/ground-station/latest/ug/site-masks.html">receive mask</a>. This time is based on the satellite's current active ephemeris for future contacts and the ephemeris that was active during contact execution for completed contacts.</p>"""
    tracking_overrides: NotRequired[
        "capo_groundstation.types.tracking_overrides.TrackingOverrides"
    ]
    """<p>Tracking configuration overrides specified when the contact was reserved.</p>"""
    ephemeris: NotRequired[
        "capo_groundstation.types.ephemeris_response_data.EphemerisResponseData"
    ]
    """<p>The ephemeris that determines antenna pointing directions for the contact.</p>"""
    version: NotRequired["capo_groundstation.types.contact_version.ContactVersion"]
    """<p>Version information for a contact.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: DescribeContactResponse) -> dict:
    out: dict = {}
    if "contact_id" in value:
        out["contactId"] = value["contact_id"]
    if "mission_profile_arn" in value:
        out["missionProfileArn"] = value["mission_profile_arn"]
    if "satellite_arn" in value:
        out["satelliteArn"] = value["satellite_arn"]
    if "start_time" in value:
        import capo_groundstation.types._prelude.timestamp

        out["startTime"] = capo_groundstation.types._prelude.timestamp.serialize_json(
            value["start_time"]
        )
    if "end_time" in value:
        import capo_groundstation.types._prelude.timestamp

        out["endTime"] = capo_groundstation.types._prelude.timestamp.serialize_json(
            value["end_time"]
        )
    if "pre_pass_start_time" in value:
        import capo_groundstation.types._prelude.timestamp

        out["prePassStartTime"] = (
            capo_groundstation.types._prelude.timestamp.serialize_json(
                value["pre_pass_start_time"]
            )
        )
    if "post_pass_end_time" in value:
        import capo_groundstation.types._prelude.timestamp

        out["postPassEndTime"] = (
            capo_groundstation.types._prelude.timestamp.serialize_json(
                value["post_pass_end_time"]
            )
        )
    if "ground_station" in value:
        out["groundStation"] = value["ground_station"]
    if "contact_status" in value:
        import capo_groundstation.types.contact_status

        out["contactStatus"] = capo_groundstation.types.contact_status.serialize_json(
            value["contact_status"]
        )
    if "error_message" in value:
        out["errorMessage"] = value["error_message"]
    if "maximum_elevation" in value:
        import capo_groundstation.types.elevation

        out["maximumElevation"] = capo_groundstation.types.elevation.serialize_json(
            value["maximum_elevation"]
        )
    if "tags" in value:
        import capo_groundstation.types.tags_map

        out["tags"] = capo_groundstation.types.tags_map.serialize_json(value["tags"])
    if "region" in value:
        out["region"] = value["region"]
    if "dataflow_list" in value:
        import capo_groundstation.types.dataflow_list

        out["dataflowList"] = capo_groundstation.types.dataflow_list.serialize_json(
            value["dataflow_list"]
        )
    if "visibility_start_time" in value:
        import capo_groundstation.types._prelude.timestamp

        out["visibilityStartTime"] = (
            capo_groundstation.types._prelude.timestamp.serialize_json(
                value["visibility_start_time"]
            )
        )
    if "visibility_end_time" in value:
        import capo_groundstation.types._prelude.timestamp

        out["visibilityEndTime"] = (
            capo_groundstation.types._prelude.timestamp.serialize_json(
                value["visibility_end_time"]
            )
        )
    if "tracking_overrides" in value:
        import capo_groundstation.types.tracking_overrides

        out["trackingOverrides"] = (
            capo_groundstation.types.tracking_overrides.serialize_json(
                value["tracking_overrides"]
            )
        )
    if "ephemeris" in value:
        import capo_groundstation.types.ephemeris_response_data

        out["ephemeris"] = (
            capo_groundstation.types.ephemeris_response_data.serialize_json(
                value["ephemeris"]
            )
        )
    if "version" in value:
        import capo_groundstation.types.contact_version

        out["version"] = capo_groundstation.types.contact_version.serialize_json(
            value["version"]
        )
    return out


def deserialize_json(data: dict) -> DescribeContactResponse:
    out: DescribeContactResponse = {}  # type: ignore[typeddict-item]
    if data.get("contactId") is not None:
        out["contact_id"] = data["contactId"]
    if data.get("missionProfileArn") is not None:
        out["mission_profile_arn"] = data["missionProfileArn"]
    if data.get("satelliteArn") is not None:
        out["satellite_arn"] = data["satelliteArn"]
    if data.get("startTime") is not None:
        import capo_groundstation.types._prelude.timestamp

        out["start_time"] = (
            capo_groundstation.types._prelude.timestamp.deserialize_json(
                data["startTime"]
            )
        )
    if data.get("endTime") is not None:
        import capo_groundstation.types._prelude.timestamp

        out["end_time"] = capo_groundstation.types._prelude.timestamp.deserialize_json(
            data["endTime"]
        )
    if data.get("prePassStartTime") is not None:
        import capo_groundstation.types._prelude.timestamp

        out["pre_pass_start_time"] = (
            capo_groundstation.types._prelude.timestamp.deserialize_json(
                data["prePassStartTime"]
            )
        )
    if data.get("postPassEndTime") is not None:
        import capo_groundstation.types._prelude.timestamp

        out["post_pass_end_time"] = (
            capo_groundstation.types._prelude.timestamp.deserialize_json(
                data["postPassEndTime"]
            )
        )
    if data.get("groundStation") is not None:
        out["ground_station"] = data["groundStation"]
    if data.get("contactStatus") is not None:
        import capo_groundstation.types.contact_status

        out["contact_status"] = (
            capo_groundstation.types.contact_status.deserialize_json(
                data["contactStatus"]
            )
        )
    if data.get("errorMessage") is not None:
        out["error_message"] = data["errorMessage"]
    if data.get("maximumElevation") is not None:
        import capo_groundstation.types.elevation

        out["maximum_elevation"] = capo_groundstation.types.elevation.deserialize_json(
            data["maximumElevation"]
        )
    if data.get("tags") is not None:
        import capo_groundstation.types.tags_map

        out["tags"] = capo_groundstation.types.tags_map.deserialize_json(data["tags"])
    if data.get("region") is not None:
        out["region"] = data["region"]
    if data.get("dataflowList") is not None:
        import capo_groundstation.types.dataflow_list

        out["dataflow_list"] = capo_groundstation.types.dataflow_list.deserialize_json(
            data["dataflowList"]
        )
    if data.get("visibilityStartTime") is not None:
        import capo_groundstation.types._prelude.timestamp

        out["visibility_start_time"] = (
            capo_groundstation.types._prelude.timestamp.deserialize_json(
                data["visibilityStartTime"]
            )
        )
    if data.get("visibilityEndTime") is not None:
        import capo_groundstation.types._prelude.timestamp

        out["visibility_end_time"] = (
            capo_groundstation.types._prelude.timestamp.deserialize_json(
                data["visibilityEndTime"]
            )
        )
    if data.get("trackingOverrides") is not None:
        import capo_groundstation.types.tracking_overrides

        out["tracking_overrides"] = (
            capo_groundstation.types.tracking_overrides.deserialize_json(
                data["trackingOverrides"]
            )
        )
    if data.get("ephemeris") is not None:
        import capo_groundstation.types.ephemeris_response_data

        out["ephemeris"] = (
            capo_groundstation.types.ephemeris_response_data.deserialize_json(
                data["ephemeris"]
            )
        )
    if data.get("version") is not None:
        import capo_groundstation.types.contact_version

        out["version"] = capo_groundstation.types.contact_version.deserialize_json(
            data["version"]
        )
    return out
