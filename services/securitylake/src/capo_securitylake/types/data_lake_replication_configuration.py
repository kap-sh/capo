"""Generated from Smithy shape ``com.amazonaws.securitylake#DataLakeReplicationConfiguration``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_securitylake.types.region_list
    import capo_securitylake.types.role_arn


class DataLakeReplicationConfiguration(TypedDict, closed=True):
    regions: NotRequired["capo_securitylake.types.region_list.RegionList"]
    """<p>Specifies one or more centralized rollup Regions. The Amazon Web Services Region specified in the <code>region</code> parameter of the <a href="https://docs.aws.amazon.com/security-lake/latest/APIReference/API_CreateDataLake.html"> <code>CreateDataLake</code> </a> or <a href="https://docs.aws.amazon.com/security-lake/latest/APIReference/API_UpdateDataLake.html"> <code>UpdateDataLake</code> </a> operations contributes data to the rollup Region or Regions specified in this parameter.</p> <p>Replication enables automatic, asynchronous copying of objects across Amazon S3 buckets. S3 buckets that are configured for object replication can be owned by the same Amazon Web Services account or by different accounts. You can replicate objects to a single destination bucket or to multiple destination buckets. The destination buckets can be in different Regions or within the same Region as the source bucket.</p>"""
    role_arn: NotRequired["capo_securitylake.types.role_arn.RoleArn"]
    """<p>Replication settings for the Amazon S3 buckets. This parameter uses the Identity and Access Management (IAM) role you created that is managed by Security Lake, to ensure the replication setting is correct.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: DataLakeReplicationConfiguration) -> dict:
    out: dict = {}
    if "regions" in value:
        import capo_securitylake.types.region_list

        out["regions"] = capo_securitylake.types.region_list.serialize_json(
            value["regions"]
        )
    if "role_arn" in value:
        out["roleArn"] = value["role_arn"]
    return out


def deserialize_json(data: dict) -> DataLakeReplicationConfiguration:
    out: DataLakeReplicationConfiguration = {}  # type: ignore[typeddict-item]
    if data.get("regions") is not None:
        import capo_securitylake.types.region_list

        out["regions"] = capo_securitylake.types.region_list.deserialize_json(
            data["regions"]
        )
    if data.get("roleArn") is not None:
        out["role_arn"] = data["roleArn"]
    return out
