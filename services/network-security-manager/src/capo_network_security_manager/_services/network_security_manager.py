"""Generated from Smithy shape ``com.amazonaws.networksecuritymanager#PiccoloCustomerAPIService``."""

import uuid
import warnings
from collections.abc import Iterator
from typing import TYPE_CHECKING, Any, Iterable, Optional

from typing_extensions import Self, TypedDict
from zapros import BaseHandler, Client

import capo_network_security_manager._auth._signers
import capo_network_security_manager._auth._sigv4
from capo_network_security_manager._auth._identity import Credentials
from capo_network_security_manager._auth._providers import (
    CredentialsProvider,
    IdentityProvider,
    StaticAwsCredentialsProvider,
    default_aws_credentials_chain,
)
from capo_network_security_manager._auth._zapros_handler import AuthMiddleware
from capo_network_security_manager._pagination import resolve_path as _resolve_path
from capo_network_security_manager._resources.piccolo_customer_api_service.deployment import (
    Deployment,
)
from capo_network_security_manager._resources.piccolo_customer_api_service.policy import (
    Policy,
)
from capo_network_security_manager._resources.piccolo_customer_api_service.rule import (
    Rule,
)
from capo_network_security_manager._resources.piccolo_customer_api_service.scope import (
    Scope,
)
from capo_network_security_manager._resources.piccolo_customer_api_service.template import (
    Template,
)
from capo_network_security_manager._services._aws_config import aws_config
from capo_network_security_manager._services._pipeline import (
    Interceptor,
    OperationOptions,
    OperationRequest,
    OperationResponse,
    execute_pipeline,
    retry,
)

if TYPE_CHECKING:
    import capo_network_security_manager.types.account_id
    import capo_network_security_manager.types.admin_account_summary
    import capo_network_security_manager.types.admin_priority
    import capo_network_security_manager.types.admin_scope_input
    import capo_network_security_manager.types.arn
    import capo_network_security_manager.types.create_deployment_input
    import capo_network_security_manager.types.create_deployment_output
    import capo_network_security_manager.types.create_deployment_snapshot_input
    import capo_network_security_manager.types.create_deployment_snapshot_output
    import capo_network_security_manager.types.create_policy_input
    import capo_network_security_manager.types.create_policy_output
    import capo_network_security_manager.types.create_policy_snapshot_input
    import capo_network_security_manager.types.create_policy_snapshot_output
    import capo_network_security_manager.types.create_rule_input
    import capo_network_security_manager.types.create_rule_output
    import capo_network_security_manager.types.create_rule_snapshot_input
    import capo_network_security_manager.types.create_rule_snapshot_output
    import capo_network_security_manager.types.create_scope_input
    import capo_network_security_manager.types.create_scope_output
    import capo_network_security_manager.types.create_scope_snapshot_input
    import capo_network_security_manager.types.create_scope_snapshot_output
    import capo_network_security_manager.types.create_template_input
    import capo_network_security_manager.types.create_template_output
    import capo_network_security_manager.types.create_template_snapshot_input
    import capo_network_security_manager.types.create_template_snapshot_output
    import capo_network_security_manager.types.delete_admin_account_request
    import capo_network_security_manager.types.delete_deployment_input
    import capo_network_security_manager.types.delete_policy_input
    import capo_network_security_manager.types.delete_rule_input
    import capo_network_security_manager.types.delete_scope_input
    import capo_network_security_manager.types.delete_template_input
    import capo_network_security_manager.types.deployment_configuration
    import capo_network_security_manager.types.deployment_identifier
    import capo_network_security_manager.types.deployment_name
    import capo_network_security_manager.types.deployment_summary
    import capo_network_security_manager.types.description
    import capo_network_security_manager.types.entity_status_filter
    import capo_network_security_manager.types.generate_rule_configuration_request
    import capo_network_security_manager.types.generate_rule_configuration_response
    import capo_network_security_manager.types.get_admin_account_request
    import capo_network_security_manager.types.get_admin_account_response
    import capo_network_security_manager.types.get_deployment_input
    import capo_network_security_manager.types.get_deployment_output
    import capo_network_security_manager.types.get_policy_input
    import capo_network_security_manager.types.get_policy_output
    import capo_network_security_manager.types.get_rule_input
    import capo_network_security_manager.types.get_rule_output
    import capo_network_security_manager.types.get_scope_input
    import capo_network_security_manager.types.get_scope_output
    import capo_network_security_manager.types.get_template_input
    import capo_network_security_manager.types.get_template_output
    import capo_network_security_manager.types.idempotency_token
    import capo_network_security_manager.types.is_published
    import capo_network_security_manager.types.json_document
    import capo_network_security_manager.types.list_admin_accounts_request
    import capo_network_security_manager.types.list_admin_accounts_response
    import capo_network_security_manager.types.list_aggregate_resource_synchronization_statuses_input
    import capo_network_security_manager.types.list_aggregate_resource_synchronization_statuses_output
    import capo_network_security_manager.types.list_deployment_snapshots_input
    import capo_network_security_manager.types.list_deployment_snapshots_output
    import capo_network_security_manager.types.list_deployments_input
    import capo_network_security_manager.types.list_deployments_output
    import capo_network_security_manager.types.list_policies_input
    import capo_network_security_manager.types.list_policies_output
    import capo_network_security_manager.types.list_policy_snapshots_input
    import capo_network_security_manager.types.list_policy_snapshots_output
    import capo_network_security_manager.types.list_resource_associations_input
    import capo_network_security_manager.types.list_resource_associations_output
    import capo_network_security_manager.types.list_resource_synchronization_statuses_input
    import capo_network_security_manager.types.list_resource_synchronization_statuses_output
    import capo_network_security_manager.types.list_rule_snapshots_input
    import capo_network_security_manager.types.list_rule_snapshots_output
    import capo_network_security_manager.types.list_rules_input
    import capo_network_security_manager.types.list_rules_output
    import capo_network_security_manager.types.list_scope_snapshots_input
    import capo_network_security_manager.types.list_scope_snapshots_output
    import capo_network_security_manager.types.list_scopes_input
    import capo_network_security_manager.types.list_scopes_output
    import capo_network_security_manager.types.list_tags_for_resource_input
    import capo_network_security_manager.types.list_tags_for_resource_output
    import capo_network_security_manager.types.list_template_snapshots_input
    import capo_network_security_manager.types.list_template_snapshots_output
    import capo_network_security_manager.types.list_templates_input
    import capo_network_security_manager.types.list_templates_output
    import capo_network_security_manager.types.max_results
    import capo_network_security_manager.types.next_token
    import capo_network_security_manager.types.policy_configuration
    import capo_network_security_manager.types.policy_firewall_type
    import capo_network_security_manager.types.policy_identifier
    import capo_network_security_manager.types.policy_name
    import capo_network_security_manager.types.policy_reference_list
    import capo_network_security_manager.types.policy_summary
    import capo_network_security_manager.types.priority
    import capo_network_security_manager.types.put_admin_account_request
    import capo_network_security_manager.types.put_admin_account_response
    import capo_network_security_manager.types.resource_association
    import capo_network_security_manager.types.resource_identifier
    import capo_network_security_manager.types.resource_synchronization_status_summary
    import capo_network_security_manager.types.rule_firewall_type
    import capo_network_security_manager.types.rule_identifier
    import capo_network_security_manager.types.rule_name
    import capo_network_security_manager.types.rule_reference_list
    import capo_network_security_manager.types.rule_summary
    import capo_network_security_manager.types.rule_type
    import capo_network_security_manager.types.scope_configuration
    import capo_network_security_manager.types.scope_identifier
    import capo_network_security_manager.types.scope_name
    import capo_network_security_manager.types.scope_reference_list
    import capo_network_security_manager.types.scope_summary
    import capo_network_security_manager.types.sensitive_string
    import capo_network_security_manager.types.synchronization_status
    import capo_network_security_manager.types.tag_key_list
    import capo_network_security_manager.types.tag_map
    import capo_network_security_manager.types.tag_resource_input
    import capo_network_security_manager.types.tag_resource_output
    import capo_network_security_manager.types.template_and_rule_reference_list
    import capo_network_security_manager.types.template_firewall_type
    import capo_network_security_manager.types.template_identifier
    import capo_network_security_manager.types.template_name
    import capo_network_security_manager.types.template_summary
    import capo_network_security_manager.types.untag_resource_input
    import capo_network_security_manager.types.untag_resource_output
    import capo_network_security_manager.types.update_deployment_input
    import capo_network_security_manager.types.update_deployment_output
    import capo_network_security_manager.types.update_policy_input
    import capo_network_security_manager.types.update_policy_output
    import capo_network_security_manager.types.update_rule_input
    import capo_network_security_manager.types.update_rule_output
    import capo_network_security_manager.types.update_scope_input
    import capo_network_security_manager.types.update_scope_output
    import capo_network_security_manager.types.update_template_input
    import capo_network_security_manager.types.update_template_output
    import capo_network_security_manager.types.update_token
    import capo_network_security_manager.types.waf_config_data_type


class NetworkSecurityManagerClientConfig(TypedDict, total=False, closed=True):
    operation_interceptors: Iterable[Interceptor[Any, Any]]
    retry_max_attempts: int | None
    use_fips: bool | None
    endpoint: str | None
    region: str | None
    credentials_provider: IdentityProvider[Credentials] | None


class NetworkSecurityManagerClient:
    """A client for the ``NetworkSecurityManager`` service.

    Args:
        http_handler: HTTP handler for sending requests. If not provided, creates a default handler.
        operation_interceptors: Interceptors that wrap every operation call. If not provided, defaults to an empty list.
        retry_max_attempts: Maximum number of times to retry a failed operation. Defaults to 3.
        use_fips: The value of the ``AWS::UseFIPS`` endpoint parameter.
        endpoint: The value of the ``SDK::Endpoint`` endpoint parameter.
        region: The value of the ``AWS::Region`` endpoint parameter.
        credentials: AWS credentials for request signing.
        credentials_provider: Provider that resolves AWS credentials. Takes precedence over ``credentials``.
    """

    def __init__(
        self,
        http_handler: BaseHandler | None = None,
        operation_interceptors: Iterable[Interceptor[Any, Any]] | None = None,
        retry_max_attempts: int | None = None,
        use_fips: bool | None = None,
        endpoint: str | None = None,
        region: str | None = None,
        credentials: Credentials | None = None,
        credentials_provider: CredentialsProvider | None = None,
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
        self._config = NetworkSecurityManagerClientConfig(
            {
                "operation_interceptors": operation_interceptors or [],
                "retry_max_attempts": retry_max_attempts,
                "use_fips": use_fips,
                "endpoint": endpoint,
                "region": region,
                "credentials_provider": resolved_credentials_provider,
            }
        )

        # resources
        self.deployment = Deployment(self)
        self.policy = Policy(self)
        self.rule = Rule(self)
        self.scope = Scope(self)
        self.template = Template(self)

    def operation_options(
        self, config_overrides: Optional[NetworkSecurityManagerClientConfig] = None
    ) -> tuple[Iterable[Interceptor[Any, Any]], OperationOptions]:
        overrides: NetworkSecurityManagerClientConfig = config_overrides or {}
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
            use_fips=overrides.get("use_fips", self._config.get("use_fips")),
            endpoint=overrides.get("endpoint", self._config.get("endpoint")),
            region=overrides.get("region", self._config.get("region")),
            credentials_provider=overrides.get(
                "credentials_provider", self._config.get("credentials_provider")
            ),
        )
        return interceptors_, options_

    def delete_admin_account(
        self,
        account_id: "capo_network_security_manager.types.account_id.AccountId",
        *,
        config_overrides: Optional[NetworkSecurityManagerClientConfig] = None,
    ) -> None:
        """<p>Removes the specified AWS Network Security Manager administrator account.</p>

        Args:
            account_id: <p>The AWS account ID of the administrator account to remove.</p>

        Raises:
            capo_network_security_manager.errors.access_denied_exception.AccessDeniedException: <p>You do not have sufficient permissions to perform this action.</p>
            capo_network_security_manager.errors.internal_server_exception.InternalServerException: <p>The request processing failed because of an internal error in the service. This is a retryable error.</p>
            capo_network_security_manager.errors.throttling_exception.ThrottlingException: <p>The request was denied because of request throttling. Reduce your request rate and try again.</p>
            capo_network_security_manager.errors.validation_exception.ValidationException: <p>The request failed validation. For details, see the <code>reason</code> and <code>fieldList</code> members of the response.</p>
            capo_network_security_manager.errors.UnknownServiceError: The service returned an error code this client does not model.

        Examples:
            Remove an administrator account
            Removes an account's Network Security Manager administrator designation.

            >>> client.delete_admin_account(account_id='234567890123')
        """

        def _handler(
            req: "OperationRequest[capo_network_security_manager.types.delete_admin_account_request.DeleteAdminAccountRequest]",
        ) -> OperationResponse[None]:
            import capo_network_security_manager._operations.piccolo_customer_api_service.delete_admin_account

            output, http_response = (
                capo_network_security_manager._operations.piccolo_customer_api_service.delete_admin_account.delete_admin_account(
                    req.options, req.input
                )
            )
            return OperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_network_security_manager.types.delete_admin_account_request.DeleteAdminAccountRequest = {
            "account_id": account_id
        }

        response = execute_pipeline(
            OperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        response.response.close()
        return response.output

    def generate_rule_configuration(
        self,
        prompt: "capo_network_security_manager.types.sensitive_string.SensitiveString",
        rule_firewall_type: "capo_network_security_manager.types.rule_firewall_type.RuleFirewallType",
        rule_type: "capo_network_security_manager.types.rule_type.RuleType",
        *,
        config_overrides: Optional[NetworkSecurityManagerClientConfig] = None,
        waf_config_data_type: Optional[
            "capo_network_security_manager.types.waf_config_data_type.WAFConfigDataType"
        ] = None,
        current_configuration: Optional[str] = None,
        client_token: Optional[
            "capo_network_security_manager.types.idempotency_token.IdempotencyToken"
        ] = None,
    ) -> "capo_network_security_manager.types.generate_rule_configuration_response.GenerateRuleConfigurationResponse":
        """<p>Generates a rule configuration from a natural-language description. Provide a prompt along with the rule's firewall type and rule type. The service returns a configuration that you can use when you create or update a rule. If you also provide an existing configuration, the service edits that configuration instead of generating a new one.</p>

        Args:
            prompt: <p>A natural-language description of the configuration that you want to generate.</p>
            rule_firewall_type: <p>The firewall type of the rule.</p>
            rule_type: <p>The type of the rule. <code>CONFIGURATION</code> rules contain firewall settings, and <code>INSPECTION</code> rules contain rule groups.</p>
            waf_config_data_type: <p>For AWS WAF configuration rules, the specific AWS WAF configuration variant to generate. This is optional; if you omit it, the service selects the variant.</p>
            current_configuration: <p>An existing configuration to edit, as a JSON string. When you provide this value, the operation edits the configuration. When you omit it, the operation generates a new configuration.</p>
            client_token: <p>A unique, case-sensitive token that you provide to ensure that the operation completes no more than one time. If you retry a request with the same client token and the same parameters, the service returns the result of the original successful request.</p>

        Raises:
            capo_network_security_manager.errors.access_denied_exception.AccessDeniedException: <p>You do not have sufficient permissions to perform this action.</p>
            capo_network_security_manager.errors.internal_server_exception.InternalServerException: <p>The request processing failed because of an internal error in the service. This is a retryable error.</p>
            capo_network_security_manager.errors.throttling_exception.ThrottlingException: <p>The request was denied because of request throttling. Reduce your request rate and try again.</p>
            capo_network_security_manager.errors.validation_exception.ValidationException: <p>The request failed validation. For details, see the <code>reason</code> and <code>fieldList</code> members of the response.</p>
            capo_network_security_manager.errors.UnknownServiceError: The service returned an error code this client does not model.

        Examples:
            Generate a rule configuration from a description
            Generates a firewall rule configuration from a natural language description. The response contains the generated configuration as a JSON string, ready to use as the configuration of a rule.

            >>> client.generate_rule_configuration(prompt='Create a rate limiting rule that blocks IP addresses sending more than 2000 requests in 5 minutes', rule_firewall_type='WAF', rule_type='INSPECTION', client_token='550e8400-e29b-41d4-a716-446655440015')
        """

        def _handler(
            req: "OperationRequest[capo_network_security_manager.types.generate_rule_configuration_request.GenerateRuleConfigurationRequest]",
        ) -> OperationResponse[
            "capo_network_security_manager.types.generate_rule_configuration_response.GenerateRuleConfigurationResponse"
        ]:
            import capo_network_security_manager._operations.piccolo_customer_api_service.generate_rule_configuration

            output, http_response = (
                capo_network_security_manager._operations.piccolo_customer_api_service.generate_rule_configuration.generate_rule_configuration(
                    req.options, req.input
                )
            )
            return OperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_network_security_manager.types.generate_rule_configuration_request.GenerateRuleConfigurationRequest = {
            "prompt": prompt,
            "rule_firewall_type": rule_firewall_type,
            "rule_type": rule_type,
        }
        if waf_config_data_type is not None:
            input_["waf_config_data_type"] = waf_config_data_type
        if current_configuration is not None:
            input_["current_configuration"] = current_configuration
        if client_token is None:
            client_token = str(uuid.uuid4())
        input_["client_token"] = client_token

        response = execute_pipeline(
            OperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        response.response.close()
        return response.output

    def get_admin_account(
        self,
        account_id: "capo_network_security_manager.types.account_id.AccountId",
        *,
        config_overrides: Optional[NetworkSecurityManagerClientConfig] = None,
    ) -> "capo_network_security_manager.types.get_admin_account_response.GetAdminAccountResponse":
        """<p>Retrieves the details of the specified AWS Network Security Manager administrator account.</p>

        Args:
            account_id: <p>The AWS account ID of the administrator account to retrieve.</p>

        Raises:
            capo_network_security_manager.errors.access_denied_exception.AccessDeniedException: <p>You do not have sufficient permissions to perform this action.</p>
            capo_network_security_manager.errors.internal_server_exception.InternalServerException: <p>The request processing failed because of an internal error in the service. This is a retryable error.</p>
            capo_network_security_manager.errors.resource_not_found_exception.ResourceNotFoundException: <p>The specified resource was not found. Verify that the resource identifier is correct and that the resource exists, then try your request again.</p>
            capo_network_security_manager.errors.throttling_exception.ThrottlingException: <p>The request was denied because of request throttling. Reduce your request rate and try again.</p>
            capo_network_security_manager.errors.validation_exception.ValidationException: <p>The request failed validation. For details, see the <code>reason</code> and <code>fieldList</code> members of the response.</p>
            capo_network_security_manager.errors.UnknownServiceError: The service returned an error code this client does not model.

        Examples:
            Get an administrator account
            Retrieves the details and administrative scope of a Network Security Manager administrator account.

            >>> client.get_admin_account(account_id='234567890123')
        """

        def _handler(
            req: "OperationRequest[capo_network_security_manager.types.get_admin_account_request.GetAdminAccountRequest]",
        ) -> OperationResponse[
            "capo_network_security_manager.types.get_admin_account_response.GetAdminAccountResponse"
        ]:
            import capo_network_security_manager._operations.piccolo_customer_api_service.get_admin_account

            output, http_response = (
                capo_network_security_manager._operations.piccolo_customer_api_service.get_admin_account.get_admin_account(
                    req.options, req.input
                )
            )
            return OperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_network_security_manager.types.get_admin_account_request.GetAdminAccountRequest = {
            "account_id": account_id
        }

        response = execute_pipeline(
            OperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        response.response.close()
        return response.output

    def list_admin_accounts(
        self,
        *,
        config_overrides: Optional[NetworkSecurityManagerClientConfig] = None,
        max_results: Optional[
            "capo_network_security_manager.types.max_results.MaxResults"
        ] = None,
        next_token: Optional[
            "capo_network_security_manager.types.next_token.NextToken"
        ] = None,
    ) -> "capo_network_security_manager.types.list_admin_accounts_response.ListAdminAccountsResponse":
        """<p>Lists the AWS Network Security Manager administrator accounts in the organization.</p>

        Args:
            max_results: <p>The maximum number of results to return in a single call. Valid range: 1-100. To retrieve the remaining results, use the returned <code>nextToken</code> value in a subsequent call.</p>
            next_token: <p>The token for the next page of results. To retrieve the next page, call the operation again and provide this value. When there are no more results, this value is null.</p>

        Raises:
            capo_network_security_manager.errors.access_denied_exception.AccessDeniedException: <p>You do not have sufficient permissions to perform this action.</p>
            capo_network_security_manager.errors.internal_server_exception.InternalServerException: <p>The request processing failed because of an internal error in the service. This is a retryable error.</p>
            capo_network_security_manager.errors.throttling_exception.ThrottlingException: <p>The request was denied because of request throttling. Reduce your request rate and try again.</p>
            capo_network_security_manager.errors.validation_exception.ValidationException: <p>The request failed validation. For details, see the <code>reason</code> and <code>fieldList</code> members of the response.</p>
            capo_network_security_manager.errors.UnknownServiceError: The service returned an error code this client does not model.

        Examples:
            List administrator accounts
            Lists the Network Security Manager administrator accounts for the organization.

            >>> client.list_admin_accounts(max_results=10)
        """

        def _handler(
            req: "OperationRequest[capo_network_security_manager.types.list_admin_accounts_request.ListAdminAccountsRequest]",
        ) -> OperationResponse[
            "capo_network_security_manager.types.list_admin_accounts_response.ListAdminAccountsResponse"
        ]:
            import capo_network_security_manager._operations.piccolo_customer_api_service.list_admin_accounts

            output, http_response = (
                capo_network_security_manager._operations.piccolo_customer_api_service.list_admin_accounts.list_admin_accounts(
                    req.options, req.input
                )
            )
            return OperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_network_security_manager.types.list_admin_accounts_request.ListAdminAccountsRequest = {}
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

    def iter_list_admin_accounts(
        self,
        *,
        config_overrides: Optional[NetworkSecurityManagerClientConfig] = None,
        max_results: Optional[
            "capo_network_security_manager.types.max_results.MaxResults"
        ] = None,
        next_token: Optional[
            "capo_network_security_manager.types.next_token.NextToken"
        ] = None,
    ) -> "Iterator[capo_network_security_manager.types.admin_account_summary.AdminAccountSummary]":
        _token = next_token
        while True:
            _response = self.list_admin_accounts(
                config_overrides=config_overrides,
                max_results=max_results,
                next_token=_token,
            )
            _page = _resolve_path(_response, ("admin_accounts",))
            for _item in _page or []:
                yield _item
            _token = _resolve_path(_response, ("next_token",))
            if not _token:
                break

    def list_aggregate_resource_synchronization_statuses(
        self,
        *,
        config_overrides: Optional[NetworkSecurityManagerClientConfig] = None,
        synchronization_status: Optional[
            "capo_network_security_manager.types.synchronization_status.SynchronizationStatus"
        ] = None,
        max_results: Optional[
            "capo_network_security_manager.types.max_results.MaxResults"
        ] = None,
        next_token: Optional[
            "capo_network_security_manager.types.next_token.NextToken"
        ] = None,
    ) -> "capo_network_security_manager.types.list_aggregate_resource_synchronization_statuses_output.ListAggregateResourceSynchronizationStatusesOutput":
        """<p>Lists the aggregated synchronization statuses of resources across the deployments in your administrator account. You can filter the results by synchronization status and page through them.</p>

        Args:
            synchronization_status: <p>Filters the results by synchronization status, such as <code>IN_SYNC</code> or <code>OUT_OF_SYNC</code>.</p>
            max_results: <p>The maximum number of results to return in a single call. Valid range: 1-100. To retrieve the remaining results, use the returned <code>nextToken</code> value in a subsequent call.</p>
            next_token: <p>The token for the next page of results. To retrieve the next page, call the operation again and provide this value. When there are no more results, this value is null.</p>

        Raises:
            capo_network_security_manager.errors.access_denied_exception.AccessDeniedException: <p>You do not have sufficient permissions to perform this action.</p>
            capo_network_security_manager.errors.internal_server_exception.InternalServerException: <p>The request processing failed because of an internal error in the service. This is a retryable error.</p>
            capo_network_security_manager.errors.throttling_exception.ThrottlingException: <p>The request was denied because of request throttling. Reduce your request rate and try again.</p>
            capo_network_security_manager.errors.validation_exception.ValidationException: <p>The request failed validation. For details, see the <code>reason</code> and <code>fieldList</code> members of the response.</p>
            capo_network_security_manager.errors.UnknownServiceError: The service returned an error code this client does not model.

        Examples:
            List synchronization statuses across all deployments
            Lists the aggregate synchronization status of resources across all deployments in the account.

            >>> client.list_aggregate_resource_synchronization_statuses(synchronization_status='IN_SYNC', max_results=10)
        """

        def _handler(
            req: "OperationRequest[capo_network_security_manager.types.list_aggregate_resource_synchronization_statuses_input.ListAggregateResourceSynchronizationStatusesInput]",
        ) -> OperationResponse[
            "capo_network_security_manager.types.list_aggregate_resource_synchronization_statuses_output.ListAggregateResourceSynchronizationStatusesOutput"
        ]:
            import capo_network_security_manager._operations.piccolo_customer_api_service.list_aggregate_resource_synchronization_statuses

            output, http_response = (
                capo_network_security_manager._operations.piccolo_customer_api_service.list_aggregate_resource_synchronization_statuses.list_aggregate_resource_synchronization_statuses(
                    req.options, req.input
                )
            )
            return OperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_network_security_manager.types.list_aggregate_resource_synchronization_statuses_input.ListAggregateResourceSynchronizationStatusesInput = {}
        if synchronization_status is not None:
            input_["synchronization_status"] = synchronization_status
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

    def iter_list_aggregate_resource_synchronization_statuses(
        self,
        *,
        config_overrides: Optional[NetworkSecurityManagerClientConfig] = None,
        synchronization_status: Optional[
            "capo_network_security_manager.types.synchronization_status.SynchronizationStatus"
        ] = None,
        max_results: Optional[
            "capo_network_security_manager.types.max_results.MaxResults"
        ] = None,
        next_token: Optional[
            "capo_network_security_manager.types.next_token.NextToken"
        ] = None,
    ) -> "Iterator[capo_network_security_manager.types.resource_synchronization_status_summary.ResourceSynchronizationStatusSummary]":
        _token = next_token
        while True:
            _response = self.list_aggregate_resource_synchronization_statuses(
                config_overrides=config_overrides,
                synchronization_status=synchronization_status,
                max_results=max_results,
                next_token=_token,
            )
            _page = _resolve_path(_response, ("resource_synchronization_statuses",))
            for _item in _page or []:
                yield _item
            _token = _resolve_path(_response, ("next_token",))
            if not _token:
                break

    def list_resource_associations(
        self,
        resource_identifier: "capo_network_security_manager.types.resource_identifier.ResourceIdentifier",
        *,
        config_overrides: Optional[NetworkSecurityManagerClientConfig] = None,
        max_results: Optional[
            "capo_network_security_manager.types.max_results.MaxResults"
        ] = None,
        next_token: Optional[
            "capo_network_security_manager.types.next_token.NextToken"
        ] = None,
    ) -> "capo_network_security_manager.types.list_resource_associations_output.ListResourceAssociationsOutput":
        """<p>Lists the resources associated with the specified resource.</p>

        Args:
            resource_identifier: <p>The identifier of the resource to list associations for. This is the resource's Amazon Resource Name (ARN).</p>
            max_results: <p>The maximum number of results to return in a single call. Valid range: 1-100. To retrieve the remaining results, use the returned <code>nextToken</code> value in a subsequent call.</p>
            next_token: <p>The token for the next page of results. To retrieve the next page, call the operation again and provide this value. When there are no more results, this value is null.</p>

        Raises:
            capo_network_security_manager.errors.access_denied_exception.AccessDeniedException: <p>You do not have sufficient permissions to perform this action.</p>
            capo_network_security_manager.errors.internal_server_exception.InternalServerException: <p>The request processing failed because of an internal error in the service. This is a retryable error.</p>
            capo_network_security_manager.errors.throttling_exception.ThrottlingException: <p>The request was denied because of request throttling. Reduce your request rate and try again.</p>
            capo_network_security_manager.errors.validation_exception.ValidationException: <p>The request failed validation. For details, see the <code>reason</code> and <code>fieldList</code> members of the response.</p>
            capo_network_security_manager.errors.UnknownServiceError: The service returned an error code this client does not model.

        Examples:
            List what references a rule
            Lists the resources that reference the given rule, such as the templates and policies it is associated with.

            >>> client.list_resource_associations(resource_identifier='arn:aws:network-security-manager:us-east-1:123456789012:rule:abc123', max_results=10)
        """

        def _handler(
            req: "OperationRequest[capo_network_security_manager.types.list_resource_associations_input.ListResourceAssociationsInput]",
        ) -> OperationResponse[
            "capo_network_security_manager.types.list_resource_associations_output.ListResourceAssociationsOutput"
        ]:
            import capo_network_security_manager._operations.piccolo_customer_api_service.list_resource_associations

            output, http_response = (
                capo_network_security_manager._operations.piccolo_customer_api_service.list_resource_associations.list_resource_associations(
                    req.options, req.input
                )
            )
            return OperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_network_security_manager.types.list_resource_associations_input.ListResourceAssociationsInput = {
            "resource_identifier": resource_identifier
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

    def iter_list_resource_associations(
        self,
        resource_identifier: "capo_network_security_manager.types.resource_identifier.ResourceIdentifier",
        *,
        config_overrides: Optional[NetworkSecurityManagerClientConfig] = None,
        max_results: Optional[
            "capo_network_security_manager.types.max_results.MaxResults"
        ] = None,
        next_token: Optional[
            "capo_network_security_manager.types.next_token.NextToken"
        ] = None,
    ) -> "Iterator[capo_network_security_manager.types.resource_association.ResourceAssociation]":
        _token = next_token
        while True:
            _response = self.list_resource_associations(
                resource_identifier,
                config_overrides=config_overrides,
                max_results=max_results,
                next_token=_token,
            )
            _page = _resolve_path(_response, ("resource_associations",))
            for _item in _page or []:
                yield _item
            _token = _resolve_path(_response, ("next_token",))
            if not _token:
                break

    def list_tags_for_resource(
        self,
        resource_arn: "capo_network_security_manager.types.arn.Arn",
        *,
        config_overrides: Optional[NetworkSecurityManagerClientConfig] = None,
    ) -> "capo_network_security_manager.types.list_tags_for_resource_output.ListTagsForResourceOutput":
        """<p>Lists the tags associated with the specified resource.</p>

        Args:
            resource_arn: <p>The ARN of the resource to list tags for. The ARN must not include a <code>:DRAFT</code> qualifier.</p>

        Raises:
            capo_network_security_manager.errors.access_denied_exception.AccessDeniedException: <p>You do not have sufficient permissions to perform this action.</p>
            capo_network_security_manager.errors.internal_server_exception.InternalServerException: <p>The request processing failed because of an internal error in the service. This is a retryable error.</p>
            capo_network_security_manager.errors.resource_not_found_exception.ResourceNotFoundException: <p>The specified resource was not found. Verify that the resource identifier is correct and that the resource exists, then try your request again.</p>
            capo_network_security_manager.errors.throttling_exception.ThrottlingException: <p>The request was denied because of request throttling. Reduce your request rate and try again.</p>
            capo_network_security_manager.errors.validation_exception.ValidationException: <p>The request failed validation. For details, see the <code>reason</code> and <code>fieldList</code> members of the response.</p>
            capo_network_security_manager.errors.UnknownServiceError: The service returned an error code this client does not model.

        Examples:
            List the tags on a resource
            Lists the tags associated with a Network Security Manager resource.

            >>> client.list_tags_for_resource(resource_arn='arn:aws:network-security-manager:us-east-1:123456789012:policy:xyz789')
        """

        def _handler(
            req: "OperationRequest[capo_network_security_manager.types.list_tags_for_resource_input.ListTagsForResourceInput]",
        ) -> OperationResponse[
            "capo_network_security_manager.types.list_tags_for_resource_output.ListTagsForResourceOutput"
        ]:
            import capo_network_security_manager._operations.piccolo_customer_api_service.list_tags_for_resource

            output, http_response = (
                capo_network_security_manager._operations.piccolo_customer_api_service.list_tags_for_resource.list_tags_for_resource(
                    req.options, req.input
                )
            )
            return OperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_network_security_manager.types.list_tags_for_resource_input.ListTagsForResourceInput = {
            "resource_arn": resource_arn
        }

        response = execute_pipeline(
            OperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        response.response.close()
        return response.output

    def put_admin_account(
        self,
        account_id: "capo_network_security_manager.types.account_id.AccountId",
        priority: "capo_network_security_manager.types.admin_priority.AdminPriority",
        *,
        config_overrides: Optional[NetworkSecurityManagerClientConfig] = None,
        admin_scope: Optional[
            "capo_network_security_manager.types.admin_scope_input.AdminScopeInput"
        ] = None,
    ) -> "capo_network_security_manager.types.put_admin_account_response.PutAdminAccountResponse":
        """<p>Sets the AWS account that serves as an AWS Network Security Manager administrator account, and optionally configures the scope of resources that the administrator can manage.</p> <p>You can't set an administrator account again immediately after you remove it, or while the service creates its service-linked role. Retry the request after a few minutes.</p>

        Args:
            account_id: <p>The AWS account ID to set as the AWS Network Security Manager administrator account.</p>
            priority: <p>The priority to assign to the administrator account.</p>
            admin_scope: <p>The scope of accounts, organizational units, and firewall types that the administrator can manage.</p>

        Raises:
            capo_network_security_manager.errors.access_denied_exception.AccessDeniedException: <p>You do not have sufficient permissions to perform this action.</p>
            capo_network_security_manager.errors.conflict_exception.ConflictException: <p>The request conflicts with the current state of the resource. For example, the resource was modified concurrently, or it is in a state that does not allow the requested operation.</p>
            capo_network_security_manager.errors.internal_server_exception.InternalServerException: <p>The request processing failed because of an internal error in the service. This is a retryable error.</p>
            capo_network_security_manager.errors.service_quota_exceeded_exception.ServiceQuotaExceededException: <p>The request would exceed a service quota.</p>
            capo_network_security_manager.errors.service_unavailable_exception.ServiceUnavailableException: <p>The service is temporarily unavailable. This is a retryable error.</p>
            capo_network_security_manager.errors.throttling_exception.ThrottlingException: <p>The request was denied because of request throttling. Reduce your request rate and try again.</p>
            capo_network_security_manager.errors.validation_exception.ValidationException: <p>The request failed validation. For details, see the <code>reason</code> and <code>fieldList</code> members of the response.</p>
            capo_network_security_manager.errors.UnknownServiceError: The service returned an error code this client does not model.

        Examples:
            Designate an administrator account
            Designates an account as a Network Security Manager administrator, scoped to a specific organizational unit and the WAF firewall type.

            >>> client.put_admin_account(account_id='234567890123', priority=2, admin_scope={'scopeFilter': {'includeOnly': {'organizationalUnits': ['ou-abcd-12345678']}}, 'firewallTypeScope': {'allFirewallTypesEnabled': False, 'firewallTypes': ['WAF']}})
        """

        def _handler(
            req: "OperationRequest[capo_network_security_manager.types.put_admin_account_request.PutAdminAccountRequest]",
        ) -> OperationResponse[
            "capo_network_security_manager.types.put_admin_account_response.PutAdminAccountResponse"
        ]:
            import capo_network_security_manager._operations.piccolo_customer_api_service.put_admin_account

            output, http_response = (
                capo_network_security_manager._operations.piccolo_customer_api_service.put_admin_account.put_admin_account(
                    req.options, req.input
                )
            )
            return OperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_network_security_manager.types.put_admin_account_request.PutAdminAccountRequest = {
            "account_id": account_id,
            "priority": priority,
        }
        if admin_scope is not None:
            input_["admin_scope"] = admin_scope

        response = execute_pipeline(
            OperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        response.response.close()
        return response.output

    def tag_resource(
        self,
        resource_arn: "capo_network_security_manager.types.arn.Arn",
        tags: "capo_network_security_manager.types.tag_map.TagMap",
        *,
        config_overrides: Optional[NetworkSecurityManagerClientConfig] = None,
    ) -> "capo_network_security_manager.types.tag_resource_output.TagResourceOutput":
        """<p>Adds or overwrites the specified tags on the given resource.</p>

        Args:
            resource_arn: <p>The ARN of the resource to tag. The ARN must not include a <code>:DRAFT</code> qualifier.</p>
            tags: <p>The tags to add to the resource.</p>

        Raises:
            capo_network_security_manager.errors.access_denied_exception.AccessDeniedException: <p>You do not have sufficient permissions to perform this action.</p>
            capo_network_security_manager.errors.internal_server_exception.InternalServerException: <p>The request processing failed because of an internal error in the service. This is a retryable error.</p>
            capo_network_security_manager.errors.resource_not_found_exception.ResourceNotFoundException: <p>The specified resource was not found. Verify that the resource identifier is correct and that the resource exists, then try your request again.</p>
            capo_network_security_manager.errors.tag_policy_violation_exception.TagPolicyViolationException: <p>The request violates a tag policy that is in effect for the account or organization.</p>
            capo_network_security_manager.errors.throttling_exception.ThrottlingException: <p>The request was denied because of request throttling. Reduce your request rate and try again.</p>
            capo_network_security_manager.errors.validation_exception.ValidationException: <p>The request failed validation. For details, see the <code>reason</code> and <code>fieldList</code> members of the response.</p>
            capo_network_security_manager.errors.UnknownServiceError: The service returned an error code this client does not model.

        Examples:
            Tag a resource
            Adds tags to a Network Security Manager resource.

            >>> client.tag_resource(resource_arn='arn:aws:network-security-manager:us-east-1:123456789012:policy:xyz789', tags={'Environment': 'Production', 'Team': 'NetworkSecurity'})
        """

        def _handler(
            req: "OperationRequest[capo_network_security_manager.types.tag_resource_input.TagResourceInput]",
        ) -> OperationResponse[
            "capo_network_security_manager.types.tag_resource_output.TagResourceOutput"
        ]:
            import capo_network_security_manager._operations.piccolo_customer_api_service.tag_resource

            output, http_response = (
                capo_network_security_manager._operations.piccolo_customer_api_service.tag_resource.tag_resource(
                    req.options, req.input
                )
            )
            return OperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_network_security_manager.types.tag_resource_input.TagResourceInput = {
            "resource_arn": resource_arn,
            "tags": tags,
        }

        response = execute_pipeline(
            OperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        response.response.close()
        return response.output

    def untag_resource(
        self,
        resource_arn: "capo_network_security_manager.types.arn.Arn",
        tag_keys: "capo_network_security_manager.types.tag_key_list.TagKeyList",
        *,
        config_overrides: Optional[NetworkSecurityManagerClientConfig] = None,
    ) -> (
        "capo_network_security_manager.types.untag_resource_output.UntagResourceOutput"
    ):
        """<p>Removes the specified tags from the given resource.</p>

        Args:
            resource_arn: <p>The ARN of the resource to remove tags from. The ARN must not include a <code>:DRAFT</code> qualifier.</p>
            tag_keys: <p>The keys of the tags to remove from the resource.</p>

        Raises:
            capo_network_security_manager.errors.access_denied_exception.AccessDeniedException: <p>You do not have sufficient permissions to perform this action.</p>
            capo_network_security_manager.errors.internal_server_exception.InternalServerException: <p>The request processing failed because of an internal error in the service. This is a retryable error.</p>
            capo_network_security_manager.errors.resource_not_found_exception.ResourceNotFoundException: <p>The specified resource was not found. Verify that the resource identifier is correct and that the resource exists, then try your request again.</p>
            capo_network_security_manager.errors.tag_policy_violation_exception.TagPolicyViolationException: <p>The request violates a tag policy that is in effect for the account or organization.</p>
            capo_network_security_manager.errors.throttling_exception.ThrottlingException: <p>The request was denied because of request throttling. Reduce your request rate and try again.</p>
            capo_network_security_manager.errors.validation_exception.ValidationException: <p>The request failed validation. For details, see the <code>reason</code> and <code>fieldList</code> members of the response.</p>
            capo_network_security_manager.errors.UnknownServiceError: The service returned an error code this client does not model.

        Examples:
            Remove tags from a resource
            Removes the specified tag keys from a Network Security Manager resource.

            >>> client.untag_resource(resource_arn='arn:aws:network-security-manager:us-east-1:123456789012:policy:xyz789', tag_keys=['Environment'])
        """

        def _handler(
            req: "OperationRequest[capo_network_security_manager.types.untag_resource_input.UntagResourceInput]",
        ) -> OperationResponse[
            "capo_network_security_manager.types.untag_resource_output.UntagResourceOutput"
        ]:
            import capo_network_security_manager._operations.piccolo_customer_api_service.untag_resource

            output, http_response = (
                capo_network_security_manager._operations.piccolo_customer_api_service.untag_resource.untag_resource(
                    req.options, req.input
                )
            )
            return OperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_network_security_manager.types.untag_resource_input.UntagResourceInput = {
            "resource_arn": resource_arn,
            "tag_keys": tag_keys,
        }

        response = execute_pipeline(
            OperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        response.response.close()
        return response.output

    def create_deployment(
        self,
        deployment_name: "capo_network_security_manager.types.deployment_name.DeploymentName",
        deployment_configuration: "capo_network_security_manager.types.deployment_configuration.DeploymentConfiguration",
        associated_policy_list: "capo_network_security_manager.types.policy_reference_list.PolicyReferenceList",
        associated_scope_list: "capo_network_security_manager.types.scope_reference_list.ScopeReferenceList",
        *,
        config_overrides: Optional[NetworkSecurityManagerClientConfig] = None,
        client_token: Optional[
            "capo_network_security_manager.types.idempotency_token.IdempotencyToken"
        ] = None,
        deployment_description: Optional[
            "capo_network_security_manager.types.description.Description"
        ] = None,
        is_published: Optional[
            "capo_network_security_manager.types.is_published.IsPublished"
        ] = None,
        tags: Optional["capo_network_security_manager.types.tag_map.TagMap"] = None,
    ) -> "capo_network_security_manager.types.create_deployment_output.CreateDeploymentOutput":
        """<p>Creates a deployment. A deployment applies one or more policies to the accounts and resources selected by a scope. Use <code>isPublished</code> to create the deployment in published (<code>ACTIVE</code>) or draft (<code>DRAFT</code>) state. The response includes coverage information and any warnings about the deployment.</p>

        Args:
            client_token: <p>A unique, case-sensitive token that you provide to ensure that the operation completes no more than one time. If you retry a request with the same client token and the same parameters, the service returns the result of the original successful request.</p>
            deployment_name: <p>The name of the deployment.</p>
            deployment_description: <p>A description of the deployment.</p>
            deployment_configuration: <p>The configuration settings for the deployment.</p>
            associated_policy_list: <p>The policies associated with the deployment.</p>
            associated_scope_list: <p>The scope associated with the deployment. A deployment has exactly one scope.</p>
            is_published: <p>Specifies whether to publish the resource. When <code>true</code>, the resource is saved in published (<code>ACTIVE</code>) state. When <code>false</code>, it is saved as a draft (<code>DRAFT</code>). Default: <code>true</code>.</p>
            tags: <p>The tags to add to the resource when it is created.</p>

        Raises:
            capo_network_security_manager.errors.access_denied_exception.AccessDeniedException: <p>You do not have sufficient permissions to perform this action.</p>
            capo_network_security_manager.errors.conflict_exception.ConflictException: <p>The request conflicts with the current state of the resource. For example, the resource was modified concurrently, or it is in a state that does not allow the requested operation.</p>
            capo_network_security_manager.errors.internal_server_exception.InternalServerException: <p>The request processing failed because of an internal error in the service. This is a retryable error.</p>
            capo_network_security_manager.errors.service_quota_exceeded_exception.ServiceQuotaExceededException: <p>The request would exceed a service quota.</p>
            capo_network_security_manager.errors.service_unavailable_exception.ServiceUnavailableException: <p>The service is temporarily unavailable. This is a retryable error.</p>
            capo_network_security_manager.errors.tag_policy_violation_exception.TagPolicyViolationException: <p>The request violates a tag policy that is in effect for the account or organization.</p>
            capo_network_security_manager.errors.throttling_exception.ThrottlingException: <p>The request was denied because of request throttling. Reduce your request rate and try again.</p>
            capo_network_security_manager.errors.validation_exception.ValidationException: <p>The request failed validation. For details, see the <code>reason</code> and <code>fieldList</code> members of the response.</p>
            capo_network_security_manager.errors.UnknownServiceError: The service returned an error code this client does not model.

        Examples:
            Create a deployment
            Creates a new deployment in draft state.

            >>> client.create_deployment(client_token='550e8400-e29b-41d4-a716-446655440003', deployment_name='prod-us-east-1-deployment', deployment_description='Production deployment for US East 1 region', associated_policy_list=[{'policyIdentifier': 'arn:aws:network-security-manager:us-east-1:123456789012:policy:xyz789'}], associated_scope_list=[{'scopeIdentifier': 'arn:aws:network-security-manager:us-east-1:123456789012:scope:abc123'}], deployment_configuration={'enableCrossAccountVisibility': False}, is_published=False)
        """

        def _handler(
            req: "OperationRequest[capo_network_security_manager.types.create_deployment_input.CreateDeploymentInput]",
        ) -> OperationResponse[
            "capo_network_security_manager.types.create_deployment_output.CreateDeploymentOutput"
        ]:
            import capo_network_security_manager._operations.piccolo_customer_api_service.create_deployment

            output, http_response = (
                capo_network_security_manager._operations.piccolo_customer_api_service.create_deployment.create_deployment(
                    req.options, req.input
                )
            )
            return OperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_network_security_manager.types.create_deployment_input.CreateDeploymentInput = {
            "deployment_name": deployment_name,
            "deployment_configuration": deployment_configuration,
            "associated_policy_list": associated_policy_list,
            "associated_scope_list": associated_scope_list,
        }
        if client_token is None:
            client_token = str(uuid.uuid4())
        input_["client_token"] = client_token
        if deployment_description is not None:
            input_["deployment_description"] = deployment_description
        if is_published is not None:
            input_["is_published"] = is_published
        if tags is not None:
            input_["tags"] = tags

        response = execute_pipeline(
            OperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        response.response.close()
        return response.output

    def get_deployment(
        self,
        deployment_identifier: "capo_network_security_manager.types.deployment_identifier.DeploymentIdentifier",
        *,
        config_overrides: Optional[NetworkSecurityManagerClientConfig] = None,
    ) -> (
        "capo_network_security_manager.types.get_deployment_output.GetDeploymentOutput"
    ):
        """<p>Retrieves the details of the specified deployment, including coverage information and any warnings.</p>

        Args:
            deployment_identifier: <p>The identifier of the deployment. This is the deployment's Amazon Resource Name (ARN).</p>

        Raises:
            capo_network_security_manager.errors.access_denied_exception.AccessDeniedException: <p>You do not have sufficient permissions to perform this action.</p>
            capo_network_security_manager.errors.internal_server_exception.InternalServerException: <p>The request processing failed because of an internal error in the service. This is a retryable error.</p>
            capo_network_security_manager.errors.resource_not_found_exception.ResourceNotFoundException: <p>The specified resource was not found. Verify that the resource identifier is correct and that the resource exists, then try your request again.</p>
            capo_network_security_manager.errors.throttling_exception.ThrottlingException: <p>The request was denied because of request throttling. Reduce your request rate and try again.</p>
            capo_network_security_manager.errors.validation_exception.ValidationException: <p>The request failed validation. For details, see the <code>reason</code> and <code>fieldList</code> members of the response.</p>
            capo_network_security_manager.errors.UnknownServiceError: The service returned an error code this client does not model.

        Examples:
            Get a deployment
            Retrieves the current published version of a deployment by its base ARN, including per-firewall-type coverage showing which in-scope resource types each policy protects.

            >>> client.get_deployment(deployment_identifier='arn:aws:network-security-manager:us-east-1:123456789012:deployment:def456')
        """

        def _handler(
            req: "OperationRequest[capo_network_security_manager.types.get_deployment_input.GetDeploymentInput]",
        ) -> OperationResponse[
            "capo_network_security_manager.types.get_deployment_output.GetDeploymentOutput"
        ]:
            import capo_network_security_manager._operations.piccolo_customer_api_service.get_deployment

            output, http_response = (
                capo_network_security_manager._operations.piccolo_customer_api_service.get_deployment.get_deployment(
                    req.options, req.input
                )
            )
            return OperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_network_security_manager.types.get_deployment_input.GetDeploymentInput = {
            "deployment_identifier": deployment_identifier
        }

        response = execute_pipeline(
            OperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        response.response.close()
        return response.output

    def update_deployment(
        self,
        deployment_identifier: "capo_network_security_manager.types.deployment_identifier.DeploymentIdentifier",
        update_token: "capo_network_security_manager.types.update_token.UpdateToken",
        is_published: "capo_network_security_manager.types.is_published.IsPublished",
        *,
        config_overrides: Optional[NetworkSecurityManagerClientConfig] = None,
        deployment_description: Optional[
            "capo_network_security_manager.types.description.Description"
        ] = None,
        deployment_configuration: Optional[
            "capo_network_security_manager.types.deployment_configuration.DeploymentConfiguration"
        ] = None,
        associated_policy_list: Optional[
            "capo_network_security_manager.types.policy_reference_list.PolicyReferenceList"
        ] = None,
        associated_scope_list: Optional[
            "capo_network_security_manager.types.scope_reference_list.ScopeReferenceList"
        ] = None,
        client_token: Optional[
            "capo_network_security_manager.types.idempotency_token.IdempotencyToken"
        ] = None,
    ) -> "capo_network_security_manager.types.update_deployment_output.UpdateDeploymentOutput":
        """<p>Updates the specified deployment. To prevent conflicting concurrent updates, provide the current <code>updateToken</code>. Use <code>isPublished</code> to publish the update or keep the deployment as a draft.</p>

        Args:
            deployment_identifier: <p>The identifier of the deployment. This is the deployment's Amazon Resource Name (ARN).</p>
            update_token: <p>A token used for optimistic concurrency control. Each read and write returns an <code>updateToken</code>. Provide the most recent value on your next update to detect and prevent conflicting concurrent modifications.</p>
            deployment_description: <p>A description of the deployment.</p>
            deployment_configuration: <p>The configuration settings for the deployment.</p>
            associated_policy_list: <p>The policies associated with the deployment.</p>
            associated_scope_list: <p>The scope associated with the deployment. A deployment has exactly one scope.</p>
            is_published: <p>Specifies whether to publish the resource. When <code>true</code>, the resource is saved in published (<code>ACTIVE</code>) state. When <code>false</code>, it is saved as a draft (<code>DRAFT</code>).</p>
            client_token: <p>A unique, case-sensitive token that you provide to ensure that the operation completes no more than one time. If you retry a request with the same client token and the same parameters, the service returns the result of the original successful request.</p>

        Raises:
            capo_network_security_manager.errors.access_denied_exception.AccessDeniedException: <p>You do not have sufficient permissions to perform this action.</p>
            capo_network_security_manager.errors.conflict_exception.ConflictException: <p>The request conflicts with the current state of the resource. For example, the resource was modified concurrently, or it is in a state that does not allow the requested operation.</p>
            capo_network_security_manager.errors.internal_server_exception.InternalServerException: <p>The request processing failed because of an internal error in the service. This is a retryable error.</p>
            capo_network_security_manager.errors.resource_not_found_exception.ResourceNotFoundException: <p>The specified resource was not found. Verify that the resource identifier is correct and that the resource exists, then try your request again.</p>
            capo_network_security_manager.errors.service_quota_exceeded_exception.ServiceQuotaExceededException: <p>The request would exceed a service quota.</p>
            capo_network_security_manager.errors.throttling_exception.ThrottlingException: <p>The request was denied because of request throttling. Reduce your request rate and try again.</p>
            capo_network_security_manager.errors.validation_exception.ValidationException: <p>The request failed validation. For details, see the <code>reason</code> and <code>fieldList</code> members of the response.</p>
            capo_network_security_manager.errors.UnknownServiceError: The service returned an error code this client does not model.

        Examples:
            Update a deployment and publish it
            Updates the deployment's associations and publishes the change. The response includes deploymentCoverage showing which resource types the associated policies can protect. The updateToken from the most recent read is required for optimistic locking.

            >>> client.update_deployment(deployment_identifier='arn:aws:network-security-manager:us-east-1:123456789012:deployment:def456', update_token='f4a5b6c7-7d8e-4f9a-8b1c-1d2e3f4a5b6c', deployment_description='Production deployment for US East 1 region - updated', associated_policy_list=[{'policyIdentifier': 'arn:aws:network-security-manager:us-east-1:123456789012:policy:xyz789'}], associated_scope_list=[{'scopeIdentifier': 'arn:aws:network-security-manager:us-east-1:123456789012:scope:abc123'}], deployment_configuration={'enableCrossAccountVisibility': True}, is_published=True)
        """

        def _handler(
            req: "OperationRequest[capo_network_security_manager.types.update_deployment_input.UpdateDeploymentInput]",
        ) -> OperationResponse[
            "capo_network_security_manager.types.update_deployment_output.UpdateDeploymentOutput"
        ]:
            import capo_network_security_manager._operations.piccolo_customer_api_service.update_deployment

            output, http_response = (
                capo_network_security_manager._operations.piccolo_customer_api_service.update_deployment.update_deployment(
                    req.options, req.input
                )
            )
            return OperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_network_security_manager.types.update_deployment_input.UpdateDeploymentInput = {
            "deployment_identifier": deployment_identifier,
            "update_token": update_token,
            "is_published": is_published,
        }
        if deployment_description is not None:
            input_["deployment_description"] = deployment_description
        if deployment_configuration is not None:
            input_["deployment_configuration"] = deployment_configuration
        if associated_policy_list is not None:
            input_["associated_policy_list"] = associated_policy_list
        if associated_scope_list is not None:
            input_["associated_scope_list"] = associated_scope_list
        if client_token is None:
            client_token = str(uuid.uuid4())
        input_["client_token"] = client_token

        response = execute_pipeline(
            OperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        response.response.close()
        return response.output

    def delete_deployment(
        self,
        deployment_identifier: "capo_network_security_manager.types.deployment_identifier.DeploymentIdentifier",
        *,
        config_overrides: Optional[NetworkSecurityManagerClientConfig] = None,
    ) -> None:
        """<p>Deletes the specified deployment.</p>

        Args:
            deployment_identifier: <p>The identifier of the deployment. This is the deployment's Amazon Resource Name (ARN).</p>

        Raises:
            capo_network_security_manager.errors.access_denied_exception.AccessDeniedException: <p>You do not have sufficient permissions to perform this action.</p>
            capo_network_security_manager.errors.conflict_exception.ConflictException: <p>The request conflicts with the current state of the resource. For example, the resource was modified concurrently, or it is in a state that does not allow the requested operation.</p>
            capo_network_security_manager.errors.internal_server_exception.InternalServerException: <p>The request processing failed because of an internal error in the service. This is a retryable error.</p>
            capo_network_security_manager.errors.throttling_exception.ThrottlingException: <p>The request was denied because of request throttling. Reduce your request rate and try again.</p>
            capo_network_security_manager.errors.validation_exception.ValidationException: <p>The request failed validation. For details, see the <code>reason</code> and <code>fieldList</code> members of the response.</p>
            capo_network_security_manager.errors.UnknownServiceError: The service returned an error code this client does not model.

        Examples:
            Delete a deployment
            Deletes a deployment by its ARN. Deleting an active deployment stops enforcement and triggers cleanup of managed firewall resources.

            >>> client.delete_deployment(deployment_identifier='arn:aws:network-security-manager:us-east-1:123456789012:deployment:def456')
        """

        def _handler(
            req: "OperationRequest[capo_network_security_manager.types.delete_deployment_input.DeleteDeploymentInput]",
        ) -> OperationResponse[None]:
            import capo_network_security_manager._operations.piccolo_customer_api_service.delete_deployment

            output, http_response = (
                capo_network_security_manager._operations.piccolo_customer_api_service.delete_deployment.delete_deployment(
                    req.options, req.input
                )
            )
            return OperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_network_security_manager.types.delete_deployment_input.DeleteDeploymentInput = {
            "deployment_identifier": deployment_identifier
        }

        response = execute_pipeline(
            OperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        response.response.close()
        return response.output

    def list_deployments(
        self,
        *,
        config_overrides: Optional[NetworkSecurityManagerClientConfig] = None,
        max_results: Optional[
            "capo_network_security_manager.types.max_results.MaxResults"
        ] = None,
        next_token: Optional[
            "capo_network_security_manager.types.next_token.NextToken"
        ] = None,
        status: Optional[
            "capo_network_security_manager.types.entity_status_filter.EntityStatusFilter"
        ] = None,
    ) -> "capo_network_security_manager.types.list_deployments_output.ListDeploymentsOutput":
        """<p>Lists the deployments in the account. You can filter the results by status and page through them using <code>maxResults</code> and <code>nextToken</code>.</p>

        Args:
            max_results: <p>The maximum number of results to return in a single call. Valid range: 1-100. To retrieve the remaining results, use the returned <code>nextToken</code> value in a subsequent call.</p>
            next_token: <p>The token for the next page of results. To retrieve the next page, call the operation again and provide this value. When there are no more results, this value is null.</p>
            status: <p>Filters the results by status: <code>ACTIVE</code>, <code>DRAFT</code>, or <code>DISABLED</code>.</p>

        Raises:
            capo_network_security_manager.errors.access_denied_exception.AccessDeniedException: <p>You do not have sufficient permissions to perform this action.</p>
            capo_network_security_manager.errors.internal_server_exception.InternalServerException: <p>The request processing failed because of an internal error in the service. This is a retryable error.</p>
            capo_network_security_manager.errors.throttling_exception.ThrottlingException: <p>The request was denied because of request throttling. Reduce your request rate and try again.</p>
            capo_network_security_manager.errors.validation_exception.ValidationException: <p>The request failed validation. For details, see the <code>reason</code> and <code>fieldList</code> members of the response.</p>
            capo_network_security_manager.errors.UnknownServiceError: The service returned an error code this client does not model.

        Examples:
            List deployments
            Lists the published deployments in the account, one page at a time.

            >>> client.list_deployments(max_results=10, status='ACTIVE')
        """

        def _handler(
            req: "OperationRequest[capo_network_security_manager.types.list_deployments_input.ListDeploymentsInput]",
        ) -> OperationResponse[
            "capo_network_security_manager.types.list_deployments_output.ListDeploymentsOutput"
        ]:
            import capo_network_security_manager._operations.piccolo_customer_api_service.list_deployments

            output, http_response = (
                capo_network_security_manager._operations.piccolo_customer_api_service.list_deployments.list_deployments(
                    req.options, req.input
                )
            )
            return OperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_network_security_manager.types.list_deployments_input.ListDeploymentsInput = {}
        if max_results is not None:
            input_["max_results"] = max_results
        if next_token is not None:
            input_["next_token"] = next_token
        if status is not None:
            input_["status"] = status

        response = execute_pipeline(
            OperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        response.response.close()
        return response.output

    def iter_list_deployments(
        self,
        *,
        config_overrides: Optional[NetworkSecurityManagerClientConfig] = None,
        max_results: Optional[
            "capo_network_security_manager.types.max_results.MaxResults"
        ] = None,
        next_token: Optional[
            "capo_network_security_manager.types.next_token.NextToken"
        ] = None,
        status: Optional[
            "capo_network_security_manager.types.entity_status_filter.EntityStatusFilter"
        ] = None,
    ) -> "Iterator[capo_network_security_manager.types.deployment_summary.DeploymentSummary]":
        _token = next_token
        while True:
            _response = self.list_deployments(
                config_overrides=config_overrides,
                max_results=max_results,
                next_token=_token,
                status=status,
            )
            _page = _resolve_path(_response, ("deployments",))
            for _item in _page or []:
                yield _item
            _token = _resolve_path(_response, ("next_token",))
            if not _token:
                break

    def create_deployment_snapshot(
        self,
        deployment_identifier: "capo_network_security_manager.types.deployment_identifier.DeploymentIdentifier",
        *,
        config_overrides: Optional[NetworkSecurityManagerClientConfig] = None,
        client_token: Optional[
            "capo_network_security_manager.types.idempotency_token.IdempotencyToken"
        ] = None,
        tags: Optional["capo_network_security_manager.types.tag_map.TagMap"] = None,
    ) -> "capo_network_security_manager.types.create_deployment_snapshot_output.CreateDeploymentSnapshotOutput":
        """<p>Creates a snapshot of the current published version of the specified deployment.</p>

        Args:
            deployment_identifier: <p>The identifier of the deployment. This is the deployment's Amazon Resource Name (ARN).</p>
            client_token: <p>A unique, case-sensitive token that you provide to ensure that the operation completes no more than one time. If you retry a request with the same client token and the same parameters, the service returns the result of the original successful request.</p>
            tags: <p>The tags to add to the snapshot when it is created.</p>

        Raises:
            capo_network_security_manager.errors.access_denied_exception.AccessDeniedException: <p>You do not have sufficient permissions to perform this action.</p>
            capo_network_security_manager.errors.conflict_exception.ConflictException: <p>The request conflicts with the current state of the resource. For example, the resource was modified concurrently, or it is in a state that does not allow the requested operation.</p>
            capo_network_security_manager.errors.internal_server_exception.InternalServerException: <p>The request processing failed because of an internal error in the service. This is a retryable error.</p>
            capo_network_security_manager.errors.resource_not_found_exception.ResourceNotFoundException: <p>The specified resource was not found. Verify that the resource identifier is correct and that the resource exists, then try your request again.</p>
            capo_network_security_manager.errors.service_quota_exceeded_exception.ServiceQuotaExceededException: <p>The request would exceed a service quota.</p>
            capo_network_security_manager.errors.throttling_exception.ThrottlingException: <p>The request was denied because of request throttling. Reduce your request rate and try again.</p>
            capo_network_security_manager.errors.validation_exception.ValidationException: <p>The request failed validation. For details, see the <code>reason</code> and <code>fieldList</code> members of the response.</p>
            capo_network_security_manager.errors.UnknownServiceError: The service returned an error code this client does not model.

        Examples:
            Create a deployment snapshot
            Creates an immutable snapshot of the current published version of a deployment. The snapshot is addressable by a version-qualified ARN.

            >>> client.create_deployment_snapshot(deployment_identifier='arn:aws:network-security-manager:us-east-1:123456789012:deployment:def456', client_token='550e8400-e29b-41d4-a716-446655440014')
        """

        def _handler(
            req: "OperationRequest[capo_network_security_manager.types.create_deployment_snapshot_input.CreateDeploymentSnapshotInput]",
        ) -> OperationResponse[
            "capo_network_security_manager.types.create_deployment_snapshot_output.CreateDeploymentSnapshotOutput"
        ]:
            import capo_network_security_manager._operations.piccolo_customer_api_service.create_deployment_snapshot

            output, http_response = (
                capo_network_security_manager._operations.piccolo_customer_api_service.create_deployment_snapshot.create_deployment_snapshot(
                    req.options, req.input
                )
            )
            return OperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_network_security_manager.types.create_deployment_snapshot_input.CreateDeploymentSnapshotInput = {
            "deployment_identifier": deployment_identifier
        }
        if client_token is None:
            client_token = str(uuid.uuid4())
        input_["client_token"] = client_token
        if tags is not None:
            input_["tags"] = tags

        response = execute_pipeline(
            OperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        response.response.close()
        return response.output

    def list_deployment_snapshots(
        self,
        deployment_identifier: "capo_network_security_manager.types.deployment_identifier.DeploymentIdentifier",
        *,
        config_overrides: Optional[NetworkSecurityManagerClientConfig] = None,
        max_results: Optional[
            "capo_network_security_manager.types.max_results.MaxResults"
        ] = None,
        next_token: Optional[
            "capo_network_security_manager.types.next_token.NextToken"
        ] = None,
    ) -> "capo_network_security_manager.types.list_deployment_snapshots_output.ListDeploymentSnapshotsOutput":
        """<p>Lists the snapshots of the specified deployment.</p>

        Args:
            deployment_identifier: <p>The identifier of the deployment. This is the deployment's Amazon Resource Name (ARN).</p>
            max_results: <p>The maximum number of results to return in a single call. Valid range: 1-100. To retrieve the remaining results, use the returned <code>nextToken</code> value in a subsequent call.</p>
            next_token: <p>The token for the next page of results. To retrieve the next page, call the operation again and provide this value. When there are no more results, this value is null.</p>

        Raises:
            capo_network_security_manager.errors.access_denied_exception.AccessDeniedException: <p>You do not have sufficient permissions to perform this action.</p>
            capo_network_security_manager.errors.internal_server_exception.InternalServerException: <p>The request processing failed because of an internal error in the service. This is a retryable error.</p>
            capo_network_security_manager.errors.resource_not_found_exception.ResourceNotFoundException: <p>The specified resource was not found. Verify that the resource identifier is correct and that the resource exists, then try your request again.</p>
            capo_network_security_manager.errors.throttling_exception.ThrottlingException: <p>The request was denied because of request throttling. Reduce your request rate and try again.</p>
            capo_network_security_manager.errors.validation_exception.ValidationException: <p>The request failed validation. For details, see the <code>reason</code> and <code>fieldList</code> members of the response.</p>
            capo_network_security_manager.errors.UnknownServiceError: The service returned an error code this client does not model.

        Examples:
            List the snapshots of a deployment
            Lists the immutable snapshots that have been created for a deployment.

            >>> client.list_deployment_snapshots(deployment_identifier='arn:aws:network-security-manager:us-east-1:123456789012:deployment:def456', max_results=10)
        """

        def _handler(
            req: "OperationRequest[capo_network_security_manager.types.list_deployment_snapshots_input.ListDeploymentSnapshotsInput]",
        ) -> OperationResponse[
            "capo_network_security_manager.types.list_deployment_snapshots_output.ListDeploymentSnapshotsOutput"
        ]:
            import capo_network_security_manager._operations.piccolo_customer_api_service.list_deployment_snapshots

            output, http_response = (
                capo_network_security_manager._operations.piccolo_customer_api_service.list_deployment_snapshots.list_deployment_snapshots(
                    req.options, req.input
                )
            )
            return OperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_network_security_manager.types.list_deployment_snapshots_input.ListDeploymentSnapshotsInput = {
            "deployment_identifier": deployment_identifier
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

    def iter_list_deployment_snapshots(
        self,
        deployment_identifier: "capo_network_security_manager.types.deployment_identifier.DeploymentIdentifier",
        *,
        config_overrides: Optional[NetworkSecurityManagerClientConfig] = None,
        max_results: Optional[
            "capo_network_security_manager.types.max_results.MaxResults"
        ] = None,
        next_token: Optional[
            "capo_network_security_manager.types.next_token.NextToken"
        ] = None,
    ) -> "Iterator[capo_network_security_manager.types.deployment_summary.DeploymentSummary]":
        _token = next_token
        while True:
            _response = self.list_deployment_snapshots(
                deployment_identifier,
                config_overrides=config_overrides,
                max_results=max_results,
                next_token=_token,
            )
            _page = _resolve_path(_response, ("snapshots",))
            for _item in _page or []:
                yield _item
            _token = _resolve_path(_response, ("next_token",))
            if not _token:
                break

    def list_resource_synchronization_statuses(
        self,
        deployment_identifier: "capo_network_security_manager.types.deployment_identifier.DeploymentIdentifier",
        *,
        config_overrides: Optional[NetworkSecurityManagerClientConfig] = None,
        synchronization_status: Optional[
            "capo_network_security_manager.types.synchronization_status.SynchronizationStatus"
        ] = None,
        max_results: Optional[
            "capo_network_security_manager.types.max_results.MaxResults"
        ] = None,
        next_token: Optional[
            "capo_network_security_manager.types.next_token.NextToken"
        ] = None,
    ) -> "capo_network_security_manager.types.list_resource_synchronization_statuses_output.ListResourceSynchronizationStatusesOutput":
        """<p>Lists the synchronization statuses of the resources covered by the specified deployment. You can filter the results by synchronization status and page through them.</p>

        Args:
            deployment_identifier: <p>The identifier of the deployment to list synchronization statuses for. This is the deployment's Amazon Resource Name (ARN).</p>
            synchronization_status: <p>Filters the results by synchronization status, such as <code>IN_SYNC</code> or <code>OUT_OF_SYNC</code>.</p>
            max_results: <p>The maximum number of results to return in a single call. Valid range: 1-100. To retrieve the remaining results, use the returned <code>nextToken</code> value in a subsequent call.</p>
            next_token: <p>The token for the next page of results. To retrieve the next page, call the operation again and provide this value. When there are no more results, this value is null.</p>

        Raises:
            capo_network_security_manager.errors.access_denied_exception.AccessDeniedException: <p>You do not have sufficient permissions to perform this action.</p>
            capo_network_security_manager.errors.internal_server_exception.InternalServerException: <p>The request processing failed because of an internal error in the service. This is a retryable error.</p>
            capo_network_security_manager.errors.resource_not_found_exception.ResourceNotFoundException: <p>The specified resource was not found. Verify that the resource identifier is correct and that the resource exists, then try your request again.</p>
            capo_network_security_manager.errors.throttling_exception.ThrottlingException: <p>The request was denied because of request throttling. Reduce your request rate and try again.</p>
            capo_network_security_manager.errors.validation_exception.ValidationException: <p>The request failed validation. For details, see the <code>reason</code> and <code>fieldList</code> members of the response.</p>
            capo_network_security_manager.errors.UnknownServiceError: The service returned an error code this client does not model.

        Examples:
            List out-of-sync resources for a deployment
            Lists the resources tracked by a deployment that are out of sync, including the structured reason. Here a CloudFront distribution has no web ACL where the policy requires one.

            >>> client.list_resource_synchronization_statuses(deployment_identifier='arn:aws:network-security-manager:us-east-1:123456789012:deployment:def456', synchronization_status='OUT_OF_SYNC', max_results=10)
        """

        def _handler(
            req: "OperationRequest[capo_network_security_manager.types.list_resource_synchronization_statuses_input.ListResourceSynchronizationStatusesInput]",
        ) -> OperationResponse[
            "capo_network_security_manager.types.list_resource_synchronization_statuses_output.ListResourceSynchronizationStatusesOutput"
        ]:
            import capo_network_security_manager._operations.piccolo_customer_api_service.list_resource_synchronization_statuses

            output, http_response = (
                capo_network_security_manager._operations.piccolo_customer_api_service.list_resource_synchronization_statuses.list_resource_synchronization_statuses(
                    req.options, req.input
                )
            )
            return OperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_network_security_manager.types.list_resource_synchronization_statuses_input.ListResourceSynchronizationStatusesInput = {
            "deployment_identifier": deployment_identifier
        }
        if synchronization_status is not None:
            input_["synchronization_status"] = synchronization_status
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

    def iter_list_resource_synchronization_statuses(
        self,
        deployment_identifier: "capo_network_security_manager.types.deployment_identifier.DeploymentIdentifier",
        *,
        config_overrides: Optional[NetworkSecurityManagerClientConfig] = None,
        synchronization_status: Optional[
            "capo_network_security_manager.types.synchronization_status.SynchronizationStatus"
        ] = None,
        max_results: Optional[
            "capo_network_security_manager.types.max_results.MaxResults"
        ] = None,
        next_token: Optional[
            "capo_network_security_manager.types.next_token.NextToken"
        ] = None,
    ) -> "Iterator[capo_network_security_manager.types.resource_synchronization_status_summary.ResourceSynchronizationStatusSummary]":
        _token = next_token
        while True:
            _response = self.list_resource_synchronization_statuses(
                deployment_identifier,
                config_overrides=config_overrides,
                synchronization_status=synchronization_status,
                max_results=max_results,
                next_token=_token,
            )
            _page = _resolve_path(_response, ("resource_synchronization_statuses",))
            for _item in _page or []:
                yield _item
            _token = _resolve_path(_response, ("next_token",))
            if not _token:
                break

    def create_policy(
        self,
        policy_name: "capo_network_security_manager.types.policy_name.PolicyName",
        priority: "capo_network_security_manager.types.priority.Priority",
        firewall_type: "capo_network_security_manager.types.policy_firewall_type.PolicyFirewallType",
        policy_configuration: "capo_network_security_manager.types.policy_configuration.PolicyConfiguration",
        *,
        config_overrides: Optional[NetworkSecurityManagerClientConfig] = None,
        client_token: Optional[
            "capo_network_security_manager.types.idempotency_token.IdempotencyToken"
        ] = None,
        policy_description: Optional[
            "capo_network_security_manager.types.description.Description"
        ] = None,
        associated_template_and_rule_list: Optional[
            "capo_network_security_manager.types.template_and_rule_reference_list.TemplateAndRuleReferenceList"
        ] = None,
        is_published: Optional[
            "capo_network_security_manager.types.is_published.IsPublished"
        ] = None,
        tags: Optional["capo_network_security_manager.types.tag_map.TagMap"] = None,
    ) -> "capo_network_security_manager.types.create_policy_output.CreatePolicyOutput":
        """<p>Creates a policy. A policy combines templates and rules with enforcement settings for a firewall type, such as AWS WAF or AWS Shield Advanced. Use <code>isPublished</code> to create the policy in published (<code>ACTIVE</code>) or draft (<code>DRAFT</code>) state.</p>

        Args:
            client_token: <p>A unique, case-sensitive token that you provide to ensure that the operation completes no more than one time. If you retry a request with the same client token and the same parameters, the service returns the result of the original successful request.</p>
            policy_name: <p>The name of the policy.</p>
            policy_description: <p>A description of the policy.</p>
            priority: <p>The priority of the resource. A lower number indicates a higher priority.</p>
            associated_template_and_rule_list: <p>The templates and rules to associate with the policy. For AWS WAF policies, specify 1 to 100 templates or rules, of which at most 2 can be templates. For AWS Shield Advanced policies, this list must be empty.</p>
            firewall_type: <p>The firewall type associated with the resource.</p>
            policy_configuration: <p>The configuration settings that control the policy's behavior, including remediation and firewall-type-specific settings.</p>
            is_published: <p>Specifies whether to publish the resource. When <code>true</code>, the resource is saved in published (<code>ACTIVE</code>) state. When <code>false</code>, it is saved as a draft (<code>DRAFT</code>). Default: <code>true</code>.</p>
            tags: <p>The tags to add to the resource when it is created.</p>

        Raises:
            capo_network_security_manager.errors.access_denied_exception.AccessDeniedException: <p>You do not have sufficient permissions to perform this action.</p>
            capo_network_security_manager.errors.conflict_exception.ConflictException: <p>The request conflicts with the current state of the resource. For example, the resource was modified concurrently, or it is in a state that does not allow the requested operation.</p>
            capo_network_security_manager.errors.internal_server_exception.InternalServerException: <p>The request processing failed because of an internal error in the service. This is a retryable error.</p>
            capo_network_security_manager.errors.service_quota_exceeded_exception.ServiceQuotaExceededException: <p>The request would exceed a service quota.</p>
            capo_network_security_manager.errors.service_unavailable_exception.ServiceUnavailableException: <p>The service is temporarily unavailable. This is a retryable error.</p>
            capo_network_security_manager.errors.tag_policy_violation_exception.TagPolicyViolationException: <p>The request violates a tag policy that is in effect for the account or organization.</p>
            capo_network_security_manager.errors.throttling_exception.ThrottlingException: <p>The request was denied because of request throttling. Reduce your request rate and try again.</p>
            capo_network_security_manager.errors.validation_exception.ValidationException: <p>The request failed validation. For details, see the <code>reason</code> and <code>fieldList</code> members of the response.</p>
            capo_network_security_manager.errors.UnknownServiceError: The service returned an error code this client does not model.

        Examples:
            Create a WAF policy
            Creates a new WAF policy in draft state with a template association.

            >>> client.create_policy(client_token='550e8400-e29b-41d4-a716-446655440002', policy_name='web-app-waf-policy', policy_description='WAF policy for web application protection', firewall_type='WAF', priority=1, associated_template_and_rule_list=[{'templateIdentifier': 'arn:aws:network-security-manager:us-east-1:123456789012:template:xyz789'}], policy_configuration={'remediationEnabled': False, 'resourcesCleanUp': False, 'wafConfig': {'existingCustomerWebACLResolution': 'NO_REMEDIATION', 'conflictResolution': 'MERGE_WHERE_APPLICABLE'}}, is_published=False)
        """

        def _handler(
            req: "OperationRequest[capo_network_security_manager.types.create_policy_input.CreatePolicyInput]",
        ) -> OperationResponse[
            "capo_network_security_manager.types.create_policy_output.CreatePolicyOutput"
        ]:
            import capo_network_security_manager._operations.piccolo_customer_api_service.create_policy

            output, http_response = (
                capo_network_security_manager._operations.piccolo_customer_api_service.create_policy.create_policy(
                    req.options, req.input
                )
            )
            return OperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_network_security_manager.types.create_policy_input.CreatePolicyInput = {
            "policy_name": policy_name,
            "priority": priority,
            "firewall_type": firewall_type,
            "policy_configuration": policy_configuration,
        }
        if client_token is None:
            client_token = str(uuid.uuid4())
        input_["client_token"] = client_token
        if policy_description is not None:
            input_["policy_description"] = policy_description
        if associated_template_and_rule_list is not None:
            input_["associated_template_and_rule_list"] = (
                associated_template_and_rule_list
            )
        if is_published is not None:
            input_["is_published"] = is_published
        if tags is not None:
            input_["tags"] = tags

        response = execute_pipeline(
            OperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        response.response.close()
        return response.output

    def get_policy(
        self,
        policy_identifier: "capo_network_security_manager.types.policy_identifier.PolicyIdentifier",
        *,
        config_overrides: Optional[NetworkSecurityManagerClientConfig] = None,
    ) -> "capo_network_security_manager.types.get_policy_output.GetPolicyOutput":
        """<p>Retrieves the details of the specified policy.</p>

        Args:
            policy_identifier: <p>The identifier of the policy. This is the policy's Amazon Resource Name (ARN).</p>

        Raises:
            capo_network_security_manager.errors.access_denied_exception.AccessDeniedException: <p>You do not have sufficient permissions to perform this action.</p>
            capo_network_security_manager.errors.internal_server_exception.InternalServerException: <p>The request processing failed because of an internal error in the service. This is a retryable error.</p>
            capo_network_security_manager.errors.resource_not_found_exception.ResourceNotFoundException: <p>The specified resource was not found. Verify that the resource identifier is correct and that the resource exists, then try your request again.</p>
            capo_network_security_manager.errors.throttling_exception.ThrottlingException: <p>The request was denied because of request throttling. Reduce your request rate and try again.</p>
            capo_network_security_manager.errors.validation_exception.ValidationException: <p>The request failed validation. For details, see the <code>reason</code> and <code>fieldList</code> members of the response.</p>
            capo_network_security_manager.errors.UnknownServiceError: The service returned an error code this client does not model.

        Examples:
            Get a policy
            Retrieves the current published version of a policy by its base ARN, including its associated templates and rules and its enforcement configuration.

            >>> client.get_policy(policy_identifier='arn:aws:network-security-manager:us-east-1:123456789012:policy:xyz789')
        """

        def _handler(
            req: "OperationRequest[capo_network_security_manager.types.get_policy_input.GetPolicyInput]",
        ) -> OperationResponse[
            "capo_network_security_manager.types.get_policy_output.GetPolicyOutput"
        ]:
            import capo_network_security_manager._operations.piccolo_customer_api_service.get_policy

            output, http_response = (
                capo_network_security_manager._operations.piccolo_customer_api_service.get_policy.get_policy(
                    req.options, req.input
                )
            )
            return OperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_network_security_manager.types.get_policy_input.GetPolicyInput = {
            "policy_identifier": policy_identifier
        }

        response = execute_pipeline(
            OperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        response.response.close()
        return response.output

    def update_policy(
        self,
        policy_identifier: "capo_network_security_manager.types.policy_identifier.PolicyIdentifier",
        update_token: "capo_network_security_manager.types.update_token.UpdateToken",
        is_published: "capo_network_security_manager.types.is_published.IsPublished",
        *,
        config_overrides: Optional[NetworkSecurityManagerClientConfig] = None,
        policy_description: Optional[
            "capo_network_security_manager.types.description.Description"
        ] = None,
        priority: Optional[
            "capo_network_security_manager.types.priority.Priority"
        ] = None,
        associated_template_and_rule_list: Optional[
            "capo_network_security_manager.types.template_and_rule_reference_list.TemplateAndRuleReferenceList"
        ] = None,
        policy_configuration: Optional[
            "capo_network_security_manager.types.policy_configuration.PolicyConfiguration"
        ] = None,
        client_token: Optional[
            "capo_network_security_manager.types.idempotency_token.IdempotencyToken"
        ] = None,
    ) -> "capo_network_security_manager.types.update_policy_output.UpdatePolicyOutput":
        """<p>Updates the specified policy. To prevent conflicting concurrent updates, provide the current <code>updateToken</code>. Use <code>isPublished</code> to publish the update or keep the policy as a draft.</p>

        Args:
            policy_identifier: <p>The identifier of the policy. This is the policy's Amazon Resource Name (ARN).</p>
            update_token: <p>A token used for optimistic concurrency control. Each read and write returns an <code>updateToken</code>. Provide the most recent value on your next update to detect and prevent conflicting concurrent modifications.</p>
            policy_description: <p>A description of the policy.</p>
            priority: <p>The priority of the resource. A lower number indicates a higher priority.</p>
            associated_template_and_rule_list: <p>The templates and rules to associate with the policy. For AWS WAF policies, specify 1 to 100 templates or rules, of which at most 2 can be templates. For AWS Shield Advanced policies, this list must be empty.</p>
            policy_configuration: <p>The configuration settings that control the policy's behavior, including remediation and firewall-type-specific settings.</p>
            is_published: <p>Specifies whether to publish the resource. When <code>true</code>, the resource is saved in published (<code>ACTIVE</code>) state. When <code>false</code>, it is saved as a draft (<code>DRAFT</code>).</p>
            client_token: <p>A unique, case-sensitive token that you provide to ensure that the operation completes no more than one time. If you retry a request with the same client token and the same parameters, the service returns the result of the original successful request.</p>

        Raises:
            capo_network_security_manager.errors.access_denied_exception.AccessDeniedException: <p>You do not have sufficient permissions to perform this action.</p>
            capo_network_security_manager.errors.conflict_exception.ConflictException: <p>The request conflicts with the current state of the resource. For example, the resource was modified concurrently, or it is in a state that does not allow the requested operation.</p>
            capo_network_security_manager.errors.internal_server_exception.InternalServerException: <p>The request processing failed because of an internal error in the service. This is a retryable error.</p>
            capo_network_security_manager.errors.resource_not_found_exception.ResourceNotFoundException: <p>The specified resource was not found. Verify that the resource identifier is correct and that the resource exists, then try your request again.</p>
            capo_network_security_manager.errors.service_quota_exceeded_exception.ServiceQuotaExceededException: <p>The request would exceed a service quota.</p>
            capo_network_security_manager.errors.throttling_exception.ThrottlingException: <p>The request was denied because of request throttling. Reduce your request rate and try again.</p>
            capo_network_security_manager.errors.validation_exception.ValidationException: <p>The request failed validation. For details, see the <code>reason</code> and <code>fieldList</code> members of the response.</p>
            capo_network_security_manager.errors.UnknownServiceError: The service returned an error code this client does not model.

        Examples:
            Update a policy and publish it
            Updates the policy's description, priority, and configuration and publishes the change. The updateToken from the most recent read is required for optimistic locking.

            >>> client.update_policy(policy_identifier='arn:aws:network-security-manager:us-east-1:123456789012:policy:xyz789', update_token='e3f4a5b6-6c7d-4e8f-9a0b-0c1d2e3f4a5b', policy_description='WAF policy for web application protection - updated', priority=2, associated_template_and_rule_list=[{'templateIdentifier': 'arn:aws:network-security-manager:us-east-1:123456789012:template:xyz789'}], policy_configuration={'remediationEnabled': True, 'resourcesCleanUp': False, 'wafConfig': {'existingCustomerWebACLResolution': 'NO_REMEDIATION', 'conflictResolution': 'MERGE_WHERE_APPLICABLE'}}, is_published=True)
        """

        def _handler(
            req: "OperationRequest[capo_network_security_manager.types.update_policy_input.UpdatePolicyInput]",
        ) -> OperationResponse[
            "capo_network_security_manager.types.update_policy_output.UpdatePolicyOutput"
        ]:
            import capo_network_security_manager._operations.piccolo_customer_api_service.update_policy

            output, http_response = (
                capo_network_security_manager._operations.piccolo_customer_api_service.update_policy.update_policy(
                    req.options, req.input
                )
            )
            return OperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_network_security_manager.types.update_policy_input.UpdatePolicyInput = {
            "policy_identifier": policy_identifier,
            "update_token": update_token,
            "is_published": is_published,
        }
        if policy_description is not None:
            input_["policy_description"] = policy_description
        if priority is not None:
            input_["priority"] = priority
        if associated_template_and_rule_list is not None:
            input_["associated_template_and_rule_list"] = (
                associated_template_and_rule_list
            )
        if policy_configuration is not None:
            input_["policy_configuration"] = policy_configuration
        if client_token is None:
            client_token = str(uuid.uuid4())
        input_["client_token"] = client_token

        response = execute_pipeline(
            OperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        response.response.close()
        return response.output

    def delete_policy(
        self,
        policy_identifier: "capo_network_security_manager.types.policy_identifier.PolicyIdentifier",
        *,
        config_overrides: Optional[NetworkSecurityManagerClientConfig] = None,
    ) -> None:
        """<p>Deletes the specified policy.</p>

        Args:
            policy_identifier: <p>The identifier of the policy. This is the policy's Amazon Resource Name (ARN).</p>

        Raises:
            capo_network_security_manager.errors.access_denied_exception.AccessDeniedException: <p>You do not have sufficient permissions to perform this action.</p>
            capo_network_security_manager.errors.conflict_exception.ConflictException: <p>The request conflicts with the current state of the resource. For example, the resource was modified concurrently, or it is in a state that does not allow the requested operation.</p>
            capo_network_security_manager.errors.internal_server_exception.InternalServerException: <p>The request processing failed because of an internal error in the service. This is a retryable error.</p>
            capo_network_security_manager.errors.throttling_exception.ThrottlingException: <p>The request was denied because of request throttling. Reduce your request rate and try again.</p>
            capo_network_security_manager.errors.validation_exception.ValidationException: <p>The request failed validation. For details, see the <code>reason</code> and <code>fieldList</code> members of the response.</p>
            capo_network_security_manager.errors.UnknownServiceError: The service returned an error code this client does not model.

        Examples:
            Delete a policy
            Deletes a policy by its ARN. The policy must not be associated with any deployment.

            >>> client.delete_policy(policy_identifier='arn:aws:network-security-manager:us-east-1:123456789012:policy:xyz789')
        """

        def _handler(
            req: "OperationRequest[capo_network_security_manager.types.delete_policy_input.DeletePolicyInput]",
        ) -> OperationResponse[None]:
            import capo_network_security_manager._operations.piccolo_customer_api_service.delete_policy

            output, http_response = (
                capo_network_security_manager._operations.piccolo_customer_api_service.delete_policy.delete_policy(
                    req.options, req.input
                )
            )
            return OperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_network_security_manager.types.delete_policy_input.DeletePolicyInput = {
            "policy_identifier": policy_identifier
        }

        response = execute_pipeline(
            OperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        response.response.close()
        return response.output

    def list_policies(
        self,
        *,
        config_overrides: Optional[NetworkSecurityManagerClientConfig] = None,
        max_results: Optional[
            "capo_network_security_manager.types.max_results.MaxResults"
        ] = None,
        next_token: Optional[
            "capo_network_security_manager.types.next_token.NextToken"
        ] = None,
        status: Optional[
            "capo_network_security_manager.types.entity_status_filter.EntityStatusFilter"
        ] = None,
    ) -> "capo_network_security_manager.types.list_policies_output.ListPoliciesOutput":
        """<p>Lists the policies in the account. You can filter the results by status and page through them using <code>maxResults</code> and <code>nextToken</code>.</p>

        Args:
            max_results: <p>The maximum number of results to return in a single call. Valid range: 1-100. To retrieve the remaining results, use the returned <code>nextToken</code> value in a subsequent call.</p>
            next_token: <p>The token for the next page of results. To retrieve the next page, call the operation again and provide this value. When there are no more results, this value is null.</p>
            status: <p>Filters the results by status, either <code>ACTIVE</code> or <code>DRAFT</code>.</p>

        Raises:
            capo_network_security_manager.errors.access_denied_exception.AccessDeniedException: <p>You do not have sufficient permissions to perform this action.</p>
            capo_network_security_manager.errors.internal_server_exception.InternalServerException: <p>The request processing failed because of an internal error in the service. This is a retryable error.</p>
            capo_network_security_manager.errors.throttling_exception.ThrottlingException: <p>The request was denied because of request throttling. Reduce your request rate and try again.</p>
            capo_network_security_manager.errors.validation_exception.ValidationException: <p>The request failed validation. For details, see the <code>reason</code> and <code>fieldList</code> members of the response.</p>
            capo_network_security_manager.errors.UnknownServiceError: The service returned an error code this client does not model.

        Examples:
            List policies
            Lists the published policies in the account, one page at a time.

            >>> client.list_policies(max_results=10, status='ACTIVE')
        """

        def _handler(
            req: "OperationRequest[capo_network_security_manager.types.list_policies_input.ListPoliciesInput]",
        ) -> OperationResponse[
            "capo_network_security_manager.types.list_policies_output.ListPoliciesOutput"
        ]:
            import capo_network_security_manager._operations.piccolo_customer_api_service.list_policies

            output, http_response = (
                capo_network_security_manager._operations.piccolo_customer_api_service.list_policies.list_policies(
                    req.options, req.input
                )
            )
            return OperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_network_security_manager.types.list_policies_input.ListPoliciesInput = {}
        if max_results is not None:
            input_["max_results"] = max_results
        if next_token is not None:
            input_["next_token"] = next_token
        if status is not None:
            input_["status"] = status

        response = execute_pipeline(
            OperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        response.response.close()
        return response.output

    def iter_list_policies(
        self,
        *,
        config_overrides: Optional[NetworkSecurityManagerClientConfig] = None,
        max_results: Optional[
            "capo_network_security_manager.types.max_results.MaxResults"
        ] = None,
        next_token: Optional[
            "capo_network_security_manager.types.next_token.NextToken"
        ] = None,
        status: Optional[
            "capo_network_security_manager.types.entity_status_filter.EntityStatusFilter"
        ] = None,
    ) -> "Iterator[capo_network_security_manager.types.policy_summary.PolicySummary]":
        _token = next_token
        while True:
            _response = self.list_policies(
                config_overrides=config_overrides,
                max_results=max_results,
                next_token=_token,
                status=status,
            )
            _page = _resolve_path(_response, ("policies",))
            for _item in _page or []:
                yield _item
            _token = _resolve_path(_response, ("next_token",))
            if not _token:
                break

    def create_policy_snapshot(
        self,
        policy_identifier: "capo_network_security_manager.types.policy_identifier.PolicyIdentifier",
        *,
        config_overrides: Optional[NetworkSecurityManagerClientConfig] = None,
        client_token: Optional[
            "capo_network_security_manager.types.idempotency_token.IdempotencyToken"
        ] = None,
        tags: Optional["capo_network_security_manager.types.tag_map.TagMap"] = None,
    ) -> "capo_network_security_manager.types.create_policy_snapshot_output.CreatePolicySnapshotOutput":
        """<p>Creates a snapshot of the current published version of the specified policy.</p>

        Args:
            policy_identifier: <p>The identifier of the policy. This is the policy's Amazon Resource Name (ARN).</p>
            client_token: <p>A unique, case-sensitive token that you provide to ensure that the operation completes no more than one time. If you retry a request with the same client token and the same parameters, the service returns the result of the original successful request.</p>
            tags: <p>The tags to add to the snapshot when it is created.</p>

        Raises:
            capo_network_security_manager.errors.access_denied_exception.AccessDeniedException: <p>You do not have sufficient permissions to perform this action.</p>
            capo_network_security_manager.errors.conflict_exception.ConflictException: <p>The request conflicts with the current state of the resource. For example, the resource was modified concurrently, or it is in a state that does not allow the requested operation.</p>
            capo_network_security_manager.errors.internal_server_exception.InternalServerException: <p>The request processing failed because of an internal error in the service. This is a retryable error.</p>
            capo_network_security_manager.errors.resource_not_found_exception.ResourceNotFoundException: <p>The specified resource was not found. Verify that the resource identifier is correct and that the resource exists, then try your request again.</p>
            capo_network_security_manager.errors.service_quota_exceeded_exception.ServiceQuotaExceededException: <p>The request would exceed a service quota.</p>
            capo_network_security_manager.errors.throttling_exception.ThrottlingException: <p>The request was denied because of request throttling. Reduce your request rate and try again.</p>
            capo_network_security_manager.errors.validation_exception.ValidationException: <p>The request failed validation. For details, see the <code>reason</code> and <code>fieldList</code> members of the response.</p>
            capo_network_security_manager.errors.UnknownServiceError: The service returned an error code this client does not model.

        Examples:
            Create a policy snapshot
            Creates an immutable snapshot of the current published version of a policy. The snapshot is addressable by a version-qualified ARN.

            >>> client.create_policy_snapshot(policy_identifier='arn:aws:network-security-manager:us-east-1:123456789012:policy:xyz789', client_token='550e8400-e29b-41d4-a716-446655440013')
        """

        def _handler(
            req: "OperationRequest[capo_network_security_manager.types.create_policy_snapshot_input.CreatePolicySnapshotInput]",
        ) -> OperationResponse[
            "capo_network_security_manager.types.create_policy_snapshot_output.CreatePolicySnapshotOutput"
        ]:
            import capo_network_security_manager._operations.piccolo_customer_api_service.create_policy_snapshot

            output, http_response = (
                capo_network_security_manager._operations.piccolo_customer_api_service.create_policy_snapshot.create_policy_snapshot(
                    req.options, req.input
                )
            )
            return OperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_network_security_manager.types.create_policy_snapshot_input.CreatePolicySnapshotInput = {
            "policy_identifier": policy_identifier
        }
        if client_token is None:
            client_token = str(uuid.uuid4())
        input_["client_token"] = client_token
        if tags is not None:
            input_["tags"] = tags

        response = execute_pipeline(
            OperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        response.response.close()
        return response.output

    def list_policy_snapshots(
        self,
        policy_identifier: "capo_network_security_manager.types.policy_identifier.PolicyIdentifier",
        *,
        config_overrides: Optional[NetworkSecurityManagerClientConfig] = None,
        max_results: Optional[
            "capo_network_security_manager.types.max_results.MaxResults"
        ] = None,
        next_token: Optional[
            "capo_network_security_manager.types.next_token.NextToken"
        ] = None,
    ) -> "capo_network_security_manager.types.list_policy_snapshots_output.ListPolicySnapshotsOutput":
        """<p>Lists the snapshots of the specified policy.</p>

        Args:
            policy_identifier: <p>The identifier of the policy. This is the policy's Amazon Resource Name (ARN).</p>
            max_results: <p>The maximum number of results to return in a single call. Valid range: 1-100. To retrieve the remaining results, use the returned <code>nextToken</code> value in a subsequent call.</p>
            next_token: <p>The token for the next page of results. To retrieve the next page, call the operation again and provide this value. When there are no more results, this value is null.</p>

        Raises:
            capo_network_security_manager.errors.access_denied_exception.AccessDeniedException: <p>You do not have sufficient permissions to perform this action.</p>
            capo_network_security_manager.errors.internal_server_exception.InternalServerException: <p>The request processing failed because of an internal error in the service. This is a retryable error.</p>
            capo_network_security_manager.errors.resource_not_found_exception.ResourceNotFoundException: <p>The specified resource was not found. Verify that the resource identifier is correct and that the resource exists, then try your request again.</p>
            capo_network_security_manager.errors.throttling_exception.ThrottlingException: <p>The request was denied because of request throttling. Reduce your request rate and try again.</p>
            capo_network_security_manager.errors.validation_exception.ValidationException: <p>The request failed validation. For details, see the <code>reason</code> and <code>fieldList</code> members of the response.</p>
            capo_network_security_manager.errors.UnknownServiceError: The service returned an error code this client does not model.

        Examples:
            List the snapshots of a policy
            Lists the immutable snapshots that have been created for a policy.

            >>> client.list_policy_snapshots(policy_identifier='arn:aws:network-security-manager:us-east-1:123456789012:policy:xyz789', max_results=10)
        """

        def _handler(
            req: "OperationRequest[capo_network_security_manager.types.list_policy_snapshots_input.ListPolicySnapshotsInput]",
        ) -> OperationResponse[
            "capo_network_security_manager.types.list_policy_snapshots_output.ListPolicySnapshotsOutput"
        ]:
            import capo_network_security_manager._operations.piccolo_customer_api_service.list_policy_snapshots

            output, http_response = (
                capo_network_security_manager._operations.piccolo_customer_api_service.list_policy_snapshots.list_policy_snapshots(
                    req.options, req.input
                )
            )
            return OperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_network_security_manager.types.list_policy_snapshots_input.ListPolicySnapshotsInput = {
            "policy_identifier": policy_identifier
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

    def iter_list_policy_snapshots(
        self,
        policy_identifier: "capo_network_security_manager.types.policy_identifier.PolicyIdentifier",
        *,
        config_overrides: Optional[NetworkSecurityManagerClientConfig] = None,
        max_results: Optional[
            "capo_network_security_manager.types.max_results.MaxResults"
        ] = None,
        next_token: Optional[
            "capo_network_security_manager.types.next_token.NextToken"
        ] = None,
    ) -> "Iterator[capo_network_security_manager.types.policy_summary.PolicySummary]":
        _token = next_token
        while True:
            _response = self.list_policy_snapshots(
                policy_identifier,
                config_overrides=config_overrides,
                max_results=max_results,
                next_token=_token,
            )
            _page = _resolve_path(_response, ("snapshots",))
            for _item in _page or []:
                yield _item
            _token = _resolve_path(_response, ("next_token",))
            if not _token:
                break

    def create_rule(
        self,
        rule_name: "capo_network_security_manager.types.rule_name.RuleName",
        firewall_type: "capo_network_security_manager.types.rule_firewall_type.RuleFirewallType",
        rule_type: "capo_network_security_manager.types.rule_type.RuleType",
        configuration: "capo_network_security_manager.types.json_document.JsonDocument",
        *,
        config_overrides: Optional[NetworkSecurityManagerClientConfig] = None,
        client_token: Optional[
            "capo_network_security_manager.types.idempotency_token.IdempotencyToken"
        ] = None,
        rule_description: Optional[
            "capo_network_security_manager.types.description.Description"
        ] = None,
        is_published: Optional[
            "capo_network_security_manager.types.is_published.IsPublished"
        ] = None,
        tags: Optional["capo_network_security_manager.types.tag_map.TagMap"] = None,
    ) -> "capo_network_security_manager.types.create_rule_output.CreateRuleOutput":
        r"""<p>Creates a rule. A rule defines a network security configuration to enforce, such as an AWS WAF rule group or configuration data. Use <code>isPublished</code> to create the rule in published (<code>ACTIVE</code>) or draft (<code>DRAFT</code>) state.</p>

        Args:
            client_token: <p>A unique, case-sensitive token that you provide to ensure that the operation completes no more than one time. If you retry a request with the same client token and the same parameters, the service returns the result of the original successful request.</p>
            rule_name: <p>The name of the rule.</p>
            firewall_type: <p>The firewall type associated with the resource.</p>
            rule_type: <p>The type of the rule. <code>CONFIGURATION</code> rules contain firewall settings, and <code>INSPECTION</code> rules contain rule groups.</p>
            rule_description: <p>A description of the rule.</p>
            configuration: <p>The firewall configuration for the rule, as a JSON document. The structure depends on the rule's firewall type and rule type. For an AWS WAF <code>INSPECTION</code> rule, provide an AWS WAF rule group. For an AWS WAF <code>CONFIGURATION</code> rule, provide a single web ACL setting, such as <code>DefaultAction</code> or <code>VisibilityConfig</code>; use <code>wafConfigDataType</code> to declare which setting the document contains. For the schema of each setting and complete examples, see <a href=\"https://docs.aws.amazon.com/network-security-manager/latest/devguide/what-is.html\">Writing rule configurations</a> in the <i>AWS Network Security Manager Developer Guide</i>.</p>
            is_published: <p>Specifies whether to publish the resource. When <code>true</code>, the resource is saved in published (<code>ACTIVE</code>) state. When <code>false</code>, it is saved as a draft (<code>DRAFT</code>). Default: <code>true</code>.</p>
            tags: <p>The tags to add to the resource when it is created.</p>

        Raises:
            capo_network_security_manager.errors.access_denied_exception.AccessDeniedException: <p>You do not have sufficient permissions to perform this action.</p>
            capo_network_security_manager.errors.conflict_exception.ConflictException: <p>The request conflicts with the current state of the resource. For example, the resource was modified concurrently, or it is in a state that does not allow the requested operation.</p>
            capo_network_security_manager.errors.internal_server_exception.InternalServerException: <p>The request processing failed because of an internal error in the service. This is a retryable error.</p>
            capo_network_security_manager.errors.service_quota_exceeded_exception.ServiceQuotaExceededException: <p>The request would exceed a service quota.</p>
            capo_network_security_manager.errors.service_unavailable_exception.ServiceUnavailableException: <p>The service is temporarily unavailable. This is a retryable error.</p>
            capo_network_security_manager.errors.tag_policy_violation_exception.TagPolicyViolationException: <p>The request violates a tag policy that is in effect for the account or organization.</p>
            capo_network_security_manager.errors.throttling_exception.ThrottlingException: <p>The request was denied because of request throttling. Reduce your request rate and try again.</p>
            capo_network_security_manager.errors.validation_exception.ValidationException: <p>The request failed validation. For details, see the <code>reason</code> and <code>fieldList</code> members of the response.</p>
            capo_network_security_manager.errors.UnknownServiceError: The service returned an error code this client does not model.

        Examples:
            Create a WAF rule
            Creates a new WAF inspection rule in draft state.

            >>> client.create_rule(client_token='550e8400-e29b-41d4-a716-446655440000', rule_name='block-known-bad-ips', firewall_type='WAF', rule_type='INSPECTION', rule_description='Blocks requests from known malicious IP addresses', configuration={}, is_published=False)
        """

        def _handler(
            req: "OperationRequest[capo_network_security_manager.types.create_rule_input.CreateRuleInput]",
        ) -> OperationResponse[
            "capo_network_security_manager.types.create_rule_output.CreateRuleOutput"
        ]:
            import capo_network_security_manager._operations.piccolo_customer_api_service.create_rule

            output, http_response = (
                capo_network_security_manager._operations.piccolo_customer_api_service.create_rule.create_rule(
                    req.options, req.input
                )
            )
            return OperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_network_security_manager.types.create_rule_input.CreateRuleInput = {
            "rule_name": rule_name,
            "firewall_type": firewall_type,
            "rule_type": rule_type,
            "configuration": configuration,
        }
        if client_token is None:
            client_token = str(uuid.uuid4())
        input_["client_token"] = client_token
        if rule_description is not None:
            input_["rule_description"] = rule_description
        if is_published is not None:
            input_["is_published"] = is_published
        if tags is not None:
            input_["tags"] = tags

        response = execute_pipeline(
            OperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        response.response.close()
        return response.output

    def get_rule(
        self,
        rule_identifier: "capo_network_security_manager.types.rule_identifier.RuleIdentifier",
        *,
        config_overrides: Optional[NetworkSecurityManagerClientConfig] = None,
    ) -> "capo_network_security_manager.types.get_rule_output.GetRuleOutput":
        """<p>Retrieves the details of the specified rule.</p>

        Args:
            rule_identifier: <p>The identifier of the rule. This is the rule's Amazon Resource Name (ARN).</p>

        Raises:
            capo_network_security_manager.errors.access_denied_exception.AccessDeniedException: <p>You do not have sufficient permissions to perform this action.</p>
            capo_network_security_manager.errors.internal_server_exception.InternalServerException: <p>The request processing failed because of an internal error in the service. This is a retryable error.</p>
            capo_network_security_manager.errors.resource_not_found_exception.ResourceNotFoundException: <p>The specified resource was not found. Verify that the resource identifier is correct and that the resource exists, then try your request again.</p>
            capo_network_security_manager.errors.throttling_exception.ThrottlingException: <p>The request was denied because of request throttling. Reduce your request rate and try again.</p>
            capo_network_security_manager.errors.validation_exception.ValidationException: <p>The request failed validation. For details, see the <code>reason</code> and <code>fieldList</code> members of the response.</p>
            capo_network_security_manager.errors.UnknownServiceError: The service returned an error code this client does not model.

        Examples:
            Get a rule
            Retrieves the current published version of a rule by its base ARN.

            >>> client.get_rule(rule_identifier='arn:aws:network-security-manager:us-east-1:123456789012:rule:abc123')
            Get a specific version of a rule
            Retrieves a specific immutable version (snapshot) of a rule using a version-qualified ARN. The response has isSnapshot set to true. Omitting the version qualifier returns the current published rule instead.

            >>> client.get_rule(rule_identifier='arn:aws:network-security-manager:us-east-1:123456789012:rule:abc123:3')
        """

        def _handler(
            req: "OperationRequest[capo_network_security_manager.types.get_rule_input.GetRuleInput]",
        ) -> OperationResponse[
            "capo_network_security_manager.types.get_rule_output.GetRuleOutput"
        ]:
            import capo_network_security_manager._operations.piccolo_customer_api_service.get_rule

            output, http_response = (
                capo_network_security_manager._operations.piccolo_customer_api_service.get_rule.get_rule(
                    req.options, req.input
                )
            )
            return OperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_network_security_manager.types.get_rule_input.GetRuleInput = {
            "rule_identifier": rule_identifier
        }

        response = execute_pipeline(
            OperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        response.response.close()
        return response.output

    def update_rule(
        self,
        rule_identifier: "capo_network_security_manager.types.rule_identifier.RuleIdentifier",
        update_token: "capo_network_security_manager.types.update_token.UpdateToken",
        is_published: "capo_network_security_manager.types.is_published.IsPublished",
        *,
        config_overrides: Optional[NetworkSecurityManagerClientConfig] = None,
        rule_type: Optional[
            "capo_network_security_manager.types.rule_type.RuleType"
        ] = None,
        rule_description: Optional[
            "capo_network_security_manager.types.description.Description"
        ] = None,
        configuration: Optional[
            "capo_network_security_manager.types.json_document.JsonDocument"
        ] = None,
        client_token: Optional[
            "capo_network_security_manager.types.idempotency_token.IdempotencyToken"
        ] = None,
    ) -> "capo_network_security_manager.types.update_rule_output.UpdateRuleOutput":
        r"""<p>Updates the specified rule. To prevent conflicting concurrent updates, provide the current <code>updateToken</code>. Use <code>isPublished</code> to publish the update or keep the rule as a draft.</p>

        Args:
            rule_identifier: <p>The identifier of the rule. This is the rule's Amazon Resource Name (ARN).</p>
            update_token: <p>A token used for optimistic concurrency control. Each read and write returns an <code>updateToken</code>. Provide the most recent value on your next update to detect and prevent conflicting concurrent modifications.</p>
            rule_type: <p>The type of the rule. <code>CONFIGURATION</code> rules contain firewall settings, and <code>INSPECTION</code> rules contain rule groups.</p>
            rule_description: <p>A description of the rule.</p>
            configuration: <p>The firewall configuration for the rule, as a JSON document. The structure depends on the rule's firewall type and rule type. For an AWS WAF <code>INSPECTION</code> rule, provide an AWS WAF rule group. For an AWS WAF <code>CONFIGURATION</code> rule, provide a single web ACL setting, such as <code>DefaultAction</code> or <code>VisibilityConfig</code>; use <code>wafConfigDataType</code> to declare which setting the document contains. For the schema of each setting and complete examples, see <a href=\"https://docs.aws.amazon.com/network-security-manager/latest/devguide/what-is.html\">Writing rule configurations</a> in the <i>AWS Network Security Manager Developer Guide</i>.</p>
            is_published: <p>Specifies whether to publish the resource. When <code>true</code>, the resource is saved in published (<code>ACTIVE</code>) state. When <code>false</code>, it is saved as a draft (<code>DRAFT</code>).</p>
            client_token: <p>A unique, case-sensitive token that you provide to ensure that the operation completes no more than one time. If you retry a request with the same client token and the same parameters, the service returns the result of the original successful request.</p>

        Raises:
            capo_network_security_manager.errors.access_denied_exception.AccessDeniedException: <p>You do not have sufficient permissions to perform this action.</p>
            capo_network_security_manager.errors.conflict_exception.ConflictException: <p>The request conflicts with the current state of the resource. For example, the resource was modified concurrently, or it is in a state that does not allow the requested operation.</p>
            capo_network_security_manager.errors.internal_server_exception.InternalServerException: <p>The request processing failed because of an internal error in the service. This is a retryable error.</p>
            capo_network_security_manager.errors.resource_not_found_exception.ResourceNotFoundException: <p>The specified resource was not found. Verify that the resource identifier is correct and that the resource exists, then try your request again.</p>
            capo_network_security_manager.errors.service_quota_exceeded_exception.ServiceQuotaExceededException: <p>The request would exceed a service quota.</p>
            capo_network_security_manager.errors.throttling_exception.ThrottlingException: <p>The request was denied because of request throttling. Reduce your request rate and try again.</p>
            capo_network_security_manager.errors.validation_exception.ValidationException: <p>The request failed validation. For details, see the <code>reason</code> and <code>fieldList</code> members of the response.</p>
            capo_network_security_manager.errors.UnknownServiceError: The service returned an error code this client does not model.

        Examples:
            Update a rule and publish it
            Updates the rule's description and configuration and publishes the change. The updateToken from the most recent read is required for optimistic locking.

            >>> client.update_rule(rule_identifier='arn:aws:network-security-manager:us-east-1:123456789012:rule:abc123', update_token='c1d2e3f4-4a5b-4c6d-9e7f-8a9b0c1d2e3f', rule_type='INSPECTION', rule_description='Blocks requests from known malicious IP addresses - updated list', configuration={}, is_published=True)
        """

        def _handler(
            req: "OperationRequest[capo_network_security_manager.types.update_rule_input.UpdateRuleInput]",
        ) -> OperationResponse[
            "capo_network_security_manager.types.update_rule_output.UpdateRuleOutput"
        ]:
            import capo_network_security_manager._operations.piccolo_customer_api_service.update_rule

            output, http_response = (
                capo_network_security_manager._operations.piccolo_customer_api_service.update_rule.update_rule(
                    req.options, req.input
                )
            )
            return OperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_network_security_manager.types.update_rule_input.UpdateRuleInput = {
            "rule_identifier": rule_identifier,
            "update_token": update_token,
            "is_published": is_published,
        }
        if rule_type is not None:
            input_["rule_type"] = rule_type
        if rule_description is not None:
            input_["rule_description"] = rule_description
        if configuration is not None:
            input_["configuration"] = configuration
        if client_token is None:
            client_token = str(uuid.uuid4())
        input_["client_token"] = client_token

        response = execute_pipeline(
            OperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        response.response.close()
        return response.output

    def delete_rule(
        self,
        rule_identifier: "capo_network_security_manager.types.rule_identifier.RuleIdentifier",
        *,
        config_overrides: Optional[NetworkSecurityManagerClientConfig] = None,
    ) -> None:
        """<p>Deletes the specified rule.</p>

        Args:
            rule_identifier: <p>The identifier of the rule. This is the rule's Amazon Resource Name (ARN).</p>

        Raises:
            capo_network_security_manager.errors.access_denied_exception.AccessDeniedException: <p>You do not have sufficient permissions to perform this action.</p>
            capo_network_security_manager.errors.conflict_exception.ConflictException: <p>The request conflicts with the current state of the resource. For example, the resource was modified concurrently, or it is in a state that does not allow the requested operation.</p>
            capo_network_security_manager.errors.internal_server_exception.InternalServerException: <p>The request processing failed because of an internal error in the service. This is a retryable error.</p>
            capo_network_security_manager.errors.throttling_exception.ThrottlingException: <p>The request was denied because of request throttling. Reduce your request rate and try again.</p>
            capo_network_security_manager.errors.validation_exception.ValidationException: <p>The request failed validation. For details, see the <code>reason</code> and <code>fieldList</code> members of the response.</p>
            capo_network_security_manager.errors.UnknownServiceError: The service returned an error code this client does not model.

        Examples:
            Delete a rule
            Deletes a rule by its ARN. The rule must not be associated with any template or policy.

            >>> client.delete_rule(rule_identifier='arn:aws:network-security-manager:us-east-1:123456789012:rule:abc123')
        """

        def _handler(
            req: "OperationRequest[capo_network_security_manager.types.delete_rule_input.DeleteRuleInput]",
        ) -> OperationResponse[None]:
            import capo_network_security_manager._operations.piccolo_customer_api_service.delete_rule

            output, http_response = (
                capo_network_security_manager._operations.piccolo_customer_api_service.delete_rule.delete_rule(
                    req.options, req.input
                )
            )
            return OperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_network_security_manager.types.delete_rule_input.DeleteRuleInput = {
            "rule_identifier": rule_identifier
        }

        response = execute_pipeline(
            OperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        response.response.close()
        return response.output

    def list_rules(
        self,
        *,
        config_overrides: Optional[NetworkSecurityManagerClientConfig] = None,
        max_results: Optional[
            "capo_network_security_manager.types.max_results.MaxResults"
        ] = None,
        next_token: Optional[
            "capo_network_security_manager.types.next_token.NextToken"
        ] = None,
        status: Optional[
            "capo_network_security_manager.types.entity_status_filter.EntityStatusFilter"
        ] = None,
    ) -> "capo_network_security_manager.types.list_rules_output.ListRulesOutput":
        """<p>Lists the rules in the account. You can filter the results by status and page through them using <code>maxResults</code> and <code>nextToken</code>.</p>

        Args:
            max_results: <p>The maximum number of results to return in a single call. Valid range: 1-100. To retrieve the remaining results, use the returned <code>nextToken</code> value in a subsequent call.</p>
            next_token: <p>The token for the next page of results. To retrieve the next page, call the operation again and provide this value. When there are no more results, this value is null.</p>
            status: <p>Filters the results by status, either <code>ACTIVE</code> or <code>DRAFT</code>.</p>

        Raises:
            capo_network_security_manager.errors.access_denied_exception.AccessDeniedException: <p>You do not have sufficient permissions to perform this action.</p>
            capo_network_security_manager.errors.internal_server_exception.InternalServerException: <p>The request processing failed because of an internal error in the service. This is a retryable error.</p>
            capo_network_security_manager.errors.throttling_exception.ThrottlingException: <p>The request was denied because of request throttling. Reduce your request rate and try again.</p>
            capo_network_security_manager.errors.validation_exception.ValidationException: <p>The request failed validation. For details, see the <code>reason</code> and <code>fieldList</code> members of the response.</p>
            capo_network_security_manager.errors.UnknownServiceError: The service returned an error code this client does not model.

        Examples:
            List rules
            Lists the published rules in the account, one page at a time.

            >>> client.list_rules(max_results=10, status='ACTIVE')
        """

        def _handler(
            req: "OperationRequest[capo_network_security_manager.types.list_rules_input.ListRulesInput]",
        ) -> OperationResponse[
            "capo_network_security_manager.types.list_rules_output.ListRulesOutput"
        ]:
            import capo_network_security_manager._operations.piccolo_customer_api_service.list_rules

            output, http_response = (
                capo_network_security_manager._operations.piccolo_customer_api_service.list_rules.list_rules(
                    req.options, req.input
                )
            )
            return OperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_network_security_manager.types.list_rules_input.ListRulesInput = {}
        if max_results is not None:
            input_["max_results"] = max_results
        if next_token is not None:
            input_["next_token"] = next_token
        if status is not None:
            input_["status"] = status

        response = execute_pipeline(
            OperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        response.response.close()
        return response.output

    def iter_list_rules(
        self,
        *,
        config_overrides: Optional[NetworkSecurityManagerClientConfig] = None,
        max_results: Optional[
            "capo_network_security_manager.types.max_results.MaxResults"
        ] = None,
        next_token: Optional[
            "capo_network_security_manager.types.next_token.NextToken"
        ] = None,
        status: Optional[
            "capo_network_security_manager.types.entity_status_filter.EntityStatusFilter"
        ] = None,
    ) -> "Iterator[capo_network_security_manager.types.rule_summary.RuleSummary]":
        _token = next_token
        while True:
            _response = self.list_rules(
                config_overrides=config_overrides,
                max_results=max_results,
                next_token=_token,
                status=status,
            )
            _page = _resolve_path(_response, ("rules",))
            for _item in _page or []:
                yield _item
            _token = _resolve_path(_response, ("next_token",))
            if not _token:
                break

    def create_rule_snapshot(
        self,
        rule_identifier: "capo_network_security_manager.types.rule_identifier.RuleIdentifier",
        *,
        config_overrides: Optional[NetworkSecurityManagerClientConfig] = None,
        client_token: Optional[
            "capo_network_security_manager.types.idempotency_token.IdempotencyToken"
        ] = None,
        tags: Optional["capo_network_security_manager.types.tag_map.TagMap"] = None,
    ) -> "capo_network_security_manager.types.create_rule_snapshot_output.CreateRuleSnapshotOutput":
        """<p>Creates a snapshot of the current published version of the specified rule. A snapshot is an immutable, versioned copy that other resources can reference.</p>

        Args:
            rule_identifier: <p>The identifier of the rule. This is the rule's Amazon Resource Name (ARN).</p>
            client_token: <p>A unique, case-sensitive token that you provide to ensure that the operation completes no more than one time. If you retry a request with the same client token and the same parameters, the service returns the result of the original successful request.</p>
            tags: <p>The tags to add to the snapshot when it is created.</p>

        Raises:
            capo_network_security_manager.errors.access_denied_exception.AccessDeniedException: <p>You do not have sufficient permissions to perform this action.</p>
            capo_network_security_manager.errors.conflict_exception.ConflictException: <p>The request conflicts with the current state of the resource. For example, the resource was modified concurrently, or it is in a state that does not allow the requested operation.</p>
            capo_network_security_manager.errors.internal_server_exception.InternalServerException: <p>The request processing failed because of an internal error in the service. This is a retryable error.</p>
            capo_network_security_manager.errors.resource_not_found_exception.ResourceNotFoundException: <p>The specified resource was not found. Verify that the resource identifier is correct and that the resource exists, then try your request again.</p>
            capo_network_security_manager.errors.service_quota_exceeded_exception.ServiceQuotaExceededException: <p>The request would exceed a service quota.</p>
            capo_network_security_manager.errors.throttling_exception.ThrottlingException: <p>The request was denied because of request throttling. Reduce your request rate and try again.</p>
            capo_network_security_manager.errors.validation_exception.ValidationException: <p>The request failed validation. For details, see the <code>reason</code> and <code>fieldList</code> members of the response.</p>
            capo_network_security_manager.errors.UnknownServiceError: The service returned an error code this client does not model.

        Examples:
            Create a rule snapshot
            Creates an immutable snapshot of the current published version of a rule. The snapshot is addressable by a version-qualified ARN.

            >>> client.create_rule_snapshot(rule_identifier='arn:aws:network-security-manager:us-east-1:123456789012:rule:abc123', client_token='550e8400-e29b-41d4-a716-446655440011')
        """

        def _handler(
            req: "OperationRequest[capo_network_security_manager.types.create_rule_snapshot_input.CreateRuleSnapshotInput]",
        ) -> OperationResponse[
            "capo_network_security_manager.types.create_rule_snapshot_output.CreateRuleSnapshotOutput"
        ]:
            import capo_network_security_manager._operations.piccolo_customer_api_service.create_rule_snapshot

            output, http_response = (
                capo_network_security_manager._operations.piccolo_customer_api_service.create_rule_snapshot.create_rule_snapshot(
                    req.options, req.input
                )
            )
            return OperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_network_security_manager.types.create_rule_snapshot_input.CreateRuleSnapshotInput = {
            "rule_identifier": rule_identifier
        }
        if client_token is None:
            client_token = str(uuid.uuid4())
        input_["client_token"] = client_token
        if tags is not None:
            input_["tags"] = tags

        response = execute_pipeline(
            OperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        response.response.close()
        return response.output

    def list_rule_snapshots(
        self,
        rule_identifier: "capo_network_security_manager.types.rule_identifier.RuleIdentifier",
        *,
        config_overrides: Optional[NetworkSecurityManagerClientConfig] = None,
        max_results: Optional[
            "capo_network_security_manager.types.max_results.MaxResults"
        ] = None,
        next_token: Optional[
            "capo_network_security_manager.types.next_token.NextToken"
        ] = None,
    ) -> "capo_network_security_manager.types.list_rule_snapshots_output.ListRuleSnapshotsOutput":
        """<p>Lists the snapshots of the specified rule.</p>

        Args:
            rule_identifier: <p>The identifier of the rule. This is the rule's Amazon Resource Name (ARN).</p>
            max_results: <p>The maximum number of results to return in a single call. Valid range: 1-100. To retrieve the remaining results, use the returned <code>nextToken</code> value in a subsequent call.</p>
            next_token: <p>The token for the next page of results. To retrieve the next page, call the operation again and provide this value. When there are no more results, this value is null.</p>

        Raises:
            capo_network_security_manager.errors.access_denied_exception.AccessDeniedException: <p>You do not have sufficient permissions to perform this action.</p>
            capo_network_security_manager.errors.internal_server_exception.InternalServerException: <p>The request processing failed because of an internal error in the service. This is a retryable error.</p>
            capo_network_security_manager.errors.resource_not_found_exception.ResourceNotFoundException: <p>The specified resource was not found. Verify that the resource identifier is correct and that the resource exists, then try your request again.</p>
            capo_network_security_manager.errors.throttling_exception.ThrottlingException: <p>The request was denied because of request throttling. Reduce your request rate and try again.</p>
            capo_network_security_manager.errors.validation_exception.ValidationException: <p>The request failed validation. For details, see the <code>reason</code> and <code>fieldList</code> members of the response.</p>
            capo_network_security_manager.errors.UnknownServiceError: The service returned an error code this client does not model.

        Examples:
            List the snapshots of a rule
            Lists the immutable snapshots that have been created for a rule.

            >>> client.list_rule_snapshots(rule_identifier='arn:aws:network-security-manager:us-east-1:123456789012:rule:abc123', max_results=10)
        """

        def _handler(
            req: "OperationRequest[capo_network_security_manager.types.list_rule_snapshots_input.ListRuleSnapshotsInput]",
        ) -> OperationResponse[
            "capo_network_security_manager.types.list_rule_snapshots_output.ListRuleSnapshotsOutput"
        ]:
            import capo_network_security_manager._operations.piccolo_customer_api_service.list_rule_snapshots

            output, http_response = (
                capo_network_security_manager._operations.piccolo_customer_api_service.list_rule_snapshots.list_rule_snapshots(
                    req.options, req.input
                )
            )
            return OperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_network_security_manager.types.list_rule_snapshots_input.ListRuleSnapshotsInput = {
            "rule_identifier": rule_identifier
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

    def iter_list_rule_snapshots(
        self,
        rule_identifier: "capo_network_security_manager.types.rule_identifier.RuleIdentifier",
        *,
        config_overrides: Optional[NetworkSecurityManagerClientConfig] = None,
        max_results: Optional[
            "capo_network_security_manager.types.max_results.MaxResults"
        ] = None,
        next_token: Optional[
            "capo_network_security_manager.types.next_token.NextToken"
        ] = None,
    ) -> "Iterator[capo_network_security_manager.types.rule_summary.RuleSummary]":
        _token = next_token
        while True:
            _response = self.list_rule_snapshots(
                rule_identifier,
                config_overrides=config_overrides,
                max_results=max_results,
                next_token=_token,
            )
            _page = _resolve_path(_response, ("snapshots",))
            for _item in _page or []:
                yield _item
            _token = _resolve_path(_response, ("next_token",))
            if not _token:
                break

    def create_scope(
        self,
        scope_name: "capo_network_security_manager.types.scope_name.ScopeName",
        scope_configuration: "capo_network_security_manager.types.scope_configuration.ScopeConfiguration",
        *,
        config_overrides: Optional[NetworkSecurityManagerClientConfig] = None,
        client_token: Optional[
            "capo_network_security_manager.types.idempotency_token.IdempotencyToken"
        ] = None,
        scope_description: Optional[
            "capo_network_security_manager.types.description.Description"
        ] = None,
        is_published: Optional[
            "capo_network_security_manager.types.is_published.IsPublished"
        ] = None,
        tags: Optional["capo_network_security_manager.types.tag_map.TagMap"] = None,
    ) -> "capo_network_security_manager.types.create_scope_output.CreateScopeOutput":
        """<p>Creates a scope. A scope selects the accounts and resources that a deployment applies to. Use <code>isPublished</code> to create the scope in published (<code>ACTIVE</code>) or draft (<code>DRAFT</code>) state.</p>

        Args:
            client_token: <p>A unique, case-sensitive token that you provide to ensure that the operation completes no more than one time. If you retry a request with the same client token and the same parameters, the service returns the result of the original successful request.</p>
            scope_name: <p>The name of the scope.</p>
            scope_description: <p>A description of the scope.</p>
            scope_configuration: <p>The configuration that defines which accounts and resources are in scope.</p>
            is_published: <p>Specifies whether to publish the resource. When <code>true</code>, the resource is saved in published (<code>ACTIVE</code>) state. When <code>false</code>, it is saved as a draft (<code>DRAFT</code>). Default: <code>true</code>.</p>
            tags: <p>The tags to add to the resource when it is created.</p>

        Raises:
            capo_network_security_manager.errors.access_denied_exception.AccessDeniedException: <p>You do not have sufficient permissions to perform this action.</p>
            capo_network_security_manager.errors.conflict_exception.ConflictException: <p>The request conflicts with the current state of the resource. For example, the resource was modified concurrently, or it is in a state that does not allow the requested operation.</p>
            capo_network_security_manager.errors.internal_server_exception.InternalServerException: <p>The request processing failed because of an internal error in the service. This is a retryable error.</p>
            capo_network_security_manager.errors.service_quota_exceeded_exception.ServiceQuotaExceededException: <p>The request would exceed a service quota.</p>
            capo_network_security_manager.errors.service_unavailable_exception.ServiceUnavailableException: <p>The service is temporarily unavailable. This is a retryable error.</p>
            capo_network_security_manager.errors.tag_policy_violation_exception.TagPolicyViolationException: <p>The request violates a tag policy that is in effect for the account or organization.</p>
            capo_network_security_manager.errors.throttling_exception.ThrottlingException: <p>The request was denied because of request throttling. Reduce your request rate and try again.</p>
            capo_network_security_manager.errors.validation_exception.ValidationException: <p>The request failed validation. For details, see the <code>reason</code> and <code>fieldList</code> members of the response.</p>
            capo_network_security_manager.errors.UnknownServiceError: The service returned an error code this client does not model.

        Examples:
            Create a scope
            Creates a new scope in published (ACTIVE) state.

            >>> client.create_scope(client_token='550e8400-e29b-41d4-a716-446655440001', scope_name='production-web-apps', scope_description='Scope covering all production web application resources', scope_configuration={'accountFilter': {'includeAll': {}}, 'resourceScopes': {}}, is_published=True)
        """

        def _handler(
            req: "OperationRequest[capo_network_security_manager.types.create_scope_input.CreateScopeInput]",
        ) -> OperationResponse[
            "capo_network_security_manager.types.create_scope_output.CreateScopeOutput"
        ]:
            import capo_network_security_manager._operations.piccolo_customer_api_service.create_scope

            output, http_response = (
                capo_network_security_manager._operations.piccolo_customer_api_service.create_scope.create_scope(
                    req.options, req.input
                )
            )
            return OperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_network_security_manager.types.create_scope_input.CreateScopeInput = {
            "scope_name": scope_name,
            "scope_configuration": scope_configuration,
        }
        if client_token is None:
            client_token = str(uuid.uuid4())
        input_["client_token"] = client_token
        if scope_description is not None:
            input_["scope_description"] = scope_description
        if is_published is not None:
            input_["is_published"] = is_published
        if tags is not None:
            input_["tags"] = tags

        response = execute_pipeline(
            OperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        response.response.close()
        return response.output

    def get_scope(
        self,
        scope_identifier: "capo_network_security_manager.types.scope_identifier.ScopeIdentifier",
        *,
        config_overrides: Optional[NetworkSecurityManagerClientConfig] = None,
    ) -> "capo_network_security_manager.types.get_scope_output.GetScopeOutput":
        """<p>Retrieves the details of the specified scope.</p>

        Args:
            scope_identifier: <p>The identifier of the scope. This is the scope's Amazon Resource Name (ARN).</p>

        Raises:
            capo_network_security_manager.errors.access_denied_exception.AccessDeniedException: <p>You do not have sufficient permissions to perform this action.</p>
            capo_network_security_manager.errors.internal_server_exception.InternalServerException: <p>The request processing failed because of an internal error in the service. This is a retryable error.</p>
            capo_network_security_manager.errors.resource_not_found_exception.ResourceNotFoundException: <p>The specified resource was not found. Verify that the resource identifier is correct and that the resource exists, then try your request again.</p>
            capo_network_security_manager.errors.throttling_exception.ThrottlingException: <p>The request was denied because of request throttling. Reduce your request rate and try again.</p>
            capo_network_security_manager.errors.validation_exception.ValidationException: <p>The request failed validation. For details, see the <code>reason</code> and <code>fieldList</code> members of the response.</p>
            capo_network_security_manager.errors.UnknownServiceError: The service returned an error code this client does not model.

        Examples:
            Get a scope
            Retrieves the current published version of a scope by its base ARN.

            >>> client.get_scope(scope_identifier='arn:aws:network-security-manager:us-east-1:123456789012:scope:abc123')
        """

        def _handler(
            req: "OperationRequest[capo_network_security_manager.types.get_scope_input.GetScopeInput]",
        ) -> OperationResponse[
            "capo_network_security_manager.types.get_scope_output.GetScopeOutput"
        ]:
            import capo_network_security_manager._operations.piccolo_customer_api_service.get_scope

            output, http_response = (
                capo_network_security_manager._operations.piccolo_customer_api_service.get_scope.get_scope(
                    req.options, req.input
                )
            )
            return OperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_network_security_manager.types.get_scope_input.GetScopeInput = {
            "scope_identifier": scope_identifier
        }

        response = execute_pipeline(
            OperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        response.response.close()
        return response.output

    def update_scope(
        self,
        scope_identifier: "capo_network_security_manager.types.scope_identifier.ScopeIdentifier",
        update_token: "capo_network_security_manager.types.update_token.UpdateToken",
        is_published: "capo_network_security_manager.types.is_published.IsPublished",
        *,
        config_overrides: Optional[NetworkSecurityManagerClientConfig] = None,
        scope_description: Optional[
            "capo_network_security_manager.types.description.Description"
        ] = None,
        scope_configuration: Optional[
            "capo_network_security_manager.types.scope_configuration.ScopeConfiguration"
        ] = None,
        client_token: Optional[
            "capo_network_security_manager.types.idempotency_token.IdempotencyToken"
        ] = None,
    ) -> "capo_network_security_manager.types.update_scope_output.UpdateScopeOutput":
        """<p>Updates the specified scope. To prevent conflicting concurrent updates, provide the current <code>updateToken</code>. Use <code>isPublished</code> to publish the update or keep the scope as a draft.</p>

        Args:
            scope_identifier: <p>The identifier of the scope. This is the scope's Amazon Resource Name (ARN).</p>
            update_token: <p>A token used for optimistic concurrency control. Each read and write returns an <code>updateToken</code>. Provide the most recent value on your next update to detect and prevent conflicting concurrent modifications.</p>
            scope_description: <p>A description of the scope.</p>
            scope_configuration: <p>The configuration that defines which accounts and resources are in scope. If you don't include this member, the scope keeps its existing configuration.</p> <p>A new configuration can change which accounts and resources are selected, but it can't add or remove the account filter itself: a scope created for multi-account use stays multi-account, and a scope created for single-account use stays single-account.</p>
            is_published: <p>Specifies whether to publish the resource. When <code>true</code>, the resource is saved in published (<code>ACTIVE</code>) state. When <code>false</code>, it is saved as a draft (<code>DRAFT</code>).</p>
            client_token: <p>A unique, case-sensitive token that you provide to ensure that the operation completes no more than one time. If you retry a request with the same client token and the same parameters, the service returns the result of the original successful request.</p>

        Raises:
            capo_network_security_manager.errors.access_denied_exception.AccessDeniedException: <p>You do not have sufficient permissions to perform this action.</p>
            capo_network_security_manager.errors.conflict_exception.ConflictException: <p>The request conflicts with the current state of the resource. For example, the resource was modified concurrently, or it is in a state that does not allow the requested operation.</p>
            capo_network_security_manager.errors.internal_server_exception.InternalServerException: <p>The request processing failed because of an internal error in the service. This is a retryable error.</p>
            capo_network_security_manager.errors.resource_not_found_exception.ResourceNotFoundException: <p>The specified resource was not found. Verify that the resource identifier is correct and that the resource exists, then try your request again.</p>
            capo_network_security_manager.errors.service_quota_exceeded_exception.ServiceQuotaExceededException: <p>The request would exceed a service quota.</p>
            capo_network_security_manager.errors.throttling_exception.ThrottlingException: <p>The request was denied because of request throttling. Reduce your request rate and try again.</p>
            capo_network_security_manager.errors.validation_exception.ValidationException: <p>The request failed validation. For details, see the <code>reason</code> and <code>fieldList</code> members of the response.</p>
            capo_network_security_manager.errors.UnknownServiceError: The service returned an error code this client does not model.

        Examples:
            Update a scope and publish it
            Updates the scope's description and configuration and publishes the change. The updateToken from the most recent read is required for optimistic locking.

            >>> client.update_scope(scope_identifier='arn:aws:network-security-manager:us-east-1:123456789012:scope:abc123', update_token='b0c4d1e2-3f4a-4b5c-8d6e-7f8a9b0c1d2e', scope_description='Scope covering all production web application resources in US East 1', scope_configuration={'accountFilter': {'includeAll': {}}, 'resourceScopes': {}}, is_published=True)
        """

        def _handler(
            req: "OperationRequest[capo_network_security_manager.types.update_scope_input.UpdateScopeInput]",
        ) -> OperationResponse[
            "capo_network_security_manager.types.update_scope_output.UpdateScopeOutput"
        ]:
            import capo_network_security_manager._operations.piccolo_customer_api_service.update_scope

            output, http_response = (
                capo_network_security_manager._operations.piccolo_customer_api_service.update_scope.update_scope(
                    req.options, req.input
                )
            )
            return OperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_network_security_manager.types.update_scope_input.UpdateScopeInput = {
            "scope_identifier": scope_identifier,
            "update_token": update_token,
            "is_published": is_published,
        }
        if scope_description is not None:
            input_["scope_description"] = scope_description
        if scope_configuration is not None:
            input_["scope_configuration"] = scope_configuration
        if client_token is None:
            client_token = str(uuid.uuid4())
        input_["client_token"] = client_token

        response = execute_pipeline(
            OperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        response.response.close()
        return response.output

    def delete_scope(
        self,
        scope_identifier: "capo_network_security_manager.types.scope_identifier.ScopeIdentifier",
        *,
        config_overrides: Optional[NetworkSecurityManagerClientConfig] = None,
    ) -> None:
        """<p>Deletes the specified scope.</p>

        Args:
            scope_identifier: <p>The identifier of the scope. This is the scope's Amazon Resource Name (ARN).</p>

        Raises:
            capo_network_security_manager.errors.access_denied_exception.AccessDeniedException: <p>You do not have sufficient permissions to perform this action.</p>
            capo_network_security_manager.errors.conflict_exception.ConflictException: <p>The request conflicts with the current state of the resource. For example, the resource was modified concurrently, or it is in a state that does not allow the requested operation.</p>
            capo_network_security_manager.errors.internal_server_exception.InternalServerException: <p>The request processing failed because of an internal error in the service. This is a retryable error.</p>
            capo_network_security_manager.errors.throttling_exception.ThrottlingException: <p>The request was denied because of request throttling. Reduce your request rate and try again.</p>
            capo_network_security_manager.errors.validation_exception.ValidationException: <p>The request failed validation. For details, see the <code>reason</code> and <code>fieldList</code> members of the response.</p>
            capo_network_security_manager.errors.UnknownServiceError: The service returned an error code this client does not model.

        Examples:
            Delete a scope
            Deletes a scope by its ARN. The scope must not be associated with any deployment.

            >>> client.delete_scope(scope_identifier='arn:aws:network-security-manager:us-east-1:123456789012:scope:abc123')
        """

        def _handler(
            req: "OperationRequest[capo_network_security_manager.types.delete_scope_input.DeleteScopeInput]",
        ) -> OperationResponse[None]:
            import capo_network_security_manager._operations.piccolo_customer_api_service.delete_scope

            output, http_response = (
                capo_network_security_manager._operations.piccolo_customer_api_service.delete_scope.delete_scope(
                    req.options, req.input
                )
            )
            return OperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_network_security_manager.types.delete_scope_input.DeleteScopeInput = {
            "scope_identifier": scope_identifier
        }

        response = execute_pipeline(
            OperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        response.response.close()
        return response.output

    def list_scopes(
        self,
        *,
        config_overrides: Optional[NetworkSecurityManagerClientConfig] = None,
        max_results: Optional[
            "capo_network_security_manager.types.max_results.MaxResults"
        ] = None,
        next_token: Optional[
            "capo_network_security_manager.types.next_token.NextToken"
        ] = None,
        status: Optional[
            "capo_network_security_manager.types.entity_status_filter.EntityStatusFilter"
        ] = None,
    ) -> "capo_network_security_manager.types.list_scopes_output.ListScopesOutput":
        """<p>Lists the scopes in the account. You can filter the results by status and page through them using <code>maxResults</code> and <code>nextToken</code>.</p>

        Args:
            max_results: <p>The maximum number of results to return in a single call. Valid range: 1-100. To retrieve the remaining results, use the returned <code>nextToken</code> value in a subsequent call.</p>
            next_token: <p>The token for the next page of results. To retrieve the next page, call the operation again and provide this value. When there are no more results, this value is null.</p>
            status: <p>Filters the results by status: <code>ACTIVE</code>, <code>DRAFT</code>, or <code>DISABLED</code>.</p>

        Raises:
            capo_network_security_manager.errors.access_denied_exception.AccessDeniedException: <p>You do not have sufficient permissions to perform this action.</p>
            capo_network_security_manager.errors.internal_server_exception.InternalServerException: <p>The request processing failed because of an internal error in the service. This is a retryable error.</p>
            capo_network_security_manager.errors.throttling_exception.ThrottlingException: <p>The request was denied because of request throttling. Reduce your request rate and try again.</p>
            capo_network_security_manager.errors.validation_exception.ValidationException: <p>The request failed validation. For details, see the <code>reason</code> and <code>fieldList</code> members of the response.</p>
            capo_network_security_manager.errors.UnknownServiceError: The service returned an error code this client does not model.

        Examples:
            List scopes
            Lists the published scopes in the account, one page at a time.

            >>> client.list_scopes(max_results=10, status='ACTIVE')
        """

        def _handler(
            req: "OperationRequest[capo_network_security_manager.types.list_scopes_input.ListScopesInput]",
        ) -> OperationResponse[
            "capo_network_security_manager.types.list_scopes_output.ListScopesOutput"
        ]:
            import capo_network_security_manager._operations.piccolo_customer_api_service.list_scopes

            output, http_response = (
                capo_network_security_manager._operations.piccolo_customer_api_service.list_scopes.list_scopes(
                    req.options, req.input
                )
            )
            return OperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_network_security_manager.types.list_scopes_input.ListScopesInput = {}
        if max_results is not None:
            input_["max_results"] = max_results
        if next_token is not None:
            input_["next_token"] = next_token
        if status is not None:
            input_["status"] = status

        response = execute_pipeline(
            OperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        response.response.close()
        return response.output

    def iter_list_scopes(
        self,
        *,
        config_overrides: Optional[NetworkSecurityManagerClientConfig] = None,
        max_results: Optional[
            "capo_network_security_manager.types.max_results.MaxResults"
        ] = None,
        next_token: Optional[
            "capo_network_security_manager.types.next_token.NextToken"
        ] = None,
        status: Optional[
            "capo_network_security_manager.types.entity_status_filter.EntityStatusFilter"
        ] = None,
    ) -> "Iterator[capo_network_security_manager.types.scope_summary.ScopeSummary]":
        _token = next_token
        while True:
            _response = self.list_scopes(
                config_overrides=config_overrides,
                max_results=max_results,
                next_token=_token,
                status=status,
            )
            _page = _resolve_path(_response, ("scopes",))
            for _item in _page or []:
                yield _item
            _token = _resolve_path(_response, ("next_token",))
            if not _token:
                break

    def create_scope_snapshot(
        self,
        scope_identifier: "capo_network_security_manager.types.scope_identifier.ScopeIdentifier",
        *,
        config_overrides: Optional[NetworkSecurityManagerClientConfig] = None,
        client_token: Optional[
            "capo_network_security_manager.types.idempotency_token.IdempotencyToken"
        ] = None,
        tags: Optional["capo_network_security_manager.types.tag_map.TagMap"] = None,
    ) -> "capo_network_security_manager.types.create_scope_snapshot_output.CreateScopeSnapshotOutput":
        """<p>Creates a snapshot of the current published version of the specified scope.</p>

        Args:
            scope_identifier: <p>The identifier of the scope. This is the scope's Amazon Resource Name (ARN).</p>
            client_token: <p>A unique, case-sensitive token that you provide to ensure that the operation completes no more than one time. If you retry a request with the same client token and the same parameters, the service returns the result of the original successful request.</p>
            tags: <p>The tags to add to the snapshot when it is created.</p>

        Raises:
            capo_network_security_manager.errors.access_denied_exception.AccessDeniedException: <p>You do not have sufficient permissions to perform this action.</p>
            capo_network_security_manager.errors.conflict_exception.ConflictException: <p>The request conflicts with the current state of the resource. For example, the resource was modified concurrently, or it is in a state that does not allow the requested operation.</p>
            capo_network_security_manager.errors.internal_server_exception.InternalServerException: <p>The request processing failed because of an internal error in the service. This is a retryable error.</p>
            capo_network_security_manager.errors.resource_not_found_exception.ResourceNotFoundException: <p>The specified resource was not found. Verify that the resource identifier is correct and that the resource exists, then try your request again.</p>
            capo_network_security_manager.errors.service_quota_exceeded_exception.ServiceQuotaExceededException: <p>The request would exceed a service quota.</p>
            capo_network_security_manager.errors.throttling_exception.ThrottlingException: <p>The request was denied because of request throttling. Reduce your request rate and try again.</p>
            capo_network_security_manager.errors.validation_exception.ValidationException: <p>The request failed validation. For details, see the <code>reason</code> and <code>fieldList</code> members of the response.</p>
            capo_network_security_manager.errors.UnknownServiceError: The service returned an error code this client does not model.

        Examples:
            Create a scope snapshot
            Creates an immutable snapshot of the current published version of a scope. The snapshot is addressable by a version-qualified ARN.

            >>> client.create_scope_snapshot(scope_identifier='arn:aws:network-security-manager:us-east-1:123456789012:scope:abc123', client_token='550e8400-e29b-41d4-a716-446655440010')
        """

        def _handler(
            req: "OperationRequest[capo_network_security_manager.types.create_scope_snapshot_input.CreateScopeSnapshotInput]",
        ) -> OperationResponse[
            "capo_network_security_manager.types.create_scope_snapshot_output.CreateScopeSnapshotOutput"
        ]:
            import capo_network_security_manager._operations.piccolo_customer_api_service.create_scope_snapshot

            output, http_response = (
                capo_network_security_manager._operations.piccolo_customer_api_service.create_scope_snapshot.create_scope_snapshot(
                    req.options, req.input
                )
            )
            return OperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_network_security_manager.types.create_scope_snapshot_input.CreateScopeSnapshotInput = {
            "scope_identifier": scope_identifier
        }
        if client_token is None:
            client_token = str(uuid.uuid4())
        input_["client_token"] = client_token
        if tags is not None:
            input_["tags"] = tags

        response = execute_pipeline(
            OperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        response.response.close()
        return response.output

    def list_scope_snapshots(
        self,
        scope_identifier: "capo_network_security_manager.types.scope_identifier.ScopeIdentifier",
        *,
        config_overrides: Optional[NetworkSecurityManagerClientConfig] = None,
        max_results: Optional[
            "capo_network_security_manager.types.max_results.MaxResults"
        ] = None,
        next_token: Optional[
            "capo_network_security_manager.types.next_token.NextToken"
        ] = None,
    ) -> "capo_network_security_manager.types.list_scope_snapshots_output.ListScopeSnapshotsOutput":
        """<p>Lists the snapshots of the specified scope.</p>

        Args:
            scope_identifier: <p>The identifier of the scope. This is the scope's Amazon Resource Name (ARN).</p>
            max_results: <p>The maximum number of results to return in a single call. Valid range: 1-100. To retrieve the remaining results, use the returned <code>nextToken</code> value in a subsequent call.</p>
            next_token: <p>The token for the next page of results. To retrieve the next page, call the operation again and provide this value. When there are no more results, this value is null.</p>

        Raises:
            capo_network_security_manager.errors.access_denied_exception.AccessDeniedException: <p>You do not have sufficient permissions to perform this action.</p>
            capo_network_security_manager.errors.internal_server_exception.InternalServerException: <p>The request processing failed because of an internal error in the service. This is a retryable error.</p>
            capo_network_security_manager.errors.resource_not_found_exception.ResourceNotFoundException: <p>The specified resource was not found. Verify that the resource identifier is correct and that the resource exists, then try your request again.</p>
            capo_network_security_manager.errors.throttling_exception.ThrottlingException: <p>The request was denied because of request throttling. Reduce your request rate and try again.</p>
            capo_network_security_manager.errors.validation_exception.ValidationException: <p>The request failed validation. For details, see the <code>reason</code> and <code>fieldList</code> members of the response.</p>
            capo_network_security_manager.errors.UnknownServiceError: The service returned an error code this client does not model.

        Examples:
            List the snapshots of a scope
            Lists the immutable snapshots that have been created for a scope.

            >>> client.list_scope_snapshots(scope_identifier='arn:aws:network-security-manager:us-east-1:123456789012:scope:abc123', max_results=10)
        """

        def _handler(
            req: "OperationRequest[capo_network_security_manager.types.list_scope_snapshots_input.ListScopeSnapshotsInput]",
        ) -> OperationResponse[
            "capo_network_security_manager.types.list_scope_snapshots_output.ListScopeSnapshotsOutput"
        ]:
            import capo_network_security_manager._operations.piccolo_customer_api_service.list_scope_snapshots

            output, http_response = (
                capo_network_security_manager._operations.piccolo_customer_api_service.list_scope_snapshots.list_scope_snapshots(
                    req.options, req.input
                )
            )
            return OperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_network_security_manager.types.list_scope_snapshots_input.ListScopeSnapshotsInput = {
            "scope_identifier": scope_identifier
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

    def iter_list_scope_snapshots(
        self,
        scope_identifier: "capo_network_security_manager.types.scope_identifier.ScopeIdentifier",
        *,
        config_overrides: Optional[NetworkSecurityManagerClientConfig] = None,
        max_results: Optional[
            "capo_network_security_manager.types.max_results.MaxResults"
        ] = None,
        next_token: Optional[
            "capo_network_security_manager.types.next_token.NextToken"
        ] = None,
    ) -> "Iterator[capo_network_security_manager.types.scope_summary.ScopeSummary]":
        _token = next_token
        while True:
            _response = self.list_scope_snapshots(
                scope_identifier,
                config_overrides=config_overrides,
                max_results=max_results,
                next_token=_token,
            )
            _page = _resolve_path(_response, ("snapshots",))
            for _item in _page or []:
                yield _item
            _token = _resolve_path(_response, ("next_token",))
            if not _token:
                break

    def create_template(
        self,
        template_name: "capo_network_security_manager.types.template_name.TemplateName",
        associated_rule_list: "capo_network_security_manager.types.rule_reference_list.RuleReferenceList",
        firewall_type: "capo_network_security_manager.types.template_firewall_type.TemplateFirewallType",
        *,
        config_overrides: Optional[NetworkSecurityManagerClientConfig] = None,
        client_token: Optional[
            "capo_network_security_manager.types.idempotency_token.IdempotencyToken"
        ] = None,
        template_description: Optional[
            "capo_network_security_manager.types.description.Description"
        ] = None,
        is_published: Optional[
            "capo_network_security_manager.types.is_published.IsPublished"
        ] = None,
        tags: Optional["capo_network_security_manager.types.tag_map.TagMap"] = None,
    ) -> "capo_network_security_manager.types.create_template_output.CreateTemplateOutput":
        """<p>Creates a template. A template groups one or more rules to simplify reuse across policies. You can also associate rules with a policy directly, without a template. Use <code>isPublished</code> to create the template in published (<code>ACTIVE</code>) or draft (<code>DRAFT</code>) state.</p>

        Args:
            client_token: <p>A unique, case-sensitive token that you provide to ensure that the operation completes no more than one time. If you retry a request with the same client token and the same parameters, the service returns the result of the original successful request.</p>
            template_name: <p>The name of the template.</p>
            template_description: <p>A description of the template.</p>
            associated_rule_list: <p>The rules associated with the template.</p>
            firewall_type: <p>The firewall type associated with the resource.</p>
            is_published: <p>Specifies whether to publish the resource. When <code>true</code>, the resource is saved in published (<code>ACTIVE</code>) state. When <code>false</code>, it is saved as a draft (<code>DRAFT</code>). Default: <code>true</code>.</p>
            tags: <p>The tags to add to the resource when it is created.</p>

        Raises:
            capo_network_security_manager.errors.access_denied_exception.AccessDeniedException: <p>You do not have sufficient permissions to perform this action.</p>
            capo_network_security_manager.errors.conflict_exception.ConflictException: <p>The request conflicts with the current state of the resource. For example, the resource was modified concurrently, or it is in a state that does not allow the requested operation.</p>
            capo_network_security_manager.errors.internal_server_exception.InternalServerException: <p>The request processing failed because of an internal error in the service. This is a retryable error.</p>
            capo_network_security_manager.errors.service_quota_exceeded_exception.ServiceQuotaExceededException: <p>The request would exceed a service quota.</p>
            capo_network_security_manager.errors.service_unavailable_exception.ServiceUnavailableException: <p>The service is temporarily unavailable. This is a retryable error.</p>
            capo_network_security_manager.errors.tag_policy_violation_exception.TagPolicyViolationException: <p>The request violates a tag policy that is in effect for the account or organization.</p>
            capo_network_security_manager.errors.throttling_exception.ThrottlingException: <p>The request was denied because of request throttling. Reduce your request rate and try again.</p>
            capo_network_security_manager.errors.validation_exception.ValidationException: <p>The request failed validation. For details, see the <code>reason</code> and <code>fieldList</code> members of the response.</p>
            capo_network_security_manager.errors.UnknownServiceError: The service returned an error code this client does not model.

        Examples:
            Create a WAF template
            Creates a new WAF template in published (ACTIVE) state with an associated rule.

            >>> client.create_template(client_token='550e8400-e29b-41d4-a716-446655440004', template_name='standard-waf-template', template_description='Standard WAF template with baseline rule groups', firewall_type='WAF', associated_rule_list=[{'ruleIdentifier': 'arn:aws:network-security-manager:us-east-1:123456789012:rule:abc123'}], is_published=True)
        """

        def _handler(
            req: "OperationRequest[capo_network_security_manager.types.create_template_input.CreateTemplateInput]",
        ) -> OperationResponse[
            "capo_network_security_manager.types.create_template_output.CreateTemplateOutput"
        ]:
            import capo_network_security_manager._operations.piccolo_customer_api_service.create_template

            output, http_response = (
                capo_network_security_manager._operations.piccolo_customer_api_service.create_template.create_template(
                    req.options, req.input
                )
            )
            return OperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_network_security_manager.types.create_template_input.CreateTemplateInput = {
            "template_name": template_name,
            "associated_rule_list": associated_rule_list,
            "firewall_type": firewall_type,
        }
        if client_token is None:
            client_token = str(uuid.uuid4())
        input_["client_token"] = client_token
        if template_description is not None:
            input_["template_description"] = template_description
        if is_published is not None:
            input_["is_published"] = is_published
        if tags is not None:
            input_["tags"] = tags

        response = execute_pipeline(
            OperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        response.response.close()
        return response.output

    def get_template(
        self,
        template_identifier: "capo_network_security_manager.types.template_identifier.TemplateIdentifier",
        *,
        config_overrides: Optional[NetworkSecurityManagerClientConfig] = None,
    ) -> "capo_network_security_manager.types.get_template_output.GetTemplateOutput":
        """<p>Retrieves the details of the specified template.</p>

        Args:
            template_identifier: <p>The identifier of the template. This is the template's Amazon Resource Name (ARN).</p>

        Raises:
            capo_network_security_manager.errors.access_denied_exception.AccessDeniedException: <p>You do not have sufficient permissions to perform this action.</p>
            capo_network_security_manager.errors.internal_server_exception.InternalServerException: <p>The request processing failed because of an internal error in the service. This is a retryable error.</p>
            capo_network_security_manager.errors.resource_not_found_exception.ResourceNotFoundException: <p>The specified resource was not found. Verify that the resource identifier is correct and that the resource exists, then try your request again.</p>
            capo_network_security_manager.errors.throttling_exception.ThrottlingException: <p>The request was denied because of request throttling. Reduce your request rate and try again.</p>
            capo_network_security_manager.errors.validation_exception.ValidationException: <p>The request failed validation. For details, see the <code>reason</code> and <code>fieldList</code> members of the response.</p>
            capo_network_security_manager.errors.UnknownServiceError: The service returned an error code this client does not model.

        Examples:
            Get a template
            Retrieves the current published version of a template by its base ARN, including its associated rules.

            >>> client.get_template(template_identifier='arn:aws:network-security-manager:us-east-1:123456789012:template:xyz789')
        """

        def _handler(
            req: "OperationRequest[capo_network_security_manager.types.get_template_input.GetTemplateInput]",
        ) -> OperationResponse[
            "capo_network_security_manager.types.get_template_output.GetTemplateOutput"
        ]:
            import capo_network_security_manager._operations.piccolo_customer_api_service.get_template

            output, http_response = (
                capo_network_security_manager._operations.piccolo_customer_api_service.get_template.get_template(
                    req.options, req.input
                )
            )
            return OperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_network_security_manager.types.get_template_input.GetTemplateInput = {
            "template_identifier": template_identifier
        }

        response = execute_pipeline(
            OperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        response.response.close()
        return response.output

    def update_template(
        self,
        template_identifier: "capo_network_security_manager.types.template_identifier.TemplateIdentifier",
        update_token: "capo_network_security_manager.types.update_token.UpdateToken",
        is_published: "capo_network_security_manager.types.is_published.IsPublished",
        *,
        config_overrides: Optional[NetworkSecurityManagerClientConfig] = None,
        template_description: Optional[
            "capo_network_security_manager.types.description.Description"
        ] = None,
        associated_rule_list: Optional[
            "capo_network_security_manager.types.rule_reference_list.RuleReferenceList"
        ] = None,
        client_token: Optional[
            "capo_network_security_manager.types.idempotency_token.IdempotencyToken"
        ] = None,
    ) -> "capo_network_security_manager.types.update_template_output.UpdateTemplateOutput":
        """<p>Updates the specified template. To prevent conflicting concurrent updates, provide the current <code>updateToken</code>. Use <code>isPublished</code> to publish the update or keep the template as a draft.</p>

        Args:
            template_identifier: <p>The identifier of the template. This is the template's Amazon Resource Name (ARN).</p>
            update_token: <p>A token used for optimistic concurrency control. Each read and write returns an <code>updateToken</code>. Provide the most recent value on your next update to detect and prevent conflicting concurrent modifications.</p>
            template_description: <p>A description of the template.</p>
            associated_rule_list: <p>The rules associated with the template.</p>
            is_published: <p>Specifies whether to publish the resource. When <code>true</code>, the resource is saved in published (<code>ACTIVE</code>) state. When <code>false</code>, it is saved as a draft (<code>DRAFT</code>).</p>
            client_token: <p>A unique, case-sensitive token that you provide to ensure that the operation completes no more than one time. If you retry a request with the same client token and the same parameters, the service returns the result of the original successful request.</p>

        Raises:
            capo_network_security_manager.errors.access_denied_exception.AccessDeniedException: <p>You do not have sufficient permissions to perform this action.</p>
            capo_network_security_manager.errors.conflict_exception.ConflictException: <p>The request conflicts with the current state of the resource. For example, the resource was modified concurrently, or it is in a state that does not allow the requested operation.</p>
            capo_network_security_manager.errors.internal_server_exception.InternalServerException: <p>The request processing failed because of an internal error in the service. This is a retryable error.</p>
            capo_network_security_manager.errors.resource_not_found_exception.ResourceNotFoundException: <p>The specified resource was not found. Verify that the resource identifier is correct and that the resource exists, then try your request again.</p>
            capo_network_security_manager.errors.service_quota_exceeded_exception.ServiceQuotaExceededException: <p>The request would exceed a service quota.</p>
            capo_network_security_manager.errors.throttling_exception.ThrottlingException: <p>The request was denied because of request throttling. Reduce your request rate and try again.</p>
            capo_network_security_manager.errors.validation_exception.ValidationException: <p>The request failed validation. For details, see the <code>reason</code> and <code>fieldList</code> members of the response.</p>
            capo_network_security_manager.errors.UnknownServiceError: The service returned an error code this client does not model.

        Examples:
            Update a template and publish it
            Updates the template's description and rule associations and publishes the change. The updateToken from the most recent read is required for optimistic locking.

            >>> client.update_template(template_identifier='arn:aws:network-security-manager:us-east-1:123456789012:template:xyz789', update_token='d2e3f4a5-5b6c-4d7e-8f9a-9b0c1d2e3f4a', template_description='Standard WAF template with baseline rule groups - updated', associated_rule_list=[{'ruleIdentifier': 'arn:aws:network-security-manager:us-east-1:123456789012:rule:abc123'}], is_published=True)
        """

        def _handler(
            req: "OperationRequest[capo_network_security_manager.types.update_template_input.UpdateTemplateInput]",
        ) -> OperationResponse[
            "capo_network_security_manager.types.update_template_output.UpdateTemplateOutput"
        ]:
            import capo_network_security_manager._operations.piccolo_customer_api_service.update_template

            output, http_response = (
                capo_network_security_manager._operations.piccolo_customer_api_service.update_template.update_template(
                    req.options, req.input
                )
            )
            return OperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_network_security_manager.types.update_template_input.UpdateTemplateInput = {
            "template_identifier": template_identifier,
            "update_token": update_token,
            "is_published": is_published,
        }
        if template_description is not None:
            input_["template_description"] = template_description
        if associated_rule_list is not None:
            input_["associated_rule_list"] = associated_rule_list
        if client_token is None:
            client_token = str(uuid.uuid4())
        input_["client_token"] = client_token

        response = execute_pipeline(
            OperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        response.response.close()
        return response.output

    def delete_template(
        self,
        template_identifier: "capo_network_security_manager.types.template_identifier.TemplateIdentifier",
        *,
        config_overrides: Optional[NetworkSecurityManagerClientConfig] = None,
    ) -> None:
        """<p>Deletes the specified template.</p>

        Args:
            template_identifier: <p>The identifier of the template. This is the template's Amazon Resource Name (ARN).</p>

        Raises:
            capo_network_security_manager.errors.access_denied_exception.AccessDeniedException: <p>You do not have sufficient permissions to perform this action.</p>
            capo_network_security_manager.errors.conflict_exception.ConflictException: <p>The request conflicts with the current state of the resource. For example, the resource was modified concurrently, or it is in a state that does not allow the requested operation.</p>
            capo_network_security_manager.errors.internal_server_exception.InternalServerException: <p>The request processing failed because of an internal error in the service. This is a retryable error.</p>
            capo_network_security_manager.errors.throttling_exception.ThrottlingException: <p>The request was denied because of request throttling. Reduce your request rate and try again.</p>
            capo_network_security_manager.errors.validation_exception.ValidationException: <p>The request failed validation. For details, see the <code>reason</code> and <code>fieldList</code> members of the response.</p>
            capo_network_security_manager.errors.UnknownServiceError: The service returned an error code this client does not model.

        Examples:
            Delete a template
            Deletes a template by its ARN. The template must not be associated with any policy.

            >>> client.delete_template(template_identifier='arn:aws:network-security-manager:us-east-1:123456789012:template:xyz789')
        """

        def _handler(
            req: "OperationRequest[capo_network_security_manager.types.delete_template_input.DeleteTemplateInput]",
        ) -> OperationResponse[None]:
            import capo_network_security_manager._operations.piccolo_customer_api_service.delete_template

            output, http_response = (
                capo_network_security_manager._operations.piccolo_customer_api_service.delete_template.delete_template(
                    req.options, req.input
                )
            )
            return OperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_network_security_manager.types.delete_template_input.DeleteTemplateInput = {
            "template_identifier": template_identifier
        }

        response = execute_pipeline(
            OperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        response.response.close()
        return response.output

    def list_templates(
        self,
        *,
        config_overrides: Optional[NetworkSecurityManagerClientConfig] = None,
        max_results: Optional[
            "capo_network_security_manager.types.max_results.MaxResults"
        ] = None,
        next_token: Optional[
            "capo_network_security_manager.types.next_token.NextToken"
        ] = None,
        status: Optional[
            "capo_network_security_manager.types.entity_status_filter.EntityStatusFilter"
        ] = None,
    ) -> (
        "capo_network_security_manager.types.list_templates_output.ListTemplatesOutput"
    ):
        """<p>Lists the templates in the account. You can filter the results by status and page through them using <code>maxResults</code> and <code>nextToken</code>.</p>

        Args:
            max_results: <p>The maximum number of results to return in a single call. Valid range: 1-100. To retrieve the remaining results, use the returned <code>nextToken</code> value in a subsequent call.</p>
            next_token: <p>The token for the next page of results. To retrieve the next page, call the operation again and provide this value. When there are no more results, this value is null.</p>
            status: <p>Filters the results by status, either <code>ACTIVE</code> or <code>DRAFT</code>.</p>

        Raises:
            capo_network_security_manager.errors.access_denied_exception.AccessDeniedException: <p>You do not have sufficient permissions to perform this action.</p>
            capo_network_security_manager.errors.internal_server_exception.InternalServerException: <p>The request processing failed because of an internal error in the service. This is a retryable error.</p>
            capo_network_security_manager.errors.throttling_exception.ThrottlingException: <p>The request was denied because of request throttling. Reduce your request rate and try again.</p>
            capo_network_security_manager.errors.validation_exception.ValidationException: <p>The request failed validation. For details, see the <code>reason</code> and <code>fieldList</code> members of the response.</p>
            capo_network_security_manager.errors.UnknownServiceError: The service returned an error code this client does not model.

        Examples:
            List templates
            Lists the published templates in the account, one page at a time.

            >>> client.list_templates(max_results=10, status='ACTIVE')
        """

        def _handler(
            req: "OperationRequest[capo_network_security_manager.types.list_templates_input.ListTemplatesInput]",
        ) -> OperationResponse[
            "capo_network_security_manager.types.list_templates_output.ListTemplatesOutput"
        ]:
            import capo_network_security_manager._operations.piccolo_customer_api_service.list_templates

            output, http_response = (
                capo_network_security_manager._operations.piccolo_customer_api_service.list_templates.list_templates(
                    req.options, req.input
                )
            )
            return OperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_network_security_manager.types.list_templates_input.ListTemplatesInput = {}
        if max_results is not None:
            input_["max_results"] = max_results
        if next_token is not None:
            input_["next_token"] = next_token
        if status is not None:
            input_["status"] = status

        response = execute_pipeline(
            OperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        response.response.close()
        return response.output

    def iter_list_templates(
        self,
        *,
        config_overrides: Optional[NetworkSecurityManagerClientConfig] = None,
        max_results: Optional[
            "capo_network_security_manager.types.max_results.MaxResults"
        ] = None,
        next_token: Optional[
            "capo_network_security_manager.types.next_token.NextToken"
        ] = None,
        status: Optional[
            "capo_network_security_manager.types.entity_status_filter.EntityStatusFilter"
        ] = None,
    ) -> (
        "Iterator[capo_network_security_manager.types.template_summary.TemplateSummary]"
    ):
        _token = next_token
        while True:
            _response = self.list_templates(
                config_overrides=config_overrides,
                max_results=max_results,
                next_token=_token,
                status=status,
            )
            _page = _resolve_path(_response, ("templates",))
            for _item in _page or []:
                yield _item
            _token = _resolve_path(_response, ("next_token",))
            if not _token:
                break

    def create_template_snapshot(
        self,
        template_identifier: "capo_network_security_manager.types.template_identifier.TemplateIdentifier",
        *,
        config_overrides: Optional[NetworkSecurityManagerClientConfig] = None,
        client_token: Optional[
            "capo_network_security_manager.types.idempotency_token.IdempotencyToken"
        ] = None,
        tags: Optional["capo_network_security_manager.types.tag_map.TagMap"] = None,
    ) -> "capo_network_security_manager.types.create_template_snapshot_output.CreateTemplateSnapshotOutput":
        """<p>Creates a snapshot of the current published version of the specified template.</p>

        Args:
            template_identifier: <p>The identifier of the template. This is the template's Amazon Resource Name (ARN).</p>
            client_token: <p>A unique, case-sensitive token that you provide to ensure that the operation completes no more than one time. If you retry a request with the same client token and the same parameters, the service returns the result of the original successful request.</p>
            tags: <p>The tags to add to the snapshot when it is created.</p>

        Raises:
            capo_network_security_manager.errors.access_denied_exception.AccessDeniedException: <p>You do not have sufficient permissions to perform this action.</p>
            capo_network_security_manager.errors.conflict_exception.ConflictException: <p>The request conflicts with the current state of the resource. For example, the resource was modified concurrently, or it is in a state that does not allow the requested operation.</p>
            capo_network_security_manager.errors.internal_server_exception.InternalServerException: <p>The request processing failed because of an internal error in the service. This is a retryable error.</p>
            capo_network_security_manager.errors.resource_not_found_exception.ResourceNotFoundException: <p>The specified resource was not found. Verify that the resource identifier is correct and that the resource exists, then try your request again.</p>
            capo_network_security_manager.errors.service_quota_exceeded_exception.ServiceQuotaExceededException: <p>The request would exceed a service quota.</p>
            capo_network_security_manager.errors.throttling_exception.ThrottlingException: <p>The request was denied because of request throttling. Reduce your request rate and try again.</p>
            capo_network_security_manager.errors.validation_exception.ValidationException: <p>The request failed validation. For details, see the <code>reason</code> and <code>fieldList</code> members of the response.</p>
            capo_network_security_manager.errors.UnknownServiceError: The service returned an error code this client does not model.

        Examples:
            Create a template snapshot
            Creates an immutable snapshot of the current published version of a template. The snapshot is addressable by a version-qualified ARN.

            >>> client.create_template_snapshot(template_identifier='arn:aws:network-security-manager:us-east-1:123456789012:template:xyz789', client_token='550e8400-e29b-41d4-a716-446655440012')
        """

        def _handler(
            req: "OperationRequest[capo_network_security_manager.types.create_template_snapshot_input.CreateTemplateSnapshotInput]",
        ) -> OperationResponse[
            "capo_network_security_manager.types.create_template_snapshot_output.CreateTemplateSnapshotOutput"
        ]:
            import capo_network_security_manager._operations.piccolo_customer_api_service.create_template_snapshot

            output, http_response = (
                capo_network_security_manager._operations.piccolo_customer_api_service.create_template_snapshot.create_template_snapshot(
                    req.options, req.input
                )
            )
            return OperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_network_security_manager.types.create_template_snapshot_input.CreateTemplateSnapshotInput = {
            "template_identifier": template_identifier
        }
        if client_token is None:
            client_token = str(uuid.uuid4())
        input_["client_token"] = client_token
        if tags is not None:
            input_["tags"] = tags

        response = execute_pipeline(
            OperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        response.response.close()
        return response.output

    def list_template_snapshots(
        self,
        template_identifier: "capo_network_security_manager.types.template_identifier.TemplateIdentifier",
        *,
        config_overrides: Optional[NetworkSecurityManagerClientConfig] = None,
        max_results: Optional[
            "capo_network_security_manager.types.max_results.MaxResults"
        ] = None,
        next_token: Optional[
            "capo_network_security_manager.types.next_token.NextToken"
        ] = None,
    ) -> "capo_network_security_manager.types.list_template_snapshots_output.ListTemplateSnapshotsOutput":
        """<p>Lists the snapshots of the specified template.</p>

        Args:
            template_identifier: <p>The identifier of the template. This is the template's Amazon Resource Name (ARN).</p>
            max_results: <p>The maximum number of results to return in a single call. Valid range: 1-100. To retrieve the remaining results, use the returned <code>nextToken</code> value in a subsequent call.</p>
            next_token: <p>The token for the next page of results. To retrieve the next page, call the operation again and provide this value. When there are no more results, this value is null.</p>

        Raises:
            capo_network_security_manager.errors.access_denied_exception.AccessDeniedException: <p>You do not have sufficient permissions to perform this action.</p>
            capo_network_security_manager.errors.internal_server_exception.InternalServerException: <p>The request processing failed because of an internal error in the service. This is a retryable error.</p>
            capo_network_security_manager.errors.resource_not_found_exception.ResourceNotFoundException: <p>The specified resource was not found. Verify that the resource identifier is correct and that the resource exists, then try your request again.</p>
            capo_network_security_manager.errors.throttling_exception.ThrottlingException: <p>The request was denied because of request throttling. Reduce your request rate and try again.</p>
            capo_network_security_manager.errors.validation_exception.ValidationException: <p>The request failed validation. For details, see the <code>reason</code> and <code>fieldList</code> members of the response.</p>
            capo_network_security_manager.errors.UnknownServiceError: The service returned an error code this client does not model.

        Examples:
            List the snapshots of a template
            Lists the immutable snapshots that have been created for a template.

            >>> client.list_template_snapshots(template_identifier='arn:aws:network-security-manager:us-east-1:123456789012:template:xyz789', max_results=10)
        """

        def _handler(
            req: "OperationRequest[capo_network_security_manager.types.list_template_snapshots_input.ListTemplateSnapshotsInput]",
        ) -> OperationResponse[
            "capo_network_security_manager.types.list_template_snapshots_output.ListTemplateSnapshotsOutput"
        ]:
            import capo_network_security_manager._operations.piccolo_customer_api_service.list_template_snapshots

            output, http_response = (
                capo_network_security_manager._operations.piccolo_customer_api_service.list_template_snapshots.list_template_snapshots(
                    req.options, req.input
                )
            )
            return OperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_network_security_manager.types.list_template_snapshots_input.ListTemplateSnapshotsInput = {
            "template_identifier": template_identifier
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

    def iter_list_template_snapshots(
        self,
        template_identifier: "capo_network_security_manager.types.template_identifier.TemplateIdentifier",
        *,
        config_overrides: Optional[NetworkSecurityManagerClientConfig] = None,
        max_results: Optional[
            "capo_network_security_manager.types.max_results.MaxResults"
        ] = None,
        next_token: Optional[
            "capo_network_security_manager.types.next_token.NextToken"
        ] = None,
    ) -> (
        "Iterator[capo_network_security_manager.types.template_summary.TemplateSummary]"
    ):
        _token = next_token
        while True:
            _response = self.list_template_snapshots(
                template_identifier,
                config_overrides=config_overrides,
                max_results=max_results,
                next_token=_token,
            )
            _page = _resolve_path(_response, ("snapshots",))
            for _item in _page or []:
                yield _item
            _token = _resolve_path(_response, ("next_token",))
            if not _token:
                break

    def __enter__(self) -> Self:
        return self

    def __exit__(self, exc_type: Any, exc: Any, tb: Any):
        self._client.close()
