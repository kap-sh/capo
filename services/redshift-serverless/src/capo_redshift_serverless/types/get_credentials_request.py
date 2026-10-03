"""Generated from Smithy shape ``com.amazonaws.redshiftserverless#GetCredentialsRequest``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_redshift_serverless.types.custom_domain_name
    import capo_redshift_serverless.types.db_name
    import capo_redshift_serverless.types.workgroup_name


class GetCredentialsRequest(TypedDict, closed=True):
    db_name: NotRequired["capo_redshift_serverless.types.db_name.DbName"]
    """<p>The name of the database to get temporary authorization to log on to.</p> <p>Constraints:</p> <ul> <li> <p>Must be 1 to 64 alphanumeric characters or hyphens.</p> </li> <li> <p>Must contain only uppercase or lowercase letters, numbers, underscore, plus sign, period (dot), at symbol (@), or hyphen.</p> </li> <li> <p>The first character must be a letter.</p> </li> <li> <p>Must not contain a colon ( : ) or slash ( / ).</p> </li> <li> <p>Cannot be a reserved word. A list of reserved words can be found in <a href="https://docs.aws.amazon.com/redshift/latest/dg/r_pg_keywords.html">Reserved Words </a> in the Amazon Redshift Database Developer Guide</p> </li> </ul>"""
    duration_seconds: NotRequired["int"]
    """<p>The number of seconds until the returned temporary password expires. The minimum is 900 seconds, and the maximum is 3600 seconds.</p>"""
    workgroup_name: NotRequired[
        "capo_redshift_serverless.types.workgroup_name.WorkgroupName"
    ]
    """<p>The name of the workgroup associated with the database.</p>"""
    custom_domain_name: NotRequired[
        "capo_redshift_serverless.types.custom_domain_name.CustomDomainName"
    ]
    """<p>The custom domain name associated with the workgroup. The custom domain name or the workgroup name must be included in the request.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: GetCredentialsRequest) -> dict:
    out: dict = {}
    if "db_name" in value:
        out["dbName"] = value["db_name"]
    if "duration_seconds" in value:
        out["durationSeconds"] = value["duration_seconds"]
    if "workgroup_name" in value:
        out["workgroupName"] = value["workgroup_name"]
    if "custom_domain_name" in value:
        out["customDomainName"] = value["custom_domain_name"]
    return out


def deserialize_aws_json_1_1(data: dict) -> GetCredentialsRequest:
    out: GetCredentialsRequest = {}  # type: ignore[typeddict-item]
    if data.get("dbName") is not None:
        out["db_name"] = data["dbName"]
    if data.get("durationSeconds") is not None:
        out["duration_seconds"] = data["durationSeconds"]
    if data.get("workgroupName") is not None:
        out["workgroup_name"] = data["workgroupName"]
    if data.get("customDomainName") is not None:
        out["custom_domain_name"] = data["customDomainName"]
    return out
