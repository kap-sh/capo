"""Generated from Smithy shape ``com.amazonaws.marketplacecommerceanalytics#GenerateDataSetRequest``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

from capo_marketplace_commerce_analytics.errors import DeserializationError

if TYPE_CHECKING:
    import capo_marketplace_commerce_analytics.types.customer_defined_values
    import capo_marketplace_commerce_analytics.types.data_set_publication_date
    import capo_marketplace_commerce_analytics.types.data_set_type
    import capo_marketplace_commerce_analytics.types.destination_s3_bucket_name
    import capo_marketplace_commerce_analytics.types.destination_s3_prefix
    import capo_marketplace_commerce_analytics.types.role_name_arn
    import capo_marketplace_commerce_analytics.types.sns_topic_arn


class GenerateDataSetRequest(TypedDict, closed=True):
    data_set_type: "capo_marketplace_commerce_analytics.types.data_set_type.DataSetType"
    """<p>The desired data set type.</p> <p> <ul> <li> <strong>customer_subscriber_hourly_monthly_subscriptions</strong> <p>From 2017-09-15 to present: Available daily by 24:00 UTC.</p> </li> <li> <strong>customer_subscriber_annual_subscriptions</strong> <p>From 2017-09-15 to present: Available daily by 24:00 UTC.</p> </li> <li> <strong>daily_business_usage_by_instance_type</strong> <p>From 2017-09-15 to present: Available daily by 24:00 UTC.</p> </li> <li> <strong>daily_business_fees</strong> <p>From 2017-09-15 to present: Available daily by 24:00 UTC.</p> </li> <li> <strong>daily_business_free_trial_conversions</strong> <p>From 2017-09-15 to present: Available daily by 24:00 UTC.</p> </li> <li> <strong>daily_business_new_instances</strong> <p>From 2017-09-15 to present: Available daily by 24:00 UTC.</p> </li> <li> <strong>daily_business_new_product_subscribers</strong> <p>From 2017-09-15 to present: Available daily by 24:00 UTC.</p> </li> <li> <strong>daily_business_canceled_product_subscribers</strong> <p>From 2017-09-15 to present: Available daily by 24:00 UTC.</p> </li> <li> <strong>monthly_revenue_billing_and_revenue_data</strong> <p>From 2017-09-15 to present: Available monthly on the 15th day of the month by 24:00 UTC. Data includes metered transactions (e.g. hourly) from one month prior.</p> </li> <li> <strong>monthly_revenue_annual_subscriptions</strong> <p>From 2017-09-15 to present: Available monthly on the 15th day of the month by 24:00 UTC. Data includes up-front software charges (e.g. annual) from one month prior.</p> </li> <li> <strong>monthly_revenue_field_demonstration_usage</strong> <p>From 2018-03-15 to present: Available monthly on the 15th day of the month by 24:00 UTC.</p> </li> <li> <strong>monthly_revenue_flexible_payment_schedule</strong> <p>From 2018-11-15 to present: Available monthly on the 15th day of the month by 24:00 UTC.</p> </li> <li> <strong>disbursed_amount_by_product</strong> <p>From 2017-09-15 to present: Available every 30 days by 24:00 UTC.</p> </li> <li> <strong>disbursed_amount_by_instance_hours</strong> <p>From 2017-09-15 to present: Available every 30 days by 24:00 UTC.</p> </li> <li> <strong>disbursed_amount_by_customer_geo</strong> <p>From 2017-09-15 to present: Available every 30 days by 24:00 UTC.</p> </li> <li> <strong>disbursed_amount_by_age_of_uncollected_funds</strong> <p>From 2017-09-15 to present: Available every 30 days by 24:00 UTC.</p> </li> <li> <strong>disbursed_amount_by_age_of_disbursed_funds</strong> <p>From 2017-09-15 to present: Available every 30 days by 24:00 UTC.</p> </li> <li> <strong>disbursed_amount_by_age_of_past_due_funds</strong> <p>From 2018-04-07 to present: Available every 30 days by 24:00 UTC.</p> </li> <li> <strong>disbursed_amount_by_uncollected_funds_breakdown</strong> <p>From 2019-10-04 to present: Available every 30 days by 24:00 UTC.</p> </li> <li> <strong>sales_compensation_billed_revenue</strong> <p>From 2017-09-15 to present: Available monthly on the 15th day of the month by 24:00 UTC. Data includes metered transactions (e.g. hourly) from one month prior, and up-front software charges (e.g. annual) from one month prior.</p> </li> <li> <strong>us_sales_and_use_tax_records</strong> <p>From 2017-09-15 to present: Available monthly on the 15th day of the month by 24:00 UTC.</p> </li> <li> <strong>disbursed_amount_by_product_with_uncollected_funds</strong> <p>This data set is deprecated. Download related reports from AMMP instead!</p> </li> <li> <strong>customer_profile_by_industry</strong> <p>This data set is deprecated. Download related reports from AMMP instead!</p> </li> <li> <strong>customer_profile_by_revenue</strong> <p>This data set is deprecated. Download related reports from AMMP instead!</p> </li> <li> <strong>customer_profile_by_geography</strong> <p>This data set is deprecated. Download related reports from AMMP instead!</p> </li> </ul> </p>"""
    data_set_publication_date: "capo_marketplace_commerce_analytics.types.data_set_publication_date.DataSetPublicationDate"
    """The date a data set was published. For daily data sets, provide a date with day-level granularity for the desired day. For monthly data sets except those with prefix disbursed_amount, provide a date with month-level granularity for the desired month (the day value will be ignored). For data sets with prefix disbursed_amount, provide a date with day-level granularity for the desired day. For these data sets we will look backwards in time over the range of 31 days until the first data set is found (the latest one)."""
    role_name_arn: "capo_marketplace_commerce_analytics.types.role_name_arn.RoleNameArn"
    """The Amazon Resource Name (ARN) of the Role with an attached permissions policy to interact with the provided AWS services."""
    destination_s3_bucket_name: "capo_marketplace_commerce_analytics.types.destination_s3_bucket_name.DestinationS3BucketName"
    """The name (friendly name, not ARN) of the destination S3 bucket."""
    destination_s3_prefix: NotRequired[
        "capo_marketplace_commerce_analytics.types.destination_s3_prefix.DestinationS3Prefix"
    ]
    """(Optional) The desired S3 prefix for the published data set, similar to a directory path in standard file systems. For example, if given the bucket name "mybucket" and the prefix "myprefix/mydatasets", the output file "outputfile" would be published to "s3://mybucket/myprefix/mydatasets/outputfile". If the prefix directory structure does not exist, it will be created. If no prefix is provided, the data set will be published to the S3 bucket root."""
    sns_topic_arn: "capo_marketplace_commerce_analytics.types.sns_topic_arn.SnsTopicArn"
    """Amazon Resource Name (ARN) for the SNS Topic that will be notified when the data set has been published or if an error has occurred."""
    customer_defined_values: NotRequired[
        "capo_marketplace_commerce_analytics.types.customer_defined_values.CustomerDefinedValues"
    ]
    """(Optional) Key-value pairs which will be returned, unmodified, in the Amazon SNS notification message and the data set metadata file. These key-value pairs can be used to correlated responses with tracking information from other systems."""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: GenerateDataSetRequest) -> dict:
    out: dict = {}
    import capo_marketplace_commerce_analytics.types.data_set_type

    out["dataSetType"] = (
        capo_marketplace_commerce_analytics.types.data_set_type.serialize_aws_json_1_1(
            value["data_set_type"]
        )
    )
    import capo_marketplace_commerce_analytics.types.data_set_publication_date

    out["dataSetPublicationDate"] = (
        capo_marketplace_commerce_analytics.types.data_set_publication_date.serialize_aws_json_1_1(
            value["data_set_publication_date"]
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


def deserialize_aws_json_1_1(data: dict) -> GenerateDataSetRequest:
    out: GenerateDataSetRequest = {}  # type: ignore[typeddict-item]
    if data.get("dataSetType") is not None:
        import capo_marketplace_commerce_analytics.types.data_set_type

        out["data_set_type"] = (
            capo_marketplace_commerce_analytics.types.data_set_type.deserialize_aws_json_1_1(
                data["dataSetType"]
            )
        )
    else:
        raise DeserializationError("GenerateDataSetRequest.data_set_type required")
    if data.get("dataSetPublicationDate") is not None:
        import capo_marketplace_commerce_analytics.types.data_set_publication_date

        out["data_set_publication_date"] = (
            capo_marketplace_commerce_analytics.types.data_set_publication_date.deserialize_aws_json_1_1(
                data["dataSetPublicationDate"]
            )
        )
    else:
        raise DeserializationError(
            "GenerateDataSetRequest.data_set_publication_date required"
        )
    if data.get("roleNameArn") is not None:
        out["role_name_arn"] = data["roleNameArn"]
    else:
        raise DeserializationError("GenerateDataSetRequest.role_name_arn required")
    if data.get("destinationS3BucketName") is not None:
        out["destination_s3_bucket_name"] = data["destinationS3BucketName"]
    else:
        raise DeserializationError(
            "GenerateDataSetRequest.destination_s3_bucket_name required"
        )
    if data.get("destinationS3Prefix") is not None:
        out["destination_s3_prefix"] = data["destinationS3Prefix"]
    if data.get("snsTopicArn") is not None:
        out["sns_topic_arn"] = data["snsTopicArn"]
    else:
        raise DeserializationError("GenerateDataSetRequest.sns_topic_arn required")
    if data.get("customerDefinedValues") is not None:
        import capo_marketplace_commerce_analytics.types.customer_defined_values

        out["customer_defined_values"] = (
            capo_marketplace_commerce_analytics.types.customer_defined_values.deserialize_aws_json_1_1(
                data["customerDefinedValues"]
            )
        )
    return out
