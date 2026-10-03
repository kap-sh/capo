"""Generated from Smithy shape ``com.amazonaws.cloudtrail#DataResource``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_cloudtrail.types.data_resource_values
    import capo_cloudtrail.types.string


class DataResource(TypedDict, closed=True):
    type: NotRequired["capo_cloudtrail.types.string.String"]
    """<p>The resource type in which you want to log data events. You can specify the following <i>basic</i> event selector resource types:</p> <ul> <li> <p> <code>AWS::DynamoDB::Table</code> </p> </li> <li> <p> <code>AWS::Lambda::Function</code> </p> </li> <li> <p> <code>AWS::S3::Object</code> </p> </li> </ul> <p>Additional resource types are available through <i>advanced</i> event selectors. For more information, see <a href="https://docs.aws.amazon.com/awscloudtrail/latest/APIReference/API_AdvancedEventSelector.html">AdvancedEventSelector</a>.</p>"""
    values: NotRequired["capo_cloudtrail.types.data_resource_values.DataResourceValues"]
    """<p>An array of Amazon Resource Name (ARN) strings or partial ARN strings for the specified resource type.</p> <ul> <li> <p>To log data events for all objects in all S3 buckets in your Amazon Web Services account, specify the prefix as <code>arn:aws:s3</code>.</p> <note> <p>This also enables logging of data event activity performed by any user or role in your Amazon Web Services account, even if that activity is performed on a bucket that belongs to another Amazon Web Services account.</p> </note> </li> <li> <p>To log data events for all objects in an S3 bucket, specify the bucket and an empty object prefix such as <code>arn:aws:s3:::amzn-s3-demo-bucket1/</code>. The trail logs data events for all objects in this S3 bucket.</p> </li> <li> <p>To log data events for specific objects, specify the S3 bucket and object prefix such as <code>arn:aws:s3:::amzn-s3-demo-bucket1/example-images</code>. The trail logs data events for objects in this S3 bucket that match the prefix.</p> </li> <li> <p>To log data events for all Lambda functions in your Amazon Web Services account, specify the prefix as <code>arn:aws:lambda</code>.</p> <note> <p>This also enables logging of <code>Invoke</code> activity performed by any user or role in your Amazon Web Services account, even if that activity is performed on a function that belongs to another Amazon Web Services account. </p> </note> </li> <li> <p>To log data events for a specific Lambda function, specify the function ARN.</p> <note> <p>Lambda function ARNs are exact. For example, if you specify a function ARN <i>arn:aws:lambda:us-west-2:111111111111:function:helloworld</i>, data events will only be logged for <i>arn:aws:lambda:us-west-2:111111111111:function:helloworld</i>. They will not be logged for <i>arn:aws:lambda:us-west-2:111111111111:function:helloworld2</i>.</p> </note> </li> <li> <p>To log data events for all DynamoDB tables in your Amazon Web Services account, specify the prefix as <code>arn:aws:dynamodb</code>.</p> </li> </ul>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: DataResource) -> dict:
    out: dict = {}
    if "type" in value:
        out["Type"] = value["type"]
    if "values" in value:
        import capo_cloudtrail.types.data_resource_values

        out["Values"] = (
            capo_cloudtrail.types.data_resource_values.serialize_aws_json_1_1(
                value["values"]
            )
        )
    return out


def deserialize_aws_json_1_1(data: dict) -> DataResource:
    out: DataResource = {}  # type: ignore[typeddict-item]
    if data.get("Type") is not None:
        out["type"] = data["Type"]
    if data.get("Values") is not None:
        import capo_cloudtrail.types.data_resource_values

        out["values"] = (
            capo_cloudtrail.types.data_resource_values.deserialize_aws_json_1_1(
                data["Values"]
            )
        )
    return out
