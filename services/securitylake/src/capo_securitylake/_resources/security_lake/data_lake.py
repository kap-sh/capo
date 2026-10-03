from __future__ import annotations

from typing import TYPE_CHECKING, Optional

import capo_securitylake._auth._signers
import capo_securitylake._auth._sigv4
from capo_securitylake._services._pipeline import (
    AsyncOperationRequest,
    AsyncOperationResponse,
    OperationRequest,
    OperationResponse,
    aexecute_pipeline,
    execute_pipeline,
)

if TYPE_CHECKING:
    import capo_securitylake.types.account_list
    import capo_securitylake.types.aws_log_source_configuration_list
    import capo_securitylake.types.create_aws_log_source_request
    import capo_securitylake.types.create_aws_log_source_response
    import capo_securitylake.types.create_custom_log_source_request
    import capo_securitylake.types.create_custom_log_source_response
    import capo_securitylake.types.create_data_lake_organization_configuration_request
    import capo_securitylake.types.create_data_lake_organization_configuration_response
    import capo_securitylake.types.create_data_lake_request
    import capo_securitylake.types.create_data_lake_response
    import capo_securitylake.types.custom_log_source_configuration
    import capo_securitylake.types.custom_log_source_name
    import capo_securitylake.types.custom_log_source_version
    import capo_securitylake.types.data_lake_auto_enable_new_account_configuration_list
    import capo_securitylake.types.data_lake_configuration_list
    import capo_securitylake.types.data_lake_source
    import capo_securitylake.types.delete_aws_log_source_request
    import capo_securitylake.types.delete_aws_log_source_response
    import capo_securitylake.types.delete_custom_log_source_request
    import capo_securitylake.types.delete_custom_log_source_response
    import capo_securitylake.types.delete_data_lake_organization_configuration_request
    import capo_securitylake.types.delete_data_lake_organization_configuration_response
    import capo_securitylake.types.delete_data_lake_request
    import capo_securitylake.types.delete_data_lake_response
    import capo_securitylake.types.get_data_lake_organization_configuration_request
    import capo_securitylake.types.get_data_lake_organization_configuration_response
    import capo_securitylake.types.get_data_lake_sources_request
    import capo_securitylake.types.get_data_lake_sources_response
    import capo_securitylake.types.list_data_lakes_request
    import capo_securitylake.types.list_data_lakes_response
    import capo_securitylake.types.list_log_sources_request
    import capo_securitylake.types.list_log_sources_response
    import capo_securitylake.types.log_source
    import capo_securitylake.types.log_source_resource_list
    import capo_securitylake.types.max_results
    import capo_securitylake.types.next_token
    import capo_securitylake.types.ocsf_event_class_list
    import capo_securitylake.types.region_list
    import capo_securitylake.types.role_arn
    import capo_securitylake.types.tag_list
    import capo_securitylake.types.update_data_lake_request
    import capo_securitylake.types.update_data_lake_response
    from capo_securitylake._services.async_security_lake import (
        AsyncSecurityLakeClient,
        AsyncSecurityLakeClientConfig,
    )
    from capo_securitylake._services.security_lake import (
        SecurityLakeClient,
        SecurityLakeClientConfig,
    )


class DataLake:
    def __init__(self, service: SecurityLakeClient) -> None:
        self._service = service

    def create_aws_log_source(
        self,
        sources: "capo_securitylake.types.aws_log_source_configuration_list.AwsLogSourceConfigurationList",
        *,
        config_overrides: Optional[SecurityLakeClientConfig] = None,
    ) -> "capo_securitylake.types.create_aws_log_source_response.CreateAwsLogSourceResponse":
        """<p>Adds a natively supported Amazon Web Services service as an Amazon Security Lake source. Enables source types for member accounts in required Amazon Web Services Regions, based on the parameters you specify. You can choose any source type in any Region for either accounts that are part of a trusted organization or standalone accounts. Once you add an Amazon Web Services service as a source, Security Lake starts collecting logs and events from it.</p> <p>You can use this API only to enable natively supported Amazon Web Services services as a source. Use <code>CreateCustomLogSource</code> to enable data collection from a custom source.</p>

        Args:
            sources: <p>Specify the natively-supported Amazon Web Services service to add as a source in Security Lake.</p>

        Raises:
            capo_securitylake.errors.access_denied_exception.AccessDeniedException: <p>You do not have sufficient access to perform this action. Access denied errors appear when Amazon Security Lake explicitly or implicitly denies an authorization request. An explicit denial occurs when a policy contains a Deny statement for the specific Amazon Web Services action. An implicit denial occurs when there is no applicable Deny statement and also no applicable Allow statement.</p>
            capo_securitylake.errors.bad_request_exception.BadRequestException: <p>The request is malformed or contains an error such as an invalid parameter value or a missing required parameter.</p>
            capo_securitylake.errors.conflict_exception.ConflictException: <p>Occurs when a conflict with a previous successful write is detected. This generally occurs when the previous write did not have time to propagate to the host serving the current request. A retry (with appropriate backoff logic) is the recommended response to this exception.</p>
            capo_securitylake.errors.internal_server_exception.InternalServerException: <p>Internal service exceptions are sometimes caused by transient issues. Before you start troubleshooting, perform the operation again.</p>
            capo_securitylake.errors.resource_not_found_exception.ResourceNotFoundException: <p>The resource could not be found.</p>
            capo_securitylake.errors.throttling_exception.ThrottlingException: <p>The limit on the number of requests per second was exceeded.</p>
            capo_securitylake.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        def _handler(
            req: "OperationRequest[capo_securitylake.types.create_aws_log_source_request.CreateAwsLogSourceRequest]",
        ) -> OperationResponse[
            "capo_securitylake.types.create_aws_log_source_response.CreateAwsLogSourceResponse"
        ]:
            import capo_securitylake._operations.security_lake.create_aws_log_source

            output, http_response = (
                capo_securitylake._operations.security_lake.create_aws_log_source.create_aws_log_source(
                    req.options, req.input
                )
            )
            return OperationResponse(output=output, response=http_response)

        interceptors_, options_ = self._service.operation_options(config_overrides)
        input_: capo_securitylake.types.create_aws_log_source_request.CreateAwsLogSourceRequest = {
            "sources": sources
        }

        response = execute_pipeline(
            OperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        response.response.close()
        return response.output

    def create_custom_log_source(
        self,
        source_name: "capo_securitylake.types.custom_log_source_name.CustomLogSourceName",
        configuration: "capo_securitylake.types.custom_log_source_configuration.CustomLogSourceConfiguration",
        *,
        config_overrides: Optional[SecurityLakeClientConfig] = None,
        source_version: Optional[
            "capo_securitylake.types.custom_log_source_version.CustomLogSourceVersion"
        ] = None,
        event_classes: Optional[
            "capo_securitylake.types.ocsf_event_class_list.OcsfEventClassList"
        ] = None,
    ) -> "capo_securitylake.types.create_custom_log_source_response.CreateCustomLogSourceResponse":
        """<p>Adds a third-party custom source in Amazon Security Lake, from the Amazon Web Services Region where you want to create a custom source. Security Lake can collect logs and events from third-party custom sources. After creating the appropriate IAM role to invoke Glue crawler, use this API to add a custom source name in Security Lake. This operation creates a partition in the Amazon S3 bucket for Security Lake as the target location for log files from the custom source. In addition, this operation also creates an associated Glue table and an Glue crawler.</p>

        Args:
            source_name: <p>Specify the name for a third-party custom source. This must be a Regionally unique value. The <code>sourceName</code> you enter here, is used in the <code>LogProviderRole</code> name which follows the convention <code>AmazonSecurityLake-Provider-{name of the custom source}-{region}</code>. You must use a <code>CustomLogSource</code> name that is shorter than or equal to 20 characters. This ensures that the <code>LogProviderRole</code> name is below the 64 character limit.</p>
            source_version: <p>Specify the source version for the third-party custom source, to limit log collection to a specific version of custom data source.</p>
            event_classes: <p>The Open Cybersecurity Schema Framework (OCSF) event classes which describes the type of data that the custom source will send to Security Lake. For the list of supported event classes, see the <a href="https://docs.aws.amazon.com/security-lake/latest/userguide/adding-custom-sources.html#ocsf-eventclass">Amazon Security Lake User Guide</a>.</p>
            configuration: <p>The configuration used for the third-party custom source.</p>

        Raises:
            capo_securitylake.errors.access_denied_exception.AccessDeniedException: <p>You do not have sufficient access to perform this action. Access denied errors appear when Amazon Security Lake explicitly or implicitly denies an authorization request. An explicit denial occurs when a policy contains a Deny statement for the specific Amazon Web Services action. An implicit denial occurs when there is no applicable Deny statement and also no applicable Allow statement.</p>
            capo_securitylake.errors.bad_request_exception.BadRequestException: <p>The request is malformed or contains an error such as an invalid parameter value or a missing required parameter.</p>
            capo_securitylake.errors.conflict_exception.ConflictException: <p>Occurs when a conflict with a previous successful write is detected. This generally occurs when the previous write did not have time to propagate to the host serving the current request. A retry (with appropriate backoff logic) is the recommended response to this exception.</p>
            capo_securitylake.errors.internal_server_exception.InternalServerException: <p>Internal service exceptions are sometimes caused by transient issues. Before you start troubleshooting, perform the operation again.</p>
            capo_securitylake.errors.resource_not_found_exception.ResourceNotFoundException: <p>The resource could not be found.</p>
            capo_securitylake.errors.throttling_exception.ThrottlingException: <p>The limit on the number of requests per second was exceeded.</p>
            capo_securitylake.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        def _handler(
            req: "OperationRequest[capo_securitylake.types.create_custom_log_source_request.CreateCustomLogSourceRequest]",
        ) -> OperationResponse[
            "capo_securitylake.types.create_custom_log_source_response.CreateCustomLogSourceResponse"
        ]:
            import capo_securitylake._operations.security_lake.create_custom_log_source

            output, http_response = (
                capo_securitylake._operations.security_lake.create_custom_log_source.create_custom_log_source(
                    req.options, req.input
                )
            )
            return OperationResponse(output=output, response=http_response)

        interceptors_, options_ = self._service.operation_options(config_overrides)
        input_: capo_securitylake.types.create_custom_log_source_request.CreateCustomLogSourceRequest = {
            "source_name": source_name,
            "configuration": configuration,
        }
        if source_version is not None:
            input_["source_version"] = source_version
        if event_classes is not None:
            input_["event_classes"] = event_classes

        response = execute_pipeline(
            OperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        response.response.close()
        return response.output

    def create_data_lake(
        self,
        configurations: "capo_securitylake.types.data_lake_configuration_list.DataLakeConfigurationList",
        meta_store_manager_role_arn: "capo_securitylake.types.role_arn.RoleArn",
        *,
        config_overrides: Optional[SecurityLakeClientConfig] = None,
        tags: Optional["capo_securitylake.types.tag_list.TagList"] = None,
    ) -> "capo_securitylake.types.create_data_lake_response.CreateDataLakeResponse":
        """<p>Initializes an Amazon Security Lake instance with the provided (or default) configuration. You can enable Security Lake in Amazon Web Services Regions with customized settings before enabling log collection in Regions. To specify particular Regions, configure these Regions using the <code>configurations</code> parameter. If you have already enabled Security Lake in a Region when you call this command, the command will update the Region if you provide new configuration parameters. If you have not already enabled Security Lake in the Region when you call this API, it will set up the data lake in the Region with the specified configurations.</p> <p>When you enable Security Lake, it starts ingesting security data after the <code>CreateAwsLogSource</code> call and after you create subscribers using the <code>CreateSubscriber</code> API. This includes ingesting security data from sources, storing data, and making data accessible to subscribers. Security Lake also enables all the existing settings and resources that it stores or maintains for your Amazon Web Services account in the current Region, including security log and event data. For more information, see the <a href="https://docs.aws.amazon.com/security-lake/latest/userguide/what-is-security-lake.html">Amazon Security Lake User Guide</a>.</p>

        Args:
            configurations: <p>Specify the Region or Regions that will contribute data to the rollup region.</p>
            meta_store_manager_role_arn: <p>The Amazon Resource Name (ARN) used to create and update the Glue table. This table contains partitions generated by the ingestion and normalization of Amazon Web Services log sources and custom sources.</p>
            tags: <p>An array of objects, one for each tag to associate with the data lake configuration. For each tag, you must specify both a tag key and a tag value. A tag value cannot be null, but it can be an empty string.</p>

        Raises:
            capo_securitylake.errors.access_denied_exception.AccessDeniedException: <p>You do not have sufficient access to perform this action. Access denied errors appear when Amazon Security Lake explicitly or implicitly denies an authorization request. An explicit denial occurs when a policy contains a Deny statement for the specific Amazon Web Services action. An implicit denial occurs when there is no applicable Deny statement and also no applicable Allow statement.</p>
            capo_securitylake.errors.bad_request_exception.BadRequestException: <p>The request is malformed or contains an error such as an invalid parameter value or a missing required parameter.</p>
            capo_securitylake.errors.conflict_exception.ConflictException: <p>Occurs when a conflict with a previous successful write is detected. This generally occurs when the previous write did not have time to propagate to the host serving the current request. A retry (with appropriate backoff logic) is the recommended response to this exception.</p>
            capo_securitylake.errors.internal_server_exception.InternalServerException: <p>Internal service exceptions are sometimes caused by transient issues. Before you start troubleshooting, perform the operation again.</p>
            capo_securitylake.errors.resource_not_found_exception.ResourceNotFoundException: <p>The resource could not be found.</p>
            capo_securitylake.errors.throttling_exception.ThrottlingException: <p>The limit on the number of requests per second was exceeded.</p>
            capo_securitylake.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        def _handler(
            req: "OperationRequest[capo_securitylake.types.create_data_lake_request.CreateDataLakeRequest]",
        ) -> OperationResponse[
            "capo_securitylake.types.create_data_lake_response.CreateDataLakeResponse"
        ]:
            import capo_securitylake._operations.security_lake.create_data_lake

            output, http_response = (
                capo_securitylake._operations.security_lake.create_data_lake.create_data_lake(
                    req.options, req.input
                )
            )
            return OperationResponse(output=output, response=http_response)

        interceptors_, options_ = self._service.operation_options(config_overrides)
        input_: capo_securitylake.types.create_data_lake_request.CreateDataLakeRequest = {
            "configurations": configurations,
            "meta_store_manager_role_arn": meta_store_manager_role_arn,
        }
        if tags is not None:
            input_["tags"] = tags

        response = execute_pipeline(
            OperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        response.response.close()
        return response.output

    def create_data_lake_organization_configuration(
        self,
        *,
        config_overrides: Optional[SecurityLakeClientConfig] = None,
        auto_enable_new_account: Optional[
            "capo_securitylake.types.data_lake_auto_enable_new_account_configuration_list.DataLakeAutoEnableNewAccountConfigurationList"
        ] = None,
    ) -> "capo_securitylake.types.create_data_lake_organization_configuration_response.CreateDataLakeOrganizationConfigurationResponse":
        """<p>Automatically enables Amazon Security Lake for new member accounts in your organization. Security Lake is not automatically enabled for any existing member accounts in your organization.</p> <p>This operation merges the new data lake organization configuration with the existing configuration for Security Lake in your organization. If you want to create a new data lake organization configuration, you must delete the existing one using <a href="https://docs.aws.amazon.com/security-lake/latest/APIReference/API_DeleteDataLakeOrganizationConfiguration.html">DeleteDataLakeOrganizationConfiguration</a>.</p>

        Args:
            auto_enable_new_account: <p>Enable Security Lake with the specified configuration settings, to begin collecting security data for new accounts in your organization.</p>

        Raises:
            capo_securitylake.errors.access_denied_exception.AccessDeniedException: <p>You do not have sufficient access to perform this action. Access denied errors appear when Amazon Security Lake explicitly or implicitly denies an authorization request. An explicit denial occurs when a policy contains a Deny statement for the specific Amazon Web Services action. An implicit denial occurs when there is no applicable Deny statement and also no applicable Allow statement.</p>
            capo_securitylake.errors.bad_request_exception.BadRequestException: <p>The request is malformed or contains an error such as an invalid parameter value or a missing required parameter.</p>
            capo_securitylake.errors.conflict_exception.ConflictException: <p>Occurs when a conflict with a previous successful write is detected. This generally occurs when the previous write did not have time to propagate to the host serving the current request. A retry (with appropriate backoff logic) is the recommended response to this exception.</p>
            capo_securitylake.errors.internal_server_exception.InternalServerException: <p>Internal service exceptions are sometimes caused by transient issues. Before you start troubleshooting, perform the operation again.</p>
            capo_securitylake.errors.resource_not_found_exception.ResourceNotFoundException: <p>The resource could not be found.</p>
            capo_securitylake.errors.throttling_exception.ThrottlingException: <p>The limit on the number of requests per second was exceeded.</p>
            capo_securitylake.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        def _handler(
            req: "OperationRequest[capo_securitylake.types.create_data_lake_organization_configuration_request.CreateDataLakeOrganizationConfigurationRequest]",
        ) -> OperationResponse[
            "capo_securitylake.types.create_data_lake_organization_configuration_response.CreateDataLakeOrganizationConfigurationResponse"
        ]:
            import capo_securitylake._operations.security_lake.create_data_lake_organization_configuration

            output, http_response = (
                capo_securitylake._operations.security_lake.create_data_lake_organization_configuration.create_data_lake_organization_configuration(
                    req.options, req.input
                )
            )
            return OperationResponse(output=output, response=http_response)

        interceptors_, options_ = self._service.operation_options(config_overrides)
        input_: capo_securitylake.types.create_data_lake_organization_configuration_request.CreateDataLakeOrganizationConfigurationRequest = {}
        if auto_enable_new_account is not None:
            input_["auto_enable_new_account"] = auto_enable_new_account

        response = execute_pipeline(
            OperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        response.response.close()
        return response.output

    def delete_aws_log_source(
        self,
        sources: "capo_securitylake.types.aws_log_source_configuration_list.AwsLogSourceConfigurationList",
        *,
        config_overrides: Optional[SecurityLakeClientConfig] = None,
    ) -> "capo_securitylake.types.delete_aws_log_source_response.DeleteAwsLogSourceResponse":
        """<p>Removes a natively supported Amazon Web Services service as an Amazon Security Lake source. You can remove a source for one or more Regions. When you remove the source, Security Lake stops collecting data from that source in the specified Regions and accounts, and subscribers can no longer consume new data from the source. However, subscribers can still consume data that Security Lake collected from the source before removal.</p> <p>You can choose any source type in any Amazon Web Services Region for either accounts that are part of a trusted organization or standalone accounts. </p>

        Args:
            sources: <p>Specify the natively-supported Amazon Web Services service to remove as a source in Security Lake.</p>

        Raises:
            capo_securitylake.errors.access_denied_exception.AccessDeniedException: <p>You do not have sufficient access to perform this action. Access denied errors appear when Amazon Security Lake explicitly or implicitly denies an authorization request. An explicit denial occurs when a policy contains a Deny statement for the specific Amazon Web Services action. An implicit denial occurs when there is no applicable Deny statement and also no applicable Allow statement.</p>
            capo_securitylake.errors.bad_request_exception.BadRequestException: <p>The request is malformed or contains an error such as an invalid parameter value or a missing required parameter.</p>
            capo_securitylake.errors.conflict_exception.ConflictException: <p>Occurs when a conflict with a previous successful write is detected. This generally occurs when the previous write did not have time to propagate to the host serving the current request. A retry (with appropriate backoff logic) is the recommended response to this exception.</p>
            capo_securitylake.errors.internal_server_exception.InternalServerException: <p>Internal service exceptions are sometimes caused by transient issues. Before you start troubleshooting, perform the operation again.</p>
            capo_securitylake.errors.resource_not_found_exception.ResourceNotFoundException: <p>The resource could not be found.</p>
            capo_securitylake.errors.throttling_exception.ThrottlingException: <p>The limit on the number of requests per second was exceeded.</p>
            capo_securitylake.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        def _handler(
            req: "OperationRequest[capo_securitylake.types.delete_aws_log_source_request.DeleteAwsLogSourceRequest]",
        ) -> OperationResponse[
            "capo_securitylake.types.delete_aws_log_source_response.DeleteAwsLogSourceResponse"
        ]:
            import capo_securitylake._operations.security_lake.delete_aws_log_source

            output, http_response = (
                capo_securitylake._operations.security_lake.delete_aws_log_source.delete_aws_log_source(
                    req.options, req.input
                )
            )
            return OperationResponse(output=output, response=http_response)

        interceptors_, options_ = self._service.operation_options(config_overrides)
        input_: capo_securitylake.types.delete_aws_log_source_request.DeleteAwsLogSourceRequest = {
            "sources": sources
        }

        response = execute_pipeline(
            OperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        response.response.close()
        return response.output

    def delete_custom_log_source(
        self,
        source_name: "capo_securitylake.types.custom_log_source_name.CustomLogSourceName",
        *,
        config_overrides: Optional[SecurityLakeClientConfig] = None,
        source_version: Optional[
            "capo_securitylake.types.custom_log_source_version.CustomLogSourceVersion"
        ] = None,
    ) -> "capo_securitylake.types.delete_custom_log_source_response.DeleteCustomLogSourceResponse":
        """<p>Removes a custom log source from Amazon Security Lake, to stop sending data from the custom source to Security Lake.</p>

        Args:
            source_name: <p>The source name of custom log source that you want to delete.</p>
            source_version: <p>The source version for the third-party custom source. You can limit the custom source removal to the specified source version.</p>

        Raises:
            capo_securitylake.errors.access_denied_exception.AccessDeniedException: <p>You do not have sufficient access to perform this action. Access denied errors appear when Amazon Security Lake explicitly or implicitly denies an authorization request. An explicit denial occurs when a policy contains a Deny statement for the specific Amazon Web Services action. An implicit denial occurs when there is no applicable Deny statement and also no applicable Allow statement.</p>
            capo_securitylake.errors.bad_request_exception.BadRequestException: <p>The request is malformed or contains an error such as an invalid parameter value or a missing required parameter.</p>
            capo_securitylake.errors.conflict_exception.ConflictException: <p>Occurs when a conflict with a previous successful write is detected. This generally occurs when the previous write did not have time to propagate to the host serving the current request. A retry (with appropriate backoff logic) is the recommended response to this exception.</p>
            capo_securitylake.errors.internal_server_exception.InternalServerException: <p>Internal service exceptions are sometimes caused by transient issues. Before you start troubleshooting, perform the operation again.</p>
            capo_securitylake.errors.resource_not_found_exception.ResourceNotFoundException: <p>The resource could not be found.</p>
            capo_securitylake.errors.throttling_exception.ThrottlingException: <p>The limit on the number of requests per second was exceeded.</p>
            capo_securitylake.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        def _handler(
            req: "OperationRequest[capo_securitylake.types.delete_custom_log_source_request.DeleteCustomLogSourceRequest]",
        ) -> OperationResponse[
            "capo_securitylake.types.delete_custom_log_source_response.DeleteCustomLogSourceResponse"
        ]:
            import capo_securitylake._operations.security_lake.delete_custom_log_source

            output, http_response = (
                capo_securitylake._operations.security_lake.delete_custom_log_source.delete_custom_log_source(
                    req.options, req.input
                )
            )
            return OperationResponse(output=output, response=http_response)

        interceptors_, options_ = self._service.operation_options(config_overrides)
        input_: capo_securitylake.types.delete_custom_log_source_request.DeleteCustomLogSourceRequest = {
            "source_name": source_name
        }
        if source_version is not None:
            input_["source_version"] = source_version

        response = execute_pipeline(
            OperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        response.response.close()
        return response.output

    def delete_data_lake(
        self,
        regions: "capo_securitylake.types.region_list.RegionList",
        *,
        config_overrides: Optional[SecurityLakeClientConfig] = None,
    ) -> "capo_securitylake.types.delete_data_lake_response.DeleteDataLakeResponse":
        """<p>When you disable Amazon Security Lake from your account, Security Lake is disabled in all Amazon Web Services Regions and it stops collecting data from your sources. Also, this API automatically takes steps to remove the account from Security Lake. However, Security Lake retains all of your existing settings and the resources that it created in your Amazon Web Services account in the current Amazon Web Services Region.</p> <p>The <code>DeleteDataLake</code> operation does not delete the data that is stored in your Amazon S3 bucket, which is owned by your Amazon Web Services account. For more information, see the <a href="https://docs.aws.amazon.com/security-lake/latest/userguide/disable-security-lake.html">Amazon Security Lake User Guide</a>.</p>

        Args:
            regions: <p>The list of Regions where Security Lake is enabled.</p>

        Raises:
            capo_securitylake.errors.access_denied_exception.AccessDeniedException: <p>You do not have sufficient access to perform this action. Access denied errors appear when Amazon Security Lake explicitly or implicitly denies an authorization request. An explicit denial occurs when a policy contains a Deny statement for the specific Amazon Web Services action. An implicit denial occurs when there is no applicable Deny statement and also no applicable Allow statement.</p>
            capo_securitylake.errors.bad_request_exception.BadRequestException: <p>The request is malformed or contains an error such as an invalid parameter value or a missing required parameter.</p>
            capo_securitylake.errors.conflict_exception.ConflictException: <p>Occurs when a conflict with a previous successful write is detected. This generally occurs when the previous write did not have time to propagate to the host serving the current request. A retry (with appropriate backoff logic) is the recommended response to this exception.</p>
            capo_securitylake.errors.internal_server_exception.InternalServerException: <p>Internal service exceptions are sometimes caused by transient issues. Before you start troubleshooting, perform the operation again.</p>
            capo_securitylake.errors.resource_not_found_exception.ResourceNotFoundException: <p>The resource could not be found.</p>
            capo_securitylake.errors.throttling_exception.ThrottlingException: <p>The limit on the number of requests per second was exceeded.</p>
            capo_securitylake.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        def _handler(
            req: "OperationRequest[capo_securitylake.types.delete_data_lake_request.DeleteDataLakeRequest]",
        ) -> OperationResponse[
            "capo_securitylake.types.delete_data_lake_response.DeleteDataLakeResponse"
        ]:
            import capo_securitylake._operations.security_lake.delete_data_lake

            output, http_response = (
                capo_securitylake._operations.security_lake.delete_data_lake.delete_data_lake(
                    req.options, req.input
                )
            )
            return OperationResponse(output=output, response=http_response)

        interceptors_, options_ = self._service.operation_options(config_overrides)
        input_: capo_securitylake.types.delete_data_lake_request.DeleteDataLakeRequest = {
            "regions": regions
        }

        response = execute_pipeline(
            OperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        response.response.close()
        return response.output

    def delete_data_lake_organization_configuration(
        self,
        *,
        config_overrides: Optional[SecurityLakeClientConfig] = None,
        auto_enable_new_account: Optional[
            "capo_securitylake.types.data_lake_auto_enable_new_account_configuration_list.DataLakeAutoEnableNewAccountConfigurationList"
        ] = None,
    ) -> "capo_securitylake.types.delete_data_lake_organization_configuration_response.DeleteDataLakeOrganizationConfigurationResponse":
        """<p>Turns off automatic enablement of Amazon Security Lake for member accounts that are added to an organization in Organizations. Only the delegated Security Lake administrator for an organization can perform this operation. If the delegated Security Lake administrator performs this operation, new member accounts won't automatically contribute data to the data lake.</p>

        Args:
            auto_enable_new_account: <p>Turns off automatic enablement of Security Lake for member accounts that are added to an organization.</p>

        Raises:
            capo_securitylake.errors.access_denied_exception.AccessDeniedException: <p>You do not have sufficient access to perform this action. Access denied errors appear when Amazon Security Lake explicitly or implicitly denies an authorization request. An explicit denial occurs when a policy contains a Deny statement for the specific Amazon Web Services action. An implicit denial occurs when there is no applicable Deny statement and also no applicable Allow statement.</p>
            capo_securitylake.errors.bad_request_exception.BadRequestException: <p>The request is malformed or contains an error such as an invalid parameter value or a missing required parameter.</p>
            capo_securitylake.errors.conflict_exception.ConflictException: <p>Occurs when a conflict with a previous successful write is detected. This generally occurs when the previous write did not have time to propagate to the host serving the current request. A retry (with appropriate backoff logic) is the recommended response to this exception.</p>
            capo_securitylake.errors.internal_server_exception.InternalServerException: <p>Internal service exceptions are sometimes caused by transient issues. Before you start troubleshooting, perform the operation again.</p>
            capo_securitylake.errors.resource_not_found_exception.ResourceNotFoundException: <p>The resource could not be found.</p>
            capo_securitylake.errors.throttling_exception.ThrottlingException: <p>The limit on the number of requests per second was exceeded.</p>
            capo_securitylake.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        def _handler(
            req: "OperationRequest[capo_securitylake.types.delete_data_lake_organization_configuration_request.DeleteDataLakeOrganizationConfigurationRequest]",
        ) -> OperationResponse[
            "capo_securitylake.types.delete_data_lake_organization_configuration_response.DeleteDataLakeOrganizationConfigurationResponse"
        ]:
            import capo_securitylake._operations.security_lake.delete_data_lake_organization_configuration

            output, http_response = (
                capo_securitylake._operations.security_lake.delete_data_lake_organization_configuration.delete_data_lake_organization_configuration(
                    req.options, req.input
                )
            )
            return OperationResponse(output=output, response=http_response)

        interceptors_, options_ = self._service.operation_options(config_overrides)
        input_: capo_securitylake.types.delete_data_lake_organization_configuration_request.DeleteDataLakeOrganizationConfigurationRequest = {}
        if auto_enable_new_account is not None:
            input_["auto_enable_new_account"] = auto_enable_new_account

        response = execute_pipeline(
            OperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        response.response.close()
        return response.output

    def get_data_lake_organization_configuration(
        self, *, config_overrides: Optional[SecurityLakeClientConfig] = None
    ) -> "capo_securitylake.types.get_data_lake_organization_configuration_response.GetDataLakeOrganizationConfigurationResponse":
        """<p>Retrieves the configuration that will be automatically set up for accounts added to the organization after the organization has onboarded to Amazon Security Lake. This API does not take input parameters.</p>

        Raises:
            capo_securitylake.errors.access_denied_exception.AccessDeniedException: <p>You do not have sufficient access to perform this action. Access denied errors appear when Amazon Security Lake explicitly or implicitly denies an authorization request. An explicit denial occurs when a policy contains a Deny statement for the specific Amazon Web Services action. An implicit denial occurs when there is no applicable Deny statement and also no applicable Allow statement.</p>
            capo_securitylake.errors.bad_request_exception.BadRequestException: <p>The request is malformed or contains an error such as an invalid parameter value or a missing required parameter.</p>
            capo_securitylake.errors.conflict_exception.ConflictException: <p>Occurs when a conflict with a previous successful write is detected. This generally occurs when the previous write did not have time to propagate to the host serving the current request. A retry (with appropriate backoff logic) is the recommended response to this exception.</p>
            capo_securitylake.errors.internal_server_exception.InternalServerException: <p>Internal service exceptions are sometimes caused by transient issues. Before you start troubleshooting, perform the operation again.</p>
            capo_securitylake.errors.resource_not_found_exception.ResourceNotFoundException: <p>The resource could not be found.</p>
            capo_securitylake.errors.throttling_exception.ThrottlingException: <p>The limit on the number of requests per second was exceeded.</p>
            capo_securitylake.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        def _handler(
            req: "OperationRequest[capo_securitylake.types.get_data_lake_organization_configuration_request.GetDataLakeOrganizationConfigurationRequest]",
        ) -> OperationResponse[
            "capo_securitylake.types.get_data_lake_organization_configuration_response.GetDataLakeOrganizationConfigurationResponse"
        ]:
            import capo_securitylake._operations.security_lake.get_data_lake_organization_configuration

            output, http_response = (
                capo_securitylake._operations.security_lake.get_data_lake_organization_configuration.get_data_lake_organization_configuration(
                    req.options, req.input
                )
            )
            return OperationResponse(output=output, response=http_response)

        interceptors_, options_ = self._service.operation_options(config_overrides)
        input_: capo_securitylake.types.get_data_lake_organization_configuration_request.GetDataLakeOrganizationConfigurationRequest = {}

        response = execute_pipeline(
            OperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        response.response.close()
        return response.output

    def get_data_lake_sources(
        self,
        *,
        config_overrides: Optional[SecurityLakeClientConfig] = None,
        accounts: Optional["capo_securitylake.types.account_list.AccountList"] = None,
        max_results: Optional["capo_securitylake.types.max_results.MaxResults"] = None,
        next_token: Optional["capo_securitylake.types.next_token.NextToken"] = None,
    ) -> "capo_securitylake.types.get_data_lake_sources_response.GetDataLakeSourcesResponse":
        """<p>Retrieves a snapshot of the current Region, including whether Amazon Security Lake is enabled for those accounts and which sources Security Lake is collecting data from.</p>

        Args:
            accounts: <p>The Amazon Web Services account ID for which a static snapshot of the current Amazon Web Services Region, including enabled accounts and log sources, is retrieved.</p>
            max_results: <p>The maximum limit of accounts for which the static snapshot of the current Region, including enabled accounts and log sources, is retrieved.</p>
            next_token: <p>Lists if there are more results available. The value of nextToken is a unique pagination token for each page. Repeat the call using the returned token to retrieve the next page. Keep all other arguments unchanged.</p> <p>Each pagination token expires after 24 hours. Using an expired pagination token will return an HTTP 400 InvalidToken error.</p>

        Raises:
            capo_securitylake.errors.access_denied_exception.AccessDeniedException: <p>You do not have sufficient access to perform this action. Access denied errors appear when Amazon Security Lake explicitly or implicitly denies an authorization request. An explicit denial occurs when a policy contains a Deny statement for the specific Amazon Web Services action. An implicit denial occurs when there is no applicable Deny statement and also no applicable Allow statement.</p>
            capo_securitylake.errors.bad_request_exception.BadRequestException: <p>The request is malformed or contains an error such as an invalid parameter value or a missing required parameter.</p>
            capo_securitylake.errors.conflict_exception.ConflictException: <p>Occurs when a conflict with a previous successful write is detected. This generally occurs when the previous write did not have time to propagate to the host serving the current request. A retry (with appropriate backoff logic) is the recommended response to this exception.</p>
            capo_securitylake.errors.internal_server_exception.InternalServerException: <p>Internal service exceptions are sometimes caused by transient issues. Before you start troubleshooting, perform the operation again.</p>
            capo_securitylake.errors.resource_not_found_exception.ResourceNotFoundException: <p>The resource could not be found.</p>
            capo_securitylake.errors.throttling_exception.ThrottlingException: <p>The limit on the number of requests per second was exceeded.</p>
            capo_securitylake.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        def _handler(
            req: "OperationRequest[capo_securitylake.types.get_data_lake_sources_request.GetDataLakeSourcesRequest]",
        ) -> OperationResponse[
            "capo_securitylake.types.get_data_lake_sources_response.GetDataLakeSourcesResponse"
        ]:
            import capo_securitylake._operations.security_lake.get_data_lake_sources

            output, http_response = (
                capo_securitylake._operations.security_lake.get_data_lake_sources.get_data_lake_sources(
                    req.options, req.input
                )
            )
            return OperationResponse(output=output, response=http_response)

        interceptors_, options_ = self._service.operation_options(config_overrides)
        input_: capo_securitylake.types.get_data_lake_sources_request.GetDataLakeSourcesRequest = {}
        if accounts is not None:
            input_["accounts"] = accounts
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

    def list_data_lakes(
        self,
        *,
        config_overrides: Optional[SecurityLakeClientConfig] = None,
        regions: Optional["capo_securitylake.types.region_list.RegionList"] = None,
    ) -> "capo_securitylake.types.list_data_lakes_response.ListDataLakesResponse":
        """<p>Retrieves the Amazon Security Lake configuration object for the specified Amazon Web Services Regions. You can use this operation to determine whether Security Lake is enabled for a Region.</p>

        Args:
            regions: <p>The list of Regions where Security Lake is enabled.</p>

        Raises:
            capo_securitylake.errors.access_denied_exception.AccessDeniedException: <p>You do not have sufficient access to perform this action. Access denied errors appear when Amazon Security Lake explicitly or implicitly denies an authorization request. An explicit denial occurs when a policy contains a Deny statement for the specific Amazon Web Services action. An implicit denial occurs when there is no applicable Deny statement and also no applicable Allow statement.</p>
            capo_securitylake.errors.bad_request_exception.BadRequestException: <p>The request is malformed or contains an error such as an invalid parameter value or a missing required parameter.</p>
            capo_securitylake.errors.conflict_exception.ConflictException: <p>Occurs when a conflict with a previous successful write is detected. This generally occurs when the previous write did not have time to propagate to the host serving the current request. A retry (with appropriate backoff logic) is the recommended response to this exception.</p>
            capo_securitylake.errors.internal_server_exception.InternalServerException: <p>Internal service exceptions are sometimes caused by transient issues. Before you start troubleshooting, perform the operation again.</p>
            capo_securitylake.errors.resource_not_found_exception.ResourceNotFoundException: <p>The resource could not be found.</p>
            capo_securitylake.errors.throttling_exception.ThrottlingException: <p>The limit on the number of requests per second was exceeded.</p>
            capo_securitylake.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        def _handler(
            req: "OperationRequest[capo_securitylake.types.list_data_lakes_request.ListDataLakesRequest]",
        ) -> OperationResponse[
            "capo_securitylake.types.list_data_lakes_response.ListDataLakesResponse"
        ]:
            import capo_securitylake._operations.security_lake.list_data_lakes

            output, http_response = (
                capo_securitylake._operations.security_lake.list_data_lakes.list_data_lakes(
                    req.options, req.input
                )
            )
            return OperationResponse(output=output, response=http_response)

        interceptors_, options_ = self._service.operation_options(config_overrides)
        input_: capo_securitylake.types.list_data_lakes_request.ListDataLakesRequest = {}
        if regions is not None:
            input_["regions"] = regions

        response = execute_pipeline(
            OperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        response.response.close()
        return response.output

    def list_log_sources(
        self,
        *,
        config_overrides: Optional[SecurityLakeClientConfig] = None,
        accounts: Optional["capo_securitylake.types.account_list.AccountList"] = None,
        regions: Optional["capo_securitylake.types.region_list.RegionList"] = None,
        sources: Optional[
            "capo_securitylake.types.log_source_resource_list.LogSourceResourceList"
        ] = None,
        max_results: Optional["capo_securitylake.types.max_results.MaxResults"] = None,
        next_token: Optional["capo_securitylake.types.next_token.NextToken"] = None,
    ) -> "capo_securitylake.types.list_log_sources_response.ListLogSourcesResponse":
        """<p>Retrieves the log sources.</p>

        Args:
            accounts: <p>The list of Amazon Web Services accounts for which log sources are displayed.</p>
            regions: <p>The list of Regions for which log sources are displayed.</p>
            sources: <p>The list of sources for which log sources are displayed.</p>
            max_results: <p>The maximum number of accounts for which the log sources are displayed.</p>
            next_token: <p>If nextToken is returned, there are more results available. You can repeat the call using the returned token to retrieve the next page.</p>

        Raises:
            capo_securitylake.errors.access_denied_exception.AccessDeniedException: <p>You do not have sufficient access to perform this action. Access denied errors appear when Amazon Security Lake explicitly or implicitly denies an authorization request. An explicit denial occurs when a policy contains a Deny statement for the specific Amazon Web Services action. An implicit denial occurs when there is no applicable Deny statement and also no applicable Allow statement.</p>
            capo_securitylake.errors.bad_request_exception.BadRequestException: <p>The request is malformed or contains an error such as an invalid parameter value or a missing required parameter.</p>
            capo_securitylake.errors.conflict_exception.ConflictException: <p>Occurs when a conflict with a previous successful write is detected. This generally occurs when the previous write did not have time to propagate to the host serving the current request. A retry (with appropriate backoff logic) is the recommended response to this exception.</p>
            capo_securitylake.errors.internal_server_exception.InternalServerException: <p>Internal service exceptions are sometimes caused by transient issues. Before you start troubleshooting, perform the operation again.</p>
            capo_securitylake.errors.resource_not_found_exception.ResourceNotFoundException: <p>The resource could not be found.</p>
            capo_securitylake.errors.throttling_exception.ThrottlingException: <p>The limit on the number of requests per second was exceeded.</p>
            capo_securitylake.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        def _handler(
            req: "OperationRequest[capo_securitylake.types.list_log_sources_request.ListLogSourcesRequest]",
        ) -> OperationResponse[
            "capo_securitylake.types.list_log_sources_response.ListLogSourcesResponse"
        ]:
            import capo_securitylake._operations.security_lake.list_log_sources

            output, http_response = (
                capo_securitylake._operations.security_lake.list_log_sources.list_log_sources(
                    req.options, req.input
                )
            )
            return OperationResponse(output=output, response=http_response)

        interceptors_, options_ = self._service.operation_options(config_overrides)
        input_: capo_securitylake.types.list_log_sources_request.ListLogSourcesRequest = {}
        if accounts is not None:
            input_["accounts"] = accounts
        if regions is not None:
            input_["regions"] = regions
        if sources is not None:
            input_["sources"] = sources
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

    def update_data_lake(
        self,
        configurations: "capo_securitylake.types.data_lake_configuration_list.DataLakeConfigurationList",
        *,
        config_overrides: Optional[SecurityLakeClientConfig] = None,
        meta_store_manager_role_arn: Optional[
            "capo_securitylake.types.role_arn.RoleArn"
        ] = None,
    ) -> "capo_securitylake.types.update_data_lake_response.UpdateDataLakeResponse":
        """<p>You can use <code>UpdateDataLake</code> to specify where to store your security data, how it should be encrypted at rest and for how long. You can add a <a href="https://docs.aws.amazon.com/security-lake/latest/userguide/manage-regions.html#add-rollup-region">Rollup Region</a> to consolidate data from multiple Amazon Web Services Regions, replace default encryption (SSE-S3) with <a href="https://docs.aws.amazon.com/kms/latest/developerguide/concepts.html#customer-cmk">Customer Manged Key</a>, or specify transition and expiration actions through storage <a href="https://docs.aws.amazon.com/security-lake/latest/userguide/lifecycle-management.html">Lifecycle management</a>. The <code>UpdateDataLake</code> API works as an "upsert" operation that performs an insert if the specified item or record does not exist, or an update if it already exists. Security Lake securely stores your data at rest using Amazon Web Services encryption solutions. For more details, see <a href="https://docs.aws.amazon.com/security-lake/latest/userguide/data-protection.html">Data protection in Amazon Security Lake</a>.</p> <p>For example, omitting the key <code>encryptionConfiguration</code> from a Region that is included in an update call that currently uses KMS will leave that Region's KMS key in place, but specifying <code>encryptionConfiguration: {kmsKeyId: 'S3_MANAGED_KEY'}</code> for that same Region will reset the key to <code>S3-managed</code>.</p> <p>For more details about lifecycle management and how to update retention settings for one or more Regions after enabling Security Lake, see the <a href="https://docs.aws.amazon.com/security-lake/latest/userguide/lifecycle-management.html">Amazon Security Lake User Guide</a>. </p>

        Args:
            configurations: <p>Specifies the Region or Regions that will contribute data to the rollup region.</p>
            meta_store_manager_role_arn: <p>The Amazon Resource Name (ARN) used to create and update the Glue table. This table contains partitions generated by the ingestion and normalization of Amazon Web Services log sources and custom sources.</p>

        Raises:
            capo_securitylake.errors.access_denied_exception.AccessDeniedException: <p>You do not have sufficient access to perform this action. Access denied errors appear when Amazon Security Lake explicitly or implicitly denies an authorization request. An explicit denial occurs when a policy contains a Deny statement for the specific Amazon Web Services action. An implicit denial occurs when there is no applicable Deny statement and also no applicable Allow statement.</p>
            capo_securitylake.errors.bad_request_exception.BadRequestException: <p>The request is malformed or contains an error such as an invalid parameter value or a missing required parameter.</p>
            capo_securitylake.errors.conflict_exception.ConflictException: <p>Occurs when a conflict with a previous successful write is detected. This generally occurs when the previous write did not have time to propagate to the host serving the current request. A retry (with appropriate backoff logic) is the recommended response to this exception.</p>
            capo_securitylake.errors.internal_server_exception.InternalServerException: <p>Internal service exceptions are sometimes caused by transient issues. Before you start troubleshooting, perform the operation again.</p>
            capo_securitylake.errors.resource_not_found_exception.ResourceNotFoundException: <p>The resource could not be found.</p>
            capo_securitylake.errors.throttling_exception.ThrottlingException: <p>The limit on the number of requests per second was exceeded.</p>
            capo_securitylake.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        def _handler(
            req: "OperationRequest[capo_securitylake.types.update_data_lake_request.UpdateDataLakeRequest]",
        ) -> OperationResponse[
            "capo_securitylake.types.update_data_lake_response.UpdateDataLakeResponse"
        ]:
            import capo_securitylake._operations.security_lake.update_data_lake

            output, http_response = (
                capo_securitylake._operations.security_lake.update_data_lake.update_data_lake(
                    req.options, req.input
                )
            )
            return OperationResponse(output=output, response=http_response)

        interceptors_, options_ = self._service.operation_options(config_overrides)
        input_: capo_securitylake.types.update_data_lake_request.UpdateDataLakeRequest = {
            "configurations": configurations
        }
        if meta_store_manager_role_arn is not None:
            input_["meta_store_manager_role_arn"] = meta_store_manager_role_arn

        response = execute_pipeline(
            OperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        response.response.close()
        return response.output


class AsyncDataLake:
    def __init__(self, service: AsyncSecurityLakeClient) -> None:
        self._service = service

    async def create_aws_log_source(
        self,
        sources: "capo_securitylake.types.aws_log_source_configuration_list.AwsLogSourceConfigurationList",
        *,
        config_overrides: Optional[AsyncSecurityLakeClientConfig] = None,
    ) -> "capo_securitylake.types.create_aws_log_source_response.CreateAwsLogSourceResponse":
        """<p>Adds a natively supported Amazon Web Services service as an Amazon Security Lake source. Enables source types for member accounts in required Amazon Web Services Regions, based on the parameters you specify. You can choose any source type in any Region for either accounts that are part of a trusted organization or standalone accounts. Once you add an Amazon Web Services service as a source, Security Lake starts collecting logs and events from it.</p> <p>You can use this API only to enable natively supported Amazon Web Services services as a source. Use <code>CreateCustomLogSource</code> to enable data collection from a custom source.</p>

        Args:
            sources: <p>Specify the natively-supported Amazon Web Services service to add as a source in Security Lake.</p>

        Raises:
            capo_securitylake.errors.access_denied_exception.AccessDeniedException: <p>You do not have sufficient access to perform this action. Access denied errors appear when Amazon Security Lake explicitly or implicitly denies an authorization request. An explicit denial occurs when a policy contains a Deny statement for the specific Amazon Web Services action. An implicit denial occurs when there is no applicable Deny statement and also no applicable Allow statement.</p>
            capo_securitylake.errors.bad_request_exception.BadRequestException: <p>The request is malformed or contains an error such as an invalid parameter value or a missing required parameter.</p>
            capo_securitylake.errors.conflict_exception.ConflictException: <p>Occurs when a conflict with a previous successful write is detected. This generally occurs when the previous write did not have time to propagate to the host serving the current request. A retry (with appropriate backoff logic) is the recommended response to this exception.</p>
            capo_securitylake.errors.internal_server_exception.InternalServerException: <p>Internal service exceptions are sometimes caused by transient issues. Before you start troubleshooting, perform the operation again.</p>
            capo_securitylake.errors.resource_not_found_exception.ResourceNotFoundException: <p>The resource could not be found.</p>
            capo_securitylake.errors.throttling_exception.ThrottlingException: <p>The limit on the number of requests per second was exceeded.</p>
            capo_securitylake.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        async def _handler(
            req: "AsyncOperationRequest[capo_securitylake.types.create_aws_log_source_request.CreateAwsLogSourceRequest]",
        ) -> AsyncOperationResponse[
            "capo_securitylake.types.create_aws_log_source_response.CreateAwsLogSourceResponse"
        ]:
            import capo_securitylake._operations.security_lake.create_aws_log_source

            (
                output,
                http_response,
            ) = await capo_securitylake._operations.security_lake.create_aws_log_source.async_create_aws_log_source(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self._service.operation_options(config_overrides)
        input_: capo_securitylake.types.create_aws_log_source_request.CreateAwsLogSourceRequest = {
            "sources": sources
        }

        response = await aexecute_pipeline(
            AsyncOperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        await response.response.aclose()
        return response.output

    async def create_custom_log_source(
        self,
        source_name: "capo_securitylake.types.custom_log_source_name.CustomLogSourceName",
        configuration: "capo_securitylake.types.custom_log_source_configuration.CustomLogSourceConfiguration",
        *,
        config_overrides: Optional[AsyncSecurityLakeClientConfig] = None,
        source_version: Optional[
            "capo_securitylake.types.custom_log_source_version.CustomLogSourceVersion"
        ] = None,
        event_classes: Optional[
            "capo_securitylake.types.ocsf_event_class_list.OcsfEventClassList"
        ] = None,
    ) -> "capo_securitylake.types.create_custom_log_source_response.CreateCustomLogSourceResponse":
        """<p>Adds a third-party custom source in Amazon Security Lake, from the Amazon Web Services Region where you want to create a custom source. Security Lake can collect logs and events from third-party custom sources. After creating the appropriate IAM role to invoke Glue crawler, use this API to add a custom source name in Security Lake. This operation creates a partition in the Amazon S3 bucket for Security Lake as the target location for log files from the custom source. In addition, this operation also creates an associated Glue table and an Glue crawler.</p>

        Args:
            source_name: <p>Specify the name for a third-party custom source. This must be a Regionally unique value. The <code>sourceName</code> you enter here, is used in the <code>LogProviderRole</code> name which follows the convention <code>AmazonSecurityLake-Provider-{name of the custom source}-{region}</code>. You must use a <code>CustomLogSource</code> name that is shorter than or equal to 20 characters. This ensures that the <code>LogProviderRole</code> name is below the 64 character limit.</p>
            source_version: <p>Specify the source version for the third-party custom source, to limit log collection to a specific version of custom data source.</p>
            event_classes: <p>The Open Cybersecurity Schema Framework (OCSF) event classes which describes the type of data that the custom source will send to Security Lake. For the list of supported event classes, see the <a href="https://docs.aws.amazon.com/security-lake/latest/userguide/adding-custom-sources.html#ocsf-eventclass">Amazon Security Lake User Guide</a>.</p>
            configuration: <p>The configuration used for the third-party custom source.</p>

        Raises:
            capo_securitylake.errors.access_denied_exception.AccessDeniedException: <p>You do not have sufficient access to perform this action. Access denied errors appear when Amazon Security Lake explicitly or implicitly denies an authorization request. An explicit denial occurs when a policy contains a Deny statement for the specific Amazon Web Services action. An implicit denial occurs when there is no applicable Deny statement and also no applicable Allow statement.</p>
            capo_securitylake.errors.bad_request_exception.BadRequestException: <p>The request is malformed or contains an error such as an invalid parameter value or a missing required parameter.</p>
            capo_securitylake.errors.conflict_exception.ConflictException: <p>Occurs when a conflict with a previous successful write is detected. This generally occurs when the previous write did not have time to propagate to the host serving the current request. A retry (with appropriate backoff logic) is the recommended response to this exception.</p>
            capo_securitylake.errors.internal_server_exception.InternalServerException: <p>Internal service exceptions are sometimes caused by transient issues. Before you start troubleshooting, perform the operation again.</p>
            capo_securitylake.errors.resource_not_found_exception.ResourceNotFoundException: <p>The resource could not be found.</p>
            capo_securitylake.errors.throttling_exception.ThrottlingException: <p>The limit on the number of requests per second was exceeded.</p>
            capo_securitylake.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        async def _handler(
            req: "AsyncOperationRequest[capo_securitylake.types.create_custom_log_source_request.CreateCustomLogSourceRequest]",
        ) -> AsyncOperationResponse[
            "capo_securitylake.types.create_custom_log_source_response.CreateCustomLogSourceResponse"
        ]:
            import capo_securitylake._operations.security_lake.create_custom_log_source

            (
                output,
                http_response,
            ) = await capo_securitylake._operations.security_lake.create_custom_log_source.async_create_custom_log_source(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self._service.operation_options(config_overrides)
        input_: capo_securitylake.types.create_custom_log_source_request.CreateCustomLogSourceRequest = {
            "source_name": source_name,
            "configuration": configuration,
        }
        if source_version is not None:
            input_["source_version"] = source_version
        if event_classes is not None:
            input_["event_classes"] = event_classes

        response = await aexecute_pipeline(
            AsyncOperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        await response.response.aclose()
        return response.output

    async def create_data_lake(
        self,
        configurations: "capo_securitylake.types.data_lake_configuration_list.DataLakeConfigurationList",
        meta_store_manager_role_arn: "capo_securitylake.types.role_arn.RoleArn",
        *,
        config_overrides: Optional[AsyncSecurityLakeClientConfig] = None,
        tags: Optional["capo_securitylake.types.tag_list.TagList"] = None,
    ) -> "capo_securitylake.types.create_data_lake_response.CreateDataLakeResponse":
        """<p>Initializes an Amazon Security Lake instance with the provided (or default) configuration. You can enable Security Lake in Amazon Web Services Regions with customized settings before enabling log collection in Regions. To specify particular Regions, configure these Regions using the <code>configurations</code> parameter. If you have already enabled Security Lake in a Region when you call this command, the command will update the Region if you provide new configuration parameters. If you have not already enabled Security Lake in the Region when you call this API, it will set up the data lake in the Region with the specified configurations.</p> <p>When you enable Security Lake, it starts ingesting security data after the <code>CreateAwsLogSource</code> call and after you create subscribers using the <code>CreateSubscriber</code> API. This includes ingesting security data from sources, storing data, and making data accessible to subscribers. Security Lake also enables all the existing settings and resources that it stores or maintains for your Amazon Web Services account in the current Region, including security log and event data. For more information, see the <a href="https://docs.aws.amazon.com/security-lake/latest/userguide/what-is-security-lake.html">Amazon Security Lake User Guide</a>.</p>

        Args:
            configurations: <p>Specify the Region or Regions that will contribute data to the rollup region.</p>
            meta_store_manager_role_arn: <p>The Amazon Resource Name (ARN) used to create and update the Glue table. This table contains partitions generated by the ingestion and normalization of Amazon Web Services log sources and custom sources.</p>
            tags: <p>An array of objects, one for each tag to associate with the data lake configuration. For each tag, you must specify both a tag key and a tag value. A tag value cannot be null, but it can be an empty string.</p>

        Raises:
            capo_securitylake.errors.access_denied_exception.AccessDeniedException: <p>You do not have sufficient access to perform this action. Access denied errors appear when Amazon Security Lake explicitly or implicitly denies an authorization request. An explicit denial occurs when a policy contains a Deny statement for the specific Amazon Web Services action. An implicit denial occurs when there is no applicable Deny statement and also no applicable Allow statement.</p>
            capo_securitylake.errors.bad_request_exception.BadRequestException: <p>The request is malformed or contains an error such as an invalid parameter value or a missing required parameter.</p>
            capo_securitylake.errors.conflict_exception.ConflictException: <p>Occurs when a conflict with a previous successful write is detected. This generally occurs when the previous write did not have time to propagate to the host serving the current request. A retry (with appropriate backoff logic) is the recommended response to this exception.</p>
            capo_securitylake.errors.internal_server_exception.InternalServerException: <p>Internal service exceptions are sometimes caused by transient issues. Before you start troubleshooting, perform the operation again.</p>
            capo_securitylake.errors.resource_not_found_exception.ResourceNotFoundException: <p>The resource could not be found.</p>
            capo_securitylake.errors.throttling_exception.ThrottlingException: <p>The limit on the number of requests per second was exceeded.</p>
            capo_securitylake.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        async def _handler(
            req: "AsyncOperationRequest[capo_securitylake.types.create_data_lake_request.CreateDataLakeRequest]",
        ) -> AsyncOperationResponse[
            "capo_securitylake.types.create_data_lake_response.CreateDataLakeResponse"
        ]:
            import capo_securitylake._operations.security_lake.create_data_lake

            (
                output,
                http_response,
            ) = await capo_securitylake._operations.security_lake.create_data_lake.async_create_data_lake(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self._service.operation_options(config_overrides)
        input_: capo_securitylake.types.create_data_lake_request.CreateDataLakeRequest = {
            "configurations": configurations,
            "meta_store_manager_role_arn": meta_store_manager_role_arn,
        }
        if tags is not None:
            input_["tags"] = tags

        response = await aexecute_pipeline(
            AsyncOperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        await response.response.aclose()
        return response.output

    async def create_data_lake_organization_configuration(
        self,
        *,
        config_overrides: Optional[AsyncSecurityLakeClientConfig] = None,
        auto_enable_new_account: Optional[
            "capo_securitylake.types.data_lake_auto_enable_new_account_configuration_list.DataLakeAutoEnableNewAccountConfigurationList"
        ] = None,
    ) -> "capo_securitylake.types.create_data_lake_organization_configuration_response.CreateDataLakeOrganizationConfigurationResponse":
        """<p>Automatically enables Amazon Security Lake for new member accounts in your organization. Security Lake is not automatically enabled for any existing member accounts in your organization.</p> <p>This operation merges the new data lake organization configuration with the existing configuration for Security Lake in your organization. If you want to create a new data lake organization configuration, you must delete the existing one using <a href="https://docs.aws.amazon.com/security-lake/latest/APIReference/API_DeleteDataLakeOrganizationConfiguration.html">DeleteDataLakeOrganizationConfiguration</a>.</p>

        Args:
            auto_enable_new_account: <p>Enable Security Lake with the specified configuration settings, to begin collecting security data for new accounts in your organization.</p>

        Raises:
            capo_securitylake.errors.access_denied_exception.AccessDeniedException: <p>You do not have sufficient access to perform this action. Access denied errors appear when Amazon Security Lake explicitly or implicitly denies an authorization request. An explicit denial occurs when a policy contains a Deny statement for the specific Amazon Web Services action. An implicit denial occurs when there is no applicable Deny statement and also no applicable Allow statement.</p>
            capo_securitylake.errors.bad_request_exception.BadRequestException: <p>The request is malformed or contains an error such as an invalid parameter value or a missing required parameter.</p>
            capo_securitylake.errors.conflict_exception.ConflictException: <p>Occurs when a conflict with a previous successful write is detected. This generally occurs when the previous write did not have time to propagate to the host serving the current request. A retry (with appropriate backoff logic) is the recommended response to this exception.</p>
            capo_securitylake.errors.internal_server_exception.InternalServerException: <p>Internal service exceptions are sometimes caused by transient issues. Before you start troubleshooting, perform the operation again.</p>
            capo_securitylake.errors.resource_not_found_exception.ResourceNotFoundException: <p>The resource could not be found.</p>
            capo_securitylake.errors.throttling_exception.ThrottlingException: <p>The limit on the number of requests per second was exceeded.</p>
            capo_securitylake.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        async def _handler(
            req: "AsyncOperationRequest[capo_securitylake.types.create_data_lake_organization_configuration_request.CreateDataLakeOrganizationConfigurationRequest]",
        ) -> AsyncOperationResponse[
            "capo_securitylake.types.create_data_lake_organization_configuration_response.CreateDataLakeOrganizationConfigurationResponse"
        ]:
            import capo_securitylake._operations.security_lake.create_data_lake_organization_configuration

            (
                output,
                http_response,
            ) = await capo_securitylake._operations.security_lake.create_data_lake_organization_configuration.async_create_data_lake_organization_configuration(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self._service.operation_options(config_overrides)
        input_: capo_securitylake.types.create_data_lake_organization_configuration_request.CreateDataLakeOrganizationConfigurationRequest = {}
        if auto_enable_new_account is not None:
            input_["auto_enable_new_account"] = auto_enable_new_account

        response = await aexecute_pipeline(
            AsyncOperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        await response.response.aclose()
        return response.output

    async def delete_aws_log_source(
        self,
        sources: "capo_securitylake.types.aws_log_source_configuration_list.AwsLogSourceConfigurationList",
        *,
        config_overrides: Optional[AsyncSecurityLakeClientConfig] = None,
    ) -> "capo_securitylake.types.delete_aws_log_source_response.DeleteAwsLogSourceResponse":
        """<p>Removes a natively supported Amazon Web Services service as an Amazon Security Lake source. You can remove a source for one or more Regions. When you remove the source, Security Lake stops collecting data from that source in the specified Regions and accounts, and subscribers can no longer consume new data from the source. However, subscribers can still consume data that Security Lake collected from the source before removal.</p> <p>You can choose any source type in any Amazon Web Services Region for either accounts that are part of a trusted organization or standalone accounts. </p>

        Args:
            sources: <p>Specify the natively-supported Amazon Web Services service to remove as a source in Security Lake.</p>

        Raises:
            capo_securitylake.errors.access_denied_exception.AccessDeniedException: <p>You do not have sufficient access to perform this action. Access denied errors appear when Amazon Security Lake explicitly or implicitly denies an authorization request. An explicit denial occurs when a policy contains a Deny statement for the specific Amazon Web Services action. An implicit denial occurs when there is no applicable Deny statement and also no applicable Allow statement.</p>
            capo_securitylake.errors.bad_request_exception.BadRequestException: <p>The request is malformed or contains an error such as an invalid parameter value or a missing required parameter.</p>
            capo_securitylake.errors.conflict_exception.ConflictException: <p>Occurs when a conflict with a previous successful write is detected. This generally occurs when the previous write did not have time to propagate to the host serving the current request. A retry (with appropriate backoff logic) is the recommended response to this exception.</p>
            capo_securitylake.errors.internal_server_exception.InternalServerException: <p>Internal service exceptions are sometimes caused by transient issues. Before you start troubleshooting, perform the operation again.</p>
            capo_securitylake.errors.resource_not_found_exception.ResourceNotFoundException: <p>The resource could not be found.</p>
            capo_securitylake.errors.throttling_exception.ThrottlingException: <p>The limit on the number of requests per second was exceeded.</p>
            capo_securitylake.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        async def _handler(
            req: "AsyncOperationRequest[capo_securitylake.types.delete_aws_log_source_request.DeleteAwsLogSourceRequest]",
        ) -> AsyncOperationResponse[
            "capo_securitylake.types.delete_aws_log_source_response.DeleteAwsLogSourceResponse"
        ]:
            import capo_securitylake._operations.security_lake.delete_aws_log_source

            (
                output,
                http_response,
            ) = await capo_securitylake._operations.security_lake.delete_aws_log_source.async_delete_aws_log_source(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self._service.operation_options(config_overrides)
        input_: capo_securitylake.types.delete_aws_log_source_request.DeleteAwsLogSourceRequest = {
            "sources": sources
        }

        response = await aexecute_pipeline(
            AsyncOperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        await response.response.aclose()
        return response.output

    async def delete_custom_log_source(
        self,
        source_name: "capo_securitylake.types.custom_log_source_name.CustomLogSourceName",
        *,
        config_overrides: Optional[AsyncSecurityLakeClientConfig] = None,
        source_version: Optional[
            "capo_securitylake.types.custom_log_source_version.CustomLogSourceVersion"
        ] = None,
    ) -> "capo_securitylake.types.delete_custom_log_source_response.DeleteCustomLogSourceResponse":
        """<p>Removes a custom log source from Amazon Security Lake, to stop sending data from the custom source to Security Lake.</p>

        Args:
            source_name: <p>The source name of custom log source that you want to delete.</p>
            source_version: <p>The source version for the third-party custom source. You can limit the custom source removal to the specified source version.</p>

        Raises:
            capo_securitylake.errors.access_denied_exception.AccessDeniedException: <p>You do not have sufficient access to perform this action. Access denied errors appear when Amazon Security Lake explicitly or implicitly denies an authorization request. An explicit denial occurs when a policy contains a Deny statement for the specific Amazon Web Services action. An implicit denial occurs when there is no applicable Deny statement and also no applicable Allow statement.</p>
            capo_securitylake.errors.bad_request_exception.BadRequestException: <p>The request is malformed or contains an error such as an invalid parameter value or a missing required parameter.</p>
            capo_securitylake.errors.conflict_exception.ConflictException: <p>Occurs when a conflict with a previous successful write is detected. This generally occurs when the previous write did not have time to propagate to the host serving the current request. A retry (with appropriate backoff logic) is the recommended response to this exception.</p>
            capo_securitylake.errors.internal_server_exception.InternalServerException: <p>Internal service exceptions are sometimes caused by transient issues. Before you start troubleshooting, perform the operation again.</p>
            capo_securitylake.errors.resource_not_found_exception.ResourceNotFoundException: <p>The resource could not be found.</p>
            capo_securitylake.errors.throttling_exception.ThrottlingException: <p>The limit on the number of requests per second was exceeded.</p>
            capo_securitylake.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        async def _handler(
            req: "AsyncOperationRequest[capo_securitylake.types.delete_custom_log_source_request.DeleteCustomLogSourceRequest]",
        ) -> AsyncOperationResponse[
            "capo_securitylake.types.delete_custom_log_source_response.DeleteCustomLogSourceResponse"
        ]:
            import capo_securitylake._operations.security_lake.delete_custom_log_source

            (
                output,
                http_response,
            ) = await capo_securitylake._operations.security_lake.delete_custom_log_source.async_delete_custom_log_source(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self._service.operation_options(config_overrides)
        input_: capo_securitylake.types.delete_custom_log_source_request.DeleteCustomLogSourceRequest = {
            "source_name": source_name
        }
        if source_version is not None:
            input_["source_version"] = source_version

        response = await aexecute_pipeline(
            AsyncOperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        await response.response.aclose()
        return response.output

    async def delete_data_lake(
        self,
        regions: "capo_securitylake.types.region_list.RegionList",
        *,
        config_overrides: Optional[AsyncSecurityLakeClientConfig] = None,
    ) -> "capo_securitylake.types.delete_data_lake_response.DeleteDataLakeResponse":
        """<p>When you disable Amazon Security Lake from your account, Security Lake is disabled in all Amazon Web Services Regions and it stops collecting data from your sources. Also, this API automatically takes steps to remove the account from Security Lake. However, Security Lake retains all of your existing settings and the resources that it created in your Amazon Web Services account in the current Amazon Web Services Region.</p> <p>The <code>DeleteDataLake</code> operation does not delete the data that is stored in your Amazon S3 bucket, which is owned by your Amazon Web Services account. For more information, see the <a href="https://docs.aws.amazon.com/security-lake/latest/userguide/disable-security-lake.html">Amazon Security Lake User Guide</a>.</p>

        Args:
            regions: <p>The list of Regions where Security Lake is enabled.</p>

        Raises:
            capo_securitylake.errors.access_denied_exception.AccessDeniedException: <p>You do not have sufficient access to perform this action. Access denied errors appear when Amazon Security Lake explicitly or implicitly denies an authorization request. An explicit denial occurs when a policy contains a Deny statement for the specific Amazon Web Services action. An implicit denial occurs when there is no applicable Deny statement and also no applicable Allow statement.</p>
            capo_securitylake.errors.bad_request_exception.BadRequestException: <p>The request is malformed or contains an error such as an invalid parameter value or a missing required parameter.</p>
            capo_securitylake.errors.conflict_exception.ConflictException: <p>Occurs when a conflict with a previous successful write is detected. This generally occurs when the previous write did not have time to propagate to the host serving the current request. A retry (with appropriate backoff logic) is the recommended response to this exception.</p>
            capo_securitylake.errors.internal_server_exception.InternalServerException: <p>Internal service exceptions are sometimes caused by transient issues. Before you start troubleshooting, perform the operation again.</p>
            capo_securitylake.errors.resource_not_found_exception.ResourceNotFoundException: <p>The resource could not be found.</p>
            capo_securitylake.errors.throttling_exception.ThrottlingException: <p>The limit on the number of requests per second was exceeded.</p>
            capo_securitylake.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        async def _handler(
            req: "AsyncOperationRequest[capo_securitylake.types.delete_data_lake_request.DeleteDataLakeRequest]",
        ) -> AsyncOperationResponse[
            "capo_securitylake.types.delete_data_lake_response.DeleteDataLakeResponse"
        ]:
            import capo_securitylake._operations.security_lake.delete_data_lake

            (
                output,
                http_response,
            ) = await capo_securitylake._operations.security_lake.delete_data_lake.async_delete_data_lake(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self._service.operation_options(config_overrides)
        input_: capo_securitylake.types.delete_data_lake_request.DeleteDataLakeRequest = {
            "regions": regions
        }

        response = await aexecute_pipeline(
            AsyncOperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        await response.response.aclose()
        return response.output

    async def delete_data_lake_organization_configuration(
        self,
        *,
        config_overrides: Optional[AsyncSecurityLakeClientConfig] = None,
        auto_enable_new_account: Optional[
            "capo_securitylake.types.data_lake_auto_enable_new_account_configuration_list.DataLakeAutoEnableNewAccountConfigurationList"
        ] = None,
    ) -> "capo_securitylake.types.delete_data_lake_organization_configuration_response.DeleteDataLakeOrganizationConfigurationResponse":
        """<p>Turns off automatic enablement of Amazon Security Lake for member accounts that are added to an organization in Organizations. Only the delegated Security Lake administrator for an organization can perform this operation. If the delegated Security Lake administrator performs this operation, new member accounts won't automatically contribute data to the data lake.</p>

        Args:
            auto_enable_new_account: <p>Turns off automatic enablement of Security Lake for member accounts that are added to an organization.</p>

        Raises:
            capo_securitylake.errors.access_denied_exception.AccessDeniedException: <p>You do not have sufficient access to perform this action. Access denied errors appear when Amazon Security Lake explicitly or implicitly denies an authorization request. An explicit denial occurs when a policy contains a Deny statement for the specific Amazon Web Services action. An implicit denial occurs when there is no applicable Deny statement and also no applicable Allow statement.</p>
            capo_securitylake.errors.bad_request_exception.BadRequestException: <p>The request is malformed or contains an error such as an invalid parameter value or a missing required parameter.</p>
            capo_securitylake.errors.conflict_exception.ConflictException: <p>Occurs when a conflict with a previous successful write is detected. This generally occurs when the previous write did not have time to propagate to the host serving the current request. A retry (with appropriate backoff logic) is the recommended response to this exception.</p>
            capo_securitylake.errors.internal_server_exception.InternalServerException: <p>Internal service exceptions are sometimes caused by transient issues. Before you start troubleshooting, perform the operation again.</p>
            capo_securitylake.errors.resource_not_found_exception.ResourceNotFoundException: <p>The resource could not be found.</p>
            capo_securitylake.errors.throttling_exception.ThrottlingException: <p>The limit on the number of requests per second was exceeded.</p>
            capo_securitylake.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        async def _handler(
            req: "AsyncOperationRequest[capo_securitylake.types.delete_data_lake_organization_configuration_request.DeleteDataLakeOrganizationConfigurationRequest]",
        ) -> AsyncOperationResponse[
            "capo_securitylake.types.delete_data_lake_organization_configuration_response.DeleteDataLakeOrganizationConfigurationResponse"
        ]:
            import capo_securitylake._operations.security_lake.delete_data_lake_organization_configuration

            (
                output,
                http_response,
            ) = await capo_securitylake._operations.security_lake.delete_data_lake_organization_configuration.async_delete_data_lake_organization_configuration(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self._service.operation_options(config_overrides)
        input_: capo_securitylake.types.delete_data_lake_organization_configuration_request.DeleteDataLakeOrganizationConfigurationRequest = {}
        if auto_enable_new_account is not None:
            input_["auto_enable_new_account"] = auto_enable_new_account

        response = await aexecute_pipeline(
            AsyncOperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        await response.response.aclose()
        return response.output

    async def get_data_lake_organization_configuration(
        self, *, config_overrides: Optional[AsyncSecurityLakeClientConfig] = None
    ) -> "capo_securitylake.types.get_data_lake_organization_configuration_response.GetDataLakeOrganizationConfigurationResponse":
        """<p>Retrieves the configuration that will be automatically set up for accounts added to the organization after the organization has onboarded to Amazon Security Lake. This API does not take input parameters.</p>

        Raises:
            capo_securitylake.errors.access_denied_exception.AccessDeniedException: <p>You do not have sufficient access to perform this action. Access denied errors appear when Amazon Security Lake explicitly or implicitly denies an authorization request. An explicit denial occurs when a policy contains a Deny statement for the specific Amazon Web Services action. An implicit denial occurs when there is no applicable Deny statement and also no applicable Allow statement.</p>
            capo_securitylake.errors.bad_request_exception.BadRequestException: <p>The request is malformed or contains an error such as an invalid parameter value or a missing required parameter.</p>
            capo_securitylake.errors.conflict_exception.ConflictException: <p>Occurs when a conflict with a previous successful write is detected. This generally occurs when the previous write did not have time to propagate to the host serving the current request. A retry (with appropriate backoff logic) is the recommended response to this exception.</p>
            capo_securitylake.errors.internal_server_exception.InternalServerException: <p>Internal service exceptions are sometimes caused by transient issues. Before you start troubleshooting, perform the operation again.</p>
            capo_securitylake.errors.resource_not_found_exception.ResourceNotFoundException: <p>The resource could not be found.</p>
            capo_securitylake.errors.throttling_exception.ThrottlingException: <p>The limit on the number of requests per second was exceeded.</p>
            capo_securitylake.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        async def _handler(
            req: "AsyncOperationRequest[capo_securitylake.types.get_data_lake_organization_configuration_request.GetDataLakeOrganizationConfigurationRequest]",
        ) -> AsyncOperationResponse[
            "capo_securitylake.types.get_data_lake_organization_configuration_response.GetDataLakeOrganizationConfigurationResponse"
        ]:
            import capo_securitylake._operations.security_lake.get_data_lake_organization_configuration

            (
                output,
                http_response,
            ) = await capo_securitylake._operations.security_lake.get_data_lake_organization_configuration.async_get_data_lake_organization_configuration(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self._service.operation_options(config_overrides)
        input_: capo_securitylake.types.get_data_lake_organization_configuration_request.GetDataLakeOrganizationConfigurationRequest = {}

        response = await aexecute_pipeline(
            AsyncOperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        await response.response.aclose()
        return response.output

    async def get_data_lake_sources(
        self,
        *,
        config_overrides: Optional[AsyncSecurityLakeClientConfig] = None,
        accounts: Optional["capo_securitylake.types.account_list.AccountList"] = None,
        max_results: Optional["capo_securitylake.types.max_results.MaxResults"] = None,
        next_token: Optional["capo_securitylake.types.next_token.NextToken"] = None,
    ) -> "capo_securitylake.types.get_data_lake_sources_response.GetDataLakeSourcesResponse":
        """<p>Retrieves a snapshot of the current Region, including whether Amazon Security Lake is enabled for those accounts and which sources Security Lake is collecting data from.</p>

        Args:
            accounts: <p>The Amazon Web Services account ID for which a static snapshot of the current Amazon Web Services Region, including enabled accounts and log sources, is retrieved.</p>
            max_results: <p>The maximum limit of accounts for which the static snapshot of the current Region, including enabled accounts and log sources, is retrieved.</p>
            next_token: <p>Lists if there are more results available. The value of nextToken is a unique pagination token for each page. Repeat the call using the returned token to retrieve the next page. Keep all other arguments unchanged.</p> <p>Each pagination token expires after 24 hours. Using an expired pagination token will return an HTTP 400 InvalidToken error.</p>

        Raises:
            capo_securitylake.errors.access_denied_exception.AccessDeniedException: <p>You do not have sufficient access to perform this action. Access denied errors appear when Amazon Security Lake explicitly or implicitly denies an authorization request. An explicit denial occurs when a policy contains a Deny statement for the specific Amazon Web Services action. An implicit denial occurs when there is no applicable Deny statement and also no applicable Allow statement.</p>
            capo_securitylake.errors.bad_request_exception.BadRequestException: <p>The request is malformed or contains an error such as an invalid parameter value or a missing required parameter.</p>
            capo_securitylake.errors.conflict_exception.ConflictException: <p>Occurs when a conflict with a previous successful write is detected. This generally occurs when the previous write did not have time to propagate to the host serving the current request. A retry (with appropriate backoff logic) is the recommended response to this exception.</p>
            capo_securitylake.errors.internal_server_exception.InternalServerException: <p>Internal service exceptions are sometimes caused by transient issues. Before you start troubleshooting, perform the operation again.</p>
            capo_securitylake.errors.resource_not_found_exception.ResourceNotFoundException: <p>The resource could not be found.</p>
            capo_securitylake.errors.throttling_exception.ThrottlingException: <p>The limit on the number of requests per second was exceeded.</p>
            capo_securitylake.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        async def _handler(
            req: "AsyncOperationRequest[capo_securitylake.types.get_data_lake_sources_request.GetDataLakeSourcesRequest]",
        ) -> AsyncOperationResponse[
            "capo_securitylake.types.get_data_lake_sources_response.GetDataLakeSourcesResponse"
        ]:
            import capo_securitylake._operations.security_lake.get_data_lake_sources

            (
                output,
                http_response,
            ) = await capo_securitylake._operations.security_lake.get_data_lake_sources.async_get_data_lake_sources(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self._service.operation_options(config_overrides)
        input_: capo_securitylake.types.get_data_lake_sources_request.GetDataLakeSourcesRequest = {}
        if accounts is not None:
            input_["accounts"] = accounts
        if max_results is not None:
            input_["max_results"] = max_results
        if next_token is not None:
            input_["next_token"] = next_token

        response = await aexecute_pipeline(
            AsyncOperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        await response.response.aclose()
        return response.output

    async def list_data_lakes(
        self,
        *,
        config_overrides: Optional[AsyncSecurityLakeClientConfig] = None,
        regions: Optional["capo_securitylake.types.region_list.RegionList"] = None,
    ) -> "capo_securitylake.types.list_data_lakes_response.ListDataLakesResponse":
        """<p>Retrieves the Amazon Security Lake configuration object for the specified Amazon Web Services Regions. You can use this operation to determine whether Security Lake is enabled for a Region.</p>

        Args:
            regions: <p>The list of Regions where Security Lake is enabled.</p>

        Raises:
            capo_securitylake.errors.access_denied_exception.AccessDeniedException: <p>You do not have sufficient access to perform this action. Access denied errors appear when Amazon Security Lake explicitly or implicitly denies an authorization request. An explicit denial occurs when a policy contains a Deny statement for the specific Amazon Web Services action. An implicit denial occurs when there is no applicable Deny statement and also no applicable Allow statement.</p>
            capo_securitylake.errors.bad_request_exception.BadRequestException: <p>The request is malformed or contains an error such as an invalid parameter value or a missing required parameter.</p>
            capo_securitylake.errors.conflict_exception.ConflictException: <p>Occurs when a conflict with a previous successful write is detected. This generally occurs when the previous write did not have time to propagate to the host serving the current request. A retry (with appropriate backoff logic) is the recommended response to this exception.</p>
            capo_securitylake.errors.internal_server_exception.InternalServerException: <p>Internal service exceptions are sometimes caused by transient issues. Before you start troubleshooting, perform the operation again.</p>
            capo_securitylake.errors.resource_not_found_exception.ResourceNotFoundException: <p>The resource could not be found.</p>
            capo_securitylake.errors.throttling_exception.ThrottlingException: <p>The limit on the number of requests per second was exceeded.</p>
            capo_securitylake.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        async def _handler(
            req: "AsyncOperationRequest[capo_securitylake.types.list_data_lakes_request.ListDataLakesRequest]",
        ) -> AsyncOperationResponse[
            "capo_securitylake.types.list_data_lakes_response.ListDataLakesResponse"
        ]:
            import capo_securitylake._operations.security_lake.list_data_lakes

            (
                output,
                http_response,
            ) = await capo_securitylake._operations.security_lake.list_data_lakes.async_list_data_lakes(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self._service.operation_options(config_overrides)
        input_: capo_securitylake.types.list_data_lakes_request.ListDataLakesRequest = {}
        if regions is not None:
            input_["regions"] = regions

        response = await aexecute_pipeline(
            AsyncOperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        await response.response.aclose()
        return response.output

    async def list_log_sources(
        self,
        *,
        config_overrides: Optional[AsyncSecurityLakeClientConfig] = None,
        accounts: Optional["capo_securitylake.types.account_list.AccountList"] = None,
        regions: Optional["capo_securitylake.types.region_list.RegionList"] = None,
        sources: Optional[
            "capo_securitylake.types.log_source_resource_list.LogSourceResourceList"
        ] = None,
        max_results: Optional["capo_securitylake.types.max_results.MaxResults"] = None,
        next_token: Optional["capo_securitylake.types.next_token.NextToken"] = None,
    ) -> "capo_securitylake.types.list_log_sources_response.ListLogSourcesResponse":
        """<p>Retrieves the log sources.</p>

        Args:
            accounts: <p>The list of Amazon Web Services accounts for which log sources are displayed.</p>
            regions: <p>The list of Regions for which log sources are displayed.</p>
            sources: <p>The list of sources for which log sources are displayed.</p>
            max_results: <p>The maximum number of accounts for which the log sources are displayed.</p>
            next_token: <p>If nextToken is returned, there are more results available. You can repeat the call using the returned token to retrieve the next page.</p>

        Raises:
            capo_securitylake.errors.access_denied_exception.AccessDeniedException: <p>You do not have sufficient access to perform this action. Access denied errors appear when Amazon Security Lake explicitly or implicitly denies an authorization request. An explicit denial occurs when a policy contains a Deny statement for the specific Amazon Web Services action. An implicit denial occurs when there is no applicable Deny statement and also no applicable Allow statement.</p>
            capo_securitylake.errors.bad_request_exception.BadRequestException: <p>The request is malformed or contains an error such as an invalid parameter value or a missing required parameter.</p>
            capo_securitylake.errors.conflict_exception.ConflictException: <p>Occurs when a conflict with a previous successful write is detected. This generally occurs when the previous write did not have time to propagate to the host serving the current request. A retry (with appropriate backoff logic) is the recommended response to this exception.</p>
            capo_securitylake.errors.internal_server_exception.InternalServerException: <p>Internal service exceptions are sometimes caused by transient issues. Before you start troubleshooting, perform the operation again.</p>
            capo_securitylake.errors.resource_not_found_exception.ResourceNotFoundException: <p>The resource could not be found.</p>
            capo_securitylake.errors.throttling_exception.ThrottlingException: <p>The limit on the number of requests per second was exceeded.</p>
            capo_securitylake.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        async def _handler(
            req: "AsyncOperationRequest[capo_securitylake.types.list_log_sources_request.ListLogSourcesRequest]",
        ) -> AsyncOperationResponse[
            "capo_securitylake.types.list_log_sources_response.ListLogSourcesResponse"
        ]:
            import capo_securitylake._operations.security_lake.list_log_sources

            (
                output,
                http_response,
            ) = await capo_securitylake._operations.security_lake.list_log_sources.async_list_log_sources(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self._service.operation_options(config_overrides)
        input_: capo_securitylake.types.list_log_sources_request.ListLogSourcesRequest = {}
        if accounts is not None:
            input_["accounts"] = accounts
        if regions is not None:
            input_["regions"] = regions
        if sources is not None:
            input_["sources"] = sources
        if max_results is not None:
            input_["max_results"] = max_results
        if next_token is not None:
            input_["next_token"] = next_token

        response = await aexecute_pipeline(
            AsyncOperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        await response.response.aclose()
        return response.output

    async def update_data_lake(
        self,
        configurations: "capo_securitylake.types.data_lake_configuration_list.DataLakeConfigurationList",
        *,
        config_overrides: Optional[AsyncSecurityLakeClientConfig] = None,
        meta_store_manager_role_arn: Optional[
            "capo_securitylake.types.role_arn.RoleArn"
        ] = None,
    ) -> "capo_securitylake.types.update_data_lake_response.UpdateDataLakeResponse":
        """<p>You can use <code>UpdateDataLake</code> to specify where to store your security data, how it should be encrypted at rest and for how long. You can add a <a href="https://docs.aws.amazon.com/security-lake/latest/userguide/manage-regions.html#add-rollup-region">Rollup Region</a> to consolidate data from multiple Amazon Web Services Regions, replace default encryption (SSE-S3) with <a href="https://docs.aws.amazon.com/kms/latest/developerguide/concepts.html#customer-cmk">Customer Manged Key</a>, or specify transition and expiration actions through storage <a href="https://docs.aws.amazon.com/security-lake/latest/userguide/lifecycle-management.html">Lifecycle management</a>. The <code>UpdateDataLake</code> API works as an "upsert" operation that performs an insert if the specified item or record does not exist, or an update if it already exists. Security Lake securely stores your data at rest using Amazon Web Services encryption solutions. For more details, see <a href="https://docs.aws.amazon.com/security-lake/latest/userguide/data-protection.html">Data protection in Amazon Security Lake</a>.</p> <p>For example, omitting the key <code>encryptionConfiguration</code> from a Region that is included in an update call that currently uses KMS will leave that Region's KMS key in place, but specifying <code>encryptionConfiguration: {kmsKeyId: 'S3_MANAGED_KEY'}</code> for that same Region will reset the key to <code>S3-managed</code>.</p> <p>For more details about lifecycle management and how to update retention settings for one or more Regions after enabling Security Lake, see the <a href="https://docs.aws.amazon.com/security-lake/latest/userguide/lifecycle-management.html">Amazon Security Lake User Guide</a>. </p>

        Args:
            configurations: <p>Specifies the Region or Regions that will contribute data to the rollup region.</p>
            meta_store_manager_role_arn: <p>The Amazon Resource Name (ARN) used to create and update the Glue table. This table contains partitions generated by the ingestion and normalization of Amazon Web Services log sources and custom sources.</p>

        Raises:
            capo_securitylake.errors.access_denied_exception.AccessDeniedException: <p>You do not have sufficient access to perform this action. Access denied errors appear when Amazon Security Lake explicitly or implicitly denies an authorization request. An explicit denial occurs when a policy contains a Deny statement for the specific Amazon Web Services action. An implicit denial occurs when there is no applicable Deny statement and also no applicable Allow statement.</p>
            capo_securitylake.errors.bad_request_exception.BadRequestException: <p>The request is malformed or contains an error such as an invalid parameter value or a missing required parameter.</p>
            capo_securitylake.errors.conflict_exception.ConflictException: <p>Occurs when a conflict with a previous successful write is detected. This generally occurs when the previous write did not have time to propagate to the host serving the current request. A retry (with appropriate backoff logic) is the recommended response to this exception.</p>
            capo_securitylake.errors.internal_server_exception.InternalServerException: <p>Internal service exceptions are sometimes caused by transient issues. Before you start troubleshooting, perform the operation again.</p>
            capo_securitylake.errors.resource_not_found_exception.ResourceNotFoundException: <p>The resource could not be found.</p>
            capo_securitylake.errors.throttling_exception.ThrottlingException: <p>The limit on the number of requests per second was exceeded.</p>
            capo_securitylake.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        async def _handler(
            req: "AsyncOperationRequest[capo_securitylake.types.update_data_lake_request.UpdateDataLakeRequest]",
        ) -> AsyncOperationResponse[
            "capo_securitylake.types.update_data_lake_response.UpdateDataLakeResponse"
        ]:
            import capo_securitylake._operations.security_lake.update_data_lake

            (
                output,
                http_response,
            ) = await capo_securitylake._operations.security_lake.update_data_lake.async_update_data_lake(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self._service.operation_options(config_overrides)
        input_: capo_securitylake.types.update_data_lake_request.UpdateDataLakeRequest = {
            "configurations": configurations
        }
        if meta_store_manager_role_arn is not None:
            input_["meta_store_manager_role_arn"] = meta_store_manager_role_arn

        response = await aexecute_pipeline(
            AsyncOperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        await response.response.aclose()
        return response.output
