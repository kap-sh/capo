"""Generated from Smithy shape ``com.amazonaws.mturk#UpdateExpirationForHITRequest``."""

from typing import TYPE_CHECKING

from typing_extensions import TypedDict

if TYPE_CHECKING:
    import capo_mturk.types.entity_id
    import capo_mturk.types.timestamp


class UpdateExpirationForHITRequest(TypedDict, closed=True):
    hit_id: "capo_mturk.types.entity_id.EntityId"
    """<p> The HIT to update. </p>"""
    expire_at: "capo_mturk.types.timestamp.Timestamp"
    """<p> The date and time at which you want the HIT to expire </p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: UpdateExpirationForHITRequest) -> dict:
    out: dict = {}
    out["HITId"] = value["hit_id"]
    import capo_mturk.types.timestamp

    out["ExpireAt"] = capo_mturk.types.timestamp.serialize_aws_json_1_1(
        value["expire_at"]
    )
    return out


def deserialize_aws_json_1_1(data: dict) -> UpdateExpirationForHITRequest:
    out: UpdateExpirationForHITRequest = {}  # type: ignore[typeddict-item]
    if data.get("HITId") is not None:
        out["hit_id"] = data["HITId"]
    else:
        out["hit_id"] = ""
    if data.get("ExpireAt") is not None:
        import capo_mturk.types.timestamp

        out["expire_at"] = capo_mturk.types.timestamp.deserialize_aws_json_1_1(
            data["ExpireAt"]
        )
    else:
        import datetime

        out["expire_at"] = datetime.datetime.fromtimestamp(0, tz=datetime.timezone.utc)
    return out
