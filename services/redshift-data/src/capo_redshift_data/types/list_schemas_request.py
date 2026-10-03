"""Generated from Smithy shape ``com.amazonaws.redshiftdata#ListSchemasRequest``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

from capo_redshift_data.errors import DeserializationError

if TYPE_CHECKING:
    import capo_redshift_data.types.cluster_identifier_string
    import capo_redshift_data.types.page_size
    import capo_redshift_data.types.secret_arn
    import capo_redshift_data.types.string
    import capo_redshift_data.types.workgroup_name_string


class ListSchemasRequest(TypedDict, closed=True):
    cluster_identifier: NotRequired[
        "capo_redshift_data.types.cluster_identifier_string.ClusterIdentifierString"
    ]
    """<p>The cluster identifier. This parameter is required when connecting to a cluster and authenticating using either Secrets Manager or temporary credentials. </p>"""
    secret_arn: NotRequired["capo_redshift_data.types.secret_arn.SecretArn"]
    """<p>The name or ARN of the secret that enables access to the database. This parameter is required when authenticating using Secrets Manager. </p>"""
    db_user: NotRequired["capo_redshift_data.types.string.String"]
    """<p>The database user name. This parameter is required when connecting to a cluster as a database user and authenticating using temporary credentials. </p>"""
    database: "capo_redshift_data.types.string.String"
    """<p>The name of the database that contains the schemas to list. If <code>ConnectedDatabase</code> is not specified, this is also the database to connect to with your authentication credentials.</p>"""
    connected_database: NotRequired["capo_redshift_data.types.string.String"]
    """<p>A database name. The connected database is specified when you connect with your authentication credentials. </p>"""
    schema_pattern: NotRequired["capo_redshift_data.types.string.String"]
    """<p>A pattern to filter results by schema name. Within a schema pattern, "%" means match any substring of 0 or more characters and "_" means match any one character. Only schema name entries matching the search pattern are returned. </p>"""
    next_token: NotRequired["capo_redshift_data.types.string.String"]
    """<p>A value that indicates the starting point for the next set of response records in a subsequent request. If a value is returned in a response, you can retrieve the next set of records by providing this returned NextToken value in the next NextToken parameter and retrying the command. If the NextToken field is empty, all response records have been retrieved for the request. </p>"""
    max_results: "capo_redshift_data.types.page_size.PageSize"
    """<p>The maximum number of schemas to return in the response. If more schemas exist than fit in one response, then <code>NextToken</code> is returned to page through the results. </p>"""
    workgroup_name: NotRequired[
        "capo_redshift_data.types.workgroup_name_string.WorkgroupNameString"
    ]
    """<p>The serverless workgroup name or Amazon Resource Name (ARN). This parameter is required when connecting to a serverless workgroup and authenticating using either Secrets Manager or temporary credentials.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: ListSchemasRequest) -> dict:
    out: dict = {}
    if "cluster_identifier" in value:
        out["ClusterIdentifier"] = value["cluster_identifier"]
    if "secret_arn" in value:
        out["SecretArn"] = value["secret_arn"]
    if "db_user" in value:
        out["DbUser"] = value["db_user"]
    out["Database"] = value["database"]
    if "connected_database" in value:
        out["ConnectedDatabase"] = value["connected_database"]
    if "schema_pattern" in value:
        out["SchemaPattern"] = value["schema_pattern"]
    if "next_token" in value:
        out["NextToken"] = value["next_token"]
    out["MaxResults"] = value.get("max_results", 0)
    if "workgroup_name" in value:
        out["WorkgroupName"] = value["workgroup_name"]
    return out


def deserialize_aws_json_1_1(data: dict) -> ListSchemasRequest:
    out: ListSchemasRequest = {}  # type: ignore[typeddict-item]
    if data.get("ClusterIdentifier") is not None:
        out["cluster_identifier"] = data["ClusterIdentifier"]
    if data.get("SecretArn") is not None:
        out["secret_arn"] = data["SecretArn"]
    if data.get("DbUser") is not None:
        out["db_user"] = data["DbUser"]
    if data.get("Database") is not None:
        out["database"] = data["Database"]
    else:
        raise DeserializationError("ListSchemasRequest.database required")
    if data.get("ConnectedDatabase") is not None:
        out["connected_database"] = data["ConnectedDatabase"]
    if data.get("SchemaPattern") is not None:
        out["schema_pattern"] = data["SchemaPattern"]
    if data.get("NextToken") is not None:
        out["next_token"] = data["NextToken"]
    if data.get("MaxResults") is not None:
        out["max_results"] = data["MaxResults"]
    else:
        out["max_results"] = 0
    if data.get("WorkgroupName") is not None:
        out["workgroup_name"] = data["WorkgroupName"]
    return out
