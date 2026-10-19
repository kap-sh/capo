"""Generated from Smithy shape ``com.amazonaws.databasemigrationservice#ElasticsearchSettings``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_database_migration_service.types.boolean_optional
    import capo_database_migration_service.types.integer_optional
    import capo_database_migration_service.types.string


class ElasticsearchSettings(TypedDict, closed=True):
    service_access_role_arn: "capo_database_migration_service.types.string.String"
    """<p>The Amazon Resource Name (ARN) used by the service to access the IAM role. The role must allow the <code>iam:PassRole</code> action.</p>"""
    endpoint_uri: "capo_database_migration_service.types.string.String"
    """<p>The endpoint for the OpenSearch cluster. DMS uses HTTPS if a transport protocol (http/https) is not specified.</p>"""
    full_load_error_percentage: NotRequired[
        "capo_database_migration_service.types.integer_optional.IntegerOptional"
    ]
    """<p>The maximum percentage of records that can fail to be written before a full load operation stops.</p> <p>To avoid early failure, this counter is only effective after 1000 records are transferred. OpenSearch also has the concept of error monitoring during the last 10 minutes of an Observation Window. If transfer of all records fail in the last 10 minutes, the full load operation stops. </p>"""
    error_retry_duration: NotRequired[
        "capo_database_migration_service.types.integer_optional.IntegerOptional"
    ]
    """<p>The maximum number of seconds for which DMS retries failed API requests to the OpenSearch cluster.</p>"""
    use_new_mapping_type: NotRequired[
        "capo_database_migration_service.types.boolean_optional.BooleanOptional"
    ]
    """<p>Set this option to <code>true</code> for DMS to migrate documentation using the documentation type <code>_doc</code>. OpenSearch and an Elasticsearch cluster only support the _doc documentation type in versions 7. x and later. The default value is <code>false</code>.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: ElasticsearchSettings) -> dict:
    out: dict = {}
    out["ServiceAccessRoleArn"] = value["service_access_role_arn"]
    out["EndpointUri"] = value["endpoint_uri"]
    if "full_load_error_percentage" in value:
        out["FullLoadErrorPercentage"] = value["full_load_error_percentage"]
    if "error_retry_duration" in value:
        out["ErrorRetryDuration"] = value["error_retry_duration"]
    if "use_new_mapping_type" in value:
        out["UseNewMappingType"] = value["use_new_mapping_type"]
    return out


def deserialize_aws_json_1_1(data: dict) -> ElasticsearchSettings:
    out: ElasticsearchSettings = {}  # type: ignore[typeddict-item]
    if data.get("ServiceAccessRoleArn") is not None:
        out["service_access_role_arn"] = data["ServiceAccessRoleArn"]
    else:
        out["service_access_role_arn"] = ""
    if data.get("EndpointUri") is not None:
        out["endpoint_uri"] = data["EndpointUri"]
    else:
        out["endpoint_uri"] = ""
    if data.get("FullLoadErrorPercentage") is not None:
        out["full_load_error_percentage"] = data["FullLoadErrorPercentage"]
    if data.get("ErrorRetryDuration") is not None:
        out["error_retry_duration"] = data["ErrorRetryDuration"]
    if data.get("UseNewMappingType") is not None:
        out["use_new_mapping_type"] = data["UseNewMappingType"]
    return out
