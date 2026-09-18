"""Generated from Smithy shape ``com.amazonaws.codeartifact#CodeArtifactControlPlaneService``."""

import warnings
from collections.abc import Generator, Iterator
from contextlib import contextmanager
from typing import TYPE_CHECKING, Any, Iterable, Optional

from typing_extensions import Self, TypedDict
from zapros import BaseHandler, Client

import capo_codeartifact._auth._signers
import capo_codeartifact._auth._sigv4
from capo_codeartifact._auth._identity import Credentials
from capo_codeartifact._auth._providers import (
    CredentialsProvider,
    IdentityProvider,
    StaticAwsCredentialsProvider,
    default_aws_credentials_chain,
)
from capo_codeartifact._auth._zapros_handler import AuthMiddleware
from capo_codeartifact._body import Body, closing_bodies
from capo_codeartifact._iter import ensure_sync_iterator
from capo_codeartifact._pagination import resolve_path as _resolve_path
from capo_codeartifact._services._aws_config import aws_config
from capo_codeartifact._services._pipeline import (
    Interceptor,
    OperationOptions,
    OperationRequest,
    OperationResponse,
    execute_pipeline,
    retry,
)

if TYPE_CHECKING:
    import capo_codeartifact.types.account_id
    import capo_codeartifact.types.allow_publish
    import capo_codeartifact.types.allow_upstream
    import capo_codeartifact.types.arn
    import capo_codeartifact.types.asset
    import capo_codeartifact.types.asset_name
    import capo_codeartifact.types.asset_summary
    import capo_codeartifact.types.associate_external_connection_request
    import capo_codeartifact.types.associate_external_connection_result
    import capo_codeartifact.types.associated_package
    import capo_codeartifact.types.authorization_token_duration_seconds
    import capo_codeartifact.types.boolean_optional
    import capo_codeartifact.types.copy_package_versions_request
    import capo_codeartifact.types.copy_package_versions_result
    import capo_codeartifact.types.create_domain_request
    import capo_codeartifact.types.create_domain_result
    import capo_codeartifact.types.create_package_group_request
    import capo_codeartifact.types.create_package_group_result
    import capo_codeartifact.types.create_repository_request
    import capo_codeartifact.types.create_repository_result
    import capo_codeartifact.types.delete_domain_permissions_policy_request
    import capo_codeartifact.types.delete_domain_permissions_policy_result
    import capo_codeartifact.types.delete_domain_request
    import capo_codeartifact.types.delete_domain_result
    import capo_codeartifact.types.delete_package_group_request
    import capo_codeartifact.types.delete_package_group_result
    import capo_codeartifact.types.delete_package_request
    import capo_codeartifact.types.delete_package_result
    import capo_codeartifact.types.delete_package_versions_request
    import capo_codeartifact.types.delete_package_versions_result
    import capo_codeartifact.types.delete_repository_permissions_policy_request
    import capo_codeartifact.types.delete_repository_permissions_policy_result
    import capo_codeartifact.types.delete_repository_request
    import capo_codeartifact.types.delete_repository_result
    import capo_codeartifact.types.describe_domain_request
    import capo_codeartifact.types.describe_domain_result
    import capo_codeartifact.types.describe_package_group_request
    import capo_codeartifact.types.describe_package_group_result
    import capo_codeartifact.types.describe_package_request
    import capo_codeartifact.types.describe_package_result
    import capo_codeartifact.types.describe_package_version_request
    import capo_codeartifact.types.describe_package_version_result
    import capo_codeartifact.types.describe_repository_request
    import capo_codeartifact.types.describe_repository_result
    import capo_codeartifact.types.description
    import capo_codeartifact.types.disassociate_external_connection_request
    import capo_codeartifact.types.disassociate_external_connection_result
    import capo_codeartifact.types.dispose_package_versions_request
    import capo_codeartifact.types.dispose_package_versions_result
    import capo_codeartifact.types.domain_name
    import capo_codeartifact.types.domain_summary
    import capo_codeartifact.types.endpoint_type
    import capo_codeartifact.types.external_connection_name
    import capo_codeartifact.types.get_associated_package_group_request
    import capo_codeartifact.types.get_associated_package_group_result
    import capo_codeartifact.types.get_authorization_token_request
    import capo_codeartifact.types.get_authorization_token_result
    import capo_codeartifact.types.get_domain_permissions_policy_request
    import capo_codeartifact.types.get_domain_permissions_policy_result
    import capo_codeartifact.types.get_package_version_asset_request
    import capo_codeartifact.types.get_package_version_asset_result
    import capo_codeartifact.types.get_package_version_readme_request
    import capo_codeartifact.types.get_package_version_readme_result
    import capo_codeartifact.types.get_repository_endpoint_request
    import capo_codeartifact.types.get_repository_endpoint_result
    import capo_codeartifact.types.get_repository_permissions_policy_request
    import capo_codeartifact.types.get_repository_permissions_policy_result
    import capo_codeartifact.types.list_allowed_repositories_for_group_max_results
    import capo_codeartifact.types.list_allowed_repositories_for_group_request
    import capo_codeartifact.types.list_allowed_repositories_for_group_result
    import capo_codeartifact.types.list_associated_packages_request
    import capo_codeartifact.types.list_associated_packages_result
    import capo_codeartifact.types.list_domains_max_results
    import capo_codeartifact.types.list_domains_request
    import capo_codeartifact.types.list_domains_result
    import capo_codeartifact.types.list_package_groups_max_results
    import capo_codeartifact.types.list_package_groups_request
    import capo_codeartifact.types.list_package_groups_result
    import capo_codeartifact.types.list_package_version_assets_max_results
    import capo_codeartifact.types.list_package_version_assets_request
    import capo_codeartifact.types.list_package_version_assets_result
    import capo_codeartifact.types.list_package_version_dependencies_request
    import capo_codeartifact.types.list_package_version_dependencies_result
    import capo_codeartifact.types.list_package_versions_max_results
    import capo_codeartifact.types.list_package_versions_request
    import capo_codeartifact.types.list_package_versions_result
    import capo_codeartifact.types.list_packages_max_results
    import capo_codeartifact.types.list_packages_request
    import capo_codeartifact.types.list_packages_result
    import capo_codeartifact.types.list_repositories_in_domain_max_results
    import capo_codeartifact.types.list_repositories_in_domain_request
    import capo_codeartifact.types.list_repositories_in_domain_result
    import capo_codeartifact.types.list_repositories_max_results
    import capo_codeartifact.types.list_repositories_request
    import capo_codeartifact.types.list_repositories_result
    import capo_codeartifact.types.list_sub_package_groups_request
    import capo_codeartifact.types.list_sub_package_groups_result
    import capo_codeartifact.types.list_tags_for_resource_request
    import capo_codeartifact.types.list_tags_for_resource_result
    import capo_codeartifact.types.origin_restrictions
    import capo_codeartifact.types.package_format
    import capo_codeartifact.types.package_group_allowed_repository_list
    import capo_codeartifact.types.package_group_contact_info
    import capo_codeartifact.types.package_group_origin_restriction_type
    import capo_codeartifact.types.package_group_pattern
    import capo_codeartifact.types.package_group_pattern_prefix
    import capo_codeartifact.types.package_group_summary
    import capo_codeartifact.types.package_name
    import capo_codeartifact.types.package_namespace
    import capo_codeartifact.types.package_origin_restrictions
    import capo_codeartifact.types.package_summary
    import capo_codeartifact.types.package_version
    import capo_codeartifact.types.package_version_list
    import capo_codeartifact.types.package_version_origin_type
    import capo_codeartifact.types.package_version_revision
    import capo_codeartifact.types.package_version_revision_map
    import capo_codeartifact.types.package_version_sort_type
    import capo_codeartifact.types.package_version_status
    import capo_codeartifact.types.package_version_summary
    import capo_codeartifact.types.pagination_token
    import capo_codeartifact.types.policy_document
    import capo_codeartifact.types.policy_revision
    import capo_codeartifact.types.publish_package_version_request
    import capo_codeartifact.types.publish_package_version_result
    import capo_codeartifact.types.put_domain_permissions_policy_request
    import capo_codeartifact.types.put_domain_permissions_policy_result
    import capo_codeartifact.types.put_package_origin_configuration_request
    import capo_codeartifact.types.put_package_origin_configuration_result
    import capo_codeartifact.types.put_repository_permissions_policy_request
    import capo_codeartifact.types.put_repository_permissions_policy_result
    import capo_codeartifact.types.repository_name
    import capo_codeartifact.types.repository_summary
    import capo_codeartifact.types.sha256
    import capo_codeartifact.types.string
    import capo_codeartifact.types.tag_key_list
    import capo_codeartifact.types.tag_list
    import capo_codeartifact.types.tag_resource_request
    import capo_codeartifact.types.tag_resource_result
    import capo_codeartifact.types.untag_resource_request
    import capo_codeartifact.types.untag_resource_result
    import capo_codeartifact.types.update_package_group_origin_configuration_request
    import capo_codeartifact.types.update_package_group_origin_configuration_result
    import capo_codeartifact.types.update_package_group_request
    import capo_codeartifact.types.update_package_group_result
    import capo_codeartifact.types.update_package_versions_status_request
    import capo_codeartifact.types.update_package_versions_status_result
    import capo_codeartifact.types.update_repository_request
    import capo_codeartifact.types.update_repository_result
    import capo_codeartifact.types.upstream_repository_list


class codeartifactClientConfig(TypedDict, total=False, closed=True):
    operation_interceptors: Iterable[Interceptor[Any, Any]]
    retry_max_attempts: int | None
    region: str | None
    use_dual_stack: bool | None
    use_fips: bool | None
    endpoint: str | None
    credentials_provider: IdentityProvider[Credentials] | None


class codeartifactClient:
    """A client for the ``codeartifact`` service.

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
        http_handler: BaseHandler | None = None,
        operation_interceptors: Iterable[Interceptor[Any, Any]] | None = None,
        retry_max_attempts: int | None = None,
        region: str | None = None,
        use_dual_stack: bool | None = None,
        use_fips: bool | None = None,
        endpoint: str | None = None,
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
        self._config = codeartifactClientConfig(
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
        self, config_overrides: Optional[codeartifactClientConfig] = None
    ) -> tuple[Iterable[Interceptor[Any, Any]], OperationOptions]:
        overrides: codeartifactClientConfig = config_overrides or {}
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
        )
        return interceptors_, options_

    def associate_external_connection(
        self,
        domain: "capo_codeartifact.types.domain_name.DomainName",
        repository: "capo_codeartifact.types.repository_name.RepositoryName",
        external_connection: "capo_codeartifact.types.external_connection_name.ExternalConnectionName",
        *,
        config_overrides: Optional[codeartifactClientConfig] = None,
        domain_owner: Optional["capo_codeartifact.types.account_id.AccountId"] = None,
    ) -> "capo_codeartifact.types.associate_external_connection_result.AssociateExternalConnectionResult":
        """<p>Adds an existing external connection to a repository. One external connection is allowed per repository.</p> <note> <p>A repository can have one or more upstream repositories, or an external connection.</p> </note>

        Args:
            domain: <p>The name of the domain that contains the repository.</p>
            domain_owner: <p> The 12-digit account number of the Amazon Web Services account that owns the domain. It does not include dashes or spaces. </p>
            repository: <p> The name of the repository to which the external connection is added. </p>
            external_connection: <p> The name of the external connection to add to the repository. The following values are supported: </p> <ul> <li> <p> <code>public:npmjs</code> - for the npm public repository. </p> </li> <li> <p> <code>public:nuget-org</code> - for the NuGet Gallery. </p> </li> <li> <p> <code>public:pypi</code> - for the Python Package Index. </p> </li> <li> <p> <code>public:maven-central</code> - for Maven Central. </p> </li> <li> <p> <code>public:maven-googleandroid</code> - for the Google Android repository. </p> </li> <li> <p> <code>public:maven-gradleplugins</code> - for the Gradle plugins repository. </p> </li> <li> <p> <code>public:maven-commonsware</code> - for the CommonsWare Android repository. </p> </li> <li> <p> <code>public:maven-clojars</code> - for the Clojars repository. </p> </li> <li> <p> <code>public:ruby-gems-org</code> - for RubyGems.org. </p> </li> <li> <p> <code>public:crates-io</code> - for Crates.io. </p> </li> </ul>

        Raises:
            capo_codeartifact.errors.access_denied_exception.AccessDeniedException: <p> The operation did not succeed because of an unauthorized access attempt. </p>
            capo_codeartifact.errors.conflict_exception.ConflictException: <p> The operation did not succeed because prerequisites are not met. </p>
            capo_codeartifact.errors.internal_server_exception.InternalServerException: <p> The operation did not succeed because of an error that occurred inside CodeArtifact. </p>
            capo_codeartifact.errors.resource_not_found_exception.ResourceNotFoundException: <p> The operation did not succeed because the resource requested is not found in the service. </p>
            capo_codeartifact.errors.service_quota_exceeded_exception.ServiceQuotaExceededException: <p> The operation did not succeed because it would have exceeded a service limit for your account. </p>
            capo_codeartifact.errors.throttling_exception.ThrottlingException: <p> The operation did not succeed because too many requests are sent to the service. </p>
            capo_codeartifact.errors.validation_exception.ValidationException: <p> The operation did not succeed because a parameter in the request was sent with an invalid value. </p>
            capo_codeartifact.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        def _handler(
            req: "OperationRequest[capo_codeartifact.types.associate_external_connection_request.AssociateExternalConnectionRequest]",
        ) -> OperationResponse[
            "capo_codeartifact.types.associate_external_connection_result.AssociateExternalConnectionResult"
        ]:
            import capo_codeartifact._operations.code_artifact_control_plane_service.associate_external_connection

            output, http_response = (
                capo_codeartifact._operations.code_artifact_control_plane_service.associate_external_connection.associate_external_connection(
                    req.options, req.input
                )
            )
            return OperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_codeartifact.types.associate_external_connection_request.AssociateExternalConnectionRequest = {
            "domain": domain,
            "repository": repository,
            "external_connection": external_connection,
        }
        if domain_owner is not None:
            input_["domain_owner"] = domain_owner

        response = execute_pipeline(
            OperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        response.response.close()
        return response.output

    def copy_package_versions(
        self,
        domain: "capo_codeartifact.types.domain_name.DomainName",
        source_repository: "capo_codeartifact.types.repository_name.RepositoryName",
        destination_repository: "capo_codeartifact.types.repository_name.RepositoryName",
        format: "capo_codeartifact.types.package_format.PackageFormat",
        package: "capo_codeartifact.types.package_name.PackageName",
        *,
        config_overrides: Optional[codeartifactClientConfig] = None,
        domain_owner: Optional["capo_codeartifact.types.account_id.AccountId"] = None,
        namespace: Optional[
            "capo_codeartifact.types.package_namespace.PackageNamespace"
        ] = None,
        versions: Optional[
            "capo_codeartifact.types.package_version_list.PackageVersionList"
        ] = None,
        version_revisions: Optional[
            "capo_codeartifact.types.package_version_revision_map.PackageVersionRevisionMap"
        ] = None,
        allow_overwrite: Optional[
            "capo_codeartifact.types.boolean_optional.BooleanOptional"
        ] = None,
        include_from_upstream: Optional[
            "capo_codeartifact.types.boolean_optional.BooleanOptional"
        ] = None,
    ) -> (
        "capo_codeartifact.types.copy_package_versions_result.CopyPackageVersionsResult"
    ):
        r"""<p> Copies package versions from one repository to another repository in the same domain. </p> <note> <p> You must specify <code>versions</code> or <code>versionRevisions</code>. You cannot specify both. </p> </note>

        Args:
            domain: <p> The name of the domain that contains the source and destination repositories. </p>
            domain_owner: <p> The 12-digit account number of the Amazon Web Services account that owns the domain. It does not include dashes or spaces. </p>
            source_repository: <p> The name of the repository that contains the package versions to be copied. </p>
            destination_repository: <p> The name of the repository into which package versions are copied. </p>
            format: <p> The format of the package versions to be copied. </p>
            namespace: <p>The namespace of the package versions to be copied. The package component that specifies its namespace depends on its type. For example:</p> <note> <p>The namespace is required when copying package versions of the following formats:</p> <ul> <li> <p>Maven</p> </li> <li> <p>Swift</p> </li> <li> <p>generic</p> </li> </ul> </note> <ul> <li> <p> The namespace of a Maven package version is its <code>groupId</code>. </p> </li> <li> <p> The namespace of an npm or Swift package version is its <code>scope</code>. </p> </li> <li> <p>The namespace of a generic package is its <code>namespace</code>.</p> </li> <li> <p> Python, NuGet, Ruby, and Cargo package versions do not contain a corresponding component, package versions of those formats do not have a namespace. </p> </li> </ul>
            package: <p> The name of the package that contains the versions to be copied. </p>
            versions: <p> The versions of the package to be copied. </p> <note> <p> You must specify <code>versions</code> or <code>versionRevisions</code>. You cannot specify both. </p> </note>
            version_revisions: <p> A list of key-value pairs. The keys are package versions and the values are package version revisions. A <code>CopyPackageVersion</code> operation succeeds if the specified versions in the source repository match the specified package version revision. </p> <note> <p> You must specify <code>versions</code> or <code>versionRevisions</code>. You cannot specify both. </p> </note>
            allow_overwrite: <p> Set to true to overwrite a package version that already exists in the destination repository. If set to false and the package version already exists in the destination repository, the package version is returned in the <code>failedVersions</code> field of the response with an <code>ALREADY_EXISTS</code> error code. </p>
            include_from_upstream: <p> Set to true to copy packages from repositories that are upstream from the source repository to the destination repository. The default setting is false. For more information, see <a href=\"https://docs.aws.amazon.com/codeartifact/latest/ug/repos-upstream.html\">Working with upstream repositories</a>. </p>

        Raises:
            capo_codeartifact.errors.access_denied_exception.AccessDeniedException: <p> The operation did not succeed because of an unauthorized access attempt. </p>
            capo_codeartifact.errors.conflict_exception.ConflictException: <p> The operation did not succeed because prerequisites are not met. </p>
            capo_codeartifact.errors.internal_server_exception.InternalServerException: <p> The operation did not succeed because of an error that occurred inside CodeArtifact. </p>
            capo_codeartifact.errors.resource_not_found_exception.ResourceNotFoundException: <p> The operation did not succeed because the resource requested is not found in the service. </p>
            capo_codeartifact.errors.service_quota_exceeded_exception.ServiceQuotaExceededException: <p> The operation did not succeed because it would have exceeded a service limit for your account. </p>
            capo_codeartifact.errors.throttling_exception.ThrottlingException: <p> The operation did not succeed because too many requests are sent to the service. </p>
            capo_codeartifact.errors.validation_exception.ValidationException: <p> The operation did not succeed because a parameter in the request was sent with an invalid value. </p>
            capo_codeartifact.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        def _handler(
            req: "OperationRequest[capo_codeartifact.types.copy_package_versions_request.CopyPackageVersionsRequest]",
        ) -> OperationResponse[
            "capo_codeartifact.types.copy_package_versions_result.CopyPackageVersionsResult"
        ]:
            import capo_codeartifact._operations.code_artifact_control_plane_service.copy_package_versions

            output, http_response = (
                capo_codeartifact._operations.code_artifact_control_plane_service.copy_package_versions.copy_package_versions(
                    req.options, req.input
                )
            )
            return OperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_codeartifact.types.copy_package_versions_request.CopyPackageVersionsRequest = {
            "domain": domain,
            "source_repository": source_repository,
            "destination_repository": destination_repository,
            "format": format,
            "package": package,
        }
        if domain_owner is not None:
            input_["domain_owner"] = domain_owner
        if namespace is not None:
            input_["namespace"] = namespace
        if versions is not None:
            input_["versions"] = versions
        if version_revisions is not None:
            input_["version_revisions"] = version_revisions
        if allow_overwrite is not None:
            input_["allow_overwrite"] = allow_overwrite
        if include_from_upstream is not None:
            input_["include_from_upstream"] = include_from_upstream

        response = execute_pipeline(
            OperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        response.response.close()
        return response.output

    def create_domain(
        self,
        domain: "capo_codeartifact.types.domain_name.DomainName",
        *,
        config_overrides: Optional[codeartifactClientConfig] = None,
        encryption_key: Optional["capo_codeartifact.types.arn.Arn"] = None,
        tags: Optional["capo_codeartifact.types.tag_list.TagList"] = None,
    ) -> "capo_codeartifact.types.create_domain_result.CreateDomainResult":
        r"""<p> Creates a domain. CodeArtifact <i>domains</i> make it easier to manage multiple repositories across an organization. You can use a domain to apply permissions across many repositories owned by different Amazon Web Services accounts. An asset is stored only once in a domain, even if it's in multiple repositories. </p> <p>Although you can have multiple domains, we recommend a single production domain that contains all published artifacts so that your development teams can find and share packages. You can use a second pre-production domain to test changes to the production domain configuration. </p>

        Args:
            domain: <p> The name of the domain to create. All domain names in an Amazon Web Services Region that are in the same Amazon Web Services account must be unique. The domain name is used as the prefix in DNS hostnames. Do not use sensitive information in a domain name because it is publicly discoverable. </p>
            encryption_key: <p> The encryption key for the domain. This is used to encrypt content stored in a domain. An encryption key can be a key ID, a key Amazon Resource Name (ARN), a key alias, or a key alias ARN. To specify an <code>encryptionKey</code>, your IAM role must have <code>kms:DescribeKey</code> and <code>kms:CreateGrant</code> permissions on the encryption key that is used. For more information, see <a href=\"https://docs.aws.amazon.com/kms/latest/APIReference/API_DescribeKey.html#API_DescribeKey_RequestSyntax\">DescribeKey</a> in the <i>Key Management Service API Reference</i> and <a href=\"https://docs.aws.amazon.com/kms/latest/developerguide/kms-api-permissions-reference.html\">Key Management Service API Permissions Reference</a> in the <i>Key Management Service Developer Guide</i>. </p> <important> <p> CodeArtifact supports only symmetric CMKs. Do not associate an asymmetric CMK with your domain. For more information, see <a href=\"https://docs.aws.amazon.com/kms/latest/developerguide/symmetric-asymmetric.html\">Using symmetric and asymmetric keys</a> in the <i>Key Management Service Developer Guide</i>. </p> </important>
            tags: <p>One or more tag key-value pairs for the domain.</p>

        Raises:
            capo_codeartifact.errors.access_denied_exception.AccessDeniedException: <p> The operation did not succeed because of an unauthorized access attempt. </p>
            capo_codeartifact.errors.conflict_exception.ConflictException: <p> The operation did not succeed because prerequisites are not met. </p>
            capo_codeartifact.errors.internal_server_exception.InternalServerException: <p> The operation did not succeed because of an error that occurred inside CodeArtifact. </p>
            capo_codeartifact.errors.resource_not_found_exception.ResourceNotFoundException: <p> The operation did not succeed because the resource requested is not found in the service. </p>
            capo_codeartifact.errors.service_quota_exceeded_exception.ServiceQuotaExceededException: <p> The operation did not succeed because it would have exceeded a service limit for your account. </p>
            capo_codeartifact.errors.throttling_exception.ThrottlingException: <p> The operation did not succeed because too many requests are sent to the service. </p>
            capo_codeartifact.errors.validation_exception.ValidationException: <p> The operation did not succeed because a parameter in the request was sent with an invalid value. </p>
            capo_codeartifact.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        def _handler(
            req: "OperationRequest[capo_codeartifact.types.create_domain_request.CreateDomainRequest]",
        ) -> OperationResponse[
            "capo_codeartifact.types.create_domain_result.CreateDomainResult"
        ]:
            import capo_codeartifact._operations.code_artifact_control_plane_service.create_domain

            output, http_response = (
                capo_codeartifact._operations.code_artifact_control_plane_service.create_domain.create_domain(
                    req.options, req.input
                )
            )
            return OperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_codeartifact.types.create_domain_request.CreateDomainRequest = {
            "domain": domain
        }
        if encryption_key is not None:
            input_["encryption_key"] = encryption_key
        if tags is not None:
            input_["tags"] = tags

        response = execute_pipeline(
            OperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        response.response.close()
        return response.output

    def create_package_group(
        self,
        domain: "capo_codeartifact.types.domain_name.DomainName",
        package_group: "capo_codeartifact.types.package_group_pattern.PackageGroupPattern",
        *,
        config_overrides: Optional[codeartifactClientConfig] = None,
        domain_owner: Optional["capo_codeartifact.types.account_id.AccountId"] = None,
        contact_info: Optional[
            "capo_codeartifact.types.package_group_contact_info.PackageGroupContactInfo"
        ] = None,
        description: Optional["capo_codeartifact.types.description.Description"] = None,
        tags: Optional["capo_codeartifact.types.tag_list.TagList"] = None,
    ) -> "capo_codeartifact.types.create_package_group_result.CreatePackageGroupResult":
        r"""<p> Creates a package group. For more information about creating package groups, including example CLI commands, see <a href=\"https://docs.aws.amazon.com/codeartifact/latest/ug/create-package-group.html\">Create a package group</a> in the <i>CodeArtifact User Guide</i>. </p>

        Args:
            domain: <p> The name of the domain in which you want to create a package group. </p>
            domain_owner: <p> The 12-digit account number of the Amazon Web Services account that owns the domain. It does not include dashes or spaces. </p>
            package_group: <p>The pattern of the package group to create. The pattern is also the identifier of the package group. </p>
            contact_info: <p> The contact information for the created package group. </p>
            description: <p> A description of the package group. </p>
            tags: <p>One or more tag key-value pairs for the package group.</p>

        Raises:
            capo_codeartifact.errors.access_denied_exception.AccessDeniedException: <p> The operation did not succeed because of an unauthorized access attempt. </p>
            capo_codeartifact.errors.conflict_exception.ConflictException: <p> The operation did not succeed because prerequisites are not met. </p>
            capo_codeartifact.errors.internal_server_exception.InternalServerException: <p> The operation did not succeed because of an error that occurred inside CodeArtifact. </p>
            capo_codeartifact.errors.resource_not_found_exception.ResourceNotFoundException: <p> The operation did not succeed because the resource requested is not found in the service. </p>
            capo_codeartifact.errors.service_quota_exceeded_exception.ServiceQuotaExceededException: <p> The operation did not succeed because it would have exceeded a service limit for your account. </p>
            capo_codeartifact.errors.throttling_exception.ThrottlingException: <p> The operation did not succeed because too many requests are sent to the service. </p>
            capo_codeartifact.errors.validation_exception.ValidationException: <p> The operation did not succeed because a parameter in the request was sent with an invalid value. </p>
            capo_codeartifact.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        def _handler(
            req: "OperationRequest[capo_codeartifact.types.create_package_group_request.CreatePackageGroupRequest]",
        ) -> OperationResponse[
            "capo_codeartifact.types.create_package_group_result.CreatePackageGroupResult"
        ]:
            import capo_codeartifact._operations.code_artifact_control_plane_service.create_package_group

            output, http_response = (
                capo_codeartifact._operations.code_artifact_control_plane_service.create_package_group.create_package_group(
                    req.options, req.input
                )
            )
            return OperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_codeartifact.types.create_package_group_request.CreatePackageGroupRequest = {
            "domain": domain,
            "package_group": package_group,
        }
        if domain_owner is not None:
            input_["domain_owner"] = domain_owner
        if contact_info is not None:
            input_["contact_info"] = contact_info
        if description is not None:
            input_["description"] = description
        if tags is not None:
            input_["tags"] = tags

        response = execute_pipeline(
            OperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        response.response.close()
        return response.output

    def create_repository(
        self,
        domain: "capo_codeartifact.types.domain_name.DomainName",
        repository: "capo_codeartifact.types.repository_name.RepositoryName",
        *,
        config_overrides: Optional[codeartifactClientConfig] = None,
        domain_owner: Optional["capo_codeartifact.types.account_id.AccountId"] = None,
        description: Optional["capo_codeartifact.types.description.Description"] = None,
        upstreams: Optional[
            "capo_codeartifact.types.upstream_repository_list.UpstreamRepositoryList"
        ] = None,
        tags: Optional["capo_codeartifact.types.tag_list.TagList"] = None,
    ) -> "capo_codeartifact.types.create_repository_result.CreateRepositoryResult":
        r"""<p> Creates a repository. </p>

        Args:
            domain: <p> The name of the domain that contains the created repository. </p>
            domain_owner: <p> The 12-digit account number of the Amazon Web Services account that owns the domain. It does not include dashes or spaces. </p>
            repository: <p>The name of the repository to create. </p>
            description: <p> A description of the created repository. </p>
            upstreams: <p> A list of upstream repositories to associate with the repository. The order of the upstream repositories in the list determines their priority order when CodeArtifact looks for a requested package version. For more information, see <a href=\"https://docs.aws.amazon.com/codeartifact/latest/ug/repos-upstream.html\">Working with upstream repositories</a>. </p>
            tags: <p>One or more tag key-value pairs for the repository.</p>

        Raises:
            capo_codeartifact.errors.access_denied_exception.AccessDeniedException: <p> The operation did not succeed because of an unauthorized access attempt. </p>
            capo_codeartifact.errors.conflict_exception.ConflictException: <p> The operation did not succeed because prerequisites are not met. </p>
            capo_codeartifact.errors.internal_server_exception.InternalServerException: <p> The operation did not succeed because of an error that occurred inside CodeArtifact. </p>
            capo_codeartifact.errors.resource_not_found_exception.ResourceNotFoundException: <p> The operation did not succeed because the resource requested is not found in the service. </p>
            capo_codeartifact.errors.service_quota_exceeded_exception.ServiceQuotaExceededException: <p> The operation did not succeed because it would have exceeded a service limit for your account. </p>
            capo_codeartifact.errors.throttling_exception.ThrottlingException: <p> The operation did not succeed because too many requests are sent to the service. </p>
            capo_codeartifact.errors.validation_exception.ValidationException: <p> The operation did not succeed because a parameter in the request was sent with an invalid value. </p>
            capo_codeartifact.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        def _handler(
            req: "OperationRequest[capo_codeartifact.types.create_repository_request.CreateRepositoryRequest]",
        ) -> OperationResponse[
            "capo_codeartifact.types.create_repository_result.CreateRepositoryResult"
        ]:
            import capo_codeartifact._operations.code_artifact_control_plane_service.create_repository

            output, http_response = (
                capo_codeartifact._operations.code_artifact_control_plane_service.create_repository.create_repository(
                    req.options, req.input
                )
            )
            return OperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_codeartifact.types.create_repository_request.CreateRepositoryRequest = {
            "domain": domain,
            "repository": repository,
        }
        if domain_owner is not None:
            input_["domain_owner"] = domain_owner
        if description is not None:
            input_["description"] = description
        if upstreams is not None:
            input_["upstreams"] = upstreams
        if tags is not None:
            input_["tags"] = tags

        response = execute_pipeline(
            OperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        response.response.close()
        return response.output

    def delete_domain(
        self,
        domain: "capo_codeartifact.types.domain_name.DomainName",
        *,
        config_overrides: Optional[codeartifactClientConfig] = None,
        domain_owner: Optional["capo_codeartifact.types.account_id.AccountId"] = None,
    ) -> "capo_codeartifact.types.delete_domain_result.DeleteDomainResult":
        """<p> Deletes a domain. You cannot delete a domain that contains repositories. If you want to delete a domain with repositories, first delete its repositories. </p>

        Args:
            domain: <p> The name of the domain to delete. </p>
            domain_owner: <p> The 12-digit account number of the Amazon Web Services account that owns the domain. It does not include dashes or spaces. </p>

        Raises:
            capo_codeartifact.errors.access_denied_exception.AccessDeniedException: <p> The operation did not succeed because of an unauthorized access attempt. </p>
            capo_codeartifact.errors.conflict_exception.ConflictException: <p> The operation did not succeed because prerequisites are not met. </p>
            capo_codeartifact.errors.internal_server_exception.InternalServerException: <p> The operation did not succeed because of an error that occurred inside CodeArtifact. </p>
            capo_codeartifact.errors.throttling_exception.ThrottlingException: <p> The operation did not succeed because too many requests are sent to the service. </p>
            capo_codeartifact.errors.validation_exception.ValidationException: <p> The operation did not succeed because a parameter in the request was sent with an invalid value. </p>
            capo_codeartifact.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        def _handler(
            req: "OperationRequest[capo_codeartifact.types.delete_domain_request.DeleteDomainRequest]",
        ) -> OperationResponse[
            "capo_codeartifact.types.delete_domain_result.DeleteDomainResult"
        ]:
            import capo_codeartifact._operations.code_artifact_control_plane_service.delete_domain

            output, http_response = (
                capo_codeartifact._operations.code_artifact_control_plane_service.delete_domain.delete_domain(
                    req.options, req.input
                )
            )
            return OperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_codeartifact.types.delete_domain_request.DeleteDomainRequest = {
            "domain": domain
        }
        if domain_owner is not None:
            input_["domain_owner"] = domain_owner

        response = execute_pipeline(
            OperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        response.response.close()
        return response.output

    def delete_domain_permissions_policy(
        self,
        domain: "capo_codeartifact.types.domain_name.DomainName",
        *,
        config_overrides: Optional[codeartifactClientConfig] = None,
        domain_owner: Optional["capo_codeartifact.types.account_id.AccountId"] = None,
        policy_revision: Optional[
            "capo_codeartifact.types.policy_revision.PolicyRevision"
        ] = None,
    ) -> "capo_codeartifact.types.delete_domain_permissions_policy_result.DeleteDomainPermissionsPolicyResult":
        """<p> Deletes the resource policy set on a domain. </p>

        Args:
            domain: <p> The name of the domain associated with the resource policy to be deleted. </p>
            domain_owner: <p> The 12-digit account number of the Amazon Web Services account that owns the domain. It does not include dashes or spaces. </p>
            policy_revision: <p> The current revision of the resource policy to be deleted. This revision is used for optimistic locking, which prevents others from overwriting your changes to the domain's resource policy. </p>

        Raises:
            capo_codeartifact.errors.access_denied_exception.AccessDeniedException: <p> The operation did not succeed because of an unauthorized access attempt. </p>
            capo_codeartifact.errors.conflict_exception.ConflictException: <p> The operation did not succeed because prerequisites are not met. </p>
            capo_codeartifact.errors.internal_server_exception.InternalServerException: <p> The operation did not succeed because of an error that occurred inside CodeArtifact. </p>
            capo_codeartifact.errors.resource_not_found_exception.ResourceNotFoundException: <p> The operation did not succeed because the resource requested is not found in the service. </p>
            capo_codeartifact.errors.throttling_exception.ThrottlingException: <p> The operation did not succeed because too many requests are sent to the service. </p>
            capo_codeartifact.errors.validation_exception.ValidationException: <p> The operation did not succeed because a parameter in the request was sent with an invalid value. </p>
            capo_codeartifact.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        def _handler(
            req: "OperationRequest[capo_codeartifact.types.delete_domain_permissions_policy_request.DeleteDomainPermissionsPolicyRequest]",
        ) -> OperationResponse[
            "capo_codeartifact.types.delete_domain_permissions_policy_result.DeleteDomainPermissionsPolicyResult"
        ]:
            import capo_codeartifact._operations.code_artifact_control_plane_service.delete_domain_permissions_policy

            output, http_response = (
                capo_codeartifact._operations.code_artifact_control_plane_service.delete_domain_permissions_policy.delete_domain_permissions_policy(
                    req.options, req.input
                )
            )
            return OperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_codeartifact.types.delete_domain_permissions_policy_request.DeleteDomainPermissionsPolicyRequest = {
            "domain": domain
        }
        if domain_owner is not None:
            input_["domain_owner"] = domain_owner
        if policy_revision is not None:
            input_["policy_revision"] = policy_revision

        response = execute_pipeline(
            OperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        response.response.close()
        return response.output

    def delete_package(
        self,
        domain: "capo_codeartifact.types.domain_name.DomainName",
        repository: "capo_codeartifact.types.repository_name.RepositoryName",
        format: "capo_codeartifact.types.package_format.PackageFormat",
        package: "capo_codeartifact.types.package_name.PackageName",
        *,
        config_overrides: Optional[codeartifactClientConfig] = None,
        domain_owner: Optional["capo_codeartifact.types.account_id.AccountId"] = None,
        namespace: Optional[
            "capo_codeartifact.types.package_namespace.PackageNamespace"
        ] = None,
    ) -> "capo_codeartifact.types.delete_package_result.DeletePackageResult":
        r"""<p>Deletes a package and all associated package versions. A deleted package cannot be restored. To delete one or more package versions, use the <a href=\"https://docs.aws.amazon.com/codeartifact/latest/APIReference/API_DeletePackageVersions.html\">DeletePackageVersions</a> API.</p>

        Args:
            domain: <p>The name of the domain that contains the package to delete.</p>
            domain_owner: <p> The 12-digit account number of the Amazon Web Services account that owns the domain. It does not include dashes or spaces. </p>
            repository: <p>The name of the repository that contains the package to delete.</p>
            format: <p>The format of the requested package to delete.</p>
            namespace: <p>The namespace of the package to delete. The package component that specifies its namespace depends on its type. For example:</p> <note> <p>The namespace is required when deleting packages of the following formats:</p> <ul> <li> <p>Maven</p> </li> <li> <p>Swift</p> </li> <li> <p>generic</p> </li> </ul> </note> <ul> <li> <p> The namespace of a Maven package version is its <code>groupId</code>. </p> </li> <li> <p> The namespace of an npm or Swift package version is its <code>scope</code>. </p> </li> <li> <p>The namespace of a generic package is its <code>namespace</code>.</p> </li> <li> <p> Python, NuGet, Ruby, and Cargo package versions do not contain a corresponding component, package versions of those formats do not have a namespace. </p> </li> </ul>
            package: <p>The name of the package to delete.</p>

        Raises:
            capo_codeartifact.errors.access_denied_exception.AccessDeniedException: <p> The operation did not succeed because of an unauthorized access attempt. </p>
            capo_codeartifact.errors.conflict_exception.ConflictException: <p> The operation did not succeed because prerequisites are not met. </p>
            capo_codeartifact.errors.internal_server_exception.InternalServerException: <p> The operation did not succeed because of an error that occurred inside CodeArtifact. </p>
            capo_codeartifact.errors.resource_not_found_exception.ResourceNotFoundException: <p> The operation did not succeed because the resource requested is not found in the service. </p>
            capo_codeartifact.errors.throttling_exception.ThrottlingException: <p> The operation did not succeed because too many requests are sent to the service. </p>
            capo_codeartifact.errors.validation_exception.ValidationException: <p> The operation did not succeed because a parameter in the request was sent with an invalid value. </p>
            capo_codeartifact.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        def _handler(
            req: "OperationRequest[capo_codeartifact.types.delete_package_request.DeletePackageRequest]",
        ) -> OperationResponse[
            "capo_codeartifact.types.delete_package_result.DeletePackageResult"
        ]:
            import capo_codeartifact._operations.code_artifact_control_plane_service.delete_package

            output, http_response = (
                capo_codeartifact._operations.code_artifact_control_plane_service.delete_package.delete_package(
                    req.options, req.input
                )
            )
            return OperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_codeartifact.types.delete_package_request.DeletePackageRequest = {
            "domain": domain,
            "repository": repository,
            "format": format,
            "package": package,
        }
        if domain_owner is not None:
            input_["domain_owner"] = domain_owner
        if namespace is not None:
            input_["namespace"] = namespace

        response = execute_pipeline(
            OperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        response.response.close()
        return response.output

    def delete_package_group(
        self,
        domain: "capo_codeartifact.types.domain_name.DomainName",
        package_group: "capo_codeartifact.types.string.String",
        *,
        config_overrides: Optional[codeartifactClientConfig] = None,
        domain_owner: Optional["capo_codeartifact.types.account_id.AccountId"] = None,
    ) -> "capo_codeartifact.types.delete_package_group_result.DeletePackageGroupResult":
        """<p>Deletes a package group. Deleting a package group does not delete packages or package versions associated with the package group. When a package group is deleted, the direct child package groups will become children of the package group's direct parent package group. Therefore, if any of the child groups are inheriting any settings from the parent, those settings could change.</p>

        Args:
            domain: <p> The domain that contains the package group to be deleted. </p>
            domain_owner: <p> The 12-digit account number of the Amazon Web Services account that owns the domain. It does not include dashes or spaces. </p>
            package_group: <p>The pattern of the package group to be deleted.</p>

        Raises:
            capo_codeartifact.errors.access_denied_exception.AccessDeniedException: <p> The operation did not succeed because of an unauthorized access attempt. </p>
            capo_codeartifact.errors.conflict_exception.ConflictException: <p> The operation did not succeed because prerequisites are not met. </p>
            capo_codeartifact.errors.internal_server_exception.InternalServerException: <p> The operation did not succeed because of an error that occurred inside CodeArtifact. </p>
            capo_codeartifact.errors.resource_not_found_exception.ResourceNotFoundException: <p> The operation did not succeed because the resource requested is not found in the service. </p>
            capo_codeartifact.errors.service_quota_exceeded_exception.ServiceQuotaExceededException: <p> The operation did not succeed because it would have exceeded a service limit for your account. </p>
            capo_codeartifact.errors.throttling_exception.ThrottlingException: <p> The operation did not succeed because too many requests are sent to the service. </p>
            capo_codeartifact.errors.validation_exception.ValidationException: <p> The operation did not succeed because a parameter in the request was sent with an invalid value. </p>
            capo_codeartifact.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        def _handler(
            req: "OperationRequest[capo_codeartifact.types.delete_package_group_request.DeletePackageGroupRequest]",
        ) -> OperationResponse[
            "capo_codeartifact.types.delete_package_group_result.DeletePackageGroupResult"
        ]:
            import capo_codeartifact._operations.code_artifact_control_plane_service.delete_package_group

            output, http_response = (
                capo_codeartifact._operations.code_artifact_control_plane_service.delete_package_group.delete_package_group(
                    req.options, req.input
                )
            )
            return OperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_codeartifact.types.delete_package_group_request.DeletePackageGroupRequest = {
            "domain": domain,
            "package_group": package_group,
        }
        if domain_owner is not None:
            input_["domain_owner"] = domain_owner

        response = execute_pipeline(
            OperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        response.response.close()
        return response.output

    def delete_package_versions(
        self,
        domain: "capo_codeartifact.types.domain_name.DomainName",
        repository: "capo_codeartifact.types.repository_name.RepositoryName",
        format: "capo_codeartifact.types.package_format.PackageFormat",
        package: "capo_codeartifact.types.package_name.PackageName",
        versions: "capo_codeartifact.types.package_version_list.PackageVersionList",
        *,
        config_overrides: Optional[codeartifactClientConfig] = None,
        domain_owner: Optional["capo_codeartifact.types.account_id.AccountId"] = None,
        namespace: Optional[
            "capo_codeartifact.types.package_namespace.PackageNamespace"
        ] = None,
        expected_status: Optional[
            "capo_codeartifact.types.package_version_status.PackageVersionStatus"
        ] = None,
    ) -> "capo_codeartifact.types.delete_package_versions_result.DeletePackageVersionsResult":
        r"""<p> Deletes one or more versions of a package. A deleted package version cannot be restored in your repository. If you want to remove a package version from your repository and be able to restore it later, set its status to <code>Archived</code>. Archived packages cannot be downloaded from a repository and don't show up with list package APIs (for example, <a href=\"https://docs.aws.amazon.com/codeartifact/latest/APIReference/API_ListPackageVersions.html\">ListPackageVersions</a>), but you can restore them using <a href=\"https://docs.aws.amazon.com/codeartifact/latest/APIReference/API_UpdatePackageVersionsStatus.html\">UpdatePackageVersionsStatus</a>. </p>

        Args:
            domain: <p> The name of the domain that contains the package to delete. </p>
            domain_owner: <p> The 12-digit account number of the Amazon Web Services account that owns the domain. It does not include dashes or spaces. </p>
            repository: <p> The name of the repository that contains the package versions to delete. </p>
            format: <p> The format of the package versions to delete. </p>
            namespace: <p>The namespace of the package versions to be deleted. The package component that specifies its namespace depends on its type. For example:</p> <note> <p>The namespace is required when deleting package versions of the following formats:</p> <ul> <li> <p>Maven</p> </li> <li> <p>Swift</p> </li> <li> <p>generic</p> </li> </ul> </note> <ul> <li> <p> The namespace of a Maven package version is its <code>groupId</code>. </p> </li> <li> <p> The namespace of an npm or Swift package version is its <code>scope</code>. </p> </li> <li> <p>The namespace of a generic package is its <code>namespace</code>.</p> </li> <li> <p> Python, NuGet, Ruby, and Cargo package versions do not contain a corresponding component, package versions of those formats do not have a namespace. </p> </li> </ul>
            package: <p> The name of the package with the versions to delete. </p>
            versions: <p> An array of strings that specify the versions of the package to delete. </p>
            expected_status: <p> The expected status of the package version to delete. </p>

        Raises:
            capo_codeartifact.errors.access_denied_exception.AccessDeniedException: <p> The operation did not succeed because of an unauthorized access attempt. </p>
            capo_codeartifact.errors.conflict_exception.ConflictException: <p> The operation did not succeed because prerequisites are not met. </p>
            capo_codeartifact.errors.internal_server_exception.InternalServerException: <p> The operation did not succeed because of an error that occurred inside CodeArtifact. </p>
            capo_codeartifact.errors.resource_not_found_exception.ResourceNotFoundException: <p> The operation did not succeed because the resource requested is not found in the service. </p>
            capo_codeartifact.errors.throttling_exception.ThrottlingException: <p> The operation did not succeed because too many requests are sent to the service. </p>
            capo_codeartifact.errors.validation_exception.ValidationException: <p> The operation did not succeed because a parameter in the request was sent with an invalid value. </p>
            capo_codeartifact.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        def _handler(
            req: "OperationRequest[capo_codeartifact.types.delete_package_versions_request.DeletePackageVersionsRequest]",
        ) -> OperationResponse[
            "capo_codeartifact.types.delete_package_versions_result.DeletePackageVersionsResult"
        ]:
            import capo_codeartifact._operations.code_artifact_control_plane_service.delete_package_versions

            output, http_response = (
                capo_codeartifact._operations.code_artifact_control_plane_service.delete_package_versions.delete_package_versions(
                    req.options, req.input
                )
            )
            return OperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_codeartifact.types.delete_package_versions_request.DeletePackageVersionsRequest = {
            "domain": domain,
            "repository": repository,
            "format": format,
            "package": package,
            "versions": versions,
        }
        if domain_owner is not None:
            input_["domain_owner"] = domain_owner
        if namespace is not None:
            input_["namespace"] = namespace
        if expected_status is not None:
            input_["expected_status"] = expected_status

        response = execute_pipeline(
            OperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        response.response.close()
        return response.output

    def delete_repository(
        self,
        domain: "capo_codeartifact.types.domain_name.DomainName",
        repository: "capo_codeartifact.types.repository_name.RepositoryName",
        *,
        config_overrides: Optional[codeartifactClientConfig] = None,
        domain_owner: Optional["capo_codeartifact.types.account_id.AccountId"] = None,
    ) -> "capo_codeartifact.types.delete_repository_result.DeleteRepositoryResult":
        """<p> Deletes a repository. </p>

        Args:
            domain: <p> The name of the domain that contains the repository to delete. </p>
            domain_owner: <p> The 12-digit account number of the Amazon Web Services account that owns the domain. It does not include dashes or spaces. </p>
            repository: <p> The name of the repository to delete. </p>

        Raises:
            capo_codeartifact.errors.access_denied_exception.AccessDeniedException: <p> The operation did not succeed because of an unauthorized access attempt. </p>
            capo_codeartifact.errors.conflict_exception.ConflictException: <p> The operation did not succeed because prerequisites are not met. </p>
            capo_codeartifact.errors.internal_server_exception.InternalServerException: <p> The operation did not succeed because of an error that occurred inside CodeArtifact. </p>
            capo_codeartifact.errors.resource_not_found_exception.ResourceNotFoundException: <p> The operation did not succeed because the resource requested is not found in the service. </p>
            capo_codeartifact.errors.throttling_exception.ThrottlingException: <p> The operation did not succeed because too many requests are sent to the service. </p>
            capo_codeartifact.errors.validation_exception.ValidationException: <p> The operation did not succeed because a parameter in the request was sent with an invalid value. </p>
            capo_codeartifact.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        def _handler(
            req: "OperationRequest[capo_codeartifact.types.delete_repository_request.DeleteRepositoryRequest]",
        ) -> OperationResponse[
            "capo_codeartifact.types.delete_repository_result.DeleteRepositoryResult"
        ]:
            import capo_codeartifact._operations.code_artifact_control_plane_service.delete_repository

            output, http_response = (
                capo_codeartifact._operations.code_artifact_control_plane_service.delete_repository.delete_repository(
                    req.options, req.input
                )
            )
            return OperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_codeartifact.types.delete_repository_request.DeleteRepositoryRequest = {
            "domain": domain,
            "repository": repository,
        }
        if domain_owner is not None:
            input_["domain_owner"] = domain_owner

        response = execute_pipeline(
            OperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        response.response.close()
        return response.output

    def delete_repository_permissions_policy(
        self,
        domain: "capo_codeartifact.types.domain_name.DomainName",
        repository: "capo_codeartifact.types.repository_name.RepositoryName",
        *,
        config_overrides: Optional[codeartifactClientConfig] = None,
        domain_owner: Optional["capo_codeartifact.types.account_id.AccountId"] = None,
        policy_revision: Optional[
            "capo_codeartifact.types.policy_revision.PolicyRevision"
        ] = None,
    ) -> "capo_codeartifact.types.delete_repository_permissions_policy_result.DeleteRepositoryPermissionsPolicyResult":
        """<p> Deletes the resource policy that is set on a repository. After a resource policy is deleted, the permissions allowed and denied by the deleted policy are removed. The effect of deleting a resource policy might not be immediate. </p> <important> <p> Use <code>DeleteRepositoryPermissionsPolicy</code> with caution. After a policy is deleted, Amazon Web Services users, roles, and accounts lose permissions to perform the repository actions granted by the deleted policy. </p> </important>

        Args:
            domain: <p> The name of the domain that contains the repository associated with the resource policy to be deleted. </p>
            domain_owner: <p> The 12-digit account number of the Amazon Web Services account that owns the domain. It does not include dashes or spaces. </p>
            repository: <p> The name of the repository that is associated with the resource policy to be deleted </p>
            policy_revision: <p> The revision of the repository's resource policy to be deleted. This revision is used for optimistic locking, which prevents others from accidentally overwriting your changes to the repository's resource policy. </p>

        Raises:
            capo_codeartifact.errors.access_denied_exception.AccessDeniedException: <p> The operation did not succeed because of an unauthorized access attempt. </p>
            capo_codeartifact.errors.conflict_exception.ConflictException: <p> The operation did not succeed because prerequisites are not met. </p>
            capo_codeartifact.errors.internal_server_exception.InternalServerException: <p> The operation did not succeed because of an error that occurred inside CodeArtifact. </p>
            capo_codeartifact.errors.resource_not_found_exception.ResourceNotFoundException: <p> The operation did not succeed because the resource requested is not found in the service. </p>
            capo_codeartifact.errors.throttling_exception.ThrottlingException: <p> The operation did not succeed because too many requests are sent to the service. </p>
            capo_codeartifact.errors.validation_exception.ValidationException: <p> The operation did not succeed because a parameter in the request was sent with an invalid value. </p>
            capo_codeartifact.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        def _handler(
            req: "OperationRequest[capo_codeartifact.types.delete_repository_permissions_policy_request.DeleteRepositoryPermissionsPolicyRequest]",
        ) -> OperationResponse[
            "capo_codeartifact.types.delete_repository_permissions_policy_result.DeleteRepositoryPermissionsPolicyResult"
        ]:
            import capo_codeartifact._operations.code_artifact_control_plane_service.delete_repository_permissions_policy

            output, http_response = (
                capo_codeartifact._operations.code_artifact_control_plane_service.delete_repository_permissions_policy.delete_repository_permissions_policy(
                    req.options, req.input
                )
            )
            return OperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_codeartifact.types.delete_repository_permissions_policy_request.DeleteRepositoryPermissionsPolicyRequest = {
            "domain": domain,
            "repository": repository,
        }
        if domain_owner is not None:
            input_["domain_owner"] = domain_owner
        if policy_revision is not None:
            input_["policy_revision"] = policy_revision

        response = execute_pipeline(
            OperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        response.response.close()
        return response.output

    def describe_domain(
        self,
        domain: "capo_codeartifact.types.domain_name.DomainName",
        *,
        config_overrides: Optional[codeartifactClientConfig] = None,
        domain_owner: Optional["capo_codeartifact.types.account_id.AccountId"] = None,
    ) -> "capo_codeartifact.types.describe_domain_result.DescribeDomainResult":
        r"""<p> Returns a <a href=\"https://docs.aws.amazon.com/codeartifact/latest/APIReference/API_DomainDescription.html\">DomainDescription</a> object that contains information about the requested domain. </p>

        Args:
            domain: <p> A string that specifies the name of the requested domain. </p>
            domain_owner: <p> The 12-digit account number of the Amazon Web Services account that owns the domain. It does not include dashes or spaces. </p>

        Raises:
            capo_codeartifact.errors.access_denied_exception.AccessDeniedException: <p> The operation did not succeed because of an unauthorized access attempt. </p>
            capo_codeartifact.errors.internal_server_exception.InternalServerException: <p> The operation did not succeed because of an error that occurred inside CodeArtifact. </p>
            capo_codeartifact.errors.resource_not_found_exception.ResourceNotFoundException: <p> The operation did not succeed because the resource requested is not found in the service. </p>
            capo_codeartifact.errors.throttling_exception.ThrottlingException: <p> The operation did not succeed because too many requests are sent to the service. </p>
            capo_codeartifact.errors.validation_exception.ValidationException: <p> The operation did not succeed because a parameter in the request was sent with an invalid value. </p>
            capo_codeartifact.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        def _handler(
            req: "OperationRequest[capo_codeartifact.types.describe_domain_request.DescribeDomainRequest]",
        ) -> OperationResponse[
            "capo_codeartifact.types.describe_domain_result.DescribeDomainResult"
        ]:
            import capo_codeartifact._operations.code_artifact_control_plane_service.describe_domain

            output, http_response = (
                capo_codeartifact._operations.code_artifact_control_plane_service.describe_domain.describe_domain(
                    req.options, req.input
                )
            )
            return OperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_codeartifact.types.describe_domain_request.DescribeDomainRequest = {
            "domain": domain
        }
        if domain_owner is not None:
            input_["domain_owner"] = domain_owner

        response = execute_pipeline(
            OperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        response.response.close()
        return response.output

    def describe_package(
        self,
        domain: "capo_codeartifact.types.domain_name.DomainName",
        repository: "capo_codeartifact.types.repository_name.RepositoryName",
        format: "capo_codeartifact.types.package_format.PackageFormat",
        package: "capo_codeartifact.types.package_name.PackageName",
        *,
        config_overrides: Optional[codeartifactClientConfig] = None,
        domain_owner: Optional["capo_codeartifact.types.account_id.AccountId"] = None,
        namespace: Optional[
            "capo_codeartifact.types.package_namespace.PackageNamespace"
        ] = None,
    ) -> "capo_codeartifact.types.describe_package_result.DescribePackageResult":
        r"""<p> Returns a <a href=\"https://docs.aws.amazon.com/codeartifact/latest/APIReference/API_PackageDescription.html\">PackageDescription</a> object that contains information about the requested package.</p>

        Args:
            domain: <p>The name of the domain that contains the repository that contains the package.</p>
            domain_owner: <p> The 12-digit account number of the Amazon Web Services account that owns the domain. It does not include dashes or spaces. </p>
            repository: <p>The name of the repository that contains the requested package. </p>
            format: <p>A format that specifies the type of the requested package.</p>
            namespace: <p>The namespace of the requested package. The package component that specifies its namespace depends on its type. For example:</p> <note> <p>The namespace is required when requesting packages of the following formats:</p> <ul> <li> <p>Maven</p> </li> <li> <p>Swift</p> </li> <li> <p>generic</p> </li> </ul> </note> <ul> <li> <p> The namespace of a Maven package version is its <code>groupId</code>. </p> </li> <li> <p> The namespace of an npm or Swift package version is its <code>scope</code>. </p> </li> <li> <p>The namespace of a generic package is its <code>namespace</code>.</p> </li> <li> <p> Python, NuGet, Ruby, and Cargo package versions do not contain a corresponding component, package versions of those formats do not have a namespace. </p> </li> </ul>
            package: <p>The name of the requested package.</p>

        Raises:
            capo_codeartifact.errors.access_denied_exception.AccessDeniedException: <p> The operation did not succeed because of an unauthorized access attempt. </p>
            capo_codeartifact.errors.internal_server_exception.InternalServerException: <p> The operation did not succeed because of an error that occurred inside CodeArtifact. </p>
            capo_codeartifact.errors.resource_not_found_exception.ResourceNotFoundException: <p> The operation did not succeed because the resource requested is not found in the service. </p>
            capo_codeartifact.errors.throttling_exception.ThrottlingException: <p> The operation did not succeed because too many requests are sent to the service. </p>
            capo_codeartifact.errors.validation_exception.ValidationException: <p> The operation did not succeed because a parameter in the request was sent with an invalid value. </p>
            capo_codeartifact.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        def _handler(
            req: "OperationRequest[capo_codeartifact.types.describe_package_request.DescribePackageRequest]",
        ) -> OperationResponse[
            "capo_codeartifact.types.describe_package_result.DescribePackageResult"
        ]:
            import capo_codeartifact._operations.code_artifact_control_plane_service.describe_package

            output, http_response = (
                capo_codeartifact._operations.code_artifact_control_plane_service.describe_package.describe_package(
                    req.options, req.input
                )
            )
            return OperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_codeartifact.types.describe_package_request.DescribePackageRequest = {
            "domain": domain,
            "repository": repository,
            "format": format,
            "package": package,
        }
        if domain_owner is not None:
            input_["domain_owner"] = domain_owner
        if namespace is not None:
            input_["namespace"] = namespace

        response = execute_pipeline(
            OperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        response.response.close()
        return response.output

    def describe_package_group(
        self,
        domain: "capo_codeartifact.types.domain_name.DomainName",
        package_group: "capo_codeartifact.types.package_group_pattern.PackageGroupPattern",
        *,
        config_overrides: Optional[codeartifactClientConfig] = None,
        domain_owner: Optional["capo_codeartifact.types.account_id.AccountId"] = None,
    ) -> "capo_codeartifact.types.describe_package_group_result.DescribePackageGroupResult":
        r"""<p>Returns a <a href=\"https://docs.aws.amazon.com/codeartifact/latest/APIReference/API_PackageGroupDescription.html\">PackageGroupDescription</a> object that contains information about the requested package group.</p>

        Args:
            domain: <p> The name of the domain that contains the package group. </p>
            domain_owner: <p> The 12-digit account number of the Amazon Web Services account that owns the domain. It does not include dashes or spaces. </p>
            package_group: <p>The pattern of the requested package group.</p>

        Raises:
            capo_codeartifact.errors.access_denied_exception.AccessDeniedException: <p> The operation did not succeed because of an unauthorized access attempt. </p>
            capo_codeartifact.errors.internal_server_exception.InternalServerException: <p> The operation did not succeed because of an error that occurred inside CodeArtifact. </p>
            capo_codeartifact.errors.resource_not_found_exception.ResourceNotFoundException: <p> The operation did not succeed because the resource requested is not found in the service. </p>
            capo_codeartifact.errors.throttling_exception.ThrottlingException: <p> The operation did not succeed because too many requests are sent to the service. </p>
            capo_codeartifact.errors.validation_exception.ValidationException: <p> The operation did not succeed because a parameter in the request was sent with an invalid value. </p>
            capo_codeartifact.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        def _handler(
            req: "OperationRequest[capo_codeartifact.types.describe_package_group_request.DescribePackageGroupRequest]",
        ) -> OperationResponse[
            "capo_codeartifact.types.describe_package_group_result.DescribePackageGroupResult"
        ]:
            import capo_codeartifact._operations.code_artifact_control_plane_service.describe_package_group

            output, http_response = (
                capo_codeartifact._operations.code_artifact_control_plane_service.describe_package_group.describe_package_group(
                    req.options, req.input
                )
            )
            return OperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_codeartifact.types.describe_package_group_request.DescribePackageGroupRequest = {
            "domain": domain,
            "package_group": package_group,
        }
        if domain_owner is not None:
            input_["domain_owner"] = domain_owner

        response = execute_pipeline(
            OperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        response.response.close()
        return response.output

    def describe_package_version(
        self,
        domain: "capo_codeartifact.types.domain_name.DomainName",
        repository: "capo_codeartifact.types.repository_name.RepositoryName",
        format: "capo_codeartifact.types.package_format.PackageFormat",
        package: "capo_codeartifact.types.package_name.PackageName",
        package_version: "capo_codeartifact.types.package_version.PackageVersion",
        *,
        config_overrides: Optional[codeartifactClientConfig] = None,
        domain_owner: Optional["capo_codeartifact.types.account_id.AccountId"] = None,
        namespace: Optional[
            "capo_codeartifact.types.package_namespace.PackageNamespace"
        ] = None,
    ) -> "capo_codeartifact.types.describe_package_version_result.DescribePackageVersionResult":
        r"""<p> Returns a <a href=\"https://docs.aws.amazon.com/codeartifact/latest/APIReference/API_PackageVersionDescription.html\">PackageVersionDescription</a> object that contains information about the requested package version. </p>

        Args:
            domain: <p> The name of the domain that contains the repository that contains the package version. </p>
            domain_owner: <p> The 12-digit account number of the Amazon Web Services account that owns the domain. It does not include dashes or spaces. </p>
            repository: <p> The name of the repository that contains the package version. </p>
            format: <p> A format that specifies the type of the requested package version. </p>
            namespace: <p>The namespace of the requested package version. The package component that specifies its namespace depends on its type. For example:</p> <note> <p>The namespace is required when requesting package versions of the following formats:</p> <ul> <li> <p>Maven</p> </li> <li> <p>Swift</p> </li> <li> <p>generic</p> </li> </ul> </note> <ul> <li> <p> The namespace of a Maven package version is its <code>groupId</code>. </p> </li> <li> <p> The namespace of an npm or Swift package version is its <code>scope</code>. </p> </li> <li> <p>The namespace of a generic package is its <code>namespace</code>.</p> </li> <li> <p> Python, NuGet, Ruby, and Cargo package versions do not contain a corresponding component, package versions of those formats do not have a namespace. </p> </li> </ul>
            package: <p> The name of the requested package version. </p>
            package_version: <p> A string that contains the package version (for example, <code>3.5.2</code>). </p>

        Raises:
            capo_codeartifact.errors.access_denied_exception.AccessDeniedException: <p> The operation did not succeed because of an unauthorized access attempt. </p>
            capo_codeartifact.errors.conflict_exception.ConflictException: <p> The operation did not succeed because prerequisites are not met. </p>
            capo_codeartifact.errors.internal_server_exception.InternalServerException: <p> The operation did not succeed because of an error that occurred inside CodeArtifact. </p>
            capo_codeartifact.errors.resource_not_found_exception.ResourceNotFoundException: <p> The operation did not succeed because the resource requested is not found in the service. </p>
            capo_codeartifact.errors.throttling_exception.ThrottlingException: <p> The operation did not succeed because too many requests are sent to the service. </p>
            capo_codeartifact.errors.validation_exception.ValidationException: <p> The operation did not succeed because a parameter in the request was sent with an invalid value. </p>
            capo_codeartifact.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        def _handler(
            req: "OperationRequest[capo_codeartifact.types.describe_package_version_request.DescribePackageVersionRequest]",
        ) -> OperationResponse[
            "capo_codeartifact.types.describe_package_version_result.DescribePackageVersionResult"
        ]:
            import capo_codeartifact._operations.code_artifact_control_plane_service.describe_package_version

            output, http_response = (
                capo_codeartifact._operations.code_artifact_control_plane_service.describe_package_version.describe_package_version(
                    req.options, req.input
                )
            )
            return OperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_codeartifact.types.describe_package_version_request.DescribePackageVersionRequest = {
            "domain": domain,
            "repository": repository,
            "format": format,
            "package": package,
            "package_version": package_version,
        }
        if domain_owner is not None:
            input_["domain_owner"] = domain_owner
        if namespace is not None:
            input_["namespace"] = namespace

        response = execute_pipeline(
            OperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        response.response.close()
        return response.output

    def describe_repository(
        self,
        domain: "capo_codeartifact.types.domain_name.DomainName",
        repository: "capo_codeartifact.types.repository_name.RepositoryName",
        *,
        config_overrides: Optional[codeartifactClientConfig] = None,
        domain_owner: Optional["capo_codeartifact.types.account_id.AccountId"] = None,
    ) -> "capo_codeartifact.types.describe_repository_result.DescribeRepositoryResult":
        """<p> Returns a <code>RepositoryDescription</code> object that contains detailed information about the requested repository. </p>

        Args:
            domain: <p> The name of the domain that contains the repository to describe. </p>
            domain_owner: <p> The 12-digit account number of the Amazon Web Services account that owns the domain. It does not include dashes or spaces. </p>
            repository: <p> A string that specifies the name of the requested repository. </p>

        Raises:
            capo_codeartifact.errors.access_denied_exception.AccessDeniedException: <p> The operation did not succeed because of an unauthorized access attempt. </p>
            capo_codeartifact.errors.internal_server_exception.InternalServerException: <p> The operation did not succeed because of an error that occurred inside CodeArtifact. </p>
            capo_codeartifact.errors.resource_not_found_exception.ResourceNotFoundException: <p> The operation did not succeed because the resource requested is not found in the service. </p>
            capo_codeartifact.errors.throttling_exception.ThrottlingException: <p> The operation did not succeed because too many requests are sent to the service. </p>
            capo_codeartifact.errors.validation_exception.ValidationException: <p> The operation did not succeed because a parameter in the request was sent with an invalid value. </p>
            capo_codeartifact.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        def _handler(
            req: "OperationRequest[capo_codeartifact.types.describe_repository_request.DescribeRepositoryRequest]",
        ) -> OperationResponse[
            "capo_codeartifact.types.describe_repository_result.DescribeRepositoryResult"
        ]:
            import capo_codeartifact._operations.code_artifact_control_plane_service.describe_repository

            output, http_response = (
                capo_codeartifact._operations.code_artifact_control_plane_service.describe_repository.describe_repository(
                    req.options, req.input
                )
            )
            return OperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_codeartifact.types.describe_repository_request.DescribeRepositoryRequest = {
            "domain": domain,
            "repository": repository,
        }
        if domain_owner is not None:
            input_["domain_owner"] = domain_owner

        response = execute_pipeline(
            OperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        response.response.close()
        return response.output

    def disassociate_external_connection(
        self,
        domain: "capo_codeartifact.types.domain_name.DomainName",
        repository: "capo_codeartifact.types.repository_name.RepositoryName",
        external_connection: "capo_codeartifact.types.external_connection_name.ExternalConnectionName",
        *,
        config_overrides: Optional[codeartifactClientConfig] = None,
        domain_owner: Optional["capo_codeartifact.types.account_id.AccountId"] = None,
    ) -> "capo_codeartifact.types.disassociate_external_connection_result.DisassociateExternalConnectionResult":
        """<p> Removes an existing external connection from a repository. </p>

        Args:
            domain: <p>The name of the domain that contains the repository from which to remove the external repository. </p>
            domain_owner: <p> The 12-digit account number of the Amazon Web Services account that owns the domain. It does not include dashes or spaces. </p>
            repository: <p>The name of the repository from which the external connection will be removed. </p>
            external_connection: <p>The name of the external connection to be removed from the repository. </p>

        Raises:
            capo_codeartifact.errors.access_denied_exception.AccessDeniedException: <p> The operation did not succeed because of an unauthorized access attempt. </p>
            capo_codeartifact.errors.conflict_exception.ConflictException: <p> The operation did not succeed because prerequisites are not met. </p>
            capo_codeartifact.errors.internal_server_exception.InternalServerException: <p> The operation did not succeed because of an error that occurred inside CodeArtifact. </p>
            capo_codeartifact.errors.resource_not_found_exception.ResourceNotFoundException: <p> The operation did not succeed because the resource requested is not found in the service. </p>
            capo_codeartifact.errors.service_quota_exceeded_exception.ServiceQuotaExceededException: <p> The operation did not succeed because it would have exceeded a service limit for your account. </p>
            capo_codeartifact.errors.throttling_exception.ThrottlingException: <p> The operation did not succeed because too many requests are sent to the service. </p>
            capo_codeartifact.errors.validation_exception.ValidationException: <p> The operation did not succeed because a parameter in the request was sent with an invalid value. </p>
            capo_codeartifact.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        def _handler(
            req: "OperationRequest[capo_codeartifact.types.disassociate_external_connection_request.DisassociateExternalConnectionRequest]",
        ) -> OperationResponse[
            "capo_codeartifact.types.disassociate_external_connection_result.DisassociateExternalConnectionResult"
        ]:
            import capo_codeartifact._operations.code_artifact_control_plane_service.disassociate_external_connection

            output, http_response = (
                capo_codeartifact._operations.code_artifact_control_plane_service.disassociate_external_connection.disassociate_external_connection(
                    req.options, req.input
                )
            )
            return OperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_codeartifact.types.disassociate_external_connection_request.DisassociateExternalConnectionRequest = {
            "domain": domain,
            "repository": repository,
            "external_connection": external_connection,
        }
        if domain_owner is not None:
            input_["domain_owner"] = domain_owner

        response = execute_pipeline(
            OperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        response.response.close()
        return response.output

    def dispose_package_versions(
        self,
        domain: "capo_codeartifact.types.domain_name.DomainName",
        repository: "capo_codeartifact.types.repository_name.RepositoryName",
        format: "capo_codeartifact.types.package_format.PackageFormat",
        package: "capo_codeartifact.types.package_name.PackageName",
        versions: "capo_codeartifact.types.package_version_list.PackageVersionList",
        *,
        config_overrides: Optional[codeartifactClientConfig] = None,
        domain_owner: Optional["capo_codeartifact.types.account_id.AccountId"] = None,
        namespace: Optional[
            "capo_codeartifact.types.package_namespace.PackageNamespace"
        ] = None,
        version_revisions: Optional[
            "capo_codeartifact.types.package_version_revision_map.PackageVersionRevisionMap"
        ] = None,
        expected_status: Optional[
            "capo_codeartifact.types.package_version_status.PackageVersionStatus"
        ] = None,
    ) -> "capo_codeartifact.types.dispose_package_versions_result.DisposePackageVersionsResult":
        r"""<p> Deletes the assets in package versions and sets the package versions' status to <code>Disposed</code>. A disposed package version cannot be restored in your repository because its assets are deleted. </p> <p> To view all disposed package versions in a repository, use <a href=\"https://docs.aws.amazon.com/codeartifact/latest/APIReference/API_ListPackageVersions.html\">ListPackageVersions</a> and set the <a href=\"https://docs.aws.amazon.com/codeartifact/latest/APIReference/API_ListPackageVersions.html#API_ListPackageVersions_RequestSyntax\">status</a> parameter to <code>Disposed</code>. </p> <p> To view information about a disposed package version, use <a href=\"https://docs.aws.amazon.com/codeartifact/latest/APIReference/API_DescribePackageVersion.html\">DescribePackageVersion</a>. </p>

        Args:
            domain: <p> The name of the domain that contains the repository you want to dispose. </p>
            domain_owner: <p> The 12-digit account number of the Amazon Web Services account that owns the domain. It does not include dashes or spaces. </p>
            repository: <p> The name of the repository that contains the package versions you want to dispose. </p>
            format: <p> A format that specifies the type of package versions you want to dispose. </p>
            namespace: <p>The namespace of the package versions to be disposed. The package component that specifies its namespace depends on its type. For example:</p> <note> <p>The namespace is required when disposing package versions of the following formats:</p> <ul> <li> <p>Maven</p> </li> <li> <p>Swift</p> </li> <li> <p>generic</p> </li> </ul> </note> <ul> <li> <p> The namespace of a Maven package version is its <code>groupId</code>. </p> </li> <li> <p> The namespace of an npm or Swift package version is its <code>scope</code>. </p> </li> <li> <p>The namespace of a generic package is its <code>namespace</code>.</p> </li> <li> <p> Python, NuGet, Ruby, and Cargo package versions do not contain a corresponding component, package versions of those formats do not have a namespace. </p> </li> </ul>
            package: <p> The name of the package with the versions you want to dispose. </p>
            versions: <p> The versions of the package you want to dispose. </p>
            version_revisions: <p> The revisions of the package versions you want to dispose. </p>
            expected_status: <p> The expected status of the package version to dispose. </p>

        Raises:
            capo_codeartifact.errors.access_denied_exception.AccessDeniedException: <p> The operation did not succeed because of an unauthorized access attempt. </p>
            capo_codeartifact.errors.conflict_exception.ConflictException: <p> The operation did not succeed because prerequisites are not met. </p>
            capo_codeartifact.errors.internal_server_exception.InternalServerException: <p> The operation did not succeed because of an error that occurred inside CodeArtifact. </p>
            capo_codeartifact.errors.resource_not_found_exception.ResourceNotFoundException: <p> The operation did not succeed because the resource requested is not found in the service. </p>
            capo_codeartifact.errors.throttling_exception.ThrottlingException: <p> The operation did not succeed because too many requests are sent to the service. </p>
            capo_codeartifact.errors.validation_exception.ValidationException: <p> The operation did not succeed because a parameter in the request was sent with an invalid value. </p>
            capo_codeartifact.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        def _handler(
            req: "OperationRequest[capo_codeartifact.types.dispose_package_versions_request.DisposePackageVersionsRequest]",
        ) -> OperationResponse[
            "capo_codeartifact.types.dispose_package_versions_result.DisposePackageVersionsResult"
        ]:
            import capo_codeartifact._operations.code_artifact_control_plane_service.dispose_package_versions

            output, http_response = (
                capo_codeartifact._operations.code_artifact_control_plane_service.dispose_package_versions.dispose_package_versions(
                    req.options, req.input
                )
            )
            return OperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_codeartifact.types.dispose_package_versions_request.DisposePackageVersionsRequest = {
            "domain": domain,
            "repository": repository,
            "format": format,
            "package": package,
            "versions": versions,
        }
        if domain_owner is not None:
            input_["domain_owner"] = domain_owner
        if namespace is not None:
            input_["namespace"] = namespace
        if version_revisions is not None:
            input_["version_revisions"] = version_revisions
        if expected_status is not None:
            input_["expected_status"] = expected_status

        response = execute_pipeline(
            OperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        response.response.close()
        return response.output

    def get_associated_package_group(
        self,
        domain: "capo_codeartifact.types.domain_name.DomainName",
        format: "capo_codeartifact.types.package_format.PackageFormat",
        package: "capo_codeartifact.types.package_name.PackageName",
        *,
        config_overrides: Optional[codeartifactClientConfig] = None,
        domain_owner: Optional["capo_codeartifact.types.account_id.AccountId"] = None,
        namespace: Optional[
            "capo_codeartifact.types.package_namespace.PackageNamespace"
        ] = None,
    ) -> "capo_codeartifact.types.get_associated_package_group_result.GetAssociatedPackageGroupResult":
        r"""<p>Returns the most closely associated package group to the specified package. This API does not require that the package exist in any repository in the domain. As such, <code>GetAssociatedPackageGroup</code> can be used to see which package group's origin configuration applies to a package before that package is in a repository. This can be helpful to check if public packages are blocked without ingesting them.</p> <p>For information package group association and matching, see <a href=\"https://docs.aws.amazon.com/codeartifact/latest/ug/package-group-definition-syntax-matching-behavior.html\">Package group definition syntax and matching behavior</a> in the <i>CodeArtifact User Guide</i>.</p>

        Args:
            domain: <p> The name of the domain that contains the package from which to get the associated package group. </p>
            domain_owner: <p> The 12-digit account number of the Amazon Web Services account that owns the domain. It does not include dashes or spaces. </p>
            format: <p> The format of the package from which to get the associated package group. </p>
            namespace: <p>The namespace of the package from which to get the associated package group. The package component that specifies its namespace depends on its type. For example:</p> <note> <p>The namespace is required when getting associated package groups from packages of the following formats:</p> <ul> <li> <p>Maven</p> </li> <li> <p>Swift</p> </li> <li> <p>generic</p> </li> </ul> </note> <ul> <li> <p> The namespace of a Maven package version is its <code>groupId</code>. </p> </li> <li> <p> The namespace of an npm or Swift package version is its <code>scope</code>. </p> </li> <li> <p>The namespace of a generic package is its <code>namespace</code>.</p> </li> <li> <p> Python, NuGet, Ruby, and Cargo package versions do not contain a corresponding component, package versions of those formats do not have a namespace. </p> </li> </ul>
            package: <p> The package from which to get the associated package group. </p>

        Raises:
            capo_codeartifact.errors.access_denied_exception.AccessDeniedException: <p> The operation did not succeed because of an unauthorized access attempt. </p>
            capo_codeartifact.errors.internal_server_exception.InternalServerException: <p> The operation did not succeed because of an error that occurred inside CodeArtifact. </p>
            capo_codeartifact.errors.resource_not_found_exception.ResourceNotFoundException: <p> The operation did not succeed because the resource requested is not found in the service. </p>
            capo_codeartifact.errors.validation_exception.ValidationException: <p> The operation did not succeed because a parameter in the request was sent with an invalid value. </p>
            capo_codeartifact.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        def _handler(
            req: "OperationRequest[capo_codeartifact.types.get_associated_package_group_request.GetAssociatedPackageGroupRequest]",
        ) -> OperationResponse[
            "capo_codeartifact.types.get_associated_package_group_result.GetAssociatedPackageGroupResult"
        ]:
            import capo_codeartifact._operations.code_artifact_control_plane_service.get_associated_package_group

            output, http_response = (
                capo_codeartifact._operations.code_artifact_control_plane_service.get_associated_package_group.get_associated_package_group(
                    req.options, req.input
                )
            )
            return OperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_codeartifact.types.get_associated_package_group_request.GetAssociatedPackageGroupRequest = {
            "domain": domain,
            "format": format,
            "package": package,
        }
        if domain_owner is not None:
            input_["domain_owner"] = domain_owner
        if namespace is not None:
            input_["namespace"] = namespace

        response = execute_pipeline(
            OperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        response.response.close()
        return response.output

    def get_authorization_token(
        self,
        domain: "capo_codeartifact.types.domain_name.DomainName",
        *,
        config_overrides: Optional[codeartifactClientConfig] = None,
        domain_owner: Optional["capo_codeartifact.types.account_id.AccountId"] = None,
        duration_seconds: Optional[
            "capo_codeartifact.types.authorization_token_duration_seconds.AuthorizationTokenDurationSeconds"
        ] = None,
    ) -> "capo_codeartifact.types.get_authorization_token_result.GetAuthorizationTokenResult":
        r"""<p> Generates a temporary authorization token for accessing repositories in the domain. This API requires the <code>codeartifact:GetAuthorizationToken</code> and <code>sts:GetServiceBearerToken</code> permissions. For more information about authorization tokens, see <a href=\"https://docs.aws.amazon.com/codeartifact/latest/ug/tokens-authentication.html\">CodeArtifact authentication and tokens</a>. </p> <note> <p>CodeArtifact authorization tokens are valid for a period of 12 hours when created with the <code>login</code> command. You can call <code>login</code> periodically to refresh the token. When you create an authorization token with the <code>GetAuthorizationToken</code> API, you can set a custom authorization period, up to a maximum of 12 hours, with the <code>durationSeconds</code> parameter.</p> <p>The authorization period begins after <code>login</code> or <code>GetAuthorizationToken</code> is called. If <code>login</code> or <code>GetAuthorizationToken</code> is called while assuming a role, the token lifetime is independent of the maximum session duration of the role. For example, if you call <code>sts assume-role</code> and specify a session duration of 15 minutes, then generate a CodeArtifact authorization token, the token will be valid for the full authorization period even though this is longer than the 15-minute session duration.</p> <p>See <a href=\"https://docs.aws.amazon.com/IAM/latest/UserGuide/id_roles_use.html\">Using IAM Roles</a> for more information on controlling session duration. </p> </note>

        Args:
            domain: <p> The name of the domain that is in scope for the generated authorization token. </p>
            domain_owner: <p> The 12-digit account number of the Amazon Web Services account that owns the domain. It does not include dashes or spaces. </p>
            duration_seconds: <p>The time, in seconds, that the generated authorization token is valid. Valid values are <code>0</code> and any number between <code>900</code> (15 minutes) and <code>43200</code> (12 hours). A value of <code>0</code> will set the expiration of the authorization token to the same expiration of the user's role's temporary credentials.</p>

        Raises:
            capo_codeartifact.errors.access_denied_exception.AccessDeniedException: <p> The operation did not succeed because of an unauthorized access attempt. </p>
            capo_codeartifact.errors.internal_server_exception.InternalServerException: <p> The operation did not succeed because of an error that occurred inside CodeArtifact. </p>
            capo_codeartifact.errors.resource_not_found_exception.ResourceNotFoundException: <p> The operation did not succeed because the resource requested is not found in the service. </p>
            capo_codeartifact.errors.throttling_exception.ThrottlingException: <p> The operation did not succeed because too many requests are sent to the service. </p>
            capo_codeartifact.errors.validation_exception.ValidationException: <p> The operation did not succeed because a parameter in the request was sent with an invalid value. </p>
            capo_codeartifact.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        def _handler(
            req: "OperationRequest[capo_codeartifact.types.get_authorization_token_request.GetAuthorizationTokenRequest]",
        ) -> OperationResponse[
            "capo_codeartifact.types.get_authorization_token_result.GetAuthorizationTokenResult"
        ]:
            import capo_codeartifact._operations.code_artifact_control_plane_service.get_authorization_token

            output, http_response = (
                capo_codeartifact._operations.code_artifact_control_plane_service.get_authorization_token.get_authorization_token(
                    req.options, req.input
                )
            )
            return OperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_codeartifact.types.get_authorization_token_request.GetAuthorizationTokenRequest = {
            "domain": domain
        }
        if domain_owner is not None:
            input_["domain_owner"] = domain_owner
        if duration_seconds is not None:
            input_["duration_seconds"] = duration_seconds

        response = execute_pipeline(
            OperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        response.response.close()
        return response.output

    def get_domain_permissions_policy(
        self,
        domain: "capo_codeartifact.types.domain_name.DomainName",
        *,
        config_overrides: Optional[codeartifactClientConfig] = None,
        domain_owner: Optional["capo_codeartifact.types.account_id.AccountId"] = None,
    ) -> "capo_codeartifact.types.get_domain_permissions_policy_result.GetDomainPermissionsPolicyResult":
        r"""<p> Returns the resource policy attached to the specified domain. </p> <note> <p> The policy is a resource-based policy, not an identity-based policy. For more information, see <a href=\"https://docs.aws.amazon.com/IAM/latest/UserGuide/access_policies_identity-vs-resource.html\">Identity-based policies and resource-based policies </a> in the <i>IAM User Guide</i>. </p> </note>

        Args:
            domain: <p> The name of the domain to which the resource policy is attached. </p>
            domain_owner: <p> The 12-digit account number of the Amazon Web Services account that owns the domain. It does not include dashes or spaces. </p>

        Raises:
            capo_codeartifact.errors.access_denied_exception.AccessDeniedException: <p> The operation did not succeed because of an unauthorized access attempt. </p>
            capo_codeartifact.errors.internal_server_exception.InternalServerException: <p> The operation did not succeed because of an error that occurred inside CodeArtifact. </p>
            capo_codeartifact.errors.resource_not_found_exception.ResourceNotFoundException: <p> The operation did not succeed because the resource requested is not found in the service. </p>
            capo_codeartifact.errors.throttling_exception.ThrottlingException: <p> The operation did not succeed because too many requests are sent to the service. </p>
            capo_codeartifact.errors.validation_exception.ValidationException: <p> The operation did not succeed because a parameter in the request was sent with an invalid value. </p>
            capo_codeartifact.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        def _handler(
            req: "OperationRequest[capo_codeartifact.types.get_domain_permissions_policy_request.GetDomainPermissionsPolicyRequest]",
        ) -> OperationResponse[
            "capo_codeartifact.types.get_domain_permissions_policy_result.GetDomainPermissionsPolicyResult"
        ]:
            import capo_codeartifact._operations.code_artifact_control_plane_service.get_domain_permissions_policy

            output, http_response = (
                capo_codeartifact._operations.code_artifact_control_plane_service.get_domain_permissions_policy.get_domain_permissions_policy(
                    req.options, req.input
                )
            )
            return OperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_codeartifact.types.get_domain_permissions_policy_request.GetDomainPermissionsPolicyRequest = {
            "domain": domain
        }
        if domain_owner is not None:
            input_["domain_owner"] = domain_owner

        response = execute_pipeline(
            OperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        response.response.close()
        return response.output

    @contextmanager
    def get_package_version_asset(
        self,
        domain: "capo_codeartifact.types.domain_name.DomainName",
        repository: "capo_codeartifact.types.repository_name.RepositoryName",
        format: "capo_codeartifact.types.package_format.PackageFormat",
        package: "capo_codeartifact.types.package_name.PackageName",
        package_version: "capo_codeartifact.types.package_version.PackageVersion",
        asset: "capo_codeartifact.types.asset_name.AssetName",
        *,
        config_overrides: Optional[codeartifactClientConfig] = None,
        domain_owner: Optional["capo_codeartifact.types.account_id.AccountId"] = None,
        namespace: Optional[
            "capo_codeartifact.types.package_namespace.PackageNamespace"
        ] = None,
        package_version_revision: Optional[
            "capo_codeartifact.types.package_version_revision.PackageVersionRevision"
        ] = None,
    ) -> "Generator[capo_codeartifact.types.get_package_version_asset_result.GetPackageVersionAssetResult]":
        """<p> Returns an asset (or file) that is in a package. For example, for a Maven package version, use <code>GetPackageVersionAsset</code> to download a <code>JAR</code> file, a <code>POM</code> file, or any other assets in the package version. </p>

        Args:
            domain: <p> The name of the domain that contains the repository that contains the package version with the requested asset. </p>
            domain_owner: <p> The 12-digit account number of the Amazon Web Services account that owns the domain. It does not include dashes or spaces. </p>
            repository: <p> The repository that contains the package version with the requested asset. </p>
            format: <p> A format that specifies the type of the package version with the requested asset file. </p>
            namespace: <p>The namespace of the package version with the requested asset file. The package component that specifies its namespace depends on its type. For example:</p> <note> <p>The namespace is required when requesting assets from package versions of the following formats:</p> <ul> <li> <p>Maven</p> </li> <li> <p>Swift</p> </li> <li> <p>generic</p> </li> </ul> </note> <ul> <li> <p> The namespace of a Maven package version is its <code>groupId</code>. </p> </li> <li> <p> The namespace of an npm or Swift package version is its <code>scope</code>. </p> </li> <li> <p>The namespace of a generic package is its <code>namespace</code>.</p> </li> <li> <p> Python, NuGet, Ruby, and Cargo package versions do not contain a corresponding component, package versions of those formats do not have a namespace. </p> </li> </ul>
            package: <p> The name of the package that contains the requested asset. </p>
            package_version: <p> A string that contains the package version (for example, <code>3.5.2</code>). </p>
            asset: <p> The name of the requested asset. </p>
            package_version_revision: <p> The name of the package version revision that contains the requested asset. </p>

        Raises:
            capo_codeartifact.errors.access_denied_exception.AccessDeniedException: <p> The operation did not succeed because of an unauthorized access attempt. </p>
            capo_codeartifact.errors.conflict_exception.ConflictException: <p> The operation did not succeed because prerequisites are not met. </p>
            capo_codeartifact.errors.internal_server_exception.InternalServerException: <p> The operation did not succeed because of an error that occurred inside CodeArtifact. </p>
            capo_codeartifact.errors.resource_not_found_exception.ResourceNotFoundException: <p> The operation did not succeed because the resource requested is not found in the service. </p>
            capo_codeartifact.errors.throttling_exception.ThrottlingException: <p> The operation did not succeed because too many requests are sent to the service. </p>
            capo_codeartifact.errors.validation_exception.ValidationException: <p> The operation did not succeed because a parameter in the request was sent with an invalid value. </p>
            capo_codeartifact.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        def _handler(
            req: "OperationRequest[capo_codeartifact.types.get_package_version_asset_request.GetPackageVersionAssetRequest]",
        ) -> OperationResponse[
            "capo_codeartifact.types.get_package_version_asset_result.GetPackageVersionAssetResult"
        ]:
            import capo_codeartifact._operations.code_artifact_control_plane_service.get_package_version_asset

            output, http_response = (
                capo_codeartifact._operations.code_artifact_control_plane_service.get_package_version_asset.get_package_version_asset(
                    req.options, req.input
                )
            )
            return OperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_codeartifact.types.get_package_version_asset_request.GetPackageVersionAssetRequest = {
            "domain": domain,
            "repository": repository,
            "format": format,
            "package": package,
            "package_version": package_version,
            "asset": asset,
        }
        if domain_owner is not None:
            input_["domain_owner"] = domain_owner
        if namespace is not None:
            input_["namespace"] = namespace
        if package_version_revision is not None:
            input_["package_version_revision"] = package_version_revision

        response = execute_pipeline(
            OperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        try:
            yield response.output
        finally:
            response.response.close()

    def get_package_version_readme(
        self,
        domain: "capo_codeartifact.types.domain_name.DomainName",
        repository: "capo_codeartifact.types.repository_name.RepositoryName",
        format: "capo_codeartifact.types.package_format.PackageFormat",
        package: "capo_codeartifact.types.package_name.PackageName",
        package_version: "capo_codeartifact.types.package_version.PackageVersion",
        *,
        config_overrides: Optional[codeartifactClientConfig] = None,
        domain_owner: Optional["capo_codeartifact.types.account_id.AccountId"] = None,
        namespace: Optional[
            "capo_codeartifact.types.package_namespace.PackageNamespace"
        ] = None,
    ) -> "capo_codeartifact.types.get_package_version_readme_result.GetPackageVersionReadmeResult":
        """<p> Gets the readme file or descriptive text for a package version. </p> <p> The returned text might contain formatting. For example, it might contain formatting for Markdown or reStructuredText. </p>

        Args:
            domain: <p> The name of the domain that contains the repository that contains the package version with the requested readme file. </p>
            domain_owner: <p> The 12-digit account number of the Amazon Web Services account that owns the domain. It does not include dashes or spaces. </p>
            repository: <p> The repository that contains the package with the requested readme file. </p>
            format: <p> A format that specifies the type of the package version with the requested readme file. </p>
            namespace: <p>The namespace of the package version with the requested readme file. The package component that specifies its namespace depends on its type. For example:</p> <note> <p>The namespace is required when requesting the readme from package versions of the following formats:</p> <ul> <li> <p>Maven</p> </li> <li> <p>Swift</p> </li> <li> <p>generic</p> </li> </ul> </note> <ul> <li> <p> The namespace of a Maven package version is its <code>groupId</code>. </p> </li> <li> <p> The namespace of an npm or Swift package version is its <code>scope</code>. </p> </li> <li> <p>The namespace of a generic package is its <code>namespace</code>.</p> </li> <li> <p> Python, NuGet, Ruby, and Cargo package versions do not contain a corresponding component, package versions of those formats do not have a namespace. </p> </li> </ul>
            package: <p> The name of the package version that contains the requested readme file. </p>
            package_version: <p> A string that contains the package version (for example, <code>3.5.2</code>). </p>

        Raises:
            capo_codeartifact.errors.access_denied_exception.AccessDeniedException: <p> The operation did not succeed because of an unauthorized access attempt. </p>
            capo_codeartifact.errors.internal_server_exception.InternalServerException: <p> The operation did not succeed because of an error that occurred inside CodeArtifact. </p>
            capo_codeartifact.errors.resource_not_found_exception.ResourceNotFoundException: <p> The operation did not succeed because the resource requested is not found in the service. </p>
            capo_codeartifact.errors.throttling_exception.ThrottlingException: <p> The operation did not succeed because too many requests are sent to the service. </p>
            capo_codeartifact.errors.validation_exception.ValidationException: <p> The operation did not succeed because a parameter in the request was sent with an invalid value. </p>
            capo_codeartifact.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        def _handler(
            req: "OperationRequest[capo_codeartifact.types.get_package_version_readme_request.GetPackageVersionReadmeRequest]",
        ) -> OperationResponse[
            "capo_codeartifact.types.get_package_version_readme_result.GetPackageVersionReadmeResult"
        ]:
            import capo_codeartifact._operations.code_artifact_control_plane_service.get_package_version_readme

            output, http_response = (
                capo_codeartifact._operations.code_artifact_control_plane_service.get_package_version_readme.get_package_version_readme(
                    req.options, req.input
                )
            )
            return OperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_codeartifact.types.get_package_version_readme_request.GetPackageVersionReadmeRequest = {
            "domain": domain,
            "repository": repository,
            "format": format,
            "package": package,
            "package_version": package_version,
        }
        if domain_owner is not None:
            input_["domain_owner"] = domain_owner
        if namespace is not None:
            input_["namespace"] = namespace

        response = execute_pipeline(
            OperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        response.response.close()
        return response.output

    def get_repository_endpoint(
        self,
        domain: "capo_codeartifact.types.domain_name.DomainName",
        repository: "capo_codeartifact.types.repository_name.RepositoryName",
        format: "capo_codeartifact.types.package_format.PackageFormat",
        *,
        config_overrides: Optional[codeartifactClientConfig] = None,
        domain_owner: Optional["capo_codeartifact.types.account_id.AccountId"] = None,
        endpoint_type: Optional[
            "capo_codeartifact.types.endpoint_type.EndpointType"
        ] = None,
    ) -> "capo_codeartifact.types.get_repository_endpoint_result.GetRepositoryEndpointResult":
        """<p> Returns the endpoint of a repository for a specific package format. A repository has one endpoint for each package format: </p> <ul> <li> <p> <code>cargo</code> </p> </li> <li> <p> <code>generic</code> </p> </li> <li> <p> <code>maven</code> </p> </li> <li> <p> <code>npm</code> </p> </li> <li> <p> <code>nuget</code> </p> </li> <li> <p> <code>pypi</code> </p> </li> <li> <p> <code>ruby</code> </p> </li> <li> <p> <code>swift</code> </p> </li> </ul>

        Args:
            domain: <p> The name of the domain that contains the repository. </p>
            domain_owner: <p> The 12-digit account number of the Amazon Web Services account that owns the domain that contains the repository. It does not include dashes or spaces. </p>
            repository: <p> The name of the repository. </p>
            format: <p> Returns which endpoint of a repository to return. A repository has one endpoint for each package format. </p>
            endpoint_type: <p>A string that specifies the type of endpoint.</p>

        Raises:
            capo_codeartifact.errors.access_denied_exception.AccessDeniedException: <p> The operation did not succeed because of an unauthorized access attempt. </p>
            capo_codeartifact.errors.internal_server_exception.InternalServerException: <p> The operation did not succeed because of an error that occurred inside CodeArtifact. </p>
            capo_codeartifact.errors.resource_not_found_exception.ResourceNotFoundException: <p> The operation did not succeed because the resource requested is not found in the service. </p>
            capo_codeartifact.errors.throttling_exception.ThrottlingException: <p> The operation did not succeed because too many requests are sent to the service. </p>
            capo_codeartifact.errors.validation_exception.ValidationException: <p> The operation did not succeed because a parameter in the request was sent with an invalid value. </p>
            capo_codeartifact.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        def _handler(
            req: "OperationRequest[capo_codeartifact.types.get_repository_endpoint_request.GetRepositoryEndpointRequest]",
        ) -> OperationResponse[
            "capo_codeartifact.types.get_repository_endpoint_result.GetRepositoryEndpointResult"
        ]:
            import capo_codeartifact._operations.code_artifact_control_plane_service.get_repository_endpoint

            output, http_response = (
                capo_codeartifact._operations.code_artifact_control_plane_service.get_repository_endpoint.get_repository_endpoint(
                    req.options, req.input
                )
            )
            return OperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_codeartifact.types.get_repository_endpoint_request.GetRepositoryEndpointRequest = {
            "domain": domain,
            "repository": repository,
            "format": format,
        }
        if domain_owner is not None:
            input_["domain_owner"] = domain_owner
        if endpoint_type is not None:
            input_["endpoint_type"] = endpoint_type

        response = execute_pipeline(
            OperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        response.response.close()
        return response.output

    def get_repository_permissions_policy(
        self,
        domain: "capo_codeartifact.types.domain_name.DomainName",
        repository: "capo_codeartifact.types.repository_name.RepositoryName",
        *,
        config_overrides: Optional[codeartifactClientConfig] = None,
        domain_owner: Optional["capo_codeartifact.types.account_id.AccountId"] = None,
    ) -> "capo_codeartifact.types.get_repository_permissions_policy_result.GetRepositoryPermissionsPolicyResult":
        """<p> Returns the resource policy that is set on a repository. </p>

        Args:
            domain: <p> The name of the domain containing the repository whose associated resource policy is to be retrieved. </p>
            domain_owner: <p> The 12-digit account number of the Amazon Web Services account that owns the domain. It does not include dashes or spaces. </p>
            repository: <p> The name of the repository whose associated resource policy is to be retrieved. </p>

        Raises:
            capo_codeartifact.errors.access_denied_exception.AccessDeniedException: <p> The operation did not succeed because of an unauthorized access attempt. </p>
            capo_codeartifact.errors.internal_server_exception.InternalServerException: <p> The operation did not succeed because of an error that occurred inside CodeArtifact. </p>
            capo_codeartifact.errors.resource_not_found_exception.ResourceNotFoundException: <p> The operation did not succeed because the resource requested is not found in the service. </p>
            capo_codeartifact.errors.throttling_exception.ThrottlingException: <p> The operation did not succeed because too many requests are sent to the service. </p>
            capo_codeartifact.errors.validation_exception.ValidationException: <p> The operation did not succeed because a parameter in the request was sent with an invalid value. </p>
            capo_codeartifact.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        def _handler(
            req: "OperationRequest[capo_codeartifact.types.get_repository_permissions_policy_request.GetRepositoryPermissionsPolicyRequest]",
        ) -> OperationResponse[
            "capo_codeartifact.types.get_repository_permissions_policy_result.GetRepositoryPermissionsPolicyResult"
        ]:
            import capo_codeartifact._operations.code_artifact_control_plane_service.get_repository_permissions_policy

            output, http_response = (
                capo_codeartifact._operations.code_artifact_control_plane_service.get_repository_permissions_policy.get_repository_permissions_policy(
                    req.options, req.input
                )
            )
            return OperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_codeartifact.types.get_repository_permissions_policy_request.GetRepositoryPermissionsPolicyRequest = {
            "domain": domain,
            "repository": repository,
        }
        if domain_owner is not None:
            input_["domain_owner"] = domain_owner

        response = execute_pipeline(
            OperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        response.response.close()
        return response.output

    def list_allowed_repositories_for_group(
        self,
        domain: "capo_codeartifact.types.domain_name.DomainName",
        package_group: "capo_codeartifact.types.package_group_pattern.PackageGroupPattern",
        origin_restriction_type: "capo_codeartifact.types.package_group_origin_restriction_type.PackageGroupOriginRestrictionType",
        *,
        config_overrides: Optional[codeartifactClientConfig] = None,
        domain_owner: Optional["capo_codeartifact.types.account_id.AccountId"] = None,
        max_results: Optional[
            "capo_codeartifact.types.list_allowed_repositories_for_group_max_results.ListAllowedRepositoriesForGroupMaxResults"
        ] = None,
        next_token: Optional[
            "capo_codeartifact.types.pagination_token.PaginationToken"
        ] = None,
    ) -> "capo_codeartifact.types.list_allowed_repositories_for_group_result.ListAllowedRepositoriesForGroupResult":
        r"""<p>Lists the repositories in the added repositories list of the specified restriction type for a package group. For more information about restriction types and added repository lists, see <a href=\"https://docs.aws.amazon.com/codeartifact/latest/ug/package-group-origin-controls.html\">Package group origin controls</a> in the <i>CodeArtifact User Guide</i>. </p>

        Args:
            domain: <p> The name of the domain that contains the package group from which to list allowed repositories. </p>
            domain_owner: <p> The 12-digit account number of the Amazon Web Services account that owns the domain. It does not include dashes or spaces. </p>
            package_group: <p>The pattern of the package group from which to list allowed repositories.</p>
            origin_restriction_type: <p>The origin configuration restriction type of which to list allowed repositories.</p>
            max_results: <p> The maximum number of results to return per page. </p>
            next_token: <p> The token for the next set of results. Use the value returned in the previous response in the next request to retrieve the next set of results. </p>

        Raises:
            capo_codeartifact.errors.access_denied_exception.AccessDeniedException: <p> The operation did not succeed because of an unauthorized access attempt. </p>
            capo_codeartifact.errors.internal_server_exception.InternalServerException: <p> The operation did not succeed because of an error that occurred inside CodeArtifact. </p>
            capo_codeartifact.errors.resource_not_found_exception.ResourceNotFoundException: <p> The operation did not succeed because the resource requested is not found in the service. </p>
            capo_codeartifact.errors.service_quota_exceeded_exception.ServiceQuotaExceededException: <p> The operation did not succeed because it would have exceeded a service limit for your account. </p>
            capo_codeartifact.errors.throttling_exception.ThrottlingException: <p> The operation did not succeed because too many requests are sent to the service. </p>
            capo_codeartifact.errors.validation_exception.ValidationException: <p> The operation did not succeed because a parameter in the request was sent with an invalid value. </p>
            capo_codeartifact.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        def _handler(
            req: "OperationRequest[capo_codeartifact.types.list_allowed_repositories_for_group_request.ListAllowedRepositoriesForGroupRequest]",
        ) -> OperationResponse[
            "capo_codeartifact.types.list_allowed_repositories_for_group_result.ListAllowedRepositoriesForGroupResult"
        ]:
            import capo_codeartifact._operations.code_artifact_control_plane_service.list_allowed_repositories_for_group

            output, http_response = (
                capo_codeartifact._operations.code_artifact_control_plane_service.list_allowed_repositories_for_group.list_allowed_repositories_for_group(
                    req.options, req.input
                )
            )
            return OperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_codeartifact.types.list_allowed_repositories_for_group_request.ListAllowedRepositoriesForGroupRequest = {
            "domain": domain,
            "package_group": package_group,
            "origin_restriction_type": origin_restriction_type,
        }
        if domain_owner is not None:
            input_["domain_owner"] = domain_owner
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

    def iter_list_allowed_repositories_for_group(
        self,
        domain: "capo_codeartifact.types.domain_name.DomainName",
        package_group: "capo_codeartifact.types.package_group_pattern.PackageGroupPattern",
        origin_restriction_type: "capo_codeartifact.types.package_group_origin_restriction_type.PackageGroupOriginRestrictionType",
        *,
        config_overrides: Optional[codeartifactClientConfig] = None,
        domain_owner: Optional["capo_codeartifact.types.account_id.AccountId"] = None,
        max_results: Optional[
            "capo_codeartifact.types.list_allowed_repositories_for_group_max_results.ListAllowedRepositoriesForGroupMaxResults"
        ] = None,
        next_token: Optional[
            "capo_codeartifact.types.pagination_token.PaginationToken"
        ] = None,
    ) -> "Iterator[capo_codeartifact.types.repository_name.RepositoryName]":
        _token = next_token
        while True:
            _response = self.list_allowed_repositories_for_group(
                domain,
                package_group,
                origin_restriction_type,
                config_overrides=config_overrides,
                domain_owner=domain_owner,
                max_results=max_results,
                next_token=_token,
            )
            _page = _resolve_path(_response, ("allowed_repositories",))
            for _item in _page or []:
                yield _item
            _token = _resolve_path(_response, ("next_token",))
            if not _token:
                break

    def list_associated_packages(
        self,
        domain: "capo_codeartifact.types.domain_name.DomainName",
        package_group: "capo_codeartifact.types.package_group_pattern.PackageGroupPattern",
        *,
        config_overrides: Optional[codeartifactClientConfig] = None,
        domain_owner: Optional["capo_codeartifact.types.account_id.AccountId"] = None,
        max_results: Optional[
            "capo_codeartifact.types.list_packages_max_results.ListPackagesMaxResults"
        ] = None,
        next_token: Optional[
            "capo_codeartifact.types.pagination_token.PaginationToken"
        ] = None,
        preview: Optional[
            "capo_codeartifact.types.boolean_optional.BooleanOptional"
        ] = None,
    ) -> "capo_codeartifact.types.list_associated_packages_result.ListAssociatedPackagesResult":
        r"""<p>Returns a list of packages associated with the requested package group. For information package group association and matching, see <a href=\"https://docs.aws.amazon.com/codeartifact/latest/ug/package-group-definition-syntax-matching-behavior.html\">Package group definition syntax and matching behavior</a> in the <i>CodeArtifact User Guide</i>.</p>

        Args:
            domain: <p> The name of the domain that contains the package group from which to list associated packages. </p>
            domain_owner: <p> The 12-digit account number of the Amazon Web Services account that owns the domain. It does not include dashes or spaces. </p>
            package_group: <p> The pattern of the package group from which to list associated packages. </p>
            max_results: <p> The maximum number of results to return per page. </p>
            next_token: <p> The token for the next set of results. Use the value returned in the previous response in the next request to retrieve the next set of results. </p>
            preview: <p> When this flag is included, <code>ListAssociatedPackages</code> will return a list of packages that would be associated with a package group, even if it does not exist. </p>

        Raises:
            capo_codeartifact.errors.access_denied_exception.AccessDeniedException: <p> The operation did not succeed because of an unauthorized access attempt. </p>
            capo_codeartifact.errors.internal_server_exception.InternalServerException: <p> The operation did not succeed because of an error that occurred inside CodeArtifact. </p>
            capo_codeartifact.errors.resource_not_found_exception.ResourceNotFoundException: <p> The operation did not succeed because the resource requested is not found in the service. </p>
            capo_codeartifact.errors.validation_exception.ValidationException: <p> The operation did not succeed because a parameter in the request was sent with an invalid value. </p>
            capo_codeartifact.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        def _handler(
            req: "OperationRequest[capo_codeartifact.types.list_associated_packages_request.ListAssociatedPackagesRequest]",
        ) -> OperationResponse[
            "capo_codeartifact.types.list_associated_packages_result.ListAssociatedPackagesResult"
        ]:
            import capo_codeartifact._operations.code_artifact_control_plane_service.list_associated_packages

            output, http_response = (
                capo_codeartifact._operations.code_artifact_control_plane_service.list_associated_packages.list_associated_packages(
                    req.options, req.input
                )
            )
            return OperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_codeartifact.types.list_associated_packages_request.ListAssociatedPackagesRequest = {
            "domain": domain,
            "package_group": package_group,
        }
        if domain_owner is not None:
            input_["domain_owner"] = domain_owner
        if max_results is not None:
            input_["max_results"] = max_results
        if next_token is not None:
            input_["next_token"] = next_token
        if preview is not None:
            input_["preview"] = preview

        response = execute_pipeline(
            OperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        response.response.close()
        return response.output

    def iter_list_associated_packages(
        self,
        domain: "capo_codeartifact.types.domain_name.DomainName",
        package_group: "capo_codeartifact.types.package_group_pattern.PackageGroupPattern",
        *,
        config_overrides: Optional[codeartifactClientConfig] = None,
        domain_owner: Optional["capo_codeartifact.types.account_id.AccountId"] = None,
        max_results: Optional[
            "capo_codeartifact.types.list_packages_max_results.ListPackagesMaxResults"
        ] = None,
        next_token: Optional[
            "capo_codeartifact.types.pagination_token.PaginationToken"
        ] = None,
        preview: Optional[
            "capo_codeartifact.types.boolean_optional.BooleanOptional"
        ] = None,
    ) -> "Iterator[capo_codeartifact.types.associated_package.AssociatedPackage]":
        _token = next_token
        while True:
            _response = self.list_associated_packages(
                domain,
                package_group,
                config_overrides=config_overrides,
                domain_owner=domain_owner,
                max_results=max_results,
                next_token=_token,
                preview=preview,
            )
            _page = _resolve_path(_response, ("packages",))
            for _item in _page or []:
                yield _item
            _token = _resolve_path(_response, ("next_token",))
            if not _token:
                break

    def list_domains(
        self,
        *,
        config_overrides: Optional[codeartifactClientConfig] = None,
        max_results: Optional[
            "capo_codeartifact.types.list_domains_max_results.ListDomainsMaxResults"
        ] = None,
        next_token: Optional[
            "capo_codeartifact.types.pagination_token.PaginationToken"
        ] = None,
    ) -> "capo_codeartifact.types.list_domains_result.ListDomainsResult":
        r"""<p> Returns a list of <a href=\"https://docs.aws.amazon.com/codeartifact/latest/APIReference/API_PackageVersionDescription.html\">DomainSummary</a> objects for all domains owned by the Amazon Web Services account that makes this call. Each returned <code>DomainSummary</code> object contains information about a domain. </p>

        Args:
            max_results: <p> The maximum number of results to return per page. </p>
            next_token: <p> The token for the next set of results. Use the value returned in the previous response in the next request to retrieve the next set of results. </p>

        Raises:
            capo_codeartifact.errors.access_denied_exception.AccessDeniedException: <p> The operation did not succeed because of an unauthorized access attempt. </p>
            capo_codeartifact.errors.internal_server_exception.InternalServerException: <p> The operation did not succeed because of an error that occurred inside CodeArtifact. </p>
            capo_codeartifact.errors.throttling_exception.ThrottlingException: <p> The operation did not succeed because too many requests are sent to the service. </p>
            capo_codeartifact.errors.validation_exception.ValidationException: <p> The operation did not succeed because a parameter in the request was sent with an invalid value. </p>
            capo_codeartifact.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        def _handler(
            req: "OperationRequest[capo_codeartifact.types.list_domains_request.ListDomainsRequest]",
        ) -> OperationResponse[
            "capo_codeartifact.types.list_domains_result.ListDomainsResult"
        ]:
            import capo_codeartifact._operations.code_artifact_control_plane_service.list_domains

            output, http_response = (
                capo_codeartifact._operations.code_artifact_control_plane_service.list_domains.list_domains(
                    req.options, req.input
                )
            )
            return OperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_codeartifact.types.list_domains_request.ListDomainsRequest = {}
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

    def iter_list_domains(
        self,
        *,
        config_overrides: Optional[codeartifactClientConfig] = None,
        max_results: Optional[
            "capo_codeartifact.types.list_domains_max_results.ListDomainsMaxResults"
        ] = None,
        next_token: Optional[
            "capo_codeartifact.types.pagination_token.PaginationToken"
        ] = None,
    ) -> "Iterator[capo_codeartifact.types.domain_summary.DomainSummary]":
        _token = next_token
        while True:
            _response = self.list_domains(
                config_overrides=config_overrides,
                max_results=max_results,
                next_token=_token,
            )
            _page = _resolve_path(_response, ("domains",))
            for _item in _page or []:
                yield _item
            _token = _resolve_path(_response, ("next_token",))
            if not _token:
                break

    def list_package_groups(
        self,
        domain: "capo_codeartifact.types.domain_name.DomainName",
        *,
        config_overrides: Optional[codeartifactClientConfig] = None,
        domain_owner: Optional["capo_codeartifact.types.account_id.AccountId"] = None,
        max_results: Optional[
            "capo_codeartifact.types.list_package_groups_max_results.ListPackageGroupsMaxResults"
        ] = None,
        next_token: Optional[
            "capo_codeartifact.types.pagination_token.PaginationToken"
        ] = None,
        prefix: Optional[
            "capo_codeartifact.types.package_group_pattern_prefix.PackageGroupPatternPrefix"
        ] = None,
    ) -> "capo_codeartifact.types.list_package_groups_result.ListPackageGroupsResult":
        """<p>Returns a list of package groups in the requested domain.</p>

        Args:
            domain: <p> The domain for which you want to list package groups. </p>
            domain_owner: <p> The 12-digit account number of the Amazon Web Services account that owns the domain. It does not include dashes or spaces. </p>
            max_results: <p> The maximum number of results to return per page. </p>
            next_token: <p> The token for the next set of results. Use the value returned in the previous response in the next request to retrieve the next set of results. </p>
            prefix: <p> A prefix for which to search package groups. When included, <code>ListPackageGroups</code> will return only package groups with patterns that match the prefix. </p>

        Raises:
            capo_codeartifact.errors.access_denied_exception.AccessDeniedException: <p> The operation did not succeed because of an unauthorized access attempt. </p>
            capo_codeartifact.errors.internal_server_exception.InternalServerException: <p> The operation did not succeed because of an error that occurred inside CodeArtifact. </p>
            capo_codeartifact.errors.resource_not_found_exception.ResourceNotFoundException: <p> The operation did not succeed because the resource requested is not found in the service. </p>
            capo_codeartifact.errors.throttling_exception.ThrottlingException: <p> The operation did not succeed because too many requests are sent to the service. </p>
            capo_codeartifact.errors.validation_exception.ValidationException: <p> The operation did not succeed because a parameter in the request was sent with an invalid value. </p>
            capo_codeartifact.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        def _handler(
            req: "OperationRequest[capo_codeartifact.types.list_package_groups_request.ListPackageGroupsRequest]",
        ) -> OperationResponse[
            "capo_codeartifact.types.list_package_groups_result.ListPackageGroupsResult"
        ]:
            import capo_codeartifact._operations.code_artifact_control_plane_service.list_package_groups

            output, http_response = (
                capo_codeartifact._operations.code_artifact_control_plane_service.list_package_groups.list_package_groups(
                    req.options, req.input
                )
            )
            return OperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_codeartifact.types.list_package_groups_request.ListPackageGroupsRequest = {
            "domain": domain
        }
        if domain_owner is not None:
            input_["domain_owner"] = domain_owner
        if max_results is not None:
            input_["max_results"] = max_results
        if next_token is not None:
            input_["next_token"] = next_token
        if prefix is not None:
            input_["prefix"] = prefix

        response = execute_pipeline(
            OperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        response.response.close()
        return response.output

    def iter_list_package_groups(
        self,
        domain: "capo_codeartifact.types.domain_name.DomainName",
        *,
        config_overrides: Optional[codeartifactClientConfig] = None,
        domain_owner: Optional["capo_codeartifact.types.account_id.AccountId"] = None,
        max_results: Optional[
            "capo_codeartifact.types.list_package_groups_max_results.ListPackageGroupsMaxResults"
        ] = None,
        next_token: Optional[
            "capo_codeartifact.types.pagination_token.PaginationToken"
        ] = None,
        prefix: Optional[
            "capo_codeartifact.types.package_group_pattern_prefix.PackageGroupPatternPrefix"
        ] = None,
    ) -> "Iterator[capo_codeartifact.types.package_group_summary.PackageGroupSummary]":
        _token = next_token
        while True:
            _response = self.list_package_groups(
                domain,
                config_overrides=config_overrides,
                domain_owner=domain_owner,
                max_results=max_results,
                next_token=_token,
                prefix=prefix,
            )
            _page = _resolve_path(_response, ("package_groups",))
            for _item in _page or []:
                yield _item
            _token = _resolve_path(_response, ("next_token",))
            if not _token:
                break

    def list_packages(
        self,
        domain: "capo_codeartifact.types.domain_name.DomainName",
        repository: "capo_codeartifact.types.repository_name.RepositoryName",
        *,
        config_overrides: Optional[codeartifactClientConfig] = None,
        domain_owner: Optional["capo_codeartifact.types.account_id.AccountId"] = None,
        format: Optional["capo_codeartifact.types.package_format.PackageFormat"] = None,
        namespace: Optional[
            "capo_codeartifact.types.package_namespace.PackageNamespace"
        ] = None,
        package_prefix: Optional[
            "capo_codeartifact.types.package_name.PackageName"
        ] = None,
        max_results: Optional[
            "capo_codeartifact.types.list_packages_max_results.ListPackagesMaxResults"
        ] = None,
        next_token: Optional[
            "capo_codeartifact.types.pagination_token.PaginationToken"
        ] = None,
        publish: Optional["capo_codeartifact.types.allow_publish.AllowPublish"] = None,
        upstream: Optional[
            "capo_codeartifact.types.allow_upstream.AllowUpstream"
        ] = None,
    ) -> "capo_codeartifact.types.list_packages_result.ListPackagesResult":
        r"""<p> Returns a list of <a href=\"https://docs.aws.amazon.com/codeartifact/latest/APIReference/API_PackageSummary.html\">PackageSummary</a> objects for packages in a repository that match the request parameters. </p>

        Args:
            domain: <p> The name of the domain that contains the repository that contains the requested packages. </p>
            domain_owner: <p> The 12-digit account number of the Amazon Web Services account that owns the domain. It does not include dashes or spaces. </p>
            repository: <p> The name of the repository that contains the requested packages. </p>
            format: <p>The format used to filter requested packages. Only packages from the provided format will be returned.</p>
            namespace: <p>The namespace prefix used to filter requested packages. Only packages with a namespace that starts with the provided string value are returned. Note that although this option is called <code>--namespace</code> and not <code>--namespace-prefix</code>, it has prefix-matching behavior.</p> <p>Each package format uses namespace as follows:</p> <ul> <li> <p> The namespace of a Maven package version is its <code>groupId</code>. </p> </li> <li> <p> The namespace of an npm or Swift package version is its <code>scope</code>. </p> </li> <li> <p>The namespace of a generic package is its <code>namespace</code>.</p> </li> <li> <p> Python, NuGet, Ruby, and Cargo package versions do not contain a corresponding component, package versions of those formats do not have a namespace. </p> </li> </ul>
            package_prefix: <p> A prefix used to filter requested packages. Only packages with names that start with <code>packagePrefix</code> are returned. </p>
            max_results: <p> The maximum number of results to return per page. </p>
            next_token: <p> The token for the next set of results. Use the value returned in the previous response in the next request to retrieve the next set of results. </p>
            publish: <p>The value of the <code>Publish</code> package origin control restriction used to filter requested packages. Only packages with the provided restriction are returned. For more information, see <a href=\"https://docs.aws.amazon.com/codeartifact/latest/APIReference/API_PackageOriginRestrictions.html\">PackageOriginRestrictions</a>.</p>
            upstream: <p>The value of the <code>Upstream</code> package origin control restriction used to filter requested packages. Only packages with the provided restriction are returned. For more information, see <a href=\"https://docs.aws.amazon.com/codeartifact/latest/APIReference/API_PackageOriginRestrictions.html\">PackageOriginRestrictions</a>.</p>

        Raises:
            capo_codeartifact.errors.access_denied_exception.AccessDeniedException: <p> The operation did not succeed because of an unauthorized access attempt. </p>
            capo_codeartifact.errors.internal_server_exception.InternalServerException: <p> The operation did not succeed because of an error that occurred inside CodeArtifact. </p>
            capo_codeartifact.errors.resource_not_found_exception.ResourceNotFoundException: <p> The operation did not succeed because the resource requested is not found in the service. </p>
            capo_codeartifact.errors.throttling_exception.ThrottlingException: <p> The operation did not succeed because too many requests are sent to the service. </p>
            capo_codeartifact.errors.validation_exception.ValidationException: <p> The operation did not succeed because a parameter in the request was sent with an invalid value. </p>
            capo_codeartifact.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        def _handler(
            req: "OperationRequest[capo_codeartifact.types.list_packages_request.ListPackagesRequest]",
        ) -> OperationResponse[
            "capo_codeartifact.types.list_packages_result.ListPackagesResult"
        ]:
            import capo_codeartifact._operations.code_artifact_control_plane_service.list_packages

            output, http_response = (
                capo_codeartifact._operations.code_artifact_control_plane_service.list_packages.list_packages(
                    req.options, req.input
                )
            )
            return OperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_codeartifact.types.list_packages_request.ListPackagesRequest = {
            "domain": domain,
            "repository": repository,
        }
        if domain_owner is not None:
            input_["domain_owner"] = domain_owner
        if format is not None:
            input_["format"] = format
        if namespace is not None:
            input_["namespace"] = namespace
        if package_prefix is not None:
            input_["package_prefix"] = package_prefix
        if max_results is not None:
            input_["max_results"] = max_results
        if next_token is not None:
            input_["next_token"] = next_token
        if publish is not None:
            input_["publish"] = publish
        if upstream is not None:
            input_["upstream"] = upstream

        response = execute_pipeline(
            OperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        response.response.close()
        return response.output

    def iter_list_packages(
        self,
        domain: "capo_codeartifact.types.domain_name.DomainName",
        repository: "capo_codeartifact.types.repository_name.RepositoryName",
        *,
        config_overrides: Optional[codeartifactClientConfig] = None,
        domain_owner: Optional["capo_codeartifact.types.account_id.AccountId"] = None,
        format: Optional["capo_codeartifact.types.package_format.PackageFormat"] = None,
        namespace: Optional[
            "capo_codeartifact.types.package_namespace.PackageNamespace"
        ] = None,
        package_prefix: Optional[
            "capo_codeartifact.types.package_name.PackageName"
        ] = None,
        max_results: Optional[
            "capo_codeartifact.types.list_packages_max_results.ListPackagesMaxResults"
        ] = None,
        next_token: Optional[
            "capo_codeartifact.types.pagination_token.PaginationToken"
        ] = None,
        publish: Optional["capo_codeartifact.types.allow_publish.AllowPublish"] = None,
        upstream: Optional[
            "capo_codeartifact.types.allow_upstream.AllowUpstream"
        ] = None,
    ) -> "Iterator[capo_codeartifact.types.package_summary.PackageSummary]":
        _token = next_token
        while True:
            _response = self.list_packages(
                domain,
                repository,
                config_overrides=config_overrides,
                domain_owner=domain_owner,
                format=format,
                namespace=namespace,
                package_prefix=package_prefix,
                max_results=max_results,
                next_token=_token,
                publish=publish,
                upstream=upstream,
            )
            _page = _resolve_path(_response, ("packages",))
            for _item in _page or []:
                yield _item
            _token = _resolve_path(_response, ("next_token",))
            if not _token:
                break

    def list_package_version_assets(
        self,
        domain: "capo_codeartifact.types.domain_name.DomainName",
        repository: "capo_codeartifact.types.repository_name.RepositoryName",
        format: "capo_codeartifact.types.package_format.PackageFormat",
        package: "capo_codeartifact.types.package_name.PackageName",
        package_version: "capo_codeartifact.types.package_version.PackageVersion",
        *,
        config_overrides: Optional[codeartifactClientConfig] = None,
        domain_owner: Optional["capo_codeartifact.types.account_id.AccountId"] = None,
        namespace: Optional[
            "capo_codeartifact.types.package_namespace.PackageNamespace"
        ] = None,
        max_results: Optional[
            "capo_codeartifact.types.list_package_version_assets_max_results.ListPackageVersionAssetsMaxResults"
        ] = None,
        next_token: Optional[
            "capo_codeartifact.types.pagination_token.PaginationToken"
        ] = None,
    ) -> "capo_codeartifact.types.list_package_version_assets_result.ListPackageVersionAssetsResult":
        r"""<p> Returns a list of <a href=\"https://docs.aws.amazon.com/codeartifact/latest/APIReference/API_AssetSummary.html\">AssetSummary</a> objects for assets in a package version. </p>

        Args:
            domain: <p> The name of the domain that contains the repository associated with the package version assets. </p>
            domain_owner: <p> The 12-digit account number of the Amazon Web Services account that owns the domain. It does not include dashes or spaces. </p>
            repository: <p> The name of the repository that contains the package that contains the requested package version assets. </p>
            format: <p> The format of the package that contains the requested package version assets. </p>
            namespace: <p>The namespace of the package version that contains the requested package version assets. The package component that specifies its namespace depends on its type. For example:</p> <note> <p>The namespace is required requesting assets from package versions of the following formats:</p> <ul> <li> <p>Maven</p> </li> <li> <p>Swift</p> </li> <li> <p>generic</p> </li> </ul> </note> <ul> <li> <p> The namespace of a Maven package version is its <code>groupId</code>. </p> </li> <li> <p> The namespace of an npm or Swift package version is its <code>scope</code>. </p> </li> <li> <p>The namespace of a generic package is its <code>namespace</code>.</p> </li> <li> <p> Python, NuGet, Ruby, and Cargo package versions do not contain a corresponding component, package versions of those formats do not have a namespace. </p> </li> </ul>
            package: <p> The name of the package that contains the requested package version assets. </p>
            package_version: <p> A string that contains the package version (for example, <code>3.5.2</code>). </p>
            max_results: <p> The maximum number of results to return per page. </p>
            next_token: <p> The token for the next set of results. Use the value returned in the previous response in the next request to retrieve the next set of results. </p>

        Raises:
            capo_codeartifact.errors.access_denied_exception.AccessDeniedException: <p> The operation did not succeed because of an unauthorized access attempt. </p>
            capo_codeartifact.errors.internal_server_exception.InternalServerException: <p> The operation did not succeed because of an error that occurred inside CodeArtifact. </p>
            capo_codeartifact.errors.resource_not_found_exception.ResourceNotFoundException: <p> The operation did not succeed because the resource requested is not found in the service. </p>
            capo_codeartifact.errors.throttling_exception.ThrottlingException: <p> The operation did not succeed because too many requests are sent to the service. </p>
            capo_codeartifact.errors.validation_exception.ValidationException: <p> The operation did not succeed because a parameter in the request was sent with an invalid value. </p>
            capo_codeartifact.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        def _handler(
            req: "OperationRequest[capo_codeartifact.types.list_package_version_assets_request.ListPackageVersionAssetsRequest]",
        ) -> OperationResponse[
            "capo_codeartifact.types.list_package_version_assets_result.ListPackageVersionAssetsResult"
        ]:
            import capo_codeartifact._operations.code_artifact_control_plane_service.list_package_version_assets

            output, http_response = (
                capo_codeartifact._operations.code_artifact_control_plane_service.list_package_version_assets.list_package_version_assets(
                    req.options, req.input
                )
            )
            return OperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_codeartifact.types.list_package_version_assets_request.ListPackageVersionAssetsRequest = {
            "domain": domain,
            "repository": repository,
            "format": format,
            "package": package,
            "package_version": package_version,
        }
        if domain_owner is not None:
            input_["domain_owner"] = domain_owner
        if namespace is not None:
            input_["namespace"] = namespace
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

    def iter_list_package_version_assets(
        self,
        domain: "capo_codeartifact.types.domain_name.DomainName",
        repository: "capo_codeartifact.types.repository_name.RepositoryName",
        format: "capo_codeartifact.types.package_format.PackageFormat",
        package: "capo_codeartifact.types.package_name.PackageName",
        package_version: "capo_codeartifact.types.package_version.PackageVersion",
        *,
        config_overrides: Optional[codeartifactClientConfig] = None,
        domain_owner: Optional["capo_codeartifact.types.account_id.AccountId"] = None,
        namespace: Optional[
            "capo_codeartifact.types.package_namespace.PackageNamespace"
        ] = None,
        max_results: Optional[
            "capo_codeartifact.types.list_package_version_assets_max_results.ListPackageVersionAssetsMaxResults"
        ] = None,
        next_token: Optional[
            "capo_codeartifact.types.pagination_token.PaginationToken"
        ] = None,
    ) -> "Iterator[capo_codeartifact.types.asset_summary.AssetSummary]":
        _token = next_token
        while True:
            _response = self.list_package_version_assets(
                domain,
                repository,
                format,
                package,
                package_version,
                config_overrides=config_overrides,
                domain_owner=domain_owner,
                namespace=namespace,
                max_results=max_results,
                next_token=_token,
            )
            _page = _resolve_path(_response, ("assets",))
            for _item in _page or []:
                yield _item
            _token = _resolve_path(_response, ("next_token",))
            if not _token:
                break

    def list_package_version_dependencies(
        self,
        domain: "capo_codeartifact.types.domain_name.DomainName",
        repository: "capo_codeartifact.types.repository_name.RepositoryName",
        format: "capo_codeartifact.types.package_format.PackageFormat",
        package: "capo_codeartifact.types.package_name.PackageName",
        package_version: "capo_codeartifact.types.package_version.PackageVersion",
        *,
        config_overrides: Optional[codeartifactClientConfig] = None,
        domain_owner: Optional["capo_codeartifact.types.account_id.AccountId"] = None,
        namespace: Optional[
            "capo_codeartifact.types.package_namespace.PackageNamespace"
        ] = None,
        next_token: Optional[
            "capo_codeartifact.types.pagination_token.PaginationToken"
        ] = None,
    ) -> "capo_codeartifact.types.list_package_version_dependencies_result.ListPackageVersionDependenciesResult":
        r"""<p> Returns the direct dependencies for a package version. The dependencies are returned as <a href=\"https://docs.aws.amazon.com/codeartifact/latest/APIReference/API_PackageDependency.html\">PackageDependency</a> objects. CodeArtifact extracts the dependencies for a package version from the metadata file for the package format (for example, the <code>package.json</code> file for npm packages and the <code>pom.xml</code> file for Maven). Any package version dependencies that are not listed in the configuration file are not returned. </p>

        Args:
            domain: <p> The name of the domain that contains the repository that contains the requested package version dependencies. </p>
            domain_owner: <p> The 12-digit account number of the Amazon Web Services account that owns the domain. It does not include dashes or spaces. </p>
            repository: <p> The name of the repository that contains the requested package version. </p>
            format: <p> The format of the package with the requested dependencies. </p>
            namespace: <p>The namespace of the package version with the requested dependencies. The package component that specifies its namespace depends on its type. For example:</p> <note> <p>The namespace is required when listing dependencies from package versions of the following formats:</p> <ul> <li> <p>Maven</p> </li> </ul> </note> <ul> <li> <p> The namespace of a Maven package version is its <code>groupId</code>. </p> </li> <li> <p> The namespace of an npm package version is its <code>scope</code>. </p> </li> <li> <p> Python and NuGet package versions do not contain a corresponding component, package versions of those formats do not have a namespace. </p> </li> </ul>
            package: <p> The name of the package versions' package. </p>
            package_version: <p> A string that contains the package version (for example, <code>3.5.2</code>). </p>
            next_token: <p> The token for the next set of results. Use the value returned in the previous response in the next request to retrieve the next set of results. </p>

        Raises:
            capo_codeartifact.errors.access_denied_exception.AccessDeniedException: <p> The operation did not succeed because of an unauthorized access attempt. </p>
            capo_codeartifact.errors.internal_server_exception.InternalServerException: <p> The operation did not succeed because of an error that occurred inside CodeArtifact. </p>
            capo_codeartifact.errors.resource_not_found_exception.ResourceNotFoundException: <p> The operation did not succeed because the resource requested is not found in the service. </p>
            capo_codeartifact.errors.throttling_exception.ThrottlingException: <p> The operation did not succeed because too many requests are sent to the service. </p>
            capo_codeartifact.errors.validation_exception.ValidationException: <p> The operation did not succeed because a parameter in the request was sent with an invalid value. </p>
            capo_codeartifact.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        def _handler(
            req: "OperationRequest[capo_codeartifact.types.list_package_version_dependencies_request.ListPackageVersionDependenciesRequest]",
        ) -> OperationResponse[
            "capo_codeartifact.types.list_package_version_dependencies_result.ListPackageVersionDependenciesResult"
        ]:
            import capo_codeartifact._operations.code_artifact_control_plane_service.list_package_version_dependencies

            output, http_response = (
                capo_codeartifact._operations.code_artifact_control_plane_service.list_package_version_dependencies.list_package_version_dependencies(
                    req.options, req.input
                )
            )
            return OperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_codeartifact.types.list_package_version_dependencies_request.ListPackageVersionDependenciesRequest = {
            "domain": domain,
            "repository": repository,
            "format": format,
            "package": package,
            "package_version": package_version,
        }
        if domain_owner is not None:
            input_["domain_owner"] = domain_owner
        if namespace is not None:
            input_["namespace"] = namespace
        if next_token is not None:
            input_["next_token"] = next_token

        response = execute_pipeline(
            OperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        response.response.close()
        return response.output

    def list_package_versions(
        self,
        domain: "capo_codeartifact.types.domain_name.DomainName",
        repository: "capo_codeartifact.types.repository_name.RepositoryName",
        format: "capo_codeartifact.types.package_format.PackageFormat",
        package: "capo_codeartifact.types.package_name.PackageName",
        *,
        config_overrides: Optional[codeartifactClientConfig] = None,
        domain_owner: Optional["capo_codeartifact.types.account_id.AccountId"] = None,
        namespace: Optional[
            "capo_codeartifact.types.package_namespace.PackageNamespace"
        ] = None,
        status: Optional[
            "capo_codeartifact.types.package_version_status.PackageVersionStatus"
        ] = None,
        sort_by: Optional[
            "capo_codeartifact.types.package_version_sort_type.PackageVersionSortType"
        ] = None,
        max_results: Optional[
            "capo_codeartifact.types.list_package_versions_max_results.ListPackageVersionsMaxResults"
        ] = None,
        next_token: Optional[
            "capo_codeartifact.types.pagination_token.PaginationToken"
        ] = None,
        origin_type: Optional[
            "capo_codeartifact.types.package_version_origin_type.PackageVersionOriginType"
        ] = None,
    ) -> (
        "capo_codeartifact.types.list_package_versions_result.ListPackageVersionsResult"
    ):
        r"""<p> Returns a list of <a href=\"https://docs.aws.amazon.com/codeartifact/latest/APIReference/API_PackageVersionSummary.html\">PackageVersionSummary</a> objects for package versions in a repository that match the request parameters. Package versions of all statuses will be returned by default when calling <code>list-package-versions</code> with no <code>--status</code> parameter. </p>

        Args:
            domain: <p> The name of the domain that contains the repository that contains the requested package versions. </p>
            domain_owner: <p> The 12-digit account number of the Amazon Web Services account that owns the domain. It does not include dashes or spaces. </p>
            repository: <p> The name of the repository that contains the requested package versions. </p>
            format: <p> The format of the package versions you want to list. </p>
            namespace: <p>The namespace of the package that contains the requested package versions. The package component that specifies its namespace depends on its type. For example:</p> <note> <p>The namespace is required when deleting package versions of the following formats:</p> <ul> <li> <p>Maven</p> </li> <li> <p>Swift</p> </li> <li> <p>generic</p> </li> </ul> </note> <ul> <li> <p> The namespace of a Maven package version is its <code>groupId</code>. </p> </li> <li> <p> The namespace of an npm or Swift package version is its <code>scope</code>. </p> </li> <li> <p>The namespace of a generic package is its <code>namespace</code>.</p> </li> <li> <p> Python, NuGet, Ruby, and Cargo package versions do not contain a corresponding component, package versions of those formats do not have a namespace. </p> </li> </ul>
            package: <p> The name of the package for which you want to request package versions. </p>
            status: <p> A string that filters the requested package versions by status. </p>
            sort_by: <p> How to sort the requested list of package versions. </p>
            max_results: <p> The maximum number of results to return per page. </p>
            next_token: <p> The token for the next set of results. Use the value returned in the previous response in the next request to retrieve the next set of results. </p>
            origin_type: <p>The <code>originType</code> used to filter package versions. Only package versions with the provided <code>originType</code> will be returned.</p>

        Raises:
            capo_codeartifact.errors.access_denied_exception.AccessDeniedException: <p> The operation did not succeed because of an unauthorized access attempt. </p>
            capo_codeartifact.errors.internal_server_exception.InternalServerException: <p> The operation did not succeed because of an error that occurred inside CodeArtifact. </p>
            capo_codeartifact.errors.resource_not_found_exception.ResourceNotFoundException: <p> The operation did not succeed because the resource requested is not found in the service. </p>
            capo_codeartifact.errors.throttling_exception.ThrottlingException: <p> The operation did not succeed because too many requests are sent to the service. </p>
            capo_codeartifact.errors.validation_exception.ValidationException: <p> The operation did not succeed because a parameter in the request was sent with an invalid value. </p>
            capo_codeartifact.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        def _handler(
            req: "OperationRequest[capo_codeartifact.types.list_package_versions_request.ListPackageVersionsRequest]",
        ) -> OperationResponse[
            "capo_codeartifact.types.list_package_versions_result.ListPackageVersionsResult"
        ]:
            import capo_codeartifact._operations.code_artifact_control_plane_service.list_package_versions

            output, http_response = (
                capo_codeartifact._operations.code_artifact_control_plane_service.list_package_versions.list_package_versions(
                    req.options, req.input
                )
            )
            return OperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_codeartifact.types.list_package_versions_request.ListPackageVersionsRequest = {
            "domain": domain,
            "repository": repository,
            "format": format,
            "package": package,
        }
        if domain_owner is not None:
            input_["domain_owner"] = domain_owner
        if namespace is not None:
            input_["namespace"] = namespace
        if status is not None:
            input_["status"] = status
        if sort_by is not None:
            input_["sort_by"] = sort_by
        if max_results is not None:
            input_["max_results"] = max_results
        if next_token is not None:
            input_["next_token"] = next_token
        if origin_type is not None:
            input_["origin_type"] = origin_type

        response = execute_pipeline(
            OperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        response.response.close()
        return response.output

    def iter_list_package_versions(
        self,
        domain: "capo_codeartifact.types.domain_name.DomainName",
        repository: "capo_codeartifact.types.repository_name.RepositoryName",
        format: "capo_codeartifact.types.package_format.PackageFormat",
        package: "capo_codeartifact.types.package_name.PackageName",
        *,
        config_overrides: Optional[codeartifactClientConfig] = None,
        domain_owner: Optional["capo_codeartifact.types.account_id.AccountId"] = None,
        namespace: Optional[
            "capo_codeartifact.types.package_namespace.PackageNamespace"
        ] = None,
        status: Optional[
            "capo_codeartifact.types.package_version_status.PackageVersionStatus"
        ] = None,
        sort_by: Optional[
            "capo_codeartifact.types.package_version_sort_type.PackageVersionSortType"
        ] = None,
        max_results: Optional[
            "capo_codeartifact.types.list_package_versions_max_results.ListPackageVersionsMaxResults"
        ] = None,
        next_token: Optional[
            "capo_codeartifact.types.pagination_token.PaginationToken"
        ] = None,
        origin_type: Optional[
            "capo_codeartifact.types.package_version_origin_type.PackageVersionOriginType"
        ] = None,
    ) -> "Iterator[capo_codeartifact.types.package_version_summary.PackageVersionSummary]":
        _token = next_token
        while True:
            _response = self.list_package_versions(
                domain,
                repository,
                format,
                package,
                config_overrides=config_overrides,
                domain_owner=domain_owner,
                namespace=namespace,
                status=status,
                sort_by=sort_by,
                max_results=max_results,
                next_token=_token,
                origin_type=origin_type,
            )
            _page = _resolve_path(_response, ("versions",))
            for _item in _page or []:
                yield _item
            _token = _resolve_path(_response, ("next_token",))
            if not _token:
                break

    def list_repositories(
        self,
        *,
        config_overrides: Optional[codeartifactClientConfig] = None,
        repository_prefix: Optional[
            "capo_codeartifact.types.repository_name.RepositoryName"
        ] = None,
        max_results: Optional[
            "capo_codeartifact.types.list_repositories_max_results.ListRepositoriesMaxResults"
        ] = None,
        next_token: Optional[
            "capo_codeartifact.types.pagination_token.PaginationToken"
        ] = None,
    ) -> "capo_codeartifact.types.list_repositories_result.ListRepositoriesResult":
        r"""<p> Returns a list of <a href=\"https://docs.aws.amazon.com/codeartifact/latest/APIReference/API_RepositorySummary.html\">RepositorySummary</a> objects. Each <code>RepositorySummary</code> contains information about a repository in the specified Amazon Web Services account and that matches the input parameters. </p>

        Args:
            repository_prefix: <p> A prefix used to filter returned repositories. Only repositories with names that start with <code>repositoryPrefix</code> are returned.</p>
            max_results: <p> The maximum number of results to return per page. </p>
            next_token: <p> The token for the next set of results. Use the value returned in the previous response in the next request to retrieve the next set of results. </p>

        Raises:
            capo_codeartifact.errors.access_denied_exception.AccessDeniedException: <p> The operation did not succeed because of an unauthorized access attempt. </p>
            capo_codeartifact.errors.internal_server_exception.InternalServerException: <p> The operation did not succeed because of an error that occurred inside CodeArtifact. </p>
            capo_codeartifact.errors.throttling_exception.ThrottlingException: <p> The operation did not succeed because too many requests are sent to the service. </p>
            capo_codeartifact.errors.validation_exception.ValidationException: <p> The operation did not succeed because a parameter in the request was sent with an invalid value. </p>
            capo_codeartifact.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        def _handler(
            req: "OperationRequest[capo_codeartifact.types.list_repositories_request.ListRepositoriesRequest]",
        ) -> OperationResponse[
            "capo_codeartifact.types.list_repositories_result.ListRepositoriesResult"
        ]:
            import capo_codeartifact._operations.code_artifact_control_plane_service.list_repositories

            output, http_response = (
                capo_codeartifact._operations.code_artifact_control_plane_service.list_repositories.list_repositories(
                    req.options, req.input
                )
            )
            return OperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_codeartifact.types.list_repositories_request.ListRepositoriesRequest = {}
        if repository_prefix is not None:
            input_["repository_prefix"] = repository_prefix
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

    def iter_list_repositories(
        self,
        *,
        config_overrides: Optional[codeartifactClientConfig] = None,
        repository_prefix: Optional[
            "capo_codeartifact.types.repository_name.RepositoryName"
        ] = None,
        max_results: Optional[
            "capo_codeartifact.types.list_repositories_max_results.ListRepositoriesMaxResults"
        ] = None,
        next_token: Optional[
            "capo_codeartifact.types.pagination_token.PaginationToken"
        ] = None,
    ) -> "Iterator[capo_codeartifact.types.repository_summary.RepositorySummary]":
        _token = next_token
        while True:
            _response = self.list_repositories(
                config_overrides=config_overrides,
                repository_prefix=repository_prefix,
                max_results=max_results,
                next_token=_token,
            )
            _page = _resolve_path(_response, ("repositories",))
            for _item in _page or []:
                yield _item
            _token = _resolve_path(_response, ("next_token",))
            if not _token:
                break

    def list_repositories_in_domain(
        self,
        domain: "capo_codeartifact.types.domain_name.DomainName",
        *,
        config_overrides: Optional[codeartifactClientConfig] = None,
        domain_owner: Optional["capo_codeartifact.types.account_id.AccountId"] = None,
        administrator_account: Optional[
            "capo_codeartifact.types.account_id.AccountId"
        ] = None,
        repository_prefix: Optional[
            "capo_codeartifact.types.repository_name.RepositoryName"
        ] = None,
        max_results: Optional[
            "capo_codeartifact.types.list_repositories_in_domain_max_results.ListRepositoriesInDomainMaxResults"
        ] = None,
        next_token: Optional[
            "capo_codeartifact.types.pagination_token.PaginationToken"
        ] = None,
    ) -> "capo_codeartifact.types.list_repositories_in_domain_result.ListRepositoriesInDomainResult":
        r"""<p> Returns a list of <a href=\"https://docs.aws.amazon.com/codeartifact/latest/APIReference/API_RepositorySummary.html\">RepositorySummary</a> objects. Each <code>RepositorySummary</code> contains information about a repository in the specified domain and that matches the input parameters. </p>

        Args:
            domain: <p> The name of the domain that contains the returned list of repositories. </p>
            domain_owner: <p> The 12-digit account number of the Amazon Web Services account that owns the domain. It does not include dashes or spaces. </p>
            administrator_account: <p> Filter the list of repositories to only include those that are managed by the Amazon Web Services account ID. </p>
            repository_prefix: <p> A prefix used to filter returned repositories. Only repositories with names that start with <code>repositoryPrefix</code> are returned. </p>
            max_results: <p> The maximum number of results to return per page. </p>
            next_token: <p> The token for the next set of results. Use the value returned in the previous response in the next request to retrieve the next set of results. </p>

        Raises:
            capo_codeartifact.errors.access_denied_exception.AccessDeniedException: <p> The operation did not succeed because of an unauthorized access attempt. </p>
            capo_codeartifact.errors.internal_server_exception.InternalServerException: <p> The operation did not succeed because of an error that occurred inside CodeArtifact. </p>
            capo_codeartifact.errors.resource_not_found_exception.ResourceNotFoundException: <p> The operation did not succeed because the resource requested is not found in the service. </p>
            capo_codeartifact.errors.throttling_exception.ThrottlingException: <p> The operation did not succeed because too many requests are sent to the service. </p>
            capo_codeartifact.errors.validation_exception.ValidationException: <p> The operation did not succeed because a parameter in the request was sent with an invalid value. </p>
            capo_codeartifact.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        def _handler(
            req: "OperationRequest[capo_codeartifact.types.list_repositories_in_domain_request.ListRepositoriesInDomainRequest]",
        ) -> OperationResponse[
            "capo_codeartifact.types.list_repositories_in_domain_result.ListRepositoriesInDomainResult"
        ]:
            import capo_codeartifact._operations.code_artifact_control_plane_service.list_repositories_in_domain

            output, http_response = (
                capo_codeartifact._operations.code_artifact_control_plane_service.list_repositories_in_domain.list_repositories_in_domain(
                    req.options, req.input
                )
            )
            return OperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_codeartifact.types.list_repositories_in_domain_request.ListRepositoriesInDomainRequest = {
            "domain": domain
        }
        if domain_owner is not None:
            input_["domain_owner"] = domain_owner
        if administrator_account is not None:
            input_["administrator_account"] = administrator_account
        if repository_prefix is not None:
            input_["repository_prefix"] = repository_prefix
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

    def iter_list_repositories_in_domain(
        self,
        domain: "capo_codeartifact.types.domain_name.DomainName",
        *,
        config_overrides: Optional[codeartifactClientConfig] = None,
        domain_owner: Optional["capo_codeartifact.types.account_id.AccountId"] = None,
        administrator_account: Optional[
            "capo_codeartifact.types.account_id.AccountId"
        ] = None,
        repository_prefix: Optional[
            "capo_codeartifact.types.repository_name.RepositoryName"
        ] = None,
        max_results: Optional[
            "capo_codeartifact.types.list_repositories_in_domain_max_results.ListRepositoriesInDomainMaxResults"
        ] = None,
        next_token: Optional[
            "capo_codeartifact.types.pagination_token.PaginationToken"
        ] = None,
    ) -> "Iterator[capo_codeartifact.types.repository_summary.RepositorySummary]":
        _token = next_token
        while True:
            _response = self.list_repositories_in_domain(
                domain,
                config_overrides=config_overrides,
                domain_owner=domain_owner,
                administrator_account=administrator_account,
                repository_prefix=repository_prefix,
                max_results=max_results,
                next_token=_token,
            )
            _page = _resolve_path(_response, ("repositories",))
            for _item in _page or []:
                yield _item
            _token = _resolve_path(_response, ("next_token",))
            if not _token:
                break

    def list_sub_package_groups(
        self,
        domain: "capo_codeartifact.types.domain_name.DomainName",
        package_group: "capo_codeartifact.types.package_group_pattern.PackageGroupPattern",
        *,
        config_overrides: Optional[codeartifactClientConfig] = None,
        domain_owner: Optional["capo_codeartifact.types.account_id.AccountId"] = None,
        max_results: Optional[
            "capo_codeartifact.types.list_package_groups_max_results.ListPackageGroupsMaxResults"
        ] = None,
        next_token: Optional[
            "capo_codeartifact.types.pagination_token.PaginationToken"
        ] = None,
    ) -> "capo_codeartifact.types.list_sub_package_groups_result.ListSubPackageGroupsResult":
        r"""<p>Returns a list of direct children of the specified package group.</p> <p>For information package group hierarchy, see <a href=\"https://docs.aws.amazon.com/codeartifact/latest/ug/package-group-definition-syntax-matching-behavior.html\">Package group definition syntax and matching behavior</a> in the <i>CodeArtifact User Guide</i>.</p>

        Args:
            domain: <p> The name of the domain which contains the package group from which to list sub package groups. </p>
            domain_owner: <p> The 12-digit account number of the Amazon Web Services account that owns the domain. It does not include dashes or spaces. </p>
            package_group: <p> The pattern of the package group from which to list sub package groups. </p>
            max_results: <p> The maximum number of results to return per page. </p>
            next_token: <p> The token for the next set of results. Use the value returned in the previous response in the next request to retrieve the next set of results. </p>

        Raises:
            capo_codeartifact.errors.access_denied_exception.AccessDeniedException: <p> The operation did not succeed because of an unauthorized access attempt. </p>
            capo_codeartifact.errors.internal_server_exception.InternalServerException: <p> The operation did not succeed because of an error that occurred inside CodeArtifact. </p>
            capo_codeartifact.errors.resource_not_found_exception.ResourceNotFoundException: <p> The operation did not succeed because the resource requested is not found in the service. </p>
            capo_codeartifact.errors.throttling_exception.ThrottlingException: <p> The operation did not succeed because too many requests are sent to the service. </p>
            capo_codeartifact.errors.validation_exception.ValidationException: <p> The operation did not succeed because a parameter in the request was sent with an invalid value. </p>
            capo_codeartifact.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        def _handler(
            req: "OperationRequest[capo_codeartifact.types.list_sub_package_groups_request.ListSubPackageGroupsRequest]",
        ) -> OperationResponse[
            "capo_codeartifact.types.list_sub_package_groups_result.ListSubPackageGroupsResult"
        ]:
            import capo_codeartifact._operations.code_artifact_control_plane_service.list_sub_package_groups

            output, http_response = (
                capo_codeartifact._operations.code_artifact_control_plane_service.list_sub_package_groups.list_sub_package_groups(
                    req.options, req.input
                )
            )
            return OperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_codeartifact.types.list_sub_package_groups_request.ListSubPackageGroupsRequest = {
            "domain": domain,
            "package_group": package_group,
        }
        if domain_owner is not None:
            input_["domain_owner"] = domain_owner
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

    def iter_list_sub_package_groups(
        self,
        domain: "capo_codeartifact.types.domain_name.DomainName",
        package_group: "capo_codeartifact.types.package_group_pattern.PackageGroupPattern",
        *,
        config_overrides: Optional[codeartifactClientConfig] = None,
        domain_owner: Optional["capo_codeartifact.types.account_id.AccountId"] = None,
        max_results: Optional[
            "capo_codeartifact.types.list_package_groups_max_results.ListPackageGroupsMaxResults"
        ] = None,
        next_token: Optional[
            "capo_codeartifact.types.pagination_token.PaginationToken"
        ] = None,
    ) -> "Iterator[capo_codeartifact.types.package_group_summary.PackageGroupSummary]":
        _token = next_token
        while True:
            _response = self.list_sub_package_groups(
                domain,
                package_group,
                config_overrides=config_overrides,
                domain_owner=domain_owner,
                max_results=max_results,
                next_token=_token,
            )
            _page = _resolve_path(_response, ("package_groups",))
            for _item in _page or []:
                yield _item
            _token = _resolve_path(_response, ("next_token",))
            if not _token:
                break

    def list_tags_for_resource(
        self,
        resource_arn: "capo_codeartifact.types.arn.Arn",
        *,
        config_overrides: Optional[codeartifactClientConfig] = None,
    ) -> "capo_codeartifact.types.list_tags_for_resource_result.ListTagsForResourceResult":
        """<p>Gets information about Amazon Web Services tags for a specified Amazon Resource Name (ARN) in CodeArtifact.</p>

        Args:
            resource_arn: <p>The Amazon Resource Name (ARN) of the resource to get tags for.</p>

        Raises:
            capo_codeartifact.errors.access_denied_exception.AccessDeniedException: <p> The operation did not succeed because of an unauthorized access attempt. </p>
            capo_codeartifact.errors.resource_not_found_exception.ResourceNotFoundException: <p> The operation did not succeed because the resource requested is not found in the service. </p>
            capo_codeartifact.errors.throttling_exception.ThrottlingException: <p> The operation did not succeed because too many requests are sent to the service. </p>
            capo_codeartifact.errors.validation_exception.ValidationException: <p> The operation did not succeed because a parameter in the request was sent with an invalid value. </p>
            capo_codeartifact.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        def _handler(
            req: "OperationRequest[capo_codeartifact.types.list_tags_for_resource_request.ListTagsForResourceRequest]",
        ) -> OperationResponse[
            "capo_codeartifact.types.list_tags_for_resource_result.ListTagsForResourceResult"
        ]:
            import capo_codeartifact._operations.code_artifact_control_plane_service.list_tags_for_resource

            output, http_response = (
                capo_codeartifact._operations.code_artifact_control_plane_service.list_tags_for_resource.list_tags_for_resource(
                    req.options, req.input
                )
            )
            return OperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_codeartifact.types.list_tags_for_resource_request.ListTagsForResourceRequest = {
            "resource_arn": resource_arn
        }

        response = execute_pipeline(
            OperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        response.response.close()
        return response.output

    def publish_package_version(
        self,
        domain: "capo_codeartifact.types.domain_name.DomainName",
        repository: "capo_codeartifact.types.repository_name.RepositoryName",
        format: "capo_codeartifact.types.package_format.PackageFormat",
        package: "capo_codeartifact.types.package_name.PackageName",
        package_version: "capo_codeartifact.types.package_version.PackageVersion",
        asset_content: Body[Iterator[bytes]] | Iterator[bytes] | bytes,
        asset_name: "capo_codeartifact.types.asset_name.AssetName",
        asset_sha256: "capo_codeartifact.types.sha256.SHA256",
        *,
        config_overrides: Optional[codeartifactClientConfig] = None,
        domain_owner: Optional["capo_codeartifact.types.account_id.AccountId"] = None,
        namespace: Optional[
            "capo_codeartifact.types.package_namespace.PackageNamespace"
        ] = None,
        unfinished: Optional[
            "capo_codeartifact.types.boolean_optional.BooleanOptional"
        ] = None,
    ) -> "capo_codeartifact.types.publish_package_version_result.PublishPackageVersionResult":
        r"""<p>Creates a new package version containing one or more assets (or files).</p> <p>The <code>unfinished</code> flag can be used to keep the package version in the <code>Unfinished</code> state until all of its assets have been uploaded (see <a href=\"https://docs.aws.amazon.com/codeartifact/latest/ug/packages-overview.html#package-version-status.html#package-version-status\">Package version status</a> in the <i>CodeArtifact user guide</i>). To set the package version’s status to <code>Published</code>, omit the <code>unfinished</code> flag when uploading the final asset, or set the status using <a href=\"https://docs.aws.amazon.com/codeartifact/latest/APIReference/API_UpdatePackageVersionsStatus.html\">UpdatePackageVersionStatus</a>. Once a package version’s status is set to <code>Published</code>, it cannot change back to <code>Unfinished</code>.</p> <note> <p>Only generic packages can be published using this API. For more information, see <a href=\"https://docs.aws.amazon.com/codeartifact/latest/ug/using-generic.html\">Using generic packages</a> in the <i>CodeArtifact User Guide</i>.</p> </note>

        Args:
            domain: <p>The name of the domain that contains the repository that contains the package version to publish.</p>
            domain_owner: <p>The 12-digit account number of the AWS account that owns the domain. It does not include dashes or spaces.</p>
            repository: <p>The name of the repository that the package version will be published to.</p>
            format: <p>A format that specifies the type of the package version with the requested asset file.</p> <p>The only supported value is <code>generic</code>.</p>
            namespace: <p>The namespace of the package version to publish.</p>
            package: <p>The name of the package version to publish.</p>
            package_version: <p>The package version to publish (for example, <code>3.5.2</code>).</p>
            asset_content: <p>The content of the asset to publish.</p>
            asset_name: <p>The name of the asset to publish. Asset names can include Unicode letters and numbers, and the following special characters: <code>~ ! @ ^ & ( ) - ` _ + [ ] { } ; , . `</code> </p>
            asset_sha256: <p>The SHA256 hash of the <code>assetContent</code> to publish. This value must be calculated by the caller and provided with the request (see <a href=\"https://docs.aws.amazon.com/codeartifact/latest/ug/using-generic.html#publishing-generic-packages\">Publishing a generic package</a> in the <i>CodeArtifact User Guide</i>).</p> <p>This value is used as an integrity check to verify that the <code>assetContent</code> has not changed after it was originally sent.</p>
            unfinished: <p>Specifies whether the package version should remain in the <code>unfinished</code> state. If omitted, the package version status will be set to <code>Published</code> (see <a href=\"https://docs.aws.amazon.com/codeartifact/latest/ug/packages-overview.html#package-version-status\">Package version status</a> in the <i>CodeArtifact User Guide</i>).</p> <p>Valid values: <code>unfinished</code> </p>

        Raises:
            capo_codeartifact.errors.access_denied_exception.AccessDeniedException: <p> The operation did not succeed because of an unauthorized access attempt. </p>
            capo_codeartifact.errors.conflict_exception.ConflictException: <p> The operation did not succeed because prerequisites are not met. </p>
            capo_codeartifact.errors.internal_server_exception.InternalServerException: <p> The operation did not succeed because of an error that occurred inside CodeArtifact. </p>
            capo_codeartifact.errors.resource_not_found_exception.ResourceNotFoundException: <p> The operation did not succeed because the resource requested is not found in the service. </p>
            capo_codeartifact.errors.service_quota_exceeded_exception.ServiceQuotaExceededException: <p> The operation did not succeed because it would have exceeded a service limit for your account. </p>
            capo_codeartifact.errors.throttling_exception.ThrottlingException: <p> The operation did not succeed because too many requests are sent to the service. </p>
            capo_codeartifact.errors.validation_exception.ValidationException: <p> The operation did not succeed because a parameter in the request was sent with an invalid value. </p>
            capo_codeartifact.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        def _handler(
            req: "OperationRequest[capo_codeartifact.types.publish_package_version_request.PublishPackageVersionRequest]",
        ) -> OperationResponse[
            "capo_codeartifact.types.publish_package_version_result.PublishPackageVersionResult"
        ]:
            import capo_codeartifact._operations.code_artifact_control_plane_service.publish_package_version

            output, http_response = (
                capo_codeartifact._operations.code_artifact_control_plane_service.publish_package_version.publish_package_version(
                    req.options, req.input
                )
            )
            return OperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_codeartifact.types.publish_package_version_request.PublishPackageVersionRequest = {
            "domain": domain,
            "repository": repository,
            "format": format,
            "package": package,
            "package_version": package_version,
            "asset_content": ensure_sync_iterator(asset_content),
            "asset_name": asset_name,
            "asset_sha256": asset_sha256,
        }
        if domain_owner is not None:
            input_["domain_owner"] = domain_owner
        if namespace is not None:
            input_["namespace"] = namespace
        if unfinished is not None:
            input_["unfinished"] = unfinished

        with closing_bodies(input_):
            response = execute_pipeline(
                OperationRequest(input=input_, options=options_),
                handler=_handler,
                interceptors=list(interceptors_),
            )
            response.response.close()
            return response.output

    def put_domain_permissions_policy(
        self,
        domain: "capo_codeartifact.types.domain_name.DomainName",
        policy_document: "capo_codeartifact.types.policy_document.PolicyDocument",
        *,
        config_overrides: Optional[codeartifactClientConfig] = None,
        domain_owner: Optional["capo_codeartifact.types.account_id.AccountId"] = None,
        policy_revision: Optional[
            "capo_codeartifact.types.policy_revision.PolicyRevision"
        ] = None,
    ) -> "capo_codeartifact.types.put_domain_permissions_policy_result.PutDomainPermissionsPolicyResult":
        """<p> Sets a resource policy on a domain that specifies permissions to access it. </p> <p> When you call <code>PutDomainPermissionsPolicy</code>, the resource policy on the domain is ignored when evaluting permissions. This ensures that the owner of a domain cannot lock themselves out of the domain, which would prevent them from being able to update the resource policy. </p>

        Args:
            domain: <p> The name of the domain on which to set the resource policy. </p>
            domain_owner: <p> The 12-digit account number of the Amazon Web Services account that owns the domain. It does not include dashes or spaces. </p>
            policy_revision: <p> The current revision of the resource policy to be set. This revision is used for optimistic locking, which prevents others from overwriting your changes to the domain's resource policy. </p>
            policy_document: <p> A valid displayable JSON Aspen policy string to be set as the access control resource policy on the provided domain. </p>

        Raises:
            capo_codeartifact.errors.access_denied_exception.AccessDeniedException: <p> The operation did not succeed because of an unauthorized access attempt. </p>
            capo_codeartifact.errors.conflict_exception.ConflictException: <p> The operation did not succeed because prerequisites are not met. </p>
            capo_codeartifact.errors.internal_server_exception.InternalServerException: <p> The operation did not succeed because of an error that occurred inside CodeArtifact. </p>
            capo_codeartifact.errors.resource_not_found_exception.ResourceNotFoundException: <p> The operation did not succeed because the resource requested is not found in the service. </p>
            capo_codeartifact.errors.service_quota_exceeded_exception.ServiceQuotaExceededException: <p> The operation did not succeed because it would have exceeded a service limit for your account. </p>
            capo_codeartifact.errors.throttling_exception.ThrottlingException: <p> The operation did not succeed because too many requests are sent to the service. </p>
            capo_codeartifact.errors.validation_exception.ValidationException: <p> The operation did not succeed because a parameter in the request was sent with an invalid value. </p>
            capo_codeartifact.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        def _handler(
            req: "OperationRequest[capo_codeartifact.types.put_domain_permissions_policy_request.PutDomainPermissionsPolicyRequest]",
        ) -> OperationResponse[
            "capo_codeartifact.types.put_domain_permissions_policy_result.PutDomainPermissionsPolicyResult"
        ]:
            import capo_codeartifact._operations.code_artifact_control_plane_service.put_domain_permissions_policy

            output, http_response = (
                capo_codeartifact._operations.code_artifact_control_plane_service.put_domain_permissions_policy.put_domain_permissions_policy(
                    req.options, req.input
                )
            )
            return OperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_codeartifact.types.put_domain_permissions_policy_request.PutDomainPermissionsPolicyRequest = {
            "domain": domain,
            "policy_document": policy_document,
        }
        if domain_owner is not None:
            input_["domain_owner"] = domain_owner
        if policy_revision is not None:
            input_["policy_revision"] = policy_revision

        response = execute_pipeline(
            OperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        response.response.close()
        return response.output

    def put_package_origin_configuration(
        self,
        domain: "capo_codeartifact.types.domain_name.DomainName",
        repository: "capo_codeartifact.types.repository_name.RepositoryName",
        format: "capo_codeartifact.types.package_format.PackageFormat",
        package: "capo_codeartifact.types.package_name.PackageName",
        restrictions: "capo_codeartifact.types.package_origin_restrictions.PackageOriginRestrictions",
        *,
        config_overrides: Optional[codeartifactClientConfig] = None,
        domain_owner: Optional["capo_codeartifact.types.account_id.AccountId"] = None,
        namespace: Optional[
            "capo_codeartifact.types.package_namespace.PackageNamespace"
        ] = None,
    ) -> "capo_codeartifact.types.put_package_origin_configuration_result.PutPackageOriginConfigurationResult":
        r"""<p>Sets the package origin configuration for a package.</p> <p>The package origin configuration determines how new versions of a package can be added to a repository. You can allow or block direct publishing of new package versions, or ingestion and retaining of new package versions from an external connection or upstream source. For more information about package origin controls and configuration, see <a href=\"https://docs.aws.amazon.com/codeartifact/latest/ug/package-origin-controls.html\">Editing package origin controls</a> in the <i>CodeArtifact User Guide</i>.</p> <p> <code>PutPackageOriginConfiguration</code> can be called on a package that doesn't yet exist in the repository. When called on a package that does not exist, a package is created in the repository with no versions and the requested restrictions are set on the package. This can be used to preemptively block ingesting or retaining any versions from external connections or upstream repositories, or to block publishing any versions of the package into the repository before connecting any package managers or publishers to the repository.</p>

        Args:
            domain: <p>The name of the domain that contains the repository that contains the package.</p>
            domain_owner: <p> The 12-digit account number of the Amazon Web Services account that owns the domain. It does not include dashes or spaces. </p>
            repository: <p>The name of the repository that contains the package.</p>
            format: <p>A format that specifies the type of the package to be updated.</p>
            namespace: <p>The namespace of the package to be updated. The package component that specifies its namespace depends on its type. For example:</p> <ul> <li> <p> The namespace of a Maven package version is its <code>groupId</code>. </p> </li> <li> <p> The namespace of an npm or Swift package version is its <code>scope</code>. </p> </li> <li> <p>The namespace of a generic package is its <code>namespace</code>.</p> </li> <li> <p> Python, NuGet, Ruby, and Cargo package versions do not contain a corresponding component, package versions of those formats do not have a namespace. </p> </li> </ul>
            package: <p>The name of the package to be updated.</p>
            restrictions: <p>A <a href=\"https://docs.aws.amazon.com/codeartifact/latest/APIReference/API_PackageOriginRestrictions.html\">PackageOriginRestrictions</a> object that contains information about the <code>upstream</code> and <code>publish</code> package origin restrictions. The <code>upstream</code> restriction determines if new package versions can be ingested or retained from external connections or upstream repositories. The <code>publish</code> restriction determines if new package versions can be published directly to the repository.</p> <p>You must include both the desired <code>upstream</code> and <code>publish</code> restrictions.</p>

        Raises:
            capo_codeartifact.errors.access_denied_exception.AccessDeniedException: <p> The operation did not succeed because of an unauthorized access attempt. </p>
            capo_codeartifact.errors.internal_server_exception.InternalServerException: <p> The operation did not succeed because of an error that occurred inside CodeArtifact. </p>
            capo_codeartifact.errors.resource_not_found_exception.ResourceNotFoundException: <p> The operation did not succeed because the resource requested is not found in the service. </p>
            capo_codeartifact.errors.throttling_exception.ThrottlingException: <p> The operation did not succeed because too many requests are sent to the service. </p>
            capo_codeartifact.errors.validation_exception.ValidationException: <p> The operation did not succeed because a parameter in the request was sent with an invalid value. </p>
            capo_codeartifact.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        def _handler(
            req: "OperationRequest[capo_codeartifact.types.put_package_origin_configuration_request.PutPackageOriginConfigurationRequest]",
        ) -> OperationResponse[
            "capo_codeartifact.types.put_package_origin_configuration_result.PutPackageOriginConfigurationResult"
        ]:
            import capo_codeartifact._operations.code_artifact_control_plane_service.put_package_origin_configuration

            output, http_response = (
                capo_codeartifact._operations.code_artifact_control_plane_service.put_package_origin_configuration.put_package_origin_configuration(
                    req.options, req.input
                )
            )
            return OperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_codeartifact.types.put_package_origin_configuration_request.PutPackageOriginConfigurationRequest = {
            "domain": domain,
            "repository": repository,
            "format": format,
            "package": package,
            "restrictions": restrictions,
        }
        if domain_owner is not None:
            input_["domain_owner"] = domain_owner
        if namespace is not None:
            input_["namespace"] = namespace

        response = execute_pipeline(
            OperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        response.response.close()
        return response.output

    def put_repository_permissions_policy(
        self,
        domain: "capo_codeartifact.types.domain_name.DomainName",
        repository: "capo_codeartifact.types.repository_name.RepositoryName",
        policy_document: "capo_codeartifact.types.policy_document.PolicyDocument",
        *,
        config_overrides: Optional[codeartifactClientConfig] = None,
        domain_owner: Optional["capo_codeartifact.types.account_id.AccountId"] = None,
        policy_revision: Optional[
            "capo_codeartifact.types.policy_revision.PolicyRevision"
        ] = None,
    ) -> "capo_codeartifact.types.put_repository_permissions_policy_result.PutRepositoryPermissionsPolicyResult":
        """<p> Sets the resource policy on a repository that specifies permissions to access it. </p> <p> When you call <code>PutRepositoryPermissionsPolicy</code>, the resource policy on the repository is ignored when evaluting permissions. This ensures that the owner of a repository cannot lock themselves out of the repository, which would prevent them from being able to update the resource policy. </p>

        Args:
            domain: <p> The name of the domain containing the repository to set the resource policy on. </p>
            domain_owner: <p> The 12-digit account number of the Amazon Web Services account that owns the domain. It does not include dashes or spaces. </p>
            repository: <p> The name of the repository to set the resource policy on. </p>
            policy_revision: <p> Sets the revision of the resource policy that specifies permissions to access the repository. This revision is used for optimistic locking, which prevents others from overwriting your changes to the repository's resource policy. </p>
            policy_document: <p> A valid displayable JSON Aspen policy string to be set as the access control resource policy on the provided repository. </p>

        Raises:
            capo_codeartifact.errors.access_denied_exception.AccessDeniedException: <p> The operation did not succeed because of an unauthorized access attempt. </p>
            capo_codeartifact.errors.conflict_exception.ConflictException: <p> The operation did not succeed because prerequisites are not met. </p>
            capo_codeartifact.errors.internal_server_exception.InternalServerException: <p> The operation did not succeed because of an error that occurred inside CodeArtifact. </p>
            capo_codeartifact.errors.resource_not_found_exception.ResourceNotFoundException: <p> The operation did not succeed because the resource requested is not found in the service. </p>
            capo_codeartifact.errors.service_quota_exceeded_exception.ServiceQuotaExceededException: <p> The operation did not succeed because it would have exceeded a service limit for your account. </p>
            capo_codeartifact.errors.throttling_exception.ThrottlingException: <p> The operation did not succeed because too many requests are sent to the service. </p>
            capo_codeartifact.errors.validation_exception.ValidationException: <p> The operation did not succeed because a parameter in the request was sent with an invalid value. </p>
            capo_codeartifact.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        def _handler(
            req: "OperationRequest[capo_codeartifact.types.put_repository_permissions_policy_request.PutRepositoryPermissionsPolicyRequest]",
        ) -> OperationResponse[
            "capo_codeartifact.types.put_repository_permissions_policy_result.PutRepositoryPermissionsPolicyResult"
        ]:
            import capo_codeartifact._operations.code_artifact_control_plane_service.put_repository_permissions_policy

            output, http_response = (
                capo_codeartifact._operations.code_artifact_control_plane_service.put_repository_permissions_policy.put_repository_permissions_policy(
                    req.options, req.input
                )
            )
            return OperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_codeartifact.types.put_repository_permissions_policy_request.PutRepositoryPermissionsPolicyRequest = {
            "domain": domain,
            "repository": repository,
            "policy_document": policy_document,
        }
        if domain_owner is not None:
            input_["domain_owner"] = domain_owner
        if policy_revision is not None:
            input_["policy_revision"] = policy_revision

        response = execute_pipeline(
            OperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        response.response.close()
        return response.output

    def tag_resource(
        self,
        resource_arn: "capo_codeartifact.types.arn.Arn",
        tags: "capo_codeartifact.types.tag_list.TagList",
        *,
        config_overrides: Optional[codeartifactClientConfig] = None,
    ) -> "capo_codeartifact.types.tag_resource_result.TagResourceResult":
        """<p>Adds or updates tags for a resource in CodeArtifact.</p>

        Args:
            resource_arn: <p>The Amazon Resource Name (ARN) of the resource that you want to add or update tags for.</p>
            tags: <p>The tags you want to modify or add to the resource.</p>

        Raises:
            capo_codeartifact.errors.access_denied_exception.AccessDeniedException: <p> The operation did not succeed because of an unauthorized access attempt. </p>
            capo_codeartifact.errors.resource_not_found_exception.ResourceNotFoundException: <p> The operation did not succeed because the resource requested is not found in the service. </p>
            capo_codeartifact.errors.service_quota_exceeded_exception.ServiceQuotaExceededException: <p> The operation did not succeed because it would have exceeded a service limit for your account. </p>
            capo_codeartifact.errors.throttling_exception.ThrottlingException: <p> The operation did not succeed because too many requests are sent to the service. </p>
            capo_codeartifact.errors.validation_exception.ValidationException: <p> The operation did not succeed because a parameter in the request was sent with an invalid value. </p>
            capo_codeartifact.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        def _handler(
            req: "OperationRequest[capo_codeartifact.types.tag_resource_request.TagResourceRequest]",
        ) -> OperationResponse[
            "capo_codeartifact.types.tag_resource_result.TagResourceResult"
        ]:
            import capo_codeartifact._operations.code_artifact_control_plane_service.tag_resource

            output, http_response = (
                capo_codeartifact._operations.code_artifact_control_plane_service.tag_resource.tag_resource(
                    req.options, req.input
                )
            )
            return OperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_codeartifact.types.tag_resource_request.TagResourceRequest = {
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
        resource_arn: "capo_codeartifact.types.arn.Arn",
        tag_keys: "capo_codeartifact.types.tag_key_list.TagKeyList",
        *,
        config_overrides: Optional[codeartifactClientConfig] = None,
    ) -> "capo_codeartifact.types.untag_resource_result.UntagResourceResult":
        """<p>Removes tags from a resource in CodeArtifact.</p>

        Args:
            resource_arn: <p>The Amazon Resource Name (ARN) of the resource that you want to remove tags from.</p>
            tag_keys: <p>The tag key for each tag that you want to remove from the resource.</p>

        Raises:
            capo_codeartifact.errors.access_denied_exception.AccessDeniedException: <p> The operation did not succeed because of an unauthorized access attempt. </p>
            capo_codeartifact.errors.resource_not_found_exception.ResourceNotFoundException: <p> The operation did not succeed because the resource requested is not found in the service. </p>
            capo_codeartifact.errors.throttling_exception.ThrottlingException: <p> The operation did not succeed because too many requests are sent to the service. </p>
            capo_codeartifact.errors.validation_exception.ValidationException: <p> The operation did not succeed because a parameter in the request was sent with an invalid value. </p>
            capo_codeartifact.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        def _handler(
            req: "OperationRequest[capo_codeartifact.types.untag_resource_request.UntagResourceRequest]",
        ) -> OperationResponse[
            "capo_codeartifact.types.untag_resource_result.UntagResourceResult"
        ]:
            import capo_codeartifact._operations.code_artifact_control_plane_service.untag_resource

            output, http_response = (
                capo_codeartifact._operations.code_artifact_control_plane_service.untag_resource.untag_resource(
                    req.options, req.input
                )
            )
            return OperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_codeartifact.types.untag_resource_request.UntagResourceRequest = {
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

    def update_package_group(
        self,
        domain: "capo_codeartifact.types.domain_name.DomainName",
        package_group: "capo_codeartifact.types.package_group_pattern.PackageGroupPattern",
        *,
        config_overrides: Optional[codeartifactClientConfig] = None,
        domain_owner: Optional["capo_codeartifact.types.account_id.AccountId"] = None,
        contact_info: Optional[
            "capo_codeartifact.types.package_group_contact_info.PackageGroupContactInfo"
        ] = None,
        description: Optional["capo_codeartifact.types.description.Description"] = None,
    ) -> "capo_codeartifact.types.update_package_group_result.UpdatePackageGroupResult":
        r"""<p>Updates a package group. This API cannot be used to update a package group's origin configuration or pattern. To update a package group's origin configuration, use <a href=\"https://docs.aws.amazon.com/codeartifact/latest/APIReference/API_UpdatePackageGroupOriginConfiguration.html\">UpdatePackageGroupOriginConfiguration</a>.</p>

        Args:
            domain: <p> The name of the domain which contains the package group to be updated. </p>
            domain_owner: <p> The 12-digit account number of the Amazon Web Services account that owns the domain. It does not include dashes or spaces. </p>
            package_group: <p> The pattern of the package group to be updated. </p>
            contact_info: <p> Contact information which you want to update the requested package group with. </p>
            description: <p> The description you want to update the requested package group with. </p>

        Raises:
            capo_codeartifact.errors.access_denied_exception.AccessDeniedException: <p> The operation did not succeed because of an unauthorized access attempt. </p>
            capo_codeartifact.errors.internal_server_exception.InternalServerException: <p> The operation did not succeed because of an error that occurred inside CodeArtifact. </p>
            capo_codeartifact.errors.resource_not_found_exception.ResourceNotFoundException: <p> The operation did not succeed because the resource requested is not found in the service. </p>
            capo_codeartifact.errors.service_quota_exceeded_exception.ServiceQuotaExceededException: <p> The operation did not succeed because it would have exceeded a service limit for your account. </p>
            capo_codeartifact.errors.throttling_exception.ThrottlingException: <p> The operation did not succeed because too many requests are sent to the service. </p>
            capo_codeartifact.errors.validation_exception.ValidationException: <p> The operation did not succeed because a parameter in the request was sent with an invalid value. </p>
            capo_codeartifact.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        def _handler(
            req: "OperationRequest[capo_codeartifact.types.update_package_group_request.UpdatePackageGroupRequest]",
        ) -> OperationResponse[
            "capo_codeartifact.types.update_package_group_result.UpdatePackageGroupResult"
        ]:
            import capo_codeartifact._operations.code_artifact_control_plane_service.update_package_group

            output, http_response = (
                capo_codeartifact._operations.code_artifact_control_plane_service.update_package_group.update_package_group(
                    req.options, req.input
                )
            )
            return OperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_codeartifact.types.update_package_group_request.UpdatePackageGroupRequest = {
            "domain": domain,
            "package_group": package_group,
        }
        if domain_owner is not None:
            input_["domain_owner"] = domain_owner
        if contact_info is not None:
            input_["contact_info"] = contact_info
        if description is not None:
            input_["description"] = description

        response = execute_pipeline(
            OperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        response.response.close()
        return response.output

    def update_package_group_origin_configuration(
        self,
        domain: "capo_codeartifact.types.domain_name.DomainName",
        package_group: "capo_codeartifact.types.package_group_pattern.PackageGroupPattern",
        *,
        config_overrides: Optional[codeartifactClientConfig] = None,
        domain_owner: Optional["capo_codeartifact.types.account_id.AccountId"] = None,
        restrictions: Optional[
            "capo_codeartifact.types.origin_restrictions.OriginRestrictions"
        ] = None,
        add_allowed_repositories: Optional[
            "capo_codeartifact.types.package_group_allowed_repository_list.PackageGroupAllowedRepositoryList"
        ] = None,
        remove_allowed_repositories: Optional[
            "capo_codeartifact.types.package_group_allowed_repository_list.PackageGroupAllowedRepositoryList"
        ] = None,
    ) -> "capo_codeartifact.types.update_package_group_origin_configuration_result.UpdatePackageGroupOriginConfigurationResult":
        r"""<p>Updates the package origin configuration for a package group.</p> <p>The package origin configuration determines how new versions of a package can be added to a repository. You can allow or block direct publishing of new package versions, or ingestion and retaining of new package versions from an external connection or upstream source. For more information about package group origin controls and configuration, see <a href=\"https://docs.aws.amazon.com/codeartifact/latest/ug/package-group-origin-controls.html\">Package group origin controls</a> in the <i>CodeArtifact User Guide</i>.</p>

        Args:
            domain: <p> The name of the domain which contains the package group for which to update the origin configuration. </p>
            domain_owner: <p> The 12-digit account number of the Amazon Web Services account that owns the domain. It does not include dashes or spaces. </p>
            package_group: <p> The pattern of the package group for which to update the origin configuration. </p>
            restrictions: <p> The origin configuration settings that determine how package versions can enter repositories. </p>
            add_allowed_repositories: <p>The repository name and restrictions to add to the allowed repository list of the specified package group.</p>
            remove_allowed_repositories: <p>The repository name and restrictions to remove from the allowed repository list of the specified package group.</p>

        Raises:
            capo_codeartifact.errors.access_denied_exception.AccessDeniedException: <p> The operation did not succeed because of an unauthorized access attempt. </p>
            capo_codeartifact.errors.internal_server_exception.InternalServerException: <p> The operation did not succeed because of an error that occurred inside CodeArtifact. </p>
            capo_codeartifact.errors.resource_not_found_exception.ResourceNotFoundException: <p> The operation did not succeed because the resource requested is not found in the service. </p>
            capo_codeartifact.errors.service_quota_exceeded_exception.ServiceQuotaExceededException: <p> The operation did not succeed because it would have exceeded a service limit for your account. </p>
            capo_codeartifact.errors.throttling_exception.ThrottlingException: <p> The operation did not succeed because too many requests are sent to the service. </p>
            capo_codeartifact.errors.validation_exception.ValidationException: <p> The operation did not succeed because a parameter in the request was sent with an invalid value. </p>
            capo_codeartifact.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        def _handler(
            req: "OperationRequest[capo_codeartifact.types.update_package_group_origin_configuration_request.UpdatePackageGroupOriginConfigurationRequest]",
        ) -> OperationResponse[
            "capo_codeartifact.types.update_package_group_origin_configuration_result.UpdatePackageGroupOriginConfigurationResult"
        ]:
            import capo_codeartifact._operations.code_artifact_control_plane_service.update_package_group_origin_configuration

            output, http_response = (
                capo_codeartifact._operations.code_artifact_control_plane_service.update_package_group_origin_configuration.update_package_group_origin_configuration(
                    req.options, req.input
                )
            )
            return OperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_codeartifact.types.update_package_group_origin_configuration_request.UpdatePackageGroupOriginConfigurationRequest = {
            "domain": domain,
            "package_group": package_group,
        }
        if domain_owner is not None:
            input_["domain_owner"] = domain_owner
        if restrictions is not None:
            input_["restrictions"] = restrictions
        if add_allowed_repositories is not None:
            input_["add_allowed_repositories"] = add_allowed_repositories
        if remove_allowed_repositories is not None:
            input_["remove_allowed_repositories"] = remove_allowed_repositories

        response = execute_pipeline(
            OperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        response.response.close()
        return response.output

    def update_package_versions_status(
        self,
        domain: "capo_codeartifact.types.domain_name.DomainName",
        repository: "capo_codeartifact.types.repository_name.RepositoryName",
        format: "capo_codeartifact.types.package_format.PackageFormat",
        package: "capo_codeartifact.types.package_name.PackageName",
        versions: "capo_codeartifact.types.package_version_list.PackageVersionList",
        target_status: "capo_codeartifact.types.package_version_status.PackageVersionStatus",
        *,
        config_overrides: Optional[codeartifactClientConfig] = None,
        domain_owner: Optional["capo_codeartifact.types.account_id.AccountId"] = None,
        namespace: Optional[
            "capo_codeartifact.types.package_namespace.PackageNamespace"
        ] = None,
        version_revisions: Optional[
            "capo_codeartifact.types.package_version_revision_map.PackageVersionRevisionMap"
        ] = None,
        expected_status: Optional[
            "capo_codeartifact.types.package_version_status.PackageVersionStatus"
        ] = None,
    ) -> "capo_codeartifact.types.update_package_versions_status_result.UpdatePackageVersionsStatusResult":
        r"""<p> Updates the status of one or more versions of a package. Using <code>UpdatePackageVersionsStatus</code>, you can update the status of package versions to <code>Archived</code>, <code>Published</code>, or <code>Unlisted</code>. To set the status of a package version to <code>Disposed</code>, use <a href=\"https://docs.aws.amazon.com/codeartifact/latest/APIReference/API_DisposePackageVersions.html\">DisposePackageVersions</a>. </p>

        Args:
            domain: <p> The name of the domain that contains the repository that contains the package versions with a status to be updated. </p>
            domain_owner: <p> The 12-digit account number of the Amazon Web Services account that owns the domain. It does not include dashes or spaces. </p>
            repository: <p> The repository that contains the package versions with the status you want to update. </p>
            format: <p> A format that specifies the type of the package with the statuses to update. </p>
            namespace: <p>The namespace of the package version to be updated. The package component that specifies its namespace depends on its type. For example:</p> <ul> <li> <p> The namespace of a Maven package version is its <code>groupId</code>. </p> </li> <li> <p> The namespace of an npm or Swift package version is its <code>scope</code>. </p> </li> <li> <p>The namespace of a generic package is its <code>namespace</code>.</p> </li> <li> <p> Python, NuGet, Ruby, and Cargo package versions do not contain a corresponding component, package versions of those formats do not have a namespace. </p> </li> </ul>
            package: <p> The name of the package with the version statuses to update. </p>
            versions: <p> An array of strings that specify the versions of the package with the statuses to update. </p>
            version_revisions: <p> A map of package versions and package version revisions. The map <code>key</code> is the package version (for example, <code>3.5.2</code>), and the map <code>value</code> is the package version revision. </p>
            expected_status: <p> The package version’s expected status before it is updated. If <code>expectedStatus</code> is provided, the package version's status is updated only if its status at the time <code>UpdatePackageVersionsStatus</code> is called matches <code>expectedStatus</code>. </p>
            target_status: <p> The status you want to change the package version status to. </p>

        Raises:
            capo_codeartifact.errors.access_denied_exception.AccessDeniedException: <p> The operation did not succeed because of an unauthorized access attempt. </p>
            capo_codeartifact.errors.conflict_exception.ConflictException: <p> The operation did not succeed because prerequisites are not met. </p>
            capo_codeartifact.errors.internal_server_exception.InternalServerException: <p> The operation did not succeed because of an error that occurred inside CodeArtifact. </p>
            capo_codeartifact.errors.resource_not_found_exception.ResourceNotFoundException: <p> The operation did not succeed because the resource requested is not found in the service. </p>
            capo_codeartifact.errors.throttling_exception.ThrottlingException: <p> The operation did not succeed because too many requests are sent to the service. </p>
            capo_codeartifact.errors.validation_exception.ValidationException: <p> The operation did not succeed because a parameter in the request was sent with an invalid value. </p>
            capo_codeartifact.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        def _handler(
            req: "OperationRequest[capo_codeartifact.types.update_package_versions_status_request.UpdatePackageVersionsStatusRequest]",
        ) -> OperationResponse[
            "capo_codeartifact.types.update_package_versions_status_result.UpdatePackageVersionsStatusResult"
        ]:
            import capo_codeartifact._operations.code_artifact_control_plane_service.update_package_versions_status

            output, http_response = (
                capo_codeartifact._operations.code_artifact_control_plane_service.update_package_versions_status.update_package_versions_status(
                    req.options, req.input
                )
            )
            return OperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_codeartifact.types.update_package_versions_status_request.UpdatePackageVersionsStatusRequest = {
            "domain": domain,
            "repository": repository,
            "format": format,
            "package": package,
            "versions": versions,
            "target_status": target_status,
        }
        if domain_owner is not None:
            input_["domain_owner"] = domain_owner
        if namespace is not None:
            input_["namespace"] = namespace
        if version_revisions is not None:
            input_["version_revisions"] = version_revisions
        if expected_status is not None:
            input_["expected_status"] = expected_status

        response = execute_pipeline(
            OperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        response.response.close()
        return response.output

    def update_repository(
        self,
        domain: "capo_codeartifact.types.domain_name.DomainName",
        repository: "capo_codeartifact.types.repository_name.RepositoryName",
        *,
        config_overrides: Optional[codeartifactClientConfig] = None,
        domain_owner: Optional["capo_codeartifact.types.account_id.AccountId"] = None,
        description: Optional["capo_codeartifact.types.description.Description"] = None,
        upstreams: Optional[
            "capo_codeartifact.types.upstream_repository_list.UpstreamRepositoryList"
        ] = None,
    ) -> "capo_codeartifact.types.update_repository_result.UpdateRepositoryResult":
        r"""<p> Update the properties of a repository. </p>

        Args:
            domain: <p> The name of the domain associated with the repository to update. </p>
            domain_owner: <p> The 12-digit account number of the Amazon Web Services account that owns the domain. It does not include dashes or spaces. </p>
            repository: <p> The name of the repository to update. </p>
            description: <p> An updated repository description. </p>
            upstreams: <p> A list of upstream repositories to associate with the repository. The order of the upstream repositories in the list determines their priority order when CodeArtifact looks for a requested package version. For more information, see <a href=\"https://docs.aws.amazon.com/codeartifact/latest/ug/repos-upstream.html\">Working with upstream repositories</a>. </p>

        Raises:
            capo_codeartifact.errors.access_denied_exception.AccessDeniedException: <p> The operation did not succeed because of an unauthorized access attempt. </p>
            capo_codeartifact.errors.conflict_exception.ConflictException: <p> The operation did not succeed because prerequisites are not met. </p>
            capo_codeartifact.errors.internal_server_exception.InternalServerException: <p> The operation did not succeed because of an error that occurred inside CodeArtifact. </p>
            capo_codeartifact.errors.resource_not_found_exception.ResourceNotFoundException: <p> The operation did not succeed because the resource requested is not found in the service. </p>
            capo_codeartifact.errors.service_quota_exceeded_exception.ServiceQuotaExceededException: <p> The operation did not succeed because it would have exceeded a service limit for your account. </p>
            capo_codeartifact.errors.throttling_exception.ThrottlingException: <p> The operation did not succeed because too many requests are sent to the service. </p>
            capo_codeartifact.errors.validation_exception.ValidationException: <p> The operation did not succeed because a parameter in the request was sent with an invalid value. </p>
            capo_codeartifact.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        def _handler(
            req: "OperationRequest[capo_codeartifact.types.update_repository_request.UpdateRepositoryRequest]",
        ) -> OperationResponse[
            "capo_codeartifact.types.update_repository_result.UpdateRepositoryResult"
        ]:
            import capo_codeartifact._operations.code_artifact_control_plane_service.update_repository

            output, http_response = (
                capo_codeartifact._operations.code_artifact_control_plane_service.update_repository.update_repository(
                    req.options, req.input
                )
            )
            return OperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_codeartifact.types.update_repository_request.UpdateRepositoryRequest = {
            "domain": domain,
            "repository": repository,
        }
        if domain_owner is not None:
            input_["domain_owner"] = domain_owner
        if description is not None:
            input_["description"] = description
        if upstreams is not None:
            input_["upstreams"] = upstreams

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
