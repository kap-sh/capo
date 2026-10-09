"""Generated from Smithy shape ``com.amazonaws.resourcegroupstaggingapi#ResourceGroupsTaggingAPI_20170126``."""

import warnings
from collections.abc import AsyncIterator
from typing import TYPE_CHECKING, Any, Iterable, Optional

from typing_extensions import Self, TypedDict
from zapros import AsyncBaseHandler, AsyncClient

import capo_resource_groups_tagging_api._auth._signers
import capo_resource_groups_tagging_api._auth._sigv4
from capo_resource_groups_tagging_api._auth._identity import Credentials
from capo_resource_groups_tagging_api._auth._providers import (
    CredentialsProvider,
    IdentityProvider,
    StaticAwsCredentialsProvider,
    default_aws_credentials_chain,
)
from capo_resource_groups_tagging_api._auth._zapros_handler import AuthMiddleware
from capo_resource_groups_tagging_api._pagination import resolve_path as _resolve_path
from capo_resource_groups_tagging_api._services._aws_config import aaws_config
from capo_resource_groups_tagging_api._services._pipeline import (
    AsyncInterceptor,
    AsyncOperationOptions,
    AsyncOperationRequest,
    AsyncOperationResponse,
    aexecute_pipeline,
    aretry,
)

if TYPE_CHECKING:
    import capo_resource_groups_tagging_api.types.describe_report_creation_input
    import capo_resource_groups_tagging_api.types.describe_report_creation_output
    import capo_resource_groups_tagging_api.types.exclude_compliant_resources
    import capo_resource_groups_tagging_api.types.get_compliance_summary_input
    import capo_resource_groups_tagging_api.types.get_compliance_summary_output
    import capo_resource_groups_tagging_api.types.get_resources_input
    import capo_resource_groups_tagging_api.types.get_resources_output
    import capo_resource_groups_tagging_api.types.get_tag_keys_input
    import capo_resource_groups_tagging_api.types.get_tag_keys_output
    import capo_resource_groups_tagging_api.types.get_tag_values_input
    import capo_resource_groups_tagging_api.types.get_tag_values_output
    import capo_resource_groups_tagging_api.types.group_by
    import capo_resource_groups_tagging_api.types.include_compliance_details
    import capo_resource_groups_tagging_api.types.list_required_tags_input
    import capo_resource_groups_tagging_api.types.list_required_tags_output
    import capo_resource_groups_tagging_api.types.max_results_for_list_required_tags
    import capo_resource_groups_tagging_api.types.max_results_get_compliance_summary
    import capo_resource_groups_tagging_api.types.pagination_token
    import capo_resource_groups_tagging_api.types.region_filter_list
    import capo_resource_groups_tagging_api.types.required_tag
    import capo_resource_groups_tagging_api.types.resource_arn_list_for_get
    import capo_resource_groups_tagging_api.types.resource_arn_list_for_tag_untag
    import capo_resource_groups_tagging_api.types.resource_tag_mapping
    import capo_resource_groups_tagging_api.types.resource_type_filter_list
    import capo_resource_groups_tagging_api.types.resources_per_page
    import capo_resource_groups_tagging_api.types.s3_bucket
    import capo_resource_groups_tagging_api.types.start_report_creation_input
    import capo_resource_groups_tagging_api.types.start_report_creation_output
    import capo_resource_groups_tagging_api.types.summary
    import capo_resource_groups_tagging_api.types.tag_filter_list
    import capo_resource_groups_tagging_api.types.tag_key
    import capo_resource_groups_tagging_api.types.tag_key_filter_list
    import capo_resource_groups_tagging_api.types.tag_key_list_for_untag
    import capo_resource_groups_tagging_api.types.tag_map
    import capo_resource_groups_tagging_api.types.tag_resources_input
    import capo_resource_groups_tagging_api.types.tag_resources_output
    import capo_resource_groups_tagging_api.types.tag_value
    import capo_resource_groups_tagging_api.types.tags_per_page
    import capo_resource_groups_tagging_api.types.target_id_filter_list
    import capo_resource_groups_tagging_api.types.untag_resources_input
    import capo_resource_groups_tagging_api.types.untag_resources_output


class AsyncResourceGroupsTaggingAPIClientConfig(TypedDict, total=False, closed=True):
    operation_interceptors: Iterable[AsyncInterceptor[Any, Any]]
    retry_max_attempts: int | None
    region: str | None
    use_dual_stack: bool | None
    use_fips: bool | None
    endpoint: str | None
    credentials_provider: IdentityProvider[Credentials] | None
    anonymous: bool | None


class AsyncResourceGroupsTaggingAPIClient:
    """A client for the ``ResourceGroupsTaggingAPI`` service.

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
        http_handler: AsyncBaseHandler | None = None,
        operation_interceptors: Iterable[AsyncInterceptor[Any, Any]] | None = None,
        retry_max_attempts: int | None = None,
        region: str | None = None,
        use_dual_stack: bool | None = None,
        use_fips: bool | None = None,
        endpoint: str | None = None,
        credentials: Credentials | None = None,
        credentials_provider: CredentialsProvider | None = None,
        anonymous: bool | None = None,
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
        self._config = AsyncResourceGroupsTaggingAPIClientConfig(
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
        config_overrides: Optional[AsyncResourceGroupsTaggingAPIClientConfig] = None,
    ) -> tuple[Iterable[AsyncInterceptor[Any, Any]], AsyncOperationOptions]:
        overrides: AsyncResourceGroupsTaggingAPIClientConfig = config_overrides or {}
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
            anonymous=overrides.get("anonymous", self._config.get("anonymous")),
        )
        return interceptors_, options_

    async def describe_report_creation(
        self,
        *,
        config_overrides: Optional[AsyncResourceGroupsTaggingAPIClientConfig] = None,
    ) -> "capo_resource_groups_tagging_api.types.describe_report_creation_output.DescribeReportCreationOutput":
        """<p>Describes the status of the <code>StartReportCreation</code> operation. </p> <p>You can call this operation only from the organization's management account and from the us-east-1 Region.</p>

        Raises:
            capo_resource_groups_tagging_api.errors.constraint_violation_exception.ConstraintViolationException: <p>The request failed because performing the operation would violate a constraint.</p> <p>Some of the reasons in the following list might not apply to this specific operation.</p> <ul> <li> <p>You must meet the prerequisites for using tag policies. For information, see <a href="https://docs.aws.amazon.com/tag-editor/latest/userguide/tag-policies-orgs.html#tag-policies-prereqs">Prerequisites and permissions</a> in the <i>Tagging Amazon Web Services resources and Tag Editor</i> user guide. </p> </li> <li> <p>You must enable the tag policies service principal (<code>tagpolicies.tag.amazonaws.com</code>) to integrate with Organizations For information, see <a href="https://docs.aws.amazon.com/organizations/latest/APIReference/API_EnableAWSServiceAccess.html">EnableAWSServiceAccess</a>.</p> </li> <li> <p>You must have a tag policy attached to the organization root, an OU, or an account.</p> </li> </ul>
            capo_resource_groups_tagging_api.errors.internal_service_exception.InternalServiceException: <p>The request processing failed because of an unknown error, exception, or failure. You can retry the request.</p>
            capo_resource_groups_tagging_api.errors.invalid_parameter_exception.InvalidParameterException: <p>The request failed because of one of the following reasons:</p> <ul> <li> <p>A required parameter is missing.</p> </li> <li> <p>A provided string parameter is malformed.</p> </li> <li> <p>An provided parameter value is out of range.</p> </li> <li> <p>The target ID is invalid, unsupported, or doesn't exist.</p> </li> <li> <p>You can't access the Amazon S3 bucket for report storage. For more information, see <a href="https://docs.aws.amazon.com/tag-editor/latest/userguide/tag-policies-orgs.html#bucket-policy">Amazon S3 bucket policy for report storage</a> in the <i>Tagging Amazon Web Services resources and Tag Editor</i> user guide. </p> </li> <li> <p>The partition specified in an ARN parameter in the request doesn't match the partition where you invoked the operation. The partition is specified by the second field of the ARN.</p> </li> </ul>
            capo_resource_groups_tagging_api.errors.throttled_exception.ThrottledException: <p>The request failed because it exceeded the allowed frequency of submitted requests.</p>
            capo_resource_groups_tagging_api.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        async def _handler(
            req: "AsyncOperationRequest[capo_resource_groups_tagging_api.types.describe_report_creation_input.DescribeReportCreationInput]",
        ) -> AsyncOperationResponse[
            "capo_resource_groups_tagging_api.types.describe_report_creation_output.DescribeReportCreationOutput"
        ]:
            import capo_resource_groups_tagging_api._operations.resource_groups_tagging_api_20170126.describe_report_creation

            (
                output,
                http_response,
            ) = await capo_resource_groups_tagging_api._operations.resource_groups_tagging_api_20170126.describe_report_creation.async_describe_report_creation(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_resource_groups_tagging_api.types.describe_report_creation_input.DescribeReportCreationInput = {}

        response = await aexecute_pipeline(
            AsyncOperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        await response.response.aclose()
        return response.output

    async def get_compliance_summary(
        self,
        *,
        config_overrides: Optional[AsyncResourceGroupsTaggingAPIClientConfig] = None,
        target_id_filters: Optional[
            "capo_resource_groups_tagging_api.types.target_id_filter_list.TargetIdFilterList"
        ] = None,
        region_filters: Optional[
            "capo_resource_groups_tagging_api.types.region_filter_list.RegionFilterList"
        ] = None,
        resource_type_filters: Optional[
            "capo_resource_groups_tagging_api.types.resource_type_filter_list.ResourceTypeFilterList"
        ] = None,
        tag_key_filters: Optional[
            "capo_resource_groups_tagging_api.types.tag_key_filter_list.TagKeyFilterList"
        ] = None,
        group_by: Optional[
            "capo_resource_groups_tagging_api.types.group_by.GroupBy"
        ] = None,
        max_results: Optional[
            "capo_resource_groups_tagging_api.types.max_results_get_compliance_summary.MaxResultsGetComplianceSummary"
        ] = None,
        pagination_token: Optional[
            "capo_resource_groups_tagging_api.types.pagination_token.PaginationToken"
        ] = None,
    ) -> "capo_resource_groups_tagging_api.types.get_compliance_summary_output.GetComplianceSummaryOutput":
        """<p>Returns a table that shows counts of resources that are noncompliant with their tag policies.</p> <p>For more information on tag policies, see <a href="https://docs.aws.amazon.com/organizations/latest/userguide/orgs_manage_policies_tag-policies.html">Tag Policies</a> in the <i>Organizations User Guide.</i> </p> <p>You can call this operation only from the organization's management account and from the us-east-1 Region.</p> <p>This operation supports pagination, where the response can be sent in multiple pages. You should check the <code>PaginationToken</code> response parameter to determine if there are additional results available to return. Repeat the query, passing the <code>PaginationToken</code> response parameter value as an input to the next request until you recieve a <code>null</code> value. A null value for <code>PaginationToken</code> indicates that there are no more results waiting to be returned.</p>

        Args:
            target_id_filters: <p>Specifies target identifiers (usually, specific account IDs) to limit the output by. If you use this parameter, the count of returned noncompliant resources includes only resources with the specified target IDs.</p>
            region_filters: <p>Specifies a list of Amazon Web Services Regions to limit the output to. If you use this parameter, the count of returned noncompliant resources includes only resources in the specified Regions.</p>
            resource_type_filters: <p>Specifies that you want the response to include information for only resources of the specified types. The format of each resource type is <code>service[:resourceType]</code>. For example, specifying a resource type of <code>ec2</code> returns all Amazon EC2 resources (which includes EC2 instances). Specifying a resource type of <code>ec2:instance</code> returns only EC2 instances.</p> <p>The string for each service name and resource type is the same as that embedded in a resource's Amazon Resource Name (ARN). Consult the <i> <a href="https://docs.aws.amazon.com/general/latest/gr/">Amazon Web Services General Reference</a> </i> for the following:</p> <ul> <li> <p>For a list of service name strings, see <a href="https://docs.aws.amazon.com/general/latest/gr/aws-arns-and-namespaces.html#genref-aws-service-namespaces">Amazon Web Services Service Namespaces</a>.</p> </li> <li> <p>For resource type strings, see <a href="https://docs.aws.amazon.com/general/latest/gr/aws-arns-and-namespaces.html#arns-syntax">Example ARNs</a>.</p> </li> <li> <p>For more information about ARNs, see <a href="https://docs.aws.amazon.com/general/latest/gr/aws-arns-and-namespaces.html">Amazon Resource Names (ARNs) and Amazon Web Services Service Namespaces</a>.</p> </li> </ul> <note> <p>For the list of services whose resources you can tag using the Resource Groups Tagging API, see <a href="https://docs.aws.amazon.com/resourcegroupstagging/latest/APIReference/supported-services.html">Services that support the Resource Groups Tagging API</a>. If an Amazon Web Services service isn't listed on that page, you might still be able to tag that service's resources by using that service's native tagging operations instead of using Resource Groups Tagging API operations. All tagged resources, whether the tagging used the Resource Groups Tagging API or not, are returned by the <code>Get*</code> operation.</p> </note> <p>You can specify multiple resource types by using a comma separated array. The array can include up to 100 items. Note that the length constraint requirement applies to each resource type filter. </p>
            tag_key_filters: <p>Specifies that you want the response to include information for only resources that have tags with the specified tag keys. If you use this parameter, the count of returned noncompliant resources includes only resources that have the specified tag keys.</p>
            group_by: <p>Specifies a list of attributes to group the counts of noncompliant resources by. If supplied, the counts are sorted by those attributes.</p>
            max_results: <p>Specifies the maximum number of results to be returned in each page. A query can return fewer than this maximum, even if there are more results still to return. You should always check the <code>PaginationToken</code> response value to see if there are more results. You can specify a minimum of 1 and a maximum value of 100.</p>
            pagination_token: <p>Specifies a <code>PaginationToken</code> response value from a previous request to indicate that you want the next page of results. Leave this parameter empty in your initial request.</p>

        Raises:
            capo_resource_groups_tagging_api.errors.constraint_violation_exception.ConstraintViolationException: <p>The request failed because performing the operation would violate a constraint.</p> <p>Some of the reasons in the following list might not apply to this specific operation.</p> <ul> <li> <p>You must meet the prerequisites for using tag policies. For information, see <a href="https://docs.aws.amazon.com/tag-editor/latest/userguide/tag-policies-orgs.html#tag-policies-prereqs">Prerequisites and permissions</a> in the <i>Tagging Amazon Web Services resources and Tag Editor</i> user guide. </p> </li> <li> <p>You must enable the tag policies service principal (<code>tagpolicies.tag.amazonaws.com</code>) to integrate with Organizations For information, see <a href="https://docs.aws.amazon.com/organizations/latest/APIReference/API_EnableAWSServiceAccess.html">EnableAWSServiceAccess</a>.</p> </li> <li> <p>You must have a tag policy attached to the organization root, an OU, or an account.</p> </li> </ul>
            capo_resource_groups_tagging_api.errors.internal_service_exception.InternalServiceException: <p>The request processing failed because of an unknown error, exception, or failure. You can retry the request.</p>
            capo_resource_groups_tagging_api.errors.invalid_parameter_exception.InvalidParameterException: <p>The request failed because of one of the following reasons:</p> <ul> <li> <p>A required parameter is missing.</p> </li> <li> <p>A provided string parameter is malformed.</p> </li> <li> <p>An provided parameter value is out of range.</p> </li> <li> <p>The target ID is invalid, unsupported, or doesn't exist.</p> </li> <li> <p>You can't access the Amazon S3 bucket for report storage. For more information, see <a href="https://docs.aws.amazon.com/tag-editor/latest/userguide/tag-policies-orgs.html#bucket-policy">Amazon S3 bucket policy for report storage</a> in the <i>Tagging Amazon Web Services resources and Tag Editor</i> user guide. </p> </li> <li> <p>The partition specified in an ARN parameter in the request doesn't match the partition where you invoked the operation. The partition is specified by the second field of the ARN.</p> </li> </ul>
            capo_resource_groups_tagging_api.errors.throttled_exception.ThrottledException: <p>The request failed because it exceeded the allowed frequency of submitted requests.</p>
            capo_resource_groups_tagging_api.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        async def _handler(
            req: "AsyncOperationRequest[capo_resource_groups_tagging_api.types.get_compliance_summary_input.GetComplianceSummaryInput]",
        ) -> AsyncOperationResponse[
            "capo_resource_groups_tagging_api.types.get_compliance_summary_output.GetComplianceSummaryOutput"
        ]:
            import capo_resource_groups_tagging_api._operations.resource_groups_tagging_api_20170126.get_compliance_summary

            (
                output,
                http_response,
            ) = await capo_resource_groups_tagging_api._operations.resource_groups_tagging_api_20170126.get_compliance_summary.async_get_compliance_summary(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_resource_groups_tagging_api.types.get_compliance_summary_input.GetComplianceSummaryInput = {}
        if target_id_filters is not None:
            input_["target_id_filters"] = target_id_filters
        if region_filters is not None:
            input_["region_filters"] = region_filters
        if resource_type_filters is not None:
            input_["resource_type_filters"] = resource_type_filters
        if tag_key_filters is not None:
            input_["tag_key_filters"] = tag_key_filters
        if group_by is not None:
            input_["group_by"] = group_by
        if max_results is not None:
            input_["max_results"] = max_results
        if pagination_token is not None:
            input_["pagination_token"] = pagination_token

        response = await aexecute_pipeline(
            AsyncOperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        await response.response.aclose()
        return response.output

    async def iter_get_compliance_summary(
        self,
        *,
        config_overrides: Optional[AsyncResourceGroupsTaggingAPIClientConfig] = None,
        target_id_filters: Optional[
            "capo_resource_groups_tagging_api.types.target_id_filter_list.TargetIdFilterList"
        ] = None,
        region_filters: Optional[
            "capo_resource_groups_tagging_api.types.region_filter_list.RegionFilterList"
        ] = None,
        resource_type_filters: Optional[
            "capo_resource_groups_tagging_api.types.resource_type_filter_list.ResourceTypeFilterList"
        ] = None,
        tag_key_filters: Optional[
            "capo_resource_groups_tagging_api.types.tag_key_filter_list.TagKeyFilterList"
        ] = None,
        group_by: Optional[
            "capo_resource_groups_tagging_api.types.group_by.GroupBy"
        ] = None,
        max_results: Optional[
            "capo_resource_groups_tagging_api.types.max_results_get_compliance_summary.MaxResultsGetComplianceSummary"
        ] = None,
        pagination_token: Optional[
            "capo_resource_groups_tagging_api.types.pagination_token.PaginationToken"
        ] = None,
    ) -> "AsyncIterator[capo_resource_groups_tagging_api.types.summary.Summary]":
        _token = pagination_token
        while True:
            _response = await self.get_compliance_summary(
                config_overrides=config_overrides,
                target_id_filters=target_id_filters,
                region_filters=region_filters,
                resource_type_filters=resource_type_filters,
                tag_key_filters=tag_key_filters,
                group_by=group_by,
                max_results=max_results,
                pagination_token=_token,
            )
            _page = _resolve_path(_response, ("summary_list",))
            for _item in _page or []:
                yield _item
            _token = _resolve_path(_response, ("pagination_token",))
            if not _token:
                break

    async def get_resources(
        self,
        *,
        config_overrides: Optional[AsyncResourceGroupsTaggingAPIClientConfig] = None,
        pagination_token: Optional[
            "capo_resource_groups_tagging_api.types.pagination_token.PaginationToken"
        ] = None,
        tag_filters: Optional[
            "capo_resource_groups_tagging_api.types.tag_filter_list.TagFilterList"
        ] = None,
        resources_per_page: Optional[
            "capo_resource_groups_tagging_api.types.resources_per_page.ResourcesPerPage"
        ] = None,
        tags_per_page: Optional[
            "capo_resource_groups_tagging_api.types.tags_per_page.TagsPerPage"
        ] = None,
        resource_type_filters: Optional[
            "capo_resource_groups_tagging_api.types.resource_type_filter_list.ResourceTypeFilterList"
        ] = None,
        include_compliance_details: Optional[
            "capo_resource_groups_tagging_api.types.include_compliance_details.IncludeComplianceDetails"
        ] = None,
        exclude_compliant_resources: Optional[
            "capo_resource_groups_tagging_api.types.exclude_compliant_resources.ExcludeCompliantResources"
        ] = None,
        resource_arn_list: Optional[
            "capo_resource_groups_tagging_api.types.resource_arn_list_for_get.ResourceARNListForGet"
        ] = None,
    ) -> (
        "capo_resource_groups_tagging_api.types.get_resources_output.GetResourcesOutput"
    ):
        """<p>Returns all the tagged or previously tagged resources that are located in the specified Amazon Web Services Region for the account. </p> <p>Depending on what information you want returned, you can also specify the following:</p> <ul> <li> <p> <i>Filters</i> that specify what tags and resource types you want returned. The response includes all tags that are associated with the requested resources.</p> </li> <li> <p>Information about compliance with the account's effective tag policy. For more information on tag policies, see <a href="https://docs.aws.amazon.com/organizations/latest/userguide/orgs_manage_policies_tag-policies.html">Tag Policies</a> in the <i>Organizations User Guide.</i> </p> </li> </ul> <p>This operation supports pagination, where the response can be sent in multiple pages. You should check the <code>PaginationToken</code> response parameter to determine if there are additional results available to return. Repeat the query, passing the <code>PaginationToken</code> response parameter value as an input to the next request until you recieve a <code>null</code> value. A null value for <code>PaginationToken</code> indicates that there are no more results waiting to be returned.</p> <note> <p> <code>GetResources</code> does not return untagged resources. </p> <p>To find untagged resources in your account, use Amazon Web Services Resource Explorer with a query that uses <code>tag:none</code>. For more information, see <a href="https://docs.aws.amazon.com/resource-explorer/latest/userguide/using-search-query-syntax.html"> Search query syntax reference for Resource Explorer</a>. </p> </note>

        Args:
            pagination_token: <p>Specifies a <code>PaginationToken</code> response value from a previous request to indicate that you want the next page of results. Leave this parameter empty in your initial request.</p>
            tag_filters: <p>Specifies a list of TagFilters (keys and values) to restrict the output to only those resources that have tags with the specified keys and, if included, the specified values. Each <code>TagFilter</code> must contain a key with values optional. A request can include up to 50 keys, and each key can include up to 20 values. </p> <p>You can't specify both this parameter and the <code>ResourceArnList</code> parameter in the same request. If you do, you get an <code>Invalid Parameter</code> exception.</p> <p>Note the following when deciding how to use TagFilters:</p> <ul> <li> <p>If you <i>don't</i> specify a <code>TagFilter</code>, the response includes all resources that are currently tagged or ever had a tag. Resources that were previously tagged, <i>but do not currently</i> have tags, are shown with an empty tag set, like this: <code>"Tags": []</code>.</p> </li> <li> <p>If you specify more than one filter in a single request, the response returns only those resources that satisfy all filters.</p> </li> <li> <p>If you specify a filter that contains more than one value for a key, the response returns resources that match <i>any</i> of the specified values for that key.</p> </li> <li> <p>If you don't specify a value for a key, the response returns all resources that are tagged with that key, with any or no value.</p> <p>For example, for the following filters: <code>filter1= {key1,{value1}}</code>, <code>filter2={key2,{value2,value3,value4}}</code>, <code>filter3= {key3}</code>:</p> <ul> <li> <p> <code>GetResources({filter1})</code> returns resources tagged with <code>key1=value1</code> </p> </li> <li> <p> <code>GetResources({filter2})</code> returns resources tagged with <code>key2=value2</code> or <code>key2=value3</code> or <code>key2=value4</code> </p> </li> <li> <p> <code>GetResources({filter3})</code> returns resources tagged with any tag with the key <code>key3</code>, and with any or no value</p> </li> <li> <p> <code>GetResources({filter1,filter2,filter3})</code> returns resources tagged with <code>(key1=value1) and (key2=value2 or key2=value3 or key2=value4) and (key3, any or no value)</code> </p> </li> </ul> </li> </ul>
            resources_per_page: <p>Specifies the maximum number of results to be returned in each page. A query can return fewer than this maximum, even if there are more results still to return. You should always check the <code>PaginationToken</code> response value to see if there are more results. You can specify a minimum of 1 and a maximum value of 100.</p>
            tags_per_page: <p>Amazon Web Services recommends using <code>ResourcesPerPage</code> instead of this parameter.</p> <p>A limit that restricts the number of tags (key and value pairs) returned by <code>GetResources</code> in paginated output. A resource with no tags is counted as having one tag (one key and value pair).</p> <p> <code>GetResources</code> does not split a resource and its associated tags across pages. If the specified <code>TagsPerPage</code> would cause such a break, a <code>PaginationToken</code> is returned in place of the affected resource and its tags. Use that token in another request to get the remaining data. For example, if you specify a <code>TagsPerPage</code> of <code>100</code> and the account has 22 resources with 10 tags each (meaning that each resource has 10 key and value pairs), the output will consist of three pages. The first page displays the first 10 resources, each with its 10 tags. The second page displays the next 10 resources, each with its 10 tags. The third page displays the remaining 2 resources, each with its 10 tags.</p> <p>You can set <code>TagsPerPage</code> to a minimum of 100 items up to a maximum of 500 items.</p>
            resource_type_filters: <p>Specifies the resource types that you want included in the response. The format of each resource type is <code>service[:resourceType]</code>. For example, specifying a service of <code>ec2</code> returns all Amazon EC2 resources (which includes EC2 instances). Specifying a resource type of <code>ec2:instance</code> returns only EC2 instances. </p> <p>You can't specify both this parameter and the <code>ResourceArnList</code> parameter in the same request. If you do, you get an <code>Invalid Parameter</code> exception.</p> <p>The string for each service name and resource type is the same as that embedded in a resource's Amazon Resource Name (ARN).</p> <note> <p>For the list of services whose resources you can tag using the Resource Groups Tagging API, see <a href="https://docs.aws.amazon.com/resourcegroupstagging/latest/APIReference/supported-services.html">Services that support the Resource Groups Tagging API</a>. If an Amazon Web Services service isn't listed on that page, you might still be able to tag that service's resources by using that service's native tagging operations instead of using Resource Groups Tagging API operations. All tagged resources, whether the tagging used the Resource Groups Tagging API or not, are returned by the <code>Get*</code> operation.</p> </note> <p>You can specify multiple resource types by using an array. The array can include up to 100 items. Note that the length constraint requirement applies to each resource type filter. For example, the following string would limit the response to only Amazon EC2 instances, Amazon S3 buckets, or any Audit Manager resource:</p> <p> <code>ec2:instance,s3:bucket,auditmanager</code> </p>
            include_compliance_details: <p>Specifies whether to include details regarding the compliance with the effective tag policy. Set this to <code>true</code> to determine whether resources are compliant with the tag policy and to get details.</p>
            exclude_compliant_resources: <p>Specifies whether to exclude resources that are compliant with the tag policy. Set this to <code>true</code> if you are interested in retrieving information on noncompliant resources only.</p> <p>You can use this parameter only if the <code>IncludeComplianceDetails</code> parameter is also set to <code>true</code>.</p>
            resource_arn_list: <p>Specifies a list of ARNs of resources for which you want to retrieve tag data.</p> <p>You can't specify both this parameter and the <code>ResourceTypeFilters</code> parameter in the same request. If you do, you get an <code>Invalid Parameter</code> exception.</p> <p>You can't specify both this parameter and the <code>TagFilters</code> parameter in the same request. If you do, you get an <code>Invalid Parameter</code> exception.</p> <p>You can't specify both this parameter and any of the pagination parameters (<code>ResourcesPerPage</code>, <code>TagsPerPage</code>, <code>PaginationToken</code>) in the same request. If you do, you get an <code>Invalid Parameter</code> exception.</p> <p>If a resource specified by this parameter doesn't exist, it doesn't generate an error; it simply isn't included in the response.</p> <p>An ARN (Amazon Resource Name) uniquely identifies a resource. For more information, see <a href="https://docs.aws.amazon.com/general/latest/gr/aws-arns-and-namespaces.html">Amazon Resource Names (ARNs) and Amazon Web Services Service Namespaces</a> in the <i>Amazon Web Services General Reference</i>.</p>

        Raises:
            capo_resource_groups_tagging_api.errors.internal_service_exception.InternalServiceException: <p>The request processing failed because of an unknown error, exception, or failure. You can retry the request.</p>
            capo_resource_groups_tagging_api.errors.invalid_parameter_exception.InvalidParameterException: <p>The request failed because of one of the following reasons:</p> <ul> <li> <p>A required parameter is missing.</p> </li> <li> <p>A provided string parameter is malformed.</p> </li> <li> <p>An provided parameter value is out of range.</p> </li> <li> <p>The target ID is invalid, unsupported, or doesn't exist.</p> </li> <li> <p>You can't access the Amazon S3 bucket for report storage. For more information, see <a href="https://docs.aws.amazon.com/tag-editor/latest/userguide/tag-policies-orgs.html#bucket-policy">Amazon S3 bucket policy for report storage</a> in the <i>Tagging Amazon Web Services resources and Tag Editor</i> user guide. </p> </li> <li> <p>The partition specified in an ARN parameter in the request doesn't match the partition where you invoked the operation. The partition is specified by the second field of the ARN.</p> </li> </ul>
            capo_resource_groups_tagging_api.errors.pagination_token_expired_exception.PaginationTokenExpiredException: <p>The request failed because the specified <code>PaginationToken</code> has expired. A <code>PaginationToken</code> is valid for a maximum of 15 minutes.</p>
            capo_resource_groups_tagging_api.errors.throttled_exception.ThrottledException: <p>The request failed because it exceeded the allowed frequency of submitted requests.</p>
            capo_resource_groups_tagging_api.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        async def _handler(
            req: "AsyncOperationRequest[capo_resource_groups_tagging_api.types.get_resources_input.GetResourcesInput]",
        ) -> AsyncOperationResponse[
            "capo_resource_groups_tagging_api.types.get_resources_output.GetResourcesOutput"
        ]:
            import capo_resource_groups_tagging_api._operations.resource_groups_tagging_api_20170126.get_resources

            (
                output,
                http_response,
            ) = await capo_resource_groups_tagging_api._operations.resource_groups_tagging_api_20170126.get_resources.async_get_resources(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_resource_groups_tagging_api.types.get_resources_input.GetResourcesInput = {}
        if pagination_token is not None:
            input_["pagination_token"] = pagination_token
        if tag_filters is not None:
            input_["tag_filters"] = tag_filters
        if resources_per_page is not None:
            input_["resources_per_page"] = resources_per_page
        if tags_per_page is not None:
            input_["tags_per_page"] = tags_per_page
        if resource_type_filters is not None:
            input_["resource_type_filters"] = resource_type_filters
        if include_compliance_details is not None:
            input_["include_compliance_details"] = include_compliance_details
        if exclude_compliant_resources is not None:
            input_["exclude_compliant_resources"] = exclude_compliant_resources
        if resource_arn_list is not None:
            input_["resource_arn_list"] = resource_arn_list

        response = await aexecute_pipeline(
            AsyncOperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        await response.response.aclose()
        return response.output

    async def iter_get_resources(
        self,
        *,
        config_overrides: Optional[AsyncResourceGroupsTaggingAPIClientConfig] = None,
        pagination_token: Optional[
            "capo_resource_groups_tagging_api.types.pagination_token.PaginationToken"
        ] = None,
        tag_filters: Optional[
            "capo_resource_groups_tagging_api.types.tag_filter_list.TagFilterList"
        ] = None,
        resources_per_page: Optional[
            "capo_resource_groups_tagging_api.types.resources_per_page.ResourcesPerPage"
        ] = None,
        tags_per_page: Optional[
            "capo_resource_groups_tagging_api.types.tags_per_page.TagsPerPage"
        ] = None,
        resource_type_filters: Optional[
            "capo_resource_groups_tagging_api.types.resource_type_filter_list.ResourceTypeFilterList"
        ] = None,
        include_compliance_details: Optional[
            "capo_resource_groups_tagging_api.types.include_compliance_details.IncludeComplianceDetails"
        ] = None,
        exclude_compliant_resources: Optional[
            "capo_resource_groups_tagging_api.types.exclude_compliant_resources.ExcludeCompliantResources"
        ] = None,
        resource_arn_list: Optional[
            "capo_resource_groups_tagging_api.types.resource_arn_list_for_get.ResourceARNListForGet"
        ] = None,
    ) -> "AsyncIterator[capo_resource_groups_tagging_api.types.resource_tag_mapping.ResourceTagMapping]":
        _token = pagination_token
        while True:
            _response = await self.get_resources(
                config_overrides=config_overrides,
                pagination_token=_token,
                tag_filters=tag_filters,
                resources_per_page=resources_per_page,
                tags_per_page=tags_per_page,
                resource_type_filters=resource_type_filters,
                include_compliance_details=include_compliance_details,
                exclude_compliant_resources=exclude_compliant_resources,
                resource_arn_list=resource_arn_list,
            )
            _page = _resolve_path(_response, ("resource_tag_mapping_list",))
            for _item in _page or []:
                yield _item
            _token = _resolve_path(_response, ("pagination_token",))
            if not _token:
                break

    async def get_tag_keys(
        self,
        *,
        config_overrides: Optional[AsyncResourceGroupsTaggingAPIClientConfig] = None,
        pagination_token: Optional[
            "capo_resource_groups_tagging_api.types.pagination_token.PaginationToken"
        ] = None,
    ) -> "capo_resource_groups_tagging_api.types.get_tag_keys_output.GetTagKeysOutput":
        """<p>Returns all tag keys currently in use in the specified Amazon Web Services Region for the calling account.</p> <p>This operation supports pagination, where the response can be sent in multiple pages. You should check the <code>PaginationToken</code> response parameter to determine if there are additional results available to return. Repeat the query, passing the <code>PaginationToken</code> response parameter value as an input to the next request until you recieve a <code>null</code> value. A null value for <code>PaginationToken</code> indicates that there are no more results waiting to be returned.</p>

        Args:
            pagination_token: <p>Specifies a <code>PaginationToken</code> response value from a previous request to indicate that you want the next page of results. Leave this parameter empty in your initial request.</p>

        Raises:
            capo_resource_groups_tagging_api.errors.internal_service_exception.InternalServiceException: <p>The request processing failed because of an unknown error, exception, or failure. You can retry the request.</p>
            capo_resource_groups_tagging_api.errors.invalid_parameter_exception.InvalidParameterException: <p>The request failed because of one of the following reasons:</p> <ul> <li> <p>A required parameter is missing.</p> </li> <li> <p>A provided string parameter is malformed.</p> </li> <li> <p>An provided parameter value is out of range.</p> </li> <li> <p>The target ID is invalid, unsupported, or doesn't exist.</p> </li> <li> <p>You can't access the Amazon S3 bucket for report storage. For more information, see <a href="https://docs.aws.amazon.com/tag-editor/latest/userguide/tag-policies-orgs.html#bucket-policy">Amazon S3 bucket policy for report storage</a> in the <i>Tagging Amazon Web Services resources and Tag Editor</i> user guide. </p> </li> <li> <p>The partition specified in an ARN parameter in the request doesn't match the partition where you invoked the operation. The partition is specified by the second field of the ARN.</p> </li> </ul>
            capo_resource_groups_tagging_api.errors.pagination_token_expired_exception.PaginationTokenExpiredException: <p>The request failed because the specified <code>PaginationToken</code> has expired. A <code>PaginationToken</code> is valid for a maximum of 15 minutes.</p>
            capo_resource_groups_tagging_api.errors.throttled_exception.ThrottledException: <p>The request failed because it exceeded the allowed frequency of submitted requests.</p>
            capo_resource_groups_tagging_api.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        async def _handler(
            req: "AsyncOperationRequest[capo_resource_groups_tagging_api.types.get_tag_keys_input.GetTagKeysInput]",
        ) -> AsyncOperationResponse[
            "capo_resource_groups_tagging_api.types.get_tag_keys_output.GetTagKeysOutput"
        ]:
            import capo_resource_groups_tagging_api._operations.resource_groups_tagging_api_20170126.get_tag_keys

            (
                output,
                http_response,
            ) = await capo_resource_groups_tagging_api._operations.resource_groups_tagging_api_20170126.get_tag_keys.async_get_tag_keys(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_resource_groups_tagging_api.types.get_tag_keys_input.GetTagKeysInput = {}
        if pagination_token is not None:
            input_["pagination_token"] = pagination_token

        response = await aexecute_pipeline(
            AsyncOperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        await response.response.aclose()
        return response.output

    async def iter_get_tag_keys(
        self,
        *,
        config_overrides: Optional[AsyncResourceGroupsTaggingAPIClientConfig] = None,
        pagination_token: Optional[
            "capo_resource_groups_tagging_api.types.pagination_token.PaginationToken"
        ] = None,
    ) -> "AsyncIterator[capo_resource_groups_tagging_api.types.tag_key.TagKey]":
        _token = pagination_token
        while True:
            _response = await self.get_tag_keys(
                config_overrides=config_overrides,
                pagination_token=_token,
            )
            _page = _resolve_path(_response, ("tag_keys",))
            for _item in _page or []:
                yield _item
            _token = _resolve_path(_response, ("pagination_token",))
            if not _token:
                break

    async def get_tag_values(
        self,
        key: "capo_resource_groups_tagging_api.types.tag_key.TagKey",
        *,
        config_overrides: Optional[AsyncResourceGroupsTaggingAPIClientConfig] = None,
        pagination_token: Optional[
            "capo_resource_groups_tagging_api.types.pagination_token.PaginationToken"
        ] = None,
    ) -> "capo_resource_groups_tagging_api.types.get_tag_values_output.GetTagValuesOutput":
        """<p>Returns all tag values for the specified key that are used in the specified Amazon Web Services Region for the calling account.</p> <p>This operation supports pagination, where the response can be sent in multiple pages. You should check the <code>PaginationToken</code> response parameter to determine if there are additional results available to return. Repeat the query, passing the <code>PaginationToken</code> response parameter value as an input to the next request until you recieve a <code>null</code> value. A null value for <code>PaginationToken</code> indicates that there are no more results waiting to be returned.</p>

        Args:
            pagination_token: <p>Specifies a <code>PaginationToken</code> response value from a previous request to indicate that you want the next page of results. Leave this parameter empty in your initial request.</p>
            key: <p>Specifies the tag key for which you want to list all existing values that are currently used in the specified Amazon Web Services Region for the calling account.</p>

        Raises:
            capo_resource_groups_tagging_api.errors.internal_service_exception.InternalServiceException: <p>The request processing failed because of an unknown error, exception, or failure. You can retry the request.</p>
            capo_resource_groups_tagging_api.errors.invalid_parameter_exception.InvalidParameterException: <p>The request failed because of one of the following reasons:</p> <ul> <li> <p>A required parameter is missing.</p> </li> <li> <p>A provided string parameter is malformed.</p> </li> <li> <p>An provided parameter value is out of range.</p> </li> <li> <p>The target ID is invalid, unsupported, or doesn't exist.</p> </li> <li> <p>You can't access the Amazon S3 bucket for report storage. For more information, see <a href="https://docs.aws.amazon.com/tag-editor/latest/userguide/tag-policies-orgs.html#bucket-policy">Amazon S3 bucket policy for report storage</a> in the <i>Tagging Amazon Web Services resources and Tag Editor</i> user guide. </p> </li> <li> <p>The partition specified in an ARN parameter in the request doesn't match the partition where you invoked the operation. The partition is specified by the second field of the ARN.</p> </li> </ul>
            capo_resource_groups_tagging_api.errors.pagination_token_expired_exception.PaginationTokenExpiredException: <p>The request failed because the specified <code>PaginationToken</code> has expired. A <code>PaginationToken</code> is valid for a maximum of 15 minutes.</p>
            capo_resource_groups_tagging_api.errors.throttled_exception.ThrottledException: <p>The request failed because it exceeded the allowed frequency of submitted requests.</p>
            capo_resource_groups_tagging_api.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        async def _handler(
            req: "AsyncOperationRequest[capo_resource_groups_tagging_api.types.get_tag_values_input.GetTagValuesInput]",
        ) -> AsyncOperationResponse[
            "capo_resource_groups_tagging_api.types.get_tag_values_output.GetTagValuesOutput"
        ]:
            import capo_resource_groups_tagging_api._operations.resource_groups_tagging_api_20170126.get_tag_values

            (
                output,
                http_response,
            ) = await capo_resource_groups_tagging_api._operations.resource_groups_tagging_api_20170126.get_tag_values.async_get_tag_values(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_resource_groups_tagging_api.types.get_tag_values_input.GetTagValuesInput = {
            "key": key
        }
        if pagination_token is not None:
            input_["pagination_token"] = pagination_token

        response = await aexecute_pipeline(
            AsyncOperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        await response.response.aclose()
        return response.output

    async def iter_get_tag_values(
        self,
        key: "capo_resource_groups_tagging_api.types.tag_key.TagKey",
        *,
        config_overrides: Optional[AsyncResourceGroupsTaggingAPIClientConfig] = None,
        pagination_token: Optional[
            "capo_resource_groups_tagging_api.types.pagination_token.PaginationToken"
        ] = None,
    ) -> "AsyncIterator[capo_resource_groups_tagging_api.types.tag_value.TagValue]":
        _token = pagination_token
        while True:
            _response = await self.get_tag_values(
                key,
                config_overrides=config_overrides,
                pagination_token=_token,
            )
            _page = _resolve_path(_response, ("tag_values",))
            for _item in _page or []:
                yield _item
            _token = _resolve_path(_response, ("pagination_token",))
            if not _token:
                break

    async def list_required_tags(
        self,
        *,
        config_overrides: Optional[AsyncResourceGroupsTaggingAPIClientConfig] = None,
        next_token: Optional[
            "capo_resource_groups_tagging_api.types.pagination_token.PaginationToken"
        ] = None,
        max_results: Optional[
            "capo_resource_groups_tagging_api.types.max_results_for_list_required_tags.MaxResultsForListRequiredTags"
        ] = None,
    ) -> "capo_resource_groups_tagging_api.types.list_required_tags_output.ListRequiredTagsOutput":
        """<p>Lists the required tags for supported resource types in an Amazon Web Services account.</p>

        Args:
            next_token: <p>A token for requesting another page of required tags if the <code>NextToken</code> response element indicates that more required tags are available. Use the value of the returned <code>NextToken</code> element in your request until the token comes back as null. Pass null if this is the first call.</p>
            max_results: <p>The maximum number of required tags.</p>

        Raises:
            capo_resource_groups_tagging_api.errors.internal_service_exception.InternalServiceException: <p>The request processing failed because of an unknown error, exception, or failure. You can retry the request.</p>
            capo_resource_groups_tagging_api.errors.invalid_parameter_exception.InvalidParameterException: <p>The request failed because of one of the following reasons:</p> <ul> <li> <p>A required parameter is missing.</p> </li> <li> <p>A provided string parameter is malformed.</p> </li> <li> <p>An provided parameter value is out of range.</p> </li> <li> <p>The target ID is invalid, unsupported, or doesn't exist.</p> </li> <li> <p>You can't access the Amazon S3 bucket for report storage. For more information, see <a href="https://docs.aws.amazon.com/tag-editor/latest/userguide/tag-policies-orgs.html#bucket-policy">Amazon S3 bucket policy for report storage</a> in the <i>Tagging Amazon Web Services resources and Tag Editor</i> user guide. </p> </li> <li> <p>The partition specified in an ARN parameter in the request doesn't match the partition where you invoked the operation. The partition is specified by the second field of the ARN.</p> </li> </ul>
            capo_resource_groups_tagging_api.errors.pagination_token_expired_exception.PaginationTokenExpiredException: <p>The request failed because the specified <code>PaginationToken</code> has expired. A <code>PaginationToken</code> is valid for a maximum of 15 minutes.</p>
            capo_resource_groups_tagging_api.errors.throttled_exception.ThrottledException: <p>The request failed because it exceeded the allowed frequency of submitted requests.</p>
            capo_resource_groups_tagging_api.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        async def _handler(
            req: "AsyncOperationRequest[capo_resource_groups_tagging_api.types.list_required_tags_input.ListRequiredTagsInput]",
        ) -> AsyncOperationResponse[
            "capo_resource_groups_tagging_api.types.list_required_tags_output.ListRequiredTagsOutput"
        ]:
            import capo_resource_groups_tagging_api._operations.resource_groups_tagging_api_20170126.list_required_tags

            (
                output,
                http_response,
            ) = await capo_resource_groups_tagging_api._operations.resource_groups_tagging_api_20170126.list_required_tags.async_list_required_tags(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_resource_groups_tagging_api.types.list_required_tags_input.ListRequiredTagsInput = {}
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

    async def iter_list_required_tags(
        self,
        *,
        config_overrides: Optional[AsyncResourceGroupsTaggingAPIClientConfig] = None,
        next_token: Optional[
            "capo_resource_groups_tagging_api.types.pagination_token.PaginationToken"
        ] = None,
        max_results: Optional[
            "capo_resource_groups_tagging_api.types.max_results_for_list_required_tags.MaxResultsForListRequiredTags"
        ] = None,
    ) -> (
        "AsyncIterator[capo_resource_groups_tagging_api.types.required_tag.RequiredTag]"
    ):
        _token = next_token
        while True:
            _response = await self.list_required_tags(
                config_overrides=config_overrides,
                next_token=_token,
                max_results=max_results,
            )
            _page = _resolve_path(_response, ("required_tags",))
            for _item in _page or []:
                yield _item
            _token = _resolve_path(_response, ("next_token",))
            if not _token:
                break

    async def start_report_creation(
        self,
        s3_bucket: "capo_resource_groups_tagging_api.types.s3_bucket.S3Bucket",
        *,
        config_overrides: Optional[AsyncResourceGroupsTaggingAPIClientConfig] = None,
    ) -> "capo_resource_groups_tagging_api.types.start_report_creation_output.StartReportCreationOutput":
        """<p>Generates a report that lists all tagged resources in the accounts across your organization and tells whether each resource is compliant with the effective tag policy. Compliance data is refreshed daily. The report is generated asynchronously.</p> <p>The generated report is saved to the following location:</p> <p> <code>s3://amzn-s3-demo-bucket/AwsTagPolicies/o-exampleorgid/YYYY-MM-ddTHH:mm:ssZ/report.csv</code> </p> <p>For more information about evaluating resource compliance with tag policies, including the required permissions, review <a href="https://docs.aws.amazon.com/tag-editor/latest/userguide/tag-policies-orgs.html#tag-policies-permissions-org">Permissions for evaluating organization-wide compliance</a> in the <i>Tagging Amazon Web Services Resources and Tag Editor</i> user guide. </p> <p>You can call this operation only from the organization's management account and from the us-east-1 Region.</p> <p>If the account associated with the identity used to call <code>StartReportCreation</code> is different from the account that owns the Amazon S3 bucket, there must be a bucket policy attached to the bucket to provide access. For more information, review <a href="https://docs.aws.amazon.com/tag-editor/latest/userguide/tag-policies-orgs.html#bucket-policy">Amazon S3 bucket policy for report storage</a> in the <i>Tagging Amazon Web Services Resources and Tag Editor</i> user guide.</p>

        Args:
            s3_bucket: <p>The name of the Amazon S3 bucket where the report will be stored; for example:</p> <p> <code>amzn-s3-demo-bucket</code> </p> <p>For more information on S3 bucket requirements, including an example bucket policy, see the example Amazon S3 bucket policy on this page.</p>

        Raises:
            capo_resource_groups_tagging_api.errors.concurrent_modification_exception.ConcurrentModificationException: <p>The request failed because the target of the operation is currently being modified by a different request. Try again later.</p>
            capo_resource_groups_tagging_api.errors.constraint_violation_exception.ConstraintViolationException: <p>The request failed because performing the operation would violate a constraint.</p> <p>Some of the reasons in the following list might not apply to this specific operation.</p> <ul> <li> <p>You must meet the prerequisites for using tag policies. For information, see <a href="https://docs.aws.amazon.com/tag-editor/latest/userguide/tag-policies-orgs.html#tag-policies-prereqs">Prerequisites and permissions</a> in the <i>Tagging Amazon Web Services resources and Tag Editor</i> user guide. </p> </li> <li> <p>You must enable the tag policies service principal (<code>tagpolicies.tag.amazonaws.com</code>) to integrate with Organizations For information, see <a href="https://docs.aws.amazon.com/organizations/latest/APIReference/API_EnableAWSServiceAccess.html">EnableAWSServiceAccess</a>.</p> </li> <li> <p>You must have a tag policy attached to the organization root, an OU, or an account.</p> </li> </ul>
            capo_resource_groups_tagging_api.errors.internal_service_exception.InternalServiceException: <p>The request processing failed because of an unknown error, exception, or failure. You can retry the request.</p>
            capo_resource_groups_tagging_api.errors.invalid_parameter_exception.InvalidParameterException: <p>The request failed because of one of the following reasons:</p> <ul> <li> <p>A required parameter is missing.</p> </li> <li> <p>A provided string parameter is malformed.</p> </li> <li> <p>An provided parameter value is out of range.</p> </li> <li> <p>The target ID is invalid, unsupported, or doesn't exist.</p> </li> <li> <p>You can't access the Amazon S3 bucket for report storage. For more information, see <a href="https://docs.aws.amazon.com/tag-editor/latest/userguide/tag-policies-orgs.html#bucket-policy">Amazon S3 bucket policy for report storage</a> in the <i>Tagging Amazon Web Services resources and Tag Editor</i> user guide. </p> </li> <li> <p>The partition specified in an ARN parameter in the request doesn't match the partition where you invoked the operation. The partition is specified by the second field of the ARN.</p> </li> </ul>
            capo_resource_groups_tagging_api.errors.throttled_exception.ThrottledException: <p>The request failed because it exceeded the allowed frequency of submitted requests.</p>
            capo_resource_groups_tagging_api.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        async def _handler(
            req: "AsyncOperationRequest[capo_resource_groups_tagging_api.types.start_report_creation_input.StartReportCreationInput]",
        ) -> AsyncOperationResponse[
            "capo_resource_groups_tagging_api.types.start_report_creation_output.StartReportCreationOutput"
        ]:
            import capo_resource_groups_tagging_api._operations.resource_groups_tagging_api_20170126.start_report_creation

            (
                output,
                http_response,
            ) = await capo_resource_groups_tagging_api._operations.resource_groups_tagging_api_20170126.start_report_creation.async_start_report_creation(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_resource_groups_tagging_api.types.start_report_creation_input.StartReportCreationInput = {
            "s3_bucket": s3_bucket
        }

        response = await aexecute_pipeline(
            AsyncOperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        await response.response.aclose()
        return response.output

    async def tag_resources(
        self,
        resource_arn_list: "capo_resource_groups_tagging_api.types.resource_arn_list_for_tag_untag.ResourceARNListForTagUntag",
        tags: "capo_resource_groups_tagging_api.types.tag_map.TagMap",
        *,
        config_overrides: Optional[AsyncResourceGroupsTaggingAPIClientConfig] = None,
    ) -> (
        "capo_resource_groups_tagging_api.types.tag_resources_output.TagResourcesOutput"
    ):
        """<p>Applies one or more tags to the specified resources. Note the following:</p> <ul> <li> <p>Not all resources can have tags. For a list of services with resources that support tagging using this operation, see <a href="https://docs.aws.amazon.com/resourcegroupstagging/latest/APIReference/supported-services.html">Services that support the Resource Groups Tagging API</a>. If the resource doesn't yet support this operation, the resource's service might support tagging using its own API operations. For more information, refer to the documentation for that service.</p> </li> <li> <p>Each resource can have up to 50 tags. For other limits, see <a href="https://docs.aws.amazon.com/general/latest/gr/aws_tagging.html#tag-conventions">Tag Naming and Usage Conventions</a> in the <i>Amazon Web Services General Reference.</i> </p> </li> <li> <p>You can only tag resources that are located in the specified Amazon Web Services Region for the Amazon Web Services account.</p> </li> <li> <p>To add tags to a resource, you need the necessary permissions for the service that the resource belongs to as well as permissions for adding tags. For more information, see the documentation for each service.</p> </li> <li> <p>When you use the <a href="https://docs.aws.amazon.com/resourcegroupstagging/latest/APIReference/overview.html">Amazon Web Services Resource Groups Tagging API</a> to update tags for Amazon Web Services CloudFormation stack sets, Amazon Web Services calls the <a href="https://docs.aws.amazon.com/AWSCloudFormation/latest/APIReference/API_UpdateStack.html">Amazon Web Services CloudFormation <code>UpdateStack</code> </a> operation. This operation may initiate additional resource property updates in addition to the desired tag updates. To avoid unexpected resource updates, Amazon Web Services recommends that you only apply or update tags to your CloudFormation stack sets using Amazon Web Services CloudFormation. </p> </li> </ul> <important> <p>Do not store personally identifiable information (PII) or other confidential or sensitive information in tags. We use tags to provide you with billing and administration services. Tags are not intended to be used for private or sensitive data.</p> </important> <p> <b>Minimum permissions</b> </p> <p>In addition to the <code>tag:TagResources</code> permission required by this operation, you must also have the tagging permission defined by the service that created the resource. For example, to tag an Amazon EC2 instance using the <code>TagResources</code> operation, you must have both of the following permissions:</p> <ul> <li> <p> <code>tag:TagResources</code> </p> </li> <li> <p> <code>ec2:CreateTags</code> </p> </li> </ul> <note> <p>In addition, some services might have specific requirements for tagging some types of resources. For example, to tag an Amazon S3 bucket, you must also have the <code>s3:GetBucketTagging</code> permission. If the expected minimum permissions don't work, check the documentation for that service's tagging APIs for more information.</p> </note>

        Args:
            resource_arn_list: <p>Specifies the list of ARNs of the resources that you want to apply tags to.</p> <p>An ARN (Amazon Resource Name) uniquely identifies a resource. For more information, see <a href="https://docs.aws.amazon.com/general/latest/gr/aws-arns-and-namespaces.html">Amazon Resource Names (ARNs) and Amazon Web Services Service Namespaces</a> in the <i>Amazon Web Services General Reference</i>.</p>
            tags: <p>Specifies a list of tags that you want to add to the specified resources. A tag consists of a key and a value that you define.</p>

        Raises:
            capo_resource_groups_tagging_api.errors.internal_service_exception.InternalServiceException: <p>The request processing failed because of an unknown error, exception, or failure. You can retry the request.</p>
            capo_resource_groups_tagging_api.errors.invalid_parameter_exception.InvalidParameterException: <p>The request failed because of one of the following reasons:</p> <ul> <li> <p>A required parameter is missing.</p> </li> <li> <p>A provided string parameter is malformed.</p> </li> <li> <p>An provided parameter value is out of range.</p> </li> <li> <p>The target ID is invalid, unsupported, or doesn't exist.</p> </li> <li> <p>You can't access the Amazon S3 bucket for report storage. For more information, see <a href="https://docs.aws.amazon.com/tag-editor/latest/userguide/tag-policies-orgs.html#bucket-policy">Amazon S3 bucket policy for report storage</a> in the <i>Tagging Amazon Web Services resources and Tag Editor</i> user guide. </p> </li> <li> <p>The partition specified in an ARN parameter in the request doesn't match the partition where you invoked the operation. The partition is specified by the second field of the ARN.</p> </li> </ul>
            capo_resource_groups_tagging_api.errors.throttled_exception.ThrottledException: <p>The request failed because it exceeded the allowed frequency of submitted requests.</p>
            capo_resource_groups_tagging_api.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        async def _handler(
            req: "AsyncOperationRequest[capo_resource_groups_tagging_api.types.tag_resources_input.TagResourcesInput]",
        ) -> AsyncOperationResponse[
            "capo_resource_groups_tagging_api.types.tag_resources_output.TagResourcesOutput"
        ]:
            import capo_resource_groups_tagging_api._operations.resource_groups_tagging_api_20170126.tag_resources

            (
                output,
                http_response,
            ) = await capo_resource_groups_tagging_api._operations.resource_groups_tagging_api_20170126.tag_resources.async_tag_resources(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_resource_groups_tagging_api.types.tag_resources_input.TagResourcesInput = {
            "resource_arn_list": resource_arn_list,
            "tags": tags,
        }

        response = await aexecute_pipeline(
            AsyncOperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        await response.response.aclose()
        return response.output

    async def untag_resources(
        self,
        resource_arn_list: "capo_resource_groups_tagging_api.types.resource_arn_list_for_tag_untag.ResourceARNListForTagUntag",
        tag_keys: "capo_resource_groups_tagging_api.types.tag_key_list_for_untag.TagKeyListForUntag",
        *,
        config_overrides: Optional[AsyncResourceGroupsTaggingAPIClientConfig] = None,
    ) -> "capo_resource_groups_tagging_api.types.untag_resources_output.UntagResourcesOutput":
        """<p>Removes the specified tags from the specified resources. When you specify a tag key, the action removes both that key and its associated value. The operation succeeds even if you attempt to remove tags from a resource that were already removed. Note the following:</p> <ul> <li> <p>To remove tags from a resource, you need the necessary permissions for the service that the resource belongs to as well as permissions for removing tags. For more information, see the documentation for the service whose resource you want to untag.</p> </li> <li> <p>You can only tag resources that are located in the specified Amazon Web Services Region for the calling Amazon Web Services account.</p> </li> </ul> <p> <b>Minimum permissions</b> </p> <p>In addition to the <code>tag:UntagResources</code> permission required by this operation, you must also have the remove tags permission defined by the service that created the resource. For example, to remove the tags from an Amazon EC2 instance using the <code>UntagResources</code> operation, you must have both of the following permissions:</p> <ul> <li> <p> <code>tag:UntagResources</code> </p> </li> <li> <p> <code>ec2:DeleteTags</code> </p> </li> </ul> <note> <p>In addition, some services might have specific requirements for untagging some types of resources. For example, to untag Amazon Web Services Glue Connection, you must also have the <code>glue:GetConnection</code> permission. If the expected minimum permissions don't work, check the documentation for that service's tagging APIs for more information.</p> </note>

        Args:
            resource_arn_list: <p>Specifies a list of ARNs of the resources that you want to remove tags from.</p> <p>An ARN (Amazon Resource Name) uniquely identifies a resource. For more information, see <a href="https://docs.aws.amazon.com/general/latest/gr/aws-arns-and-namespaces.html">Amazon Resource Names (ARNs) and Amazon Web Services Service Namespaces</a> in the <i>Amazon Web Services General Reference</i>.</p>
            tag_keys: <p>Specifies a list of tag keys that you want to remove from the specified resources.</p>

        Raises:
            capo_resource_groups_tagging_api.errors.internal_service_exception.InternalServiceException: <p>The request processing failed because of an unknown error, exception, or failure. You can retry the request.</p>
            capo_resource_groups_tagging_api.errors.invalid_parameter_exception.InvalidParameterException: <p>The request failed because of one of the following reasons:</p> <ul> <li> <p>A required parameter is missing.</p> </li> <li> <p>A provided string parameter is malformed.</p> </li> <li> <p>An provided parameter value is out of range.</p> </li> <li> <p>The target ID is invalid, unsupported, or doesn't exist.</p> </li> <li> <p>You can't access the Amazon S3 bucket for report storage. For more information, see <a href="https://docs.aws.amazon.com/tag-editor/latest/userguide/tag-policies-orgs.html#bucket-policy">Amazon S3 bucket policy for report storage</a> in the <i>Tagging Amazon Web Services resources and Tag Editor</i> user guide. </p> </li> <li> <p>The partition specified in an ARN parameter in the request doesn't match the partition where you invoked the operation. The partition is specified by the second field of the ARN.</p> </li> </ul>
            capo_resource_groups_tagging_api.errors.throttled_exception.ThrottledException: <p>The request failed because it exceeded the allowed frequency of submitted requests.</p>
            capo_resource_groups_tagging_api.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        async def _handler(
            req: "AsyncOperationRequest[capo_resource_groups_tagging_api.types.untag_resources_input.UntagResourcesInput]",
        ) -> AsyncOperationResponse[
            "capo_resource_groups_tagging_api.types.untag_resources_output.UntagResourcesOutput"
        ]:
            import capo_resource_groups_tagging_api._operations.resource_groups_tagging_api_20170126.untag_resources

            (
                output,
                http_response,
            ) = await capo_resource_groups_tagging_api._operations.resource_groups_tagging_api_20170126.untag_resources.async_untag_resources(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_resource_groups_tagging_api.types.untag_resources_input.UntagResourcesInput = {
            "resource_arn_list": resource_arn_list,
            "tag_keys": tag_keys,
        }

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
