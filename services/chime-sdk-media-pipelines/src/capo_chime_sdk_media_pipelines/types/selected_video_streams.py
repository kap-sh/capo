"""Generated from Smithy shape ``com.amazonaws.chimesdkmediapipelines#SelectedVideoStreams``."""

from typing import TYPE_CHECKING, Any

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_chime_sdk_media_pipelines.types.attendee_id_list
    import capo_chime_sdk_media_pipelines.types.external_user_id_list


class SelectedVideoStreams(TypedDict, closed=True):
    attendee_ids: NotRequired[
        "capo_chime_sdk_media_pipelines.types.attendee_id_list.AttendeeIdList"
    ]
    """<p>The attendee IDs of the streams selected for a media pipeline. </p>"""
    external_user_ids: NotRequired[
        "capo_chime_sdk_media_pipelines.types.external_user_id_list.ExternalUserIdList"
    ]
    """<p>The external user IDs of the streams selected for a media pipeline.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: SelectedVideoStreams) -> dict:
    out: dict = {}
    if "attendee_ids" in value:
        import capo_chime_sdk_media_pipelines.types.attendee_id_list

        out["AttendeeIds"] = (
            capo_chime_sdk_media_pipelines.types.attendee_id_list.serialize_json(
                value["attendee_ids"]
            )
        )
    if "external_user_ids" in value:
        import capo_chime_sdk_media_pipelines.types.external_user_id_list

        out["ExternalUserIds"] = (
            capo_chime_sdk_media_pipelines.types.external_user_id_list.serialize_json(
                value["external_user_ids"]
            )
        )
    return out


def deserialize_json(data: dict) -> SelectedVideoStreams:
    out: SelectedVideoStreams = {}  # type: ignore[typeddict-item]
    if data.get("AttendeeIds") is not None:
        import capo_chime_sdk_media_pipelines.types.attendee_id_list

        out["attendee_ids"] = (
            capo_chime_sdk_media_pipelines.types.attendee_id_list.deserialize_json(
                data["AttendeeIds"]
            )
        )
    if data.get("ExternalUserIds") is not None:
        import capo_chime_sdk_media_pipelines.types.external_user_id_list

        out["external_user_ids"] = (
            capo_chime_sdk_media_pipelines.types.external_user_id_list.deserialize_json(
                data["ExternalUserIds"]
            )
        )
    return out


def redact_sensitive(value: SelectedVideoStreams) -> dict[str, Any]:
    out: dict[str, Any] = dict(value)
    if "external_user_ids" in value:
        import capo_chime_sdk_media_pipelines.types.external_user_id_list

        out["external_user_ids"] = (
            capo_chime_sdk_media_pipelines.types.external_user_id_list.redact_sensitive(
                value["external_user_ids"]
            )
        )
    return out
