"""Generated from Smithy shape ``com.amazonaws.pinpointsmsvoicev2#DeletePoolRequest``."""

from typing import TYPE_CHECKING

from typing_extensions import TypedDict

if TYPE_CHECKING:
    import capo_pinpoint_sms_voice_v2.types.pool_id_or_arn


class DeletePoolRequest(TypedDict, closed=True):
    pool_id: "capo_pinpoint_sms_voice_v2.types.pool_id_or_arn.PoolIdOrArn"
    """<p>The PoolId or PoolArn of the pool to delete. You can use <a>DescribePools</a> to find the values for PoolId and PoolArn .</p> <important> <p>If you are using a shared End User Messaging SMS resource then you must use the full Amazon Resource Name(ARN).</p> </important>"""


# --- awsJson1_0 ser/de ---
def serialize_aws_json_1_0(value: DeletePoolRequest) -> dict:
    out: dict = {}
    out["PoolId"] = value["pool_id"]
    return out


def deserialize_aws_json_1_0(data: dict) -> DeletePoolRequest:
    out: DeletePoolRequest = {}  # type: ignore[typeddict-item]
    if data.get("PoolId") is not None:
        out["pool_id"] = data["PoolId"]
    else:
        out["pool_id"] = ""
    return out
