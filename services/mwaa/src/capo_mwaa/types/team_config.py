"""Generated from Smithy shape ``com.amazonaws.mwaa#TeamConfig``."""

from typing import TYPE_CHECKING

from typing_extensions import TypedDict

if TYPE_CHECKING:
    import capo_mwaa.types.relative_path
    import capo_mwaa.types.s3_bucket_arn


class TeamConfig(TypedDict, closed=True):
    source_bucket_arn: "capo_mwaa.types.s3_bucket_arn.S3BucketArn"
    """<p>The Amazon Resource Name (ARN) of the Amazon S3 bucket where the team's DAG code and supporting files are stored. For example, <code>arn:aws:s3:::my-airflow-bucket-unique-name</code>. For more information, refer to <a href="https://docs.aws.amazon.com/mwaa/latest/userguide/mwaa-s3-bucket.html">Create an Amazon S3 bucket for Amazon MWAA</a>.</p>"""
    dag_s3_path: "capo_mwaa.types.relative_path.RelativePath"
    """<p>The relative path to the DAGs folder for the team in the team's Amazon S3 bucket. For example, <code>dags/team-a</code>. For more information, refer to <a href="https://docs.aws.amazon.com/mwaa/latest/userguide/configuring-dag-folder.html">Adding or updating DAGs</a>.</p> <p>DAG folders can't overlap. A team folder can't be inside the global folder or another team's folder, and the global folder can't be inside a team folder. Amazon Managed Workflows for Apache Airflow (Amazon MWAA) compares folder paths as Amazon S3 prefixes, so the trailing slash matters:</p> <ul> <li> <p> <code>s3://amzn-s3-demo-bucket/dags/</code> and <code>s3://amzn-s3-demo-bucket/dags/team-a/</code> overlap, because the first path is a prefix of the second.</p> </li> <li> <p> <code>s3://amzn-s3-demo-bucket/dags/</code> and <code>s3://amzn-s3-demo-bucket/dags-team-a/</code> don't overlap.</p> </li> <li> <p> <code>s3://amzn-s3-demo-bucket/teams/team-a/</code> and <code>s3://amzn-s3-demo-bucket/teams/team-b/</code> don't overlap.</p> </li> </ul>"""


# --- restJson1 ser/de ---
def serialize_json(value: TeamConfig) -> dict:
    out: dict = {}
    out["SourceBucketArn"] = value["source_bucket_arn"]
    out["DagS3Path"] = value["dag_s3_path"]
    return out


def deserialize_json(data: dict) -> TeamConfig:
    out: TeamConfig = {}  # type: ignore[typeddict-item]
    if data.get("SourceBucketArn") is not None:
        out["source_bucket_arn"] = data["SourceBucketArn"]
    else:
        out["source_bucket_arn"] = ""
    if data.get("DagS3Path") is not None:
        out["dag_s3_path"] = data["DagS3Path"]
    else:
        out["dag_s3_path"] = ""
    return out
