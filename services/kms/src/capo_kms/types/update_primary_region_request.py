"""Generated from Smithy shape ``com.amazonaws.kms#UpdatePrimaryRegionRequest``."""

from typing import TYPE_CHECKING

from typing_extensions import TypedDict

if TYPE_CHECKING:
    import capo_kms.types.key_id_type
    import capo_kms.types.region_type


class UpdatePrimaryRegionRequest(TypedDict, closed=True):
    key_id: "capo_kms.types.key_id_type.KeyIdType"
    """<p>Identifies the current primary key. When the operation completes, this KMS key will be a replica key.</p> <p>Specify the key ID or key ARN of a multi-Region primary key.</p> <p>For example:</p> <ul> <li> <p>Key ID: <code>mrk-1234abcd12ab34cd56ef1234567890ab</code> </p> </li> <li> <p>Key ARN: <code>arn:aws:kms:us-east-2:111122223333:key/mrk-1234abcd12ab34cd56ef1234567890ab</code> </p> </li> </ul> <p>To get the key ID and key ARN for a KMS key, use <a>ListKeys</a> or <a>DescribeKey</a>.</p>"""
    primary_region: "capo_kms.types.region_type.RegionType"
    """<p>The Amazon Web Services Region of the new primary key. Enter the Region ID, such as <code>us-east-1</code> or <code>ap-southeast-2</code>. There must be an existing replica key in this Region. </p> <p>When the operation completes, the multi-Region key in this Region will be the primary key.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: UpdatePrimaryRegionRequest) -> dict:
    out: dict = {}
    out["KeyId"] = value["key_id"]
    out["PrimaryRegion"] = value["primary_region"]
    return out


def deserialize_aws_json_1_1(data: dict) -> UpdatePrimaryRegionRequest:
    out: UpdatePrimaryRegionRequest = {}  # type: ignore[typeddict-item]
    if data.get("KeyId") is not None:
        out["key_id"] = data["KeyId"]
    else:
        out["key_id"] = ""
    if data.get("PrimaryRegion") is not None:
        out["primary_region"] = data["PrimaryRegion"]
    else:
        out["primary_region"] = ""
    return out
