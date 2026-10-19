"""Generated from Smithy shape ``com.amazonaws.omics#PutS3AccessPolicyRequest``."""

from typing import TYPE_CHECKING

from typing_extensions import TypedDict

if TYPE_CHECKING:
    import capo_omics.types.s3_access_point_arn
    import capo_omics.types.s3_access_policy


class PutS3AccessPolicyRequest(TypedDict, closed=True):
    s3_access_point_arn: "capo_omics.types.s3_access_point_arn.S3AccessPointArn"
    """<p>The S3 access point ARN where you want to put the access policy.</p>"""
    s3_access_policy: "capo_omics.types.s3_access_policy.S3AccessPolicy"
    """<p>The resource policy that controls S3 access to the store.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: PutS3AccessPolicyRequest) -> dict:
    out: dict = {}
    out["s3AccessPolicy"] = value["s3_access_policy"]
    return out


def deserialize_json(data: dict) -> PutS3AccessPolicyRequest:
    out: PutS3AccessPolicyRequest = {}  # type: ignore[typeddict-item]
    if data.get("s3AccessPolicy") is not None:
        out["s3_access_policy"] = data["s3AccessPolicy"]
    else:
        out["s3_access_policy"] = ""
    return out
