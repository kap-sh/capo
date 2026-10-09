"""Generated from Smithy shape ``com.amazonaws.cloudsearch#A9SearchCloudConfigService2013``."""

import warnings
from typing import TYPE_CHECKING, Any, Iterable, Optional

from typing_extensions import Self, TypedDict
from zapros import BaseHandler, Client

import capo_cloudsearch._auth._signers
import capo_cloudsearch._auth._sigv4
from capo_cloudsearch._auth._identity import Credentials
from capo_cloudsearch._auth._providers import (
    CredentialsProvider,
    IdentityProvider,
    StaticAwsCredentialsProvider,
    default_aws_credentials_chain,
)
from capo_cloudsearch._auth._zapros_handler import AuthMiddleware
from capo_cloudsearch._services._aws_config import aws_config
from capo_cloudsearch._services._pipeline import (
    Interceptor,
    OperationOptions,
    OperationRequest,
    OperationResponse,
    execute_pipeline,
    retry,
)

if TYPE_CHECKING:
    import capo_cloudsearch.types.analysis_scheme
    import capo_cloudsearch.types.boolean
    import capo_cloudsearch.types.build_suggesters_request
    import capo_cloudsearch.types.build_suggesters_response
    import capo_cloudsearch.types.create_domain_request
    import capo_cloudsearch.types.create_domain_response
    import capo_cloudsearch.types.define_analysis_scheme_request
    import capo_cloudsearch.types.define_analysis_scheme_response
    import capo_cloudsearch.types.define_expression_request
    import capo_cloudsearch.types.define_expression_response
    import capo_cloudsearch.types.define_index_field_request
    import capo_cloudsearch.types.define_index_field_response
    import capo_cloudsearch.types.define_suggester_request
    import capo_cloudsearch.types.define_suggester_response
    import capo_cloudsearch.types.delete_analysis_scheme_request
    import capo_cloudsearch.types.delete_analysis_scheme_response
    import capo_cloudsearch.types.delete_domain_request
    import capo_cloudsearch.types.delete_domain_response
    import capo_cloudsearch.types.delete_expression_request
    import capo_cloudsearch.types.delete_expression_response
    import capo_cloudsearch.types.delete_index_field_request
    import capo_cloudsearch.types.delete_index_field_response
    import capo_cloudsearch.types.delete_suggester_request
    import capo_cloudsearch.types.delete_suggester_response
    import capo_cloudsearch.types.describe_analysis_schemes_request
    import capo_cloudsearch.types.describe_analysis_schemes_response
    import capo_cloudsearch.types.describe_availability_options_request
    import capo_cloudsearch.types.describe_availability_options_response
    import capo_cloudsearch.types.describe_domain_endpoint_options_request
    import capo_cloudsearch.types.describe_domain_endpoint_options_response
    import capo_cloudsearch.types.describe_domains_request
    import capo_cloudsearch.types.describe_domains_response
    import capo_cloudsearch.types.describe_expressions_request
    import capo_cloudsearch.types.describe_expressions_response
    import capo_cloudsearch.types.describe_index_fields_request
    import capo_cloudsearch.types.describe_index_fields_response
    import capo_cloudsearch.types.describe_scaling_parameters_request
    import capo_cloudsearch.types.describe_scaling_parameters_response
    import capo_cloudsearch.types.describe_service_access_policies_request
    import capo_cloudsearch.types.describe_service_access_policies_response
    import capo_cloudsearch.types.describe_suggesters_request
    import capo_cloudsearch.types.describe_suggesters_response
    import capo_cloudsearch.types.domain_endpoint_options
    import capo_cloudsearch.types.domain_name
    import capo_cloudsearch.types.domain_name_list
    import capo_cloudsearch.types.dynamic_field_name
    import capo_cloudsearch.types.dynamic_field_name_list
    import capo_cloudsearch.types.expression
    import capo_cloudsearch.types.index_documents_request
    import capo_cloudsearch.types.index_documents_response
    import capo_cloudsearch.types.index_field
    import capo_cloudsearch.types.list_domain_names_response
    import capo_cloudsearch.types.policy_document
    import capo_cloudsearch.types.scaling_parameters
    import capo_cloudsearch.types.standard_name
    import capo_cloudsearch.types.standard_name_list
    import capo_cloudsearch.types.suggester
    import capo_cloudsearch.types.update_availability_options_request
    import capo_cloudsearch.types.update_availability_options_response
    import capo_cloudsearch.types.update_domain_endpoint_options_request
    import capo_cloudsearch.types.update_domain_endpoint_options_response
    import capo_cloudsearch.types.update_scaling_parameters_request
    import capo_cloudsearch.types.update_scaling_parameters_response
    import capo_cloudsearch.types.update_service_access_policies_request
    import capo_cloudsearch.types.update_service_access_policies_response


class CloudSearchClientConfig(TypedDict, total=False, closed=True):
    operation_interceptors: Iterable[Interceptor[Any, Any]]
    retry_max_attempts: int | None
    region: str | None
    use_dual_stack: bool | None
    use_fips: bool | None
    endpoint: str | None
    credentials_provider: IdentityProvider[Credentials] | None
    anonymous: bool | None


class CloudSearchClient:
    """A client for the ``CloudSearch`` service.

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
        self._config = CloudSearchClientConfig(
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
        self, config_overrides: Optional[CloudSearchClientConfig] = None
    ) -> tuple[Iterable[Interceptor[Any, Any]], OperationOptions]:
        overrides: CloudSearchClientConfig = config_overrides or {}
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

    def build_suggesters(
        self,
        domain_name: "capo_cloudsearch.types.domain_name.DomainName",
        *,
        config_overrides: Optional[CloudSearchClientConfig] = None,
    ) -> "capo_cloudsearch.types.build_suggesters_response.BuildSuggestersResponse":
        """<p>Indexes the search suggestions. For more information, see <a href="http://docs.aws.amazon.com/cloudsearch/latest/developerguide/getting-suggestions.html#configuring-suggesters">Configuring Suggesters</a> in the <i>Amazon CloudSearch Developer Guide</i>.</p>

        Raises:
            capo_cloudsearch.errors.base_exception.BaseException: <p>An error occurred while processing the request.</p>
            capo_cloudsearch.errors.internal_exception.InternalException: <p>An internal error occurred while processing the request. If this problem persists, report an issue from the <a href="http://status.aws.amazon.com/" target="_blank">Service Health Dashboard</a>.</p>
            capo_cloudsearch.errors.resource_not_found_exception.ResourceNotFoundException: <p>The request was rejected because it attempted to reference a resource that does not exist.</p>
            capo_cloudsearch.errors.validation_exception.ValidationException: <p>The request was rejected because it has invalid parameters.</p>
            capo_cloudsearch.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        def _handler(
            req: "OperationRequest[capo_cloudsearch.types.build_suggesters_request.BuildSuggestersRequest]",
        ) -> OperationResponse[
            "capo_cloudsearch.types.build_suggesters_response.BuildSuggestersResponse"
        ]:
            import capo_cloudsearch._operations.a9_search_cloud_config_service2013.build_suggesters

            output, http_response = (
                capo_cloudsearch._operations.a9_search_cloud_config_service2013.build_suggesters.build_suggesters(
                    req.options, req.input
                )
            )
            return OperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_cloudsearch.types.build_suggesters_request.BuildSuggestersRequest = {
            "domain_name": domain_name
        }

        response = execute_pipeline(
            OperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        response.response.close()
        return response.output

    def create_domain(
        self,
        domain_name: "capo_cloudsearch.types.domain_name.DomainName",
        *,
        config_overrides: Optional[CloudSearchClientConfig] = None,
    ) -> "capo_cloudsearch.types.create_domain_response.CreateDomainResponse":
        """<p>Creates a new search domain. For more information, see <a href="http://docs.aws.amazon.com/cloudsearch/latest/developerguide/creating-domains.html" target="_blank">Creating a Search Domain</a> in the <i>Amazon CloudSearch Developer Guide</i>.</p>

        Args:
            domain_name: <p>A name for the domain you are creating. Allowed characters are a-z (lower-case letters), 0-9, and hyphen (-). Domain names must start with a letter or number and be at least 3 and no more than 28 characters long.</p>

        Raises:
            capo_cloudsearch.errors.base_exception.BaseException: <p>An error occurred while processing the request.</p>
            capo_cloudsearch.errors.internal_exception.InternalException: <p>An internal error occurred while processing the request. If this problem persists, report an issue from the <a href="http://status.aws.amazon.com/" target="_blank">Service Health Dashboard</a>.</p>
            capo_cloudsearch.errors.limit_exceeded_exception.LimitExceededException: <p>The request was rejected because a resource limit has already been met.</p>
            capo_cloudsearch.errors.resource_already_exists_exception.ResourceAlreadyExistsException: <p>The request was rejected because it attempted to create a resource that already exists.</p>
            capo_cloudsearch.errors.validation_exception.ValidationException: <p>The request was rejected because it has invalid parameters.</p>
            capo_cloudsearch.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        def _handler(
            req: "OperationRequest[capo_cloudsearch.types.create_domain_request.CreateDomainRequest]",
        ) -> OperationResponse[
            "capo_cloudsearch.types.create_domain_response.CreateDomainResponse"
        ]:
            import capo_cloudsearch._operations.a9_search_cloud_config_service2013.create_domain

            output, http_response = (
                capo_cloudsearch._operations.a9_search_cloud_config_service2013.create_domain.create_domain(
                    req.options, req.input
                )
            )
            return OperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_cloudsearch.types.create_domain_request.CreateDomainRequest = {
            "domain_name": domain_name
        }

        response = execute_pipeline(
            OperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        response.response.close()
        return response.output

    def define_analysis_scheme(
        self,
        domain_name: "capo_cloudsearch.types.domain_name.DomainName",
        analysis_scheme: "capo_cloudsearch.types.analysis_scheme.AnalysisScheme",
        *,
        config_overrides: Optional[CloudSearchClientConfig] = None,
    ) -> "capo_cloudsearch.types.define_analysis_scheme_response.DefineAnalysisSchemeResponse":
        """<p>Configures an analysis scheme that can be applied to a <code>text</code> or <code>text-array</code> field to define language-specific text processing options. For more information, see <a href="http://docs.aws.amazon.com/cloudsearch/latest/developerguide/configuring-analysis-schemes.html" target="_blank">Configuring Analysis Schemes</a> in the <i>Amazon CloudSearch Developer Guide</i>.</p>

        Raises:
            capo_cloudsearch.errors.base_exception.BaseException: <p>An error occurred while processing the request.</p>
            capo_cloudsearch.errors.internal_exception.InternalException: <p>An internal error occurred while processing the request. If this problem persists, report an issue from the <a href="http://status.aws.amazon.com/" target="_blank">Service Health Dashboard</a>.</p>
            capo_cloudsearch.errors.invalid_type_exception.InvalidTypeException: <p>The request was rejected because it specified an invalid type definition.</p>
            capo_cloudsearch.errors.limit_exceeded_exception.LimitExceededException: <p>The request was rejected because a resource limit has already been met.</p>
            capo_cloudsearch.errors.resource_not_found_exception.ResourceNotFoundException: <p>The request was rejected because it attempted to reference a resource that does not exist.</p>
            capo_cloudsearch.errors.validation_exception.ValidationException: <p>The request was rejected because it has invalid parameters.</p>
            capo_cloudsearch.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        def _handler(
            req: "OperationRequest[capo_cloudsearch.types.define_analysis_scheme_request.DefineAnalysisSchemeRequest]",
        ) -> OperationResponse[
            "capo_cloudsearch.types.define_analysis_scheme_response.DefineAnalysisSchemeResponse"
        ]:
            import capo_cloudsearch._operations.a9_search_cloud_config_service2013.define_analysis_scheme

            output, http_response = (
                capo_cloudsearch._operations.a9_search_cloud_config_service2013.define_analysis_scheme.define_analysis_scheme(
                    req.options, req.input
                )
            )
            return OperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_cloudsearch.types.define_analysis_scheme_request.DefineAnalysisSchemeRequest = {
            "domain_name": domain_name,
            "analysis_scheme": analysis_scheme,
        }

        response = execute_pipeline(
            OperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        response.response.close()
        return response.output

    def define_expression(
        self,
        domain_name: "capo_cloudsearch.types.domain_name.DomainName",
        expression: "capo_cloudsearch.types.expression.Expression",
        *,
        config_overrides: Optional[CloudSearchClientConfig] = None,
    ) -> "capo_cloudsearch.types.define_expression_response.DefineExpressionResponse":
        """<p>Configures an <code><a>Expression</a></code> for the search domain. Used to create new expressions and modify existing ones. If the expression exists, the new configuration replaces the old one. For more information, see <a href="http://docs.aws.amazon.com/cloudsearch/latest/developerguide/configuring-expressions.html" target="_blank">Configuring Expressions</a> in the <i>Amazon CloudSearch Developer Guide</i>.</p>

        Raises:
            capo_cloudsearch.errors.base_exception.BaseException: <p>An error occurred while processing the request.</p>
            capo_cloudsearch.errors.internal_exception.InternalException: <p>An internal error occurred while processing the request. If this problem persists, report an issue from the <a href="http://status.aws.amazon.com/" target="_blank">Service Health Dashboard</a>.</p>
            capo_cloudsearch.errors.invalid_type_exception.InvalidTypeException: <p>The request was rejected because it specified an invalid type definition.</p>
            capo_cloudsearch.errors.limit_exceeded_exception.LimitExceededException: <p>The request was rejected because a resource limit has already been met.</p>
            capo_cloudsearch.errors.resource_not_found_exception.ResourceNotFoundException: <p>The request was rejected because it attempted to reference a resource that does not exist.</p>
            capo_cloudsearch.errors.validation_exception.ValidationException: <p>The request was rejected because it has invalid parameters.</p>
            capo_cloudsearch.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        def _handler(
            req: "OperationRequest[capo_cloudsearch.types.define_expression_request.DefineExpressionRequest]",
        ) -> OperationResponse[
            "capo_cloudsearch.types.define_expression_response.DefineExpressionResponse"
        ]:
            import capo_cloudsearch._operations.a9_search_cloud_config_service2013.define_expression

            output, http_response = (
                capo_cloudsearch._operations.a9_search_cloud_config_service2013.define_expression.define_expression(
                    req.options, req.input
                )
            )
            return OperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_cloudsearch.types.define_expression_request.DefineExpressionRequest = {
            "domain_name": domain_name,
            "expression": expression,
        }

        response = execute_pipeline(
            OperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        response.response.close()
        return response.output

    def define_index_field(
        self,
        domain_name: "capo_cloudsearch.types.domain_name.DomainName",
        index_field: "capo_cloudsearch.types.index_field.IndexField",
        *,
        config_overrides: Optional[CloudSearchClientConfig] = None,
    ) -> "capo_cloudsearch.types.define_index_field_response.DefineIndexFieldResponse":
        """<p>Configures an <code><a>IndexField</a></code> for the search domain. Used to create new fields and modify existing ones. You must specify the name of the domain you are configuring and an index field configuration. The index field configuration specifies a unique name, the index field type, and the options you want to configure for the field. The options you can specify depend on the <code><a>IndexFieldType</a></code>. If the field exists, the new configuration replaces the old one. For more information, see <a href="http://docs.aws.amazon.com/cloudsearch/latest/developerguide/configuring-index-fields.html" target="_blank">Configuring Index Fields</a> in the <i>Amazon CloudSearch Developer Guide</i>. </p>

        Args:
            index_field: <p>The index field and field options you want to configure. </p>

        Raises:
            capo_cloudsearch.errors.base_exception.BaseException: <p>An error occurred while processing the request.</p>
            capo_cloudsearch.errors.internal_exception.InternalException: <p>An internal error occurred while processing the request. If this problem persists, report an issue from the <a href="http://status.aws.amazon.com/" target="_blank">Service Health Dashboard</a>.</p>
            capo_cloudsearch.errors.invalid_type_exception.InvalidTypeException: <p>The request was rejected because it specified an invalid type definition.</p>
            capo_cloudsearch.errors.limit_exceeded_exception.LimitExceededException: <p>The request was rejected because a resource limit has already been met.</p>
            capo_cloudsearch.errors.resource_not_found_exception.ResourceNotFoundException: <p>The request was rejected because it attempted to reference a resource that does not exist.</p>
            capo_cloudsearch.errors.validation_exception.ValidationException: <p>The request was rejected because it has invalid parameters.</p>
            capo_cloudsearch.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        def _handler(
            req: "OperationRequest[capo_cloudsearch.types.define_index_field_request.DefineIndexFieldRequest]",
        ) -> OperationResponse[
            "capo_cloudsearch.types.define_index_field_response.DefineIndexFieldResponse"
        ]:
            import capo_cloudsearch._operations.a9_search_cloud_config_service2013.define_index_field

            output, http_response = (
                capo_cloudsearch._operations.a9_search_cloud_config_service2013.define_index_field.define_index_field(
                    req.options, req.input
                )
            )
            return OperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_cloudsearch.types.define_index_field_request.DefineIndexFieldRequest = {
            "domain_name": domain_name,
            "index_field": index_field,
        }

        response = execute_pipeline(
            OperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        response.response.close()
        return response.output

    def define_suggester(
        self,
        domain_name: "capo_cloudsearch.types.domain_name.DomainName",
        suggester: "capo_cloudsearch.types.suggester.Suggester",
        *,
        config_overrides: Optional[CloudSearchClientConfig] = None,
    ) -> "capo_cloudsearch.types.define_suggester_response.DefineSuggesterResponse":
        """<p>Configures a suggester for a domain. A suggester enables you to display possible matches before users finish typing their queries. When you configure a suggester, you must specify the name of the text field you want to search for possible matches and a unique name for the suggester. For more information, see <a href="http://docs.aws.amazon.com/cloudsearch/latest/developerguide/getting-suggestions.html" target="_blank">Getting Search Suggestions</a> in the <i>Amazon CloudSearch Developer Guide</i>.</p>

        Raises:
            capo_cloudsearch.errors.base_exception.BaseException: <p>An error occurred while processing the request.</p>
            capo_cloudsearch.errors.internal_exception.InternalException: <p>An internal error occurred while processing the request. If this problem persists, report an issue from the <a href="http://status.aws.amazon.com/" target="_blank">Service Health Dashboard</a>.</p>
            capo_cloudsearch.errors.invalid_type_exception.InvalidTypeException: <p>The request was rejected because it specified an invalid type definition.</p>
            capo_cloudsearch.errors.limit_exceeded_exception.LimitExceededException: <p>The request was rejected because a resource limit has already been met.</p>
            capo_cloudsearch.errors.resource_not_found_exception.ResourceNotFoundException: <p>The request was rejected because it attempted to reference a resource that does not exist.</p>
            capo_cloudsearch.errors.validation_exception.ValidationException: <p>The request was rejected because it has invalid parameters.</p>
            capo_cloudsearch.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        def _handler(
            req: "OperationRequest[capo_cloudsearch.types.define_suggester_request.DefineSuggesterRequest]",
        ) -> OperationResponse[
            "capo_cloudsearch.types.define_suggester_response.DefineSuggesterResponse"
        ]:
            import capo_cloudsearch._operations.a9_search_cloud_config_service2013.define_suggester

            output, http_response = (
                capo_cloudsearch._operations.a9_search_cloud_config_service2013.define_suggester.define_suggester(
                    req.options, req.input
                )
            )
            return OperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_cloudsearch.types.define_suggester_request.DefineSuggesterRequest = {
            "domain_name": domain_name,
            "suggester": suggester,
        }

        response = execute_pipeline(
            OperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        response.response.close()
        return response.output

    def delete_analysis_scheme(
        self,
        domain_name: "capo_cloudsearch.types.domain_name.DomainName",
        analysis_scheme_name: "capo_cloudsearch.types.standard_name.StandardName",
        *,
        config_overrides: Optional[CloudSearchClientConfig] = None,
    ) -> "capo_cloudsearch.types.delete_analysis_scheme_response.DeleteAnalysisSchemeResponse":
        """<p>Deletes an analysis scheme. For more information, see <a href="http://docs.aws.amazon.com/cloudsearch/latest/developerguide/configuring-analysis-schemes.html" target="_blank">Configuring Analysis Schemes</a> in the <i>Amazon CloudSearch Developer Guide</i>. </p>

        Args:
            analysis_scheme_name: <p>The name of the analysis scheme you want to delete.</p>

        Raises:
            capo_cloudsearch.errors.base_exception.BaseException: <p>An error occurred while processing the request.</p>
            capo_cloudsearch.errors.internal_exception.InternalException: <p>An internal error occurred while processing the request. If this problem persists, report an issue from the <a href="http://status.aws.amazon.com/" target="_blank">Service Health Dashboard</a>.</p>
            capo_cloudsearch.errors.invalid_type_exception.InvalidTypeException: <p>The request was rejected because it specified an invalid type definition.</p>
            capo_cloudsearch.errors.resource_not_found_exception.ResourceNotFoundException: <p>The request was rejected because it attempted to reference a resource that does not exist.</p>
            capo_cloudsearch.errors.validation_exception.ValidationException: <p>The request was rejected because it has invalid parameters.</p>
            capo_cloudsearch.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        def _handler(
            req: "OperationRequest[capo_cloudsearch.types.delete_analysis_scheme_request.DeleteAnalysisSchemeRequest]",
        ) -> OperationResponse[
            "capo_cloudsearch.types.delete_analysis_scheme_response.DeleteAnalysisSchemeResponse"
        ]:
            import capo_cloudsearch._operations.a9_search_cloud_config_service2013.delete_analysis_scheme

            output, http_response = (
                capo_cloudsearch._operations.a9_search_cloud_config_service2013.delete_analysis_scheme.delete_analysis_scheme(
                    req.options, req.input
                )
            )
            return OperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_cloudsearch.types.delete_analysis_scheme_request.DeleteAnalysisSchemeRequest = {
            "domain_name": domain_name,
            "analysis_scheme_name": analysis_scheme_name,
        }

        response = execute_pipeline(
            OperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        response.response.close()
        return response.output

    def delete_domain(
        self,
        domain_name: "capo_cloudsearch.types.domain_name.DomainName",
        *,
        config_overrides: Optional[CloudSearchClientConfig] = None,
    ) -> "capo_cloudsearch.types.delete_domain_response.DeleteDomainResponse":
        """<p>Permanently deletes a search domain and all of its data. Once a domain has been deleted, it cannot be recovered. For more information, see <a href="http://docs.aws.amazon.com/cloudsearch/latest/developerguide/deleting-domains.html" target="_blank">Deleting a Search Domain</a> in the <i>Amazon CloudSearch Developer Guide</i>. </p>

        Args:
            domain_name: <p>The name of the domain you want to permanently delete.</p>

        Raises:
            capo_cloudsearch.errors.base_exception.BaseException: <p>An error occurred while processing the request.</p>
            capo_cloudsearch.errors.internal_exception.InternalException: <p>An internal error occurred while processing the request. If this problem persists, report an issue from the <a href="http://status.aws.amazon.com/" target="_blank">Service Health Dashboard</a>.</p>
            capo_cloudsearch.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        def _handler(
            req: "OperationRequest[capo_cloudsearch.types.delete_domain_request.DeleteDomainRequest]",
        ) -> OperationResponse[
            "capo_cloudsearch.types.delete_domain_response.DeleteDomainResponse"
        ]:
            import capo_cloudsearch._operations.a9_search_cloud_config_service2013.delete_domain

            output, http_response = (
                capo_cloudsearch._operations.a9_search_cloud_config_service2013.delete_domain.delete_domain(
                    req.options, req.input
                )
            )
            return OperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_cloudsearch.types.delete_domain_request.DeleteDomainRequest = {
            "domain_name": domain_name
        }

        response = execute_pipeline(
            OperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        response.response.close()
        return response.output

    def delete_expression(
        self,
        domain_name: "capo_cloudsearch.types.domain_name.DomainName",
        expression_name: "capo_cloudsearch.types.standard_name.StandardName",
        *,
        config_overrides: Optional[CloudSearchClientConfig] = None,
    ) -> "capo_cloudsearch.types.delete_expression_response.DeleteExpressionResponse":
        """<p>Removes an <code><a>Expression</a></code> from the search domain. For more information, see <a href="http://docs.aws.amazon.com/cloudsearch/latest/developerguide/configuring-expressions.html" target="_blank">Configuring Expressions</a> in the <i>Amazon CloudSearch Developer Guide</i>.</p>

        Args:
            expression_name: <p>The name of the <code><a>Expression</a></code> to delete.</p>

        Raises:
            capo_cloudsearch.errors.base_exception.BaseException: <p>An error occurred while processing the request.</p>
            capo_cloudsearch.errors.internal_exception.InternalException: <p>An internal error occurred while processing the request. If this problem persists, report an issue from the <a href="http://status.aws.amazon.com/" target="_blank">Service Health Dashboard</a>.</p>
            capo_cloudsearch.errors.invalid_type_exception.InvalidTypeException: <p>The request was rejected because it specified an invalid type definition.</p>
            capo_cloudsearch.errors.resource_not_found_exception.ResourceNotFoundException: <p>The request was rejected because it attempted to reference a resource that does not exist.</p>
            capo_cloudsearch.errors.validation_exception.ValidationException: <p>The request was rejected because it has invalid parameters.</p>
            capo_cloudsearch.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        def _handler(
            req: "OperationRequest[capo_cloudsearch.types.delete_expression_request.DeleteExpressionRequest]",
        ) -> OperationResponse[
            "capo_cloudsearch.types.delete_expression_response.DeleteExpressionResponse"
        ]:
            import capo_cloudsearch._operations.a9_search_cloud_config_service2013.delete_expression

            output, http_response = (
                capo_cloudsearch._operations.a9_search_cloud_config_service2013.delete_expression.delete_expression(
                    req.options, req.input
                )
            )
            return OperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_cloudsearch.types.delete_expression_request.DeleteExpressionRequest = {
            "domain_name": domain_name,
            "expression_name": expression_name,
        }

        response = execute_pipeline(
            OperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        response.response.close()
        return response.output

    def delete_index_field(
        self,
        domain_name: "capo_cloudsearch.types.domain_name.DomainName",
        index_field_name: "capo_cloudsearch.types.dynamic_field_name.DynamicFieldName",
        *,
        config_overrides: Optional[CloudSearchClientConfig] = None,
    ) -> "capo_cloudsearch.types.delete_index_field_response.DeleteIndexFieldResponse":
        """<p>Removes an <code><a>IndexField</a></code> from the search domain. For more information, see <a href="http://docs.aws.amazon.com/cloudsearch/latest/developerguide/configuring-index-fields.html" target="_blank">Configuring Index Fields</a> in the <i>Amazon CloudSearch Developer Guide</i>.</p>

        Args:
            index_field_name: <p>The name of the index field your want to remove from the domain's indexing options.</p>

        Raises:
            capo_cloudsearch.errors.base_exception.BaseException: <p>An error occurred while processing the request.</p>
            capo_cloudsearch.errors.internal_exception.InternalException: <p>An internal error occurred while processing the request. If this problem persists, report an issue from the <a href="http://status.aws.amazon.com/" target="_blank">Service Health Dashboard</a>.</p>
            capo_cloudsearch.errors.invalid_type_exception.InvalidTypeException: <p>The request was rejected because it specified an invalid type definition.</p>
            capo_cloudsearch.errors.resource_not_found_exception.ResourceNotFoundException: <p>The request was rejected because it attempted to reference a resource that does not exist.</p>
            capo_cloudsearch.errors.validation_exception.ValidationException: <p>The request was rejected because it has invalid parameters.</p>
            capo_cloudsearch.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        def _handler(
            req: "OperationRequest[capo_cloudsearch.types.delete_index_field_request.DeleteIndexFieldRequest]",
        ) -> OperationResponse[
            "capo_cloudsearch.types.delete_index_field_response.DeleteIndexFieldResponse"
        ]:
            import capo_cloudsearch._operations.a9_search_cloud_config_service2013.delete_index_field

            output, http_response = (
                capo_cloudsearch._operations.a9_search_cloud_config_service2013.delete_index_field.delete_index_field(
                    req.options, req.input
                )
            )
            return OperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_cloudsearch.types.delete_index_field_request.DeleteIndexFieldRequest = {
            "domain_name": domain_name,
            "index_field_name": index_field_name,
        }

        response = execute_pipeline(
            OperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        response.response.close()
        return response.output

    def delete_suggester(
        self,
        domain_name: "capo_cloudsearch.types.domain_name.DomainName",
        suggester_name: "capo_cloudsearch.types.standard_name.StandardName",
        *,
        config_overrides: Optional[CloudSearchClientConfig] = None,
    ) -> "capo_cloudsearch.types.delete_suggester_response.DeleteSuggesterResponse":
        """<p>Deletes a suggester. For more information, see <a href="http://docs.aws.amazon.com/cloudsearch/latest/developerguide/getting-suggestions.html" target="_blank">Getting Search Suggestions</a> in the <i>Amazon CloudSearch Developer Guide</i>.</p>

        Args:
            suggester_name: <p>Specifies the name of the suggester you want to delete.</p>

        Raises:
            capo_cloudsearch.errors.base_exception.BaseException: <p>An error occurred while processing the request.</p>
            capo_cloudsearch.errors.internal_exception.InternalException: <p>An internal error occurred while processing the request. If this problem persists, report an issue from the <a href="http://status.aws.amazon.com/" target="_blank">Service Health Dashboard</a>.</p>
            capo_cloudsearch.errors.invalid_type_exception.InvalidTypeException: <p>The request was rejected because it specified an invalid type definition.</p>
            capo_cloudsearch.errors.resource_not_found_exception.ResourceNotFoundException: <p>The request was rejected because it attempted to reference a resource that does not exist.</p>
            capo_cloudsearch.errors.validation_exception.ValidationException: <p>The request was rejected because it has invalid parameters.</p>
            capo_cloudsearch.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        def _handler(
            req: "OperationRequest[capo_cloudsearch.types.delete_suggester_request.DeleteSuggesterRequest]",
        ) -> OperationResponse[
            "capo_cloudsearch.types.delete_suggester_response.DeleteSuggesterResponse"
        ]:
            import capo_cloudsearch._operations.a9_search_cloud_config_service2013.delete_suggester

            output, http_response = (
                capo_cloudsearch._operations.a9_search_cloud_config_service2013.delete_suggester.delete_suggester(
                    req.options, req.input
                )
            )
            return OperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_cloudsearch.types.delete_suggester_request.DeleteSuggesterRequest = {
            "domain_name": domain_name,
            "suggester_name": suggester_name,
        }

        response = execute_pipeline(
            OperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        response.response.close()
        return response.output

    def describe_analysis_schemes(
        self,
        domain_name: "capo_cloudsearch.types.domain_name.DomainName",
        *,
        config_overrides: Optional[CloudSearchClientConfig] = None,
        analysis_scheme_names: Optional[
            "capo_cloudsearch.types.standard_name_list.StandardNameList"
        ] = None,
        deployed: Optional["capo_cloudsearch.types.boolean.Boolean"] = None,
    ) -> "capo_cloudsearch.types.describe_analysis_schemes_response.DescribeAnalysisSchemesResponse":
        """<p>Gets the analysis schemes configured for a domain. An analysis scheme defines language-specific text processing options for a <code>text</code> field. Can be limited to specific analysis schemes by name. By default, shows all analysis schemes and includes any pending changes to the configuration. Set the <code>Deployed</code> option to <code>true</code> to show the active configuration and exclude pending changes. For more information, see <a href="http://docs.aws.amazon.com/cloudsearch/latest/developerguide/configuring-analysis-schemes.html" target="_blank">Configuring Analysis Schemes</a> in the <i>Amazon CloudSearch Developer Guide</i>.</p>

        Args:
            domain_name: <p>The name of the domain you want to describe.</p>
            analysis_scheme_names: <p>The analysis schemes you want to describe.</p>
            deployed: <p>Whether to display the deployed configuration (<code>true</code>) or include any pending changes (<code>false</code>). Defaults to <code>false</code>.</p>

        Raises:
            capo_cloudsearch.errors.base_exception.BaseException: <p>An error occurred while processing the request.</p>
            capo_cloudsearch.errors.internal_exception.InternalException: <p>An internal error occurred while processing the request. If this problem persists, report an issue from the <a href="http://status.aws.amazon.com/" target="_blank">Service Health Dashboard</a>.</p>
            capo_cloudsearch.errors.resource_not_found_exception.ResourceNotFoundException: <p>The request was rejected because it attempted to reference a resource that does not exist.</p>
            capo_cloudsearch.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        def _handler(
            req: "OperationRequest[capo_cloudsearch.types.describe_analysis_schemes_request.DescribeAnalysisSchemesRequest]",
        ) -> OperationResponse[
            "capo_cloudsearch.types.describe_analysis_schemes_response.DescribeAnalysisSchemesResponse"
        ]:
            import capo_cloudsearch._operations.a9_search_cloud_config_service2013.describe_analysis_schemes

            output, http_response = (
                capo_cloudsearch._operations.a9_search_cloud_config_service2013.describe_analysis_schemes.describe_analysis_schemes(
                    req.options, req.input
                )
            )
            return OperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_cloudsearch.types.describe_analysis_schemes_request.DescribeAnalysisSchemesRequest = {
            "domain_name": domain_name
        }
        if analysis_scheme_names is not None:
            input_["analysis_scheme_names"] = analysis_scheme_names
        if deployed is not None:
            input_["deployed"] = deployed

        response = execute_pipeline(
            OperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        response.response.close()
        return response.output

    def describe_availability_options(
        self,
        domain_name: "capo_cloudsearch.types.domain_name.DomainName",
        *,
        config_overrides: Optional[CloudSearchClientConfig] = None,
        deployed: Optional["capo_cloudsearch.types.boolean.Boolean"] = None,
    ) -> "capo_cloudsearch.types.describe_availability_options_response.DescribeAvailabilityOptionsResponse":
        """<p>Gets the availability options configured for a domain. By default, shows the configuration with any pending changes. Set the <code>Deployed</code> option to <code>true</code> to show the active configuration and exclude pending changes. For more information, see <a href="http://docs.aws.amazon.com/cloudsearch/latest/developerguide/configuring-availability-options.html" target="_blank">Configuring Availability Options</a> in the <i>Amazon CloudSearch Developer Guide</i>.</p>

        Args:
            domain_name: <p>The name of the domain you want to describe.</p>
            deployed: <p>Whether to display the deployed configuration (<code>true</code>) or include any pending changes (<code>false</code>). Defaults to <code>false</code>.</p>

        Raises:
            capo_cloudsearch.errors.base_exception.BaseException: <p>An error occurred while processing the request.</p>
            capo_cloudsearch.errors.disabled_operation_exception.DisabledOperationException: <p>The request was rejected because it attempted an operation which is not enabled.</p>
            capo_cloudsearch.errors.internal_exception.InternalException: <p>An internal error occurred while processing the request. If this problem persists, report an issue from the <a href="http://status.aws.amazon.com/" target="_blank">Service Health Dashboard</a>.</p>
            capo_cloudsearch.errors.invalid_type_exception.InvalidTypeException: <p>The request was rejected because it specified an invalid type definition.</p>
            capo_cloudsearch.errors.limit_exceeded_exception.LimitExceededException: <p>The request was rejected because a resource limit has already been met.</p>
            capo_cloudsearch.errors.resource_not_found_exception.ResourceNotFoundException: <p>The request was rejected because it attempted to reference a resource that does not exist.</p>
            capo_cloudsearch.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        def _handler(
            req: "OperationRequest[capo_cloudsearch.types.describe_availability_options_request.DescribeAvailabilityOptionsRequest]",
        ) -> OperationResponse[
            "capo_cloudsearch.types.describe_availability_options_response.DescribeAvailabilityOptionsResponse"
        ]:
            import capo_cloudsearch._operations.a9_search_cloud_config_service2013.describe_availability_options

            output, http_response = (
                capo_cloudsearch._operations.a9_search_cloud_config_service2013.describe_availability_options.describe_availability_options(
                    req.options, req.input
                )
            )
            return OperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_cloudsearch.types.describe_availability_options_request.DescribeAvailabilityOptionsRequest = {
            "domain_name": domain_name
        }
        if deployed is not None:
            input_["deployed"] = deployed

        response = execute_pipeline(
            OperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        response.response.close()
        return response.output

    def describe_domain_endpoint_options(
        self,
        domain_name: "capo_cloudsearch.types.domain_name.DomainName",
        *,
        config_overrides: Optional[CloudSearchClientConfig] = None,
        deployed: Optional["capo_cloudsearch.types.boolean.Boolean"] = None,
    ) -> "capo_cloudsearch.types.describe_domain_endpoint_options_response.DescribeDomainEndpointOptionsResponse":
        """<p>Returns the domain's endpoint options, specifically whether all requests to the domain must arrive over HTTPS. For more information, see <a href="http://docs.aws.amazon.com/cloudsearch/latest/developerguide/configuring-domain-endpoint-options.html" target="_blank">Configuring Domain Endpoint Options</a> in the <i>Amazon CloudSearch Developer Guide</i>.</p>

        Args:
            domain_name: <p>A string that represents the name of a domain.</p>
            deployed: <p>Whether to retrieve the latest configuration (which might be in a Processing state) or the current, active configuration. Defaults to <code>false</code>.</p>

        Raises:
            capo_cloudsearch.errors.base_exception.BaseException: <p>An error occurred while processing the request.</p>
            capo_cloudsearch.errors.disabled_operation_exception.DisabledOperationException: <p>The request was rejected because it attempted an operation which is not enabled.</p>
            capo_cloudsearch.errors.internal_exception.InternalException: <p>An internal error occurred while processing the request. If this problem persists, report an issue from the <a href="http://status.aws.amazon.com/" target="_blank">Service Health Dashboard</a>.</p>
            capo_cloudsearch.errors.limit_exceeded_exception.LimitExceededException: <p>The request was rejected because a resource limit has already been met.</p>
            capo_cloudsearch.errors.resource_not_found_exception.ResourceNotFoundException: <p>The request was rejected because it attempted to reference a resource that does not exist.</p>
            capo_cloudsearch.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        def _handler(
            req: "OperationRequest[capo_cloudsearch.types.describe_domain_endpoint_options_request.DescribeDomainEndpointOptionsRequest]",
        ) -> OperationResponse[
            "capo_cloudsearch.types.describe_domain_endpoint_options_response.DescribeDomainEndpointOptionsResponse"
        ]:
            import capo_cloudsearch._operations.a9_search_cloud_config_service2013.describe_domain_endpoint_options

            output, http_response = (
                capo_cloudsearch._operations.a9_search_cloud_config_service2013.describe_domain_endpoint_options.describe_domain_endpoint_options(
                    req.options, req.input
                )
            )
            return OperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_cloudsearch.types.describe_domain_endpoint_options_request.DescribeDomainEndpointOptionsRequest = {
            "domain_name": domain_name
        }
        if deployed is not None:
            input_["deployed"] = deployed

        response = execute_pipeline(
            OperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        response.response.close()
        return response.output

    def describe_domains(
        self,
        *,
        config_overrides: Optional[CloudSearchClientConfig] = None,
        domain_names: Optional[
            "capo_cloudsearch.types.domain_name_list.DomainNameList"
        ] = None,
    ) -> "capo_cloudsearch.types.describe_domains_response.DescribeDomainsResponse":
        """<p>Gets information about the search domains owned by this account. Can be limited to specific domains. Shows all domains by default. To get the number of searchable documents in a domain, use the console or submit a <code>matchall</code> request to your domain's search endpoint: <code>q=matchall&amp;q.parser=structured&amp;size=0</code>. For more information, see <a href="http://docs.aws.amazon.com/cloudsearch/latest/developerguide/getting-domain-info.html" target="_blank">Getting Information about a Search Domain</a> in the <i>Amazon CloudSearch Developer Guide</i>.</p>

        Args:
            domain_names: <p>The names of the domains you want to include in the response.</p>

        Raises:
            capo_cloudsearch.errors.base_exception.BaseException: <p>An error occurred while processing the request.</p>
            capo_cloudsearch.errors.internal_exception.InternalException: <p>An internal error occurred while processing the request. If this problem persists, report an issue from the <a href="http://status.aws.amazon.com/" target="_blank">Service Health Dashboard</a>.</p>
            capo_cloudsearch.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        def _handler(
            req: "OperationRequest[capo_cloudsearch.types.describe_domains_request.DescribeDomainsRequest]",
        ) -> OperationResponse[
            "capo_cloudsearch.types.describe_domains_response.DescribeDomainsResponse"
        ]:
            import capo_cloudsearch._operations.a9_search_cloud_config_service2013.describe_domains

            output, http_response = (
                capo_cloudsearch._operations.a9_search_cloud_config_service2013.describe_domains.describe_domains(
                    req.options, req.input
                )
            )
            return OperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_cloudsearch.types.describe_domains_request.DescribeDomainsRequest = {}
        if domain_names is not None:
            input_["domain_names"] = domain_names

        response = execute_pipeline(
            OperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        response.response.close()
        return response.output

    def describe_expressions(
        self,
        domain_name: "capo_cloudsearch.types.domain_name.DomainName",
        *,
        config_overrides: Optional[CloudSearchClientConfig] = None,
        expression_names: Optional[
            "capo_cloudsearch.types.standard_name_list.StandardNameList"
        ] = None,
        deployed: Optional["capo_cloudsearch.types.boolean.Boolean"] = None,
    ) -> "capo_cloudsearch.types.describe_expressions_response.DescribeExpressionsResponse":
        """<p>Gets the expressions configured for the search domain. Can be limited to specific expressions by name. By default, shows all expressions and includes any pending changes to the configuration. Set the <code>Deployed</code> option to <code>true</code> to show the active configuration and exclude pending changes. For more information, see <a href="http://docs.aws.amazon.com/cloudsearch/latest/developerguide/configuring-expressions.html" target="_blank">Configuring Expressions</a> in the <i>Amazon CloudSearch Developer Guide</i>.</p>

        Args:
            domain_name: <p>The name of the domain you want to describe.</p>
            expression_names: <p>Limits the <code><a>DescribeExpressions</a></code> response to the specified expressions. If not specified, all expressions are shown.</p>
            deployed: <p>Whether to display the deployed configuration (<code>true</code>) or include any pending changes (<code>false</code>). Defaults to <code>false</code>.</p>

        Raises:
            capo_cloudsearch.errors.base_exception.BaseException: <p>An error occurred while processing the request.</p>
            capo_cloudsearch.errors.internal_exception.InternalException: <p>An internal error occurred while processing the request. If this problem persists, report an issue from the <a href="http://status.aws.amazon.com/" target="_blank">Service Health Dashboard</a>.</p>
            capo_cloudsearch.errors.resource_not_found_exception.ResourceNotFoundException: <p>The request was rejected because it attempted to reference a resource that does not exist.</p>
            capo_cloudsearch.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        def _handler(
            req: "OperationRequest[capo_cloudsearch.types.describe_expressions_request.DescribeExpressionsRequest]",
        ) -> OperationResponse[
            "capo_cloudsearch.types.describe_expressions_response.DescribeExpressionsResponse"
        ]:
            import capo_cloudsearch._operations.a9_search_cloud_config_service2013.describe_expressions

            output, http_response = (
                capo_cloudsearch._operations.a9_search_cloud_config_service2013.describe_expressions.describe_expressions(
                    req.options, req.input
                )
            )
            return OperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_cloudsearch.types.describe_expressions_request.DescribeExpressionsRequest = {
            "domain_name": domain_name
        }
        if expression_names is not None:
            input_["expression_names"] = expression_names
        if deployed is not None:
            input_["deployed"] = deployed

        response = execute_pipeline(
            OperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        response.response.close()
        return response.output

    def describe_index_fields(
        self,
        domain_name: "capo_cloudsearch.types.domain_name.DomainName",
        *,
        config_overrides: Optional[CloudSearchClientConfig] = None,
        field_names: Optional[
            "capo_cloudsearch.types.dynamic_field_name_list.DynamicFieldNameList"
        ] = None,
        deployed: Optional["capo_cloudsearch.types.boolean.Boolean"] = None,
    ) -> "capo_cloudsearch.types.describe_index_fields_response.DescribeIndexFieldsResponse":
        """<p>Gets information about the index fields configured for the search domain. Can be limited to specific fields by name. By default, shows all fields and includes any pending changes to the configuration. Set the <code>Deployed</code> option to <code>true</code> to show the active configuration and exclude pending changes. For more information, see <a href="http://docs.aws.amazon.com/cloudsearch/latest/developerguide/getting-domain-info.html" target="_blank">Getting Domain Information</a> in the <i>Amazon CloudSearch Developer Guide</i>.</p>

        Args:
            domain_name: <p>The name of the domain you want to describe.</p>
            field_names: <p>A list of the index fields you want to describe. If not specified, information is returned for all configured index fields.</p>
            deployed: <p>Whether to display the deployed configuration (<code>true</code>) or include any pending changes (<code>false</code>). Defaults to <code>false</code>.</p>

        Raises:
            capo_cloudsearch.errors.base_exception.BaseException: <p>An error occurred while processing the request.</p>
            capo_cloudsearch.errors.internal_exception.InternalException: <p>An internal error occurred while processing the request. If this problem persists, report an issue from the <a href="http://status.aws.amazon.com/" target="_blank">Service Health Dashboard</a>.</p>
            capo_cloudsearch.errors.resource_not_found_exception.ResourceNotFoundException: <p>The request was rejected because it attempted to reference a resource that does not exist.</p>
            capo_cloudsearch.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        def _handler(
            req: "OperationRequest[capo_cloudsearch.types.describe_index_fields_request.DescribeIndexFieldsRequest]",
        ) -> OperationResponse[
            "capo_cloudsearch.types.describe_index_fields_response.DescribeIndexFieldsResponse"
        ]:
            import capo_cloudsearch._operations.a9_search_cloud_config_service2013.describe_index_fields

            output, http_response = (
                capo_cloudsearch._operations.a9_search_cloud_config_service2013.describe_index_fields.describe_index_fields(
                    req.options, req.input
                )
            )
            return OperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_cloudsearch.types.describe_index_fields_request.DescribeIndexFieldsRequest = {
            "domain_name": domain_name
        }
        if field_names is not None:
            input_["field_names"] = field_names
        if deployed is not None:
            input_["deployed"] = deployed

        response = execute_pipeline(
            OperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        response.response.close()
        return response.output

    def describe_scaling_parameters(
        self,
        domain_name: "capo_cloudsearch.types.domain_name.DomainName",
        *,
        config_overrides: Optional[CloudSearchClientConfig] = None,
    ) -> "capo_cloudsearch.types.describe_scaling_parameters_response.DescribeScalingParametersResponse":
        """<p>Gets the scaling parameters configured for a domain. A domain's scaling parameters specify the desired search instance type and replication count. For more information, see <a href="http://docs.aws.amazon.com/cloudsearch/latest/developerguide/configuring-scaling-options.html" target="_blank">Configuring Scaling Options</a> in the <i>Amazon CloudSearch Developer Guide</i>.</p>

        Raises:
            capo_cloudsearch.errors.base_exception.BaseException: <p>An error occurred while processing the request.</p>
            capo_cloudsearch.errors.internal_exception.InternalException: <p>An internal error occurred while processing the request. If this problem persists, report an issue from the <a href="http://status.aws.amazon.com/" target="_blank">Service Health Dashboard</a>.</p>
            capo_cloudsearch.errors.resource_not_found_exception.ResourceNotFoundException: <p>The request was rejected because it attempted to reference a resource that does not exist.</p>
            capo_cloudsearch.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        def _handler(
            req: "OperationRequest[capo_cloudsearch.types.describe_scaling_parameters_request.DescribeScalingParametersRequest]",
        ) -> OperationResponse[
            "capo_cloudsearch.types.describe_scaling_parameters_response.DescribeScalingParametersResponse"
        ]:
            import capo_cloudsearch._operations.a9_search_cloud_config_service2013.describe_scaling_parameters

            output, http_response = (
                capo_cloudsearch._operations.a9_search_cloud_config_service2013.describe_scaling_parameters.describe_scaling_parameters(
                    req.options, req.input
                )
            )
            return OperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_cloudsearch.types.describe_scaling_parameters_request.DescribeScalingParametersRequest = {
            "domain_name": domain_name
        }

        response = execute_pipeline(
            OperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        response.response.close()
        return response.output

    def describe_service_access_policies(
        self,
        domain_name: "capo_cloudsearch.types.domain_name.DomainName",
        *,
        config_overrides: Optional[CloudSearchClientConfig] = None,
        deployed: Optional["capo_cloudsearch.types.boolean.Boolean"] = None,
    ) -> "capo_cloudsearch.types.describe_service_access_policies_response.DescribeServiceAccessPoliciesResponse":
        """<p>Gets information about the access policies that control access to the domain's document and search endpoints. By default, shows the configuration with any pending changes. Set the <code>Deployed</code> option to <code>true</code> to show the active configuration and exclude pending changes. For more information, see <a href="http://docs.aws.amazon.com/cloudsearch/latest/developerguide/configuring-access.html" target="_blank">Configuring Access for a Search Domain</a> in the <i>Amazon CloudSearch Developer Guide</i>.</p>

        Args:
            domain_name: <p>The name of the domain you want to describe.</p>
            deployed: <p>Whether to display the deployed configuration (<code>true</code>) or include any pending changes (<code>false</code>). Defaults to <code>false</code>.</p>

        Raises:
            capo_cloudsearch.errors.base_exception.BaseException: <p>An error occurred while processing the request.</p>
            capo_cloudsearch.errors.internal_exception.InternalException: <p>An internal error occurred while processing the request. If this problem persists, report an issue from the <a href="http://status.aws.amazon.com/" target="_blank">Service Health Dashboard</a>.</p>
            capo_cloudsearch.errors.resource_not_found_exception.ResourceNotFoundException: <p>The request was rejected because it attempted to reference a resource that does not exist.</p>
            capo_cloudsearch.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        def _handler(
            req: "OperationRequest[capo_cloudsearch.types.describe_service_access_policies_request.DescribeServiceAccessPoliciesRequest]",
        ) -> OperationResponse[
            "capo_cloudsearch.types.describe_service_access_policies_response.DescribeServiceAccessPoliciesResponse"
        ]:
            import capo_cloudsearch._operations.a9_search_cloud_config_service2013.describe_service_access_policies

            output, http_response = (
                capo_cloudsearch._operations.a9_search_cloud_config_service2013.describe_service_access_policies.describe_service_access_policies(
                    req.options, req.input
                )
            )
            return OperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_cloudsearch.types.describe_service_access_policies_request.DescribeServiceAccessPoliciesRequest = {
            "domain_name": domain_name
        }
        if deployed is not None:
            input_["deployed"] = deployed

        response = execute_pipeline(
            OperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        response.response.close()
        return response.output

    def describe_suggesters(
        self,
        domain_name: "capo_cloudsearch.types.domain_name.DomainName",
        *,
        config_overrides: Optional[CloudSearchClientConfig] = None,
        suggester_names: Optional[
            "capo_cloudsearch.types.standard_name_list.StandardNameList"
        ] = None,
        deployed: Optional["capo_cloudsearch.types.boolean.Boolean"] = None,
    ) -> (
        "capo_cloudsearch.types.describe_suggesters_response.DescribeSuggestersResponse"
    ):
        """<p>Gets the suggesters configured for a domain. A suggester enables you to display possible matches before users finish typing their queries. Can be limited to specific suggesters by name. By default, shows all suggesters and includes any pending changes to the configuration. Set the <code>Deployed</code> option to <code>true</code> to show the active configuration and exclude pending changes. For more information, see <a href="http://docs.aws.amazon.com/cloudsearch/latest/developerguide/getting-suggestions.html" target="_blank">Getting Search Suggestions</a> in the <i>Amazon CloudSearch Developer Guide</i>.</p>

        Args:
            domain_name: <p>The name of the domain you want to describe.</p>
            suggester_names: <p>The suggesters you want to describe.</p>
            deployed: <p>Whether to display the deployed configuration (<code>true</code>) or include any pending changes (<code>false</code>). Defaults to <code>false</code>.</p>

        Raises:
            capo_cloudsearch.errors.base_exception.BaseException: <p>An error occurred while processing the request.</p>
            capo_cloudsearch.errors.internal_exception.InternalException: <p>An internal error occurred while processing the request. If this problem persists, report an issue from the <a href="http://status.aws.amazon.com/" target="_blank">Service Health Dashboard</a>.</p>
            capo_cloudsearch.errors.resource_not_found_exception.ResourceNotFoundException: <p>The request was rejected because it attempted to reference a resource that does not exist.</p>
            capo_cloudsearch.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        def _handler(
            req: "OperationRequest[capo_cloudsearch.types.describe_suggesters_request.DescribeSuggestersRequest]",
        ) -> OperationResponse[
            "capo_cloudsearch.types.describe_suggesters_response.DescribeSuggestersResponse"
        ]:
            import capo_cloudsearch._operations.a9_search_cloud_config_service2013.describe_suggesters

            output, http_response = (
                capo_cloudsearch._operations.a9_search_cloud_config_service2013.describe_suggesters.describe_suggesters(
                    req.options, req.input
                )
            )
            return OperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_cloudsearch.types.describe_suggesters_request.DescribeSuggestersRequest = {
            "domain_name": domain_name
        }
        if suggester_names is not None:
            input_["suggester_names"] = suggester_names
        if deployed is not None:
            input_["deployed"] = deployed

        response = execute_pipeline(
            OperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        response.response.close()
        return response.output

    def index_documents(
        self,
        domain_name: "capo_cloudsearch.types.domain_name.DomainName",
        *,
        config_overrides: Optional[CloudSearchClientConfig] = None,
    ) -> "capo_cloudsearch.types.index_documents_response.IndexDocumentsResponse":
        """<p>Tells the search domain to start indexing its documents using the latest indexing options. This operation must be invoked to activate options whose <a>OptionStatus</a> is <code>RequiresIndexDocuments</code>.</p>

        Raises:
            capo_cloudsearch.errors.base_exception.BaseException: <p>An error occurred while processing the request.</p>
            capo_cloudsearch.errors.internal_exception.InternalException: <p>An internal error occurred while processing the request. If this problem persists, report an issue from the <a href="http://status.aws.amazon.com/" target="_blank">Service Health Dashboard</a>.</p>
            capo_cloudsearch.errors.resource_not_found_exception.ResourceNotFoundException: <p>The request was rejected because it attempted to reference a resource that does not exist.</p>
            capo_cloudsearch.errors.validation_exception.ValidationException: <p>The request was rejected because it has invalid parameters.</p>
            capo_cloudsearch.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        def _handler(
            req: "OperationRequest[capo_cloudsearch.types.index_documents_request.IndexDocumentsRequest]",
        ) -> OperationResponse[
            "capo_cloudsearch.types.index_documents_response.IndexDocumentsResponse"
        ]:
            import capo_cloudsearch._operations.a9_search_cloud_config_service2013.index_documents

            output, http_response = (
                capo_cloudsearch._operations.a9_search_cloud_config_service2013.index_documents.index_documents(
                    req.options, req.input
                )
            )
            return OperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_cloudsearch.types.index_documents_request.IndexDocumentsRequest = {
            "domain_name": domain_name
        }

        response = execute_pipeline(
            OperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        response.response.close()
        return response.output

    def list_domain_names(
        self, *, config_overrides: Optional[CloudSearchClientConfig] = None
    ) -> "capo_cloudsearch.types.list_domain_names_response.ListDomainNamesResponse":
        """<p>Lists all search domains owned by an account.</p>

        Raises:
            capo_cloudsearch.errors.base_exception.BaseException: <p>An error occurred while processing the request.</p>
            capo_cloudsearch.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        def _handler(
            req: "OperationRequest[None]",
        ) -> OperationResponse[
            "capo_cloudsearch.types.list_domain_names_response.ListDomainNamesResponse"
        ]:
            import capo_cloudsearch._operations.a9_search_cloud_config_service2013.list_domain_names

            output, http_response = (
                capo_cloudsearch._operations.a9_search_cloud_config_service2013.list_domain_names.list_domain_names(
                    req.options
                )
            )
            return OperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)

        response = execute_pipeline(
            OperationRequest(input=None, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        response.response.close()
        return response.output

    def update_availability_options(
        self,
        domain_name: "capo_cloudsearch.types.domain_name.DomainName",
        multi_az: "capo_cloudsearch.types.boolean.Boolean",
        *,
        config_overrides: Optional[CloudSearchClientConfig] = None,
    ) -> "capo_cloudsearch.types.update_availability_options_response.UpdateAvailabilityOptionsResponse":
        """<p>Configures the availability options for a domain. Enabling the Multi-AZ option expands an Amazon CloudSearch domain to an additional Availability Zone in the same Region to increase fault tolerance in the event of a service disruption. Changes to the Multi-AZ option can take about half an hour to become active. For more information, see <a href="http://docs.aws.amazon.com/cloudsearch/latest/developerguide/configuring-availability-options.html" target="_blank">Configuring Availability Options</a> in the <i>Amazon CloudSearch Developer Guide</i>.</p>

        Args:
            multi_az: <p>You expand an existing search domain to a second Availability Zone by setting the Multi-AZ option to true. Similarly, you can turn off the Multi-AZ option to downgrade the domain to a single Availability Zone by setting the Multi-AZ option to <code>false</code>. </p>

        Raises:
            capo_cloudsearch.errors.base_exception.BaseException: <p>An error occurred while processing the request.</p>
            capo_cloudsearch.errors.disabled_operation_exception.DisabledOperationException: <p>The request was rejected because it attempted an operation which is not enabled.</p>
            capo_cloudsearch.errors.internal_exception.InternalException: <p>An internal error occurred while processing the request. If this problem persists, report an issue from the <a href="http://status.aws.amazon.com/" target="_blank">Service Health Dashboard</a>.</p>
            capo_cloudsearch.errors.invalid_type_exception.InvalidTypeException: <p>The request was rejected because it specified an invalid type definition.</p>
            capo_cloudsearch.errors.limit_exceeded_exception.LimitExceededException: <p>The request was rejected because a resource limit has already been met.</p>
            capo_cloudsearch.errors.resource_not_found_exception.ResourceNotFoundException: <p>The request was rejected because it attempted to reference a resource that does not exist.</p>
            capo_cloudsearch.errors.validation_exception.ValidationException: <p>The request was rejected because it has invalid parameters.</p>
            capo_cloudsearch.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        def _handler(
            req: "OperationRequest[capo_cloudsearch.types.update_availability_options_request.UpdateAvailabilityOptionsRequest]",
        ) -> OperationResponse[
            "capo_cloudsearch.types.update_availability_options_response.UpdateAvailabilityOptionsResponse"
        ]:
            import capo_cloudsearch._operations.a9_search_cloud_config_service2013.update_availability_options

            output, http_response = (
                capo_cloudsearch._operations.a9_search_cloud_config_service2013.update_availability_options.update_availability_options(
                    req.options, req.input
                )
            )
            return OperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_cloudsearch.types.update_availability_options_request.UpdateAvailabilityOptionsRequest = {
            "domain_name": domain_name,
            "multi_az": multi_az,
        }

        response = execute_pipeline(
            OperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        response.response.close()
        return response.output

    def update_domain_endpoint_options(
        self,
        domain_name: "capo_cloudsearch.types.domain_name.DomainName",
        domain_endpoint_options: "capo_cloudsearch.types.domain_endpoint_options.DomainEndpointOptions",
        *,
        config_overrides: Optional[CloudSearchClientConfig] = None,
    ) -> "capo_cloudsearch.types.update_domain_endpoint_options_response.UpdateDomainEndpointOptionsResponse":
        """<p>Updates the domain's endpoint options, specifically whether all requests to the domain must arrive over HTTPS. For more information, see <a href="http://docs.aws.amazon.com/cloudsearch/latest/developerguide/configuring-domain-endpoint-options.html" target="_blank">Configuring Domain Endpoint Options</a> in the <i>Amazon CloudSearch Developer Guide</i>.</p>

        Args:
            domain_name: <p>A string that represents the name of a domain.</p>
            domain_endpoint_options: <p>Whether to require that all requests to the domain arrive over HTTPS. We recommend Policy-Min-TLS-1-2-2019-07 for TLSSecurityPolicy. For compatibility with older clients, the default is Policy-Min-TLS-1-0-2019-07. </p>

        Raises:
            capo_cloudsearch.errors.base_exception.BaseException: <p>An error occurred while processing the request.</p>
            capo_cloudsearch.errors.disabled_operation_exception.DisabledOperationException: <p>The request was rejected because it attempted an operation which is not enabled.</p>
            capo_cloudsearch.errors.internal_exception.InternalException: <p>An internal error occurred while processing the request. If this problem persists, report an issue from the <a href="http://status.aws.amazon.com/" target="_blank">Service Health Dashboard</a>.</p>
            capo_cloudsearch.errors.invalid_type_exception.InvalidTypeException: <p>The request was rejected because it specified an invalid type definition.</p>
            capo_cloudsearch.errors.limit_exceeded_exception.LimitExceededException: <p>The request was rejected because a resource limit has already been met.</p>
            capo_cloudsearch.errors.resource_not_found_exception.ResourceNotFoundException: <p>The request was rejected because it attempted to reference a resource that does not exist.</p>
            capo_cloudsearch.errors.validation_exception.ValidationException: <p>The request was rejected because it has invalid parameters.</p>
            capo_cloudsearch.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        def _handler(
            req: "OperationRequest[capo_cloudsearch.types.update_domain_endpoint_options_request.UpdateDomainEndpointOptionsRequest]",
        ) -> OperationResponse[
            "capo_cloudsearch.types.update_domain_endpoint_options_response.UpdateDomainEndpointOptionsResponse"
        ]:
            import capo_cloudsearch._operations.a9_search_cloud_config_service2013.update_domain_endpoint_options

            output, http_response = (
                capo_cloudsearch._operations.a9_search_cloud_config_service2013.update_domain_endpoint_options.update_domain_endpoint_options(
                    req.options, req.input
                )
            )
            return OperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_cloudsearch.types.update_domain_endpoint_options_request.UpdateDomainEndpointOptionsRequest = {
            "domain_name": domain_name,
            "domain_endpoint_options": domain_endpoint_options,
        }

        response = execute_pipeline(
            OperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        response.response.close()
        return response.output

    def update_scaling_parameters(
        self,
        domain_name: "capo_cloudsearch.types.domain_name.DomainName",
        scaling_parameters: "capo_cloudsearch.types.scaling_parameters.ScalingParameters",
        *,
        config_overrides: Optional[CloudSearchClientConfig] = None,
    ) -> "capo_cloudsearch.types.update_scaling_parameters_response.UpdateScalingParametersResponse":
        """<p>Configures scaling parameters for a domain. A domain's scaling parameters specify the desired search instance type and replication count. Amazon CloudSearch will still automatically scale your domain based on the volume of data and traffic, but not below the desired instance type and replication count. If the Multi-AZ option is enabled, these values control the resources used per Availability Zone. For more information, see <a href="http://docs.aws.amazon.com/cloudsearch/latest/developerguide/configuring-scaling-options.html" target="_blank">Configuring Scaling Options</a> in the <i>Amazon CloudSearch Developer Guide</i>. </p>

        Raises:
            capo_cloudsearch.errors.base_exception.BaseException: <p>An error occurred while processing the request.</p>
            capo_cloudsearch.errors.internal_exception.InternalException: <p>An internal error occurred while processing the request. If this problem persists, report an issue from the <a href="http://status.aws.amazon.com/" target="_blank">Service Health Dashboard</a>.</p>
            capo_cloudsearch.errors.invalid_type_exception.InvalidTypeException: <p>The request was rejected because it specified an invalid type definition.</p>
            capo_cloudsearch.errors.limit_exceeded_exception.LimitExceededException: <p>The request was rejected because a resource limit has already been met.</p>
            capo_cloudsearch.errors.resource_not_found_exception.ResourceNotFoundException: <p>The request was rejected because it attempted to reference a resource that does not exist.</p>
            capo_cloudsearch.errors.validation_exception.ValidationException: <p>The request was rejected because it has invalid parameters.</p>
            capo_cloudsearch.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        def _handler(
            req: "OperationRequest[capo_cloudsearch.types.update_scaling_parameters_request.UpdateScalingParametersRequest]",
        ) -> OperationResponse[
            "capo_cloudsearch.types.update_scaling_parameters_response.UpdateScalingParametersResponse"
        ]:
            import capo_cloudsearch._operations.a9_search_cloud_config_service2013.update_scaling_parameters

            output, http_response = (
                capo_cloudsearch._operations.a9_search_cloud_config_service2013.update_scaling_parameters.update_scaling_parameters(
                    req.options, req.input
                )
            )
            return OperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_cloudsearch.types.update_scaling_parameters_request.UpdateScalingParametersRequest = {
            "domain_name": domain_name,
            "scaling_parameters": scaling_parameters,
        }

        response = execute_pipeline(
            OperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        response.response.close()
        return response.output

    def update_service_access_policies(
        self,
        domain_name: "capo_cloudsearch.types.domain_name.DomainName",
        access_policies: "capo_cloudsearch.types.policy_document.PolicyDocument",
        *,
        config_overrides: Optional[CloudSearchClientConfig] = None,
    ) -> "capo_cloudsearch.types.update_service_access_policies_response.UpdateServiceAccessPoliciesResponse":
        """<p>Configures the access rules that control access to the domain's document and search endpoints. For more information, see <a href="http://docs.aws.amazon.com/cloudsearch/latest/developerguide/configuring-access.html" target="_blank"> Configuring Access for an Amazon CloudSearch Domain</a>.</p>

        Args:
            access_policies: <p>The access rules you want to configure. These rules replace any existing rules. </p>

        Raises:
            capo_cloudsearch.errors.base_exception.BaseException: <p>An error occurred while processing the request.</p>
            capo_cloudsearch.errors.internal_exception.InternalException: <p>An internal error occurred while processing the request. If this problem persists, report an issue from the <a href="http://status.aws.amazon.com/" target="_blank">Service Health Dashboard</a>.</p>
            capo_cloudsearch.errors.invalid_type_exception.InvalidTypeException: <p>The request was rejected because it specified an invalid type definition.</p>
            capo_cloudsearch.errors.limit_exceeded_exception.LimitExceededException: <p>The request was rejected because a resource limit has already been met.</p>
            capo_cloudsearch.errors.resource_not_found_exception.ResourceNotFoundException: <p>The request was rejected because it attempted to reference a resource that does not exist.</p>
            capo_cloudsearch.errors.validation_exception.ValidationException: <p>The request was rejected because it has invalid parameters.</p>
            capo_cloudsearch.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        def _handler(
            req: "OperationRequest[capo_cloudsearch.types.update_service_access_policies_request.UpdateServiceAccessPoliciesRequest]",
        ) -> OperationResponse[
            "capo_cloudsearch.types.update_service_access_policies_response.UpdateServiceAccessPoliciesResponse"
        ]:
            import capo_cloudsearch._operations.a9_search_cloud_config_service2013.update_service_access_policies

            output, http_response = (
                capo_cloudsearch._operations.a9_search_cloud_config_service2013.update_service_access_policies.update_service_access_policies(
                    req.options, req.input
                )
            )
            return OperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_cloudsearch.types.update_service_access_policies_request.UpdateServiceAccessPoliciesRequest = {
            "domain_name": domain_name,
            "access_policies": access_policies,
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
