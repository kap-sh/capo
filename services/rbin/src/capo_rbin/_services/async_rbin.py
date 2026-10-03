"""Generated from Smithy shape ``com.amazonaws.rbin#AmazonRecycleBin``."""

import warnings
from collections.abc import AsyncIterator
from typing import TYPE_CHECKING, Any, Iterable, Optional

from typing_extensions import Self, TypedDict
from zapros import AsyncBaseHandler, AsyncClient

import capo_rbin._auth._signers
import capo_rbin._auth._sigv4
from capo_rbin._auth._identity import Credentials
from capo_rbin._auth._providers import (
    CredentialsProvider,
    IdentityProvider,
    StaticAwsCredentialsProvider,
    default_aws_credentials_chain,
)
from capo_rbin._auth._zapros_handler import AuthMiddleware
from capo_rbin._pagination import resolve_path as _resolve_path
from capo_rbin._services._aws_config import aaws_config
from capo_rbin._services._pipeline import (
    AsyncInterceptor,
    AsyncOperationOptions,
    AsyncOperationRequest,
    AsyncOperationResponse,
    aexecute_pipeline,
    aretry,
)

if TYPE_CHECKING:
    import capo_rbin.types.create_rule_request
    import capo_rbin.types.create_rule_response
    import capo_rbin.types.delete_rule_request
    import capo_rbin.types.delete_rule_response
    import capo_rbin.types.description
    import capo_rbin.types.exclude_resource_tags
    import capo_rbin.types.get_rule_request
    import capo_rbin.types.get_rule_response
    import capo_rbin.types.list_rules_request
    import capo_rbin.types.list_rules_response
    import capo_rbin.types.list_tags_for_resource_request
    import capo_rbin.types.list_tags_for_resource_response
    import capo_rbin.types.lock_configuration
    import capo_rbin.types.lock_rule_request
    import capo_rbin.types.lock_rule_response
    import capo_rbin.types.lock_state
    import capo_rbin.types.max_results
    import capo_rbin.types.next_token
    import capo_rbin.types.resource_tags
    import capo_rbin.types.resource_type
    import capo_rbin.types.retention_period
    import capo_rbin.types.rule_arn
    import capo_rbin.types.rule_identifier
    import capo_rbin.types.rule_summary
    import capo_rbin.types.tag_key_list
    import capo_rbin.types.tag_list
    import capo_rbin.types.tag_resource_request
    import capo_rbin.types.tag_resource_response
    import capo_rbin.types.unlock_rule_request
    import capo_rbin.types.unlock_rule_response
    import capo_rbin.types.untag_resource_request
    import capo_rbin.types.untag_resource_response
    import capo_rbin.types.update_rule_request
    import capo_rbin.types.update_rule_response


class AsyncrbinClientConfig(TypedDict, total=False, closed=True):
    operation_interceptors: Iterable[AsyncInterceptor[Any, Any]]
    retry_max_attempts: int | None
    region: str | None
    use_dual_stack: bool | None
    use_fips: bool | None
    endpoint: str | None
    credentials_provider: IdentityProvider[Credentials] | None


class AsyncrbinClient:
    """A client for the ``rbin`` service.

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
    """

    def __init__(
        self,
        http_handler: AsyncBaseHandler | None = None,
        operation_interceptors: Iterable[AsyncInterceptor[Any, Any]] | None = None,
        retry_max_attempts: int | None = None,
        region: str | None = None,
        use_dual_stack: bool | None = None,
        use_fips: bool | None = None,
        endpoint: str | None = None,
        credentials: Credentials | None = None,
        credentials_provider: CredentialsProvider | None = None,
    ):
        self._client = AsyncClient(http_handler).wrap_with_middleware(
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
                AsyncClient(http_handler)
            )
        self._config = AsyncrbinClientConfig(
            {
                "operation_interceptors": operation_interceptors or [],
                "retry_max_attempts": retry_max_attempts,
                "region": region,
                "use_dual_stack": use_dual_stack,
                "use_fips": use_fips,
                "endpoint": endpoint,
                "credentials_provider": resolved_credentials_provider,
            }
        )

    def operation_options(
        self, config_overrides: Optional[AsyncrbinClientConfig] = None
    ) -> tuple[Iterable[AsyncInterceptor[Any, Any]], AsyncOperationOptions]:
        overrides: AsyncrbinClientConfig = config_overrides or {}
        interceptors_: list[AsyncInterceptor[Any, Any]] = [
            *overrides.get(
                "operation_interceptors", self._config.get("operation_interceptors", [])
            ),
            aaws_config(),
            aretry(),
        ]
        options_: AsyncOperationOptions = AsyncOperationOptions(
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
        )
        return interceptors_, options_

    async def create_rule(
        self,
        retention_period: "capo_rbin.types.retention_period.RetentionPeriod",
        resource_type: "capo_rbin.types.resource_type.ResourceType",
        *,
        config_overrides: Optional[AsyncrbinClientConfig] = None,
        description: Optional["capo_rbin.types.description.Description"] = None,
        tags: Optional["capo_rbin.types.tag_list.TagList"] = None,
        resource_tags: Optional["capo_rbin.types.resource_tags.ResourceTags"] = None,
        lock_configuration: Optional[
            "capo_rbin.types.lock_configuration.LockConfiguration"
        ] = None,
        exclude_resource_tags: Optional[
            "capo_rbin.types.exclude_resource_tags.ExcludeResourceTags"
        ] = None,
    ) -> "capo_rbin.types.create_rule_response.CreateRuleResponse":
        """<p>Creates a Recycle Bin retention rule. You can create two types of retention rules:</p> <ul> <li> <p> <b>Tag-level retention rules</b> - These retention rules use resource tags to identify the resources to protect. For each retention rule, you specify one or more tag key and value pairs. Resources (of the specified type) that have at least one of these tag key and value pairs are automatically retained in the Recycle Bin upon deletion. Use this type of retention rule to protect specific resources in your account based on their tags.</p> </li> <li> <p> <b>Region-level retention rules</b> - These retention rules, by default, apply to all of the resources (of the specified type) in the Region, even if the resources are not tagged. However, you can specify exclusion tags to exclude resources that have specific tags. Use this type of retention rule to protect all resources of a specific type in a Region.</p> </li> </ul> <p>For more information, see <a href="https://docs.aws.amazon.com/ebs/latest/userguide/recycle-bin.html"> Create Recycle Bin retention rules</a> in the <i>Amazon EBS User Guide</i>.</p>

        Args:
            retention_period: <p>Information about the retention period for which the retention rule is to retain resources.</p>
            description: <p>The retention rule description.</p>
            tags: <p>Information about the tags to assign to the retention rule.</p>
            resource_type: <p>The resource type to be retained by the retention rule. Currently, only EBS volumes, EBS snapshots, and EBS-backed AMIs are supported.</p> <ul> <li> <p>To retain EBS volumes, specify <code>EBS_VOLUME</code>.</p> </li> <li> <p>To retain EBS snapshots, specify <code>EBS_SNAPSHOT</code> </p> </li> <li> <p>To retain EBS-backed AMIs, specify <code>EC2_IMAGE</code>.</p> </li> </ul>
            resource_tags: <p>[Tag-level retention rules only] Specifies the resource tags to use to identify resources that are to be retained by a tag-level retention rule. For tag-level retention rules, only deleted resources, of the specified resource type, that have one or more of the specified tag key and value pairs are retained. If a resource is deleted, but it does not have any of the specified tag key and value pairs, it is immediately deleted without being retained by the retention rule.</p> <p>You can add the same tag key and value pair to a maximum or five retention rules.</p> <p>To create a Region-level retention rule, omit this parameter. A Region-level retention rule does not have any resource tags specified. It retains all deleted resources of the specified resource type in the Region in which the rule is created, even if the resources are not tagged.</p>
            lock_configuration: <p>Information about the retention rule lock configuration.</p>
            exclude_resource_tags: <p>[Region-level retention rules only] Specifies the exclusion tags to use to identify resources that are to be excluded, or ignored, by a Region-level retention rule. Resources that have any of these tags are not retained by the retention rule upon deletion.</p> <p>You can't specify exclusion tags for tag-level retention rules.</p>

        Raises:
            capo_rbin.errors.internal_server_exception.InternalServerException: <p>The service could not respond to the request due to an internal problem.</p>
            capo_rbin.errors.service_quota_exceeded_exception.ServiceQuotaExceededException: <p>The request would cause a service quota for the number of tags per resource to be exceeded.</p>
            capo_rbin.errors.validation_exception.ValidationException: <p>One or more of the parameters in the request is not valid.</p>
            capo_rbin.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        async def _handler(
            req: "AsyncOperationRequest[capo_rbin.types.create_rule_request.CreateRuleRequest]",
        ) -> AsyncOperationResponse[
            "capo_rbin.types.create_rule_response.CreateRuleResponse"
        ]:
            import capo_rbin._operations.amazon_recycle_bin.create_rule

            (
                output,
                http_response,
            ) = await capo_rbin._operations.amazon_recycle_bin.create_rule.async_create_rule(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_rbin.types.create_rule_request.CreateRuleRequest = {
            "retention_period": retention_period,
            "resource_type": resource_type,
        }
        if description is not None:
            input_["description"] = description
        if tags is not None:
            input_["tags"] = tags
        if resource_tags is not None:
            input_["resource_tags"] = resource_tags
        if lock_configuration is not None:
            input_["lock_configuration"] = lock_configuration
        if exclude_resource_tags is not None:
            input_["exclude_resource_tags"] = exclude_resource_tags

        response = await aexecute_pipeline(
            AsyncOperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        await response.response.aclose()
        return response.output

    async def delete_rule(
        self,
        identifier: "capo_rbin.types.rule_identifier.RuleIdentifier",
        *,
        config_overrides: Optional[AsyncrbinClientConfig] = None,
    ) -> "capo_rbin.types.delete_rule_response.DeleteRuleResponse":
        """<p>Deletes a Recycle Bin retention rule. For more information, see <a href="https://docs.aws.amazon.com/AWSEC2/latest/UserGuide/recycle-bin-working-with-rules.html#recycle-bin-delete-rule"> Delete Recycle Bin retention rules</a> in the <i>Amazon Elastic Compute Cloud User Guide</i>.</p>

        Args:
            identifier: <p>The unique ID of the retention rule.</p>

        Raises:
            capo_rbin.errors.conflict_exception.ConflictException: <p>The specified retention rule lock request can't be completed.</p>
            capo_rbin.errors.internal_server_exception.InternalServerException: <p>The service could not respond to the request due to an internal problem.</p>
            capo_rbin.errors.resource_not_found_exception.ResourceNotFoundException: <p>The specified resource was not found.</p>
            capo_rbin.errors.validation_exception.ValidationException: <p>One or more of the parameters in the request is not valid.</p>
            capo_rbin.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        async def _handler(
            req: "AsyncOperationRequest[capo_rbin.types.delete_rule_request.DeleteRuleRequest]",
        ) -> AsyncOperationResponse[
            "capo_rbin.types.delete_rule_response.DeleteRuleResponse"
        ]:
            import capo_rbin._operations.amazon_recycle_bin.delete_rule

            (
                output,
                http_response,
            ) = await capo_rbin._operations.amazon_recycle_bin.delete_rule.async_delete_rule(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_rbin.types.delete_rule_request.DeleteRuleRequest = {
            "identifier": identifier
        }

        response = await aexecute_pipeline(
            AsyncOperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        await response.response.aclose()
        return response.output

    async def get_rule(
        self,
        identifier: "capo_rbin.types.rule_identifier.RuleIdentifier",
        *,
        config_overrides: Optional[AsyncrbinClientConfig] = None,
    ) -> "capo_rbin.types.get_rule_response.GetRuleResponse":
        """<p>Gets information about a Recycle Bin retention rule.</p>

        Args:
            identifier: <p>The unique ID of the retention rule.</p>

        Raises:
            capo_rbin.errors.internal_server_exception.InternalServerException: <p>The service could not respond to the request due to an internal problem.</p>
            capo_rbin.errors.resource_not_found_exception.ResourceNotFoundException: <p>The specified resource was not found.</p>
            capo_rbin.errors.validation_exception.ValidationException: <p>One or more of the parameters in the request is not valid.</p>
            capo_rbin.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        async def _handler(
            req: "AsyncOperationRequest[capo_rbin.types.get_rule_request.GetRuleRequest]",
        ) -> AsyncOperationResponse[
            "capo_rbin.types.get_rule_response.GetRuleResponse"
        ]:
            import capo_rbin._operations.amazon_recycle_bin.get_rule

            (
                output,
                http_response,
            ) = await capo_rbin._operations.amazon_recycle_bin.get_rule.async_get_rule(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_rbin.types.get_rule_request.GetRuleRequest = {
            "identifier": identifier
        }

        response = await aexecute_pipeline(
            AsyncOperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        await response.response.aclose()
        return response.output

    async def list_rules(
        self,
        resource_type: "capo_rbin.types.resource_type.ResourceType",
        *,
        config_overrides: Optional[AsyncrbinClientConfig] = None,
        max_results: Optional["capo_rbin.types.max_results.MaxResults"] = None,
        next_token: Optional["capo_rbin.types.next_token.NextToken"] = None,
        resource_tags: Optional["capo_rbin.types.resource_tags.ResourceTags"] = None,
        lock_state: Optional["capo_rbin.types.lock_state.LockState"] = None,
        exclude_resource_tags: Optional[
            "capo_rbin.types.exclude_resource_tags.ExcludeResourceTags"
        ] = None,
    ) -> "capo_rbin.types.list_rules_response.ListRulesResponse":
        """<p>Lists the Recycle Bin retention rules in the Region.</p>

        Args:
            max_results: <p>The maximum number of results to return with a single call. To retrieve the remaining results, make another call with the returned <code>NextToken</code> value.</p>
            next_token: <p>The token for the next page of results.</p>
            resource_type: <p>The resource type retained by the retention rule. Only retention rules that retain the specified resource type are listed. Currently, only EBS volumes, EBS snapshots, and EBS-backed AMIs are supported.</p> <ul> <li> <p>To list retention rules that retain EBS volumes, specify <code>EBS_VOLUME</code>.</p> </li> <li> <p>To list retention rules that retain EBS snapshots, specify <code>EBS_SNAPSHOT</code>.</p> </li> <li> <p>To list retention rules that retain EBS-backed AMIs, specify <code>EC2_IMAGE</code>.</p> </li> </ul>
            resource_tags: <p>[Tag-level retention rules only] Information about the resource tags used to identify resources that are retained by the retention rule.</p>
            lock_state: <p>The lock state of the retention rules to list. Only retention rules with the specified lock state are returned.</p>
            exclude_resource_tags: <p>[Region-level retention rules only] Information about the exclusion tags used to identify resources that are to be excluded, or ignored, by the retention rule.</p>

        Raises:
            capo_rbin.errors.internal_server_exception.InternalServerException: <p>The service could not respond to the request due to an internal problem.</p>
            capo_rbin.errors.validation_exception.ValidationException: <p>One or more of the parameters in the request is not valid.</p>
            capo_rbin.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        async def _handler(
            req: "AsyncOperationRequest[capo_rbin.types.list_rules_request.ListRulesRequest]",
        ) -> AsyncOperationResponse[
            "capo_rbin.types.list_rules_response.ListRulesResponse"
        ]:
            import capo_rbin._operations.amazon_recycle_bin.list_rules

            (
                output,
                http_response,
            ) = await capo_rbin._operations.amazon_recycle_bin.list_rules.async_list_rules(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_rbin.types.list_rules_request.ListRulesRequest = {
            "resource_type": resource_type
        }
        if max_results is not None:
            input_["max_results"] = max_results
        if next_token is not None:
            input_["next_token"] = next_token
        if resource_tags is not None:
            input_["resource_tags"] = resource_tags
        if lock_state is not None:
            input_["lock_state"] = lock_state
        if exclude_resource_tags is not None:
            input_["exclude_resource_tags"] = exclude_resource_tags

        response = await aexecute_pipeline(
            AsyncOperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        await response.response.aclose()
        return response.output

    async def iter_list_rules(
        self,
        resource_type: "capo_rbin.types.resource_type.ResourceType",
        *,
        config_overrides: Optional[AsyncrbinClientConfig] = None,
        max_results: Optional["capo_rbin.types.max_results.MaxResults"] = None,
        next_token: Optional["capo_rbin.types.next_token.NextToken"] = None,
        resource_tags: Optional["capo_rbin.types.resource_tags.ResourceTags"] = None,
        lock_state: Optional["capo_rbin.types.lock_state.LockState"] = None,
        exclude_resource_tags: Optional[
            "capo_rbin.types.exclude_resource_tags.ExcludeResourceTags"
        ] = None,
    ) -> "AsyncIterator[capo_rbin.types.rule_summary.RuleSummary]":
        _token = next_token
        while True:
            _response = await self.list_rules(
                resource_type,
                config_overrides=config_overrides,
                max_results=max_results,
                next_token=_token,
                resource_tags=resource_tags,
                lock_state=lock_state,
                exclude_resource_tags=exclude_resource_tags,
            )
            _page = _resolve_path(_response, ("rules",))
            for _item in _page or []:
                yield _item
            _token = _resolve_path(_response, ("next_token",))
            if not _token:
                break

    async def list_tags_for_resource(
        self,
        resource_arn: "capo_rbin.types.rule_arn.RuleArn",
        *,
        config_overrides: Optional[AsyncrbinClientConfig] = None,
    ) -> "capo_rbin.types.list_tags_for_resource_response.ListTagsForResourceResponse":
        """<p>Lists the tags assigned to a retention rule.</p>

        Args:
            resource_arn: <p>The Amazon Resource Name (ARN) of the retention rule.</p>

        Raises:
            capo_rbin.errors.internal_server_exception.InternalServerException: <p>The service could not respond to the request due to an internal problem.</p>
            capo_rbin.errors.resource_not_found_exception.ResourceNotFoundException: <p>The specified resource was not found.</p>
            capo_rbin.errors.validation_exception.ValidationException: <p>One or more of the parameters in the request is not valid.</p>
            capo_rbin.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        async def _handler(
            req: "AsyncOperationRequest[capo_rbin.types.list_tags_for_resource_request.ListTagsForResourceRequest]",
        ) -> AsyncOperationResponse[
            "capo_rbin.types.list_tags_for_resource_response.ListTagsForResourceResponse"
        ]:
            import capo_rbin._operations.amazon_recycle_bin.list_tags_for_resource

            (
                output,
                http_response,
            ) = await capo_rbin._operations.amazon_recycle_bin.list_tags_for_resource.async_list_tags_for_resource(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_rbin.types.list_tags_for_resource_request.ListTagsForResourceRequest = {
            "resource_arn": resource_arn
        }

        response = await aexecute_pipeline(
            AsyncOperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        await response.response.aclose()
        return response.output

    async def lock_rule(
        self,
        identifier: "capo_rbin.types.rule_identifier.RuleIdentifier",
        lock_configuration: "capo_rbin.types.lock_configuration.LockConfiguration",
        *,
        config_overrides: Optional[AsyncrbinClientConfig] = None,
    ) -> "capo_rbin.types.lock_rule_response.LockRuleResponse":
        """<p>Locks a Region-level retention rule. A locked retention rule can't be modified or deleted.</p> <note> <p>You can't lock tag-level retention rules, or Region-level retention rules that have exclusion tags.</p> </note>

        Args:
            identifier: <p>The unique ID of the retention rule.</p>
            lock_configuration: <p>Information about the retention rule lock configuration.</p>

        Raises:
            capo_rbin.errors.conflict_exception.ConflictException: <p>The specified retention rule lock request can't be completed.</p>
            capo_rbin.errors.internal_server_exception.InternalServerException: <p>The service could not respond to the request due to an internal problem.</p>
            capo_rbin.errors.resource_not_found_exception.ResourceNotFoundException: <p>The specified resource was not found.</p>
            capo_rbin.errors.validation_exception.ValidationException: <p>One or more of the parameters in the request is not valid.</p>
            capo_rbin.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        async def _handler(
            req: "AsyncOperationRequest[capo_rbin.types.lock_rule_request.LockRuleRequest]",
        ) -> AsyncOperationResponse[
            "capo_rbin.types.lock_rule_response.LockRuleResponse"
        ]:
            import capo_rbin._operations.amazon_recycle_bin.lock_rule

            (
                output,
                http_response,
            ) = await capo_rbin._operations.amazon_recycle_bin.lock_rule.async_lock_rule(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_rbin.types.lock_rule_request.LockRuleRequest = {
            "identifier": identifier,
            "lock_configuration": lock_configuration,
        }

        response = await aexecute_pipeline(
            AsyncOperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        await response.response.aclose()
        return response.output

    async def tag_resource(
        self,
        resource_arn: "capo_rbin.types.rule_arn.RuleArn",
        tags: "capo_rbin.types.tag_list.TagList",
        *,
        config_overrides: Optional[AsyncrbinClientConfig] = None,
    ) -> "capo_rbin.types.tag_resource_response.TagResourceResponse":
        """<p>Assigns tags to the specified retention rule.</p>

        Args:
            resource_arn: <p>The Amazon Resource Name (ARN) of the retention rule.</p>
            tags: <p>Information about the tags to assign to the retention rule.</p>

        Raises:
            capo_rbin.errors.internal_server_exception.InternalServerException: <p>The service could not respond to the request due to an internal problem.</p>
            capo_rbin.errors.resource_not_found_exception.ResourceNotFoundException: <p>The specified resource was not found.</p>
            capo_rbin.errors.service_quota_exceeded_exception.ServiceQuotaExceededException: <p>The request would cause a service quota for the number of tags per resource to be exceeded.</p>
            capo_rbin.errors.validation_exception.ValidationException: <p>One or more of the parameters in the request is not valid.</p>
            capo_rbin.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        async def _handler(
            req: "AsyncOperationRequest[capo_rbin.types.tag_resource_request.TagResourceRequest]",
        ) -> AsyncOperationResponse[
            "capo_rbin.types.tag_resource_response.TagResourceResponse"
        ]:
            import capo_rbin._operations.amazon_recycle_bin.tag_resource

            (
                output,
                http_response,
            ) = await capo_rbin._operations.amazon_recycle_bin.tag_resource.async_tag_resource(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_rbin.types.tag_resource_request.TagResourceRequest = {
            "resource_arn": resource_arn,
            "tags": tags,
        }

        response = await aexecute_pipeline(
            AsyncOperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        await response.response.aclose()
        return response.output

    async def unlock_rule(
        self,
        identifier: "capo_rbin.types.rule_identifier.RuleIdentifier",
        *,
        config_overrides: Optional[AsyncrbinClientConfig] = None,
    ) -> "capo_rbin.types.unlock_rule_response.UnlockRuleResponse":
        """<p>Unlocks a retention rule. After a retention rule is unlocked, it can be modified or deleted only after the unlock delay period expires.</p>

        Args:
            identifier: <p>The unique ID of the retention rule.</p>

        Raises:
            capo_rbin.errors.conflict_exception.ConflictException: <p>The specified retention rule lock request can't be completed.</p>
            capo_rbin.errors.internal_server_exception.InternalServerException: <p>The service could not respond to the request due to an internal problem.</p>
            capo_rbin.errors.resource_not_found_exception.ResourceNotFoundException: <p>The specified resource was not found.</p>
            capo_rbin.errors.validation_exception.ValidationException: <p>One or more of the parameters in the request is not valid.</p>
            capo_rbin.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        async def _handler(
            req: "AsyncOperationRequest[capo_rbin.types.unlock_rule_request.UnlockRuleRequest]",
        ) -> AsyncOperationResponse[
            "capo_rbin.types.unlock_rule_response.UnlockRuleResponse"
        ]:
            import capo_rbin._operations.amazon_recycle_bin.unlock_rule

            (
                output,
                http_response,
            ) = await capo_rbin._operations.amazon_recycle_bin.unlock_rule.async_unlock_rule(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_rbin.types.unlock_rule_request.UnlockRuleRequest = {
            "identifier": identifier
        }

        response = await aexecute_pipeline(
            AsyncOperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        await response.response.aclose()
        return response.output

    async def untag_resource(
        self,
        resource_arn: "capo_rbin.types.rule_arn.RuleArn",
        tag_keys: "capo_rbin.types.tag_key_list.TagKeyList",
        *,
        config_overrides: Optional[AsyncrbinClientConfig] = None,
    ) -> "capo_rbin.types.untag_resource_response.UntagResourceResponse":
        """<p>Unassigns a tag from a retention rule.</p>

        Args:
            resource_arn: <p>The Amazon Resource Name (ARN) of the retention rule.</p>
            tag_keys: <p>The tag keys of the tags to unassign. All tags that have the specified tag key are unassigned.</p>

        Raises:
            capo_rbin.errors.internal_server_exception.InternalServerException: <p>The service could not respond to the request due to an internal problem.</p>
            capo_rbin.errors.resource_not_found_exception.ResourceNotFoundException: <p>The specified resource was not found.</p>
            capo_rbin.errors.validation_exception.ValidationException: <p>One or more of the parameters in the request is not valid.</p>
            capo_rbin.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        async def _handler(
            req: "AsyncOperationRequest[capo_rbin.types.untag_resource_request.UntagResourceRequest]",
        ) -> AsyncOperationResponse[
            "capo_rbin.types.untag_resource_response.UntagResourceResponse"
        ]:
            import capo_rbin._operations.amazon_recycle_bin.untag_resource

            (
                output,
                http_response,
            ) = await capo_rbin._operations.amazon_recycle_bin.untag_resource.async_untag_resource(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_rbin.types.untag_resource_request.UntagResourceRequest = {
            "resource_arn": resource_arn,
            "tag_keys": tag_keys,
        }

        response = await aexecute_pipeline(
            AsyncOperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        await response.response.aclose()
        return response.output

    async def update_rule(
        self,
        identifier: "capo_rbin.types.rule_identifier.RuleIdentifier",
        *,
        config_overrides: Optional[AsyncrbinClientConfig] = None,
        retention_period: Optional[
            "capo_rbin.types.retention_period.RetentionPeriod"
        ] = None,
        description: Optional["capo_rbin.types.description.Description"] = None,
        resource_type: Optional["capo_rbin.types.resource_type.ResourceType"] = None,
        resource_tags: Optional["capo_rbin.types.resource_tags.ResourceTags"] = None,
        exclude_resource_tags: Optional[
            "capo_rbin.types.exclude_resource_tags.ExcludeResourceTags"
        ] = None,
    ) -> "capo_rbin.types.update_rule_response.UpdateRuleResponse":
        """<p>Updates an existing Recycle Bin retention rule. You can update a retention rule's description, resource tags, and retention period at any time after creation. You can't update a retention rule's resource type after creation. For more information, see <a href="https://docs.aws.amazon.com/AWSEC2/latest/UserGuide/recycle-bin-working-with-rules.html#recycle-bin-update-rule"> Update Recycle Bin retention rules</a> in the <i>Amazon Elastic Compute Cloud User Guide</i>.</p>

        Args:
            identifier: <p>The unique ID of the retention rule.</p>
            retention_period: <p>Information about the retention period for which the retention rule is to retain resources.</p>
            description: <p>The retention rule description.</p>
            resource_type: <note> <p>This parameter is currently not supported. You can't update a retention rule's resource type after creation.</p> </note>
            resource_tags: <p>[Tag-level retention rules only] Specifies the resource tags to use to identify resources that are to be retained by a tag-level retention rule. For tag-level retention rules, only deleted resources, of the specified resource type, that have one or more of the specified tag key and value pairs are retained. If a resource is deleted, but it does not have any of the specified tag key and value pairs, it is immediately deleted without being retained by the retention rule.</p> <p>You can add the same tag key and value pair to a maximum or five retention rules.</p> <p>To create a Region-level retention rule, omit this parameter. A Region-level retention rule does not have any resource tags specified. It retains all deleted resources of the specified resource type in the Region in which the rule is created, even if the resources are not tagged.</p>
            exclude_resource_tags: <p>[Region-level retention rules only] Specifies the exclusion tags to use to identify resources that are to be excluded, or ignored, by a Region-level retention rule. Resources that have any of these tags are not retained by the retention rule upon deletion.</p> <p>You can't specify exclusion tags for tag-level retention rules.</p>

        Raises:
            capo_rbin.errors.conflict_exception.ConflictException: <p>The specified retention rule lock request can't be completed.</p>
            capo_rbin.errors.internal_server_exception.InternalServerException: <p>The service could not respond to the request due to an internal problem.</p>
            capo_rbin.errors.resource_not_found_exception.ResourceNotFoundException: <p>The specified resource was not found.</p>
            capo_rbin.errors.service_quota_exceeded_exception.ServiceQuotaExceededException: <p>The request would cause a service quota for the number of tags per resource to be exceeded.</p>
            capo_rbin.errors.validation_exception.ValidationException: <p>One or more of the parameters in the request is not valid.</p>
            capo_rbin.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        async def _handler(
            req: "AsyncOperationRequest[capo_rbin.types.update_rule_request.UpdateRuleRequest]",
        ) -> AsyncOperationResponse[
            "capo_rbin.types.update_rule_response.UpdateRuleResponse"
        ]:
            import capo_rbin._operations.amazon_recycle_bin.update_rule

            (
                output,
                http_response,
            ) = await capo_rbin._operations.amazon_recycle_bin.update_rule.async_update_rule(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_rbin.types.update_rule_request.UpdateRuleRequest = {
            "identifier": identifier
        }
        if retention_period is not None:
            input_["retention_period"] = retention_period
        if description is not None:
            input_["description"] = description
        if resource_type is not None:
            input_["resource_type"] = resource_type
        if resource_tags is not None:
            input_["resource_tags"] = resource_tags
        if exclude_resource_tags is not None:
            input_["exclude_resource_tags"] = exclude_resource_tags

        response = await aexecute_pipeline(
            AsyncOperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        await response.response.aclose()
        return response.output

    async def __aenter__(self) -> Self:
        return self

    async def __aexit__(self, exc_type: Any, exc: Any, tb: Any):
        await self._client.aclose()
