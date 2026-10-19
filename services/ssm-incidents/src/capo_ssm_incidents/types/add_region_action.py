"""Generated from Smithy shape ``com.amazonaws.ssmincidents#AddRegionAction``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_ssm_incidents.types.region_name
    import capo_ssm_incidents.types.sse_kms_key


class AddRegionAction(TypedDict, closed=True):
    region_name: "capo_ssm_incidents.types.region_name.RegionName"
    """<p>The Amazon Web Services Region name to add to the replication set.</p>"""
    sse_kms_key_id: NotRequired["capo_ssm_incidents.types.sse_kms_key.SseKmsKey"]
    """<p>The KMS key ID to use to encrypt your replication set.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: AddRegionAction) -> dict:
    out: dict = {}
    out["regionName"] = value["region_name"]
    if "sse_kms_key_id" in value:
        out["sseKmsKeyId"] = value["sse_kms_key_id"]
    return out


def deserialize_json(data: dict) -> AddRegionAction:
    out: AddRegionAction = {}  # type: ignore[typeddict-item]
    if data.get("regionName") is not None:
        out["region_name"] = data["regionName"]
    else:
        out["region_name"] = ""
    if data.get("sseKmsKeyId") is not None:
        out["sse_kms_key_id"] = data["sseKmsKeyId"]
    return out
