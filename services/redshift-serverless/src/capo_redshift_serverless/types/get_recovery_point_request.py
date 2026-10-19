"""Generated from Smithy shape ``com.amazonaws.redshiftserverless#GetRecoveryPointRequest``."""

from typing_extensions import TypedDict


class GetRecoveryPointRequest(TypedDict, closed=True):
    recovery_point_id: "str"
    """<p>The unique identifier of the recovery point to return information for.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: GetRecoveryPointRequest) -> dict:
    out: dict = {}
    out["recoveryPointId"] = value["recovery_point_id"]
    return out


def deserialize_aws_json_1_1(data: dict) -> GetRecoveryPointRequest:
    out: GetRecoveryPointRequest = {}  # type: ignore[typeddict-item]
    if data.get("recoveryPointId") is not None:
        out["recovery_point_id"] = data["recoveryPointId"]
    else:
        out["recovery_point_id"] = ""
    return out
