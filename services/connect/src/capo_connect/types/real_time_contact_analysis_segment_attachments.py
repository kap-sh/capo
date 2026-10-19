"""Generated from Smithy shape ``com.amazonaws.connect#RealTimeContactAnalysisSegmentAttachments``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_connect.types.display_name
    import capo_connect.types.participant_id
    import capo_connect.types.participant_role
    import capo_connect.types.real_time_contact_analysis_attachments
    import capo_connect.types.real_time_contact_analysis_id256
    import capo_connect.types.real_time_contact_analysis_time_data


class RealTimeContactAnalysisSegmentAttachments(TypedDict, closed=True):
    id: "capo_connect.types.real_time_contact_analysis_id256.RealTimeContactAnalysisId256"
    """<p>The identifier of the segment.</p>"""
    participant_id: "capo_connect.types.participant_id.ParticipantId"
    """<p>The identifier of the participant.</p>"""
    participant_role: "capo_connect.types.participant_role.ParticipantRole"
    """<p>The role of the participant. For example, is it a customer, agent, or system.</p>"""
    display_name: NotRequired["capo_connect.types.display_name.DisplayName"]
    """<p>The display name of the participant. Can be redacted. </p>"""
    attachments: "capo_connect.types.real_time_contact_analysis_attachments.RealTimeContactAnalysisAttachments"
    """<p>List of objects describing an individual attachment.</p>"""
    time: "capo_connect.types.real_time_contact_analysis_time_data.RealTimeContactAnalysisTimeData"
    """<p>Field describing the time of the event. It can have different representations of time.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: RealTimeContactAnalysisSegmentAttachments) -> dict:
    out: dict = {}
    out["Id"] = value["id"]
    out["ParticipantId"] = value["participant_id"]
    import capo_connect.types.participant_role

    out["ParticipantRole"] = capo_connect.types.participant_role.serialize_json(
        value["participant_role"]
    )
    if "display_name" in value:
        out["DisplayName"] = value["display_name"]
    import capo_connect.types.real_time_contact_analysis_attachments

    out["Attachments"] = (
        capo_connect.types.real_time_contact_analysis_attachments.serialize_json(
            value["attachments"]
        )
    )
    import capo_connect.types.real_time_contact_analysis_time_data

    out["Time"] = (
        capo_connect.types.real_time_contact_analysis_time_data.serialize_json(
            value["time"]
        )
    )
    return out


def deserialize_json(data: dict) -> RealTimeContactAnalysisSegmentAttachments:
    out: RealTimeContactAnalysisSegmentAttachments = {}  # type: ignore[typeddict-item]
    if data.get("Id") is not None:
        out["id"] = data["Id"]
    else:
        out["id"] = ""
    if data.get("ParticipantId") is not None:
        out["participant_id"] = data["ParticipantId"]
    else:
        out["participant_id"] = ""
    if data.get("ParticipantRole") is not None:
        import capo_connect.types.participant_role

        out["participant_role"] = capo_connect.types.participant_role.deserialize_json(
            data["ParticipantRole"]
        )
    else:
        import typing

        out["participant_role"] = typing.cast(
            "capo_connect.types.participant_role.ParticipantRole", ""
        )
    if data.get("DisplayName") is not None:
        out["display_name"] = data["DisplayName"]
    if data.get("Attachments") is not None:
        import capo_connect.types.real_time_contact_analysis_attachments

        out["attachments"] = (
            capo_connect.types.real_time_contact_analysis_attachments.deserialize_json(
                data["Attachments"]
            )
        )
    else:
        out["attachments"] = []
    if data.get("Time") is not None:
        import capo_connect.types.real_time_contact_analysis_time_data

        out["time"] = (
            capo_connect.types.real_time_contact_analysis_time_data.deserialize_json(
                data["Time"]
            )
        )
    else:
        import capo_connect.types._unknown

        out["time"] = capo_connect.types._unknown.UnknownUnionMember("")
    return out
