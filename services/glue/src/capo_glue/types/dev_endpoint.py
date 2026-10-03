"""Generated from Smithy shape ``com.amazonaws.glue#DevEndpoint``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_glue.types.generic_string
    import capo_glue.types.glue_version_string
    import capo_glue.types.integer_value
    import capo_glue.types.map_value
    import capo_glue.types.name_string
    import capo_glue.types.nullable_integer
    import capo_glue.types.public_keys_list
    import capo_glue.types.role_arn
    import capo_glue.types.string_list
    import capo_glue.types.timestamp_value
    import capo_glue.types.worker_type


class DevEndpoint(TypedDict, closed=True):
    endpoint_name: NotRequired["capo_glue.types.generic_string.GenericString"]
    """<p>The name of the <code>DevEndpoint</code>.</p>"""
    role_arn: NotRequired["capo_glue.types.role_arn.RoleArn"]
    """<p>The Amazon Resource Name (ARN) of the IAM role used in this <code>DevEndpoint</code>.</p>"""
    security_group_ids: NotRequired["capo_glue.types.string_list.StringList"]
    """<p>A list of security group identifiers used in this <code>DevEndpoint</code>.</p>"""
    subnet_id: NotRequired["capo_glue.types.generic_string.GenericString"]
    """<p>The subnet ID for this <code>DevEndpoint</code>.</p>"""
    yarn_endpoint_address: NotRequired["capo_glue.types.generic_string.GenericString"]
    """<p>The YARN endpoint address used by this <code>DevEndpoint</code>.</p>"""
    private_address: NotRequired["capo_glue.types.generic_string.GenericString"]
    """<p>A private IP address to access the <code>DevEndpoint</code> within a VPC if the <code>DevEndpoint</code> is created within one. The <code>PrivateAddress</code> field is present only when you create the <code>DevEndpoint</code> within your VPC.</p>"""
    zeppelin_remote_spark_interpreter_port: "capo_glue.types.integer_value.IntegerValue"
    """<p>The Apache Zeppelin port for the remote Apache Spark interpreter.</p>"""
    public_address: NotRequired["capo_glue.types.generic_string.GenericString"]
    """<p>The public IP address used by this <code>DevEndpoint</code>. The <code>PublicAddress</code> field is present only when you create a non-virtual private cloud (VPC) <code>DevEndpoint</code>.</p>"""
    status: NotRequired["capo_glue.types.generic_string.GenericString"]
    """<p>The current status of this <code>DevEndpoint</code>.</p>"""
    worker_type: NotRequired["capo_glue.types.worker_type.WorkerType"]
    """<p>The type of predefined worker that is allocated to the development endpoint. Accepts a value of Standard, G.1X, or G.2X.</p> <ul> <li> <p>For the <code>Standard</code> worker type, each worker provides 4 vCPU, 16 GB of memory and a 50GB disk, and 2 executors per worker.</p> </li> <li> <p>For the <code>G.1X</code> worker type, each worker maps to 1 DPU (4 vCPU, 16 GB of memory, 64 GB disk), and provides 1 executor per worker. We recommend this worker type for memory-intensive jobs.</p> </li> <li> <p>For the <code>G.2X</code> worker type, each worker maps to 2 DPU (8 vCPU, 32 GB of memory, 128 GB disk), and provides 1 executor per worker. We recommend this worker type for memory-intensive jobs.</p> </li> </ul> <p>Known issue: when a development endpoint is created with the <code>G.2X</code> <code>WorkerType</code> configuration, the Spark drivers for the development endpoint will run on 4 vCPU, 16 GB of memory, and a 64 GB disk. </p>"""
    glue_version: NotRequired["capo_glue.types.glue_version_string.GlueVersionString"]
    """<p>Glue version determines the versions of Apache Spark and Python that Glue supports. The Python version indicates the version supported for running your ETL scripts on development endpoints. </p> <p>For more information about the available Glue versions and corresponding Spark and Python versions, see <a href="https://docs.aws.amazon.com/glue/latest/dg/add-job.html">Glue version</a> in the developer guide.</p> <p>Development endpoints that are created without specifying a Glue version default to Glue 0.9.</p> <p>You can specify a version of Python support for development endpoints by using the <code>Arguments</code> parameter in the <code>CreateDevEndpoint</code> or <code>UpdateDevEndpoint</code> APIs. If no arguments are provided, the version defaults to Python 2.</p>"""
    number_of_workers: NotRequired["capo_glue.types.nullable_integer.NullableInteger"]
    """<p>The number of workers of a defined <code>workerType</code> that are allocated to the development endpoint.</p> <p>The maximum number of workers you can define are 299 for <code>G.1X</code>, and 149 for <code>G.2X</code>. </p>"""
    number_of_nodes: "capo_glue.types.integer_value.IntegerValue"
    """<p>The number of Glue Data Processing Units (DPUs) allocated to this <code>DevEndpoint</code>.</p>"""
    availability_zone: NotRequired["capo_glue.types.generic_string.GenericString"]
    """<p>The Amazon Web Services Availability Zone where this <code>DevEndpoint</code> is located.</p>"""
    vpc_id: NotRequired["capo_glue.types.generic_string.GenericString"]
    """<p>The ID of the virtual private cloud (VPC) used by this <code>DevEndpoint</code>.</p>"""
    extra_python_libs_s3_path: NotRequired[
        "capo_glue.types.generic_string.GenericString"
    ]
    """<p>The paths to one or more Python libraries in an Amazon S3 bucket that should be loaded in your <code>DevEndpoint</code>. Multiple values must be complete paths separated by a comma.</p> <note> <p>You can only use pure Python libraries with a <code>DevEndpoint</code>. Libraries that rely on C extensions, such as the <a href="http://pandas.pydata.org/">pandas</a> Python data analysis library, are not currently supported.</p> </note>"""
    extra_jars_s3_path: NotRequired["capo_glue.types.generic_string.GenericString"]
    """<p>The path to one or more Java <code>.jar</code> files in an S3 bucket that should be loaded in your <code>DevEndpoint</code>.</p> <note> <p>You can only use pure Java/Scala libraries with a <code>DevEndpoint</code>.</p> </note>"""
    failure_reason: NotRequired["capo_glue.types.generic_string.GenericString"]
    """<p>The reason for a current failure in this <code>DevEndpoint</code>.</p>"""
    last_update_status: NotRequired["capo_glue.types.generic_string.GenericString"]
    """<p>The status of the last update.</p>"""
    created_timestamp: NotRequired["capo_glue.types.timestamp_value.TimestampValue"]
    """<p>The point in time at which this DevEndpoint was created.</p>"""
    last_modified_timestamp: NotRequired[
        "capo_glue.types.timestamp_value.TimestampValue"
    ]
    """<p>The point in time at which this <code>DevEndpoint</code> was last modified.</p>"""
    public_key: NotRequired["capo_glue.types.generic_string.GenericString"]
    """<p>The public key to be used by this <code>DevEndpoint</code> for authentication. This attribute is provided for backward compatibility because the recommended attribute to use is public keys.</p>"""
    public_keys: NotRequired["capo_glue.types.public_keys_list.PublicKeysList"]
    """<p>A list of public keys to be used by the <code>DevEndpoints</code> for authentication. Using this attribute is preferred over a single public key because the public keys allow you to have a different private key per client.</p> <note> <p>If you previously created an endpoint with a public key, you must remove that key to be able to set a list of public keys. Call the <code>UpdateDevEndpoint</code> API operation with the public key content in the <code>deletePublicKeys</code> attribute, and the list of new keys in the <code>addPublicKeys</code> attribute.</p> </note>"""
    security_configuration: NotRequired["capo_glue.types.name_string.NameString"]
    """<p>The name of the <code>SecurityConfiguration</code> structure to be used with this <code>DevEndpoint</code>.</p>"""
    arguments: NotRequired["capo_glue.types.map_value.MapValue"]
    """<p>A map of arguments used to configure the <code>DevEndpoint</code>.</p> <p>Valid arguments are:</p> <ul> <li> <p> <code>"--enable-glue-datacatalog": ""</code> </p> </li> </ul> <p>You can specify a version of Python support for development endpoints by using the <code>Arguments</code> parameter in the <code>CreateDevEndpoint</code> or <code>UpdateDevEndpoint</code> APIs. If no arguments are provided, the version defaults to Python 2.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: DevEndpoint) -> dict:
    out: dict = {}
    if "endpoint_name" in value:
        out["EndpointName"] = value["endpoint_name"]
    if "role_arn" in value:
        out["RoleArn"] = value["role_arn"]
    if "security_group_ids" in value:
        import capo_glue.types.string_list

        out["SecurityGroupIds"] = capo_glue.types.string_list.serialize_aws_json_1_1(
            value["security_group_ids"]
        )
    if "subnet_id" in value:
        out["SubnetId"] = value["subnet_id"]
    if "yarn_endpoint_address" in value:
        out["YarnEndpointAddress"] = value["yarn_endpoint_address"]
    if "private_address" in value:
        out["PrivateAddress"] = value["private_address"]
    out["ZeppelinRemoteSparkInterpreterPort"] = value.get(
        "zeppelin_remote_spark_interpreter_port", 0
    )
    if "public_address" in value:
        out["PublicAddress"] = value["public_address"]
    if "status" in value:
        out["Status"] = value["status"]
    if "worker_type" in value:
        import capo_glue.types.worker_type

        out["WorkerType"] = capo_glue.types.worker_type.serialize_aws_json_1_1(
            value["worker_type"]
        )
    if "glue_version" in value:
        out["GlueVersion"] = value["glue_version"]
    if "number_of_workers" in value:
        out["NumberOfWorkers"] = value["number_of_workers"]
    out["NumberOfNodes"] = value.get("number_of_nodes", 0)
    if "availability_zone" in value:
        out["AvailabilityZone"] = value["availability_zone"]
    if "vpc_id" in value:
        out["VpcId"] = value["vpc_id"]
    if "extra_python_libs_s3_path" in value:
        out["ExtraPythonLibsS3Path"] = value["extra_python_libs_s3_path"]
    if "extra_jars_s3_path" in value:
        out["ExtraJarsS3Path"] = value["extra_jars_s3_path"]
    if "failure_reason" in value:
        out["FailureReason"] = value["failure_reason"]
    if "last_update_status" in value:
        out["LastUpdateStatus"] = value["last_update_status"]
    if "created_timestamp" in value:
        import capo_glue.types.timestamp_value

        out["CreatedTimestamp"] = (
            capo_glue.types.timestamp_value.serialize_aws_json_1_1(
                value["created_timestamp"]
            )
        )
    if "last_modified_timestamp" in value:
        import capo_glue.types.timestamp_value

        out["LastModifiedTimestamp"] = (
            capo_glue.types.timestamp_value.serialize_aws_json_1_1(
                value["last_modified_timestamp"]
            )
        )
    if "public_key" in value:
        out["PublicKey"] = value["public_key"]
    if "public_keys" in value:
        import capo_glue.types.public_keys_list

        out["PublicKeys"] = capo_glue.types.public_keys_list.serialize_aws_json_1_1(
            value["public_keys"]
        )
    if "security_configuration" in value:
        out["SecurityConfiguration"] = value["security_configuration"]
    if "arguments" in value:
        import capo_glue.types.map_value

        out["Arguments"] = capo_glue.types.map_value.serialize_aws_json_1_1(
            value["arguments"]
        )
    return out


def deserialize_aws_json_1_1(data: dict) -> DevEndpoint:
    out: DevEndpoint = {}  # type: ignore[typeddict-item]
    if data.get("EndpointName") is not None:
        out["endpoint_name"] = data["EndpointName"]
    if data.get("RoleArn") is not None:
        out["role_arn"] = data["RoleArn"]
    if data.get("SecurityGroupIds") is not None:
        import capo_glue.types.string_list

        out["security_group_ids"] = (
            capo_glue.types.string_list.deserialize_aws_json_1_1(
                data["SecurityGroupIds"]
            )
        )
    if data.get("SubnetId") is not None:
        out["subnet_id"] = data["SubnetId"]
    if data.get("YarnEndpointAddress") is not None:
        out["yarn_endpoint_address"] = data["YarnEndpointAddress"]
    if data.get("PrivateAddress") is not None:
        out["private_address"] = data["PrivateAddress"]
    if data.get("ZeppelinRemoteSparkInterpreterPort") is not None:
        out["zeppelin_remote_spark_interpreter_port"] = data[
            "ZeppelinRemoteSparkInterpreterPort"
        ]
    else:
        out["zeppelin_remote_spark_interpreter_port"] = 0
    if data.get("PublicAddress") is not None:
        out["public_address"] = data["PublicAddress"]
    if data.get("Status") is not None:
        out["status"] = data["Status"]
    if data.get("WorkerType") is not None:
        import capo_glue.types.worker_type

        out["worker_type"] = capo_glue.types.worker_type.deserialize_aws_json_1_1(
            data["WorkerType"]
        )
    if data.get("GlueVersion") is not None:
        out["glue_version"] = data["GlueVersion"]
    if data.get("NumberOfWorkers") is not None:
        out["number_of_workers"] = data["NumberOfWorkers"]
    if data.get("NumberOfNodes") is not None:
        out["number_of_nodes"] = data["NumberOfNodes"]
    else:
        out["number_of_nodes"] = 0
    if data.get("AvailabilityZone") is not None:
        out["availability_zone"] = data["AvailabilityZone"]
    if data.get("VpcId") is not None:
        out["vpc_id"] = data["VpcId"]
    if data.get("ExtraPythonLibsS3Path") is not None:
        out["extra_python_libs_s3_path"] = data["ExtraPythonLibsS3Path"]
    if data.get("ExtraJarsS3Path") is not None:
        out["extra_jars_s3_path"] = data["ExtraJarsS3Path"]
    if data.get("FailureReason") is not None:
        out["failure_reason"] = data["FailureReason"]
    if data.get("LastUpdateStatus") is not None:
        out["last_update_status"] = data["LastUpdateStatus"]
    if data.get("CreatedTimestamp") is not None:
        import capo_glue.types.timestamp_value

        out["created_timestamp"] = (
            capo_glue.types.timestamp_value.deserialize_aws_json_1_1(
                data["CreatedTimestamp"]
            )
        )
    if data.get("LastModifiedTimestamp") is not None:
        import capo_glue.types.timestamp_value

        out["last_modified_timestamp"] = (
            capo_glue.types.timestamp_value.deserialize_aws_json_1_1(
                data["LastModifiedTimestamp"]
            )
        )
    if data.get("PublicKey") is not None:
        out["public_key"] = data["PublicKey"]
    if data.get("PublicKeys") is not None:
        import capo_glue.types.public_keys_list

        out["public_keys"] = capo_glue.types.public_keys_list.deserialize_aws_json_1_1(
            data["PublicKeys"]
        )
    if data.get("SecurityConfiguration") is not None:
        out["security_configuration"] = data["SecurityConfiguration"]
    if data.get("Arguments") is not None:
        import capo_glue.types.map_value

        out["arguments"] = capo_glue.types.map_value.deserialize_aws_json_1_1(
            data["Arguments"]
        )
    return out
