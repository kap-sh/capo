"""Generated from Smithy shape ``com.amazonaws.snowball#AWSIESnowballJobManagementService``."""

import warnings
from collections.abc import Iterator
from typing import TYPE_CHECKING, Any, Iterable, Optional

from typing_extensions import Self, TypedDict
from zapros import BaseHandler, Client

import capo_snowball._auth._signers
import capo_snowball._auth._sigv4
from capo_snowball._auth._identity import Credentials
from capo_snowball._auth._providers import (
    CredentialsProvider,
    IdentityProvider,
    StaticAwsCredentialsProvider,
    default_aws_credentials_chain,
)
from capo_snowball._auth._zapros_handler import AuthMiddleware
from capo_snowball._pagination import resolve_path as _resolve_path
from capo_snowball._services._aws_config import aws_config
from capo_snowball._services._pipeline import (
    Interceptor,
    OperationOptions,
    OperationRequest,
    OperationResponse,
    execute_pipeline,
    retry,
)

if TYPE_CHECKING:
    import capo_snowball.types.address
    import capo_snowball.types.address_id
    import capo_snowball.types.boolean
    import capo_snowball.types.cancel_cluster_request
    import capo_snowball.types.cancel_cluster_result
    import capo_snowball.types.cancel_job_request
    import capo_snowball.types.cancel_job_result
    import capo_snowball.types.cluster_id
    import capo_snowball.types.cluster_list_entry
    import capo_snowball.types.compatible_image
    import capo_snowball.types.create_address_request
    import capo_snowball.types.create_address_result
    import capo_snowball.types.create_cluster_request
    import capo_snowball.types.create_cluster_result
    import capo_snowball.types.create_job_request
    import capo_snowball.types.create_job_result
    import capo_snowball.types.create_long_term_pricing_request
    import capo_snowball.types.create_long_term_pricing_result
    import capo_snowball.types.create_return_shipping_label_request
    import capo_snowball.types.create_return_shipping_label_result
    import capo_snowball.types.dependent_service_list
    import capo_snowball.types.describe_address_request
    import capo_snowball.types.describe_address_result
    import capo_snowball.types.describe_addresses_request
    import capo_snowball.types.describe_addresses_result
    import capo_snowball.types.describe_cluster_request
    import capo_snowball.types.describe_cluster_result
    import capo_snowball.types.describe_job_request
    import capo_snowball.types.describe_job_result
    import capo_snowball.types.describe_return_shipping_label_request
    import capo_snowball.types.describe_return_shipping_label_result
    import capo_snowball.types.device_configuration
    import capo_snowball.types.get_job_manifest_request
    import capo_snowball.types.get_job_manifest_result
    import capo_snowball.types.get_job_unlock_code_request
    import capo_snowball.types.get_job_unlock_code_result
    import capo_snowball.types.get_snowball_usage_request
    import capo_snowball.types.get_snowball_usage_result
    import capo_snowball.types.get_software_updates_request
    import capo_snowball.types.get_software_updates_result
    import capo_snowball.types.impact_level
    import capo_snowball.types.initial_cluster_size
    import capo_snowball.types.java_boolean
    import capo_snowball.types.job_id
    import capo_snowball.types.job_list_entry
    import capo_snowball.types.job_resource
    import capo_snowball.types.job_type
    import capo_snowball.types.kms_key_arn
    import capo_snowball.types.list_cluster_jobs_request
    import capo_snowball.types.list_cluster_jobs_result
    import capo_snowball.types.list_clusters_request
    import capo_snowball.types.list_clusters_result
    import capo_snowball.types.list_compatible_images_request
    import capo_snowball.types.list_compatible_images_result
    import capo_snowball.types.list_jobs_request
    import capo_snowball.types.list_jobs_result
    import capo_snowball.types.list_limit
    import capo_snowball.types.list_long_term_pricing_request
    import capo_snowball.types.list_long_term_pricing_result
    import capo_snowball.types.list_pickup_locations_request
    import capo_snowball.types.list_pickup_locations_result
    import capo_snowball.types.list_service_versions_request
    import capo_snowball.types.list_service_versions_result
    import capo_snowball.types.long_term_pricing_id
    import capo_snowball.types.long_term_pricing_id_list
    import capo_snowball.types.long_term_pricing_list_entry
    import capo_snowball.types.long_term_pricing_type
    import capo_snowball.types.notification
    import capo_snowball.types.on_device_service_configuration
    import capo_snowball.types.pickup_details
    import capo_snowball.types.remote_management
    import capo_snowball.types.role_arn
    import capo_snowball.types.service_name
    import capo_snowball.types.shipment_state
    import capo_snowball.types.shipping_option
    import capo_snowball.types.snowball_capacity
    import capo_snowball.types.snowball_type
    import capo_snowball.types.string
    import capo_snowball.types.tax_documents
    import capo_snowball.types.update_cluster_request
    import capo_snowball.types.update_cluster_result
    import capo_snowball.types.update_job_request
    import capo_snowball.types.update_job_result
    import capo_snowball.types.update_job_shipment_state_request
    import capo_snowball.types.update_job_shipment_state_result
    import capo_snowball.types.update_long_term_pricing_request
    import capo_snowball.types.update_long_term_pricing_result


class SnowballClientConfig(TypedDict, total=False, closed=True):
    operation_interceptors: Iterable[Interceptor[Any, Any]]
    retry_max_attempts: int | None
    region: str | None
    use_dual_stack: bool | None
    use_fips: bool | None
    endpoint: str | None
    credentials_provider: IdentityProvider[Credentials] | None
    anonymous: bool | None


class SnowballClient:
    """A client for the ``Snowball`` service.

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
        self._config = SnowballClientConfig(
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
        self, config_overrides: Optional[SnowballClientConfig] = None
    ) -> tuple[Iterable[Interceptor[Any, Any]], OperationOptions]:
        overrides: SnowballClientConfig = config_overrides or {}
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

    def cancel_cluster(
        self,
        cluster_id: "capo_snowball.types.cluster_id.ClusterId",
        *,
        config_overrides: Optional[SnowballClientConfig] = None,
    ) -> "capo_snowball.types.cancel_cluster_result.CancelClusterResult":
        """<p>Cancels a cluster job. You can only cancel a cluster job while it's in the <code>AwaitingQuorum</code> status. You'll have at least an hour after creating a cluster job to cancel it.</p>

        Args:
            cluster_id: <p>The 39-character ID for the cluster that you want to cancel, for example <code>CID123e4567-e89b-12d3-a456-426655440000</code>.</p>

        Raises:
            capo_snowball.errors.invalid_job_state_exception.InvalidJobStateException: <p>The action can't be performed because the job's current state doesn't allow that action to be performed.</p>
            capo_snowball.errors.invalid_resource_exception.InvalidResourceException: <p>The specified resource can't be found. Check the information you provided in your last request, and try again.</p>
            capo_snowball.errors.kms_request_failed_exception.KMSRequestFailedException: <p>The provided Key Management Service key lacks the permissions to perform the specified <a>CreateJob</a> or <a>UpdateJob</a> action.</p>
            capo_snowball.errors.UnknownServiceError: The service returned an error code this client does not model.

        Examples:
            To cancel a cluster job
            This operation cancels a cluster job. You can only cancel a cluster job while it's in the AwaitingQuorum status.

            >>> client.cancel_cluster(cluster_id='CID123e4567-e89b-12d3-a456-426655440000')
        """

        def _handler(
            req: "OperationRequest[capo_snowball.types.cancel_cluster_request.CancelClusterRequest]",
        ) -> OperationResponse[
            "capo_snowball.types.cancel_cluster_result.CancelClusterResult"
        ]:
            import capo_snowball._operations.awsie_snowball_job_management_service.cancel_cluster

            output, http_response = (
                capo_snowball._operations.awsie_snowball_job_management_service.cancel_cluster.cancel_cluster(
                    req.options, req.input
                )
            )
            return OperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_snowball.types.cancel_cluster_request.CancelClusterRequest = {
            "cluster_id": cluster_id
        }

        response = execute_pipeline(
            OperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        response.response.close()
        return response.output

    def cancel_job(
        self,
        job_id: "capo_snowball.types.job_id.JobId",
        *,
        config_overrides: Optional[SnowballClientConfig] = None,
    ) -> "capo_snowball.types.cancel_job_result.CancelJobResult":
        """<p>Cancels the specified job. You can only cancel a job before its <code>JobState</code> value changes to <code>PreparingAppliance</code>. Requesting the <code>ListJobs</code> or <code>DescribeJob</code> action returns a job's <code>JobState</code> as part of the response element data returned.</p>

        Args:
            job_id: <p>The 39-character job ID for the job that you want to cancel, for example <code>JID123e4567-e89b-12d3-a456-426655440000</code>.</p>

        Raises:
            capo_snowball.errors.invalid_job_state_exception.InvalidJobStateException: <p>The action can't be performed because the job's current state doesn't allow that action to be performed.</p>
            capo_snowball.errors.invalid_resource_exception.InvalidResourceException: <p>The specified resource can't be found. Check the information you provided in your last request, and try again.</p>
            capo_snowball.errors.kms_request_failed_exception.KMSRequestFailedException: <p>The provided Key Management Service key lacks the permissions to perform the specified <a>CreateJob</a> or <a>UpdateJob</a> action.</p>
            capo_snowball.errors.UnknownServiceError: The service returned an error code this client does not model.

        Examples:
            To cancel a job for a Snowball device
            This operation cancels a job. You can only cancel a job before its JobState value changes to PreparingAppliance.

            >>> client.cancel_job(job_id='JID123e4567-e89b-12d3-a456-426655440000')
        """

        def _handler(
            req: "OperationRequest[capo_snowball.types.cancel_job_request.CancelJobRequest]",
        ) -> OperationResponse["capo_snowball.types.cancel_job_result.CancelJobResult"]:
            import capo_snowball._operations.awsie_snowball_job_management_service.cancel_job

            output, http_response = (
                capo_snowball._operations.awsie_snowball_job_management_service.cancel_job.cancel_job(
                    req.options, req.input
                )
            )
            return OperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_snowball.types.cancel_job_request.CancelJobRequest = {
            "job_id": job_id
        }

        response = execute_pipeline(
            OperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        response.response.close()
        return response.output

    def create_address(
        self,
        address: "capo_snowball.types.address.Address",
        *,
        config_overrides: Optional[SnowballClientConfig] = None,
    ) -> "capo_snowball.types.create_address_result.CreateAddressResult":
        """<p>Creates an address for a Snow device to be shipped to. In most regions, addresses are validated at the time of creation. The address you provide must be located within the serviceable area of your region. If the address is invalid or unsupported, then an exception is thrown. If providing an address as a JSON file through the <code>cli-input-json</code> option, include the full file path. For example, <code>--cli-input-json file://create-address.json</code>.</p>

        Args:
            address: <p>The address that you want the Snow device shipped to.</p>

        Raises:
            capo_snowball.errors.invalid_address_exception.InvalidAddressException: <p>The address provided was invalid. Check the address with your region's carrier, and try again.</p>
            capo_snowball.errors.unsupported_address_exception.UnsupportedAddressException: <p>The address is either outside the serviceable area for your region, or an error occurred. Check the address with your region's carrier and try again. If the issue persists, contact Amazon Web Services Support.</p>
            capo_snowball.errors.UnknownServiceError: The service returned an error code this client does not model.

        Examples:
            To create an address for a job
            This operation creates an address for a job. Addresses are validated at the time of creation. The address you provide must be located within the serviceable area of your region. If the address is invalid or unsupported, then an exception is thrown.

            >>> client.create_address(address={'City': 'Seattle', 'Company': "My Company's Name", 'Country': 'USA', 'Name': 'My Name', 'PhoneNumber': '425-555-5555', 'PostalCode': '98101', 'StateOrProvince': 'WA', 'Street1': '123 Main Street'})
        """

        def _handler(
            req: "OperationRequest[capo_snowball.types.create_address_request.CreateAddressRequest]",
        ) -> OperationResponse[
            "capo_snowball.types.create_address_result.CreateAddressResult"
        ]:
            import capo_snowball._operations.awsie_snowball_job_management_service.create_address

            output, http_response = (
                capo_snowball._operations.awsie_snowball_job_management_service.create_address.create_address(
                    req.options, req.input
                )
            )
            return OperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_snowball.types.create_address_request.CreateAddressRequest = {
            "address": address
        }

        response = execute_pipeline(
            OperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        response.response.close()
        return response.output

    def create_cluster(
        self,
        job_type: "capo_snowball.types.job_type.JobType",
        address_id: "capo_snowball.types.address_id.AddressId",
        snowball_type: "capo_snowball.types.snowball_type.SnowballType",
        shipping_option: "capo_snowball.types.shipping_option.ShippingOption",
        *,
        config_overrides: Optional[SnowballClientConfig] = None,
        resources: Optional["capo_snowball.types.job_resource.JobResource"] = None,
        on_device_service_configuration: Optional[
            "capo_snowball.types.on_device_service_configuration.OnDeviceServiceConfiguration"
        ] = None,
        description: Optional["capo_snowball.types.string.String"] = None,
        kms_key_arn: Optional["capo_snowball.types.kms_key_arn.KmsKeyARN"] = None,
        role_arn: Optional["capo_snowball.types.role_arn.RoleARN"] = None,
        notification: Optional["capo_snowball.types.notification.Notification"] = None,
        forwarding_address_id: Optional[
            "capo_snowball.types.address_id.AddressId"
        ] = None,
        tax_documents: Optional[
            "capo_snowball.types.tax_documents.TaxDocuments"
        ] = None,
        remote_management: Optional[
            "capo_snowball.types.remote_management.RemoteManagement"
        ] = None,
        initial_cluster_size: Optional[
            "capo_snowball.types.initial_cluster_size.InitialClusterSize"
        ] = None,
        force_create_jobs: Optional["capo_snowball.types.boolean.Boolean"] = None,
        long_term_pricing_ids: Optional[
            "capo_snowball.types.long_term_pricing_id_list.LongTermPricingIdList"
        ] = None,
        snowball_capacity_preference: Optional[
            "capo_snowball.types.snowball_capacity.SnowballCapacity"
        ] = None,
    ) -> "capo_snowball.types.create_cluster_result.CreateClusterResult":
        """<p>Creates an empty cluster. Each cluster supports five nodes. You use the <a>CreateJob</a> action separately to create the jobs for each of these nodes. The cluster does not ship until these five node jobs have been created.</p>

        Args:
            job_type: <p>The type of job for this cluster. Currently, the only job type supported for clusters is <code>LOCAL_USE</code>.</p> <p>For more information, see "https://docs.aws.amazon.com/snowball/latest/snowcone-guide/snow-device-types.html" (Snow Family Devices and Capacity) in the <i>Snowcone User Guide</i> or "https://docs.aws.amazon.com/snowball/latest/developer-guide/snow-device-types.html" (Snow Family Devices and Capacity) in the <i>Snowcone User Guide</i>.</p>
            resources: <p>The resources associated with the cluster job. These resources include Amazon S3 buckets and optional Lambda functions written in the Python language. </p>
            on_device_service_configuration: <p>Specifies the service or services on the Snow Family device that your transferred data will be exported from or imported into. Amazon Web Services Snow Family device clusters support Amazon S3 and NFS (Network File System).</p>
            description: <p>An optional description of this specific cluster, for example <code>Environmental Data Cluster-01</code>.</p>
            address_id: <p>The ID for the address that you want the cluster shipped to.</p>
            kms_key_arn: <p>The <code>KmsKeyARN</code> value that you want to associate with this cluster. <code>KmsKeyARN</code> values are created by using the <a href="https://docs.aws.amazon.com/kms/latest/APIReference/API_CreateKey.html">CreateKey</a> API action in Key Management Service (KMS). </p>
            role_arn: <p>The <code>RoleARN</code> that you want to associate with this cluster. <code>RoleArn</code> values are created by using the <a href="https://docs.aws.amazon.com/IAM/latest/APIReference/API_CreateRole.html">CreateRole</a> API action in Identity and Access Management (IAM).</p>
            snowball_type: <p>The type of Snow Family devices to use for this cluster. </p> <note> <p>For cluster jobs, Amazon Web Services Snow Family currently supports only the <code>EDGE</code> device type.</p> </note> <p>For more information, see "https://docs.aws.amazon.com/snowball/latest/snowcone-guide/snow-device-types.html" (Snow Family Devices and Capacity) in the <i>Snowcone User Guide</i> or "https://docs.aws.amazon.com/snowball/latest/developer-guide/snow-device-types.html" (Snow Family Devices and Capacity) in the <i>Snowcone User Guide</i>.</p>
            shipping_option: <p>The shipping speed for each node in this cluster. This speed doesn't dictate how soon you'll get each Snowball Edge device, rather it represents how quickly each device moves to its destination while in transit. Regional shipping speeds are as follows: </p> <ul> <li> <p>In Australia, you have access to express shipping. Typically, Snow devices shipped express are delivered in about a day.</p> </li> <li> <p>In the European Union (EU), you have access to express shipping. Typically, Snow devices shipped express are delivered in about a day. In addition, most countries in the EU have access to standard shipping, which typically takes less than a week, one way.</p> </li> <li> <p>In India, Snow devices are delivered in one to seven days.</p> </li> <li> <p>In the United States of America (US), you have access to one-day shipping and two-day shipping.</p> </li> </ul> <ul> <li> <p>In Australia, you have access to express shipping. Typically, devices shipped express are delivered in about a day.</p> </li> <li> <p>In the European Union (EU), you have access to express shipping. Typically, Snow devices shipped express are delivered in about a day. In addition, most countries in the EU have access to standard shipping, which typically takes less than a week, one way.</p> </li> <li> <p>In India, Snow devices are delivered in one to seven days.</p> </li> <li> <p>In the US, you have access to one-day shipping and two-day shipping.</p> </li> </ul>
            notification: <p>The Amazon Simple Notification Service (Amazon SNS) notification settings for this cluster.</p>
            forwarding_address_id: <p>The forwarding address ID for a cluster. This field is not supported in most regions.</p>
            tax_documents: <p>The tax documents required in your Amazon Web Services Region.</p>
            remote_management: <p>Allows you to securely operate and manage Snow devices in a cluster remotely from outside of your internal network. When set to <code>INSTALLED_AUTOSTART</code>, remote management will automatically be available when the device arrives at your location. Otherwise, you need to use the Snowball Client to manage the device.</p>
            initial_cluster_size: <p>If provided, each job will be automatically created and associated with the new cluster. If not provided, will be treated as 0.</p>
            force_create_jobs: <p>Force to create cluster when user attempts to overprovision or underprovision a cluster. A cluster is overprovisioned or underprovisioned if the initial size of the cluster is more (overprovisioned) or less (underprovisioned) than what needed to meet capacity requirement specified with <code>OnDeviceServiceConfiguration</code>.</p>
            long_term_pricing_ids: <p>Lists long-term pricing id that will be used to associate with jobs automatically created for the new cluster.</p>
            snowball_capacity_preference: <p>If your job is being created in one of the US regions, you have the option of specifying what size Snow device you'd like for this job. In all other regions, Snowballs come with 80 TB in storage capacity.</p> <p>For more information, see "https://docs.aws.amazon.com/snowball/latest/snowcone-guide/snow-device-types.html" (Snow Family Devices and Capacity) in the <i>Snowcone User Guide</i> or "https://docs.aws.amazon.com/snowball/latest/developer-guide/snow-device-types.html" (Snow Family Devices and Capacity) in the <i>Snowcone User Guide</i>.</p>

        Raises:
            capo_snowball.errors.ec2_request_failed_exception.Ec2RequestFailedException: <p>Your user lacks the necessary Amazon EC2 permissions to perform the attempted action.</p>
            capo_snowball.errors.invalid_input_combination_exception.InvalidInputCombinationException: <p>Job or cluster creation failed. One or more inputs were invalid. Confirm that the <a>CreateClusterRequest$SnowballType</a> value supports your <a>CreateJobRequest$JobType</a>, and try again.</p>
            capo_snowball.errors.invalid_resource_exception.InvalidResourceException: <p>The specified resource can't be found. Check the information you provided in your last request, and try again.</p>
            capo_snowball.errors.kms_request_failed_exception.KMSRequestFailedException: <p>The provided Key Management Service key lacks the permissions to perform the specified <a>CreateJob</a> or <a>UpdateJob</a> action.</p>
            capo_snowball.errors.UnknownServiceError: The service returned an error code this client does not model.

        Examples:
            To create a cluster
            Creates an empty cluster. Each cluster supports five nodes. You use the CreateJob action separately to create the jobs for each of these nodes. The cluster does not ship until these five node jobs have been created.

            >>> client.create_cluster(job_type='LOCAL_USE', resources={'S3Resources': [{'BucketArn': 'arn:aws:s3:::MyBucket', 'KeyRange': {}}]}, description='MyCluster', address_id='ADID1234ab12-3eec-4eb3-9be6-9374c10eb51b', kms_key_arn='arn:aws:kms:us-east-1:123456789012:key/abcd1234-12ab-34cd-56ef-123456123456', role_arn='arn:aws:iam::123456789012:role/snowball-import-S3-role', snowball_type='EDGE', shipping_option='SECOND_DAY', notification={'NotifyAll': False, 'JobStatesToNotify': []})
        """

        def _handler(
            req: "OperationRequest[capo_snowball.types.create_cluster_request.CreateClusterRequest]",
        ) -> OperationResponse[
            "capo_snowball.types.create_cluster_result.CreateClusterResult"
        ]:
            import capo_snowball._operations.awsie_snowball_job_management_service.create_cluster

            output, http_response = (
                capo_snowball._operations.awsie_snowball_job_management_service.create_cluster.create_cluster(
                    req.options, req.input
                )
            )
            return OperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_snowball.types.create_cluster_request.CreateClusterRequest = {
            "job_type": job_type,
            "address_id": address_id,
            "snowball_type": snowball_type,
            "shipping_option": shipping_option,
        }
        if resources is not None:
            input_["resources"] = resources
        if on_device_service_configuration is not None:
            input_["on_device_service_configuration"] = on_device_service_configuration
        if description is not None:
            input_["description"] = description
        if kms_key_arn is not None:
            input_["kms_key_arn"] = kms_key_arn
        if role_arn is not None:
            input_["role_arn"] = role_arn
        if notification is not None:
            input_["notification"] = notification
        if forwarding_address_id is not None:
            input_["forwarding_address_id"] = forwarding_address_id
        if tax_documents is not None:
            input_["tax_documents"] = tax_documents
        if remote_management is not None:
            input_["remote_management"] = remote_management
        if initial_cluster_size is not None:
            input_["initial_cluster_size"] = initial_cluster_size
        if force_create_jobs is not None:
            input_["force_create_jobs"] = force_create_jobs
        if long_term_pricing_ids is not None:
            input_["long_term_pricing_ids"] = long_term_pricing_ids
        if snowball_capacity_preference is not None:
            input_["snowball_capacity_preference"] = snowball_capacity_preference

        response = execute_pipeline(
            OperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        response.response.close()
        return response.output

    def create_job(
        self,
        *,
        config_overrides: Optional[SnowballClientConfig] = None,
        job_type: Optional["capo_snowball.types.job_type.JobType"] = None,
        resources: Optional["capo_snowball.types.job_resource.JobResource"] = None,
        on_device_service_configuration: Optional[
            "capo_snowball.types.on_device_service_configuration.OnDeviceServiceConfiguration"
        ] = None,
        description: Optional["capo_snowball.types.string.String"] = None,
        address_id: Optional["capo_snowball.types.address_id.AddressId"] = None,
        kms_key_arn: Optional["capo_snowball.types.kms_key_arn.KmsKeyARN"] = None,
        role_arn: Optional["capo_snowball.types.role_arn.RoleARN"] = None,
        snowball_capacity_preference: Optional[
            "capo_snowball.types.snowball_capacity.SnowballCapacity"
        ] = None,
        shipping_option: Optional[
            "capo_snowball.types.shipping_option.ShippingOption"
        ] = None,
        notification: Optional["capo_snowball.types.notification.Notification"] = None,
        cluster_id: Optional["capo_snowball.types.cluster_id.ClusterId"] = None,
        snowball_type: Optional[
            "capo_snowball.types.snowball_type.SnowballType"
        ] = None,
        forwarding_address_id: Optional[
            "capo_snowball.types.address_id.AddressId"
        ] = None,
        tax_documents: Optional[
            "capo_snowball.types.tax_documents.TaxDocuments"
        ] = None,
        device_configuration: Optional[
            "capo_snowball.types.device_configuration.DeviceConfiguration"
        ] = None,
        remote_management: Optional[
            "capo_snowball.types.remote_management.RemoteManagement"
        ] = None,
        long_term_pricing_id: Optional[
            "capo_snowball.types.long_term_pricing_id.LongTermPricingId"
        ] = None,
        impact_level: Optional["capo_snowball.types.impact_level.ImpactLevel"] = None,
        pickup_details: Optional[
            "capo_snowball.types.pickup_details.PickupDetails"
        ] = None,
    ) -> "capo_snowball.types.create_job_result.CreateJobResult":
        """<p>Creates a job to import or export data between Amazon S3 and your on-premises data center. Your Amazon Web Services account must have the right trust policies and permissions in place to create a job for a Snow device. If you're creating a job for a node in a cluster, you only need to provide the <code>clusterId</code> value; the other job attributes are inherited from the cluster. </p> <note> <p>Only the Snowball; Edge device type is supported when ordering clustered jobs.</p> <p>The device capacity is optional.</p> <p>Availability of device types differ by Amazon Web Services Region. For more information about Region availability, see <a href="https://aws.amazon.com/about-aws/global-infrastructure/regional-product-services/?p=ngi&loc=4">Amazon Web Services Regional Services</a>.</p> </note> <p></p> <p class="title"> <b>Snow Family devices and their capacities.</b> </p> <ul> <li> <p>Device type: <b>SNC1_SSD</b> </p> <ul> <li> <p>Capacity: T14</p> </li> <li> <p>Description: Snowcone </p> </li> </ul> <p></p> </li> <li> <p>Device type: <b>SNC1_HDD</b> </p> <ul> <li> <p>Capacity: T8</p> </li> <li> <p>Description: Snowcone </p> </li> </ul> <p></p> </li> <li> <p>Device type: <b>EDGE_S</b> </p> <ul> <li> <p>Capacity: T98</p> </li> <li> <p>Description: Snowball Edge Storage Optimized for data transfer only </p> </li> </ul> <p></p> </li> <li> <p>Device type: <b>EDGE_CG</b> </p> <ul> <li> <p>Capacity: T42</p> </li> <li> <p>Description: Snowball Edge Compute Optimized with GPU</p> </li> </ul> <p></p> </li> <li> <p>Device type: <b>EDGE_C</b> </p> <ul> <li> <p>Capacity: T42</p> </li> <li> <p>Description: Snowball Edge Compute Optimized without GPU</p> </li> </ul> <p></p> </li> <li> <p>Device type: <b>EDGE</b> </p> <ul> <li> <p>Capacity: T100</p> </li> <li> <p>Description: Snowball Edge Storage Optimized with EC2 Compute</p> </li> </ul> <note> <p>This device is replaced with T98.</p> </note> <p></p> </li> <li> <p>Device type: <b>STANDARD</b> </p> <ul> <li> <p>Capacity: T50</p> </li> <li> <p>Description: Original Snowball device</p> <note> <p>This device is only available in the Ningxia, Beijing, and Singapore Amazon Web Services Region </p> </note> </li> </ul> <p></p> </li> <li> <p>Device type: <b>STANDARD</b> </p> <ul> <li> <p>Capacity: T80</p> </li> <li> <p>Description: Original Snowball device</p> <note> <p>This device is only available in the Ningxia, Beijing, and Singapore Amazon Web Services Region. </p> </note> </li> </ul> <p></p> </li> <li> <p>Snow Family device type: <b>RACK_5U_C</b> </p> <ul> <li> <p>Capacity: T13 </p> </li> <li> <p>Description: Snowblade.</p> </li> </ul> </li> <li> <p>Device type: <b>V3_5S</b> </p> <ul> <li> <p>Capacity: T240</p> </li> <li> <p>Description: Snowball Edge Storage Optimized 210TB</p> </li> </ul> </li> </ul>

        Args:
            job_type: <p>Defines the type of job that you're creating. </p>
            resources: <p>Defines the Amazon S3 buckets associated with this job.</p> <p>With <code>IMPORT</code> jobs, you specify the bucket or buckets that your transferred data will be imported into.</p> <p>With <code>EXPORT</code> jobs, you specify the bucket or buckets that your transferred data will be exported from. Optionally, you can also specify a <code>KeyRange</code> value. If you choose to export a range, you define the length of the range by providing either an inclusive <code>BeginMarker</code> value, an inclusive <code>EndMarker</code> value, or both. Ranges are UTF-8 binary sorted.</p>
            on_device_service_configuration: <p>Specifies the service or services on the Snow Family device that your transferred data will be exported from or imported into. Amazon Web Services Snow Family supports Amazon S3 and NFS (Network File System) and the Amazon Web Services Storage Gateway service Tape Gateway type.</p>
            description: <p>Defines an optional description of this specific job, for example <code>Important Photos 2016-08-11</code>.</p>
            address_id: <p>The ID for the address that you want the Snow device shipped to.</p>
            kms_key_arn: <p>The <code>KmsKeyARN</code> that you want to associate with this job. <code>KmsKeyARN</code>s are created using the <a href="https://docs.aws.amazon.com/kms/latest/APIReference/API_CreateKey.html">CreateKey</a> Key Management Service (KMS) API action.</p>
            role_arn: <p>The <code>RoleARN</code> that you want to associate with this job. <code>RoleArn</code>s are created using the <a href="https://docs.aws.amazon.com/IAM/latest/APIReference/API_CreateRole.html">CreateRole</a> Identity and Access Management (IAM) API action.</p>
            snowball_capacity_preference: <p>If your job is being created in one of the US regions, you have the option of specifying what size Snow device you'd like for this job. In all other regions, Snowballs come with 80 TB in storage capacity.</p> <p>For more information, see "https://docs.aws.amazon.com/snowball/latest/snowcone-guide/snow-device-types.html" (Snow Family Devices and Capacity) in the <i>Snowcone User Guide</i> or "https://docs.aws.amazon.com/snowball/latest/developer-guide/snow-device-types.html" (Snow Family Devices and Capacity) in the <i>Snowcone User Guide</i>.</p>
            shipping_option: <p>The shipping speed for this job. This speed doesn't dictate how soon you'll get the Snow device, rather it represents how quickly the Snow device moves to its destination while in transit. Regional shipping speeds are as follows:</p> <ul> <li> <p>In Australia, you have access to express shipping. Typically, Snow devices shipped express are delivered in about a day.</p> </li> <li> <p>In the European Union (EU), you have access to express shipping. Typically, Snow devices shipped express are delivered in about a day. In addition, most countries in the EU have access to standard shipping, which typically takes less than a week, one way.</p> </li> <li> <p>In India, Snow devices are delivered in one to seven days.</p> </li> <li> <p>In the US, you have access to one-day shipping and two-day shipping.</p> </li> </ul>
            notification: <p>Defines the Amazon Simple Notification Service (Amazon SNS) notification settings for this job.</p>
            cluster_id: <p>The ID of a cluster. If you're creating a job for a node in a cluster, you need to provide only this <code>clusterId</code> value. The other job attributes are inherited from the cluster.</p>
            snowball_type: <p>The type of Snow Family devices to use for this job. </p> <note> <p>For cluster jobs, Amazon Web Services Snow Family currently supports only the <code>EDGE</code> device type.</p> </note> <p>The type of Amazon Web Services Snow device to use for this job. Currently, the only supported device type for cluster jobs is <code>EDGE</code>.</p> <p>For more information, see <a href="https://docs.aws.amazon.com/snowball/latest/developer-guide/device-differences.html">Snowball Edge Device Options</a> in the Snowball Edge Developer Guide.</p> <p>For more information, see "https://docs.aws.amazon.com/snowball/latest/snowcone-guide/snow-device-types.html" (Snow Family Devices and Capacity) in the <i>Snowcone User Guide</i> or "https://docs.aws.amazon.com/snowball/latest/developer-guide/snow-device-types.html" (Snow Family Devices and Capacity) in the <i>Snowcone User Guide</i>.</p>
            forwarding_address_id: <p>The forwarding address ID for a job. This field is not supported in most Regions.</p>
            tax_documents: <p>The tax documents required in your Amazon Web Services Region.</p>
            device_configuration: <p>Defines the device configuration for an Snowball Edge job.</p> <p>For more information, see "https://docs.aws.amazon.com/snowball/latest/snowcone-guide/snow-device-types.html" (Snow Family Devices and Capacity) in the <i>Snowcone User Guide</i> or "https://docs.aws.amazon.com/snowball/latest/developer-guide/snow-device-types.html" (Snow Family Devices and Capacity) in the <i>Snowcone User Guide</i>.</p>
            remote_management: <p>Allows you to securely operate and manage Snowcone devices remotely from outside of your internal network. When set to <code>INSTALLED_AUTOSTART</code>, remote management will automatically be available when the device arrives at your location. Otherwise, you need to use the Snowball Edge client to manage the device. When set to <code>NOT_INSTALLED</code>, remote management will not be available on the device. </p>
            long_term_pricing_id: <p>The ID of the long-term pricing type for the device.</p>
            impact_level: <p>The highest impact level of data that will be stored or processed on the device, provided at job creation.</p>
            pickup_details: <p>Information identifying the person picking up the device.</p>

        Raises:
            capo_snowball.errors.cluster_limit_exceeded_exception.ClusterLimitExceededException: <p>Job creation failed. Currently, clusters support five nodes. If you have fewer than five nodes for your cluster and you have more nodes to create for this cluster, try again and create jobs until your cluster has exactly five nodes.</p>
            capo_snowball.errors.ec2_request_failed_exception.Ec2RequestFailedException: <p>Your user lacks the necessary Amazon EC2 permissions to perform the attempted action.</p>
            capo_snowball.errors.invalid_input_combination_exception.InvalidInputCombinationException: <p>Job or cluster creation failed. One or more inputs were invalid. Confirm that the <a>CreateClusterRequest$SnowballType</a> value supports your <a>CreateJobRequest$JobType</a>, and try again.</p>
            capo_snowball.errors.invalid_resource_exception.InvalidResourceException: <p>The specified resource can't be found. Check the information you provided in your last request, and try again.</p>
            capo_snowball.errors.kms_request_failed_exception.KMSRequestFailedException: <p>The provided Key Management Service key lacks the permissions to perform the specified <a>CreateJob</a> or <a>UpdateJob</a> action.</p>
            capo_snowball.errors.UnknownServiceError: The service returned an error code this client does not model.

        Examples:
            To create a job
            Creates a job to import or export data between Amazon S3 and your on-premises data center. Your AWS account must have the right trust policies and permissions in place to create a job for Snowball. If you're creating a job for a node in a cluster, you only need to provide the clusterId value; the other job attributes are inherited from the cluster.

            >>> client.create_job(job_type='IMPORT', resources={'S3Resources': [{'BucketArn': 'arn:aws:s3:::MyBucket', 'KeyRange': {}}]}, description='My Job', address_id='ADID1234ab12-3eec-4eb3-9be6-9374c10eb51b', kms_key_arn='arn:aws:kms:us-east-1:123456789012:key/abcd1234-12ab-34cd-56ef-123456123456', role_arn='arn:aws:iam::123456789012:role/snowball-import-S3-role', snowball_capacity_preference='T80', shipping_option='SECOND_DAY', notification={'NotifyAll': False, 'JobStatesToNotify': []}, snowball_type='STANDARD')
        """

        def _handler(
            req: "OperationRequest[capo_snowball.types.create_job_request.CreateJobRequest]",
        ) -> OperationResponse["capo_snowball.types.create_job_result.CreateJobResult"]:
            import capo_snowball._operations.awsie_snowball_job_management_service.create_job

            output, http_response = (
                capo_snowball._operations.awsie_snowball_job_management_service.create_job.create_job(
                    req.options, req.input
                )
            )
            return OperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_snowball.types.create_job_request.CreateJobRequest = {}
        if job_type is not None:
            input_["job_type"] = job_type
        if resources is not None:
            input_["resources"] = resources
        if on_device_service_configuration is not None:
            input_["on_device_service_configuration"] = on_device_service_configuration
        if description is not None:
            input_["description"] = description
        if address_id is not None:
            input_["address_id"] = address_id
        if kms_key_arn is not None:
            input_["kms_key_arn"] = kms_key_arn
        if role_arn is not None:
            input_["role_arn"] = role_arn
        if snowball_capacity_preference is not None:
            input_["snowball_capacity_preference"] = snowball_capacity_preference
        if shipping_option is not None:
            input_["shipping_option"] = shipping_option
        if notification is not None:
            input_["notification"] = notification
        if cluster_id is not None:
            input_["cluster_id"] = cluster_id
        if snowball_type is not None:
            input_["snowball_type"] = snowball_type
        if forwarding_address_id is not None:
            input_["forwarding_address_id"] = forwarding_address_id
        if tax_documents is not None:
            input_["tax_documents"] = tax_documents
        if device_configuration is not None:
            input_["device_configuration"] = device_configuration
        if remote_management is not None:
            input_["remote_management"] = remote_management
        if long_term_pricing_id is not None:
            input_["long_term_pricing_id"] = long_term_pricing_id
        if impact_level is not None:
            input_["impact_level"] = impact_level
        if pickup_details is not None:
            input_["pickup_details"] = pickup_details

        response = execute_pipeline(
            OperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        response.response.close()
        return response.output

    def create_long_term_pricing(
        self,
        long_term_pricing_type: "capo_snowball.types.long_term_pricing_type.LongTermPricingType",
        snowball_type: "capo_snowball.types.snowball_type.SnowballType",
        *,
        config_overrides: Optional[SnowballClientConfig] = None,
        is_long_term_pricing_auto_renew: Optional[
            "capo_snowball.types.java_boolean.JavaBoolean"
        ] = None,
    ) -> "capo_snowball.types.create_long_term_pricing_result.CreateLongTermPricingResult":
        """<p>Creates a job with the long-term usage option for a device. The long-term usage is a 1-year or 3-year long-term pricing type for the device. You are billed upfront, and Amazon Web Services provides discounts for long-term pricing. </p>

        Args:
            long_term_pricing_type: <p>The type of long-term pricing option you want for the device, either 1-year or 3-year long-term pricing.</p>
            is_long_term_pricing_auto_renew: <p>Specifies whether the current long-term pricing type for the device should be renewed.</p>
            snowball_type: <p>The type of Snow Family devices to use for the long-term pricing job.</p>

        Raises:
            capo_snowball.errors.invalid_resource_exception.InvalidResourceException: <p>The specified resource can't be found. Check the information you provided in your last request, and try again.</p>
            capo_snowball.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        def _handler(
            req: "OperationRequest[capo_snowball.types.create_long_term_pricing_request.CreateLongTermPricingRequest]",
        ) -> OperationResponse[
            "capo_snowball.types.create_long_term_pricing_result.CreateLongTermPricingResult"
        ]:
            import capo_snowball._operations.awsie_snowball_job_management_service.create_long_term_pricing

            output, http_response = (
                capo_snowball._operations.awsie_snowball_job_management_service.create_long_term_pricing.create_long_term_pricing(
                    req.options, req.input
                )
            )
            return OperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_snowball.types.create_long_term_pricing_request.CreateLongTermPricingRequest = {
            "long_term_pricing_type": long_term_pricing_type,
            "snowball_type": snowball_type,
        }
        if is_long_term_pricing_auto_renew is not None:
            input_["is_long_term_pricing_auto_renew"] = is_long_term_pricing_auto_renew

        response = execute_pipeline(
            OperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        response.response.close()
        return response.output

    def create_return_shipping_label(
        self,
        job_id: "capo_snowball.types.job_id.JobId",
        *,
        config_overrides: Optional[SnowballClientConfig] = None,
        shipping_option: Optional[
            "capo_snowball.types.shipping_option.ShippingOption"
        ] = None,
    ) -> "capo_snowball.types.create_return_shipping_label_result.CreateReturnShippingLabelResult":
        """<p>Creates a shipping label that will be used to return the Snow device to Amazon Web Services.</p>

        Args:
            job_id: <p>The ID for a job that you want to create the return shipping label for; for example, <code>JID123e4567-e89b-12d3-a456-426655440000</code>.</p>
            shipping_option: <p>The shipping speed for a particular job. This speed doesn't dictate how soon the device is returned to Amazon Web Services. This speed represents how quickly it moves to its destination while in transit. Regional shipping speeds are as follows:</p>

        Raises:
            capo_snowball.errors.conflict_exception.ConflictException: <p>You get this exception when you call <code>CreateReturnShippingLabel</code> more than once when other requests are not completed.</p>
            capo_snowball.errors.invalid_input_combination_exception.InvalidInputCombinationException: <p>Job or cluster creation failed. One or more inputs were invalid. Confirm that the <a>CreateClusterRequest$SnowballType</a> value supports your <a>CreateJobRequest$JobType</a>, and try again.</p>
            capo_snowball.errors.invalid_job_state_exception.InvalidJobStateException: <p>The action can't be performed because the job's current state doesn't allow that action to be performed.</p>
            capo_snowball.errors.invalid_resource_exception.InvalidResourceException: <p>The specified resource can't be found. Check the information you provided in your last request, and try again.</p>
            capo_snowball.errors.return_shipping_label_already_exists_exception.ReturnShippingLabelAlreadyExistsException: <p>You get this exception if you call <code>CreateReturnShippingLabel</code> and a valid return shipping label already exists. In this case, use <code>DescribeReturnShippingLabel</code> to get the URL.</p>
            capo_snowball.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        def _handler(
            req: "OperationRequest[capo_snowball.types.create_return_shipping_label_request.CreateReturnShippingLabelRequest]",
        ) -> OperationResponse[
            "capo_snowball.types.create_return_shipping_label_result.CreateReturnShippingLabelResult"
        ]:
            import capo_snowball._operations.awsie_snowball_job_management_service.create_return_shipping_label

            output, http_response = (
                capo_snowball._operations.awsie_snowball_job_management_service.create_return_shipping_label.create_return_shipping_label(
                    req.options, req.input
                )
            )
            return OperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_snowball.types.create_return_shipping_label_request.CreateReturnShippingLabelRequest = {
            "job_id": job_id
        }
        if shipping_option is not None:
            input_["shipping_option"] = shipping_option

        response = execute_pipeline(
            OperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        response.response.close()
        return response.output

    def describe_address(
        self,
        address_id: "capo_snowball.types.address_id.AddressId",
        *,
        config_overrides: Optional[SnowballClientConfig] = None,
    ) -> "capo_snowball.types.describe_address_result.DescribeAddressResult":
        """<p>Takes an <code>AddressId</code> and returns specific details about that address in the form of an <code>Address</code> object.</p>

        Args:
            address_id: <p>The automatically generated ID for a specific address.</p>

        Raises:
            capo_snowball.errors.invalid_resource_exception.InvalidResourceException: <p>The specified resource can't be found. Check the information you provided in your last request, and try again.</p>
            capo_snowball.errors.UnknownServiceError: The service returned an error code this client does not model.

        Examples:
            To describe an address for a job
            This operation describes an address for a job.

            >>> client.describe_address(address_id='ADID1234ab12-3eec-4eb3-9be6-9374c10eb51b')
        """

        def _handler(
            req: "OperationRequest[capo_snowball.types.describe_address_request.DescribeAddressRequest]",
        ) -> OperationResponse[
            "capo_snowball.types.describe_address_result.DescribeAddressResult"
        ]:
            import capo_snowball._operations.awsie_snowball_job_management_service.describe_address

            output, http_response = (
                capo_snowball._operations.awsie_snowball_job_management_service.describe_address.describe_address(
                    req.options, req.input
                )
            )
            return OperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_snowball.types.describe_address_request.DescribeAddressRequest = {
            "address_id": address_id
        }

        response = execute_pipeline(
            OperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        response.response.close()
        return response.output

    def describe_addresses(
        self,
        *,
        config_overrides: Optional[SnowballClientConfig] = None,
        max_results: Optional["capo_snowball.types.list_limit.ListLimit"] = None,
        next_token: Optional["capo_snowball.types.string.String"] = None,
    ) -> "capo_snowball.types.describe_addresses_result.DescribeAddressesResult":
        """<p>Returns a specified number of <code>ADDRESS</code> objects. Calling this API in one of the US regions will return addresses from the list of all addresses associated with this account in all US regions.</p>

        Args:
            max_results: <p>The number of <code>ADDRESS</code> objects to return.</p>
            next_token: <p>HTTP requests are stateless. To identify what object comes "next" in the list of <code>ADDRESS</code> objects, you have the option of specifying a value for <code>NextToken</code> as the starting point for your list of returned addresses.</p>

        Raises:
            capo_snowball.errors.invalid_next_token_exception.InvalidNextTokenException: <p>The <code>NextToken</code> string was altered unexpectedly, and the operation has stopped. Run the operation without changing the <code>NextToken</code> string, and try again.</p>
            capo_snowball.errors.invalid_resource_exception.InvalidResourceException: <p>The specified resource can't be found. Check the information you provided in your last request, and try again.</p>
            capo_snowball.errors.UnknownServiceError: The service returned an error code this client does not model.

        Examples:
            To describe all the addresses you've created for AWS Snowball
            This operation describes all the addresses that you've created for AWS Snowball. Calling this API in one of the US regions will return addresses from the list of all addresses associated with this account in all US regions.

            >>> client.describe_addresses()
        """

        def _handler(
            req: "OperationRequest[capo_snowball.types.describe_addresses_request.DescribeAddressesRequest]",
        ) -> OperationResponse[
            "capo_snowball.types.describe_addresses_result.DescribeAddressesResult"
        ]:
            import capo_snowball._operations.awsie_snowball_job_management_service.describe_addresses

            output, http_response = (
                capo_snowball._operations.awsie_snowball_job_management_service.describe_addresses.describe_addresses(
                    req.options, req.input
                )
            )
            return OperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_snowball.types.describe_addresses_request.DescribeAddressesRequest = {}
        if max_results is not None:
            input_["max_results"] = max_results
        if next_token is not None:
            input_["next_token"] = next_token

        response = execute_pipeline(
            OperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        response.response.close()
        return response.output

    def iter_describe_addresses(
        self,
        *,
        config_overrides: Optional[SnowballClientConfig] = None,
        max_results: Optional["capo_snowball.types.list_limit.ListLimit"] = None,
        next_token: Optional["capo_snowball.types.string.String"] = None,
    ) -> "Iterator[capo_snowball.types.address.Address]":
        _token = next_token
        while True:
            _response = self.describe_addresses(
                config_overrides=config_overrides,
                max_results=max_results,
                next_token=_token,
            )
            _page = _resolve_path(_response, ("addresses",))
            for _item in _page or []:
                yield _item
            _token = _resolve_path(_response, ("next_token",))
            if not _token:
                break

    def describe_cluster(
        self,
        cluster_id: "capo_snowball.types.cluster_id.ClusterId",
        *,
        config_overrides: Optional[SnowballClientConfig] = None,
    ) -> "capo_snowball.types.describe_cluster_result.DescribeClusterResult":
        """<p>Returns information about a specific cluster including shipping information, cluster status, and other important metadata.</p>

        Args:
            cluster_id: <p>The automatically generated ID for a cluster.</p>

        Raises:
            capo_snowball.errors.invalid_resource_exception.InvalidResourceException: <p>The specified resource can't be found. Check the information you provided in your last request, and try again.</p>
            capo_snowball.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        def _handler(
            req: "OperationRequest[capo_snowball.types.describe_cluster_request.DescribeClusterRequest]",
        ) -> OperationResponse[
            "capo_snowball.types.describe_cluster_result.DescribeClusterResult"
        ]:
            import capo_snowball._operations.awsie_snowball_job_management_service.describe_cluster

            output, http_response = (
                capo_snowball._operations.awsie_snowball_job_management_service.describe_cluster.describe_cluster(
                    req.options, req.input
                )
            )
            return OperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_snowball.types.describe_cluster_request.DescribeClusterRequest = {
            "cluster_id": cluster_id
        }

        response = execute_pipeline(
            OperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        response.response.close()
        return response.output

    def describe_job(
        self,
        job_id: "capo_snowball.types.job_id.JobId",
        *,
        config_overrides: Optional[SnowballClientConfig] = None,
    ) -> "capo_snowball.types.describe_job_result.DescribeJobResult":
        """<p>Returns information about a specific job including shipping information, job status, and other important metadata. </p>

        Args:
            job_id: <p>The automatically generated ID for a job, for example <code>JID123e4567-e89b-12d3-a456-426655440000</code>.</p>

        Raises:
            capo_snowball.errors.invalid_resource_exception.InvalidResourceException: <p>The specified resource can't be found. Check the information you provided in your last request, and try again.</p>
            capo_snowball.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        def _handler(
            req: "OperationRequest[capo_snowball.types.describe_job_request.DescribeJobRequest]",
        ) -> OperationResponse[
            "capo_snowball.types.describe_job_result.DescribeJobResult"
        ]:
            import capo_snowball._operations.awsie_snowball_job_management_service.describe_job

            output, http_response = (
                capo_snowball._operations.awsie_snowball_job_management_service.describe_job.describe_job(
                    req.options, req.input
                )
            )
            return OperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_snowball.types.describe_job_request.DescribeJobRequest = {
            "job_id": job_id
        }

        response = execute_pipeline(
            OperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        response.response.close()
        return response.output

    def describe_return_shipping_label(
        self,
        job_id: "capo_snowball.types.job_id.JobId",
        *,
        config_overrides: Optional[SnowballClientConfig] = None,
    ) -> "capo_snowball.types.describe_return_shipping_label_result.DescribeReturnShippingLabelResult":
        """<p>Information on the shipping label of a Snow device that is being returned to Amazon Web Services.</p>

        Args:
            job_id: <p>The automatically generated ID for a job, for example <code>JID123e4567-e89b-12d3-a456-426655440000</code>.</p>

        Raises:
            capo_snowball.errors.conflict_exception.ConflictException: <p>You get this exception when you call <code>CreateReturnShippingLabel</code> more than once when other requests are not completed.</p>
            capo_snowball.errors.invalid_job_state_exception.InvalidJobStateException: <p>The action can't be performed because the job's current state doesn't allow that action to be performed.</p>
            capo_snowball.errors.invalid_resource_exception.InvalidResourceException: <p>The specified resource can't be found. Check the information you provided in your last request, and try again.</p>
            capo_snowball.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        def _handler(
            req: "OperationRequest[capo_snowball.types.describe_return_shipping_label_request.DescribeReturnShippingLabelRequest]",
        ) -> OperationResponse[
            "capo_snowball.types.describe_return_shipping_label_result.DescribeReturnShippingLabelResult"
        ]:
            import capo_snowball._operations.awsie_snowball_job_management_service.describe_return_shipping_label

            output, http_response = (
                capo_snowball._operations.awsie_snowball_job_management_service.describe_return_shipping_label.describe_return_shipping_label(
                    req.options, req.input
                )
            )
            return OperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_snowball.types.describe_return_shipping_label_request.DescribeReturnShippingLabelRequest = {
            "job_id": job_id
        }

        response = execute_pipeline(
            OperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        response.response.close()
        return response.output

    def get_job_manifest(
        self,
        job_id: "capo_snowball.types.job_id.JobId",
        *,
        config_overrides: Optional[SnowballClientConfig] = None,
    ) -> "capo_snowball.types.get_job_manifest_result.GetJobManifestResult":
        """<p>Returns a link to an Amazon S3 presigned URL for the manifest file associated with the specified <code>JobId</code> value. You can access the manifest file for up to 60 minutes after this request has been made. To access the manifest file after 60 minutes have passed, you'll have to make another call to the <code>GetJobManifest</code> action.</p> <p>The manifest is an encrypted file that you can download after your job enters the <code>WithCustomer</code> status. This is the only valid status for calling this API as the manifest and <code>UnlockCode</code> code value are used for securing your device and should only be used when you have the device. The manifest is decrypted by using the <code>UnlockCode</code> code value, when you pass both values to the Snow device through the Snowball client when the client is started for the first time. </p> <p>As a best practice, we recommend that you don't save a copy of an <code>UnlockCode</code> value in the same location as the manifest file for that job. Saving these separately helps prevent unauthorized parties from gaining access to the Snow device associated with that job.</p> <p>The credentials of a given job, including its manifest file and unlock code, expire 360 days after the job is created.</p>

                Args:
                    job_id: <p>The ID for a job that you want to get the manifest file for, for example <code>JID123e4567-e89b-12d3-a456-426655440000</code>.</p>

                Raises:
                    capo_snowball.errors.invalid_job_state_exception.InvalidJobStateException: <p>The action can't be performed because the job's current state doesn't allow that action to be performed.</p>
                    capo_snowball.errors.invalid_resource_exception.InvalidResourceException: <p>The specified resource can't be found. Check the information you provided in your last request, and try again.</p>
                    capo_snowball.errors.UnknownServiceError: The service returned an error code this client does not model.

                Examples:
                    To get the manifest for a job you've created for AWS Snowball
                    Returns a link to an Amazon S3 presigned URL for the manifest file associated with the specified JobId value. You can access the manifest file for up to 60 minutes after this request has been made. To access the manifest file after 60 minutes have passed, you'll have to make another call to the GetJobManifest action.

        The manifest is an encrypted file that you can download after your job enters the WithCustomer status. The manifest is decrypted by using the UnlockCode code value, when you pass both values to the Snowball through the Snowball client when the client is started for the first time.

        As a best practice, we recommend that you don't save a copy of an UnlockCode value in the same location as the manifest file for that job. Saving these separately helps prevent unauthorized parties from gaining access to the Snowball associated with that job.

        The credentials of a given job, including its manifest file and unlock code, expire 90 days after the job is created.

                    >>> client.get_job_manifest(job_id='JID123e4567-e89b-12d3-a456-426655440000')
        """

        def _handler(
            req: "OperationRequest[capo_snowball.types.get_job_manifest_request.GetJobManifestRequest]",
        ) -> OperationResponse[
            "capo_snowball.types.get_job_manifest_result.GetJobManifestResult"
        ]:
            import capo_snowball._operations.awsie_snowball_job_management_service.get_job_manifest

            output, http_response = (
                capo_snowball._operations.awsie_snowball_job_management_service.get_job_manifest.get_job_manifest(
                    req.options, req.input
                )
            )
            return OperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_snowball.types.get_job_manifest_request.GetJobManifestRequest = {
            "job_id": job_id
        }

        response = execute_pipeline(
            OperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        response.response.close()
        return response.output

    def get_job_unlock_code(
        self,
        job_id: "capo_snowball.types.job_id.JobId",
        *,
        config_overrides: Optional[SnowballClientConfig] = None,
    ) -> "capo_snowball.types.get_job_unlock_code_result.GetJobUnlockCodeResult":
        """<p>Returns the <code>UnlockCode</code> code value for the specified job. A particular <code>UnlockCode</code> value can be accessed for up to 360 days after the associated job has been created.</p> <p>The <code>UnlockCode</code> value is a 29-character code with 25 alphanumeric characters and 4 hyphens. This code is used to decrypt the manifest file when it is passed along with the manifest to the Snow device through the Snowball client when the client is started for the first time. The only valid status for calling this API is <code>WithCustomer</code> as the manifest and <code>Unlock</code> code values are used for securing your device and should only be used when you have the device.</p> <p>As a best practice, we recommend that you don't save a copy of the <code>UnlockCode</code> in the same location as the manifest file for that job. Saving these separately helps prevent unauthorized parties from gaining access to the Snow device associated with that job.</p>

                Args:
                    job_id: <p>The ID for the job that you want to get the <code>UnlockCode</code> value for, for example <code>JID123e4567-e89b-12d3-a456-426655440000</code>.</p>

                Raises:
                    capo_snowball.errors.invalid_job_state_exception.InvalidJobStateException: <p>The action can't be performed because the job's current state doesn't allow that action to be performed.</p>
                    capo_snowball.errors.invalid_resource_exception.InvalidResourceException: <p>The specified resource can't be found. Check the information you provided in your last request, and try again.</p>
                    capo_snowball.errors.UnknownServiceError: The service returned an error code this client does not model.

                Examples:
                    To get the unlock code for a job you've created for AWS Snowball
                    Returns the UnlockCode code value for the specified job. A particular UnlockCode value can be accessed for up to 90 days after the associated job has been created.

        The UnlockCode value is a 29-character code with 25 alphanumeric characters and 4 hyphens. This code is used to decrypt the manifest file when it is passed along with the manifest to the Snowball through the Snowball client when the client is started for the first time.

        As a best practice, we recommend that you don't save a copy of the UnlockCode in the same location as the manifest file for that job. Saving these separately helps prevent unauthorized parties from gaining access to the Snowball associated with that job.

                    >>> client.get_job_unlock_code(job_id='JID123e4567-e89b-12d3-a456-426655440000')
        """

        def _handler(
            req: "OperationRequest[capo_snowball.types.get_job_unlock_code_request.GetJobUnlockCodeRequest]",
        ) -> OperationResponse[
            "capo_snowball.types.get_job_unlock_code_result.GetJobUnlockCodeResult"
        ]:
            import capo_snowball._operations.awsie_snowball_job_management_service.get_job_unlock_code

            output, http_response = (
                capo_snowball._operations.awsie_snowball_job_management_service.get_job_unlock_code.get_job_unlock_code(
                    req.options, req.input
                )
            )
            return OperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_snowball.types.get_job_unlock_code_request.GetJobUnlockCodeRequest = {
            "job_id": job_id
        }

        response = execute_pipeline(
            OperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        response.response.close()
        return response.output

    def get_snowball_usage(
        self, *, config_overrides: Optional[SnowballClientConfig] = None
    ) -> "capo_snowball.types.get_snowball_usage_result.GetSnowballUsageResult":
        """<p>Returns information about the Snow Family service limit for your account, and also the number of Snow devices your account has in use.</p> <p>The default service limit for the number of Snow devices that you can have at one time is 1. If you want to increase your service limit, contact Amazon Web Services Support.</p>

                Raises:
                    capo_snowball.errors.UnknownServiceError: The service returned an error code this client does not model.

                Examples:
                    To see your Snowball service limit and the number of Snowballs you have in use
                    Returns information about the Snowball service limit for your account, and also the number of Snowballs your account has in use.

        The default service limit for the number of Snowballs that you can have at one time is 1. If you want to increase your service limit, contact AWS Support.

                    >>> client.get_snowball_usage()
        """

        def _handler(
            req: "OperationRequest[capo_snowball.types.get_snowball_usage_request.GetSnowballUsageRequest]",
        ) -> OperationResponse[
            "capo_snowball.types.get_snowball_usage_result.GetSnowballUsageResult"
        ]:
            import capo_snowball._operations.awsie_snowball_job_management_service.get_snowball_usage

            output, http_response = (
                capo_snowball._operations.awsie_snowball_job_management_service.get_snowball_usage.get_snowball_usage(
                    req.options, req.input
                )
            )
            return OperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_snowball.types.get_snowball_usage_request.GetSnowballUsageRequest = {}

        response = execute_pipeline(
            OperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        response.response.close()
        return response.output

    def get_software_updates(
        self,
        job_id: "capo_snowball.types.job_id.JobId",
        *,
        config_overrides: Optional[SnowballClientConfig] = None,
    ) -> "capo_snowball.types.get_software_updates_result.GetSoftwareUpdatesResult":
        """<p>Returns an Amazon S3 presigned URL for an update file associated with a specified <code>JobId</code>.</p>

        Args:
            job_id: <p>The ID for a job that you want to get the software update file for, for example <code>JID123e4567-e89b-12d3-a456-426655440000</code>.</p>

        Raises:
            capo_snowball.errors.invalid_job_state_exception.InvalidJobStateException: <p>The action can't be performed because the job's current state doesn't allow that action to be performed.</p>
            capo_snowball.errors.invalid_resource_exception.InvalidResourceException: <p>The specified resource can't be found. Check the information you provided in your last request, and try again.</p>
            capo_snowball.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        def _handler(
            req: "OperationRequest[capo_snowball.types.get_software_updates_request.GetSoftwareUpdatesRequest]",
        ) -> OperationResponse[
            "capo_snowball.types.get_software_updates_result.GetSoftwareUpdatesResult"
        ]:
            import capo_snowball._operations.awsie_snowball_job_management_service.get_software_updates

            output, http_response = (
                capo_snowball._operations.awsie_snowball_job_management_service.get_software_updates.get_software_updates(
                    req.options, req.input
                )
            )
            return OperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_snowball.types.get_software_updates_request.GetSoftwareUpdatesRequest = {
            "job_id": job_id
        }

        response = execute_pipeline(
            OperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        response.response.close()
        return response.output

    def list_cluster_jobs(
        self,
        cluster_id: "capo_snowball.types.cluster_id.ClusterId",
        *,
        config_overrides: Optional[SnowballClientConfig] = None,
        max_results: Optional["capo_snowball.types.list_limit.ListLimit"] = None,
        next_token: Optional["capo_snowball.types.string.String"] = None,
    ) -> "capo_snowball.types.list_cluster_jobs_result.ListClusterJobsResult":
        """<p>Returns an array of <code>JobListEntry</code> objects of the specified length. Each <code>JobListEntry</code> object is for a job in the specified cluster and contains a job's state, a job's ID, and other information.</p>

        Args:
            cluster_id: <p>The 39-character ID for the cluster that you want to list, for example <code>CID123e4567-e89b-12d3-a456-426655440000</code>.</p>
            max_results: <p>The number of <code>JobListEntry</code> objects to return.</p>
            next_token: <p>HTTP requests are stateless. To identify what object comes "next" in the list of <code>JobListEntry</code> objects, you have the option of specifying <code>NextToken</code> as the starting point for your returned list.</p>

        Raises:
            capo_snowball.errors.invalid_next_token_exception.InvalidNextTokenException: <p>The <code>NextToken</code> string was altered unexpectedly, and the operation has stopped. Run the operation without changing the <code>NextToken</code> string, and try again.</p>
            capo_snowball.errors.invalid_resource_exception.InvalidResourceException: <p>The specified resource can't be found. Check the information you provided in your last request, and try again.</p>
            capo_snowball.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        def _handler(
            req: "OperationRequest[capo_snowball.types.list_cluster_jobs_request.ListClusterJobsRequest]",
        ) -> OperationResponse[
            "capo_snowball.types.list_cluster_jobs_result.ListClusterJobsResult"
        ]:
            import capo_snowball._operations.awsie_snowball_job_management_service.list_cluster_jobs

            output, http_response = (
                capo_snowball._operations.awsie_snowball_job_management_service.list_cluster_jobs.list_cluster_jobs(
                    req.options, req.input
                )
            )
            return OperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_snowball.types.list_cluster_jobs_request.ListClusterJobsRequest = {
            "cluster_id": cluster_id
        }
        if max_results is not None:
            input_["max_results"] = max_results
        if next_token is not None:
            input_["next_token"] = next_token

        response = execute_pipeline(
            OperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        response.response.close()
        return response.output

    def iter_list_cluster_jobs(
        self,
        cluster_id: "capo_snowball.types.cluster_id.ClusterId",
        *,
        config_overrides: Optional[SnowballClientConfig] = None,
        max_results: Optional["capo_snowball.types.list_limit.ListLimit"] = None,
        next_token: Optional["capo_snowball.types.string.String"] = None,
    ) -> "Iterator[capo_snowball.types.job_list_entry.JobListEntry]":
        _token = next_token
        while True:
            _response = self.list_cluster_jobs(
                cluster_id,
                config_overrides=config_overrides,
                max_results=max_results,
                next_token=_token,
            )
            _page = _resolve_path(_response, ("job_list_entries",))
            for _item in _page or []:
                yield _item
            _token = _resolve_path(_response, ("next_token",))
            if not _token:
                break

    def list_clusters(
        self,
        *,
        config_overrides: Optional[SnowballClientConfig] = None,
        max_results: Optional["capo_snowball.types.list_limit.ListLimit"] = None,
        next_token: Optional["capo_snowball.types.string.String"] = None,
    ) -> "capo_snowball.types.list_clusters_result.ListClustersResult":
        """<p>Returns an array of <code>ClusterListEntry</code> objects of the specified length. Each <code>ClusterListEntry</code> object contains a cluster's state, a cluster's ID, and other important status information.</p>

        Args:
            max_results: <p>The number of <code>ClusterListEntry</code> objects to return.</p>
            next_token: <p>HTTP requests are stateless. To identify what object comes "next" in the list of <code>ClusterListEntry</code> objects, you have the option of specifying <code>NextToken</code> as the starting point for your returned list.</p>

        Raises:
            capo_snowball.errors.invalid_next_token_exception.InvalidNextTokenException: <p>The <code>NextToken</code> string was altered unexpectedly, and the operation has stopped. Run the operation without changing the <code>NextToken</code> string, and try again.</p>
            capo_snowball.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        def _handler(
            req: "OperationRequest[capo_snowball.types.list_clusters_request.ListClustersRequest]",
        ) -> OperationResponse[
            "capo_snowball.types.list_clusters_result.ListClustersResult"
        ]:
            import capo_snowball._operations.awsie_snowball_job_management_service.list_clusters

            output, http_response = (
                capo_snowball._operations.awsie_snowball_job_management_service.list_clusters.list_clusters(
                    req.options, req.input
                )
            )
            return OperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_snowball.types.list_clusters_request.ListClustersRequest = {}
        if max_results is not None:
            input_["max_results"] = max_results
        if next_token is not None:
            input_["next_token"] = next_token

        response = execute_pipeline(
            OperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        response.response.close()
        return response.output

    def iter_list_clusters(
        self,
        *,
        config_overrides: Optional[SnowballClientConfig] = None,
        max_results: Optional["capo_snowball.types.list_limit.ListLimit"] = None,
        next_token: Optional["capo_snowball.types.string.String"] = None,
    ) -> "Iterator[capo_snowball.types.cluster_list_entry.ClusterListEntry]":
        _token = next_token
        while True:
            _response = self.list_clusters(
                config_overrides=config_overrides,
                max_results=max_results,
                next_token=_token,
            )
            _page = _resolve_path(_response, ("cluster_list_entries",))
            for _item in _page or []:
                yield _item
            _token = _resolve_path(_response, ("next_token",))
            if not _token:
                break

    def list_compatible_images(
        self,
        *,
        config_overrides: Optional[SnowballClientConfig] = None,
        max_results: Optional["capo_snowball.types.list_limit.ListLimit"] = None,
        next_token: Optional["capo_snowball.types.string.String"] = None,
    ) -> "capo_snowball.types.list_compatible_images_result.ListCompatibleImagesResult":
        """<p>This action returns a list of the different Amazon EC2-compatible Amazon Machine Images (AMIs) that are owned by your Amazon Web Services accountthat would be supported for use on a Snow device. Currently, supported AMIs are based on the Amazon Linux-2, Ubuntu 20.04 LTS - Focal, or Ubuntu 22.04 LTS - Jammy images, available on the Amazon Web Services Marketplace. Ubuntu 16.04 LTS - Xenial (HVM) images are no longer supported in the Market, but still supported for use on devices through Amazon EC2 VM Import/Export and running locally in AMIs.</p>

        Args:
            max_results: <p>The maximum number of results for the list of compatible images. Currently, a Snowball Edge device can store 10 AMIs.</p>
            next_token: <p>HTTP requests are stateless. To identify what object comes "next" in the list of compatible images, you can specify a value for <code>NextToken</code> as the starting point for your list of returned images.</p>

        Raises:
            capo_snowball.errors.ec2_request_failed_exception.Ec2RequestFailedException: <p>Your user lacks the necessary Amazon EC2 permissions to perform the attempted action.</p>
            capo_snowball.errors.invalid_next_token_exception.InvalidNextTokenException: <p>The <code>NextToken</code> string was altered unexpectedly, and the operation has stopped. Run the operation without changing the <code>NextToken</code> string, and try again.</p>
            capo_snowball.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        def _handler(
            req: "OperationRequest[capo_snowball.types.list_compatible_images_request.ListCompatibleImagesRequest]",
        ) -> OperationResponse[
            "capo_snowball.types.list_compatible_images_result.ListCompatibleImagesResult"
        ]:
            import capo_snowball._operations.awsie_snowball_job_management_service.list_compatible_images

            output, http_response = (
                capo_snowball._operations.awsie_snowball_job_management_service.list_compatible_images.list_compatible_images(
                    req.options, req.input
                )
            )
            return OperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_snowball.types.list_compatible_images_request.ListCompatibleImagesRequest = {}
        if max_results is not None:
            input_["max_results"] = max_results
        if next_token is not None:
            input_["next_token"] = next_token

        response = execute_pipeline(
            OperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        response.response.close()
        return response.output

    def iter_list_compatible_images(
        self,
        *,
        config_overrides: Optional[SnowballClientConfig] = None,
        max_results: Optional["capo_snowball.types.list_limit.ListLimit"] = None,
        next_token: Optional["capo_snowball.types.string.String"] = None,
    ) -> "Iterator[capo_snowball.types.compatible_image.CompatibleImage]":
        _token = next_token
        while True:
            _response = self.list_compatible_images(
                config_overrides=config_overrides,
                max_results=max_results,
                next_token=_token,
            )
            _page = _resolve_path(_response, ("compatible_images",))
            for _item in _page or []:
                yield _item
            _token = _resolve_path(_response, ("next_token",))
            if not _token:
                break

    def list_jobs(
        self,
        *,
        config_overrides: Optional[SnowballClientConfig] = None,
        max_results: Optional["capo_snowball.types.list_limit.ListLimit"] = None,
        next_token: Optional["capo_snowball.types.string.String"] = None,
    ) -> "capo_snowball.types.list_jobs_result.ListJobsResult":
        """<p>Returns an array of <code>JobListEntry</code> objects of the specified length. Each <code>JobListEntry</code> object contains a job's state, a job's ID, and a value that indicates whether the job is a job part, in the case of export jobs. Calling this API action in one of the US regions will return jobs from the list of all jobs associated with this account in all US regions.</p>

        Args:
            max_results: <p>The number of <code>JobListEntry</code> objects to return.</p>
            next_token: <p>HTTP requests are stateless. To identify what object comes "next" in the list of <code>JobListEntry</code> objects, you have the option of specifying <code>NextToken</code> as the starting point for your returned list.</p>

        Raises:
            capo_snowball.errors.invalid_next_token_exception.InvalidNextTokenException: <p>The <code>NextToken</code> string was altered unexpectedly, and the operation has stopped. Run the operation without changing the <code>NextToken</code> string, and try again.</p>
            capo_snowball.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        def _handler(
            req: "OperationRequest[capo_snowball.types.list_jobs_request.ListJobsRequest]",
        ) -> OperationResponse["capo_snowball.types.list_jobs_result.ListJobsResult"]:
            import capo_snowball._operations.awsie_snowball_job_management_service.list_jobs

            output, http_response = (
                capo_snowball._operations.awsie_snowball_job_management_service.list_jobs.list_jobs(
                    req.options, req.input
                )
            )
            return OperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_snowball.types.list_jobs_request.ListJobsRequest = {}
        if max_results is not None:
            input_["max_results"] = max_results
        if next_token is not None:
            input_["next_token"] = next_token

        response = execute_pipeline(
            OperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        response.response.close()
        return response.output

    def iter_list_jobs(
        self,
        *,
        config_overrides: Optional[SnowballClientConfig] = None,
        max_results: Optional["capo_snowball.types.list_limit.ListLimit"] = None,
        next_token: Optional["capo_snowball.types.string.String"] = None,
    ) -> "Iterator[capo_snowball.types.job_list_entry.JobListEntry]":
        _token = next_token
        while True:
            _response = self.list_jobs(
                config_overrides=config_overrides,
                max_results=max_results,
                next_token=_token,
            )
            _page = _resolve_path(_response, ("job_list_entries",))
            for _item in _page or []:
                yield _item
            _token = _resolve_path(_response, ("next_token",))
            if not _token:
                break

    def list_long_term_pricing(
        self,
        *,
        config_overrides: Optional[SnowballClientConfig] = None,
        max_results: Optional["capo_snowball.types.list_limit.ListLimit"] = None,
        next_token: Optional["capo_snowball.types.string.String"] = None,
    ) -> "capo_snowball.types.list_long_term_pricing_result.ListLongTermPricingResult":
        """<p>Lists all long-term pricing types.</p>

        Args:
            max_results: <p>The maximum number of <code>ListLongTermPricing</code> objects to return.</p>
            next_token: <p>Because HTTP requests are stateless, this is the starting point for your next list of <code>ListLongTermPricing</code> to return.</p>

        Raises:
            capo_snowball.errors.invalid_next_token_exception.InvalidNextTokenException: <p>The <code>NextToken</code> string was altered unexpectedly, and the operation has stopped. Run the operation without changing the <code>NextToken</code> string, and try again.</p>
            capo_snowball.errors.invalid_resource_exception.InvalidResourceException: <p>The specified resource can't be found. Check the information you provided in your last request, and try again.</p>
            capo_snowball.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        def _handler(
            req: "OperationRequest[capo_snowball.types.list_long_term_pricing_request.ListLongTermPricingRequest]",
        ) -> OperationResponse[
            "capo_snowball.types.list_long_term_pricing_result.ListLongTermPricingResult"
        ]:
            import capo_snowball._operations.awsie_snowball_job_management_service.list_long_term_pricing

            output, http_response = (
                capo_snowball._operations.awsie_snowball_job_management_service.list_long_term_pricing.list_long_term_pricing(
                    req.options, req.input
                )
            )
            return OperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_snowball.types.list_long_term_pricing_request.ListLongTermPricingRequest = {}
        if max_results is not None:
            input_["max_results"] = max_results
        if next_token is not None:
            input_["next_token"] = next_token

        response = execute_pipeline(
            OperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        response.response.close()
        return response.output

    def iter_list_long_term_pricing(
        self,
        *,
        config_overrides: Optional[SnowballClientConfig] = None,
        max_results: Optional["capo_snowball.types.list_limit.ListLimit"] = None,
        next_token: Optional["capo_snowball.types.string.String"] = None,
    ) -> "Iterator[capo_snowball.types.long_term_pricing_list_entry.LongTermPricingListEntry]":
        _token = next_token
        while True:
            _response = self.list_long_term_pricing(
                config_overrides=config_overrides,
                max_results=max_results,
                next_token=_token,
            )
            _page = _resolve_path(_response, ("long_term_pricing_entries",))
            for _item in _page or []:
                yield _item
            _token = _resolve_path(_response, ("next_token",))
            if not _token:
                break

    def list_pickup_locations(
        self,
        *,
        config_overrides: Optional[SnowballClientConfig] = None,
        max_results: Optional["capo_snowball.types.list_limit.ListLimit"] = None,
        next_token: Optional["capo_snowball.types.string.String"] = None,
    ) -> "capo_snowball.types.list_pickup_locations_result.ListPickupLocationsResult":
        """<p>A list of locations from which the customer can choose to pickup a device.</p>

        Args:
            max_results: <p>The maximum number of locations to list per page.</p>
            next_token: <p>HTTP requests are stateless. To identify what object comes "next" in the list of <code>ListPickupLocationsRequest</code> objects, you have the option of specifying <code>NextToken</code> as the starting point for your returned list.</p>

        Raises:
            capo_snowball.errors.invalid_resource_exception.InvalidResourceException: <p>The specified resource can't be found. Check the information you provided in your last request, and try again.</p>
            capo_snowball.errors.UnknownServiceError: The service returned an error code this client does not model.

        Examples:
            To get a list of locations from which the customer can choose to pickup a device.
            Returns a specified number of Address objects. Each Address is a pickup location address for Snow Family devices.

            >>> client.list_pickup_locations()
        """

        def _handler(
            req: "OperationRequest[capo_snowball.types.list_pickup_locations_request.ListPickupLocationsRequest]",
        ) -> OperationResponse[
            "capo_snowball.types.list_pickup_locations_result.ListPickupLocationsResult"
        ]:
            import capo_snowball._operations.awsie_snowball_job_management_service.list_pickup_locations

            output, http_response = (
                capo_snowball._operations.awsie_snowball_job_management_service.list_pickup_locations.list_pickup_locations(
                    req.options, req.input
                )
            )
            return OperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_snowball.types.list_pickup_locations_request.ListPickupLocationsRequest = {}
        if max_results is not None:
            input_["max_results"] = max_results
        if next_token is not None:
            input_["next_token"] = next_token

        response = execute_pipeline(
            OperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        response.response.close()
        return response.output

    def iter_list_pickup_locations(
        self,
        *,
        config_overrides: Optional[SnowballClientConfig] = None,
        max_results: Optional["capo_snowball.types.list_limit.ListLimit"] = None,
        next_token: Optional["capo_snowball.types.string.String"] = None,
    ) -> "Iterator[capo_snowball.types.list_pickup_locations_result.ListPickupLocationsResult]":
        _token = next_token
        while True:
            _response = self.list_pickup_locations(
                config_overrides=config_overrides,
                max_results=max_results,
                next_token=_token,
            )
            yield _response
            _token = _resolve_path(_response, ("next_token",))
            if not _token:
                break

    def list_service_versions(
        self,
        service_name: "capo_snowball.types.service_name.ServiceName",
        *,
        config_overrides: Optional[SnowballClientConfig] = None,
        dependent_services: Optional[
            "capo_snowball.types.dependent_service_list.DependentServiceList"
        ] = None,
        max_results: Optional["capo_snowball.types.list_limit.ListLimit"] = None,
        next_token: Optional["capo_snowball.types.string.String"] = None,
    ) -> "capo_snowball.types.list_service_versions_result.ListServiceVersionsResult":
        """<p>Lists all supported versions for Snow on-device services. Returns an array of <code>ServiceVersion</code> object containing the supported versions for a particular service.</p>

        Args:
            service_name: <p>The name of the service for which you're requesting supported versions.</p>
            dependent_services: <p>A list of names and versions of dependant services of the requested service.</p>
            max_results: <p>The maximum number of <code>ListServiceVersions</code> objects to return.</p>
            next_token: <p>Because HTTP requests are stateless, this is the starting point for the next list of returned <code>ListServiceVersionsRequest</code> versions.</p>

        Raises:
            capo_snowball.errors.invalid_next_token_exception.InvalidNextTokenException: <p>The <code>NextToken</code> string was altered unexpectedly, and the operation has stopped. Run the operation without changing the <code>NextToken</code> string, and try again.</p>
            capo_snowball.errors.invalid_resource_exception.InvalidResourceException: <p>The specified resource can't be found. Check the information you provided in your last request, and try again.</p>
            capo_snowball.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        def _handler(
            req: "OperationRequest[capo_snowball.types.list_service_versions_request.ListServiceVersionsRequest]",
        ) -> OperationResponse[
            "capo_snowball.types.list_service_versions_result.ListServiceVersionsResult"
        ]:
            import capo_snowball._operations.awsie_snowball_job_management_service.list_service_versions

            output, http_response = (
                capo_snowball._operations.awsie_snowball_job_management_service.list_service_versions.list_service_versions(
                    req.options, req.input
                )
            )
            return OperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_snowball.types.list_service_versions_request.ListServiceVersionsRequest = {
            "service_name": service_name
        }
        if dependent_services is not None:
            input_["dependent_services"] = dependent_services
        if max_results is not None:
            input_["max_results"] = max_results
        if next_token is not None:
            input_["next_token"] = next_token

        response = execute_pipeline(
            OperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        response.response.close()
        return response.output

    def update_cluster(
        self,
        cluster_id: "capo_snowball.types.cluster_id.ClusterId",
        *,
        config_overrides: Optional[SnowballClientConfig] = None,
        role_arn: Optional["capo_snowball.types.role_arn.RoleARN"] = None,
        description: Optional["capo_snowball.types.string.String"] = None,
        resources: Optional["capo_snowball.types.job_resource.JobResource"] = None,
        on_device_service_configuration: Optional[
            "capo_snowball.types.on_device_service_configuration.OnDeviceServiceConfiguration"
        ] = None,
        address_id: Optional["capo_snowball.types.address_id.AddressId"] = None,
        shipping_option: Optional[
            "capo_snowball.types.shipping_option.ShippingOption"
        ] = None,
        notification: Optional["capo_snowball.types.notification.Notification"] = None,
        forwarding_address_id: Optional[
            "capo_snowball.types.address_id.AddressId"
        ] = None,
    ) -> "capo_snowball.types.update_cluster_result.UpdateClusterResult":
        """<p>While a cluster's <code>ClusterState</code> value is in the <code>AwaitingQuorum</code> state, you can update some of the information associated with a cluster. Once the cluster changes to a different job state, usually 60 minutes after the cluster being created, this action is no longer available.</p>

        Args:
            cluster_id: <p>The cluster ID of the cluster that you want to update, for example <code>CID123e4567-e89b-12d3-a456-426655440000</code>.</p>
            role_arn: <p>The new role Amazon Resource Name (ARN) that you want to associate with this cluster. To create a role ARN, use the <a href="https://docs.aws.amazon.com/IAM/latest/APIReference/API_CreateRole.html">CreateRole</a> API action in Identity and Access Management (IAM).</p>
            description: <p>The updated description of this cluster.</p>
            resources: <p>The updated arrays of <a>JobResource</a> objects that can include updated <a>S3Resource</a> objects or <a>LambdaResource</a> objects.</p>
            on_device_service_configuration: <p>Specifies the service or services on the Snow Family device that your transferred data will be exported from or imported into. Amazon Web Services Snow Family device clusters support Amazon S3 and NFS (Network File System).</p>
            address_id: <p>The ID of the updated <a>Address</a> object.</p>
            shipping_option: <p>The updated shipping option value of this cluster's <a>ShippingDetails</a> object.</p>
            notification: <p>The new or updated <a>Notification</a> object.</p>
            forwarding_address_id: <p>The updated ID for the forwarding address for a cluster. This field is not supported in most regions.</p>

        Raises:
            capo_snowball.errors.ec2_request_failed_exception.Ec2RequestFailedException: <p>Your user lacks the necessary Amazon EC2 permissions to perform the attempted action.</p>
            capo_snowball.errors.invalid_input_combination_exception.InvalidInputCombinationException: <p>Job or cluster creation failed. One or more inputs were invalid. Confirm that the <a>CreateClusterRequest$SnowballType</a> value supports your <a>CreateJobRequest$JobType</a>, and try again.</p>
            capo_snowball.errors.invalid_job_state_exception.InvalidJobStateException: <p>The action can't be performed because the job's current state doesn't allow that action to be performed.</p>
            capo_snowball.errors.invalid_resource_exception.InvalidResourceException: <p>The specified resource can't be found. Check the information you provided in your last request, and try again.</p>
            capo_snowball.errors.kms_request_failed_exception.KMSRequestFailedException: <p>The provided Key Management Service key lacks the permissions to perform the specified <a>CreateJob</a> or <a>UpdateJob</a> action.</p>
            capo_snowball.errors.UnknownServiceError: The service returned an error code this client does not model.

        Examples:
            To update a cluster
            This action allows you to update certain parameters for a cluster. Once the cluster changes to a different state, usually within 60 minutes of it being created, this action is no longer available.

            >>> client.update_cluster(cluster_id='CID123e4567-e89b-12d3-a456-426655440000', description='updated-cluster-name', address_id='ADID1234ab12-3eec-4eb3-9be6-9374c10eb51b')
        """

        def _handler(
            req: "OperationRequest[capo_snowball.types.update_cluster_request.UpdateClusterRequest]",
        ) -> OperationResponse[
            "capo_snowball.types.update_cluster_result.UpdateClusterResult"
        ]:
            import capo_snowball._operations.awsie_snowball_job_management_service.update_cluster

            output, http_response = (
                capo_snowball._operations.awsie_snowball_job_management_service.update_cluster.update_cluster(
                    req.options, req.input
                )
            )
            return OperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_snowball.types.update_cluster_request.UpdateClusterRequest = {
            "cluster_id": cluster_id
        }
        if role_arn is not None:
            input_["role_arn"] = role_arn
        if description is not None:
            input_["description"] = description
        if resources is not None:
            input_["resources"] = resources
        if on_device_service_configuration is not None:
            input_["on_device_service_configuration"] = on_device_service_configuration
        if address_id is not None:
            input_["address_id"] = address_id
        if shipping_option is not None:
            input_["shipping_option"] = shipping_option
        if notification is not None:
            input_["notification"] = notification
        if forwarding_address_id is not None:
            input_["forwarding_address_id"] = forwarding_address_id

        response = execute_pipeline(
            OperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        response.response.close()
        return response.output

    def update_job(
        self,
        job_id: "capo_snowball.types.job_id.JobId",
        *,
        config_overrides: Optional[SnowballClientConfig] = None,
        role_arn: Optional["capo_snowball.types.role_arn.RoleARN"] = None,
        notification: Optional["capo_snowball.types.notification.Notification"] = None,
        resources: Optional["capo_snowball.types.job_resource.JobResource"] = None,
        on_device_service_configuration: Optional[
            "capo_snowball.types.on_device_service_configuration.OnDeviceServiceConfiguration"
        ] = None,
        address_id: Optional["capo_snowball.types.address_id.AddressId"] = None,
        shipping_option: Optional[
            "capo_snowball.types.shipping_option.ShippingOption"
        ] = None,
        description: Optional["capo_snowball.types.string.String"] = None,
        snowball_capacity_preference: Optional[
            "capo_snowball.types.snowball_capacity.SnowballCapacity"
        ] = None,
        forwarding_address_id: Optional[
            "capo_snowball.types.address_id.AddressId"
        ] = None,
        pickup_details: Optional[
            "capo_snowball.types.pickup_details.PickupDetails"
        ] = None,
    ) -> "capo_snowball.types.update_job_result.UpdateJobResult":
        """<p>While a job's <code>JobState</code> value is <code>New</code>, you can update some of the information associated with a job. Once the job changes to a different job state, usually within 60 minutes of the job being created, this action is no longer available.</p>

        Args:
            job_id: <p>The job ID of the job that you want to update, for example <code>JID123e4567-e89b-12d3-a456-426655440000</code>.</p>
            role_arn: <p>The new role Amazon Resource Name (ARN) that you want to associate with this job. To create a role ARN, use the <a href="https://docs.aws.amazon.com/IAM/latest/APIReference/API_CreateRole.html">CreateRole</a>Identity and Access Management (IAM) API action.</p>
            notification: <p>The new or updated <a>Notification</a> object.</p>
            resources: <p>The updated <code>JobResource</code> object, or the updated <a>JobResource</a> object. </p>
            on_device_service_configuration: <p>Specifies the service or services on the Snow Family device that your transferred data will be exported from or imported into. Amazon Web Services Snow Family supports Amazon S3 and NFS (Network File System) and the Amazon Web Services Storage Gateway service Tape Gateway type.</p>
            address_id: <p>The ID of the updated <a>Address</a> object.</p>
            shipping_option: <p>The updated shipping option value of this job's <a>ShippingDetails</a> object.</p>
            description: <p>The updated description of this job's <a>JobMetadata</a> object.</p>
            snowball_capacity_preference: <p>The updated <code>SnowballCapacityPreference</code> of this job's <a>JobMetadata</a> object. The 50 TB Snowballs are only available in the US regions.</p> <p>For more information, see "https://docs.aws.amazon.com/snowball/latest/snowcone-guide/snow-device-types.html" (Snow Family Devices and Capacity) in the <i>Snowcone User Guide</i> or "https://docs.aws.amazon.com/snowball/latest/developer-guide/snow-device-types.html" (Snow Family Devices and Capacity) in the <i>Snowcone User Guide</i>.</p>
            forwarding_address_id: <p>The updated ID for the forwarding address for a job. This field is not supported in most regions.</p>

        Raises:
            capo_snowball.errors.cluster_limit_exceeded_exception.ClusterLimitExceededException: <p>Job creation failed. Currently, clusters support five nodes. If you have fewer than five nodes for your cluster and you have more nodes to create for this cluster, try again and create jobs until your cluster has exactly five nodes.</p>
            capo_snowball.errors.ec2_request_failed_exception.Ec2RequestFailedException: <p>Your user lacks the necessary Amazon EC2 permissions to perform the attempted action.</p>
            capo_snowball.errors.invalid_input_combination_exception.InvalidInputCombinationException: <p>Job or cluster creation failed. One or more inputs were invalid. Confirm that the <a>CreateClusterRequest$SnowballType</a> value supports your <a>CreateJobRequest$JobType</a>, and try again.</p>
            capo_snowball.errors.invalid_job_state_exception.InvalidJobStateException: <p>The action can't be performed because the job's current state doesn't allow that action to be performed.</p>
            capo_snowball.errors.invalid_resource_exception.InvalidResourceException: <p>The specified resource can't be found. Check the information you provided in your last request, and try again.</p>
            capo_snowball.errors.kms_request_failed_exception.KMSRequestFailedException: <p>The provided Key Management Service key lacks the permissions to perform the specified <a>CreateJob</a> or <a>UpdateJob</a> action.</p>
            capo_snowball.errors.UnknownServiceError: The service returned an error code this client does not model.

        Examples:
            To update a job
            This action allows you to update certain parameters for a job. Once the job changes to a different job state, usually within 60 minutes of the job being created, this action is no longer available.

            >>> client.update_job(job_id='JID123e4567-e89b-12d3-a456-426655440000', address_id='ADID1234ab12-3eec-4eb3-9be6-9374c10eb51b', shipping_option='NEXT_DAY', description='updated-job-name', snowball_capacity_preference='T100')
        """

        def _handler(
            req: "OperationRequest[capo_snowball.types.update_job_request.UpdateJobRequest]",
        ) -> OperationResponse["capo_snowball.types.update_job_result.UpdateJobResult"]:
            import capo_snowball._operations.awsie_snowball_job_management_service.update_job

            output, http_response = (
                capo_snowball._operations.awsie_snowball_job_management_service.update_job.update_job(
                    req.options, req.input
                )
            )
            return OperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_snowball.types.update_job_request.UpdateJobRequest = {
            "job_id": job_id
        }
        if role_arn is not None:
            input_["role_arn"] = role_arn
        if notification is not None:
            input_["notification"] = notification
        if resources is not None:
            input_["resources"] = resources
        if on_device_service_configuration is not None:
            input_["on_device_service_configuration"] = on_device_service_configuration
        if address_id is not None:
            input_["address_id"] = address_id
        if shipping_option is not None:
            input_["shipping_option"] = shipping_option
        if description is not None:
            input_["description"] = description
        if snowball_capacity_preference is not None:
            input_["snowball_capacity_preference"] = snowball_capacity_preference
        if forwarding_address_id is not None:
            input_["forwarding_address_id"] = forwarding_address_id
        if pickup_details is not None:
            input_["pickup_details"] = pickup_details

        response = execute_pipeline(
            OperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        response.response.close()
        return response.output

    def update_job_shipment_state(
        self,
        job_id: "capo_snowball.types.job_id.JobId",
        shipment_state: "capo_snowball.types.shipment_state.ShipmentState",
        *,
        config_overrides: Optional[SnowballClientConfig] = None,
    ) -> "capo_snowball.types.update_job_shipment_state_result.UpdateJobShipmentStateResult":
        """<p>Updates the state when a shipment state changes to a different state.</p>

        Args:
            job_id: <p>The job ID of the job whose shipment date you want to update, for example <code>JID123e4567-e89b-12d3-a456-426655440000</code>.</p>
            shipment_state: <p>The state of a device when it is being shipped. </p> <p>Set to <code>RECEIVED</code> when the device arrives at your location.</p> <p>Set to <code>RETURNED</code> when you have returned the device to Amazon Web Services.</p>

        Raises:
            capo_snowball.errors.invalid_job_state_exception.InvalidJobStateException: <p>The action can't be performed because the job's current state doesn't allow that action to be performed.</p>
            capo_snowball.errors.invalid_resource_exception.InvalidResourceException: <p>The specified resource can't be found. Check the information you provided in your last request, and try again.</p>
            capo_snowball.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        def _handler(
            req: "OperationRequest[capo_snowball.types.update_job_shipment_state_request.UpdateJobShipmentStateRequest]",
        ) -> OperationResponse[
            "capo_snowball.types.update_job_shipment_state_result.UpdateJobShipmentStateResult"
        ]:
            import capo_snowball._operations.awsie_snowball_job_management_service.update_job_shipment_state

            output, http_response = (
                capo_snowball._operations.awsie_snowball_job_management_service.update_job_shipment_state.update_job_shipment_state(
                    req.options, req.input
                )
            )
            return OperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_snowball.types.update_job_shipment_state_request.UpdateJobShipmentStateRequest = {
            "job_id": job_id,
            "shipment_state": shipment_state,
        }

        response = execute_pipeline(
            OperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        response.response.close()
        return response.output

    def update_long_term_pricing(
        self,
        long_term_pricing_id: "capo_snowball.types.long_term_pricing_id.LongTermPricingId",
        *,
        config_overrides: Optional[SnowballClientConfig] = None,
        replacement_job: Optional["capo_snowball.types.job_id.JobId"] = None,
        is_long_term_pricing_auto_renew: Optional[
            "capo_snowball.types.java_boolean.JavaBoolean"
        ] = None,
    ) -> "capo_snowball.types.update_long_term_pricing_result.UpdateLongTermPricingResult":
        """<p>Updates the long-term pricing type.</p>

        Args:
            long_term_pricing_id: <p>The ID of the long-term pricing type for the device.</p>
            replacement_job: <p>Specifies that a device that is ordered with long-term pricing should be replaced with a new device.</p>
            is_long_term_pricing_auto_renew: <p>If set to <code>true</code>, specifies that the current long-term pricing type for the device should be automatically renewed before the long-term pricing contract expires.</p>

        Raises:
            capo_snowball.errors.invalid_resource_exception.InvalidResourceException: <p>The specified resource can't be found. Check the information you provided in your last request, and try again.</p>
            capo_snowball.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        def _handler(
            req: "OperationRequest[capo_snowball.types.update_long_term_pricing_request.UpdateLongTermPricingRequest]",
        ) -> OperationResponse[
            "capo_snowball.types.update_long_term_pricing_result.UpdateLongTermPricingResult"
        ]:
            import capo_snowball._operations.awsie_snowball_job_management_service.update_long_term_pricing

            output, http_response = (
                capo_snowball._operations.awsie_snowball_job_management_service.update_long_term_pricing.update_long_term_pricing(
                    req.options, req.input
                )
            )
            return OperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_snowball.types.update_long_term_pricing_request.UpdateLongTermPricingRequest = {
            "long_term_pricing_id": long_term_pricing_id
        }
        if replacement_job is not None:
            input_["replacement_job"] = replacement_job
        if is_long_term_pricing_auto_renew is not None:
            input_["is_long_term_pricing_auto_renew"] = is_long_term_pricing_auto_renew

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
