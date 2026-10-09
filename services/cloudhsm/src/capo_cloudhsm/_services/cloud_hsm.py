"""Generated from Smithy shape ``com.amazonaws.cloudhsm#CloudHsmFrontendService``."""

import warnings
from typing import TYPE_CHECKING, Any, Iterable, Optional

from typing_extensions import Self, TypedDict
from zapros import BaseHandler, Client

import capo_cloudhsm._auth._signers
import capo_cloudhsm._auth._sigv4
from capo_cloudhsm._auth._identity import Credentials
from capo_cloudhsm._auth._providers import (
    CredentialsProvider,
    IdentityProvider,
    StaticAwsCredentialsProvider,
    default_aws_credentials_chain,
)
from capo_cloudhsm._auth._zapros_handler import AuthMiddleware
from capo_cloudhsm._services._aws_config import aws_config
from capo_cloudhsm._services._pipeline import (
    Interceptor,
    OperationOptions,
    OperationRequest,
    OperationResponse,
    execute_pipeline,
    retry,
)

if TYPE_CHECKING:
    import capo_cloudhsm.types.add_tags_to_resource_request
    import capo_cloudhsm.types.add_tags_to_resource_response
    import capo_cloudhsm.types.certificate
    import capo_cloudhsm.types.certificate_fingerprint
    import capo_cloudhsm.types.client_arn
    import capo_cloudhsm.types.client_label
    import capo_cloudhsm.types.client_token
    import capo_cloudhsm.types.client_version
    import capo_cloudhsm.types.create_hapg_request
    import capo_cloudhsm.types.create_hapg_response
    import capo_cloudhsm.types.create_hsm_request
    import capo_cloudhsm.types.create_hsm_response
    import capo_cloudhsm.types.create_luna_client_request
    import capo_cloudhsm.types.create_luna_client_response
    import capo_cloudhsm.types.delete_hapg_request
    import capo_cloudhsm.types.delete_hapg_response
    import capo_cloudhsm.types.delete_hsm_request
    import capo_cloudhsm.types.delete_hsm_response
    import capo_cloudhsm.types.delete_luna_client_request
    import capo_cloudhsm.types.delete_luna_client_response
    import capo_cloudhsm.types.describe_hapg_request
    import capo_cloudhsm.types.describe_hapg_response
    import capo_cloudhsm.types.describe_hsm_request
    import capo_cloudhsm.types.describe_hsm_response
    import capo_cloudhsm.types.describe_luna_client_request
    import capo_cloudhsm.types.describe_luna_client_response
    import capo_cloudhsm.types.external_id
    import capo_cloudhsm.types.get_config_request
    import capo_cloudhsm.types.get_config_response
    import capo_cloudhsm.types.hapg_arn
    import capo_cloudhsm.types.hapg_list
    import capo_cloudhsm.types.hsm_arn
    import capo_cloudhsm.types.hsm_serial_number
    import capo_cloudhsm.types.iam_role_arn
    import capo_cloudhsm.types.ip_address
    import capo_cloudhsm.types.label
    import capo_cloudhsm.types.list_available_zones_request
    import capo_cloudhsm.types.list_available_zones_response
    import capo_cloudhsm.types.list_hapgs_request
    import capo_cloudhsm.types.list_hapgs_response
    import capo_cloudhsm.types.list_hsms_request
    import capo_cloudhsm.types.list_hsms_response
    import capo_cloudhsm.types.list_luna_clients_request
    import capo_cloudhsm.types.list_luna_clients_response
    import capo_cloudhsm.types.list_tags_for_resource_request
    import capo_cloudhsm.types.list_tags_for_resource_response
    import capo_cloudhsm.types.modify_hapg_request
    import capo_cloudhsm.types.modify_hapg_response
    import capo_cloudhsm.types.modify_hsm_request
    import capo_cloudhsm.types.modify_hsm_response
    import capo_cloudhsm.types.modify_luna_client_request
    import capo_cloudhsm.types.modify_luna_client_response
    import capo_cloudhsm.types.pagination_token
    import capo_cloudhsm.types.partition_serial_list
    import capo_cloudhsm.types.remove_tags_from_resource_request
    import capo_cloudhsm.types.remove_tags_from_resource_response
    import capo_cloudhsm.types.ssh_key
    import capo_cloudhsm.types.string
    import capo_cloudhsm.types.subnet_id
    import capo_cloudhsm.types.subscription_type
    import capo_cloudhsm.types.tag_key_list
    import capo_cloudhsm.types.tag_list


class CloudHSMClientConfig(TypedDict, total=False, closed=True):
    operation_interceptors: Iterable[Interceptor[Any, Any]]
    retry_max_attempts: int | None
    region: str | None
    use_dual_stack: bool | None
    use_fips: bool | None
    endpoint: str | None
    credentials_provider: IdentityProvider[Credentials] | None
    anonymous: bool | None


class CloudHSMClient:
    """A client for the ``CloudHSM`` service.

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
        self._config = CloudHSMClientConfig(
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
        self, config_overrides: Optional[CloudHSMClientConfig] = None
    ) -> tuple[Iterable[Interceptor[Any, Any]], OperationOptions]:
        overrides: CloudHSMClientConfig = config_overrides or {}
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

    def add_tags_to_resource(
        self,
        resource_arn: "capo_cloudhsm.types.string.String",
        tag_list: "capo_cloudhsm.types.tag_list.TagList",
        *,
        config_overrides: Optional[CloudHSMClientConfig] = None,
    ) -> "capo_cloudhsm.types.add_tags_to_resource_response.AddTagsToResourceResponse":
        """<p>This is documentation for <b>AWS CloudHSM Classic</b>. For more information, see <a href="http://aws.amazon.com/cloudhsm/faqs-classic/">AWS CloudHSM Classic FAQs</a>, the <a href="https://docs.aws.amazon.com/cloudhsm/classic/userguide/">AWS CloudHSM Classic User Guide</a>, and the <a href="https://docs.aws.amazon.com/cloudhsm/classic/APIReference/">AWS CloudHSM Classic API Reference</a>.</p> <p> <b>For information about the current version of AWS CloudHSM</b>, see <a href="http://aws.amazon.com/cloudhsm/">AWS CloudHSM</a>, the <a href="https://docs.aws.amazon.com/cloudhsm/latest/userguide/">AWS CloudHSM User Guide</a>, and the <a href="https://docs.aws.amazon.com/cloudhsm/latest/APIReference/">AWS CloudHSM API Reference</a>.</p> <p>Adds or overwrites one or more tags for the specified AWS CloudHSM resource.</p> <p>Each tag consists of a key and a value. Tag keys must be unique to each resource.</p>

        Args:
            resource_arn: <p>The Amazon Resource Name (ARN) of the AWS CloudHSM resource to tag.</p>
            tag_list: <p>One or more tags.</p>

        Raises:
            capo_cloudhsm.errors.cloud_hsm_internal_exception.CloudHsmInternalException: <p>Indicates that an internal error occurred.</p>
            capo_cloudhsm.errors.cloud_hsm_service_exception.CloudHsmServiceException: <p>Indicates that an exception occurred in the AWS CloudHSM service.</p>
            capo_cloudhsm.errors.invalid_request_exception.InvalidRequestException: <p>Indicates that one or more of the request parameters are not valid.</p>
            capo_cloudhsm.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        def _handler(
            req: "OperationRequest[capo_cloudhsm.types.add_tags_to_resource_request.AddTagsToResourceRequest]",
        ) -> OperationResponse[
            "capo_cloudhsm.types.add_tags_to_resource_response.AddTagsToResourceResponse"
        ]:
            import capo_cloudhsm._operations.cloud_hsm_frontend_service.add_tags_to_resource

            output, http_response = (
                capo_cloudhsm._operations.cloud_hsm_frontend_service.add_tags_to_resource.add_tags_to_resource(
                    req.options, req.input
                )
            )
            return OperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_cloudhsm.types.add_tags_to_resource_request.AddTagsToResourceRequest = {
            "resource_arn": resource_arn,
            "tag_list": tag_list,
        }

        response = execute_pipeline(
            OperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        response.response.close()
        return response.output

    def create_hapg(
        self,
        label: "capo_cloudhsm.types.label.Label",
        *,
        config_overrides: Optional[CloudHSMClientConfig] = None,
    ) -> "capo_cloudhsm.types.create_hapg_response.CreateHapgResponse":
        """<p>This is documentation for <b>AWS CloudHSM Classic</b>. For more information, see <a href="http://aws.amazon.com/cloudhsm/faqs-classic/">AWS CloudHSM Classic FAQs</a>, the <a href="https://docs.aws.amazon.com/cloudhsm/classic/userguide/">AWS CloudHSM Classic User Guide</a>, and the <a href="https://docs.aws.amazon.com/cloudhsm/classic/APIReference/">AWS CloudHSM Classic API Reference</a>.</p> <p> <b>For information about the current version of AWS CloudHSM</b>, see <a href="http://aws.amazon.com/cloudhsm/">AWS CloudHSM</a>, the <a href="https://docs.aws.amazon.com/cloudhsm/latest/userguide/">AWS CloudHSM User Guide</a>, and the <a href="https://docs.aws.amazon.com/cloudhsm/latest/APIReference/">AWS CloudHSM API Reference</a>.</p> <p>Creates a high-availability partition group. A high-availability partition group is a group of partitions that spans multiple physical HSMs.</p>

        Args:
            label: <p>The label of the new high-availability partition group.</p>

        Raises:
            capo_cloudhsm.errors.cloud_hsm_internal_exception.CloudHsmInternalException: <p>Indicates that an internal error occurred.</p>
            capo_cloudhsm.errors.cloud_hsm_service_exception.CloudHsmServiceException: <p>Indicates that an exception occurred in the AWS CloudHSM service.</p>
            capo_cloudhsm.errors.invalid_request_exception.InvalidRequestException: <p>Indicates that one or more of the request parameters are not valid.</p>
            capo_cloudhsm.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        def _handler(
            req: "OperationRequest[capo_cloudhsm.types.create_hapg_request.CreateHapgRequest]",
        ) -> OperationResponse[
            "capo_cloudhsm.types.create_hapg_response.CreateHapgResponse"
        ]:
            import capo_cloudhsm._operations.cloud_hsm_frontend_service.create_hapg

            output, http_response = (
                capo_cloudhsm._operations.cloud_hsm_frontend_service.create_hapg.create_hapg(
                    req.options, req.input
                )
            )
            return OperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_cloudhsm.types.create_hapg_request.CreateHapgRequest = {
            "label": label
        }

        response = execute_pipeline(
            OperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        response.response.close()
        return response.output

    def create_hsm(
        self,
        subnet_id: "capo_cloudhsm.types.subnet_id.SubnetId",
        ssh_key: "capo_cloudhsm.types.ssh_key.SshKey",
        iam_role_arn: "capo_cloudhsm.types.iam_role_arn.IamRoleArn",
        subscription_type: "capo_cloudhsm.types.subscription_type.SubscriptionType",
        *,
        config_overrides: Optional[CloudHSMClientConfig] = None,
        eni_ip: Optional["capo_cloudhsm.types.ip_address.IpAddress"] = None,
        external_id: Optional["capo_cloudhsm.types.external_id.ExternalId"] = None,
        client_token: Optional["capo_cloudhsm.types.client_token.ClientToken"] = None,
        syslog_ip: Optional["capo_cloudhsm.types.ip_address.IpAddress"] = None,
    ) -> "capo_cloudhsm.types.create_hsm_response.CreateHsmResponse":
        """<p>This is documentation for <b>AWS CloudHSM Classic</b>. For more information, see <a href="http://aws.amazon.com/cloudhsm/faqs-classic/">AWS CloudHSM Classic FAQs</a>, the <a href="https://docs.aws.amazon.com/cloudhsm/classic/userguide/">AWS CloudHSM Classic User Guide</a>, and the <a href="https://docs.aws.amazon.com/cloudhsm/classic/APIReference/">AWS CloudHSM Classic API Reference</a>.</p> <p> <b>For information about the current version of AWS CloudHSM</b>, see <a href="http://aws.amazon.com/cloudhsm/">AWS CloudHSM</a>, the <a href="https://docs.aws.amazon.com/cloudhsm/latest/userguide/">AWS CloudHSM User Guide</a>, and the <a href="https://docs.aws.amazon.com/cloudhsm/latest/APIReference/">AWS CloudHSM API Reference</a>.</p> <p>Creates an uninitialized HSM instance.</p> <p>There is an upfront fee charged for each HSM instance that you create with the <code>CreateHsm</code> operation. If you accidentally provision an HSM and want to request a refund, delete the instance using the <a>DeleteHsm</a> operation, go to the <a href="https://console.aws.amazon.com/support/home">AWS Support Center</a>, create a new case, and select <b>Account and Billing Support</b>.</p> <important> <p>It can take up to 20 minutes to create and provision an HSM. You can monitor the status of the HSM with the <a>DescribeHsm</a> operation. The HSM is ready to be initialized when the status changes to <code>RUNNING</code>.</p> </important>

        Args:
            subnet_id: <p>The identifier of the subnet in your VPC in which to place the HSM.</p>
            ssh_key: <p>The SSH public key to install on the HSM.</p>
            eni_ip: <p>The IP address to assign to the HSM's ENI.</p> <p>If an IP address is not specified, an IP address will be randomly chosen from the CIDR range of the subnet.</p>
            iam_role_arn: <p>The ARN of an IAM role to enable the AWS CloudHSM service to allocate an ENI on your behalf.</p>
            external_id: <p>The external ID from <code>IamRoleArn</code>, if present.</p>
            client_token: <p>A user-defined token to ensure idempotence. Subsequent calls to this operation with the same token will be ignored.</p>
            syslog_ip: <p>The IP address for the syslog monitoring server. The AWS CloudHSM service only supports one syslog monitoring server.</p>

        Raises:
            capo_cloudhsm.errors.cloud_hsm_internal_exception.CloudHsmInternalException: <p>Indicates that an internal error occurred.</p>
            capo_cloudhsm.errors.cloud_hsm_service_exception.CloudHsmServiceException: <p>Indicates that an exception occurred in the AWS CloudHSM service.</p>
            capo_cloudhsm.errors.invalid_request_exception.InvalidRequestException: <p>Indicates that one or more of the request parameters are not valid.</p>
            capo_cloudhsm.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        def _handler(
            req: "OperationRequest[capo_cloudhsm.types.create_hsm_request.CreateHsmRequest]",
        ) -> OperationResponse[
            "capo_cloudhsm.types.create_hsm_response.CreateHsmResponse"
        ]:
            import capo_cloudhsm._operations.cloud_hsm_frontend_service.create_hsm

            output, http_response = (
                capo_cloudhsm._operations.cloud_hsm_frontend_service.create_hsm.create_hsm(
                    req.options, req.input
                )
            )
            return OperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_cloudhsm.types.create_hsm_request.CreateHsmRequest = {
            "subnet_id": subnet_id,
            "ssh_key": ssh_key,
            "iam_role_arn": iam_role_arn,
            "subscription_type": subscription_type,
        }
        if eni_ip is not None:
            input_["eni_ip"] = eni_ip
        if external_id is not None:
            input_["external_id"] = external_id
        if client_token is not None:
            input_["client_token"] = client_token
        if syslog_ip is not None:
            input_["syslog_ip"] = syslog_ip

        response = execute_pipeline(
            OperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        response.response.close()
        return response.output

    def create_luna_client(
        self,
        certificate: "capo_cloudhsm.types.certificate.Certificate",
        *,
        config_overrides: Optional[CloudHSMClientConfig] = None,
        label: Optional["capo_cloudhsm.types.client_label.ClientLabel"] = None,
    ) -> "capo_cloudhsm.types.create_luna_client_response.CreateLunaClientResponse":
        """<p>This is documentation for <b>AWS CloudHSM Classic</b>. For more information, see <a href="http://aws.amazon.com/cloudhsm/faqs-classic/">AWS CloudHSM Classic FAQs</a>, the <a href="https://docs.aws.amazon.com/cloudhsm/classic/userguide/">AWS CloudHSM Classic User Guide</a>, and the <a href="https://docs.aws.amazon.com/cloudhsm/classic/APIReference/">AWS CloudHSM Classic API Reference</a>.</p> <p> <b>For information about the current version of AWS CloudHSM</b>, see <a href="http://aws.amazon.com/cloudhsm/">AWS CloudHSM</a>, the <a href="https://docs.aws.amazon.com/cloudhsm/latest/userguide/">AWS CloudHSM User Guide</a>, and the <a href="https://docs.aws.amazon.com/cloudhsm/latest/APIReference/">AWS CloudHSM API Reference</a>.</p> <p>Creates an HSM client.</p>

        Args:
            label: <p>The label for the client.</p>
            certificate: <p>The contents of a Base64-Encoded X.509 v3 certificate to be installed on the HSMs used by this client.</p>

        Raises:
            capo_cloudhsm.errors.cloud_hsm_internal_exception.CloudHsmInternalException: <p>Indicates that an internal error occurred.</p>
            capo_cloudhsm.errors.cloud_hsm_service_exception.CloudHsmServiceException: <p>Indicates that an exception occurred in the AWS CloudHSM service.</p>
            capo_cloudhsm.errors.invalid_request_exception.InvalidRequestException: <p>Indicates that one or more of the request parameters are not valid.</p>
            capo_cloudhsm.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        def _handler(
            req: "OperationRequest[capo_cloudhsm.types.create_luna_client_request.CreateLunaClientRequest]",
        ) -> OperationResponse[
            "capo_cloudhsm.types.create_luna_client_response.CreateLunaClientResponse"
        ]:
            import capo_cloudhsm._operations.cloud_hsm_frontend_service.create_luna_client

            output, http_response = (
                capo_cloudhsm._operations.cloud_hsm_frontend_service.create_luna_client.create_luna_client(
                    req.options, req.input
                )
            )
            return OperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_cloudhsm.types.create_luna_client_request.CreateLunaClientRequest = {
            "certificate": certificate
        }
        if label is not None:
            input_["label"] = label

        response = execute_pipeline(
            OperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        response.response.close()
        return response.output

    def delete_hapg(
        self,
        hapg_arn: "capo_cloudhsm.types.hapg_arn.HapgArn",
        *,
        config_overrides: Optional[CloudHSMClientConfig] = None,
    ) -> "capo_cloudhsm.types.delete_hapg_response.DeleteHapgResponse":
        """<p>This is documentation for <b>AWS CloudHSM Classic</b>. For more information, see <a href="http://aws.amazon.com/cloudhsm/faqs-classic/">AWS CloudHSM Classic FAQs</a>, the <a href="https://docs.aws.amazon.com/cloudhsm/classic/userguide/">AWS CloudHSM Classic User Guide</a>, and the <a href="https://docs.aws.amazon.com/cloudhsm/classic/APIReference/">AWS CloudHSM Classic API Reference</a>.</p> <p> <b>For information about the current version of AWS CloudHSM</b>, see <a href="http://aws.amazon.com/cloudhsm/">AWS CloudHSM</a>, the <a href="https://docs.aws.amazon.com/cloudhsm/latest/userguide/">AWS CloudHSM User Guide</a>, and the <a href="https://docs.aws.amazon.com/cloudhsm/latest/APIReference/">AWS CloudHSM API Reference</a>.</p> <p>Deletes a high-availability partition group.</p>

        Args:
            hapg_arn: <p>The ARN of the high-availability partition group to delete.</p>

        Raises:
            capo_cloudhsm.errors.cloud_hsm_internal_exception.CloudHsmInternalException: <p>Indicates that an internal error occurred.</p>
            capo_cloudhsm.errors.cloud_hsm_service_exception.CloudHsmServiceException: <p>Indicates that an exception occurred in the AWS CloudHSM service.</p>
            capo_cloudhsm.errors.invalid_request_exception.InvalidRequestException: <p>Indicates that one or more of the request parameters are not valid.</p>
            capo_cloudhsm.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        def _handler(
            req: "OperationRequest[capo_cloudhsm.types.delete_hapg_request.DeleteHapgRequest]",
        ) -> OperationResponse[
            "capo_cloudhsm.types.delete_hapg_response.DeleteHapgResponse"
        ]:
            import capo_cloudhsm._operations.cloud_hsm_frontend_service.delete_hapg

            output, http_response = (
                capo_cloudhsm._operations.cloud_hsm_frontend_service.delete_hapg.delete_hapg(
                    req.options, req.input
                )
            )
            return OperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_cloudhsm.types.delete_hapg_request.DeleteHapgRequest = {
            "hapg_arn": hapg_arn
        }

        response = execute_pipeline(
            OperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        response.response.close()
        return response.output

    def delete_hsm(
        self,
        hsm_arn: "capo_cloudhsm.types.hsm_arn.HsmArn",
        *,
        config_overrides: Optional[CloudHSMClientConfig] = None,
    ) -> "capo_cloudhsm.types.delete_hsm_response.DeleteHsmResponse":
        """<p>This is documentation for <b>AWS CloudHSM Classic</b>. For more information, see <a href="http://aws.amazon.com/cloudhsm/faqs-classic/">AWS CloudHSM Classic FAQs</a>, the <a href="https://docs.aws.amazon.com/cloudhsm/classic/userguide/">AWS CloudHSM Classic User Guide</a>, and the <a href="https://docs.aws.amazon.com/cloudhsm/classic/APIReference/">AWS CloudHSM Classic API Reference</a>.</p> <p> <b>For information about the current version of AWS CloudHSM</b>, see <a href="http://aws.amazon.com/cloudhsm/">AWS CloudHSM</a>, the <a href="https://docs.aws.amazon.com/cloudhsm/latest/userguide/">AWS CloudHSM User Guide</a>, and the <a href="https://docs.aws.amazon.com/cloudhsm/latest/APIReference/">AWS CloudHSM API Reference</a>.</p> <p>Deletes an HSM. After completion, this operation cannot be undone and your key material cannot be recovered.</p>

        Args:
            hsm_arn: <p>The ARN of the HSM to delete.</p>

        Raises:
            capo_cloudhsm.errors.cloud_hsm_internal_exception.CloudHsmInternalException: <p>Indicates that an internal error occurred.</p>
            capo_cloudhsm.errors.cloud_hsm_service_exception.CloudHsmServiceException: <p>Indicates that an exception occurred in the AWS CloudHSM service.</p>
            capo_cloudhsm.errors.invalid_request_exception.InvalidRequestException: <p>Indicates that one or more of the request parameters are not valid.</p>
            capo_cloudhsm.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        def _handler(
            req: "OperationRequest[capo_cloudhsm.types.delete_hsm_request.DeleteHsmRequest]",
        ) -> OperationResponse[
            "capo_cloudhsm.types.delete_hsm_response.DeleteHsmResponse"
        ]:
            import capo_cloudhsm._operations.cloud_hsm_frontend_service.delete_hsm

            output, http_response = (
                capo_cloudhsm._operations.cloud_hsm_frontend_service.delete_hsm.delete_hsm(
                    req.options, req.input
                )
            )
            return OperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_cloudhsm.types.delete_hsm_request.DeleteHsmRequest = {
            "hsm_arn": hsm_arn
        }

        response = execute_pipeline(
            OperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        response.response.close()
        return response.output

    def delete_luna_client(
        self,
        client_arn: "capo_cloudhsm.types.client_arn.ClientArn",
        *,
        config_overrides: Optional[CloudHSMClientConfig] = None,
    ) -> "capo_cloudhsm.types.delete_luna_client_response.DeleteLunaClientResponse":
        """<p>This is documentation for <b>AWS CloudHSM Classic</b>. For more information, see <a href="http://aws.amazon.com/cloudhsm/faqs-classic/">AWS CloudHSM Classic FAQs</a>, the <a href="https://docs.aws.amazon.com/cloudhsm/classic/userguide/">AWS CloudHSM Classic User Guide</a>, and the <a href="https://docs.aws.amazon.com/cloudhsm/classic/APIReference/">AWS CloudHSM Classic API Reference</a>.</p> <p> <b>For information about the current version of AWS CloudHSM</b>, see <a href="http://aws.amazon.com/cloudhsm/">AWS CloudHSM</a>, the <a href="https://docs.aws.amazon.com/cloudhsm/latest/userguide/">AWS CloudHSM User Guide</a>, and the <a href="https://docs.aws.amazon.com/cloudhsm/latest/APIReference/">AWS CloudHSM API Reference</a>.</p> <p>Deletes a client.</p>

        Args:
            client_arn: <p>The ARN of the client to delete.</p>

        Raises:
            capo_cloudhsm.errors.cloud_hsm_internal_exception.CloudHsmInternalException: <p>Indicates that an internal error occurred.</p>
            capo_cloudhsm.errors.cloud_hsm_service_exception.CloudHsmServiceException: <p>Indicates that an exception occurred in the AWS CloudHSM service.</p>
            capo_cloudhsm.errors.invalid_request_exception.InvalidRequestException: <p>Indicates that one or more of the request parameters are not valid.</p>
            capo_cloudhsm.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        def _handler(
            req: "OperationRequest[capo_cloudhsm.types.delete_luna_client_request.DeleteLunaClientRequest]",
        ) -> OperationResponse[
            "capo_cloudhsm.types.delete_luna_client_response.DeleteLunaClientResponse"
        ]:
            import capo_cloudhsm._operations.cloud_hsm_frontend_service.delete_luna_client

            output, http_response = (
                capo_cloudhsm._operations.cloud_hsm_frontend_service.delete_luna_client.delete_luna_client(
                    req.options, req.input
                )
            )
            return OperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_cloudhsm.types.delete_luna_client_request.DeleteLunaClientRequest = {
            "client_arn": client_arn
        }

        response = execute_pipeline(
            OperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        response.response.close()
        return response.output

    def describe_hapg(
        self,
        hapg_arn: "capo_cloudhsm.types.hapg_arn.HapgArn",
        *,
        config_overrides: Optional[CloudHSMClientConfig] = None,
    ) -> "capo_cloudhsm.types.describe_hapg_response.DescribeHapgResponse":
        """<p>This is documentation for <b>AWS CloudHSM Classic</b>. For more information, see <a href="http://aws.amazon.com/cloudhsm/faqs-classic/">AWS CloudHSM Classic FAQs</a>, the <a href="https://docs.aws.amazon.com/cloudhsm/classic/userguide/">AWS CloudHSM Classic User Guide</a>, and the <a href="https://docs.aws.amazon.com/cloudhsm/classic/APIReference/">AWS CloudHSM Classic API Reference</a>.</p> <p> <b>For information about the current version of AWS CloudHSM</b>, see <a href="http://aws.amazon.com/cloudhsm/">AWS CloudHSM</a>, the <a href="https://docs.aws.amazon.com/cloudhsm/latest/userguide/">AWS CloudHSM User Guide</a>, and the <a href="https://docs.aws.amazon.com/cloudhsm/latest/APIReference/">AWS CloudHSM API Reference</a>.</p> <p>Retrieves information about a high-availability partition group.</p>

        Args:
            hapg_arn: <p>The ARN of the high-availability partition group to describe.</p>

        Raises:
            capo_cloudhsm.errors.cloud_hsm_internal_exception.CloudHsmInternalException: <p>Indicates that an internal error occurred.</p>
            capo_cloudhsm.errors.cloud_hsm_service_exception.CloudHsmServiceException: <p>Indicates that an exception occurred in the AWS CloudHSM service.</p>
            capo_cloudhsm.errors.invalid_request_exception.InvalidRequestException: <p>Indicates that one or more of the request parameters are not valid.</p>
            capo_cloudhsm.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        def _handler(
            req: "OperationRequest[capo_cloudhsm.types.describe_hapg_request.DescribeHapgRequest]",
        ) -> OperationResponse[
            "capo_cloudhsm.types.describe_hapg_response.DescribeHapgResponse"
        ]:
            import capo_cloudhsm._operations.cloud_hsm_frontend_service.describe_hapg

            output, http_response = (
                capo_cloudhsm._operations.cloud_hsm_frontend_service.describe_hapg.describe_hapg(
                    req.options, req.input
                )
            )
            return OperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_cloudhsm.types.describe_hapg_request.DescribeHapgRequest = {
            "hapg_arn": hapg_arn
        }

        response = execute_pipeline(
            OperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        response.response.close()
        return response.output

    def describe_hsm(
        self,
        *,
        config_overrides: Optional[CloudHSMClientConfig] = None,
        hsm_arn: Optional["capo_cloudhsm.types.hsm_arn.HsmArn"] = None,
        hsm_serial_number: Optional[
            "capo_cloudhsm.types.hsm_serial_number.HsmSerialNumber"
        ] = None,
    ) -> "capo_cloudhsm.types.describe_hsm_response.DescribeHsmResponse":
        """<p>This is documentation for <b>AWS CloudHSM Classic</b>. For more information, see <a href="http://aws.amazon.com/cloudhsm/faqs-classic/">AWS CloudHSM Classic FAQs</a>, the <a href="https://docs.aws.amazon.com/cloudhsm/classic/userguide/">AWS CloudHSM Classic User Guide</a>, and the <a href="https://docs.aws.amazon.com/cloudhsm/classic/APIReference/">AWS CloudHSM Classic API Reference</a>.</p> <p> <b>For information about the current version of AWS CloudHSM</b>, see <a href="http://aws.amazon.com/cloudhsm/">AWS CloudHSM</a>, the <a href="https://docs.aws.amazon.com/cloudhsm/latest/userguide/">AWS CloudHSM User Guide</a>, and the <a href="https://docs.aws.amazon.com/cloudhsm/latest/APIReference/">AWS CloudHSM API Reference</a>.</p> <p>Retrieves information about an HSM. You can identify the HSM by its ARN or its serial number.</p>

        Args:
            hsm_arn: <p>The ARN of the HSM. Either the <code>HsmArn</code> or the <code>SerialNumber</code> parameter must be specified.</p>
            hsm_serial_number: <p>The serial number of the HSM. Either the <code>HsmArn</code> or the <code>HsmSerialNumber</code> parameter must be specified.</p>

        Raises:
            capo_cloudhsm.errors.cloud_hsm_internal_exception.CloudHsmInternalException: <p>Indicates that an internal error occurred.</p>
            capo_cloudhsm.errors.cloud_hsm_service_exception.CloudHsmServiceException: <p>Indicates that an exception occurred in the AWS CloudHSM service.</p>
            capo_cloudhsm.errors.invalid_request_exception.InvalidRequestException: <p>Indicates that one or more of the request parameters are not valid.</p>
            capo_cloudhsm.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        def _handler(
            req: "OperationRequest[capo_cloudhsm.types.describe_hsm_request.DescribeHsmRequest]",
        ) -> OperationResponse[
            "capo_cloudhsm.types.describe_hsm_response.DescribeHsmResponse"
        ]:
            import capo_cloudhsm._operations.cloud_hsm_frontend_service.describe_hsm

            output, http_response = (
                capo_cloudhsm._operations.cloud_hsm_frontend_service.describe_hsm.describe_hsm(
                    req.options, req.input
                )
            )
            return OperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_cloudhsm.types.describe_hsm_request.DescribeHsmRequest = {}
        if hsm_arn is not None:
            input_["hsm_arn"] = hsm_arn
        if hsm_serial_number is not None:
            input_["hsm_serial_number"] = hsm_serial_number

        response = execute_pipeline(
            OperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        response.response.close()
        return response.output

    def describe_luna_client(
        self,
        *,
        config_overrides: Optional[CloudHSMClientConfig] = None,
        client_arn: Optional["capo_cloudhsm.types.client_arn.ClientArn"] = None,
        certificate_fingerprint: Optional[
            "capo_cloudhsm.types.certificate_fingerprint.CertificateFingerprint"
        ] = None,
    ) -> "capo_cloudhsm.types.describe_luna_client_response.DescribeLunaClientResponse":
        """<p>This is documentation for <b>AWS CloudHSM Classic</b>. For more information, see <a href="http://aws.amazon.com/cloudhsm/faqs-classic/">AWS CloudHSM Classic FAQs</a>, the <a href="https://docs.aws.amazon.com/cloudhsm/classic/userguide/">AWS CloudHSM Classic User Guide</a>, and the <a href="https://docs.aws.amazon.com/cloudhsm/classic/APIReference/">AWS CloudHSM Classic API Reference</a>.</p> <p> <b>For information about the current version of AWS CloudHSM</b>, see <a href="http://aws.amazon.com/cloudhsm/">AWS CloudHSM</a>, the <a href="https://docs.aws.amazon.com/cloudhsm/latest/userguide/">AWS CloudHSM User Guide</a>, and the <a href="https://docs.aws.amazon.com/cloudhsm/latest/APIReference/">AWS CloudHSM API Reference</a>.</p> <p>Retrieves information about an HSM client.</p>

        Args:
            client_arn: <p>The ARN of the client.</p>
            certificate_fingerprint: <p>The certificate fingerprint.</p>

        Raises:
            capo_cloudhsm.errors.cloud_hsm_internal_exception.CloudHsmInternalException: <p>Indicates that an internal error occurred.</p>
            capo_cloudhsm.errors.cloud_hsm_service_exception.CloudHsmServiceException: <p>Indicates that an exception occurred in the AWS CloudHSM service.</p>
            capo_cloudhsm.errors.invalid_request_exception.InvalidRequestException: <p>Indicates that one or more of the request parameters are not valid.</p>
            capo_cloudhsm.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        def _handler(
            req: "OperationRequest[capo_cloudhsm.types.describe_luna_client_request.DescribeLunaClientRequest]",
        ) -> OperationResponse[
            "capo_cloudhsm.types.describe_luna_client_response.DescribeLunaClientResponse"
        ]:
            import capo_cloudhsm._operations.cloud_hsm_frontend_service.describe_luna_client

            output, http_response = (
                capo_cloudhsm._operations.cloud_hsm_frontend_service.describe_luna_client.describe_luna_client(
                    req.options, req.input
                )
            )
            return OperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_cloudhsm.types.describe_luna_client_request.DescribeLunaClientRequest = {}
        if client_arn is not None:
            input_["client_arn"] = client_arn
        if certificate_fingerprint is not None:
            input_["certificate_fingerprint"] = certificate_fingerprint

        response = execute_pipeline(
            OperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        response.response.close()
        return response.output

    def get_config(
        self,
        client_arn: "capo_cloudhsm.types.client_arn.ClientArn",
        client_version: "capo_cloudhsm.types.client_version.ClientVersion",
        hapg_list: "capo_cloudhsm.types.hapg_list.HapgList",
        *,
        config_overrides: Optional[CloudHSMClientConfig] = None,
    ) -> "capo_cloudhsm.types.get_config_response.GetConfigResponse":
        """<p>This is documentation for <b>AWS CloudHSM Classic</b>. For more information, see <a href="http://aws.amazon.com/cloudhsm/faqs-classic/">AWS CloudHSM Classic FAQs</a>, the <a href="https://docs.aws.amazon.com/cloudhsm/classic/userguide/">AWS CloudHSM Classic User Guide</a>, and the <a href="https://docs.aws.amazon.com/cloudhsm/classic/APIReference/">AWS CloudHSM Classic API Reference</a>.</p> <p> <b>For information about the current version of AWS CloudHSM</b>, see <a href="http://aws.amazon.com/cloudhsm/">AWS CloudHSM</a>, the <a href="https://docs.aws.amazon.com/cloudhsm/latest/userguide/">AWS CloudHSM User Guide</a>, and the <a href="https://docs.aws.amazon.com/cloudhsm/latest/APIReference/">AWS CloudHSM API Reference</a>.</p> <p>Gets the configuration files necessary to connect to all high availability partition groups the client is associated with.</p>

        Args:
            client_arn: <p>The ARN of the client.</p>
            client_version: <p>The client version.</p>
            hapg_list: <p>A list of ARNs that identify the high-availability partition groups that are associated with the client.</p>

        Raises:
            capo_cloudhsm.errors.cloud_hsm_internal_exception.CloudHsmInternalException: <p>Indicates that an internal error occurred.</p>
            capo_cloudhsm.errors.cloud_hsm_service_exception.CloudHsmServiceException: <p>Indicates that an exception occurred in the AWS CloudHSM service.</p>
            capo_cloudhsm.errors.invalid_request_exception.InvalidRequestException: <p>Indicates that one or more of the request parameters are not valid.</p>
            capo_cloudhsm.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        def _handler(
            req: "OperationRequest[capo_cloudhsm.types.get_config_request.GetConfigRequest]",
        ) -> OperationResponse[
            "capo_cloudhsm.types.get_config_response.GetConfigResponse"
        ]:
            import capo_cloudhsm._operations.cloud_hsm_frontend_service.get_config

            output, http_response = (
                capo_cloudhsm._operations.cloud_hsm_frontend_service.get_config.get_config(
                    req.options, req.input
                )
            )
            return OperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_cloudhsm.types.get_config_request.GetConfigRequest = {
            "client_arn": client_arn,
            "client_version": client_version,
            "hapg_list": hapg_list,
        }

        response = execute_pipeline(
            OperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        response.response.close()
        return response.output

    def list_available_zones(
        self, *, config_overrides: Optional[CloudHSMClientConfig] = None
    ) -> "capo_cloudhsm.types.list_available_zones_response.ListAvailableZonesResponse":
        """<p>This is documentation for <b>AWS CloudHSM Classic</b>. For more information, see <a href="http://aws.amazon.com/cloudhsm/faqs-classic/">AWS CloudHSM Classic FAQs</a>, the <a href="https://docs.aws.amazon.com/cloudhsm/classic/userguide/">AWS CloudHSM Classic User Guide</a>, and the <a href="https://docs.aws.amazon.com/cloudhsm/classic/APIReference/">AWS CloudHSM Classic API Reference</a>.</p> <p> <b>For information about the current version of AWS CloudHSM</b>, see <a href="http://aws.amazon.com/cloudhsm/">AWS CloudHSM</a>, the <a href="https://docs.aws.amazon.com/cloudhsm/latest/userguide/">AWS CloudHSM User Guide</a>, and the <a href="https://docs.aws.amazon.com/cloudhsm/latest/APIReference/">AWS CloudHSM API Reference</a>.</p> <p>Lists the Availability Zones that have available AWS CloudHSM capacity.</p>

        Raises:
            capo_cloudhsm.errors.cloud_hsm_internal_exception.CloudHsmInternalException: <p>Indicates that an internal error occurred.</p>
            capo_cloudhsm.errors.cloud_hsm_service_exception.CloudHsmServiceException: <p>Indicates that an exception occurred in the AWS CloudHSM service.</p>
            capo_cloudhsm.errors.invalid_request_exception.InvalidRequestException: <p>Indicates that one or more of the request parameters are not valid.</p>
            capo_cloudhsm.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        def _handler(
            req: "OperationRequest[capo_cloudhsm.types.list_available_zones_request.ListAvailableZonesRequest]",
        ) -> OperationResponse[
            "capo_cloudhsm.types.list_available_zones_response.ListAvailableZonesResponse"
        ]:
            import capo_cloudhsm._operations.cloud_hsm_frontend_service.list_available_zones

            output, http_response = (
                capo_cloudhsm._operations.cloud_hsm_frontend_service.list_available_zones.list_available_zones(
                    req.options, req.input
                )
            )
            return OperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_cloudhsm.types.list_available_zones_request.ListAvailableZonesRequest = {}

        response = execute_pipeline(
            OperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        response.response.close()
        return response.output

    def list_hapgs(
        self,
        *,
        config_overrides: Optional[CloudHSMClientConfig] = None,
        next_token: Optional[
            "capo_cloudhsm.types.pagination_token.PaginationToken"
        ] = None,
    ) -> "capo_cloudhsm.types.list_hapgs_response.ListHapgsResponse":
        """<p>This is documentation for <b>AWS CloudHSM Classic</b>. For more information, see <a href="http://aws.amazon.com/cloudhsm/faqs-classic/">AWS CloudHSM Classic FAQs</a>, the <a href="https://docs.aws.amazon.com/cloudhsm/classic/userguide/">AWS CloudHSM Classic User Guide</a>, and the <a href="https://docs.aws.amazon.com/cloudhsm/classic/APIReference/">AWS CloudHSM Classic API Reference</a>.</p> <p> <b>For information about the current version of AWS CloudHSM</b>, see <a href="http://aws.amazon.com/cloudhsm/">AWS CloudHSM</a>, the <a href="https://docs.aws.amazon.com/cloudhsm/latest/userguide/">AWS CloudHSM User Guide</a>, and the <a href="https://docs.aws.amazon.com/cloudhsm/latest/APIReference/">AWS CloudHSM API Reference</a>.</p> <p>Lists the high-availability partition groups for the account.</p> <p>This operation supports pagination with the use of the <code>NextToken</code> member. If more results are available, the <code>NextToken</code> member of the response contains a token that you pass in the next call to <code>ListHapgs</code> to retrieve the next set of items.</p>

        Args:
            next_token: <p>The <code>NextToken</code> value from a previous call to <code>ListHapgs</code>. Pass null if this is the first call.</p>

        Raises:
            capo_cloudhsm.errors.cloud_hsm_internal_exception.CloudHsmInternalException: <p>Indicates that an internal error occurred.</p>
            capo_cloudhsm.errors.cloud_hsm_service_exception.CloudHsmServiceException: <p>Indicates that an exception occurred in the AWS CloudHSM service.</p>
            capo_cloudhsm.errors.invalid_request_exception.InvalidRequestException: <p>Indicates that one or more of the request parameters are not valid.</p>
            capo_cloudhsm.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        def _handler(
            req: "OperationRequest[capo_cloudhsm.types.list_hapgs_request.ListHapgsRequest]",
        ) -> OperationResponse[
            "capo_cloudhsm.types.list_hapgs_response.ListHapgsResponse"
        ]:
            import capo_cloudhsm._operations.cloud_hsm_frontend_service.list_hapgs

            output, http_response = (
                capo_cloudhsm._operations.cloud_hsm_frontend_service.list_hapgs.list_hapgs(
                    req.options, req.input
                )
            )
            return OperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_cloudhsm.types.list_hapgs_request.ListHapgsRequest = {}
        if next_token is not None:
            input_["next_token"] = next_token

        response = execute_pipeline(
            OperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        response.response.close()
        return response.output

    def list_hsms(
        self,
        *,
        config_overrides: Optional[CloudHSMClientConfig] = None,
        next_token: Optional[
            "capo_cloudhsm.types.pagination_token.PaginationToken"
        ] = None,
    ) -> "capo_cloudhsm.types.list_hsms_response.ListHsmsResponse":
        """<p>This is documentation for <b>AWS CloudHSM Classic</b>. For more information, see <a href="http://aws.amazon.com/cloudhsm/faqs-classic/">AWS CloudHSM Classic FAQs</a>, the <a href="https://docs.aws.amazon.com/cloudhsm/classic/userguide/">AWS CloudHSM Classic User Guide</a>, and the <a href="https://docs.aws.amazon.com/cloudhsm/classic/APIReference/">AWS CloudHSM Classic API Reference</a>.</p> <p> <b>For information about the current version of AWS CloudHSM</b>, see <a href="http://aws.amazon.com/cloudhsm/">AWS CloudHSM</a>, the <a href="https://docs.aws.amazon.com/cloudhsm/latest/userguide/">AWS CloudHSM User Guide</a>, and the <a href="https://docs.aws.amazon.com/cloudhsm/latest/APIReference/">AWS CloudHSM API Reference</a>.</p> <p>Retrieves the identifiers of all of the HSMs provisioned for the current customer.</p> <p>This operation supports pagination with the use of the <code>NextToken</code> member. If more results are available, the <code>NextToken</code> member of the response contains a token that you pass in the next call to <code>ListHsms</code> to retrieve the next set of items.</p>

        Args:
            next_token: <p>The <code>NextToken</code> value from a previous call to <code>ListHsms</code>. Pass null if this is the first call.</p>

        Raises:
            capo_cloudhsm.errors.cloud_hsm_internal_exception.CloudHsmInternalException: <p>Indicates that an internal error occurred.</p>
            capo_cloudhsm.errors.cloud_hsm_service_exception.CloudHsmServiceException: <p>Indicates that an exception occurred in the AWS CloudHSM service.</p>
            capo_cloudhsm.errors.invalid_request_exception.InvalidRequestException: <p>Indicates that one or more of the request parameters are not valid.</p>
            capo_cloudhsm.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        def _handler(
            req: "OperationRequest[capo_cloudhsm.types.list_hsms_request.ListHsmsRequest]",
        ) -> OperationResponse[
            "capo_cloudhsm.types.list_hsms_response.ListHsmsResponse"
        ]:
            import capo_cloudhsm._operations.cloud_hsm_frontend_service.list_hsms

            output, http_response = (
                capo_cloudhsm._operations.cloud_hsm_frontend_service.list_hsms.list_hsms(
                    req.options, req.input
                )
            )
            return OperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_cloudhsm.types.list_hsms_request.ListHsmsRequest = {}
        if next_token is not None:
            input_["next_token"] = next_token

        response = execute_pipeline(
            OperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        response.response.close()
        return response.output

    def list_luna_clients(
        self,
        *,
        config_overrides: Optional[CloudHSMClientConfig] = None,
        next_token: Optional[
            "capo_cloudhsm.types.pagination_token.PaginationToken"
        ] = None,
    ) -> "capo_cloudhsm.types.list_luna_clients_response.ListLunaClientsResponse":
        """<p>This is documentation for <b>AWS CloudHSM Classic</b>. For more information, see <a href="http://aws.amazon.com/cloudhsm/faqs-classic/">AWS CloudHSM Classic FAQs</a>, the <a href="https://docs.aws.amazon.com/cloudhsm/classic/userguide/">AWS CloudHSM Classic User Guide</a>, and the <a href="https://docs.aws.amazon.com/cloudhsm/classic/APIReference/">AWS CloudHSM Classic API Reference</a>.</p> <p> <b>For information about the current version of AWS CloudHSM</b>, see <a href="http://aws.amazon.com/cloudhsm/">AWS CloudHSM</a>, the <a href="https://docs.aws.amazon.com/cloudhsm/latest/userguide/">AWS CloudHSM User Guide</a>, and the <a href="https://docs.aws.amazon.com/cloudhsm/latest/APIReference/">AWS CloudHSM API Reference</a>.</p> <p>Lists all of the clients.</p> <p>This operation supports pagination with the use of the <code>NextToken</code> member. If more results are available, the <code>NextToken</code> member of the response contains a token that you pass in the next call to <code>ListLunaClients</code> to retrieve the next set of items.</p>

        Args:
            next_token: <p>The <code>NextToken</code> value from a previous call to <code>ListLunaClients</code>. Pass null if this is the first call.</p>

        Raises:
            capo_cloudhsm.errors.cloud_hsm_internal_exception.CloudHsmInternalException: <p>Indicates that an internal error occurred.</p>
            capo_cloudhsm.errors.cloud_hsm_service_exception.CloudHsmServiceException: <p>Indicates that an exception occurred in the AWS CloudHSM service.</p>
            capo_cloudhsm.errors.invalid_request_exception.InvalidRequestException: <p>Indicates that one or more of the request parameters are not valid.</p>
            capo_cloudhsm.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        def _handler(
            req: "OperationRequest[capo_cloudhsm.types.list_luna_clients_request.ListLunaClientsRequest]",
        ) -> OperationResponse[
            "capo_cloudhsm.types.list_luna_clients_response.ListLunaClientsResponse"
        ]:
            import capo_cloudhsm._operations.cloud_hsm_frontend_service.list_luna_clients

            output, http_response = (
                capo_cloudhsm._operations.cloud_hsm_frontend_service.list_luna_clients.list_luna_clients(
                    req.options, req.input
                )
            )
            return OperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_cloudhsm.types.list_luna_clients_request.ListLunaClientsRequest = {}
        if next_token is not None:
            input_["next_token"] = next_token

        response = execute_pipeline(
            OperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        response.response.close()
        return response.output

    def list_tags_for_resource(
        self,
        resource_arn: "capo_cloudhsm.types.string.String",
        *,
        config_overrides: Optional[CloudHSMClientConfig] = None,
    ) -> "capo_cloudhsm.types.list_tags_for_resource_response.ListTagsForResourceResponse":
        """<p>This is documentation for <b>AWS CloudHSM Classic</b>. For more information, see <a href="http://aws.amazon.com/cloudhsm/faqs-classic/">AWS CloudHSM Classic FAQs</a>, the <a href="https://docs.aws.amazon.com/cloudhsm/classic/userguide/">AWS CloudHSM Classic User Guide</a>, and the <a href="https://docs.aws.amazon.com/cloudhsm/classic/APIReference/">AWS CloudHSM Classic API Reference</a>.</p> <p> <b>For information about the current version of AWS CloudHSM</b>, see <a href="http://aws.amazon.com/cloudhsm/">AWS CloudHSM</a>, the <a href="https://docs.aws.amazon.com/cloudhsm/latest/userguide/">AWS CloudHSM User Guide</a>, and the <a href="https://docs.aws.amazon.com/cloudhsm/latest/APIReference/">AWS CloudHSM API Reference</a>.</p> <p>Returns a list of all tags for the specified AWS CloudHSM resource.</p>

        Args:
            resource_arn: <p>The Amazon Resource Name (ARN) of the AWS CloudHSM resource.</p>

        Raises:
            capo_cloudhsm.errors.cloud_hsm_internal_exception.CloudHsmInternalException: <p>Indicates that an internal error occurred.</p>
            capo_cloudhsm.errors.cloud_hsm_service_exception.CloudHsmServiceException: <p>Indicates that an exception occurred in the AWS CloudHSM service.</p>
            capo_cloudhsm.errors.invalid_request_exception.InvalidRequestException: <p>Indicates that one or more of the request parameters are not valid.</p>
            capo_cloudhsm.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        def _handler(
            req: "OperationRequest[capo_cloudhsm.types.list_tags_for_resource_request.ListTagsForResourceRequest]",
        ) -> OperationResponse[
            "capo_cloudhsm.types.list_tags_for_resource_response.ListTagsForResourceResponse"
        ]:
            import capo_cloudhsm._operations.cloud_hsm_frontend_service.list_tags_for_resource

            output, http_response = (
                capo_cloudhsm._operations.cloud_hsm_frontend_service.list_tags_for_resource.list_tags_for_resource(
                    req.options, req.input
                )
            )
            return OperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_cloudhsm.types.list_tags_for_resource_request.ListTagsForResourceRequest = {
            "resource_arn": resource_arn
        }

        response = execute_pipeline(
            OperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        response.response.close()
        return response.output

    def modify_hapg(
        self,
        hapg_arn: "capo_cloudhsm.types.hapg_arn.HapgArn",
        *,
        config_overrides: Optional[CloudHSMClientConfig] = None,
        label: Optional["capo_cloudhsm.types.label.Label"] = None,
        partition_serial_list: Optional[
            "capo_cloudhsm.types.partition_serial_list.PartitionSerialList"
        ] = None,
    ) -> "capo_cloudhsm.types.modify_hapg_response.ModifyHapgResponse":
        """<p>This is documentation for <b>AWS CloudHSM Classic</b>. For more information, see <a href="http://aws.amazon.com/cloudhsm/faqs-classic/">AWS CloudHSM Classic FAQs</a>, the <a href="https://docs.aws.amazon.com/cloudhsm/classic/userguide/">AWS CloudHSM Classic User Guide</a>, and the <a href="https://docs.aws.amazon.com/cloudhsm/classic/APIReference/">AWS CloudHSM Classic API Reference</a>.</p> <p> <b>For information about the current version of AWS CloudHSM</b>, see <a href="http://aws.amazon.com/cloudhsm/">AWS CloudHSM</a>, the <a href="https://docs.aws.amazon.com/cloudhsm/latest/userguide/">AWS CloudHSM User Guide</a>, and the <a href="https://docs.aws.amazon.com/cloudhsm/latest/APIReference/">AWS CloudHSM API Reference</a>.</p> <p>Modifies an existing high-availability partition group.</p>

        Args:
            hapg_arn: <p>The ARN of the high-availability partition group to modify.</p>
            label: <p>The new label for the high-availability partition group.</p>
            partition_serial_list: <p>The list of partition serial numbers to make members of the high-availability partition group.</p>

        Raises:
            capo_cloudhsm.errors.cloud_hsm_internal_exception.CloudHsmInternalException: <p>Indicates that an internal error occurred.</p>
            capo_cloudhsm.errors.cloud_hsm_service_exception.CloudHsmServiceException: <p>Indicates that an exception occurred in the AWS CloudHSM service.</p>
            capo_cloudhsm.errors.invalid_request_exception.InvalidRequestException: <p>Indicates that one or more of the request parameters are not valid.</p>
            capo_cloudhsm.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        def _handler(
            req: "OperationRequest[capo_cloudhsm.types.modify_hapg_request.ModifyHapgRequest]",
        ) -> OperationResponse[
            "capo_cloudhsm.types.modify_hapg_response.ModifyHapgResponse"
        ]:
            import capo_cloudhsm._operations.cloud_hsm_frontend_service.modify_hapg

            output, http_response = (
                capo_cloudhsm._operations.cloud_hsm_frontend_service.modify_hapg.modify_hapg(
                    req.options, req.input
                )
            )
            return OperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_cloudhsm.types.modify_hapg_request.ModifyHapgRequest = {
            "hapg_arn": hapg_arn
        }
        if label is not None:
            input_["label"] = label
        if partition_serial_list is not None:
            input_["partition_serial_list"] = partition_serial_list

        response = execute_pipeline(
            OperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        response.response.close()
        return response.output

    def modify_hsm(
        self,
        hsm_arn: "capo_cloudhsm.types.hsm_arn.HsmArn",
        *,
        config_overrides: Optional[CloudHSMClientConfig] = None,
        subnet_id: Optional["capo_cloudhsm.types.subnet_id.SubnetId"] = None,
        eni_ip: Optional["capo_cloudhsm.types.ip_address.IpAddress"] = None,
        iam_role_arn: Optional["capo_cloudhsm.types.iam_role_arn.IamRoleArn"] = None,
        external_id: Optional["capo_cloudhsm.types.external_id.ExternalId"] = None,
        syslog_ip: Optional["capo_cloudhsm.types.ip_address.IpAddress"] = None,
    ) -> "capo_cloudhsm.types.modify_hsm_response.ModifyHsmResponse":
        """<p>This is documentation for <b>AWS CloudHSM Classic</b>. For more information, see <a href="http://aws.amazon.com/cloudhsm/faqs-classic/">AWS CloudHSM Classic FAQs</a>, the <a href="https://docs.aws.amazon.com/cloudhsm/classic/userguide/">AWS CloudHSM Classic User Guide</a>, and the <a href="https://docs.aws.amazon.com/cloudhsm/classic/APIReference/">AWS CloudHSM Classic API Reference</a>.</p> <p> <b>For information about the current version of AWS CloudHSM</b>, see <a href="http://aws.amazon.com/cloudhsm/">AWS CloudHSM</a>, the <a href="https://docs.aws.amazon.com/cloudhsm/latest/userguide/">AWS CloudHSM User Guide</a>, and the <a href="https://docs.aws.amazon.com/cloudhsm/latest/APIReference/">AWS CloudHSM API Reference</a>.</p> <p>Modifies an HSM.</p> <important> <p>This operation can result in the HSM being offline for up to 15 minutes while the AWS CloudHSM service is reconfigured. If you are modifying a production HSM, you should ensure that your AWS CloudHSM service is configured for high availability, and consider executing this operation during a maintenance window.</p> </important>

        Args:
            hsm_arn: <p>The ARN of the HSM to modify.</p>
            subnet_id: <p>The new identifier of the subnet that the HSM is in. The new subnet must be in the same Availability Zone as the current subnet.</p>
            eni_ip: <p>The new IP address for the elastic network interface (ENI) attached to the HSM.</p> <p>If the HSM is moved to a different subnet, and an IP address is not specified, an IP address will be randomly chosen from the CIDR range of the new subnet.</p>
            iam_role_arn: <p>The new IAM role ARN.</p>
            external_id: <p>The new external ID.</p>
            syslog_ip: <p>The new IP address for the syslog monitoring server. The AWS CloudHSM service only supports one syslog monitoring server.</p>

        Raises:
            capo_cloudhsm.errors.cloud_hsm_internal_exception.CloudHsmInternalException: <p>Indicates that an internal error occurred.</p>
            capo_cloudhsm.errors.cloud_hsm_service_exception.CloudHsmServiceException: <p>Indicates that an exception occurred in the AWS CloudHSM service.</p>
            capo_cloudhsm.errors.invalid_request_exception.InvalidRequestException: <p>Indicates that one or more of the request parameters are not valid.</p>
            capo_cloudhsm.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        def _handler(
            req: "OperationRequest[capo_cloudhsm.types.modify_hsm_request.ModifyHsmRequest]",
        ) -> OperationResponse[
            "capo_cloudhsm.types.modify_hsm_response.ModifyHsmResponse"
        ]:
            import capo_cloudhsm._operations.cloud_hsm_frontend_service.modify_hsm

            output, http_response = (
                capo_cloudhsm._operations.cloud_hsm_frontend_service.modify_hsm.modify_hsm(
                    req.options, req.input
                )
            )
            return OperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_cloudhsm.types.modify_hsm_request.ModifyHsmRequest = {
            "hsm_arn": hsm_arn
        }
        if subnet_id is not None:
            input_["subnet_id"] = subnet_id
        if eni_ip is not None:
            input_["eni_ip"] = eni_ip
        if iam_role_arn is not None:
            input_["iam_role_arn"] = iam_role_arn
        if external_id is not None:
            input_["external_id"] = external_id
        if syslog_ip is not None:
            input_["syslog_ip"] = syslog_ip

        response = execute_pipeline(
            OperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        response.response.close()
        return response.output

    def modify_luna_client(
        self,
        client_arn: "capo_cloudhsm.types.client_arn.ClientArn",
        certificate: "capo_cloudhsm.types.certificate.Certificate",
        *,
        config_overrides: Optional[CloudHSMClientConfig] = None,
    ) -> "capo_cloudhsm.types.modify_luna_client_response.ModifyLunaClientResponse":
        """<p>This is documentation for <b>AWS CloudHSM Classic</b>. For more information, see <a href="http://aws.amazon.com/cloudhsm/faqs-classic/">AWS CloudHSM Classic FAQs</a>, the <a href="https://docs.aws.amazon.com/cloudhsm/classic/userguide/">AWS CloudHSM Classic User Guide</a>, and the <a href="https://docs.aws.amazon.com/cloudhsm/classic/APIReference/">AWS CloudHSM Classic API Reference</a>.</p> <p> <b>For information about the current version of AWS CloudHSM</b>, see <a href="http://aws.amazon.com/cloudhsm/">AWS CloudHSM</a>, the <a href="https://docs.aws.amazon.com/cloudhsm/latest/userguide/">AWS CloudHSM User Guide</a>, and the <a href="https://docs.aws.amazon.com/cloudhsm/latest/APIReference/">AWS CloudHSM API Reference</a>.</p> <p>Modifies the certificate used by the client.</p> <p>This action can potentially start a workflow to install the new certificate on the client's HSMs.</p>

        Args:
            client_arn: <p>The ARN of the client.</p>
            certificate: <p>The new certificate for the client.</p>

        Raises:
            capo_cloudhsm.errors.cloud_hsm_service_exception.CloudHsmServiceException: <p>Indicates that an exception occurred in the AWS CloudHSM service.</p>
            capo_cloudhsm.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        def _handler(
            req: "OperationRequest[capo_cloudhsm.types.modify_luna_client_request.ModifyLunaClientRequest]",
        ) -> OperationResponse[
            "capo_cloudhsm.types.modify_luna_client_response.ModifyLunaClientResponse"
        ]:
            import capo_cloudhsm._operations.cloud_hsm_frontend_service.modify_luna_client

            output, http_response = (
                capo_cloudhsm._operations.cloud_hsm_frontend_service.modify_luna_client.modify_luna_client(
                    req.options, req.input
                )
            )
            return OperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_cloudhsm.types.modify_luna_client_request.ModifyLunaClientRequest = {
            "client_arn": client_arn,
            "certificate": certificate,
        }

        response = execute_pipeline(
            OperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        response.response.close()
        return response.output

    def remove_tags_from_resource(
        self,
        resource_arn: "capo_cloudhsm.types.string.String",
        tag_key_list: "capo_cloudhsm.types.tag_key_list.TagKeyList",
        *,
        config_overrides: Optional[CloudHSMClientConfig] = None,
    ) -> "capo_cloudhsm.types.remove_tags_from_resource_response.RemoveTagsFromResourceResponse":
        """<p>This is documentation for <b>AWS CloudHSM Classic</b>. For more information, see <a href="http://aws.amazon.com/cloudhsm/faqs-classic/">AWS CloudHSM Classic FAQs</a>, the <a href="https://docs.aws.amazon.com/cloudhsm/classic/userguide/">AWS CloudHSM Classic User Guide</a>, and the <a href="https://docs.aws.amazon.com/cloudhsm/classic/APIReference/">AWS CloudHSM Classic API Reference</a>.</p> <p> <b>For information about the current version of AWS CloudHSM</b>, see <a href="http://aws.amazon.com/cloudhsm/">AWS CloudHSM</a>, the <a href="https://docs.aws.amazon.com/cloudhsm/latest/userguide/">AWS CloudHSM User Guide</a>, and the <a href="https://docs.aws.amazon.com/cloudhsm/latest/APIReference/">AWS CloudHSM API Reference</a>.</p> <p>Removes one or more tags from the specified AWS CloudHSM resource.</p> <p>To remove a tag, specify only the tag key to remove (not the value). To overwrite the value for an existing tag, use <a>AddTagsToResource</a>.</p>

        Args:
            resource_arn: <p>The Amazon Resource Name (ARN) of the AWS CloudHSM resource.</p>
            tag_key_list: <p>The tag key or keys to remove.</p> <p>Specify only the tag key to remove (not the value). To overwrite the value for an existing tag, use <a>AddTagsToResource</a>.</p>

        Raises:
            capo_cloudhsm.errors.cloud_hsm_internal_exception.CloudHsmInternalException: <p>Indicates that an internal error occurred.</p>
            capo_cloudhsm.errors.cloud_hsm_service_exception.CloudHsmServiceException: <p>Indicates that an exception occurred in the AWS CloudHSM service.</p>
            capo_cloudhsm.errors.invalid_request_exception.InvalidRequestException: <p>Indicates that one or more of the request parameters are not valid.</p>
            capo_cloudhsm.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        def _handler(
            req: "OperationRequest[capo_cloudhsm.types.remove_tags_from_resource_request.RemoveTagsFromResourceRequest]",
        ) -> OperationResponse[
            "capo_cloudhsm.types.remove_tags_from_resource_response.RemoveTagsFromResourceResponse"
        ]:
            import capo_cloudhsm._operations.cloud_hsm_frontend_service.remove_tags_from_resource

            output, http_response = (
                capo_cloudhsm._operations.cloud_hsm_frontend_service.remove_tags_from_resource.remove_tags_from_resource(
                    req.options, req.input
                )
            )
            return OperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_cloudhsm.types.remove_tags_from_resource_request.RemoveTagsFromResourceRequest = {
            "resource_arn": resource_arn,
            "tag_key_list": tag_key_list,
        }

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
