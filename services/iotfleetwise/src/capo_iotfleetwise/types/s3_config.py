"""Generated from Smithy shape ``com.amazonaws.iotfleetwise#S3Config``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

from capo_iotfleetwise.errors import DeserializationError

if TYPE_CHECKING:
    import capo_iotfleetwise.types.data_format
    import capo_iotfleetwise.types.prefix
    import capo_iotfleetwise.types.s3_bucket_arn
    import capo_iotfleetwise.types.storage_compression_format


class S3Config(TypedDict, closed=True):
    bucket_arn: "capo_iotfleetwise.types.s3_bucket_arn.S3BucketArn"
    """<p>The Amazon Resource Name (ARN) of the Amazon S3 bucket.</p>"""
    data_format: NotRequired["capo_iotfleetwise.types.data_format.DataFormat"]
    """<p>Specify the format that files are saved in the Amazon S3 bucket. You can save files in an Apache Parquet or JSON format.</p> <ul> <li> <p>Parquet - Store data in a columnar storage file format. Parquet is optimal for fast data retrieval and can reduce costs. This option is selected by default.</p> </li> <li> <p>JSON - Store data in a standard text-based JSON file format.</p> </li> </ul>"""
    storage_compression_format: NotRequired[
        "capo_iotfleetwise.types.storage_compression_format.StorageCompressionFormat"
    ]
    """<p>By default, stored data is compressed as a .gzip file. Compressed files have a reduced file size, which can optimize the cost of data storage.</p>"""
    prefix: NotRequired["capo_iotfleetwise.types.prefix.Prefix"]
    """<p>Enter an S3 bucket prefix. The prefix is the string of characters after the bucket name and before the object name. You can use the prefix to organize data stored in Amazon S3 buckets. For more information, see <a href="https://docs.aws.amazon.com/AmazonS3/latest/userguide/using-prefixes.html">Organizing objects using prefixes</a> in the <i>Amazon Simple Storage Service User Guide</i>.</p> <p>By default, Amazon Web Services IoT FleetWise sets the prefix <code>processed-data/year=YY/month=MM/date=DD/hour=HH/</code> (in UTC) to data it delivers to Amazon S3. You can enter a prefix to append it to this default prefix. For example, if you enter the prefix <code>vehicles</code>, the prefix will be <code>vehicles/processed-data/year=YY/month=MM/date=DD/hour=HH/</code>.</p>"""


# --- awsJson1_0 ser/de ---
def serialize_aws_json_1_0(value: S3Config) -> dict:
    out: dict = {}
    out["bucketArn"] = value["bucket_arn"]
    if "data_format" in value:
        import capo_iotfleetwise.types.data_format

        out["dataFormat"] = capo_iotfleetwise.types.data_format.serialize_aws_json_1_0(
            value["data_format"]
        )
    if "storage_compression_format" in value:
        import capo_iotfleetwise.types.storage_compression_format

        out["storageCompressionFormat"] = (
            capo_iotfleetwise.types.storage_compression_format.serialize_aws_json_1_0(
                value["storage_compression_format"]
            )
        )
    if "prefix" in value:
        out["prefix"] = value["prefix"]
    return out


def deserialize_aws_json_1_0(data: dict) -> S3Config:
    out: S3Config = {}  # type: ignore[typeddict-item]
    if data.get("bucketArn") is not None:
        out["bucket_arn"] = data["bucketArn"]
    else:
        raise DeserializationError("S3Config.bucket_arn required")
    if data.get("dataFormat") is not None:
        import capo_iotfleetwise.types.data_format

        out["data_format"] = (
            capo_iotfleetwise.types.data_format.deserialize_aws_json_1_0(
                data["dataFormat"]
            )
        )
    if data.get("storageCompressionFormat") is not None:
        import capo_iotfleetwise.types.storage_compression_format

        out["storage_compression_format"] = (
            capo_iotfleetwise.types.storage_compression_format.deserialize_aws_json_1_0(
                data["storageCompressionFormat"]
            )
        )
    if data.get("prefix") is not None:
        out["prefix"] = data["prefix"]
    return out
