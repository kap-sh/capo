"""Generated from Smithy shape ``com.amazonaws.marketplacecommerceanalytics#StartSupportDataExportRequest``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

from capo_marketplace_commerce_analytics.errors import DeserializationError

if TYPE_CHECKING:
    import capo_marketplace_commerce_analytics.types.customer_defined_values
    import capo_marketplace_commerce_analytics.types.destination_s3_bucket_name
    import capo_marketplace_commerce_analytics.types.destination_s3_prefix
    import capo_marketplace_commerce_analytics.types.from_date
    import capo_marketplace_commerce_analytics.types.role_name_arn
    import capo_marketplace_commerce_analytics.types.sns_topic_arn
    import capo_marketplace_commerce_analytics.types.support_data_set_type


class StartSupportDataExportRequest(TypedDict, closed=True):
    data_set_type: "capo_marketplace_commerce_analytics.types.support_data_set_type.SupportDataSetType"
    """<p> <i>This target has been deprecated.</i> Specifies the data set type to be written to the output csv file. The data set types customer_support_contacts_data and test_customer_support_contacts_data both result in a csv file containing the following fields: Product Id, Product Code, Customer Guid, Subscription Guid, Subscription Start Date, Organization, AWS Account Id, Given Name, Surname, Telephone Number, Email, Title, Country Code, ZIP Code, Operation Type, and Operation Time. </p> <p> <ul> <li><i>customer_support_contacts_data</i> Customer support contact data. The data set will contain all changes (Creates, Updates, and Deletes) to customer support contact data from the date specified in the from_date parameter.</li> <li><i>test_customer_support_contacts_data</i> An example data set containing static test data in the same format as customer_support_contacts_data</li> </ul> </p>"""
    from_date: "capo_marketplace_commerce_analytics.types.from_date.FromDate"
    """<i>This target has been deprecated.</i> The start date from which to retrieve the data set in UTC. This parameter only affects the customer_support_contacts_data data set type."""
    role_name_arn: "capo_marketplace_commerce_analytics.types.role_name_arn.RoleNameArn"
    """<i>This target has been deprecated.</i> The Amazon Resource Name (ARN) of the Role with an attached permissions policy to interact with the provided AWS services."""
    destination_s3_bucket_name: "capo_marketplace_commerce_analytics.types.destination_s3_bucket_name.DestinationS3BucketName"
    """<i>This target has been deprecated.</i> The name (friendly name, not ARN) of the destination S3 bucket."""
    destination_s3_prefix: NotRequired[
        "capo_marketplace_commerce_analytics.types.destination_s3_prefix.DestinationS3Prefix"
    ]
    """<i>This target has been deprecated.</i> (Optional) The desired S3 prefix for the published data set, similar to a directory path in standard file systems. For example, if given the bucket name "mybucket" and the prefix "myprefix/mydatasets", the output file "outputfile" would be published to "s3://mybucket/myprefix/mydatasets/outputfile". If the prefix directory structure does not exist, it will be created. If no prefix is provided, the data set will be published to the S3 bucket root."""
    sns_topic_arn: "capo_marketplace_commerce_analytics.types.sns_topic_arn.SnsTopicArn"
    """<i>This target has been deprecated.</i> Amazon Resource Name (ARN) for the SNS Topic that will be notified when the data set has been published or if an error has occurred."""
    customer_defined_values: NotRequired[
        "capo_marketplace_commerce_analytics.types.customer_defined_values.CustomerDefinedValues"
    ]
    """<i>This target has been deprecated.</i> (Optional) Key-value pairs which will be returned, unmodified, in the Amazon SNS notification message and the data set metadata file."""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: StartSupportDataExportRequest) -> dict:
    out: dict = {}
    import capo_marketplace_commerce_analytics.types.support_data_set_type

    out["dataSetType"] = (
        capo_marketplace_commerce_analytics.types.support_data_set_type.serialize_aws_json_1_1(
            value["data_set_type"]
        )
    )
    import capo_marketplace_commerce_analytics.types.from_date

    out["fromDate"] = (
        capo_marketplace_commerce_analytics.types.from_date.serialize_aws_json_1_1(
            value["from_date"]
        )
    )
    out["roleNameArn"] = value["role_name_arn"]
    out["destinationS3BucketName"] = value["destination_s3_bucket_name"]
    if "destination_s3_prefix" in value:
        out["destinationS3Prefix"] = value["destination_s3_prefix"]
    out["snsTopicArn"] = value["sns_topic_arn"]
    if "customer_defined_values" in value:
        import capo_marketplace_commerce_analytics.types.customer_defined_values

        out["customerDefinedValues"] = (
            capo_marketplace_commerce_analytics.types.customer_defined_values.serialize_aws_json_1_1(
                value["customer_defined_values"]
            )
        )
    return out


def deserialize_aws_json_1_1(data: dict) -> StartSupportDataExportRequest:
    out: StartSupportDataExportRequest = {}  # type: ignore[typeddict-item]
    if data.get("dataSetType") is not None:
        import capo_marketplace_commerce_analytics.types.support_data_set_type

        out["data_set_type"] = (
            capo_marketplace_commerce_analytics.types.support_data_set_type.deserialize_aws_json_1_1(
                data["dataSetType"]
            )
        )
    else:
        raise DeserializationError(
            "StartSupportDataExportRequest.data_set_type required"
        )
    if data.get("fromDate") is not None:
        import capo_marketplace_commerce_analytics.types.from_date

        out["from_date"] = (
            capo_marketplace_commerce_analytics.types.from_date.deserialize_aws_json_1_1(
                data["fromDate"]
            )
        )
    else:
        raise DeserializationError("StartSupportDataExportRequest.from_date required")
    if data.get("roleNameArn") is not None:
        out["role_name_arn"] = data["roleNameArn"]
    else:
        raise DeserializationError(
            "StartSupportDataExportRequest.role_name_arn required"
        )
    if data.get("destinationS3BucketName") is not None:
        out["destination_s3_bucket_name"] = data["destinationS3BucketName"]
    else:
        raise DeserializationError(
            "StartSupportDataExportRequest.destination_s3_bucket_name required"
        )
    if data.get("destinationS3Prefix") is not None:
        out["destination_s3_prefix"] = data["destinationS3Prefix"]
    if data.get("snsTopicArn") is not None:
        out["sns_topic_arn"] = data["snsTopicArn"]
    else:
        raise DeserializationError(
            "StartSupportDataExportRequest.sns_topic_arn required"
        )
    if data.get("customerDefinedValues") is not None:
        import capo_marketplace_commerce_analytics.types.customer_defined_values

        out["customer_defined_values"] = (
            capo_marketplace_commerce_analytics.types.customer_defined_values.deserialize_aws_json_1_1(
                data["customerDefinedValues"]
            )
        )
    return out
