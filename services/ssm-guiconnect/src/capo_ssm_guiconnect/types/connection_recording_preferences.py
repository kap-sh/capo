"""Generated from Smithy shape ``com.amazonaws.ssmguiconnect#ConnectionRecordingPreferences``."""

from typing import TYPE_CHECKING

from typing_extensions import TypedDict

from capo_ssm_guiconnect.errors import DeserializationError

if TYPE_CHECKING:
    import capo_ssm_guiconnect.types.recording_destinations


class ConnectionRecordingPreferences(TypedDict, closed=True):
    recording_destinations: (
        "capo_ssm_guiconnect.types.recording_destinations.RecordingDestinations"
    )
    """<p>Determines where recordings of RDP connections are stored.</p>"""
    kms_key_arn: "str"
    """<p>The ARN of a KMS key that is used to encrypt data while it is being processed by the service. This key must exist in the same Amazon Web Services Region as the node you start an RDP connection to.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: ConnectionRecordingPreferences) -> dict:
    out: dict = {}
    import capo_ssm_guiconnect.types.recording_destinations

    out["RecordingDestinations"] = (
        capo_ssm_guiconnect.types.recording_destinations.serialize_json(
            value["recording_destinations"]
        )
    )
    out["KMSKeyArn"] = value["kms_key_arn"]
    return out


def deserialize_json(data: dict) -> ConnectionRecordingPreferences:
    out: ConnectionRecordingPreferences = {}  # type: ignore[typeddict-item]
    if data.get("RecordingDestinations") is not None:
        import capo_ssm_guiconnect.types.recording_destinations

        out["recording_destinations"] = (
            capo_ssm_guiconnect.types.recording_destinations.deserialize_json(
                data["RecordingDestinations"]
            )
        )
    else:
        raise DeserializationError(
            "ConnectionRecordingPreferences.recording_destinations required"
        )
    if data.get("KMSKeyArn") is not None:
        out["kms_key_arn"] = data["KMSKeyArn"]
    else:
        out["kms_key_arn"] = ""
    return out
