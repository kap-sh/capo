"""Generated from Smithy shape ``com.amazonaws.shield#DescribeDRTAccessResponse``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_shield.types.log_bucket_list
    import capo_shield.types.role_arn


class DescribeDRTAccessResponse(TypedDict, closed=True):
    role_arn: NotRequired["capo_shield.types.role_arn.RoleArn"]
    """<p>The Amazon Resource Name (ARN) of the role the SRT used to access your Amazon Web Services account.</p>"""
    log_bucket_list: NotRequired["capo_shield.types.log_bucket_list.LogBucketList"]
    """<p>The list of Amazon S3 buckets accessed by the SRT.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: DescribeDRTAccessResponse) -> dict:
    out: dict = {}
    if "role_arn" in value:
        out["RoleArn"] = value["role_arn"]
    if "log_bucket_list" in value:
        import capo_shield.types.log_bucket_list

        out["LogBucketList"] = capo_shield.types.log_bucket_list.serialize_aws_json_1_1(
            value["log_bucket_list"]
        )
    return out


def deserialize_aws_json_1_1(data: dict) -> DescribeDRTAccessResponse:
    out: DescribeDRTAccessResponse = {}  # type: ignore[typeddict-item]
    if data.get("RoleArn") is not None:
        out["role_arn"] = data["RoleArn"]
    if data.get("LogBucketList") is not None:
        import capo_shield.types.log_bucket_list

        out["log_bucket_list"] = (
            capo_shield.types.log_bucket_list.deserialize_aws_json_1_1(
                data["LogBucketList"]
            )
        )
    return out


# --- rpcv2Cbor ser/de ---
def serialize_cbor(value: DescribeDRTAccessResponse) -> dict:
    out: dict = {}
    if "role_arn" in value:
        out["RoleArn"] = value["role_arn"]
    if "log_bucket_list" in value:
        import capo_shield.types.log_bucket_list

        out["LogBucketList"] = capo_shield.types.log_bucket_list.serialize_cbor(
            value["log_bucket_list"]
        )
    return out


def deserialize_cbor(data: dict) -> DescribeDRTAccessResponse:
    out: DescribeDRTAccessResponse = {}  # type: ignore[typeddict-item]
    if data.get("RoleArn") is not None:
        out["role_arn"] = data["RoleArn"]
    if data.get("LogBucketList") is not None:
        import capo_shield.types.log_bucket_list

        out["log_bucket_list"] = capo_shield.types.log_bucket_list.deserialize_cbor(
            data["LogBucketList"]
        )
    return out
