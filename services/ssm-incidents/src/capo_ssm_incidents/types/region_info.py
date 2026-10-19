"""Generated from Smithy shape ``com.amazonaws.ssmincidents#RegionInfo``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import datetime

    import capo_ssm_incidents.types.region_status
    import capo_ssm_incidents.types.sse_kms_key


class RegionInfo(TypedDict, closed=True):
    sse_kms_key_id: NotRequired["capo_ssm_incidents.types.sse_kms_key.SseKmsKey"]
    """<p>The ID of the KMS key used to encrypt the data in this Amazon Web Services Region.</p>"""
    status: "capo_ssm_incidents.types.region_status.RegionStatus"
    """<p>The status of the Amazon Web Services Region in the replication set.</p>"""
    status_message: NotRequired["str"]
    """<p>Information displayed about the status of the Amazon Web Services Region.</p>"""
    status_update_date_time: "datetime.datetime"
    """<p>The timestamp for when Incident Manager updated the status of the Amazon Web Services Region.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: RegionInfo) -> dict:
    out: dict = {}
    if "sse_kms_key_id" in value:
        out["sseKmsKeyId"] = value["sse_kms_key_id"]
    out["status"] = value["status"]
    if "status_message" in value:
        out["statusMessage"] = value["status_message"]
    import capo_ssm_incidents.types._prelude.timestamp

    out["statusUpdateDateTime"] = (
        capo_ssm_incidents.types._prelude.timestamp.serialize_json(
            value["status_update_date_time"]
        )
    )
    return out


def deserialize_json(data: dict) -> RegionInfo:
    out: RegionInfo = {}  # type: ignore[typeddict-item]
    if data.get("sseKmsKeyId") is not None:
        out["sse_kms_key_id"] = data["sseKmsKeyId"]
    if data.get("status") is not None:
        out["status"] = data["status"]
    else:
        out["status"] = ""
    if data.get("statusMessage") is not None:
        out["status_message"] = data["statusMessage"]
    if data.get("statusUpdateDateTime") is not None:
        import capo_ssm_incidents.types._prelude.timestamp

        out["status_update_date_time"] = (
            capo_ssm_incidents.types._prelude.timestamp.deserialize_json(
                data["statusUpdateDateTime"]
            )
        )
    else:
        import datetime

        out["status_update_date_time"] = datetime.datetime.fromtimestamp(
            0, tz=datetime.timezone.utc
        )
    return out
