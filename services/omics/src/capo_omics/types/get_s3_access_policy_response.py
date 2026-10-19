"""Generated from Smithy shape ``com.amazonaws.omics#GetS3AccessPolicyResponse``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import datetime

    import capo_omics.types.s3_access_point_arn
    import capo_omics.types.s3_access_policy
    import capo_omics.types.store_id
    import capo_omics.types.store_type


class GetS3AccessPolicyResponse(TypedDict, closed=True):
    s3_access_point_arn: NotRequired[
        "capo_omics.types.s3_access_point_arn.S3AccessPointArn"
    ]
    """<p>The S3 access point ARN that has the access policy.</p>"""
    store_id: NotRequired["capo_omics.types.store_id.StoreId"]
    """<p>The Amazon Web Services-generated Sequence Store or Reference Store ID.</p>"""
    store_type: NotRequired["capo_omics.types.store_type.StoreType"]
    """<p>The type of store associated with the access point.</p>"""
    update_time: NotRequired["datetime.datetime"]
    """<p>The time when the policy was last updated.</p>"""
    s3_access_policy: "capo_omics.types.s3_access_policy.S3AccessPolicy"
    """<p>The current resource policy that controls S3 access on the store.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: GetS3AccessPolicyResponse) -> dict:
    out: dict = {}
    if "s3_access_point_arn" in value:
        out["s3AccessPointArn"] = value["s3_access_point_arn"]
    if "store_id" in value:
        out["storeId"] = value["store_id"]
    if "store_type" in value:
        import capo_omics.types.store_type

        out["storeType"] = capo_omics.types.store_type.serialize_json(
            value["store_type"]
        )
    if "update_time" in value:
        import capo_omics._protocol.serialize

        out["updateTime"] = capo_omics._protocol.serialize.fmt_date_time(
            value["update_time"]
        )
    out["s3AccessPolicy"] = value["s3_access_policy"]
    return out


def deserialize_json(data: dict) -> GetS3AccessPolicyResponse:
    out: GetS3AccessPolicyResponse = {}  # type: ignore[typeddict-item]
    if data.get("s3AccessPointArn") is not None:
        out["s3_access_point_arn"] = data["s3AccessPointArn"]
    if data.get("storeId") is not None:
        out["store_id"] = data["storeId"]
    if data.get("storeType") is not None:
        import capo_omics.types.store_type

        out["store_type"] = capo_omics.types.store_type.deserialize_json(
            data["storeType"]
        )
    if data.get("updateTime") is not None:
        import datetime

        out["update_time"] = datetime.datetime.fromisoformat(
            data["updateTime"].replace("Z", "+00:00")
        )
    if data.get("s3AccessPolicy") is not None:
        out["s3_access_policy"] = data["s3AccessPolicy"]
    else:
        out["s3_access_policy"] = ""
    return out
