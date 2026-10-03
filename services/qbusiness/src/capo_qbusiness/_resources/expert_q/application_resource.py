from __future__ import annotations

import uuid
from typing import TYPE_CHECKING, Optional

import capo_qbusiness._auth._signers
import capo_qbusiness._auth._sigv4
from capo_qbusiness._services._pipeline import (
    AsyncOperationRequest,
    AsyncOperationResponse,
    OperationRequest,
    OperationResponse,
    aexecute_pipeline,
    execute_pipeline,
)

if TYPE_CHECKING:
    import capo_qbusiness.types.application
    import capo_qbusiness.types.application_id
    import capo_qbusiness.types.application_name
    import capo_qbusiness.types.attachments_configuration
    import capo_qbusiness.types.auto_subscription_configuration
    import capo_qbusiness.types.client_ids_for_oidc
    import capo_qbusiness.types.client_token
    import capo_qbusiness.types.create_application_request
    import capo_qbusiness.types.create_application_response
    import capo_qbusiness.types.delete_application_request
    import capo_qbusiness.types.delete_application_response
    import capo_qbusiness.types.description
    import capo_qbusiness.types.encryption_configuration
    import capo_qbusiness.types.get_application_request
    import capo_qbusiness.types.get_application_response
    import capo_qbusiness.types.iam_identity_provider_arn
    import capo_qbusiness.types.identity_type
    import capo_qbusiness.types.instance_arn
    import capo_qbusiness.types.list_applications_request
    import capo_qbusiness.types.list_applications_response
    import capo_qbusiness.types.max_results_integer_for_list_applications
    import capo_qbusiness.types.next_token
    import capo_qbusiness.types.personalization_configuration
    import capo_qbusiness.types.q_apps_configuration
    import capo_qbusiness.types.quick_sight_configuration
    import capo_qbusiness.types.role_arn
    import capo_qbusiness.types.tags
    import capo_qbusiness.types.update_application_request
    import capo_qbusiness.types.update_application_response
    from capo_qbusiness._services.async_q_business import (
        AsyncQBusinessClient,
        AsyncQBusinessClientConfig,
    )
    from capo_qbusiness._services.q_business import (
        QBusinessClient,
        QBusinessClientConfig,
    )


class ApplicationResource:
    def __init__(self, service: QBusinessClient) -> None:
        self._service = service

    def create(
        self,
        display_name: "capo_qbusiness.types.application_name.ApplicationName",
        *,
        config_overrides: Optional[QBusinessClientConfig] = None,
        role_arn: Optional["capo_qbusiness.types.role_arn.RoleArn"] = None,
        identity_type: Optional[
            "capo_qbusiness.types.identity_type.IdentityType"
        ] = None,
        iam_identity_provider_arn: Optional[
            "capo_qbusiness.types.iam_identity_provider_arn.IAMIdentityProviderArn"
        ] = None,
        identity_center_instance_arn: Optional[
            "capo_qbusiness.types.instance_arn.InstanceArn"
        ] = None,
        client_ids_for_oidc: Optional[
            "capo_qbusiness.types.client_ids_for_oidc.ClientIdsForOIDC"
        ] = None,
        description: Optional["capo_qbusiness.types.description.Description"] = None,
        encryption_configuration: Optional[
            "capo_qbusiness.types.encryption_configuration.EncryptionConfiguration"
        ] = None,
        tags: Optional["capo_qbusiness.types.tags.Tags"] = None,
        client_token: Optional["capo_qbusiness.types.client_token.ClientToken"] = None,
        attachments_configuration: Optional[
            "capo_qbusiness.types.attachments_configuration.AttachmentsConfiguration"
        ] = None,
        q_apps_configuration: Optional[
            "capo_qbusiness.types.q_apps_configuration.QAppsConfiguration"
        ] = None,
        personalization_configuration: Optional[
            "capo_qbusiness.types.personalization_configuration.PersonalizationConfiguration"
        ] = None,
        quick_sight_configuration: Optional[
            "capo_qbusiness.types.quick_sight_configuration.QuickSightConfiguration"
        ] = None,
    ) -> "capo_qbusiness.types.create_application_response.CreateApplicationResponse":
        """<p>Creates an Amazon Q Business application.</p> <note> <p>There are new tiers for Amazon Q Business. Not all features in Amazon Q Business Pro are also available in Amazon Q Business Lite. For information on what's included in Amazon Q Business Lite and what's included in Amazon Q Business Pro, see <a href="https://docs.aws.amazon.com/amazonq/latest/qbusiness-ug/tiers.html#user-sub-tiers">Amazon Q Business tiers</a>. You must use the Amazon Q Business console to assign subscription tiers to users. </p> <p>An Amazon Q Apps service linked role will be created if it's absent in the Amazon Web Services account when <code>QAppsConfiguration</code> is enabled in the request. For more information, see <a href="https://docs.aws.amazon.com/amazonq/latest/qbusiness-ug/using-service-linked-roles-qapps.html"> Using service-linked roles for Q Apps</a>.</p> <p>When you create an application, Amazon Q Business may securely transmit data for processing from your selected Amazon Web Services region, but within your geography. For more information, see <a href="https://docs.aws.amazon.com/amazonq/latest/qbusiness-ug/cross-region-inference.html">Cross region inference in Amazon Q Business</a>.</p> </note>

        Args:
            display_name: <p>A name for the Amazon Q Business application. </p>
            role_arn: <p> The Amazon Resource Name (ARN) of an IAM role with permissions to access your Amazon CloudWatch logs and metrics. If this property is not specified, Amazon Q Business will create a <a href="https://docs.aws.amazon.com/amazonq/latest/qbusiness-ug/using-service-linked-roles.html#slr-permissions">service linked role (SLR)</a> and use it as the application's role.</p>
            identity_type: <p>The authentication type being used by a Amazon Q Business application.</p>
            iam_identity_provider_arn: <p>The Amazon Resource Name (ARN) of an identity provider being used by an Amazon Q Business application.</p>
            identity_center_instance_arn: <p> The Amazon Resource Name (ARN) of the IAM Identity Center instance you are either creating for—or connecting to—your Amazon Q Business application.</p>
            client_ids_for_oidc: <p>The OIDC client ID for a Amazon Q Business application.</p>
            description: <p>A description for the Amazon Q Business application. </p>
            encryption_configuration: <p>The identifier of the KMS key that is used to encrypt your data. Amazon Q Business doesn't support asymmetric keys.</p>
            tags: <p>A list of key-value pairs that identify or categorize your Amazon Q Business application. You can also use tags to help control access to the application. Tag keys and values can consist of Unicode letters, digits, white space, and any of the following symbols: _ . : / = + - @.</p>
            client_token: <p>A token that you provide to identify the request to create your Amazon Q Business application.</p>
            attachments_configuration: <p>An option to allow end users to upload files directly during chat.</p>
            q_apps_configuration: <p>An option to allow end users to create and use Amazon Q Apps in the web experience.</p>
            personalization_configuration: <p>Configuration information about chat response personalization. For more information, see <a href="https://docs.aws.amazon.com/amazonq/latest/qbusiness-ug/personalizing-chat-responses.html">Personalizing chat responses</a> </p>
            quick_sight_configuration: <p>The Amazon Quick Suite configuration for an Amazon Q Business application that uses Quick Suite for authentication. This configuration is required if your application uses Quick Suite as the identity provider. For more information, see <a href="https://docs.aws.amazon.com/amazonq/latest/qbusiness-ug/create-quicksight-integrated-application.html">Creating an Amazon Quick Suite integrated application</a>.</p>

        Raises:
            capo_qbusiness.errors.access_denied_exception.AccessDeniedException: <p> You don't have access to perform this action. Make sure you have the required permission policies and user accounts and try again.</p>
            capo_qbusiness.errors.conflict_exception.ConflictException: <p>You are trying to perform an action that conflicts with the current status of your resource. Fix any inconsistencies with your resources and try again.</p>
            capo_qbusiness.errors.internal_server_exception.InternalServerException: <p>An issue occurred with the internal server used for your Amazon Q Business service. Wait some minutes and try again, or contact <a href="http://aws.amazon.com/contact-us/">Support</a> for help.</p>
            capo_qbusiness.errors.resource_not_found_exception.ResourceNotFoundException: <p>The application or plugin resource you want to use doesn’t exist. Make sure you have provided the correct resource and try again.</p>
            capo_qbusiness.errors.service_quota_exceeded_exception.ServiceQuotaExceededException: <p>You have exceeded the set limits for your Amazon Q Business service. </p>
            capo_qbusiness.errors.throttling_exception.ThrottlingException: <p>The request was denied due to throttling. Reduce the number of requests and try again.</p>
            capo_qbusiness.errors.validation_exception.ValidationException: <p>The input doesn't meet the constraints set by the Amazon Q Business service. Provide the correct input and try again.</p>
            capo_qbusiness.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        def _handler(
            req: "OperationRequest[capo_qbusiness.types.create_application_request.CreateApplicationRequest]",
        ) -> OperationResponse[
            "capo_qbusiness.types.create_application_response.CreateApplicationResponse"
        ]:
            import capo_qbusiness._operations.expert_q.create_application

            output, http_response = (
                capo_qbusiness._operations.expert_q.create_application.create_application(
                    req.options, req.input
                )
            )
            return OperationResponse(output=output, response=http_response)

        interceptors_, options_ = self._service.operation_options(config_overrides)
        input_: capo_qbusiness.types.create_application_request.CreateApplicationRequest = {
            "display_name": display_name
        }
        if role_arn is not None:
            input_["role_arn"] = role_arn
        if identity_type is not None:
            input_["identity_type"] = identity_type
        if iam_identity_provider_arn is not None:
            input_["iam_identity_provider_arn"] = iam_identity_provider_arn
        if identity_center_instance_arn is not None:
            input_["identity_center_instance_arn"] = identity_center_instance_arn
        if client_ids_for_oidc is not None:
            input_["client_ids_for_oidc"] = client_ids_for_oidc
        if description is not None:
            input_["description"] = description
        if encryption_configuration is not None:
            input_["encryption_configuration"] = encryption_configuration
        if tags is not None:
            input_["tags"] = tags
        if client_token is None:
            client_token = str(uuid.uuid4())
        input_["client_token"] = client_token
        if attachments_configuration is not None:
            input_["attachments_configuration"] = attachments_configuration
        if q_apps_configuration is not None:
            input_["q_apps_configuration"] = q_apps_configuration
        if personalization_configuration is not None:
            input_["personalization_configuration"] = personalization_configuration
        if quick_sight_configuration is not None:
            input_["quick_sight_configuration"] = quick_sight_configuration

        response = execute_pipeline(
            OperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        response.response.close()
        return response.output

    def read(
        self,
        application_id: "capo_qbusiness.types.application_id.ApplicationId",
        *,
        config_overrides: Optional[QBusinessClientConfig] = None,
    ) -> "capo_qbusiness.types.get_application_response.GetApplicationResponse":
        """<p>Gets information about an existing Amazon Q Business application.</p>

        Args:
            application_id: <p>The identifier of the Amazon Q Business application.</p>

        Raises:
            capo_qbusiness.errors.access_denied_exception.AccessDeniedException: <p> You don't have access to perform this action. Make sure you have the required permission policies and user accounts and try again.</p>
            capo_qbusiness.errors.internal_server_exception.InternalServerException: <p>An issue occurred with the internal server used for your Amazon Q Business service. Wait some minutes and try again, or contact <a href="http://aws.amazon.com/contact-us/">Support</a> for help.</p>
            capo_qbusiness.errors.resource_not_found_exception.ResourceNotFoundException: <p>The application or plugin resource you want to use doesn’t exist. Make sure you have provided the correct resource and try again.</p>
            capo_qbusiness.errors.throttling_exception.ThrottlingException: <p>The request was denied due to throttling. Reduce the number of requests and try again.</p>
            capo_qbusiness.errors.validation_exception.ValidationException: <p>The input doesn't meet the constraints set by the Amazon Q Business service. Provide the correct input and try again.</p>
            capo_qbusiness.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        def _handler(
            req: "OperationRequest[capo_qbusiness.types.get_application_request.GetApplicationRequest]",
        ) -> OperationResponse[
            "capo_qbusiness.types.get_application_response.GetApplicationResponse"
        ]:
            import capo_qbusiness._operations.expert_q.get_application

            output, http_response = (
                capo_qbusiness._operations.expert_q.get_application.get_application(
                    req.options, req.input
                )
            )
            return OperationResponse(output=output, response=http_response)

        interceptors_, options_ = self._service.operation_options(config_overrides)
        input_: capo_qbusiness.types.get_application_request.GetApplicationRequest = {
            "application_id": application_id
        }

        response = execute_pipeline(
            OperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        response.response.close()
        return response.output

    def update(
        self,
        application_id: "capo_qbusiness.types.application_id.ApplicationId",
        *,
        config_overrides: Optional[QBusinessClientConfig] = None,
        identity_center_instance_arn: Optional[
            "capo_qbusiness.types.instance_arn.InstanceArn"
        ] = None,
        display_name: Optional[
            "capo_qbusiness.types.application_name.ApplicationName"
        ] = None,
        description: Optional["capo_qbusiness.types.description.Description"] = None,
        role_arn: Optional["capo_qbusiness.types.role_arn.RoleArn"] = None,
        attachments_configuration: Optional[
            "capo_qbusiness.types.attachments_configuration.AttachmentsConfiguration"
        ] = None,
        q_apps_configuration: Optional[
            "capo_qbusiness.types.q_apps_configuration.QAppsConfiguration"
        ] = None,
        personalization_configuration: Optional[
            "capo_qbusiness.types.personalization_configuration.PersonalizationConfiguration"
        ] = None,
        auto_subscription_configuration: Optional[
            "capo_qbusiness.types.auto_subscription_configuration.AutoSubscriptionConfiguration"
        ] = None,
    ) -> "capo_qbusiness.types.update_application_response.UpdateApplicationResponse":
        """<p>Updates an existing Amazon Q Business application.</p> <note> <p>Amazon Q Business applications may securely transmit data for processing across Amazon Web Services Regions within your geography. For more information, see <a href="https://docs.aws.amazon.com/amazonq/latest/qbusiness-ug/cross-region-inference.html">Cross region inference in Amazon Q Business</a>.</p> </note> <note> <p>An Amazon Q Apps service-linked role will be created if it's absent in the Amazon Web Services account when <code>QAppsConfiguration</code> is enabled in the request. For more information, see <a href="https://docs.aws.amazon.com/amazonq/latest/qbusiness-ug/using-service-linked-roles-qapps.html">Using service-linked roles for Q Apps</a>. </p> </note>

        Args:
            application_id: <p>The identifier of the Amazon Q Business application.</p>
            identity_center_instance_arn: <p> The Amazon Resource Name (ARN) of the IAM Identity Center instance you are either creating for—or connecting to—your Amazon Q Business application.</p>
            display_name: <p>A name for the Amazon Q Business application.</p>
            description: <p>A description for the Amazon Q Business application.</p>
            role_arn: <p>An Amazon Web Services Identity and Access Management (IAM) role that gives Amazon Q Business permission to access Amazon CloudWatch logs and metrics.</p>
            attachments_configuration: <p>An option to allow end users to upload files directly during chat.</p>
            q_apps_configuration: <p>An option to allow end users to create and use Amazon Q Apps in the web experience.</p>
            personalization_configuration: <p>Configuration information about chat response personalization. For more information, see <a href="https://docs.aws.amazon.com/amazonq/latest/qbusiness-ug/personalizing-chat-responses.html">Personalizing chat responses</a>.</p>
            auto_subscription_configuration: <p>An option to enable updating the default subscription type assigned to an Amazon Q Business application using IAM identity federation for user management.</p>

        Raises:
            capo_qbusiness.errors.access_denied_exception.AccessDeniedException: <p> You don't have access to perform this action. Make sure you have the required permission policies and user accounts and try again.</p>
            capo_qbusiness.errors.conflict_exception.ConflictException: <p>You are trying to perform an action that conflicts with the current status of your resource. Fix any inconsistencies with your resources and try again.</p>
            capo_qbusiness.errors.internal_server_exception.InternalServerException: <p>An issue occurred with the internal server used for your Amazon Q Business service. Wait some minutes and try again, or contact <a href="http://aws.amazon.com/contact-us/">Support</a> for help.</p>
            capo_qbusiness.errors.resource_not_found_exception.ResourceNotFoundException: <p>The application or plugin resource you want to use doesn’t exist. Make sure you have provided the correct resource and try again.</p>
            capo_qbusiness.errors.throttling_exception.ThrottlingException: <p>The request was denied due to throttling. Reduce the number of requests and try again.</p>
            capo_qbusiness.errors.validation_exception.ValidationException: <p>The input doesn't meet the constraints set by the Amazon Q Business service. Provide the correct input and try again.</p>
            capo_qbusiness.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        def _handler(
            req: "OperationRequest[capo_qbusiness.types.update_application_request.UpdateApplicationRequest]",
        ) -> OperationResponse[
            "capo_qbusiness.types.update_application_response.UpdateApplicationResponse"
        ]:
            import capo_qbusiness._operations.expert_q.update_application

            output, http_response = (
                capo_qbusiness._operations.expert_q.update_application.update_application(
                    req.options, req.input
                )
            )
            return OperationResponse(output=output, response=http_response)

        interceptors_, options_ = self._service.operation_options(config_overrides)
        input_: capo_qbusiness.types.update_application_request.UpdateApplicationRequest = {
            "application_id": application_id
        }
        if identity_center_instance_arn is not None:
            input_["identity_center_instance_arn"] = identity_center_instance_arn
        if display_name is not None:
            input_["display_name"] = display_name
        if description is not None:
            input_["description"] = description
        if role_arn is not None:
            input_["role_arn"] = role_arn
        if attachments_configuration is not None:
            input_["attachments_configuration"] = attachments_configuration
        if q_apps_configuration is not None:
            input_["q_apps_configuration"] = q_apps_configuration
        if personalization_configuration is not None:
            input_["personalization_configuration"] = personalization_configuration
        if auto_subscription_configuration is not None:
            input_["auto_subscription_configuration"] = auto_subscription_configuration

        response = execute_pipeline(
            OperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        response.response.close()
        return response.output

    def delete(
        self,
        application_id: "capo_qbusiness.types.application_id.ApplicationId",
        *,
        config_overrides: Optional[QBusinessClientConfig] = None,
    ) -> "capo_qbusiness.types.delete_application_response.DeleteApplicationResponse":
        """<p>Deletes an Amazon Q Business application.</p>

        Args:
            application_id: <p>The identifier of the Amazon Q Business application.</p>

        Raises:
            capo_qbusiness.errors.access_denied_exception.AccessDeniedException: <p> You don't have access to perform this action. Make sure you have the required permission policies and user accounts and try again.</p>
            capo_qbusiness.errors.conflict_exception.ConflictException: <p>You are trying to perform an action that conflicts with the current status of your resource. Fix any inconsistencies with your resources and try again.</p>
            capo_qbusiness.errors.internal_server_exception.InternalServerException: <p>An issue occurred with the internal server used for your Amazon Q Business service. Wait some minutes and try again, or contact <a href="http://aws.amazon.com/contact-us/">Support</a> for help.</p>
            capo_qbusiness.errors.resource_not_found_exception.ResourceNotFoundException: <p>The application or plugin resource you want to use doesn’t exist. Make sure you have provided the correct resource and try again.</p>
            capo_qbusiness.errors.throttling_exception.ThrottlingException: <p>The request was denied due to throttling. Reduce the number of requests and try again.</p>
            capo_qbusiness.errors.validation_exception.ValidationException: <p>The input doesn't meet the constraints set by the Amazon Q Business service. Provide the correct input and try again.</p>
            capo_qbusiness.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        def _handler(
            req: "OperationRequest[capo_qbusiness.types.delete_application_request.DeleteApplicationRequest]",
        ) -> OperationResponse[
            "capo_qbusiness.types.delete_application_response.DeleteApplicationResponse"
        ]:
            import capo_qbusiness._operations.expert_q.delete_application

            output, http_response = (
                capo_qbusiness._operations.expert_q.delete_application.delete_application(
                    req.options, req.input
                )
            )
            return OperationResponse(output=output, response=http_response)

        interceptors_, options_ = self._service.operation_options(config_overrides)
        input_: capo_qbusiness.types.delete_application_request.DeleteApplicationRequest = {
            "application_id": application_id
        }

        response = execute_pipeline(
            OperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        response.response.close()
        return response.output

    def list(
        self,
        *,
        config_overrides: Optional[QBusinessClientConfig] = None,
        next_token: Optional["capo_qbusiness.types.next_token.NextToken"] = None,
        max_results: Optional[
            "capo_qbusiness.types.max_results_integer_for_list_applications.MaxResultsIntegerForListApplications"
        ] = None,
    ) -> "capo_qbusiness.types.list_applications_response.ListApplicationsResponse":
        """<p>Lists Amazon Q Business applications.</p> <note> <p>Amazon Q Business applications may securely transmit data for processing across Amazon Web Services Regions within your geography. For more information, see <a href="https://docs.aws.amazon.com/amazonq/latest/qbusiness-ug/cross-region-inference.html">Cross region inference in Amazon Q Business</a>.</p> </note>

        Args:
            next_token: <p>If the <code>maxResults</code> response was incomplete because there is more data to retrieve, Amazon Q Business returns a pagination token in the response. You can use this pagination token to retrieve the next set of Amazon Q Business applications.</p>
            max_results: <p>The maximum number of Amazon Q Business applications to return.</p>

        Raises:
            capo_qbusiness.errors.access_denied_exception.AccessDeniedException: <p> You don't have access to perform this action. Make sure you have the required permission policies and user accounts and try again.</p>
            capo_qbusiness.errors.internal_server_exception.InternalServerException: <p>An issue occurred with the internal server used for your Amazon Q Business service. Wait some minutes and try again, or contact <a href="http://aws.amazon.com/contact-us/">Support</a> for help.</p>
            capo_qbusiness.errors.throttling_exception.ThrottlingException: <p>The request was denied due to throttling. Reduce the number of requests and try again.</p>
            capo_qbusiness.errors.validation_exception.ValidationException: <p>The input doesn't meet the constraints set by the Amazon Q Business service. Provide the correct input and try again.</p>
            capo_qbusiness.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        def _handler(
            req: "OperationRequest[capo_qbusiness.types.list_applications_request.ListApplicationsRequest]",
        ) -> OperationResponse[
            "capo_qbusiness.types.list_applications_response.ListApplicationsResponse"
        ]:
            import capo_qbusiness._operations.expert_q.list_applications

            output, http_response = (
                capo_qbusiness._operations.expert_q.list_applications.list_applications(
                    req.options, req.input
                )
            )
            return OperationResponse(output=output, response=http_response)

        interceptors_, options_ = self._service.operation_options(config_overrides)
        input_: capo_qbusiness.types.list_applications_request.ListApplicationsRequest = {}
        if next_token is not None:
            input_["next_token"] = next_token
        if max_results is not None:
            input_["max_results"] = max_results

        response = execute_pipeline(
            OperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        response.response.close()
        return response.output


class AsyncApplicationResource:
    def __init__(self, service: AsyncQBusinessClient) -> None:
        self._service = service

    async def create(
        self,
        display_name: "capo_qbusiness.types.application_name.ApplicationName",
        *,
        config_overrides: Optional[AsyncQBusinessClientConfig] = None,
        role_arn: Optional["capo_qbusiness.types.role_arn.RoleArn"] = None,
        identity_type: Optional[
            "capo_qbusiness.types.identity_type.IdentityType"
        ] = None,
        iam_identity_provider_arn: Optional[
            "capo_qbusiness.types.iam_identity_provider_arn.IAMIdentityProviderArn"
        ] = None,
        identity_center_instance_arn: Optional[
            "capo_qbusiness.types.instance_arn.InstanceArn"
        ] = None,
        client_ids_for_oidc: Optional[
            "capo_qbusiness.types.client_ids_for_oidc.ClientIdsForOIDC"
        ] = None,
        description: Optional["capo_qbusiness.types.description.Description"] = None,
        encryption_configuration: Optional[
            "capo_qbusiness.types.encryption_configuration.EncryptionConfiguration"
        ] = None,
        tags: Optional["capo_qbusiness.types.tags.Tags"] = None,
        client_token: Optional["capo_qbusiness.types.client_token.ClientToken"] = None,
        attachments_configuration: Optional[
            "capo_qbusiness.types.attachments_configuration.AttachmentsConfiguration"
        ] = None,
        q_apps_configuration: Optional[
            "capo_qbusiness.types.q_apps_configuration.QAppsConfiguration"
        ] = None,
        personalization_configuration: Optional[
            "capo_qbusiness.types.personalization_configuration.PersonalizationConfiguration"
        ] = None,
        quick_sight_configuration: Optional[
            "capo_qbusiness.types.quick_sight_configuration.QuickSightConfiguration"
        ] = None,
    ) -> "capo_qbusiness.types.create_application_response.CreateApplicationResponse":
        """<p>Creates an Amazon Q Business application.</p> <note> <p>There are new tiers for Amazon Q Business. Not all features in Amazon Q Business Pro are also available in Amazon Q Business Lite. For information on what's included in Amazon Q Business Lite and what's included in Amazon Q Business Pro, see <a href="https://docs.aws.amazon.com/amazonq/latest/qbusiness-ug/tiers.html#user-sub-tiers">Amazon Q Business tiers</a>. You must use the Amazon Q Business console to assign subscription tiers to users. </p> <p>An Amazon Q Apps service linked role will be created if it's absent in the Amazon Web Services account when <code>QAppsConfiguration</code> is enabled in the request. For more information, see <a href="https://docs.aws.amazon.com/amazonq/latest/qbusiness-ug/using-service-linked-roles-qapps.html"> Using service-linked roles for Q Apps</a>.</p> <p>When you create an application, Amazon Q Business may securely transmit data for processing from your selected Amazon Web Services region, but within your geography. For more information, see <a href="https://docs.aws.amazon.com/amazonq/latest/qbusiness-ug/cross-region-inference.html">Cross region inference in Amazon Q Business</a>.</p> </note>

        Args:
            display_name: <p>A name for the Amazon Q Business application. </p>
            role_arn: <p> The Amazon Resource Name (ARN) of an IAM role with permissions to access your Amazon CloudWatch logs and metrics. If this property is not specified, Amazon Q Business will create a <a href="https://docs.aws.amazon.com/amazonq/latest/qbusiness-ug/using-service-linked-roles.html#slr-permissions">service linked role (SLR)</a> and use it as the application's role.</p>
            identity_type: <p>The authentication type being used by a Amazon Q Business application.</p>
            iam_identity_provider_arn: <p>The Amazon Resource Name (ARN) of an identity provider being used by an Amazon Q Business application.</p>
            identity_center_instance_arn: <p> The Amazon Resource Name (ARN) of the IAM Identity Center instance you are either creating for—or connecting to—your Amazon Q Business application.</p>
            client_ids_for_oidc: <p>The OIDC client ID for a Amazon Q Business application.</p>
            description: <p>A description for the Amazon Q Business application. </p>
            encryption_configuration: <p>The identifier of the KMS key that is used to encrypt your data. Amazon Q Business doesn't support asymmetric keys.</p>
            tags: <p>A list of key-value pairs that identify or categorize your Amazon Q Business application. You can also use tags to help control access to the application. Tag keys and values can consist of Unicode letters, digits, white space, and any of the following symbols: _ . : / = + - @.</p>
            client_token: <p>A token that you provide to identify the request to create your Amazon Q Business application.</p>
            attachments_configuration: <p>An option to allow end users to upload files directly during chat.</p>
            q_apps_configuration: <p>An option to allow end users to create and use Amazon Q Apps in the web experience.</p>
            personalization_configuration: <p>Configuration information about chat response personalization. For more information, see <a href="https://docs.aws.amazon.com/amazonq/latest/qbusiness-ug/personalizing-chat-responses.html">Personalizing chat responses</a> </p>
            quick_sight_configuration: <p>The Amazon Quick Suite configuration for an Amazon Q Business application that uses Quick Suite for authentication. This configuration is required if your application uses Quick Suite as the identity provider. For more information, see <a href="https://docs.aws.amazon.com/amazonq/latest/qbusiness-ug/create-quicksight-integrated-application.html">Creating an Amazon Quick Suite integrated application</a>.</p>

        Raises:
            capo_qbusiness.errors.access_denied_exception.AccessDeniedException: <p> You don't have access to perform this action. Make sure you have the required permission policies and user accounts and try again.</p>
            capo_qbusiness.errors.conflict_exception.ConflictException: <p>You are trying to perform an action that conflicts with the current status of your resource. Fix any inconsistencies with your resources and try again.</p>
            capo_qbusiness.errors.internal_server_exception.InternalServerException: <p>An issue occurred with the internal server used for your Amazon Q Business service. Wait some minutes and try again, or contact <a href="http://aws.amazon.com/contact-us/">Support</a> for help.</p>
            capo_qbusiness.errors.resource_not_found_exception.ResourceNotFoundException: <p>The application or plugin resource you want to use doesn’t exist. Make sure you have provided the correct resource and try again.</p>
            capo_qbusiness.errors.service_quota_exceeded_exception.ServiceQuotaExceededException: <p>You have exceeded the set limits for your Amazon Q Business service. </p>
            capo_qbusiness.errors.throttling_exception.ThrottlingException: <p>The request was denied due to throttling. Reduce the number of requests and try again.</p>
            capo_qbusiness.errors.validation_exception.ValidationException: <p>The input doesn't meet the constraints set by the Amazon Q Business service. Provide the correct input and try again.</p>
            capo_qbusiness.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        async def _handler(
            req: "AsyncOperationRequest[capo_qbusiness.types.create_application_request.CreateApplicationRequest]",
        ) -> AsyncOperationResponse[
            "capo_qbusiness.types.create_application_response.CreateApplicationResponse"
        ]:
            import capo_qbusiness._operations.expert_q.create_application

            (
                output,
                http_response,
            ) = await capo_qbusiness._operations.expert_q.create_application.async_create_application(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self._service.operation_options(config_overrides)
        input_: capo_qbusiness.types.create_application_request.CreateApplicationRequest = {
            "display_name": display_name
        }
        if role_arn is not None:
            input_["role_arn"] = role_arn
        if identity_type is not None:
            input_["identity_type"] = identity_type
        if iam_identity_provider_arn is not None:
            input_["iam_identity_provider_arn"] = iam_identity_provider_arn
        if identity_center_instance_arn is not None:
            input_["identity_center_instance_arn"] = identity_center_instance_arn
        if client_ids_for_oidc is not None:
            input_["client_ids_for_oidc"] = client_ids_for_oidc
        if description is not None:
            input_["description"] = description
        if encryption_configuration is not None:
            input_["encryption_configuration"] = encryption_configuration
        if tags is not None:
            input_["tags"] = tags
        if client_token is None:
            client_token = str(uuid.uuid4())
        input_["client_token"] = client_token
        if attachments_configuration is not None:
            input_["attachments_configuration"] = attachments_configuration
        if q_apps_configuration is not None:
            input_["q_apps_configuration"] = q_apps_configuration
        if personalization_configuration is not None:
            input_["personalization_configuration"] = personalization_configuration
        if quick_sight_configuration is not None:
            input_["quick_sight_configuration"] = quick_sight_configuration

        response = await aexecute_pipeline(
            AsyncOperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        await response.response.aclose()
        return response.output

    async def read(
        self,
        application_id: "capo_qbusiness.types.application_id.ApplicationId",
        *,
        config_overrides: Optional[AsyncQBusinessClientConfig] = None,
    ) -> "capo_qbusiness.types.get_application_response.GetApplicationResponse":
        """<p>Gets information about an existing Amazon Q Business application.</p>

        Args:
            application_id: <p>The identifier of the Amazon Q Business application.</p>

        Raises:
            capo_qbusiness.errors.access_denied_exception.AccessDeniedException: <p> You don't have access to perform this action. Make sure you have the required permission policies and user accounts and try again.</p>
            capo_qbusiness.errors.internal_server_exception.InternalServerException: <p>An issue occurred with the internal server used for your Amazon Q Business service. Wait some minutes and try again, or contact <a href="http://aws.amazon.com/contact-us/">Support</a> for help.</p>
            capo_qbusiness.errors.resource_not_found_exception.ResourceNotFoundException: <p>The application or plugin resource you want to use doesn’t exist. Make sure you have provided the correct resource and try again.</p>
            capo_qbusiness.errors.throttling_exception.ThrottlingException: <p>The request was denied due to throttling. Reduce the number of requests and try again.</p>
            capo_qbusiness.errors.validation_exception.ValidationException: <p>The input doesn't meet the constraints set by the Amazon Q Business service. Provide the correct input and try again.</p>
            capo_qbusiness.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        async def _handler(
            req: "AsyncOperationRequest[capo_qbusiness.types.get_application_request.GetApplicationRequest]",
        ) -> AsyncOperationResponse[
            "capo_qbusiness.types.get_application_response.GetApplicationResponse"
        ]:
            import capo_qbusiness._operations.expert_q.get_application

            (
                output,
                http_response,
            ) = await capo_qbusiness._operations.expert_q.get_application.async_get_application(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self._service.operation_options(config_overrides)
        input_: capo_qbusiness.types.get_application_request.GetApplicationRequest = {
            "application_id": application_id
        }

        response = await aexecute_pipeline(
            AsyncOperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        await response.response.aclose()
        return response.output

    async def update(
        self,
        application_id: "capo_qbusiness.types.application_id.ApplicationId",
        *,
        config_overrides: Optional[AsyncQBusinessClientConfig] = None,
        identity_center_instance_arn: Optional[
            "capo_qbusiness.types.instance_arn.InstanceArn"
        ] = None,
        display_name: Optional[
            "capo_qbusiness.types.application_name.ApplicationName"
        ] = None,
        description: Optional["capo_qbusiness.types.description.Description"] = None,
        role_arn: Optional["capo_qbusiness.types.role_arn.RoleArn"] = None,
        attachments_configuration: Optional[
            "capo_qbusiness.types.attachments_configuration.AttachmentsConfiguration"
        ] = None,
        q_apps_configuration: Optional[
            "capo_qbusiness.types.q_apps_configuration.QAppsConfiguration"
        ] = None,
        personalization_configuration: Optional[
            "capo_qbusiness.types.personalization_configuration.PersonalizationConfiguration"
        ] = None,
        auto_subscription_configuration: Optional[
            "capo_qbusiness.types.auto_subscription_configuration.AutoSubscriptionConfiguration"
        ] = None,
    ) -> "capo_qbusiness.types.update_application_response.UpdateApplicationResponse":
        """<p>Updates an existing Amazon Q Business application.</p> <note> <p>Amazon Q Business applications may securely transmit data for processing across Amazon Web Services Regions within your geography. For more information, see <a href="https://docs.aws.amazon.com/amazonq/latest/qbusiness-ug/cross-region-inference.html">Cross region inference in Amazon Q Business</a>.</p> </note> <note> <p>An Amazon Q Apps service-linked role will be created if it's absent in the Amazon Web Services account when <code>QAppsConfiguration</code> is enabled in the request. For more information, see <a href="https://docs.aws.amazon.com/amazonq/latest/qbusiness-ug/using-service-linked-roles-qapps.html">Using service-linked roles for Q Apps</a>. </p> </note>

        Args:
            application_id: <p>The identifier of the Amazon Q Business application.</p>
            identity_center_instance_arn: <p> The Amazon Resource Name (ARN) of the IAM Identity Center instance you are either creating for—or connecting to—your Amazon Q Business application.</p>
            display_name: <p>A name for the Amazon Q Business application.</p>
            description: <p>A description for the Amazon Q Business application.</p>
            role_arn: <p>An Amazon Web Services Identity and Access Management (IAM) role that gives Amazon Q Business permission to access Amazon CloudWatch logs and metrics.</p>
            attachments_configuration: <p>An option to allow end users to upload files directly during chat.</p>
            q_apps_configuration: <p>An option to allow end users to create and use Amazon Q Apps in the web experience.</p>
            personalization_configuration: <p>Configuration information about chat response personalization. For more information, see <a href="https://docs.aws.amazon.com/amazonq/latest/qbusiness-ug/personalizing-chat-responses.html">Personalizing chat responses</a>.</p>
            auto_subscription_configuration: <p>An option to enable updating the default subscription type assigned to an Amazon Q Business application using IAM identity federation for user management.</p>

        Raises:
            capo_qbusiness.errors.access_denied_exception.AccessDeniedException: <p> You don't have access to perform this action. Make sure you have the required permission policies and user accounts and try again.</p>
            capo_qbusiness.errors.conflict_exception.ConflictException: <p>You are trying to perform an action that conflicts with the current status of your resource. Fix any inconsistencies with your resources and try again.</p>
            capo_qbusiness.errors.internal_server_exception.InternalServerException: <p>An issue occurred with the internal server used for your Amazon Q Business service. Wait some minutes and try again, or contact <a href="http://aws.amazon.com/contact-us/">Support</a> for help.</p>
            capo_qbusiness.errors.resource_not_found_exception.ResourceNotFoundException: <p>The application or plugin resource you want to use doesn’t exist. Make sure you have provided the correct resource and try again.</p>
            capo_qbusiness.errors.throttling_exception.ThrottlingException: <p>The request was denied due to throttling. Reduce the number of requests and try again.</p>
            capo_qbusiness.errors.validation_exception.ValidationException: <p>The input doesn't meet the constraints set by the Amazon Q Business service. Provide the correct input and try again.</p>
            capo_qbusiness.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        async def _handler(
            req: "AsyncOperationRequest[capo_qbusiness.types.update_application_request.UpdateApplicationRequest]",
        ) -> AsyncOperationResponse[
            "capo_qbusiness.types.update_application_response.UpdateApplicationResponse"
        ]:
            import capo_qbusiness._operations.expert_q.update_application

            (
                output,
                http_response,
            ) = await capo_qbusiness._operations.expert_q.update_application.async_update_application(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self._service.operation_options(config_overrides)
        input_: capo_qbusiness.types.update_application_request.UpdateApplicationRequest = {
            "application_id": application_id
        }
        if identity_center_instance_arn is not None:
            input_["identity_center_instance_arn"] = identity_center_instance_arn
        if display_name is not None:
            input_["display_name"] = display_name
        if description is not None:
            input_["description"] = description
        if role_arn is not None:
            input_["role_arn"] = role_arn
        if attachments_configuration is not None:
            input_["attachments_configuration"] = attachments_configuration
        if q_apps_configuration is not None:
            input_["q_apps_configuration"] = q_apps_configuration
        if personalization_configuration is not None:
            input_["personalization_configuration"] = personalization_configuration
        if auto_subscription_configuration is not None:
            input_["auto_subscription_configuration"] = auto_subscription_configuration

        response = await aexecute_pipeline(
            AsyncOperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        await response.response.aclose()
        return response.output

    async def delete(
        self,
        application_id: "capo_qbusiness.types.application_id.ApplicationId",
        *,
        config_overrides: Optional[AsyncQBusinessClientConfig] = None,
    ) -> "capo_qbusiness.types.delete_application_response.DeleteApplicationResponse":
        """<p>Deletes an Amazon Q Business application.</p>

        Args:
            application_id: <p>The identifier of the Amazon Q Business application.</p>

        Raises:
            capo_qbusiness.errors.access_denied_exception.AccessDeniedException: <p> You don't have access to perform this action. Make sure you have the required permission policies and user accounts and try again.</p>
            capo_qbusiness.errors.conflict_exception.ConflictException: <p>You are trying to perform an action that conflicts with the current status of your resource. Fix any inconsistencies with your resources and try again.</p>
            capo_qbusiness.errors.internal_server_exception.InternalServerException: <p>An issue occurred with the internal server used for your Amazon Q Business service. Wait some minutes and try again, or contact <a href="http://aws.amazon.com/contact-us/">Support</a> for help.</p>
            capo_qbusiness.errors.resource_not_found_exception.ResourceNotFoundException: <p>The application or plugin resource you want to use doesn’t exist. Make sure you have provided the correct resource and try again.</p>
            capo_qbusiness.errors.throttling_exception.ThrottlingException: <p>The request was denied due to throttling. Reduce the number of requests and try again.</p>
            capo_qbusiness.errors.validation_exception.ValidationException: <p>The input doesn't meet the constraints set by the Amazon Q Business service. Provide the correct input and try again.</p>
            capo_qbusiness.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        async def _handler(
            req: "AsyncOperationRequest[capo_qbusiness.types.delete_application_request.DeleteApplicationRequest]",
        ) -> AsyncOperationResponse[
            "capo_qbusiness.types.delete_application_response.DeleteApplicationResponse"
        ]:
            import capo_qbusiness._operations.expert_q.delete_application

            (
                output,
                http_response,
            ) = await capo_qbusiness._operations.expert_q.delete_application.async_delete_application(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self._service.operation_options(config_overrides)
        input_: capo_qbusiness.types.delete_application_request.DeleteApplicationRequest = {
            "application_id": application_id
        }

        response = await aexecute_pipeline(
            AsyncOperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        await response.response.aclose()
        return response.output

    async def list(
        self,
        *,
        config_overrides: Optional[AsyncQBusinessClientConfig] = None,
        next_token: Optional["capo_qbusiness.types.next_token.NextToken"] = None,
        max_results: Optional[
            "capo_qbusiness.types.max_results_integer_for_list_applications.MaxResultsIntegerForListApplications"
        ] = None,
    ) -> "capo_qbusiness.types.list_applications_response.ListApplicationsResponse":
        """<p>Lists Amazon Q Business applications.</p> <note> <p>Amazon Q Business applications may securely transmit data for processing across Amazon Web Services Regions within your geography. For more information, see <a href="https://docs.aws.amazon.com/amazonq/latest/qbusiness-ug/cross-region-inference.html">Cross region inference in Amazon Q Business</a>.</p> </note>

        Args:
            next_token: <p>If the <code>maxResults</code> response was incomplete because there is more data to retrieve, Amazon Q Business returns a pagination token in the response. You can use this pagination token to retrieve the next set of Amazon Q Business applications.</p>
            max_results: <p>The maximum number of Amazon Q Business applications to return.</p>

        Raises:
            capo_qbusiness.errors.access_denied_exception.AccessDeniedException: <p> You don't have access to perform this action. Make sure you have the required permission policies and user accounts and try again.</p>
            capo_qbusiness.errors.internal_server_exception.InternalServerException: <p>An issue occurred with the internal server used for your Amazon Q Business service. Wait some minutes and try again, or contact <a href="http://aws.amazon.com/contact-us/">Support</a> for help.</p>
            capo_qbusiness.errors.throttling_exception.ThrottlingException: <p>The request was denied due to throttling. Reduce the number of requests and try again.</p>
            capo_qbusiness.errors.validation_exception.ValidationException: <p>The input doesn't meet the constraints set by the Amazon Q Business service. Provide the correct input and try again.</p>
            capo_qbusiness.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        async def _handler(
            req: "AsyncOperationRequest[capo_qbusiness.types.list_applications_request.ListApplicationsRequest]",
        ) -> AsyncOperationResponse[
            "capo_qbusiness.types.list_applications_response.ListApplicationsResponse"
        ]:
            import capo_qbusiness._operations.expert_q.list_applications

            (
                output,
                http_response,
            ) = await capo_qbusiness._operations.expert_q.list_applications.async_list_applications(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self._service.operation_options(config_overrides)
        input_: capo_qbusiness.types.list_applications_request.ListApplicationsRequest = {}
        if next_token is not None:
            input_["next_token"] = next_token
        if max_results is not None:
            input_["max_results"] = max_results

        response = await aexecute_pipeline(
            AsyncOperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        await response.response.aclose()
        return response.output
