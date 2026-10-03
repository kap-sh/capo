"""Generated from Smithy shape ``com.amazonaws.sagemaker#S3DataSource``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_sagemaker.types.attribute_names
    import capo_sagemaker.types.hub_access_config
    import capo_sagemaker.types.instance_group_names
    import capo_sagemaker.types.model_access_config
    import capo_sagemaker.types.s3_data_distribution
    import capo_sagemaker.types.s3_data_type
    import capo_sagemaker.types.s3_uri


class S3DataSource(TypedDict, closed=True):
    s3_data_type: NotRequired["capo_sagemaker.types.s3_data_type.S3DataType"]
    """<p>If you choose <code>S3Prefix</code>, <code>S3Uri</code> identifies a key name prefix. SageMaker uses all objects that match the specified key name prefix for model training. </p> <p>If you choose <code>ManifestFile</code>, <code>S3Uri</code> identifies an object that is a manifest file containing a list of object keys that you want SageMaker to use for model training. </p> <p>If you choose <code>AugmentedManifestFile</code>, <code>S3Uri</code> identifies an object that is an augmented manifest file in JSON lines format. This file contains the data you want to use for model training. <code>AugmentedManifestFile</code> can only be used if the Channel's input mode is <code>Pipe</code>.</p> <p>If you choose <code>Converse</code>, <code>S3Uri</code> identifies an Amazon S3 location that contains data formatted according to Converse format. This format structures conversational messages with specific roles and content types used for training and fine-tuning foundational models.</p>"""
    s3_uri: NotRequired["capo_sagemaker.types.s3_uri.S3Uri"]
    """<p>Depending on the value specified for the <code>S3DataType</code>, identifies either a key name prefix or a manifest. For example: </p> <ul> <li> <p> A key name prefix might look like this: <code>s3://bucketname/exampleprefix/</code> </p> </li> <li> <p> A manifest might look like this: <code>s3://bucketname/example.manifest</code> </p> <p> A manifest is an S3 object which is a JSON file consisting of an array of elements. The first element is a prefix which is followed by one or more suffixes. SageMaker appends the suffix elements to the prefix to get a full set of <code>S3Uri</code>. Note that the prefix must be a valid non-empty <code>S3Uri</code> that precludes users from specifying a manifest whose individual <code>S3Uri</code> is sourced from different S3 buckets.</p> <p> The following code example shows a valid manifest format: </p> <p> <code>[ {"prefix": "s3://customer_bucket/some/prefix/"},</code> </p> <p> <code> "relative/path/to/custdata-1",</code> </p> <p> <code> "relative/path/custdata-2",</code> </p> <p> <code> ...</code> </p> <p> <code> "relative/path/custdata-N"</code> </p> <p> <code>]</code> </p> <p> This JSON is equivalent to the following <code>S3Uri</code> list:</p> <p> <code>s3://customer_bucket/some/prefix/relative/path/to/custdata-1</code> </p> <p> <code>s3://customer_bucket/some/prefix/relative/path/custdata-2</code> </p> <p> <code>...</code> </p> <p> <code>s3://customer_bucket/some/prefix/relative/path/custdata-N</code> </p> <p>The complete set of <code>S3Uri</code> in this manifest is the input data for the channel for this data source. The object that each <code>S3Uri</code> points to must be readable by the IAM role that SageMaker uses to perform tasks on your behalf. </p> </li> </ul> <p>Your input bucket must be located in same Amazon Web Services region as your training job.</p>"""
    s3_data_distribution_type: NotRequired[
        "capo_sagemaker.types.s3_data_distribution.S3DataDistribution"
    ]
    """<p>If you want SageMaker to replicate the entire dataset on each ML compute instance that is launched for model training, specify <code>FullyReplicated</code>. </p> <p>If you want SageMaker to replicate a subset of data on each ML compute instance that is launched for model training, specify <code>ShardedByS3Key</code>. If there are <i>n</i> ML compute instances launched for a training job, each instance gets approximately 1/<i>n</i> of the number of S3 objects. In this case, model training on each machine uses only the subset of training data. </p> <p>Don't choose more ML compute instances for training than available S3 objects. If you do, some nodes won't get any data and you will pay for nodes that aren't getting any training data. This applies in both File and Pipe modes. Keep this in mind when developing algorithms. </p> <p>In distributed training, where you use multiple ML compute EC2 instances, you might choose <code>ShardedByS3Key</code>. If the algorithm requires copying training data to the ML storage volume (when <code>TrainingInputMode</code> is set to <code>File</code>), this copies 1/<i>n</i> of the number of objects. </p>"""
    attribute_names: NotRequired["capo_sagemaker.types.attribute_names.AttributeNames"]
    """<p>A list of one or more attribute names to use that are found in a specified augmented manifest file.</p>"""
    instance_group_names: NotRequired[
        "capo_sagemaker.types.instance_group_names.InstanceGroupNames"
    ]
    """<p>A list of names of instance groups that get data from the S3 data source.</p>"""
    model_access_config: NotRequired[
        "capo_sagemaker.types.model_access_config.ModelAccessConfig"
    ]
    hub_access_config: NotRequired[
        "capo_sagemaker.types.hub_access_config.HubAccessConfig"
    ]
    """<p>The configuration for a private hub model reference that points to a SageMaker JumpStart public hub model.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: S3DataSource) -> dict:
    out: dict = {}
    if "s3_data_type" in value:
        import capo_sagemaker.types.s3_data_type

        out["S3DataType"] = capo_sagemaker.types.s3_data_type.serialize_aws_json_1_1(
            value["s3_data_type"]
        )
    if "s3_uri" in value:
        out["S3Uri"] = value["s3_uri"]
    if "s3_data_distribution_type" in value:
        import capo_sagemaker.types.s3_data_distribution

        out["S3DataDistributionType"] = (
            capo_sagemaker.types.s3_data_distribution.serialize_aws_json_1_1(
                value["s3_data_distribution_type"]
            )
        )
    if "attribute_names" in value:
        import capo_sagemaker.types.attribute_names

        out["AttributeNames"] = (
            capo_sagemaker.types.attribute_names.serialize_aws_json_1_1(
                value["attribute_names"]
            )
        )
    if "instance_group_names" in value:
        import capo_sagemaker.types.instance_group_names

        out["InstanceGroupNames"] = (
            capo_sagemaker.types.instance_group_names.serialize_aws_json_1_1(
                value["instance_group_names"]
            )
        )
    if "model_access_config" in value:
        import capo_sagemaker.types.model_access_config

        out["ModelAccessConfig"] = (
            capo_sagemaker.types.model_access_config.serialize_aws_json_1_1(
                value["model_access_config"]
            )
        )
    if "hub_access_config" in value:
        import capo_sagemaker.types.hub_access_config

        out["HubAccessConfig"] = (
            capo_sagemaker.types.hub_access_config.serialize_aws_json_1_1(
                value["hub_access_config"]
            )
        )
    return out


def deserialize_aws_json_1_1(data: dict) -> S3DataSource:
    out: S3DataSource = {}  # type: ignore[typeddict-item]
    if data.get("S3DataType") is not None:
        import capo_sagemaker.types.s3_data_type

        out["s3_data_type"] = (
            capo_sagemaker.types.s3_data_type.deserialize_aws_json_1_1(
                data["S3DataType"]
            )
        )
    if data.get("S3Uri") is not None:
        out["s3_uri"] = data["S3Uri"]
    if data.get("S3DataDistributionType") is not None:
        import capo_sagemaker.types.s3_data_distribution

        out["s3_data_distribution_type"] = (
            capo_sagemaker.types.s3_data_distribution.deserialize_aws_json_1_1(
                data["S3DataDistributionType"]
            )
        )
    if data.get("AttributeNames") is not None:
        import capo_sagemaker.types.attribute_names

        out["attribute_names"] = (
            capo_sagemaker.types.attribute_names.deserialize_aws_json_1_1(
                data["AttributeNames"]
            )
        )
    if data.get("InstanceGroupNames") is not None:
        import capo_sagemaker.types.instance_group_names

        out["instance_group_names"] = (
            capo_sagemaker.types.instance_group_names.deserialize_aws_json_1_1(
                data["InstanceGroupNames"]
            )
        )
    if data.get("ModelAccessConfig") is not None:
        import capo_sagemaker.types.model_access_config

        out["model_access_config"] = (
            capo_sagemaker.types.model_access_config.deserialize_aws_json_1_1(
                data["ModelAccessConfig"]
            )
        )
    if data.get("HubAccessConfig") is not None:
        import capo_sagemaker.types.hub_access_config

        out["hub_access_config"] = (
            capo_sagemaker.types.hub_access_config.deserialize_aws_json_1_1(
                data["HubAccessConfig"]
            )
        )
    return out
