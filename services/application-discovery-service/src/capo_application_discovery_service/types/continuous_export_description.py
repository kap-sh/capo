"""Generated from Smithy shape ``com.amazonaws.applicationdiscoveryservice#ContinuousExportDescription``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_application_discovery_service.types.configurations_export_id
    import capo_application_discovery_service.types.continuous_export_status
    import capo_application_discovery_service.types.data_source
    import capo_application_discovery_service.types.s3_bucket
    import capo_application_discovery_service.types.schema_storage_config
    import capo_application_discovery_service.types.string_max255
    import capo_application_discovery_service.types.time_stamp


class ContinuousExportDescription(TypedDict, closed=True):
    export_id: NotRequired[
        "capo_application_discovery_service.types.configurations_export_id.ConfigurationsExportId"
    ]
    """<p>The unique ID assigned to this export.</p>"""
    status: NotRequired[
        "capo_application_discovery_service.types.continuous_export_status.ContinuousExportStatus"
    ]
    """<p>Describes the status of the export. Can be one of the following values:</p> <ul> <li> <p>START_IN_PROGRESS - setting up resources to start continuous export.</p> </li> <li> <p>START_FAILED - an error occurred setting up continuous export. To recover, call start-continuous-export again.</p> </li> <li> <p>ACTIVE - data is being exported to the customer bucket.</p> </li> <li> <p>ERROR - an error occurred during export. To fix the issue, call stop-continuous-export and start-continuous-export.</p> </li> <li> <p>STOP_IN_PROGRESS - stopping the export.</p> </li> <li> <p>STOP_FAILED - an error occurred stopping the export. To recover, call stop-continuous-export again.</p> </li> <li> <p>INACTIVE - the continuous export has been stopped. Data is no longer being exported to the customer bucket.</p> </li> </ul>"""
    status_detail: NotRequired[
        "capo_application_discovery_service.types.string_max255.StringMax255"
    ]
    """<p>Contains information about any errors that have occurred. This data type can have the following values:</p> <ul> <li> <p>ACCESS_DENIED - You don’t have permission to start Data Exploration in Amazon Athena. Contact your Amazon Web Services administrator for help. For more information, see <a href="http://docs.aws.amazon.com/application-discovery/latest/userguide/setting-up.html">Setting Up Amazon Web Services Application Discovery Service</a> in the Application Discovery Service User Guide.</p> </li> <li> <p>DELIVERY_STREAM_LIMIT_FAILURE - You reached the limit for Amazon Kinesis Data Firehose delivery streams. Reduce the number of streams or request a limit increase and try again. For more information, see <a href="http://docs.aws.amazon.com/streams/latest/dev/service-sizes-and-limits.html">Kinesis Data Streams Limits</a> in the Amazon Kinesis Data Streams Developer Guide.</p> </li> <li> <p>FIREHOSE_ROLE_MISSING - The Data Exploration feature is in an error state because your user is missing the Amazon Web ServicesApplicationDiscoveryServiceFirehose role. Turn on Data Exploration in Amazon Athena and try again. For more information, see <a href="https://docs.aws.amazon.com/application-discovery/latest/userguide/security-iam-awsmanpol.html#security-iam-awsmanpol-create-firehose-role">Creating the Amazon Web ServicesApplicationDiscoveryServiceFirehose Role</a> in the Application Discovery Service User Guide.</p> </li> <li> <p>FIREHOSE_STREAM_DOES_NOT_EXIST - The Data Exploration feature is in an error state because your user is missing one or more of the Kinesis data delivery streams.</p> </li> <li> <p>INTERNAL_FAILURE - The Data Exploration feature is in an error state because of an internal failure. Try again later. If this problem persists, contact Amazon Web Services Support.</p> </li> <li> <p>LAKE_FORMATION_ACCESS_DENIED - You don't have sufficient lake formation permissions to start continuous export. For more information, see <a href="http://docs.aws.amazon.com/lake-formation/latest/dg/upgrade-glue-lake-formation.html"> Upgrading Amazon Web Services Glue Data Permissions to the Amazon Web Services Lake Formation Model </a> in the Amazon Web Services <i>Lake Formation Developer Guide</i>. </p> <p>You can use one of the following two ways to resolve this issue.</p> <ol> <li> <p>If you don’t want to use the Lake Formation permission model, you can change the default Data Catalog settings to use only Amazon Web Services Identity and Access Management (IAM) access control for new databases. For more information, see <a href="https://docs.aws.amazon.com/lake-formation/latest/dg/getting-started-setup.html#setup-change-cat-settings">Change Data Catalog Settings</a> in the <i>Lake Formation Developer Guide</i>.</p> </li> <li> <p>You can give the service-linked IAM roles AWSServiceRoleForApplicationDiscoveryServiceContinuousExport and AWSApplicationDiscoveryServiceFirehose the required Lake Formation permissions. For more information, see <a href="https://docs.aws.amazon.com/lake-formation/latest/dg/granting-database-permissions.html"> Granting Database Permissions</a> in the <i>Lake Formation Developer Guide</i>. </p> <ol> <li> <p>AWSServiceRoleForApplicationDiscoveryServiceContinuousExport - Grant database creator permissions, which gives the role database creation ability and implicit permissions for any created tables. For more information, see <a href="https://docs.aws.amazon.com/lake-formation/latest/dg/implicit-permissions.html"> Implicit Lake Formation Permissions </a> in the <i>Lake Formation Developer Guide</i>.</p> </li> <li> <p>AWSApplicationDiscoveryServiceFirehose - Grant describe permissions for all tables in the database.</p> </li> </ol> </li> </ol> </li> <li> <p>S3_BUCKET_LIMIT_FAILURE - You reached the limit for Amazon S3 buckets. Reduce the number of S3 buckets or request a limit increase and try again. For more information, see <a href="http://docs.aws.amazon.com/AmazonS3/latest/dev/BucketRestrictions.html">Bucket Restrictions and Limitations</a> in the Amazon Simple Storage Service Developer Guide.</p> </li> <li> <p>S3_NOT_SIGNED_UP - Your account is not signed up for the Amazon S3 service. You must sign up before you can use Amazon S3. You can sign up at the following URL: <a href="https://aws.amazon.com/s3">https://aws.amazon.com/s3</a>.</p> </li> </ul>"""
    s3_bucket: NotRequired[
        "capo_application_discovery_service.types.s3_bucket.S3Bucket"
    ]
    """<p>The name of the s3 bucket where the export data parquet files are stored.</p>"""
    start_time: NotRequired[
        "capo_application_discovery_service.types.time_stamp.TimeStamp"
    ]
    """<p>The timestamp representing when the continuous export was started.</p>"""
    stop_time: NotRequired[
        "capo_application_discovery_service.types.time_stamp.TimeStamp"
    ]
    """<p>The timestamp that represents when this continuous export was stopped.</p>"""
    data_source: NotRequired[
        "capo_application_discovery_service.types.data_source.DataSource"
    ]
    """<p>The type of data collector used to gather this data (currently only offered for AGENT).</p>"""
    schema_storage_config: NotRequired[
        "capo_application_discovery_service.types.schema_storage_config.SchemaStorageConfig"
    ]
    """<p>An object which describes how the data is stored.</p> <ul> <li> <p> <code>databaseName</code> - the name of the Glue database used to store the schema.</p> </li> </ul>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: ContinuousExportDescription) -> dict:
    out: dict = {}
    if "export_id" in value:
        out["exportId"] = value["export_id"]
    if "status" in value:
        import capo_application_discovery_service.types.continuous_export_status

        out["status"] = (
            capo_application_discovery_service.types.continuous_export_status.serialize_aws_json_1_1(
                value["status"]
            )
        )
    if "status_detail" in value:
        out["statusDetail"] = value["status_detail"]
    if "s3_bucket" in value:
        out["s3Bucket"] = value["s3_bucket"]
    if "start_time" in value:
        import capo_application_discovery_service.types.time_stamp

        out["startTime"] = (
            capo_application_discovery_service.types.time_stamp.serialize_aws_json_1_1(
                value["start_time"]
            )
        )
    if "stop_time" in value:
        import capo_application_discovery_service.types.time_stamp

        out["stopTime"] = (
            capo_application_discovery_service.types.time_stamp.serialize_aws_json_1_1(
                value["stop_time"]
            )
        )
    if "data_source" in value:
        import capo_application_discovery_service.types.data_source

        out["dataSource"] = (
            capo_application_discovery_service.types.data_source.serialize_aws_json_1_1(
                value["data_source"]
            )
        )
    if "schema_storage_config" in value:
        import capo_application_discovery_service.types.schema_storage_config

        out["schemaStorageConfig"] = (
            capo_application_discovery_service.types.schema_storage_config.serialize_aws_json_1_1(
                value["schema_storage_config"]
            )
        )
    return out


def deserialize_aws_json_1_1(data: dict) -> ContinuousExportDescription:
    out: ContinuousExportDescription = {}  # type: ignore[typeddict-item]
    if data.get("exportId") is not None:
        out["export_id"] = data["exportId"]
    if data.get("status") is not None:
        import capo_application_discovery_service.types.continuous_export_status

        out["status"] = (
            capo_application_discovery_service.types.continuous_export_status.deserialize_aws_json_1_1(
                data["status"]
            )
        )
    if data.get("statusDetail") is not None:
        out["status_detail"] = data["statusDetail"]
    if data.get("s3Bucket") is not None:
        out["s3_bucket"] = data["s3Bucket"]
    if data.get("startTime") is not None:
        import capo_application_discovery_service.types.time_stamp

        out["start_time"] = (
            capo_application_discovery_service.types.time_stamp.deserialize_aws_json_1_1(
                data["startTime"]
            )
        )
    if data.get("stopTime") is not None:
        import capo_application_discovery_service.types.time_stamp

        out["stop_time"] = (
            capo_application_discovery_service.types.time_stamp.deserialize_aws_json_1_1(
                data["stopTime"]
            )
        )
    if data.get("dataSource") is not None:
        import capo_application_discovery_service.types.data_source

        out["data_source"] = (
            capo_application_discovery_service.types.data_source.deserialize_aws_json_1_1(
                data["dataSource"]
            )
        )
    if data.get("schemaStorageConfig") is not None:
        import capo_application_discovery_service.types.schema_storage_config

        out["schema_storage_config"] = (
            capo_application_discovery_service.types.schema_storage_config.deserialize_aws_json_1_1(
                data["schemaStorageConfig"]
            )
        )
    return out
