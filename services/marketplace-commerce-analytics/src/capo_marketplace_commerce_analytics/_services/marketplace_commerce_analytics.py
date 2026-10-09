"""Generated from Smithy shape ``com.amazonaws.marketplacecommerceanalytics#MarketplaceCommerceAnalytics20150701``."""

import warnings
from typing import TYPE_CHECKING, Any, Iterable, Optional

from typing_extensions import Self, TypedDict
from zapros import BaseHandler, Client

import capo_marketplace_commerce_analytics._auth._signers
import capo_marketplace_commerce_analytics._auth._sigv4
from capo_marketplace_commerce_analytics._auth._identity import Credentials
from capo_marketplace_commerce_analytics._auth._providers import (
    CredentialsProvider,
    IdentityProvider,
    StaticAwsCredentialsProvider,
    default_aws_credentials_chain,
)
from capo_marketplace_commerce_analytics._auth._zapros_handler import AuthMiddleware
from capo_marketplace_commerce_analytics._services._aws_config import aws_config
from capo_marketplace_commerce_analytics._services._pipeline import (
    Interceptor,
    OperationOptions,
    OperationRequest,
    OperationResponse,
    execute_pipeline,
    retry,
)

if TYPE_CHECKING:
    import capo_marketplace_commerce_analytics.types.customer_defined_values
    import capo_marketplace_commerce_analytics.types.data_set_publication_date
    import capo_marketplace_commerce_analytics.types.data_set_type
    import capo_marketplace_commerce_analytics.types.destination_s3_bucket_name
    import capo_marketplace_commerce_analytics.types.destination_s3_prefix
    import capo_marketplace_commerce_analytics.types.from_date
    import capo_marketplace_commerce_analytics.types.generate_data_set_request
    import capo_marketplace_commerce_analytics.types.generate_data_set_result
    import capo_marketplace_commerce_analytics.types.role_name_arn
    import capo_marketplace_commerce_analytics.types.sns_topic_arn
    import capo_marketplace_commerce_analytics.types.start_support_data_export_request
    import capo_marketplace_commerce_analytics.types.start_support_data_export_result
    import capo_marketplace_commerce_analytics.types.support_data_set_type


class MarketplaceCommerceAnalyticsClientConfig(TypedDict, total=False, closed=True):
    operation_interceptors: Iterable[Interceptor[Any, Any]]
    retry_max_attempts: int | None
    region: str | None
    use_dual_stack: bool | None
    use_fips: bool | None
    endpoint: str | None
    credentials_provider: IdentityProvider[Credentials] | None
    anonymous: bool | None


class MarketplaceCommerceAnalyticsClient:
    """A client for the ``MarketplaceCommerceAnalytics`` service.

    Args:
        http_handler: HTTP handler for sending requests. If not provided, creates a default handler.
        operation_interceptors: Interceptors that wrap every operation call. If not provided, defaults to an empty list.
        retry_max_attempts: Maximum number of times to retry a failed operation. Defaults to 3.
        region: The value of the ``AWS::Region`` endpoint parameter.
        use_dual_stack: The value of the ``AWS::UseDualStack`` endpoint parameter.
        use_fips: The value of the ``AWS::UseFIPS`` endpoint parameter.
        endpoint: The value of the ``SDK::Endpoint`` endpoint parameter.
        credentials: AWS credentials for request signing.
        credentials_provider: Provider that resolves AWS credentials. Takes precedence over ``credentials``.
        anonymous: Send requests unsigned, without resolving credentials, even for operations that require authentication.
    """

    def __init__(
        self,
        http_handler: BaseHandler | None = None,
        operation_interceptors: Iterable[Interceptor[Any, Any]] | None = None,
        retry_max_attempts: int | None = None,
        region: str | None = None,
        use_dual_stack: bool | None = None,
        use_fips: bool | None = None,
        endpoint: str | None = None,
        credentials: Credentials | None = None,
        credentials_provider: CredentialsProvider | None = None,
        anonymous: bool | None = None,
    ):
        self._client = Client(http_handler).wrap_with_middleware(
            lambda next: AuthMiddleware(next)
        )
        if credentials is not None and credentials_provider is not None:
            warnings.warn(
                "Both credentials and credentials_provider given; provider takes precedence"
            )
        resolved_credentials_provider: IdentityProvider[Credentials] | None = (
            credentials_provider
        )
        if resolved_credentials_provider is None and credentials is not None:
            resolved_credentials_provider = StaticAwsCredentialsProvider(credentials)
        if resolved_credentials_provider is None and credentials is None:
            resolved_credentials_provider = default_aws_credentials_chain(
                Client(http_handler)
            )
        self._config = MarketplaceCommerceAnalyticsClientConfig(
            {
                "operation_interceptors": operation_interceptors or [],
                "retry_max_attempts": retry_max_attempts,
                "region": region,
                "use_dual_stack": use_dual_stack,
                "use_fips": use_fips,
                "endpoint": endpoint,
                "credentials_provider": resolved_credentials_provider,
                "anonymous": anonymous,
            }
        )

    def operation_options(
        self,
        config_overrides: Optional[MarketplaceCommerceAnalyticsClientConfig] = None,
    ) -> tuple[Iterable[Interceptor[Any, Any]], OperationOptions]:
        overrides: MarketplaceCommerceAnalyticsClientConfig = config_overrides or {}
        interceptors_: list[Interceptor[Any, Any]] = [
            *overrides.get(
                "operation_interceptors", self._config.get("operation_interceptors", [])
            ),
            aws_config(),
            retry(),
        ]
        options_: OperationOptions = OperationOptions(
            client=self._client,
            retry_max_attempts=overrides.get(
                "retry_max_attempts", self._config.get("retry_max_attempts")
            ),
            region=overrides.get("region", self._config.get("region")),
            use_dual_stack=overrides.get(
                "use_dual_stack", self._config.get("use_dual_stack")
            ),
            use_fips=overrides.get("use_fips", self._config.get("use_fips")),
            endpoint=overrides.get("endpoint", self._config.get("endpoint")),
            credentials_provider=overrides.get(
                "credentials_provider", self._config.get("credentials_provider")
            ),
            anonymous=overrides.get("anonymous", self._config.get("anonymous")),
        )
        return interceptors_, options_

    def generate_data_set(
        self,
        data_set_type: "capo_marketplace_commerce_analytics.types.data_set_type.DataSetType",
        data_set_publication_date: "capo_marketplace_commerce_analytics.types.data_set_publication_date.DataSetPublicationDate",
        role_name_arn: "capo_marketplace_commerce_analytics.types.role_name_arn.RoleNameArn",
        destination_s3_bucket_name: "capo_marketplace_commerce_analytics.types.destination_s3_bucket_name.DestinationS3BucketName",
        sns_topic_arn: "capo_marketplace_commerce_analytics.types.sns_topic_arn.SnsTopicArn",
        *,
        config_overrides: Optional[MarketplaceCommerceAnalyticsClientConfig] = None,
        destination_s3_prefix: Optional[
            "capo_marketplace_commerce_analytics.types.destination_s3_prefix.DestinationS3Prefix"
        ] = None,
        customer_defined_values: Optional[
            "capo_marketplace_commerce_analytics.types.customer_defined_values.CustomerDefinedValues"
        ] = None,
    ) -> "capo_marketplace_commerce_analytics.types.generate_data_set_result.GenerateDataSetResult":
        """Given a data set type and data set publication date, asynchronously publishes the requested data set to the specified S3 bucket and notifies the specified SNS topic once the data is available. Returns a unique request identifier that can be used to correlate requests with notifications from the SNS topic. Data sets will be published in comma-separated values (CSV) format with the file name {data_set_type}_YYYY-MM-DD.csv. If a file with the same name already exists (e.g. if the same data set is requested twice), the original file will be overwritten by the new file. Requires a Role with an attached permissions policy providing Allow permissions for the following actions: s3:PutObject, s3:GetBucketLocation, sns:GetTopicAttributes, sns:Publish, iam:GetRolePolicy.

        Args:
            data_set_type: <p>The desired data set type.</p> <p> <ul> <li> <strong>customer_subscriber_hourly_monthly_subscriptions</strong> <p>From 2017-09-15 to present: Available daily by 24:00 UTC.</p> </li> <li> <strong>customer_subscriber_annual_subscriptions</strong> <p>From 2017-09-15 to present: Available daily by 24:00 UTC.</p> </li> <li> <strong>daily_business_usage_by_instance_type</strong> <p>From 2017-09-15 to present: Available daily by 24:00 UTC.</p> </li> <li> <strong>daily_business_fees</strong> <p>From 2017-09-15 to present: Available daily by 24:00 UTC.</p> </li> <li> <strong>daily_business_free_trial_conversions</strong> <p>From 2017-09-15 to present: Available daily by 24:00 UTC.</p> </li> <li> <strong>daily_business_new_instances</strong> <p>From 2017-09-15 to present: Available daily by 24:00 UTC.</p> </li> <li> <strong>daily_business_new_product_subscribers</strong> <p>From 2017-09-15 to present: Available daily by 24:00 UTC.</p> </li> <li> <strong>daily_business_canceled_product_subscribers</strong> <p>From 2017-09-15 to present: Available daily by 24:00 UTC.</p> </li> <li> <strong>monthly_revenue_billing_and_revenue_data</strong> <p>From 2017-09-15 to present: Available monthly on the 15th day of the month by 24:00 UTC. Data includes metered transactions (e.g. hourly) from one month prior.</p> </li> <li> <strong>monthly_revenue_annual_subscriptions</strong> <p>From 2017-09-15 to present: Available monthly on the 15th day of the month by 24:00 UTC. Data includes up-front software charges (e.g. annual) from one month prior.</p> </li> <li> <strong>monthly_revenue_field_demonstration_usage</strong> <p>From 2018-03-15 to present: Available monthly on the 15th day of the month by 24:00 UTC.</p> </li> <li> <strong>monthly_revenue_flexible_payment_schedule</strong> <p>From 2018-11-15 to present: Available monthly on the 15th day of the month by 24:00 UTC.</p> </li> <li> <strong>disbursed_amount_by_product</strong> <p>From 2017-09-15 to present: Available every 30 days by 24:00 UTC.</p> </li> <li> <strong>disbursed_amount_by_instance_hours</strong> <p>From 2017-09-15 to present: Available every 30 days by 24:00 UTC.</p> </li> <li> <strong>disbursed_amount_by_customer_geo</strong> <p>From 2017-09-15 to present: Available every 30 days by 24:00 UTC.</p> </li> <li> <strong>disbursed_amount_by_age_of_uncollected_funds</strong> <p>From 2017-09-15 to present: Available every 30 days by 24:00 UTC.</p> </li> <li> <strong>disbursed_amount_by_age_of_disbursed_funds</strong> <p>From 2017-09-15 to present: Available every 30 days by 24:00 UTC.</p> </li> <li> <strong>disbursed_amount_by_age_of_past_due_funds</strong> <p>From 2018-04-07 to present: Available every 30 days by 24:00 UTC.</p> </li> <li> <strong>disbursed_amount_by_uncollected_funds_breakdown</strong> <p>From 2019-10-04 to present: Available every 30 days by 24:00 UTC.</p> </li> <li> <strong>sales_compensation_billed_revenue</strong> <p>From 2017-09-15 to present: Available monthly on the 15th day of the month by 24:00 UTC. Data includes metered transactions (e.g. hourly) from one month prior, and up-front software charges (e.g. annual) from one month prior.</p> </li> <li> <strong>us_sales_and_use_tax_records</strong> <p>From 2017-09-15 to present: Available monthly on the 15th day of the month by 24:00 UTC.</p> </li> <li> <strong>disbursed_amount_by_product_with_uncollected_funds</strong> <p>This data set is deprecated. Download related reports from AMMP instead!</p> </li> <li> <strong>customer_profile_by_industry</strong> <p>This data set is deprecated. Download related reports from AMMP instead!</p> </li> <li> <strong>customer_profile_by_revenue</strong> <p>This data set is deprecated. Download related reports from AMMP instead!</p> </li> <li> <strong>customer_profile_by_geography</strong> <p>This data set is deprecated. Download related reports from AMMP instead!</p> </li> </ul> </p>
            data_set_publication_date: The date a data set was published. For daily data sets, provide a date with day-level granularity for the desired day. For monthly data sets except those with prefix disbursed_amount, provide a date with month-level granularity for the desired month (the day value will be ignored). For data sets with prefix disbursed_amount, provide a date with day-level granularity for the desired day. For these data sets we will look backwards in time over the range of 31 days until the first data set is found (the latest one).
            role_name_arn: The Amazon Resource Name (ARN) of the Role with an attached permissions policy to interact with the provided AWS services.
            destination_s3_bucket_name: The name (friendly name, not ARN) of the destination S3 bucket.
            destination_s3_prefix: (Optional) The desired S3 prefix for the published data set, similar to a directory path in standard file systems. For example, if given the bucket name "mybucket" and the prefix "myprefix/mydatasets", the output file "outputfile" would be published to "s3://mybucket/myprefix/mydatasets/outputfile". If the prefix directory structure does not exist, it will be created. If no prefix is provided, the data set will be published to the S3 bucket root.
            sns_topic_arn: Amazon Resource Name (ARN) for the SNS Topic that will be notified when the data set has been published or if an error has occurred.
            customer_defined_values: (Optional) Key-value pairs which will be returned, unmodified, in the Amazon SNS notification message and the data set metadata file. These key-value pairs can be used to correlated responses with tracking information from other systems.

        Raises:
            capo_marketplace_commerce_analytics.errors.marketplace_commerce_analytics_exception.MarketplaceCommerceAnalyticsException: This exception is thrown when an internal service error occurs.
            capo_marketplace_commerce_analytics.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        def _handler(
            req: "OperationRequest[capo_marketplace_commerce_analytics.types.generate_data_set_request.GenerateDataSetRequest]",
        ) -> OperationResponse[
            "capo_marketplace_commerce_analytics.types.generate_data_set_result.GenerateDataSetResult"
        ]:
            import capo_marketplace_commerce_analytics._operations.marketplace_commerce_analytics20150701.generate_data_set

            output, http_response = (
                capo_marketplace_commerce_analytics._operations.marketplace_commerce_analytics20150701.generate_data_set.generate_data_set(
                    req.options, req.input
                )
            )
            return OperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_marketplace_commerce_analytics.types.generate_data_set_request.GenerateDataSetRequest = {
            "data_set_type": data_set_type,
            "data_set_publication_date": data_set_publication_date,
            "role_name_arn": role_name_arn,
            "destination_s3_bucket_name": destination_s3_bucket_name,
            "sns_topic_arn": sns_topic_arn,
        }
        if destination_s3_prefix is not None:
            input_["destination_s3_prefix"] = destination_s3_prefix
        if customer_defined_values is not None:
            input_["customer_defined_values"] = customer_defined_values

        response = execute_pipeline(
            OperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        response.response.close()
        return response.output

    def start_support_data_export(
        self,
        data_set_type: "capo_marketplace_commerce_analytics.types.support_data_set_type.SupportDataSetType",
        from_date: "capo_marketplace_commerce_analytics.types.from_date.FromDate",
        role_name_arn: "capo_marketplace_commerce_analytics.types.role_name_arn.RoleNameArn",
        destination_s3_bucket_name: "capo_marketplace_commerce_analytics.types.destination_s3_bucket_name.DestinationS3BucketName",
        sns_topic_arn: "capo_marketplace_commerce_analytics.types.sns_topic_arn.SnsTopicArn",
        *,
        config_overrides: Optional[MarketplaceCommerceAnalyticsClientConfig] = None,
        destination_s3_prefix: Optional[
            "capo_marketplace_commerce_analytics.types.destination_s3_prefix.DestinationS3Prefix"
        ] = None,
        customer_defined_values: Optional[
            "capo_marketplace_commerce_analytics.types.customer_defined_values.CustomerDefinedValues"
        ] = None,
    ) -> "capo_marketplace_commerce_analytics.types.start_support_data_export_result.StartSupportDataExportResult":
        """<i>This target has been deprecated.</i> Given a data set type and a from date, asynchronously publishes the requested customer support data to the specified S3 bucket and notifies the specified SNS topic once the data is available. Returns a unique request identifier that can be used to correlate requests with notifications from the SNS topic. Data sets will be published in comma-separated values (CSV) format with the file name {data_set_type}_YYYY-MM-DD'T'HH-mm-ss'Z'.csv. If a file with the same name already exists (e.g. if the same data set is requested twice), the original file will be overwritten by the new file. Requires a Role with an attached permissions policy providing Allow permissions for the following actions: s3:PutObject, s3:GetBucketLocation, sns:GetTopicAttributes, sns:Publish, iam:GetRolePolicy.

        Args:
            data_set_type: <p> <i>This target has been deprecated.</i> Specifies the data set type to be written to the output csv file. The data set types customer_support_contacts_data and test_customer_support_contacts_data both result in a csv file containing the following fields: Product Id, Product Code, Customer Guid, Subscription Guid, Subscription Start Date, Organization, AWS Account Id, Given Name, Surname, Telephone Number, Email, Title, Country Code, ZIP Code, Operation Type, and Operation Time. </p> <p> <ul> <li><i>customer_support_contacts_data</i> Customer support contact data. The data set will contain all changes (Creates, Updates, and Deletes) to customer support contact data from the date specified in the from_date parameter.</li> <li><i>test_customer_support_contacts_data</i> An example data set containing static test data in the same format as customer_support_contacts_data</li> </ul> </p>
            from_date: <i>This target has been deprecated.</i> The start date from which to retrieve the data set in UTC. This parameter only affects the customer_support_contacts_data data set type.
            role_name_arn: <i>This target has been deprecated.</i> The Amazon Resource Name (ARN) of the Role with an attached permissions policy to interact with the provided AWS services.
            destination_s3_bucket_name: <i>This target has been deprecated.</i> The name (friendly name, not ARN) of the destination S3 bucket.
            destination_s3_prefix: <i>This target has been deprecated.</i> (Optional) The desired S3 prefix for the published data set, similar to a directory path in standard file systems. For example, if given the bucket name "mybucket" and the prefix "myprefix/mydatasets", the output file "outputfile" would be published to "s3://mybucket/myprefix/mydatasets/outputfile". If the prefix directory structure does not exist, it will be created. If no prefix is provided, the data set will be published to the S3 bucket root.
            sns_topic_arn: <i>This target has been deprecated.</i> Amazon Resource Name (ARN) for the SNS Topic that will be notified when the data set has been published or if an error has occurred.
            customer_defined_values: <i>This target has been deprecated.</i> (Optional) Key-value pairs which will be returned, unmodified, in the Amazon SNS notification message and the data set metadata file.

        Raises:
            capo_marketplace_commerce_analytics.errors.marketplace_commerce_analytics_exception.MarketplaceCommerceAnalyticsException: This exception is thrown when an internal service error occurs.
            capo_marketplace_commerce_analytics.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        def _handler(
            req: "OperationRequest[capo_marketplace_commerce_analytics.types.start_support_data_export_request.StartSupportDataExportRequest]",
        ) -> OperationResponse[
            "capo_marketplace_commerce_analytics.types.start_support_data_export_result.StartSupportDataExportResult"
        ]:
            import capo_marketplace_commerce_analytics._operations.marketplace_commerce_analytics20150701.start_support_data_export

            output, http_response = (
                capo_marketplace_commerce_analytics._operations.marketplace_commerce_analytics20150701.start_support_data_export.start_support_data_export(
                    req.options, req.input
                )
            )
            return OperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_marketplace_commerce_analytics.types.start_support_data_export_request.StartSupportDataExportRequest = {
            "data_set_type": data_set_type,
            "from_date": from_date,
            "role_name_arn": role_name_arn,
            "destination_s3_bucket_name": destination_s3_bucket_name,
            "sns_topic_arn": sns_topic_arn,
        }
        if destination_s3_prefix is not None:
            input_["destination_s3_prefix"] = destination_s3_prefix
        if customer_defined_values is not None:
            input_["customer_defined_values"] = customer_defined_values

        response = execute_pipeline(
            OperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        response.response.close()
        return response.output

    def __enter__(self) -> Self:
        return self

    def __exit__(self, exc_type: Any, exc: Any, tb: Any):
        self._client.close()
