from __future__ import annotations

from typing import TYPE_CHECKING, Optional

import capo_artifact._auth._signers
import capo_artifact._auth._sigv4
from capo_artifact._services._pipeline import (
    AsyncOperationRequest,
    AsyncOperationResponse,
    OperationLogging,
    OperationRequest,
    OperationResponse,
    aexecute_pipeline,
    execute_pipeline,
)

if TYPE_CHECKING:
    import capo_artifact.types.get_report_metadata_request
    import capo_artifact.types.get_report_metadata_response
    import capo_artifact.types.get_report_request
    import capo_artifact.types.get_report_response
    import capo_artifact.types.get_term_for_report_request
    import capo_artifact.types.get_term_for_report_response
    import capo_artifact.types.list_report_versions_request
    import capo_artifact.types.list_report_versions_response
    import capo_artifact.types.list_reports_request
    import capo_artifact.types.list_reports_response
    import capo_artifact.types.max_results_attribute
    import capo_artifact.types.next_token_attribute
    import capo_artifact.types.report_id
    import capo_artifact.types.report_summary
    import capo_artifact.types.short_string_attribute
    import capo_artifact.types.version_attribute
    from capo_artifact._services.artifact import ArtifactClient, ArtifactClientConfig
    from capo_artifact._services.async_artifact import (
        AsyncArtifactClient,
        AsyncArtifactClientConfig,
    )


class ReportResource:
    def __init__(self, service: ArtifactClient) -> None:
        self._service = service

    def read(
        self,
        report_id: "capo_artifact.types.report_id.ReportId",
        *,
        config_overrides: Optional[ArtifactClientConfig] = None,
        report_version: Optional[
            "capo_artifact.types.version_attribute.VersionAttribute"
        ] = None,
    ) -> "capo_artifact.types.get_report_metadata_response.GetReportMetadataResponse":
        """<p>Get the metadata for a single report.</p>

        Args:
            report_id: <p>Unique resource ID for the report resource.</p>
            report_version: <p>Version for the report resource.</p>

        Raises:
            capo_artifact.errors.access_denied_exception.AccessDeniedException: <p>User does not have sufficient access to perform this action.</p>
            capo_artifact.errors.internal_server_exception.InternalServerException: <p>An unknown server exception has occurred.</p>
            capo_artifact.errors.resource_not_found_exception.ResourceNotFoundException: <p>Request references a resource which does not exist.</p>
            capo_artifact.errors.service_quota_exceeded_exception.ServiceQuotaExceededException: <p>Request would cause a service quota to be exceeded.</p>
            capo_artifact.errors.throttling_exception.ThrottlingException: <p>Request was denied due to request throttling.</p>
            capo_artifact.errors.validation_exception.ValidationException: <p>Request fails to satisfy the constraints specified by an AWS service.</p>
            capo_artifact.errors.UnknownServiceError: The service returned an error code this client does not model.

        Examples:
            Invoke GetReportMetadata operation on the latest version of a specific report
            The GetReportMetadata operation is invoked on a reportId and on a optional version.
                        If callers do not provide a version, it will default to the report's latest version.

            >>> client.read(report_id='report-bqhUJF3FrQZsMJpb')
        """

        def _handler(
            req: "OperationRequest[capo_artifact.types.get_report_metadata_request.GetReportMetadataRequest]",
        ) -> OperationResponse[
            "capo_artifact.types.get_report_metadata_response.GetReportMetadataResponse"
        ]:
            import capo_artifact._operations.artifact.get_report_metadata

            output, http_response = (
                capo_artifact._operations.artifact.get_report_metadata.get_report_metadata(
                    req.options, req.input
                )
            )
            return OperationResponse(output=output, response=http_response)

        interceptors_, options_ = self._service.operation_options(
            config_overrides, OperationLogging("GetReportMetadata")
        )
        input_: capo_artifact.types.get_report_metadata_request.GetReportMetadataRequest = {
            "report_id": report_id
        }
        if report_version is not None:
            input_["report_version"] = report_version

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
        config_overrides: Optional[ArtifactClientConfig] = None,
        max_results: Optional[
            "capo_artifact.types.max_results_attribute.MaxResultsAttribute"
        ] = None,
        next_token: Optional[
            "capo_artifact.types.next_token_attribute.NextTokenAttribute"
        ] = None,
    ) -> "capo_artifact.types.list_reports_response.ListReportsResponse":
        """<p>List available reports.</p>

        Args:
            max_results: <p>Maximum number of resources to return in the paginated response.</p>
            next_token: <p>Pagination token to request the next page of resources.</p>

        Raises:
            capo_artifact.errors.access_denied_exception.AccessDeniedException: <p>User does not have sufficient access to perform this action.</p>
            capo_artifact.errors.internal_server_exception.InternalServerException: <p>An unknown server exception has occurred.</p>
            capo_artifact.errors.resource_not_found_exception.ResourceNotFoundException: <p>Request references a resource which does not exist.</p>
            capo_artifact.errors.service_quota_exceeded_exception.ServiceQuotaExceededException: <p>Request would cause a service quota to be exceeded.</p>
            capo_artifact.errors.throttling_exception.ThrottlingException: <p>Request was denied due to request throttling.</p>
            capo_artifact.errors.validation_exception.ValidationException: <p>Request fails to satisfy the constraints specified by an AWS service.</p>
            capo_artifact.errors.UnknownServiceError: The service returned an error code this client does not model.

        Examples:
            Invoke ListReports operation
            The ListReports operation returns a collection of report resources.

            >>> client.list()
        """

        def _handler(
            req: "OperationRequest[capo_artifact.types.list_reports_request.ListReportsRequest]",
        ) -> OperationResponse[
            "capo_artifact.types.list_reports_response.ListReportsResponse"
        ]:
            import capo_artifact._operations.artifact.list_reports

            output, http_response = (
                capo_artifact._operations.artifact.list_reports.list_reports(
                    req.options, req.input
                )
            )
            return OperationResponse(output=output, response=http_response)

        interceptors_, options_ = self._service.operation_options(
            config_overrides, OperationLogging("ListReports")
        )
        input_: capo_artifact.types.list_reports_request.ListReportsRequest = {}
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

    def get_report(
        self,
        report_id: "capo_artifact.types.report_id.ReportId",
        term_token: "capo_artifact.types.short_string_attribute.ShortStringAttribute",
        *,
        config_overrides: Optional[ArtifactClientConfig] = None,
        report_version: Optional[
            "capo_artifact.types.version_attribute.VersionAttribute"
        ] = None,
    ) -> "capo_artifact.types.get_report_response.GetReportResponse":
        """<p>Get the content for a single report.</p>

        Args:
            report_id: <p>Unique resource ID for the report resource.</p>
            report_version: <p>Version for the report resource.</p>
            term_token: <p>Unique download token provided by GetTermForReport API.</p>

        Raises:
            capo_artifact.errors.access_denied_exception.AccessDeniedException: <p>User does not have sufficient access to perform this action.</p>
            capo_artifact.errors.conflict_exception.ConflictException: <p>Request to create/modify content would result in a conflict.</p>
            capo_artifact.errors.internal_server_exception.InternalServerException: <p>An unknown server exception has occurred.</p>
            capo_artifact.errors.resource_not_found_exception.ResourceNotFoundException: <p>Request references a resource which does not exist.</p>
            capo_artifact.errors.service_quota_exceeded_exception.ServiceQuotaExceededException: <p>Request would cause a service quota to be exceeded.</p>
            capo_artifact.errors.throttling_exception.ThrottlingException: <p>Request was denied due to request throttling.</p>
            capo_artifact.errors.validation_exception.ValidationException: <p>Request fails to satisfy the constraints specified by an AWS service.</p>
            capo_artifact.errors.UnknownServiceError: The service returned an error code this client does not model.

        Examples:
            Invoke GetReport operation on the latest version of a specific report
            The GetReport operation is invoked on a reportId and on a optional version.
                        Callers must provide a termToken, which is provided by the GetTermForReport
                        operation. If callers do not provide a version, it will default to the
                        report's latest version

            >>> client.get_report(report_id='report-abcdef0123456789', term_token='term-token-abcdefghijklm01234567890')
        """

        def _handler(
            req: "OperationRequest[capo_artifact.types.get_report_request.GetReportRequest]",
        ) -> OperationResponse[
            "capo_artifact.types.get_report_response.GetReportResponse"
        ]:
            import capo_artifact._operations.artifact.get_report

            output, http_response = (
                capo_artifact._operations.artifact.get_report.get_report(
                    req.options, req.input
                )
            )
            return OperationResponse(output=output, response=http_response)

        interceptors_, options_ = self._service.operation_options(
            config_overrides, OperationLogging("GetReport")
        )
        input_: capo_artifact.types.get_report_request.GetReportRequest = {
            "report_id": report_id,
            "term_token": term_token,
        }
        if report_version is not None:
            input_["report_version"] = report_version

        response = execute_pipeline(
            OperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        response.response.close()
        return response.output

    def get_term_for_report(
        self,
        report_id: "capo_artifact.types.report_id.ReportId",
        *,
        config_overrides: Optional[ArtifactClientConfig] = None,
        report_version: Optional[
            "capo_artifact.types.version_attribute.VersionAttribute"
        ] = None,
    ) -> "capo_artifact.types.get_term_for_report_response.GetTermForReportResponse":
        """<p>Get the Term content associated with a single report.</p>

        Args:
            report_id: <p>Unique resource ID for the report resource.</p>
            report_version: <p>Version for the report resource.</p>

        Raises:
            capo_artifact.errors.access_denied_exception.AccessDeniedException: <p>User does not have sufficient access to perform this action.</p>
            capo_artifact.errors.conflict_exception.ConflictException: <p>Request to create/modify content would result in a conflict.</p>
            capo_artifact.errors.internal_server_exception.InternalServerException: <p>An unknown server exception has occurred.</p>
            capo_artifact.errors.resource_not_found_exception.ResourceNotFoundException: <p>Request references a resource which does not exist.</p>
            capo_artifact.errors.service_quota_exceeded_exception.ServiceQuotaExceededException: <p>Request would cause a service quota to be exceeded.</p>
            capo_artifact.errors.throttling_exception.ThrottlingException: <p>Request was denied due to request throttling.</p>
            capo_artifact.errors.validation_exception.ValidationException: <p>Request fails to satisfy the constraints specified by an AWS service.</p>
            capo_artifact.errors.UnknownServiceError: The service returned an error code this client does not model.

        Examples:
            Invoke GetTermForReport operation on the latest version of a specific report
            The GetTermForReport operation is invoked on a reportId and on a optional version.
                        If callers do not provide a version, it will default to the report's latest version.

            >>> client.get_term_for_report(report_id='report-abcdef0123456789')
        """

        def _handler(
            req: "OperationRequest[capo_artifact.types.get_term_for_report_request.GetTermForReportRequest]",
        ) -> OperationResponse[
            "capo_artifact.types.get_term_for_report_response.GetTermForReportResponse"
        ]:
            import capo_artifact._operations.artifact.get_term_for_report

            output, http_response = (
                capo_artifact._operations.artifact.get_term_for_report.get_term_for_report(
                    req.options, req.input
                )
            )
            return OperationResponse(output=output, response=http_response)

        interceptors_, options_ = self._service.operation_options(
            config_overrides, OperationLogging("GetTermForReport")
        )
        input_: capo_artifact.types.get_term_for_report_request.GetTermForReportRequest = {
            "report_id": report_id
        }
        if report_version is not None:
            input_["report_version"] = report_version

        response = execute_pipeline(
            OperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        response.response.close()
        return response.output

    def list_report_versions(
        self,
        report_id: "capo_artifact.types.report_id.ReportId",
        *,
        config_overrides: Optional[ArtifactClientConfig] = None,
        max_results: Optional[
            "capo_artifact.types.max_results_attribute.MaxResultsAttribute"
        ] = None,
        next_token: Optional[
            "capo_artifact.types.next_token_attribute.NextTokenAttribute"
        ] = None,
    ) -> "capo_artifact.types.list_report_versions_response.ListReportVersionsResponse":
        """<p>List available report versions for a given report.</p>

        Args:
            report_id: <p>Unique resource ID for the report resource.</p>
            max_results: <p>Maximum number of resources to return in the paginated response.</p>
            next_token: <p>Pagination token to request the next page of resources.</p>

        Raises:
            capo_artifact.errors.access_denied_exception.AccessDeniedException: <p>User does not have sufficient access to perform this action.</p>
            capo_artifact.errors.internal_server_exception.InternalServerException: <p>An unknown server exception has occurred.</p>
            capo_artifact.errors.resource_not_found_exception.ResourceNotFoundException: <p>Request references a resource which does not exist.</p>
            capo_artifact.errors.service_quota_exceeded_exception.ServiceQuotaExceededException: <p>Request would cause a service quota to be exceeded.</p>
            capo_artifact.errors.throttling_exception.ThrottlingException: <p>Request was denied due to request throttling.</p>
            capo_artifact.errors.validation_exception.ValidationException: <p>Request fails to satisfy the constraints specified by an AWS service.</p>
            capo_artifact.errors.UnknownServiceError: The service returned an error code this client does not model.

        Examples:
            Invoke ListReportVersions operation
            The ListReportVersions operation returns a collection of report versions
                        for a given resource.

            >>> client.list_report_versions(report_id='report-abcdef0123456789')
        """

        def _handler(
            req: "OperationRequest[capo_artifact.types.list_report_versions_request.ListReportVersionsRequest]",
        ) -> OperationResponse[
            "capo_artifact.types.list_report_versions_response.ListReportVersionsResponse"
        ]:
            import capo_artifact._operations.artifact.list_report_versions

            output, http_response = (
                capo_artifact._operations.artifact.list_report_versions.list_report_versions(
                    req.options, req.input
                )
            )
            return OperationResponse(output=output, response=http_response)

        interceptors_, options_ = self._service.operation_options(
            config_overrides, OperationLogging("ListReportVersions")
        )
        input_: capo_artifact.types.list_report_versions_request.ListReportVersionsRequest = {
            "report_id": report_id
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


class AsyncReportResource:
    def __init__(self, service: AsyncArtifactClient) -> None:
        self._service = service

    async def read(
        self,
        report_id: "capo_artifact.types.report_id.ReportId",
        *,
        config_overrides: Optional[AsyncArtifactClientConfig] = None,
        report_version: Optional[
            "capo_artifact.types.version_attribute.VersionAttribute"
        ] = None,
    ) -> "capo_artifact.types.get_report_metadata_response.GetReportMetadataResponse":
        """<p>Get the metadata for a single report.</p>

        Args:
            report_id: <p>Unique resource ID for the report resource.</p>
            report_version: <p>Version for the report resource.</p>

        Raises:
            capo_artifact.errors.access_denied_exception.AccessDeniedException: <p>User does not have sufficient access to perform this action.</p>
            capo_artifact.errors.internal_server_exception.InternalServerException: <p>An unknown server exception has occurred.</p>
            capo_artifact.errors.resource_not_found_exception.ResourceNotFoundException: <p>Request references a resource which does not exist.</p>
            capo_artifact.errors.service_quota_exceeded_exception.ServiceQuotaExceededException: <p>Request would cause a service quota to be exceeded.</p>
            capo_artifact.errors.throttling_exception.ThrottlingException: <p>Request was denied due to request throttling.</p>
            capo_artifact.errors.validation_exception.ValidationException: <p>Request fails to satisfy the constraints specified by an AWS service.</p>
            capo_artifact.errors.UnknownServiceError: The service returned an error code this client does not model.

        Examples:
            Invoke GetReportMetadata operation on the latest version of a specific report
            The GetReportMetadata operation is invoked on a reportId and on a optional version.
                        If callers do not provide a version, it will default to the report's latest version.

            >>> await client.read(report_id='report-bqhUJF3FrQZsMJpb')
        """

        async def _handler(
            req: "AsyncOperationRequest[capo_artifact.types.get_report_metadata_request.GetReportMetadataRequest]",
        ) -> AsyncOperationResponse[
            "capo_artifact.types.get_report_metadata_response.GetReportMetadataResponse"
        ]:
            import capo_artifact._operations.artifact.get_report_metadata

            (
                output,
                http_response,
            ) = await capo_artifact._operations.artifact.get_report_metadata.async_get_report_metadata(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self._service.operation_options(
            config_overrides, OperationLogging("GetReportMetadata")
        )
        input_: capo_artifact.types.get_report_metadata_request.GetReportMetadataRequest = {
            "report_id": report_id
        }
        if report_version is not None:
            input_["report_version"] = report_version

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
        config_overrides: Optional[AsyncArtifactClientConfig] = None,
        max_results: Optional[
            "capo_artifact.types.max_results_attribute.MaxResultsAttribute"
        ] = None,
        next_token: Optional[
            "capo_artifact.types.next_token_attribute.NextTokenAttribute"
        ] = None,
    ) -> "capo_artifact.types.list_reports_response.ListReportsResponse":
        """<p>List available reports.</p>

        Args:
            max_results: <p>Maximum number of resources to return in the paginated response.</p>
            next_token: <p>Pagination token to request the next page of resources.</p>

        Raises:
            capo_artifact.errors.access_denied_exception.AccessDeniedException: <p>User does not have sufficient access to perform this action.</p>
            capo_artifact.errors.internal_server_exception.InternalServerException: <p>An unknown server exception has occurred.</p>
            capo_artifact.errors.resource_not_found_exception.ResourceNotFoundException: <p>Request references a resource which does not exist.</p>
            capo_artifact.errors.service_quota_exceeded_exception.ServiceQuotaExceededException: <p>Request would cause a service quota to be exceeded.</p>
            capo_artifact.errors.throttling_exception.ThrottlingException: <p>Request was denied due to request throttling.</p>
            capo_artifact.errors.validation_exception.ValidationException: <p>Request fails to satisfy the constraints specified by an AWS service.</p>
            capo_artifact.errors.UnknownServiceError: The service returned an error code this client does not model.

        Examples:
            Invoke ListReports operation
            The ListReports operation returns a collection of report resources.

            >>> await client.list()
        """

        async def _handler(
            req: "AsyncOperationRequest[capo_artifact.types.list_reports_request.ListReportsRequest]",
        ) -> AsyncOperationResponse[
            "capo_artifact.types.list_reports_response.ListReportsResponse"
        ]:
            import capo_artifact._operations.artifact.list_reports

            (
                output,
                http_response,
            ) = await capo_artifact._operations.artifact.list_reports.async_list_reports(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self._service.operation_options(
            config_overrides, OperationLogging("ListReports")
        )
        input_: capo_artifact.types.list_reports_request.ListReportsRequest = {}
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

    async def get_report(
        self,
        report_id: "capo_artifact.types.report_id.ReportId",
        term_token: "capo_artifact.types.short_string_attribute.ShortStringAttribute",
        *,
        config_overrides: Optional[AsyncArtifactClientConfig] = None,
        report_version: Optional[
            "capo_artifact.types.version_attribute.VersionAttribute"
        ] = None,
    ) -> "capo_artifact.types.get_report_response.GetReportResponse":
        """<p>Get the content for a single report.</p>

        Args:
            report_id: <p>Unique resource ID for the report resource.</p>
            report_version: <p>Version for the report resource.</p>
            term_token: <p>Unique download token provided by GetTermForReport API.</p>

        Raises:
            capo_artifact.errors.access_denied_exception.AccessDeniedException: <p>User does not have sufficient access to perform this action.</p>
            capo_artifact.errors.conflict_exception.ConflictException: <p>Request to create/modify content would result in a conflict.</p>
            capo_artifact.errors.internal_server_exception.InternalServerException: <p>An unknown server exception has occurred.</p>
            capo_artifact.errors.resource_not_found_exception.ResourceNotFoundException: <p>Request references a resource which does not exist.</p>
            capo_artifact.errors.service_quota_exceeded_exception.ServiceQuotaExceededException: <p>Request would cause a service quota to be exceeded.</p>
            capo_artifact.errors.throttling_exception.ThrottlingException: <p>Request was denied due to request throttling.</p>
            capo_artifact.errors.validation_exception.ValidationException: <p>Request fails to satisfy the constraints specified by an AWS service.</p>
            capo_artifact.errors.UnknownServiceError: The service returned an error code this client does not model.

        Examples:
            Invoke GetReport operation on the latest version of a specific report
            The GetReport operation is invoked on a reportId and on a optional version.
                        Callers must provide a termToken, which is provided by the GetTermForReport
                        operation. If callers do not provide a version, it will default to the
                        report's latest version

            >>> await client.get_report(report_id='report-abcdef0123456789', term_token='term-token-abcdefghijklm01234567890')
        """

        async def _handler(
            req: "AsyncOperationRequest[capo_artifact.types.get_report_request.GetReportRequest]",
        ) -> AsyncOperationResponse[
            "capo_artifact.types.get_report_response.GetReportResponse"
        ]:
            import capo_artifact._operations.artifact.get_report

            (
                output,
                http_response,
            ) = await capo_artifact._operations.artifact.get_report.async_get_report(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self._service.operation_options(
            config_overrides, OperationLogging("GetReport")
        )
        input_: capo_artifact.types.get_report_request.GetReportRequest = {
            "report_id": report_id,
            "term_token": term_token,
        }
        if report_version is not None:
            input_["report_version"] = report_version

        response = await aexecute_pipeline(
            AsyncOperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        await response.response.aclose()
        return response.output

    async def get_term_for_report(
        self,
        report_id: "capo_artifact.types.report_id.ReportId",
        *,
        config_overrides: Optional[AsyncArtifactClientConfig] = None,
        report_version: Optional[
            "capo_artifact.types.version_attribute.VersionAttribute"
        ] = None,
    ) -> "capo_artifact.types.get_term_for_report_response.GetTermForReportResponse":
        """<p>Get the Term content associated with a single report.</p>

        Args:
            report_id: <p>Unique resource ID for the report resource.</p>
            report_version: <p>Version for the report resource.</p>

        Raises:
            capo_artifact.errors.access_denied_exception.AccessDeniedException: <p>User does not have sufficient access to perform this action.</p>
            capo_artifact.errors.conflict_exception.ConflictException: <p>Request to create/modify content would result in a conflict.</p>
            capo_artifact.errors.internal_server_exception.InternalServerException: <p>An unknown server exception has occurred.</p>
            capo_artifact.errors.resource_not_found_exception.ResourceNotFoundException: <p>Request references a resource which does not exist.</p>
            capo_artifact.errors.service_quota_exceeded_exception.ServiceQuotaExceededException: <p>Request would cause a service quota to be exceeded.</p>
            capo_artifact.errors.throttling_exception.ThrottlingException: <p>Request was denied due to request throttling.</p>
            capo_artifact.errors.validation_exception.ValidationException: <p>Request fails to satisfy the constraints specified by an AWS service.</p>
            capo_artifact.errors.UnknownServiceError: The service returned an error code this client does not model.

        Examples:
            Invoke GetTermForReport operation on the latest version of a specific report
            The GetTermForReport operation is invoked on a reportId and on a optional version.
                        If callers do not provide a version, it will default to the report's latest version.

            >>> await client.get_term_for_report(report_id='report-abcdef0123456789')
        """

        async def _handler(
            req: "AsyncOperationRequest[capo_artifact.types.get_term_for_report_request.GetTermForReportRequest]",
        ) -> AsyncOperationResponse[
            "capo_artifact.types.get_term_for_report_response.GetTermForReportResponse"
        ]:
            import capo_artifact._operations.artifact.get_term_for_report

            (
                output,
                http_response,
            ) = await capo_artifact._operations.artifact.get_term_for_report.async_get_term_for_report(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self._service.operation_options(
            config_overrides, OperationLogging("GetTermForReport")
        )
        input_: capo_artifact.types.get_term_for_report_request.GetTermForReportRequest = {
            "report_id": report_id
        }
        if report_version is not None:
            input_["report_version"] = report_version

        response = await aexecute_pipeline(
            AsyncOperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        await response.response.aclose()
        return response.output

    async def list_report_versions(
        self,
        report_id: "capo_artifact.types.report_id.ReportId",
        *,
        config_overrides: Optional[AsyncArtifactClientConfig] = None,
        max_results: Optional[
            "capo_artifact.types.max_results_attribute.MaxResultsAttribute"
        ] = None,
        next_token: Optional[
            "capo_artifact.types.next_token_attribute.NextTokenAttribute"
        ] = None,
    ) -> "capo_artifact.types.list_report_versions_response.ListReportVersionsResponse":
        """<p>List available report versions for a given report.</p>

        Args:
            report_id: <p>Unique resource ID for the report resource.</p>
            max_results: <p>Maximum number of resources to return in the paginated response.</p>
            next_token: <p>Pagination token to request the next page of resources.</p>

        Raises:
            capo_artifact.errors.access_denied_exception.AccessDeniedException: <p>User does not have sufficient access to perform this action.</p>
            capo_artifact.errors.internal_server_exception.InternalServerException: <p>An unknown server exception has occurred.</p>
            capo_artifact.errors.resource_not_found_exception.ResourceNotFoundException: <p>Request references a resource which does not exist.</p>
            capo_artifact.errors.service_quota_exceeded_exception.ServiceQuotaExceededException: <p>Request would cause a service quota to be exceeded.</p>
            capo_artifact.errors.throttling_exception.ThrottlingException: <p>Request was denied due to request throttling.</p>
            capo_artifact.errors.validation_exception.ValidationException: <p>Request fails to satisfy the constraints specified by an AWS service.</p>
            capo_artifact.errors.UnknownServiceError: The service returned an error code this client does not model.

        Examples:
            Invoke ListReportVersions operation
            The ListReportVersions operation returns a collection of report versions
                        for a given resource.

            >>> await client.list_report_versions(report_id='report-abcdef0123456789')
        """

        async def _handler(
            req: "AsyncOperationRequest[capo_artifact.types.list_report_versions_request.ListReportVersionsRequest]",
        ) -> AsyncOperationResponse[
            "capo_artifact.types.list_report_versions_response.ListReportVersionsResponse"
        ]:
            import capo_artifact._operations.artifact.list_report_versions

            (
                output,
                http_response,
            ) = await capo_artifact._operations.artifact.list_report_versions.async_list_report_versions(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self._service.operation_options(
            config_overrides, OperationLogging("ListReportVersions")
        )
        input_: capo_artifact.types.list_report_versions_request.ListReportVersionsRequest = {
            "report_id": report_id
        }
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
