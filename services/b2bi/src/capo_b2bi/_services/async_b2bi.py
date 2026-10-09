"""Generated from Smithy shape ``com.amazonaws.b2bi#B2BI``."""

import uuid
import warnings
from collections.abc import AsyncIterator
from typing import TYPE_CHECKING, Any, Iterable, Optional

from typing_extensions import Self, TypedDict
from zapros import AsyncBaseHandler, AsyncClient

import capo_b2bi._auth._signers
import capo_b2bi._auth._sigv4
from capo_b2bi._auth._identity import Credentials
from capo_b2bi._auth._providers import (
    CredentialsProvider,
    IdentityProvider,
    StaticAwsCredentialsProvider,
    default_aws_credentials_chain,
)
from capo_b2bi._auth._zapros_handler import AuthMiddleware
from capo_b2bi._pagination import resolve_path as _resolve_path
from capo_b2bi._resources.b2_bi.capability import AsyncCapability
from capo_b2bi._resources.b2_bi.partnership import AsyncPartnership
from capo_b2bi._resources.b2_bi.profile import AsyncProfile
from capo_b2bi._resources.b2_bi.transformer import AsyncTransformer
from capo_b2bi._services._aws_config import aaws_config
from capo_b2bi._services._pipeline import (
    AsyncInterceptor,
    AsyncOperationOptions,
    AsyncOperationRequest,
    AsyncOperationResponse,
    aexecute_pipeline,
    aretry,
)

if TYPE_CHECKING:
    import capo_b2bi.types.advanced_options
    import capo_b2bi.types.amazon_resource_name
    import capo_b2bi.types.business_name
    import capo_b2bi.types.capability_configuration
    import capo_b2bi.types.capability_id
    import capo_b2bi.types.capability_name
    import capo_b2bi.types.capability_options
    import capo_b2bi.types.capability_summary
    import capo_b2bi.types.capability_type
    import capo_b2bi.types.conversion_source
    import capo_b2bi.types.conversion_target
    import capo_b2bi.types.create_capability_request
    import capo_b2bi.types.create_capability_response
    import capo_b2bi.types.create_partnership_request
    import capo_b2bi.types.create_partnership_response
    import capo_b2bi.types.create_profile_request
    import capo_b2bi.types.create_profile_response
    import capo_b2bi.types.create_starter_mapping_template_request
    import capo_b2bi.types.create_starter_mapping_template_response
    import capo_b2bi.types.create_transformer_request
    import capo_b2bi.types.create_transformer_response
    import capo_b2bi.types.delete_capability_request
    import capo_b2bi.types.delete_partnership_request
    import capo_b2bi.types.delete_profile_request
    import capo_b2bi.types.delete_transformer_request
    import capo_b2bi.types.edi_type
    import capo_b2bi.types.email
    import capo_b2bi.types.file_format
    import capo_b2bi.types.file_location
    import capo_b2bi.types.generate_mapping_input_file_content
    import capo_b2bi.types.generate_mapping_output_file_content
    import capo_b2bi.types.generate_mapping_request
    import capo_b2bi.types.generate_mapping_response
    import capo_b2bi.types.get_capability_request
    import capo_b2bi.types.get_capability_response
    import capo_b2bi.types.get_partnership_request
    import capo_b2bi.types.get_partnership_response
    import capo_b2bi.types.get_profile_request
    import capo_b2bi.types.get_profile_response
    import capo_b2bi.types.get_transformer_job_request
    import capo_b2bi.types.get_transformer_job_response
    import capo_b2bi.types.get_transformer_request
    import capo_b2bi.types.get_transformer_response
    import capo_b2bi.types.input_conversion
    import capo_b2bi.types.instructions_documents
    import capo_b2bi.types.list_capabilities_request
    import capo_b2bi.types.list_capabilities_response
    import capo_b2bi.types.list_partnerships_request
    import capo_b2bi.types.list_partnerships_response
    import capo_b2bi.types.list_profiles_request
    import capo_b2bi.types.list_profiles_response
    import capo_b2bi.types.list_tags_for_resource_request
    import capo_b2bi.types.list_tags_for_resource_response
    import capo_b2bi.types.list_transformers_request
    import capo_b2bi.types.list_transformers_response
    import capo_b2bi.types.logging
    import capo_b2bi.types.mapping
    import capo_b2bi.types.mapping_template
    import capo_b2bi.types.mapping_type
    import capo_b2bi.types.max_results
    import capo_b2bi.types.output_conversion
    import capo_b2bi.types.page_token
    import capo_b2bi.types.partner_name
    import capo_b2bi.types.partnership_capabilities
    import capo_b2bi.types.partnership_id
    import capo_b2bi.types.partnership_summary
    import capo_b2bi.types.phone
    import capo_b2bi.types.profile_id
    import capo_b2bi.types.profile_name
    import capo_b2bi.types.profile_summary
    import capo_b2bi.types.s3_location
    import capo_b2bi.types.sample_documents
    import capo_b2bi.types.start_transformer_job_request
    import capo_b2bi.types.start_transformer_job_response
    import capo_b2bi.types.tag_key_list
    import capo_b2bi.types.tag_list
    import capo_b2bi.types.tag_resource_request
    import capo_b2bi.types.template_details
    import capo_b2bi.types.test_conversion_request
    import capo_b2bi.types.test_conversion_response
    import capo_b2bi.types.test_mapping_input_file_content
    import capo_b2bi.types.test_mapping_request
    import capo_b2bi.types.test_mapping_response
    import capo_b2bi.types.test_parsing_request
    import capo_b2bi.types.test_parsing_response
    import capo_b2bi.types.transformer_id
    import capo_b2bi.types.transformer_job_id
    import capo_b2bi.types.transformer_name
    import capo_b2bi.types.transformer_status
    import capo_b2bi.types.transformer_summary
    import capo_b2bi.types.untag_resource_request
    import capo_b2bi.types.update_capability_request
    import capo_b2bi.types.update_capability_response
    import capo_b2bi.types.update_partnership_request
    import capo_b2bi.types.update_partnership_response
    import capo_b2bi.types.update_profile_request
    import capo_b2bi.types.update_profile_response
    import capo_b2bi.types.update_transformer_request
    import capo_b2bi.types.update_transformer_response


class Asyncb2biClientConfig(TypedDict, total=False, closed=True):
    operation_interceptors: Iterable[AsyncInterceptor[Any, Any]]
    retry_max_attempts: int | None
    region: str | None
    use_dual_stack: bool | None
    use_fips: bool | None
    endpoint: str | None
    credentials_provider: IdentityProvider[Credentials] | None
    anonymous: bool | None


class Asyncb2biClient:
    """A client for the ``b2bi`` service.

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
        self._config = Asyncb2biClientConfig(
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

        # resources
        self.capability = AsyncCapability(self)
        self.partnership = AsyncPartnership(self)
        self.profile = AsyncProfile(self)
        self.transformer = AsyncTransformer(self)

    def operation_options(
        self, config_overrides: Optional[Asyncb2biClientConfig] = None
    ) -> tuple[Iterable[AsyncInterceptor[Any, Any]], AsyncOperationOptions]:
        overrides: Asyncb2biClientConfig = config_overrides or {}
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

    async def create_starter_mapping_template(
        self,
        mapping_type: "capo_b2bi.types.mapping_type.MappingType",
        template_details: "capo_b2bi.types.template_details.TemplateDetails",
        *,
        config_overrides: Optional[Asyncb2biClientConfig] = None,
        output_sample_location: Optional[
            "capo_b2bi.types.s3_location.S3Location"
        ] = None,
    ) -> "capo_b2bi.types.create_starter_mapping_template_response.CreateStarterMappingTemplateResponse":
        """<p>Amazon Web Services B2B Data Interchange uses a mapping template in JSONata or XSLT format to transform a customer input file into a JSON or XML file that can be converted to EDI.</p> <p>If you provide a sample EDI file with the same structure as the EDI files that you wish to generate, then the service can generate a mapping template. The starter template contains placeholder values which you can replace with JSONata or XSLT expressions to take data from your input file and insert it into the JSON or XML file that is used to generate the EDI.</p> <p>If you do not provide a sample EDI file, then the service can generate a mapping template based on the EDI settings in the <code>templateDetails</code> parameter. </p> <p> Currently, we only support generating a template that can generate the input to produce an Outbound X12 EDI file.</p>

        Args:
            output_sample_location: <p>Specify the location of the sample EDI file that is used to generate the mapping template.</p>
            mapping_type: <p>Specify the format for the mapping template: either JSONATA or XSLT.</p>
            template_details: <p> Describes the details needed for generating the template. Specify the X12 transaction set and version for which the template is used: currently, we only support X12. </p>

        Raises:
            capo_b2bi.errors.access_denied_exception.AccessDeniedException: <p>You do not have sufficient access to perform this action.</p>
            capo_b2bi.errors.internal_server_exception.InternalServerException: <p>This exception is thrown when an error occurs in the Amazon Web Services B2B Data Interchange service.</p>
            capo_b2bi.errors.resource_not_found_exception.ResourceNotFoundException: <p>Occurs when the requested resource does not exist, or cannot be found. In some cases, the resource exists in a region other than the region specified in the API call.</p>
            capo_b2bi.errors.validation_exception.ValidationException: <p>Occurs when a B2BI object cannot be validated against a request from another object. This exception can be thrown during standard EDI validation or when custom validation rules fail, such as when element length constraints are violated, invalid codes are used in code list validations, or required elements are missing based on configured element requirement rules.</p>
            capo_b2bi.errors.UnknownServiceError: The service returned an error code this client does not model.

        Examples:
            Sample CreateStarterMappingTemplate call

            >>> await client.create_starter_mapping_template(mapping_type='JSONATA', template_details={'x12': {'transactionSet': 'X12_110', 'version': 'VERSION_4010'}}, output_sample_location={'bucketName': 'output-sample-bucket', 'key': 'output-sample-key'})
        """

        async def _handler(
            req: "AsyncOperationRequest[capo_b2bi.types.create_starter_mapping_template_request.CreateStarterMappingTemplateRequest]",
        ) -> AsyncOperationResponse[
            "capo_b2bi.types.create_starter_mapping_template_response.CreateStarterMappingTemplateResponse"
        ]:
            import capo_b2bi._operations.b2_bi.create_starter_mapping_template

            (
                output,
                http_response,
            ) = await capo_b2bi._operations.b2_bi.create_starter_mapping_template.async_create_starter_mapping_template(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_b2bi.types.create_starter_mapping_template_request.CreateStarterMappingTemplateRequest = {
            "mapping_type": mapping_type,
            "template_details": template_details,
        }
        if output_sample_location is not None:
            input_["output_sample_location"] = output_sample_location

        response = await aexecute_pipeline(
            AsyncOperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        await response.response.aclose()
        return response.output

    async def generate_mapping(
        self,
        input_file_content: "capo_b2bi.types.generate_mapping_input_file_content.GenerateMappingInputFileContent",
        output_file_content: "capo_b2bi.types.generate_mapping_output_file_content.GenerateMappingOutputFileContent",
        mapping_type: "capo_b2bi.types.mapping_type.MappingType",
        *,
        config_overrides: Optional[Asyncb2biClientConfig] = None,
    ) -> "capo_b2bi.types.generate_mapping_response.GenerateMappingResponse":
        """<p>Takes sample input and output documents and uses Amazon Bedrock to generate a mapping automatically. Depending on the accuracy and other factors, you can then edit the mapping for your needs.</p> <note> <p>Before you can use the AI-assisted feature for Amazon Web Services B2B Data Interchange you must enable models in Amazon Bedrock. For details, see <a href="https://docs.aws.amazon.com/b2bi/latest/userguide/ai-assisted-mapping.html#ai-assist-prereq">AI-assisted template mapping prerequisites</a> in the <i>Amazon Web Services B2B Data Interchange User guide</i>.</p> </note> <p>To generate a mapping, perform the following steps:</p> <ol> <li> <p>Start with an X12 EDI document to use as the input.</p> </li> <li> <p>Call <code>TestMapping</code> using your EDI document.</p> </li> <li> <p>Use the output from the <code>TestMapping</code> operation as either input or output for your GenerateMapping call, along with your sample file.</p> </li> </ol>

        Args:
            input_file_content: <p>Provide the contents of a sample X12 EDI file, either in JSON or XML format, to use as a starting point for the mapping.</p>
            output_file_content: <p>Provide the contents of a sample X12 EDI file, either in JSON or XML format, to use as a target for the mapping.</p>
            mapping_type: <p>Specify the mapping type: either <code>JSONATA</code> or <code>XSLT.</code> </p>

        Raises:
            capo_b2bi.errors.access_denied_exception.AccessDeniedException: <p>You do not have sufficient access to perform this action.</p>
            capo_b2bi.errors.internal_server_exception.InternalServerException: <p>This exception is thrown when an error occurs in the Amazon Web Services B2B Data Interchange service.</p>
            capo_b2bi.errors.throttling_exception.ThrottlingException: <p>The request was denied due to throttling: the data speed and rendering may be limited depending on various parameters and conditions.</p>
            capo_b2bi.errors.validation_exception.ValidationException: <p>Occurs when a B2BI object cannot be validated against a request from another object. This exception can be thrown during standard EDI validation or when custom validation rules fail, such as when element length constraints are violated, invalid codes are used in code list validations, or required elements are missing based on configured element requirement rules.</p>
            capo_b2bi.errors.UnknownServiceError: The service returned an error code this client does not model.

        Examples:
            Sample GenerateMapping call

            >>> await client.generate_mapping(input_file_content='Sample input file content', output_file_content='Sample output file content', mapping_type='JSONATA')
        """

        async def _handler(
            req: "AsyncOperationRequest[capo_b2bi.types.generate_mapping_request.GenerateMappingRequest]",
        ) -> AsyncOperationResponse[
            "capo_b2bi.types.generate_mapping_response.GenerateMappingResponse"
        ]:
            import capo_b2bi._operations.b2_bi.generate_mapping

            (
                output,
                http_response,
            ) = await capo_b2bi._operations.b2_bi.generate_mapping.async_generate_mapping(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_b2bi.types.generate_mapping_request.GenerateMappingRequest = {
            "input_file_content": input_file_content,
            "output_file_content": output_file_content,
            "mapping_type": mapping_type,
        }

        response = await aexecute_pipeline(
            AsyncOperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        await response.response.aclose()
        return response.output

    async def get_transformer_job(
        self,
        transformer_job_id: "capo_b2bi.types.transformer_job_id.TransformerJobId",
        transformer_id: "capo_b2bi.types.transformer_id.TransformerId",
        *,
        config_overrides: Optional[Asyncb2biClientConfig] = None,
    ) -> "capo_b2bi.types.get_transformer_job_response.GetTransformerJobResponse":
        """<p>Returns the details of the transformer run, based on the Transformer job ID.</p> <note> <p>If 30 days have elapsed since your transformer job was started, the system deletes it. So, if you run <code>GetTransformerJob</code> and supply a <code>transformerId</code> and <code>transformerJobId</code> for a job that was started more than 30 days previously, you receive a 404 response.</p> </note>

        Args:
            transformer_job_id: <p>Specifies the unique, system-generated identifier for a transformer run.</p>
            transformer_id: <p>Specifies the system-assigned unique identifier for the transformer.</p>

        Raises:
            capo_b2bi.errors.access_denied_exception.AccessDeniedException: <p>You do not have sufficient access to perform this action.</p>
            capo_b2bi.errors.internal_server_exception.InternalServerException: <p>This exception is thrown when an error occurs in the Amazon Web Services B2B Data Interchange service.</p>
            capo_b2bi.errors.resource_not_found_exception.ResourceNotFoundException: <p>Occurs when the requested resource does not exist, or cannot be found. In some cases, the resource exists in a region other than the region specified in the API call.</p>
            capo_b2bi.errors.throttling_exception.ThrottlingException: <p>The request was denied due to throttling: the data speed and rendering may be limited depending on various parameters and conditions.</p>
            capo_b2bi.errors.validation_exception.ValidationException: <p>Occurs when a B2BI object cannot be validated against a request from another object. This exception can be thrown during standard EDI validation or when custom validation rules fail, such as when element length constraints are violated, invalid codes are used in code list validations, or required elements are missing based on configured element requirement rules.</p>
            capo_b2bi.errors.UnknownServiceError: The service returned an error code this client does not model.

        Examples:
            Sample GetTransformerJob call

            >>> await client.get_transformer_job(transformer_id='tr-974c129999f84d8c9', transformer_job_id='tj-vpYxfV7yQOqjMSYllEslLw')
        """

        async def _handler(
            req: "AsyncOperationRequest[capo_b2bi.types.get_transformer_job_request.GetTransformerJobRequest]",
        ) -> AsyncOperationResponse[
            "capo_b2bi.types.get_transformer_job_response.GetTransformerJobResponse"
        ]:
            import capo_b2bi._operations.b2_bi.get_transformer_job

            (
                output,
                http_response,
            ) = await capo_b2bi._operations.b2_bi.get_transformer_job.async_get_transformer_job(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_b2bi.types.get_transformer_job_request.GetTransformerJobRequest = {
            "transformer_job_id": transformer_job_id,
            "transformer_id": transformer_id,
        }

        response = await aexecute_pipeline(
            AsyncOperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        await response.response.aclose()
        return response.output

    async def list_tags_for_resource(
        self,
        resource_arn: "capo_b2bi.types.amazon_resource_name.AmazonResourceName",
        *,
        config_overrides: Optional[Asyncb2biClientConfig] = None,
    ) -> "capo_b2bi.types.list_tags_for_resource_response.ListTagsForResourceResponse":
        """<p>Lists all of the tags associated with the Amazon Resource Name (ARN) that you specify. The resource can be a capability, partnership, profile, or transformer.</p>

        Args:
            resource_arn: <p>Requests the tags associated with a particular Amazon Resource Name (ARN). An ARN is an identifier for a specific Amazon Web Services resource, such as a capability, partnership, profile, or transformer.</p>

        Raises:
            capo_b2bi.errors.internal_server_exception.InternalServerException: <p>This exception is thrown when an error occurs in the Amazon Web Services B2B Data Interchange service.</p>
            capo_b2bi.errors.resource_not_found_exception.ResourceNotFoundException: <p>Occurs when the requested resource does not exist, or cannot be found. In some cases, the resource exists in a region other than the region specified in the API call.</p>
            capo_b2bi.errors.validation_exception.ValidationException: <p>Occurs when a B2BI object cannot be validated against a request from another object. This exception can be thrown during standard EDI validation or when custom validation rules fail, such as when element length constraints are violated, invalid codes are used in code list validations, or required elements are missing based on configured element requirement rules.</p>
            capo_b2bi.errors.UnknownServiceError: The service returned an error code this client does not model.

        Examples:
            Sample ListTagsForResources call

            >>> await client.list_tags_for_resource(resource_arn='arn:aws:b2bi:us-west-2:123456789012:profile/p-60fbc37c87f04fce9')
        """

        async def _handler(
            req: "AsyncOperationRequest[capo_b2bi.types.list_tags_for_resource_request.ListTagsForResourceRequest]",
        ) -> AsyncOperationResponse[
            "capo_b2bi.types.list_tags_for_resource_response.ListTagsForResourceResponse"
        ]:
            import capo_b2bi._operations.b2_bi.list_tags_for_resource

            (
                output,
                http_response,
            ) = await capo_b2bi._operations.b2_bi.list_tags_for_resource.async_list_tags_for_resource(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_b2bi.types.list_tags_for_resource_request.ListTagsForResourceRequest = {
            "resource_arn": resource_arn
        }

        response = await aexecute_pipeline(
            AsyncOperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        await response.response.aclose()
        return response.output

    async def start_transformer_job(
        self,
        input_file: "capo_b2bi.types.s3_location.S3Location",
        output_location: "capo_b2bi.types.s3_location.S3Location",
        transformer_id: "capo_b2bi.types.transformer_id.TransformerId",
        *,
        config_overrides: Optional[Asyncb2biClientConfig] = None,
        client_token: Optional[str] = None,
    ) -> "capo_b2bi.types.start_transformer_job_response.StartTransformerJobResponse":
        """<p>Runs a job, using a transformer, to parse input EDI (electronic data interchange) file into the output structures used by Amazon Web Services B2B Data Interchange.</p> <p>If you only want to transform EDI (electronic data interchange) documents, you don't need to create profiles, partnerships or capabilities. Just create and configure a transformer, and then run the <code>StartTransformerJob</code> API to process your files.</p> <note> <p>The system stores transformer jobs for 30 days. During that period, you can run <a href="https://docs.aws.amazon.com/b2bi/latest/APIReference/API_GetTransformerJob.html">GetTransformerJob</a> and supply its <code>transformerId</code> and <code>transformerJobId</code> to return details of the job.</p> </note>

        Args:
            input_file: <p>Specifies the location of the input file for the transformation. The location consists of an Amazon S3 bucket and prefix.</p>
            output_location: <p>Specifies the location of the output file for the transformation. The location consists of an Amazon S3 bucket and prefix.</p>
            transformer_id: <p>Specifies the system-assigned unique identifier for the transformer.</p>
            client_token: <p>Reserved for future use.</p>

        Raises:
            capo_b2bi.errors.access_denied_exception.AccessDeniedException: <p>You do not have sufficient access to perform this action.</p>
            capo_b2bi.errors.conflict_exception.ConflictException: <p>A conflict exception is thrown when you attempt to delete a resource (such as a profile or a capability) that is being used by other resources.</p>
            capo_b2bi.errors.internal_server_exception.InternalServerException: <p>This exception is thrown when an error occurs in the Amazon Web Services B2B Data Interchange service.</p>
            capo_b2bi.errors.resource_not_found_exception.ResourceNotFoundException: <p>Occurs when the requested resource does not exist, or cannot be found. In some cases, the resource exists in a region other than the region specified in the API call.</p>
            capo_b2bi.errors.throttling_exception.ThrottlingException: <p>The request was denied due to throttling: the data speed and rendering may be limited depending on various parameters and conditions.</p>
            capo_b2bi.errors.validation_exception.ValidationException: <p>Occurs when a B2BI object cannot be validated against a request from another object. This exception can be thrown during standard EDI validation or when custom validation rules fail, such as when element length constraints are violated, invalid codes are used in code list validations, or required elements are missing based on configured element requirement rules.</p>
            capo_b2bi.errors.UnknownServiceError: The service returned an error code this client does not model.

        Examples:
            Sample StartTransformerJob call

            >>> await client.start_transformer_job(client_token='foo', input_file={'bucketName': 'test-bucket', 'key': 'input/inputFile.txt'}, output_location={'bucketName': 'test-bucket', 'key': 'output/'}, transformer_id='tr-974c129999f84d8c9')
        """

        async def _handler(
            req: "AsyncOperationRequest[capo_b2bi.types.start_transformer_job_request.StartTransformerJobRequest]",
        ) -> AsyncOperationResponse[
            "capo_b2bi.types.start_transformer_job_response.StartTransformerJobResponse"
        ]:
            import capo_b2bi._operations.b2_bi.start_transformer_job

            (
                output,
                http_response,
            ) = await capo_b2bi._operations.b2_bi.start_transformer_job.async_start_transformer_job(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_b2bi.types.start_transformer_job_request.StartTransformerJobRequest = {
            "input_file": input_file,
            "output_location": output_location,
            "transformer_id": transformer_id,
        }
        if client_token is None:
            client_token = str(uuid.uuid4())
        input_["client_token"] = client_token

        response = await aexecute_pipeline(
            AsyncOperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        await response.response.aclose()
        return response.output

    async def tag_resource(
        self,
        resource_arn: "capo_b2bi.types.amazon_resource_name.AmazonResourceName",
        tags: "capo_b2bi.types.tag_list.TagList",
        *,
        config_overrides: Optional[Asyncb2biClientConfig] = None,
    ) -> None:
        """<p>Attaches a key-value pair to a resource, as identified by its Amazon Resource Name (ARN). Resources are capability, partnership, profile, transformers and other entities.</p> <p>There is no response returned from this call.</p>

        Args:
            resource_arn: <p>Specifies an Amazon Resource Name (ARN) for a specific Amazon Web Services resource, such as a capability, partnership, profile, or transformer.</p>
            tags: <p>Specifies the key-value pairs assigned to ARNs that you can use to group and search for resources by type. You can attach this metadata to resources (capabilities, partnerships, and so on) for any purpose.</p>

        Raises:
            capo_b2bi.errors.internal_server_exception.InternalServerException: <p>This exception is thrown when an error occurs in the Amazon Web Services B2B Data Interchange service.</p>
            capo_b2bi.errors.resource_not_found_exception.ResourceNotFoundException: <p>Occurs when the requested resource does not exist, or cannot be found. In some cases, the resource exists in a region other than the region specified in the API call.</p>
            capo_b2bi.errors.throttling_exception.ThrottlingException: <p>The request was denied due to throttling: the data speed and rendering may be limited depending on various parameters and conditions.</p>
            capo_b2bi.errors.validation_exception.ValidationException: <p>Occurs when a B2BI object cannot be validated against a request from another object. This exception can be thrown during standard EDI validation or when custom validation rules fail, such as when element length constraints are violated, invalid codes are used in code list validations, or required elements are missing based on configured element requirement rules.</p>
            capo_b2bi.errors.UnknownServiceError: The service returned an error code this client does not model.

        Examples:
            Sample TagResource call

            >>> await client.tag_resource(resource_arn='arn:aws:b2bi:us-west-2:123456789012:profile/p-60fbc37c87f04fce9', tags=[{'Key': 'sampleKey', 'Value': 'SampleValue'}])
        """

        async def _handler(
            req: "AsyncOperationRequest[capo_b2bi.types.tag_resource_request.TagResourceRequest]",
        ) -> AsyncOperationResponse[None]:
            import capo_b2bi._operations.b2_bi.tag_resource

            (
                output,
                http_response,
            ) = await capo_b2bi._operations.b2_bi.tag_resource.async_tag_resource(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_b2bi.types.tag_resource_request.TagResourceRequest = {
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

    async def test_conversion(
        self,
        source: "capo_b2bi.types.conversion_source.ConversionSource",
        target: "capo_b2bi.types.conversion_target.ConversionTarget",
        *,
        config_overrides: Optional[Asyncb2biClientConfig] = None,
    ) -> "capo_b2bi.types.test_conversion_response.TestConversionResponse":
        """<p>This operation mimics the latter half of a typical Outbound EDI request. It takes an input JSON/XML in the B2Bi shape as input, converts it to an X12 EDI string, and return that string.</p>

        Args:
            source: <p>Specify the source file for an outbound EDI request.</p>
            target: <p>Specify the format (X12 is the only currently supported format), and other details for the conversion target.</p>

        Raises:
            capo_b2bi.errors.access_denied_exception.AccessDeniedException: <p>You do not have sufficient access to perform this action.</p>
            capo_b2bi.errors.internal_server_exception.InternalServerException: <p>This exception is thrown when an error occurs in the Amazon Web Services B2B Data Interchange service.</p>
            capo_b2bi.errors.resource_not_found_exception.ResourceNotFoundException: <p>Occurs when the requested resource does not exist, or cannot be found. In some cases, the resource exists in a region other than the region specified in the API call.</p>
            capo_b2bi.errors.throttling_exception.ThrottlingException: <p>The request was denied due to throttling: the data speed and rendering may be limited depending on various parameters and conditions.</p>
            capo_b2bi.errors.validation_exception.ValidationException: <p>Occurs when a B2BI object cannot be validated against a request from another object. This exception can be thrown during standard EDI validation or when custom validation rules fail, such as when element length constraints are violated, invalid codes are used in code list validations, or required elements are missing based on configured element requirement rules.</p>
            capo_b2bi.errors.UnknownServiceError: The service returned an error code this client does not model.

        Examples:
            Sample TestConversion call

            >>> await client.test_conversion(source={'fileFormat': 'JSON', 'inputFile': {'fileContent': 'Sample file content'}}, target={'fileFormat': 'X12', 'formatDetails': {'x12': {'transactionSet': 'X12_110', 'version': 'VERSION_4010'}}, 'advancedOptions': {'x12': {'validationOptions': {'validationRules': [{'codeListValidationRule': {'elementId': '1280', 'codesToAdd': ['X', 'Y', 'Z'], 'codesToRemove': ['A', 'B', 'C']}}, {'elementRequirementValidationRule': {'elementPosition': 'NM1-01', 'requirement': 'OPTIONAL'}}, {'elementLengthValidationRule': {'elementId': '0803', 'maxLength': 30, 'minLength': 5}}]}}}})
        """

        async def _handler(
            req: "AsyncOperationRequest[capo_b2bi.types.test_conversion_request.TestConversionRequest]",
        ) -> AsyncOperationResponse[
            "capo_b2bi.types.test_conversion_response.TestConversionResponse"
        ]:
            import capo_b2bi._operations.b2_bi.test_conversion

            (
                output,
                http_response,
            ) = await capo_b2bi._operations.b2_bi.test_conversion.async_test_conversion(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_b2bi.types.test_conversion_request.TestConversionRequest = {
            "source": source,
            "target": target,
        }

        response = await aexecute_pipeline(
            AsyncOperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        await response.response.aclose()
        return response.output

    async def test_mapping(
        self,
        input_file_content: "capo_b2bi.types.test_mapping_input_file_content.TestMappingInputFileContent",
        mapping_template: "capo_b2bi.types.mapping_template.MappingTemplate",
        file_format: "capo_b2bi.types.file_format.FileFormat",
        *,
        config_overrides: Optional[Asyncb2biClientConfig] = None,
    ) -> "capo_b2bi.types.test_mapping_response.TestMappingResponse":
        """<p>Maps the input file according to the provided template file. The API call downloads the file contents from the Amazon S3 location, and passes the contents in as a string, to the <code>inputFileContent</code> parameter.</p>

        Args:
            input_file_content: <p>Specify the contents of the EDI (electronic data interchange) XML or JSON file that is used as input for the transform.</p>
            mapping_template: <p>Specifies the mapping template for the transformer. This template is used to map the parsed EDI file using JSONata or XSLT.</p> <note> <p>This parameter is available for backwards compatibility. Use the <a href="https://docs.aws.amazon.com/b2bi/latest/APIReference/API_Mapping.html">Mapping</a> data type instead.</p> </note>
            file_format: <p>Specifies that the currently supported file formats for EDI transformations are <code>JSON</code> and <code>XML</code>.</p>

        Raises:
            capo_b2bi.errors.access_denied_exception.AccessDeniedException: <p>You do not have sufficient access to perform this action.</p>
            capo_b2bi.errors.internal_server_exception.InternalServerException: <p>This exception is thrown when an error occurs in the Amazon Web Services B2B Data Interchange service.</p>
            capo_b2bi.errors.resource_not_found_exception.ResourceNotFoundException: <p>Occurs when the requested resource does not exist, or cannot be found. In some cases, the resource exists in a region other than the region specified in the API call.</p>
            capo_b2bi.errors.throttling_exception.ThrottlingException: <p>The request was denied due to throttling: the data speed and rendering may be limited depending on various parameters and conditions.</p>
            capo_b2bi.errors.validation_exception.ValidationException: <p>Occurs when a B2BI object cannot be validated against a request from another object. This exception can be thrown during standard EDI validation or when custom validation rules fail, such as when element length constraints are violated, invalid codes are used in code list validations, or required elements are missing based on configured element requirement rules.</p>
            capo_b2bi.errors.UnknownServiceError: The service returned an error code this client does not model.

        Examples:
            Sample TestMapping call

            >>> await client.test_mapping(file_format='JSON', input_file_content='Sample file content', mapping_template='$')
        """

        async def _handler(
            req: "AsyncOperationRequest[capo_b2bi.types.test_mapping_request.TestMappingRequest]",
        ) -> AsyncOperationResponse[
            "capo_b2bi.types.test_mapping_response.TestMappingResponse"
        ]:
            import capo_b2bi._operations.b2_bi.test_mapping

            (
                output,
                http_response,
            ) = await capo_b2bi._operations.b2_bi.test_mapping.async_test_mapping(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_b2bi.types.test_mapping_request.TestMappingRequest = {
            "input_file_content": input_file_content,
            "mapping_template": mapping_template,
            "file_format": file_format,
        }

        response = await aexecute_pipeline(
            AsyncOperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        await response.response.aclose()
        return response.output

    async def test_parsing(
        self,
        input_file: "capo_b2bi.types.s3_location.S3Location",
        file_format: "capo_b2bi.types.file_format.FileFormat",
        edi_type: "capo_b2bi.types.edi_type.EdiType",
        *,
        config_overrides: Optional[Asyncb2biClientConfig] = None,
        advanced_options: Optional[
            "capo_b2bi.types.advanced_options.AdvancedOptions"
        ] = None,
    ) -> "capo_b2bi.types.test_parsing_response.TestParsingResponse":
        """<p>Parses the input EDI (electronic data interchange) file. The input file has a file size limit of 250 KB.</p>

        Args:
            input_file: <p>Specifies an <code>S3Location</code> object, which contains the Amazon S3 bucket and prefix for the location of the input file.</p>
            file_format: <p>Specifies that the currently supported file formats for EDI transformations are <code>JSON</code> and <code>XML</code>.</p>
            edi_type: <p>Specifies the details for the EDI standard that is being used for the transformer. Currently, only X12 is supported. X12 is a set of standards and corresponding messages that define specific business documents.</p>
            advanced_options: <p>Specifies advanced options for parsing the input EDI file. These options allow for more granular control over the parsing process, including split options for X12 files.</p>

        Raises:
            capo_b2bi.errors.access_denied_exception.AccessDeniedException: <p>You do not have sufficient access to perform this action.</p>
            capo_b2bi.errors.internal_server_exception.InternalServerException: <p>This exception is thrown when an error occurs in the Amazon Web Services B2B Data Interchange service.</p>
            capo_b2bi.errors.resource_not_found_exception.ResourceNotFoundException: <p>Occurs when the requested resource does not exist, or cannot be found. In some cases, the resource exists in a region other than the region specified in the API call.</p>
            capo_b2bi.errors.throttling_exception.ThrottlingException: <p>The request was denied due to throttling: the data speed and rendering may be limited depending on various parameters and conditions.</p>
            capo_b2bi.errors.validation_exception.ValidationException: <p>Occurs when a B2BI object cannot be validated against a request from another object. This exception can be thrown during standard EDI validation or when custom validation rules fail, such as when element length constraints are violated, invalid codes are used in code list validations, or required elements are missing based on configured element requirement rules.</p>
            capo_b2bi.errors.UnknownServiceError: The service returned an error code this client does not model.

        Examples:
            Sample TestParsing call

            >>> await client.test_parsing(edi_type={'x12Details': {'transactionSet': 'X12_110', 'version': 'VERSION_4010'}}, file_format='JSON', input_file={'bucketName': 'test-bucket', 'key': 'sampleFile.txt'})
            Sample TestParsing call without EDI Splitting

            >>> await client.test_parsing(edi_type={'x12Details': {'transactionSet': 'X12_110', 'version': 'VERSION_4010'}}, file_format='JSON', advanced_options={'x12': {'splitOptions': {'splitBy': 'NONE'}}}, input_file={'bucketName': 'test-bucket', 'key': 'sampleFile.txt'})
            Sample TestParsing call with EDI Splitting by Transaction

            >>> await client.test_parsing(edi_type={'x12Details': {'transactionSet': 'X12_110', 'version': 'VERSION_4010'}}, file_format='JSON', advanced_options={'x12': {'splitOptions': {'splitBy': 'TRANSACTION'}}}, input_file={'bucketName': 'test-bucket', 'key': 'sampleFile.txt'})
            Sample TestParsing call with Validation Options

            >>> await client.test_parsing(edi_type={'x12Details': {'transactionSet': 'X12_110', 'version': 'VERSION_4010'}}, file_format='JSON', advanced_options={'x12': {'validationOptions': {'validationRules': [{'codeListValidationRule': {'elementId': '1280', 'codesToAdd': ['X', 'Y', 'Z'], 'codesToRemove': ['A', 'B', 'C']}}, {'elementRequirementValidationRule': {'elementPosition': 'NM1-01', 'requirement': 'OPTIONAL'}}, {'elementLengthValidationRule': {'elementId': '0803', 'maxLength': 30, 'minLength': 5}}]}}}, input_file={'bucketName': 'test-bucket', 'key': 'sampleFile.txt'})
        """

        async def _handler(
            req: "AsyncOperationRequest[capo_b2bi.types.test_parsing_request.TestParsingRequest]",
        ) -> AsyncOperationResponse[
            "capo_b2bi.types.test_parsing_response.TestParsingResponse"
        ]:
            import capo_b2bi._operations.b2_bi.test_parsing

            (
                output,
                http_response,
            ) = await capo_b2bi._operations.b2_bi.test_parsing.async_test_parsing(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_b2bi.types.test_parsing_request.TestParsingRequest = {
            "input_file": input_file,
            "file_format": file_format,
            "edi_type": edi_type,
        }
        if advanced_options is not None:
            input_["advanced_options"] = advanced_options

        response = await aexecute_pipeline(
            AsyncOperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        await response.response.aclose()
        return response.output

    async def untag_resource(
        self,
        resource_arn: "capo_b2bi.types.amazon_resource_name.AmazonResourceName",
        tag_keys: "capo_b2bi.types.tag_key_list.TagKeyList",
        *,
        config_overrides: Optional[Asyncb2biClientConfig] = None,
    ) -> None:
        """<p>Detaches a key-value pair from the specified resource, as identified by its Amazon Resource Name (ARN). Resources are capability, partnership, profile, transformers and other entities.</p>

        Args:
            resource_arn: <p>Specifies an Amazon Resource Name (ARN) for a specific Amazon Web Services resource, such as a capability, partnership, profile, or transformer.</p>
            tag_keys: <p>Specifies the key-value pairs assigned to ARNs that you can use to group and search for resources by type. You can attach this metadata to resources (capabilities, partnerships, and so on) for any purpose.</p>

        Raises:
            capo_b2bi.errors.internal_server_exception.InternalServerException: <p>This exception is thrown when an error occurs in the Amazon Web Services B2B Data Interchange service.</p>
            capo_b2bi.errors.resource_not_found_exception.ResourceNotFoundException: <p>Occurs when the requested resource does not exist, or cannot be found. In some cases, the resource exists in a region other than the region specified in the API call.</p>
            capo_b2bi.errors.validation_exception.ValidationException: <p>Occurs when a B2BI object cannot be validated against a request from another object. This exception can be thrown during standard EDI validation or when custom validation rules fail, such as when element length constraints are violated, invalid codes are used in code list validations, or required elements are missing based on configured element requirement rules.</p>
            capo_b2bi.errors.UnknownServiceError: The service returned an error code this client does not model.

        Examples:
            Sample UntagResource call

            >>> await client.untag_resource(resource_arn='arn:aws:b2bi:us-west-2:123456789012:profile/p-60fbc37c87f04fce9', tag_keys=['sampleKey'])
        """

        async def _handler(
            req: "AsyncOperationRequest[capo_b2bi.types.untag_resource_request.UntagResourceRequest]",
        ) -> AsyncOperationResponse[None]:
            import capo_b2bi._operations.b2_bi.untag_resource

            (
                output,
                http_response,
            ) = await capo_b2bi._operations.b2_bi.untag_resource.async_untag_resource(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_b2bi.types.untag_resource_request.UntagResourceRequest = {
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

    async def create_capability(
        self,
        name: "capo_b2bi.types.capability_name.CapabilityName",
        type: "capo_b2bi.types.capability_type.CapabilityType",
        configuration: "capo_b2bi.types.capability_configuration.CapabilityConfiguration",
        *,
        config_overrides: Optional[Asyncb2biClientConfig] = None,
        instructions_documents: Optional[
            "capo_b2bi.types.instructions_documents.InstructionsDocuments"
        ] = None,
        client_token: Optional[str] = None,
        tags: Optional["capo_b2bi.types.tag_list.TagList"] = None,
    ) -> "capo_b2bi.types.create_capability_response.CreateCapabilityResponse":
        """<p>Instantiates a capability based on the specified parameters. A trading capability contains the information required to transform incoming EDI documents into JSON or XML outputs.</p>

        Args:
            name: <p>Specifies the name of the capability, used to identify it.</p>
            type: <p>Specifies the type of the capability. Currently, only <code>edi</code> is supported.</p>
            configuration: <p>Specifies a structure that contains the details for a capability.</p>
            instructions_documents: <p>Specifies one or more locations in Amazon S3, each specifying an EDI document that can be used with this capability. Each item contains the name of the bucket and the key, to identify the document's location.</p>
            client_token: <p>Reserved for future use.</p>
            tags: <p>Specifies the key-value pairs assigned to ARNs that you can use to group and search for resources by type. You can attach this metadata to resources (capabilities, partnerships, and so on) for any purpose.</p>

        Raises:
            capo_b2bi.errors.access_denied_exception.AccessDeniedException: <p>You do not have sufficient access to perform this action.</p>
            capo_b2bi.errors.conflict_exception.ConflictException: <p>A conflict exception is thrown when you attempt to delete a resource (such as a profile or a capability) that is being used by other resources.</p>
            capo_b2bi.errors.internal_server_exception.InternalServerException: <p>This exception is thrown when an error occurs in the Amazon Web Services B2B Data Interchange service.</p>
            capo_b2bi.errors.resource_not_found_exception.ResourceNotFoundException: <p>Occurs when the requested resource does not exist, or cannot be found. In some cases, the resource exists in a region other than the region specified in the API call.</p>
            capo_b2bi.errors.service_quota_exceeded_exception.ServiceQuotaExceededException: <p>Occurs when the calling command attempts to exceed one of the service quotas, for example trying to create a capability when you already have the maximum number of capabilities allowed.</p>
            capo_b2bi.errors.throttling_exception.ThrottlingException: <p>The request was denied due to throttling: the data speed and rendering may be limited depending on various parameters and conditions.</p>
            capo_b2bi.errors.validation_exception.ValidationException: <p>Occurs when a B2BI object cannot be validated against a request from another object. This exception can be thrown during standard EDI validation or when custom validation rules fail, such as when element length constraints are violated, invalid codes are used in code list validations, or required elements are missing based on configured element requirement rules.</p>
            capo_b2bi.errors.UnknownServiceError: The service returned an error code this client does not model.

        Examples:
            Sample CreateCapability call

            >>> await client.create_capability(name='b2biexample', type='edi', configuration={'edi': {'type': {'x12Details': {'transactionSet': 'X12_110', 'version': 'VERSION_4010'}}, 'inputLocation': {'bucketName': 'test-bucket', 'key': 'input/'}, 'outputLocation': {'bucketName': 'test-bucket', 'key': 'output/'}, 'transformerId': 'tr-9a893cf536df4658b'}}, instructions_documents=[{'bucketName': 'test-bucket', 'key': 'instructiondoc.txt'}], client_token='foo', tags=[{'Key': 'capabilityKey1', 'Value': 'capabilityValue1'}])
        """

        async def _handler(
            req: "AsyncOperationRequest[capo_b2bi.types.create_capability_request.CreateCapabilityRequest]",
        ) -> AsyncOperationResponse[
            "capo_b2bi.types.create_capability_response.CreateCapabilityResponse"
        ]:
            import capo_b2bi._operations.b2_bi.create_capability

            (
                output,
                http_response,
            ) = await capo_b2bi._operations.b2_bi.create_capability.async_create_capability(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_b2bi.types.create_capability_request.CreateCapabilityRequest = {
            "name": name,
            "type": type,
            "configuration": configuration,
        }
        if instructions_documents is not None:
            input_["instructions_documents"] = instructions_documents
        if client_token is None:
            client_token = str(uuid.uuid4())
        input_["client_token"] = client_token
        if tags is not None:
            input_["tags"] = tags

        response = await aexecute_pipeline(
            AsyncOperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        await response.response.aclose()
        return response.output

    async def get_capability(
        self,
        capability_id: "capo_b2bi.types.capability_id.CapabilityId",
        *,
        config_overrides: Optional[Asyncb2biClientConfig] = None,
    ) -> "capo_b2bi.types.get_capability_response.GetCapabilityResponse":
        """<p>Retrieves the details for the specified capability. A trading capability contains the information required to transform incoming EDI documents into JSON or XML outputs.</p>

        Args:
            capability_id: <p>Specifies a system-assigned unique identifier for the capability.</p>

        Raises:
            capo_b2bi.errors.access_denied_exception.AccessDeniedException: <p>You do not have sufficient access to perform this action.</p>
            capo_b2bi.errors.internal_server_exception.InternalServerException: <p>This exception is thrown when an error occurs in the Amazon Web Services B2B Data Interchange service.</p>
            capo_b2bi.errors.resource_not_found_exception.ResourceNotFoundException: <p>Occurs when the requested resource does not exist, or cannot be found. In some cases, the resource exists in a region other than the region specified in the API call.</p>
            capo_b2bi.errors.throttling_exception.ThrottlingException: <p>The request was denied due to throttling: the data speed and rendering may be limited depending on various parameters and conditions.</p>
            capo_b2bi.errors.validation_exception.ValidationException: <p>Occurs when a B2BI object cannot be validated against a request from another object. This exception can be thrown during standard EDI validation or when custom validation rules fail, such as when element length constraints are violated, invalid codes are used in code list validations, or required elements are missing based on configured element requirement rules.</p>
            capo_b2bi.errors.UnknownServiceError: The service returned an error code this client does not model.

        Examples:
            Sample GetCapabilty call

            >>> await client.get_capability(capability_id='ca-963a8121e4fc4e348')
        """

        async def _handler(
            req: "AsyncOperationRequest[capo_b2bi.types.get_capability_request.GetCapabilityRequest]",
        ) -> AsyncOperationResponse[
            "capo_b2bi.types.get_capability_response.GetCapabilityResponse"
        ]:
            import capo_b2bi._operations.b2_bi.get_capability

            (
                output,
                http_response,
            ) = await capo_b2bi._operations.b2_bi.get_capability.async_get_capability(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_b2bi.types.get_capability_request.GetCapabilityRequest = {
            "capability_id": capability_id
        }

        response = await aexecute_pipeline(
            AsyncOperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        await response.response.aclose()
        return response.output

    async def update_capability(
        self,
        capability_id: "capo_b2bi.types.capability_id.CapabilityId",
        *,
        config_overrides: Optional[Asyncb2biClientConfig] = None,
        name: Optional["capo_b2bi.types.capability_name.CapabilityName"] = None,
        configuration: Optional[
            "capo_b2bi.types.capability_configuration.CapabilityConfiguration"
        ] = None,
        instructions_documents: Optional[
            "capo_b2bi.types.instructions_documents.InstructionsDocuments"
        ] = None,
    ) -> "capo_b2bi.types.update_capability_response.UpdateCapabilityResponse":
        """<p>Updates some of the parameters for a capability, based on the specified parameters. A trading capability contains the information required to transform incoming EDI documents into JSON or XML outputs.</p>

        Args:
            capability_id: <p>Specifies a system-assigned unique identifier for the capability.</p>
            name: <p>Specifies a new name for the capability, to replace the existing name.</p>
            configuration: <p>Specifies a structure that contains the details for a capability.</p>
            instructions_documents: <p>Specifies one or more locations in Amazon S3, each specifying an EDI document that can be used with this capability. Each item contains the name of the bucket and the key, to identify the document's location.</p>

        Raises:
            capo_b2bi.errors.access_denied_exception.AccessDeniedException: <p>You do not have sufficient access to perform this action.</p>
            capo_b2bi.errors.conflict_exception.ConflictException: <p>A conflict exception is thrown when you attempt to delete a resource (such as a profile or a capability) that is being used by other resources.</p>
            capo_b2bi.errors.internal_server_exception.InternalServerException: <p>This exception is thrown when an error occurs in the Amazon Web Services B2B Data Interchange service.</p>
            capo_b2bi.errors.resource_not_found_exception.ResourceNotFoundException: <p>Occurs when the requested resource does not exist, or cannot be found. In some cases, the resource exists in a region other than the region specified in the API call.</p>
            capo_b2bi.errors.service_quota_exceeded_exception.ServiceQuotaExceededException: <p>Occurs when the calling command attempts to exceed one of the service quotas, for example trying to create a capability when you already have the maximum number of capabilities allowed.</p>
            capo_b2bi.errors.throttling_exception.ThrottlingException: <p>The request was denied due to throttling: the data speed and rendering may be limited depending on various parameters and conditions.</p>
            capo_b2bi.errors.validation_exception.ValidationException: <p>Occurs when a B2BI object cannot be validated against a request from another object. This exception can be thrown during standard EDI validation or when custom validation rules fail, such as when element length constraints are violated, invalid codes are used in code list validations, or required elements are missing based on configured element requirement rules.</p>
            capo_b2bi.errors.UnknownServiceError: The service returned an error code this client does not model.

        Examples:
            Sample UpdateCapability call

            >>> await client.update_capability(capability_id='ca-963a8121e4fc4e348', name='b2biexample', instructions_documents=[{'bucketName': 'test-bucket', 'key': 'instructiondoc.txt'}], configuration={'edi': {'type': {'x12Details': {'transactionSet': 'X12_110', 'version': 'VERSION_4010'}}, 'inputLocation': {'bucketName': 'test-bucket', 'key': 'input/'}, 'outputLocation': {'bucketName': 'test-bucket', 'key': 'output/'}, 'transformerId': 'tr-9a893cf536df4658b'}})
        """

        async def _handler(
            req: "AsyncOperationRequest[capo_b2bi.types.update_capability_request.UpdateCapabilityRequest]",
        ) -> AsyncOperationResponse[
            "capo_b2bi.types.update_capability_response.UpdateCapabilityResponse"
        ]:
            import capo_b2bi._operations.b2_bi.update_capability

            (
                output,
                http_response,
            ) = await capo_b2bi._operations.b2_bi.update_capability.async_update_capability(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_b2bi.types.update_capability_request.UpdateCapabilityRequest = {
            "capability_id": capability_id
        }
        if name is not None:
            input_["name"] = name
        if configuration is not None:
            input_["configuration"] = configuration
        if instructions_documents is not None:
            input_["instructions_documents"] = instructions_documents

        response = await aexecute_pipeline(
            AsyncOperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        await response.response.aclose()
        return response.output

    async def delete_capability(
        self,
        capability_id: "capo_b2bi.types.capability_id.CapabilityId",
        *,
        config_overrides: Optional[Asyncb2biClientConfig] = None,
    ) -> None:
        """<p>Deletes the specified capability. A trading capability contains the information required to transform incoming EDI documents into JSON or XML outputs.</p>

        Args:
            capability_id: <p>Specifies a system-assigned unique identifier for the capability.</p>

        Raises:
            capo_b2bi.errors.access_denied_exception.AccessDeniedException: <p>You do not have sufficient access to perform this action.</p>
            capo_b2bi.errors.conflict_exception.ConflictException: <p>A conflict exception is thrown when you attempt to delete a resource (such as a profile or a capability) that is being used by other resources.</p>
            capo_b2bi.errors.internal_server_exception.InternalServerException: <p>This exception is thrown when an error occurs in the Amazon Web Services B2B Data Interchange service.</p>
            capo_b2bi.errors.resource_not_found_exception.ResourceNotFoundException: <p>Occurs when the requested resource does not exist, or cannot be found. In some cases, the resource exists in a region other than the region specified in the API call.</p>
            capo_b2bi.errors.throttling_exception.ThrottlingException: <p>The request was denied due to throttling: the data speed and rendering may be limited depending on various parameters and conditions.</p>
            capo_b2bi.errors.validation_exception.ValidationException: <p>Occurs when a B2BI object cannot be validated against a request from another object. This exception can be thrown during standard EDI validation or when custom validation rules fail, such as when element length constraints are violated, invalid codes are used in code list validations, or required elements are missing based on configured element requirement rules.</p>
            capo_b2bi.errors.UnknownServiceError: The service returned an error code this client does not model.

        Examples:
            Sample DeleteCapabilty call

            >>> await client.delete_capability(capability_id='ca-963a8121e4fc4e348')
        """

        async def _handler(
            req: "AsyncOperationRequest[capo_b2bi.types.delete_capability_request.DeleteCapabilityRequest]",
        ) -> AsyncOperationResponse[None]:
            import capo_b2bi._operations.b2_bi.delete_capability

            (
                output,
                http_response,
            ) = await capo_b2bi._operations.b2_bi.delete_capability.async_delete_capability(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_b2bi.types.delete_capability_request.DeleteCapabilityRequest = {
            "capability_id": capability_id
        }

        response = await aexecute_pipeline(
            AsyncOperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        await response.response.aclose()
        return response.output

    async def list_capabilities(
        self,
        *,
        config_overrides: Optional[Asyncb2biClientConfig] = None,
        next_token: Optional["capo_b2bi.types.page_token.PageToken"] = None,
        max_results: Optional["capo_b2bi.types.max_results.MaxResults"] = None,
    ) -> "capo_b2bi.types.list_capabilities_response.ListCapabilitiesResponse":
        """<p>Lists the capabilities associated with your Amazon Web Services account for your current or specified region. A trading capability contains the information required to transform incoming EDI documents into JSON or XML outputs.</p>

        Args:
            next_token: <p>When additional results are obtained from the command, a <code>NextToken</code> parameter is returned in the output. You can then pass the <code>NextToken</code> parameter in a subsequent command to continue listing additional resources.</p>
            max_results: <p>Specifies the maximum number of capabilities to return.</p>

        Raises:
            capo_b2bi.errors.access_denied_exception.AccessDeniedException: <p>You do not have sufficient access to perform this action.</p>
            capo_b2bi.errors.internal_server_exception.InternalServerException: <p>This exception is thrown when an error occurs in the Amazon Web Services B2B Data Interchange service.</p>
            capo_b2bi.errors.throttling_exception.ThrottlingException: <p>The request was denied due to throttling: the data speed and rendering may be limited depending on various parameters and conditions.</p>
            capo_b2bi.errors.validation_exception.ValidationException: <p>Occurs when a B2BI object cannot be validated against a request from another object. This exception can be thrown during standard EDI validation or when custom validation rules fail, such as when element length constraints are violated, invalid codes are used in code list validations, or required elements are missing based on configured element requirement rules.</p>
            capo_b2bi.errors.UnknownServiceError: The service returned an error code this client does not model.

        Examples:
            Sample ListCapabilities call

            >>> await client.list_capabilities(max_results=50, next_token='foo')
        """

        async def _handler(
            req: "AsyncOperationRequest[capo_b2bi.types.list_capabilities_request.ListCapabilitiesRequest]",
        ) -> AsyncOperationResponse[
            "capo_b2bi.types.list_capabilities_response.ListCapabilitiesResponse"
        ]:
            import capo_b2bi._operations.b2_bi.list_capabilities

            (
                output,
                http_response,
            ) = await capo_b2bi._operations.b2_bi.list_capabilities.async_list_capabilities(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_b2bi.types.list_capabilities_request.ListCapabilitiesRequest = {}
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

    async def iter_list_capabilities(
        self,
        *,
        config_overrides: Optional[Asyncb2biClientConfig] = None,
        next_token: Optional["capo_b2bi.types.page_token.PageToken"] = None,
        max_results: Optional["capo_b2bi.types.max_results.MaxResults"] = None,
    ) -> "AsyncIterator[capo_b2bi.types.capability_summary.CapabilitySummary]":
        _token = next_token
        while True:
            _response = await self.list_capabilities(
                config_overrides=config_overrides,
                next_token=_token,
                max_results=max_results,
            )
            _page = _resolve_path(_response, ("capabilities",))
            for _item in _page or []:
                yield _item
            _token = _resolve_path(_response, ("next_token",))
            if not _token:
                break

    async def create_partnership(
        self,
        profile_id: "capo_b2bi.types.profile_id.ProfileId",
        name: "capo_b2bi.types.partner_name.PartnerName",
        email: "capo_b2bi.types.email.Email",
        capabilities: "capo_b2bi.types.partnership_capabilities.PartnershipCapabilities",
        *,
        config_overrides: Optional[Asyncb2biClientConfig] = None,
        phone: Optional["capo_b2bi.types.phone.Phone"] = None,
        capability_options: Optional[
            "capo_b2bi.types.capability_options.CapabilityOptions"
        ] = None,
        client_token: Optional[str] = None,
        tags: Optional["capo_b2bi.types.tag_list.TagList"] = None,
    ) -> "capo_b2bi.types.create_partnership_response.CreatePartnershipResponse":
        """<p>Creates a partnership between a customer and a trading partner, based on the supplied parameters. A partnership represents the connection between you and your trading partner. It ties together a profile and one or more trading capabilities.</p>

        Args:
            profile_id: <p>Specifies the unique, system-generated identifier for the profile connected to this partnership.</p>
            name: <p>Specifies a descriptive name for the partnership.</p>
            email: <p>Specifies the email address associated with this trading partner.</p>
            phone: <p>Specifies the phone number associated with the partnership.</p>
            capabilities: <p>Specifies a list of the capabilities associated with this partnership.</p>
            capability_options: <p>Specify the structure that contains the details for the associated capabilities.</p>
            client_token: <p>Reserved for future use.</p>
            tags: <p>Specifies the key-value pairs assigned to ARNs that you can use to group and search for resources by type. You can attach this metadata to resources (capabilities, partnerships, and so on) for any purpose.</p>

        Raises:
            capo_b2bi.errors.access_denied_exception.AccessDeniedException: <p>You do not have sufficient access to perform this action.</p>
            capo_b2bi.errors.conflict_exception.ConflictException: <p>A conflict exception is thrown when you attempt to delete a resource (such as a profile or a capability) that is being used by other resources.</p>
            capo_b2bi.errors.internal_server_exception.InternalServerException: <p>This exception is thrown when an error occurs in the Amazon Web Services B2B Data Interchange service.</p>
            capo_b2bi.errors.resource_not_found_exception.ResourceNotFoundException: <p>Occurs when the requested resource does not exist, or cannot be found. In some cases, the resource exists in a region other than the region specified in the API call.</p>
            capo_b2bi.errors.service_quota_exceeded_exception.ServiceQuotaExceededException: <p>Occurs when the calling command attempts to exceed one of the service quotas, for example trying to create a capability when you already have the maximum number of capabilities allowed.</p>
            capo_b2bi.errors.throttling_exception.ThrottlingException: <p>The request was denied due to throttling: the data speed and rendering may be limited depending on various parameters and conditions.</p>
            capo_b2bi.errors.validation_exception.ValidationException: <p>Occurs when a B2BI object cannot be validated against a request from another object. This exception can be thrown during standard EDI validation or when custom validation rules fail, such as when element length constraints are violated, invalid codes are used in code list validations, or required elements are missing based on configured element requirement rules.</p>
            capo_b2bi.errors.UnknownServiceError: The service returned an error code this client does not model.

        Examples:
            Sample CreatePartnership call

            >>> await client.create_partnership(capabilities=['ca-963a8121e4fc4e348'], client_token='foo', email='john@example.com', name='b2bipartner', phone='5555555555', profile_id='p-60fbc37c87f04fce9', tags=[{'Key': 'sampleKey1', 'Value': 'sampleValue1'}])
        """

        async def _handler(
            req: "AsyncOperationRequest[capo_b2bi.types.create_partnership_request.CreatePartnershipRequest]",
        ) -> AsyncOperationResponse[
            "capo_b2bi.types.create_partnership_response.CreatePartnershipResponse"
        ]:
            import capo_b2bi._operations.b2_bi.create_partnership

            (
                output,
                http_response,
            ) = await capo_b2bi._operations.b2_bi.create_partnership.async_create_partnership(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_b2bi.types.create_partnership_request.CreatePartnershipRequest = {
            "profile_id": profile_id,
            "name": name,
            "email": email,
            "capabilities": capabilities,
        }
        if phone is not None:
            input_["phone"] = phone
        if capability_options is not None:
            input_["capability_options"] = capability_options
        if client_token is None:
            client_token = str(uuid.uuid4())
        input_["client_token"] = client_token
        if tags is not None:
            input_["tags"] = tags

        response = await aexecute_pipeline(
            AsyncOperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        await response.response.aclose()
        return response.output

    async def get_partnership(
        self,
        partnership_id: "capo_b2bi.types.partnership_id.PartnershipId",
        *,
        config_overrides: Optional[Asyncb2biClientConfig] = None,
    ) -> "capo_b2bi.types.get_partnership_response.GetPartnershipResponse":
        """<p>Retrieves the details for a partnership, based on the partner and profile IDs specified. A partnership represents the connection between you and your trading partner. It ties together a profile and one or more trading capabilities.</p>

        Args:
            partnership_id: <p>Specifies the unique, system-generated identifier for a partnership.</p>

        Raises:
            capo_b2bi.errors.access_denied_exception.AccessDeniedException: <p>You do not have sufficient access to perform this action.</p>
            capo_b2bi.errors.internal_server_exception.InternalServerException: <p>This exception is thrown when an error occurs in the Amazon Web Services B2B Data Interchange service.</p>
            capo_b2bi.errors.resource_not_found_exception.ResourceNotFoundException: <p>Occurs when the requested resource does not exist, or cannot be found. In some cases, the resource exists in a region other than the region specified in the API call.</p>
            capo_b2bi.errors.throttling_exception.ThrottlingException: <p>The request was denied due to throttling: the data speed and rendering may be limited depending on various parameters and conditions.</p>
            capo_b2bi.errors.validation_exception.ValidationException: <p>Occurs when a B2BI object cannot be validated against a request from another object. This exception can be thrown during standard EDI validation or when custom validation rules fail, such as when element length constraints are violated, invalid codes are used in code list validations, or required elements are missing based on configured element requirement rules.</p>
            capo_b2bi.errors.UnknownServiceError: The service returned an error code this client does not model.

        Examples:
            Sample GetPartnership call

            >>> await client.get_partnership(partnership_id='ps-219fa02f5b4242af8')
        """

        async def _handler(
            req: "AsyncOperationRequest[capo_b2bi.types.get_partnership_request.GetPartnershipRequest]",
        ) -> AsyncOperationResponse[
            "capo_b2bi.types.get_partnership_response.GetPartnershipResponse"
        ]:
            import capo_b2bi._operations.b2_bi.get_partnership

            (
                output,
                http_response,
            ) = await capo_b2bi._operations.b2_bi.get_partnership.async_get_partnership(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_b2bi.types.get_partnership_request.GetPartnershipRequest = {
            "partnership_id": partnership_id
        }

        response = await aexecute_pipeline(
            AsyncOperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        await response.response.aclose()
        return response.output

    async def update_partnership(
        self,
        partnership_id: "capo_b2bi.types.partnership_id.PartnershipId",
        *,
        config_overrides: Optional[Asyncb2biClientConfig] = None,
        name: Optional["capo_b2bi.types.partner_name.PartnerName"] = None,
        capabilities: Optional[
            "capo_b2bi.types.partnership_capabilities.PartnershipCapabilities"
        ] = None,
        capability_options: Optional[
            "capo_b2bi.types.capability_options.CapabilityOptions"
        ] = None,
    ) -> "capo_b2bi.types.update_partnership_response.UpdatePartnershipResponse":
        """<p>Updates some of the parameters for a partnership between a customer and trading partner. A partnership represents the connection between you and your trading partner. It ties together a profile and one or more trading capabilities.</p>

        Args:
            partnership_id: <p>Specifies the unique, system-generated identifier for a partnership.</p>
            name: <p>The name of the partnership, used to identify it.</p>
            capabilities: <p>List of the capabilities associated with this partnership.</p>
            capability_options: <p>To update, specify the structure that contains the details for the associated capabilities.</p>

        Raises:
            capo_b2bi.errors.access_denied_exception.AccessDeniedException: <p>You do not have sufficient access to perform this action.</p>
            capo_b2bi.errors.conflict_exception.ConflictException: <p>A conflict exception is thrown when you attempt to delete a resource (such as a profile or a capability) that is being used by other resources.</p>
            capo_b2bi.errors.internal_server_exception.InternalServerException: <p>This exception is thrown when an error occurs in the Amazon Web Services B2B Data Interchange service.</p>
            capo_b2bi.errors.resource_not_found_exception.ResourceNotFoundException: <p>Occurs when the requested resource does not exist, or cannot be found. In some cases, the resource exists in a region other than the region specified in the API call.</p>
            capo_b2bi.errors.service_quota_exceeded_exception.ServiceQuotaExceededException: <p>Occurs when the calling command attempts to exceed one of the service quotas, for example trying to create a capability when you already have the maximum number of capabilities allowed.</p>
            capo_b2bi.errors.throttling_exception.ThrottlingException: <p>The request was denied due to throttling: the data speed and rendering may be limited depending on various parameters and conditions.</p>
            capo_b2bi.errors.validation_exception.ValidationException: <p>Occurs when a B2BI object cannot be validated against a request from another object. This exception can be thrown during standard EDI validation or when custom validation rules fail, such as when element length constraints are violated, invalid codes are used in code list validations, or required elements are missing based on configured element requirement rules.</p>
            capo_b2bi.errors.UnknownServiceError: The service returned an error code this client does not model.

        Examples:
            Sample UpdatePartnership call

            >>> await client.update_partnership(capabilities=['ca-963a8121e4fc4e348'], name='b2bipartner', partnership_id='ps-219fa02f5b4242af8')
        """

        async def _handler(
            req: "AsyncOperationRequest[capo_b2bi.types.update_partnership_request.UpdatePartnershipRequest]",
        ) -> AsyncOperationResponse[
            "capo_b2bi.types.update_partnership_response.UpdatePartnershipResponse"
        ]:
            import capo_b2bi._operations.b2_bi.update_partnership

            (
                output,
                http_response,
            ) = await capo_b2bi._operations.b2_bi.update_partnership.async_update_partnership(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_b2bi.types.update_partnership_request.UpdatePartnershipRequest = {
            "partnership_id": partnership_id
        }
        if name is not None:
            input_["name"] = name
        if capabilities is not None:
            input_["capabilities"] = capabilities
        if capability_options is not None:
            input_["capability_options"] = capability_options

        response = await aexecute_pipeline(
            AsyncOperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        await response.response.aclose()
        return response.output

    async def delete_partnership(
        self,
        partnership_id: "capo_b2bi.types.partnership_id.PartnershipId",
        *,
        config_overrides: Optional[Asyncb2biClientConfig] = None,
    ) -> None:
        """<p>Deletes the specified partnership. A partnership represents the connection between you and your trading partner. It ties together a profile and one or more trading capabilities.</p>

        Args:
            partnership_id: <p>Specifies the unique, system-generated identifier for a partnership.</p>

        Raises:
            capo_b2bi.errors.access_denied_exception.AccessDeniedException: <p>You do not have sufficient access to perform this action.</p>
            capo_b2bi.errors.conflict_exception.ConflictException: <p>A conflict exception is thrown when you attempt to delete a resource (such as a profile or a capability) that is being used by other resources.</p>
            capo_b2bi.errors.internal_server_exception.InternalServerException: <p>This exception is thrown when an error occurs in the Amazon Web Services B2B Data Interchange service.</p>
            capo_b2bi.errors.resource_not_found_exception.ResourceNotFoundException: <p>Occurs when the requested resource does not exist, or cannot be found. In some cases, the resource exists in a region other than the region specified in the API call.</p>
            capo_b2bi.errors.throttling_exception.ThrottlingException: <p>The request was denied due to throttling: the data speed and rendering may be limited depending on various parameters and conditions.</p>
            capo_b2bi.errors.validation_exception.ValidationException: <p>Occurs when a B2BI object cannot be validated against a request from another object. This exception can be thrown during standard EDI validation or when custom validation rules fail, such as when element length constraints are violated, invalid codes are used in code list validations, or required elements are missing based on configured element requirement rules.</p>
            capo_b2bi.errors.UnknownServiceError: The service returned an error code this client does not model.

        Examples:
            Sample DeletePartnership call

            >>> await client.delete_partnership(partnership_id='ps-219fa02f5b4242af8')
        """

        async def _handler(
            req: "AsyncOperationRequest[capo_b2bi.types.delete_partnership_request.DeletePartnershipRequest]",
        ) -> AsyncOperationResponse[None]:
            import capo_b2bi._operations.b2_bi.delete_partnership

            (
                output,
                http_response,
            ) = await capo_b2bi._operations.b2_bi.delete_partnership.async_delete_partnership(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_b2bi.types.delete_partnership_request.DeletePartnershipRequest = {
            "partnership_id": partnership_id
        }

        response = await aexecute_pipeline(
            AsyncOperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        await response.response.aclose()
        return response.output

    async def list_partnerships(
        self,
        *,
        config_overrides: Optional[Asyncb2biClientConfig] = None,
        profile_id: Optional["capo_b2bi.types.profile_id.ProfileId"] = None,
        next_token: Optional["capo_b2bi.types.page_token.PageToken"] = None,
        max_results: Optional["capo_b2bi.types.max_results.MaxResults"] = None,
    ) -> "capo_b2bi.types.list_partnerships_response.ListPartnershipsResponse":
        """<p>Lists the partnerships associated with your Amazon Web Services account for your current or specified region. A partnership represents the connection between you and your trading partner. It ties together a profile and one or more trading capabilities.</p>

        Args:
            profile_id: <p>Specifies the unique, system-generated identifier for the profile connected to this partnership.</p>
            next_token: <p>When additional results are obtained from the command, a <code>NextToken</code> parameter is returned in the output. You can then pass the <code>NextToken</code> parameter in a subsequent command to continue listing additional resources.</p>
            max_results: <p>Specifies the maximum number of capabilities to return.</p>

        Raises:
            capo_b2bi.errors.access_denied_exception.AccessDeniedException: <p>You do not have sufficient access to perform this action.</p>
            capo_b2bi.errors.internal_server_exception.InternalServerException: <p>This exception is thrown when an error occurs in the Amazon Web Services B2B Data Interchange service.</p>
            capo_b2bi.errors.resource_not_found_exception.ResourceNotFoundException: <p>Occurs when the requested resource does not exist, or cannot be found. In some cases, the resource exists in a region other than the region specified in the API call.</p>
            capo_b2bi.errors.throttling_exception.ThrottlingException: <p>The request was denied due to throttling: the data speed and rendering may be limited depending on various parameters and conditions.</p>
            capo_b2bi.errors.validation_exception.ValidationException: <p>Occurs when a B2BI object cannot be validated against a request from another object. This exception can be thrown during standard EDI validation or when custom validation rules fail, such as when element length constraints are violated, invalid codes are used in code list validations, or required elements are missing based on configured element requirement rules.</p>
            capo_b2bi.errors.UnknownServiceError: The service returned an error code this client does not model.

        Examples:
            Sample ListPartnerships call

            >>> await client.list_partnerships(max_results=50, next_token='foo', profile_id='p-60fbc37c87f04fce9')
        """

        async def _handler(
            req: "AsyncOperationRequest[capo_b2bi.types.list_partnerships_request.ListPartnershipsRequest]",
        ) -> AsyncOperationResponse[
            "capo_b2bi.types.list_partnerships_response.ListPartnershipsResponse"
        ]:
            import capo_b2bi._operations.b2_bi.list_partnerships

            (
                output,
                http_response,
            ) = await capo_b2bi._operations.b2_bi.list_partnerships.async_list_partnerships(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_b2bi.types.list_partnerships_request.ListPartnershipsRequest = {}
        if profile_id is not None:
            input_["profile_id"] = profile_id
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

    async def iter_list_partnerships(
        self,
        *,
        config_overrides: Optional[Asyncb2biClientConfig] = None,
        profile_id: Optional["capo_b2bi.types.profile_id.ProfileId"] = None,
        next_token: Optional["capo_b2bi.types.page_token.PageToken"] = None,
        max_results: Optional["capo_b2bi.types.max_results.MaxResults"] = None,
    ) -> "AsyncIterator[capo_b2bi.types.partnership_summary.PartnershipSummary]":
        _token = next_token
        while True:
            _response = await self.list_partnerships(
                config_overrides=config_overrides,
                profile_id=profile_id,
                next_token=_token,
                max_results=max_results,
            )
            _page = _resolve_path(_response, ("partnerships",))
            for _item in _page or []:
                yield _item
            _token = _resolve_path(_response, ("next_token",))
            if not _token:
                break

    async def create_profile(
        self,
        name: "capo_b2bi.types.profile_name.ProfileName",
        phone: "capo_b2bi.types.phone.Phone",
        business_name: "capo_b2bi.types.business_name.BusinessName",
        logging: "capo_b2bi.types.logging.Logging",
        *,
        config_overrides: Optional[Asyncb2biClientConfig] = None,
        email: Optional["capo_b2bi.types.email.Email"] = None,
        client_token: Optional[str] = None,
        tags: Optional["capo_b2bi.types.tag_list.TagList"] = None,
    ) -> "capo_b2bi.types.create_profile_response.CreateProfileResponse":
        """<p>Creates a customer profile. You can have up to five customer profiles, each representing a distinct private network. A profile is the mechanism used to create the concept of a private network.</p>

        Args:
            name: <p>Specifies the name of the profile.</p>
            email: <p>Specifies the email address associated with this customer profile.</p>
            phone: <p>Specifies the phone number associated with the profile.</p>
            business_name: <p>Specifies the name for the business associated with this profile.</p>
            logging: <p>Specifies whether or not logging is enabled for this profile.</p>
            client_token: <p>Reserved for future use.</p>
            tags: <p>Specifies the key-value pairs assigned to ARNs that you can use to group and search for resources by type. You can attach this metadata to resources (capabilities, partnerships, and so on) for any purpose.</p>

        Raises:
            capo_b2bi.errors.access_denied_exception.AccessDeniedException: <p>You do not have sufficient access to perform this action.</p>
            capo_b2bi.errors.conflict_exception.ConflictException: <p>A conflict exception is thrown when you attempt to delete a resource (such as a profile or a capability) that is being used by other resources.</p>
            capo_b2bi.errors.internal_server_exception.InternalServerException: <p>This exception is thrown when an error occurs in the Amazon Web Services B2B Data Interchange service.</p>
            capo_b2bi.errors.resource_not_found_exception.ResourceNotFoundException: <p>Occurs when the requested resource does not exist, or cannot be found. In some cases, the resource exists in a region other than the region specified in the API call.</p>
            capo_b2bi.errors.service_quota_exceeded_exception.ServiceQuotaExceededException: <p>Occurs when the calling command attempts to exceed one of the service quotas, for example trying to create a capability when you already have the maximum number of capabilities allowed.</p>
            capo_b2bi.errors.throttling_exception.ThrottlingException: <p>The request was denied due to throttling: the data speed and rendering may be limited depending on various parameters and conditions.</p>
            capo_b2bi.errors.validation_exception.ValidationException: <p>Occurs when a B2BI object cannot be validated against a request from another object. This exception can be thrown during standard EDI validation or when custom validation rules fail, such as when element length constraints are violated, invalid codes are used in code list validations, or required elements are missing based on configured element requirement rules.</p>
            capo_b2bi.errors.UnknownServiceError: The service returned an error code this client does not model.

        Examples:
            Sample CreateProfile call

            >>> await client.create_profile(business_name="John's Shipping", client_token='foo', email='john@example.com', logging='ENABLED', name='Shipping Profile', phone='5555555555', tags=[{'Key': 'sampleKey', 'Value': 'sampleValue'}])
        """

        async def _handler(
            req: "AsyncOperationRequest[capo_b2bi.types.create_profile_request.CreateProfileRequest]",
        ) -> AsyncOperationResponse[
            "capo_b2bi.types.create_profile_response.CreateProfileResponse"
        ]:
            import capo_b2bi._operations.b2_bi.create_profile

            (
                output,
                http_response,
            ) = await capo_b2bi._operations.b2_bi.create_profile.async_create_profile(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_b2bi.types.create_profile_request.CreateProfileRequest = {
            "name": name,
            "phone": phone,
            "business_name": business_name,
            "logging": logging,
        }
        if email is not None:
            input_["email"] = email
        if client_token is None:
            client_token = str(uuid.uuid4())
        input_["client_token"] = client_token
        if tags is not None:
            input_["tags"] = tags

        response = await aexecute_pipeline(
            AsyncOperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        await response.response.aclose()
        return response.output

    async def get_profile(
        self,
        profile_id: "capo_b2bi.types.profile_id.ProfileId",
        *,
        config_overrides: Optional[Asyncb2biClientConfig] = None,
    ) -> "capo_b2bi.types.get_profile_response.GetProfileResponse":
        """<p>Retrieves the details for the profile specified by the profile ID. A profile is the mechanism used to create the concept of a private network.</p>

        Args:
            profile_id: <p>Specifies the unique, system-generated identifier for the profile.</p>

        Raises:
            capo_b2bi.errors.access_denied_exception.AccessDeniedException: <p>You do not have sufficient access to perform this action.</p>
            capo_b2bi.errors.internal_server_exception.InternalServerException: <p>This exception is thrown when an error occurs in the Amazon Web Services B2B Data Interchange service.</p>
            capo_b2bi.errors.resource_not_found_exception.ResourceNotFoundException: <p>Occurs when the requested resource does not exist, or cannot be found. In some cases, the resource exists in a region other than the region specified in the API call.</p>
            capo_b2bi.errors.throttling_exception.ThrottlingException: <p>The request was denied due to throttling: the data speed and rendering may be limited depending on various parameters and conditions.</p>
            capo_b2bi.errors.validation_exception.ValidationException: <p>Occurs when a B2BI object cannot be validated against a request from another object. This exception can be thrown during standard EDI validation or when custom validation rules fail, such as when element length constraints are violated, invalid codes are used in code list validations, or required elements are missing based on configured element requirement rules.</p>
            capo_b2bi.errors.UnknownServiceError: The service returned an error code this client does not model.

        Examples:
            Sample GetProfile call

            >>> await client.get_profile(profile_id='p-60fbc37c87f04fce9')
        """

        async def _handler(
            req: "AsyncOperationRequest[capo_b2bi.types.get_profile_request.GetProfileRequest]",
        ) -> AsyncOperationResponse[
            "capo_b2bi.types.get_profile_response.GetProfileResponse"
        ]:
            import capo_b2bi._operations.b2_bi.get_profile

            (
                output,
                http_response,
            ) = await capo_b2bi._operations.b2_bi.get_profile.async_get_profile(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_b2bi.types.get_profile_request.GetProfileRequest = {
            "profile_id": profile_id
        }

        response = await aexecute_pipeline(
            AsyncOperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        await response.response.aclose()
        return response.output

    async def update_profile(
        self,
        profile_id: "capo_b2bi.types.profile_id.ProfileId",
        *,
        config_overrides: Optional[Asyncb2biClientConfig] = None,
        name: Optional["capo_b2bi.types.profile_name.ProfileName"] = None,
        email: Optional["capo_b2bi.types.email.Email"] = None,
        phone: Optional["capo_b2bi.types.phone.Phone"] = None,
        business_name: Optional["capo_b2bi.types.business_name.BusinessName"] = None,
    ) -> "capo_b2bi.types.update_profile_response.UpdateProfileResponse":
        """<p>Updates the specified parameters for a profile. A profile is the mechanism used to create the concept of a private network.</p>

        Args:
            profile_id: <p>Specifies the unique, system-generated identifier for the profile.</p>
            name: <p>The name of the profile, used to identify it.</p>
            email: <p>Specifies the email address associated with this customer profile.</p>
            phone: <p>Specifies the phone number associated with the profile.</p>
            business_name: <p>Specifies the name for the business associated with this profile.</p>

        Raises:
            capo_b2bi.errors.access_denied_exception.AccessDeniedException: <p>You do not have sufficient access to perform this action.</p>
            capo_b2bi.errors.conflict_exception.ConflictException: <p>A conflict exception is thrown when you attempt to delete a resource (such as a profile or a capability) that is being used by other resources.</p>
            capo_b2bi.errors.internal_server_exception.InternalServerException: <p>This exception is thrown when an error occurs in the Amazon Web Services B2B Data Interchange service.</p>
            capo_b2bi.errors.resource_not_found_exception.ResourceNotFoundException: <p>Occurs when the requested resource does not exist, or cannot be found. In some cases, the resource exists in a region other than the region specified in the API call.</p>
            capo_b2bi.errors.service_quota_exceeded_exception.ServiceQuotaExceededException: <p>Occurs when the calling command attempts to exceed one of the service quotas, for example trying to create a capability when you already have the maximum number of capabilities allowed.</p>
            capo_b2bi.errors.throttling_exception.ThrottlingException: <p>The request was denied due to throttling: the data speed and rendering may be limited depending on various parameters and conditions.</p>
            capo_b2bi.errors.validation_exception.ValidationException: <p>Occurs when a B2BI object cannot be validated against a request from another object. This exception can be thrown during standard EDI validation or when custom validation rules fail, such as when element length constraints are violated, invalid codes are used in code list validations, or required elements are missing based on configured element requirement rules.</p>
            capo_b2bi.errors.UnknownServiceError: The service returned an error code this client does not model.

        Examples:
            Sample UpdateProfile call

            >>> await client.update_profile(business_name="John's Shipping", email='john@example.com', name='Shipping Profile', phone='5555555555', profile_id='p-60fbc37c87f04fce9')
        """

        async def _handler(
            req: "AsyncOperationRequest[capo_b2bi.types.update_profile_request.UpdateProfileRequest]",
        ) -> AsyncOperationResponse[
            "capo_b2bi.types.update_profile_response.UpdateProfileResponse"
        ]:
            import capo_b2bi._operations.b2_bi.update_profile

            (
                output,
                http_response,
            ) = await capo_b2bi._operations.b2_bi.update_profile.async_update_profile(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_b2bi.types.update_profile_request.UpdateProfileRequest = {
            "profile_id": profile_id
        }
        if name is not None:
            input_["name"] = name
        if email is not None:
            input_["email"] = email
        if phone is not None:
            input_["phone"] = phone
        if business_name is not None:
            input_["business_name"] = business_name

        response = await aexecute_pipeline(
            AsyncOperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        await response.response.aclose()
        return response.output

    async def delete_profile(
        self,
        profile_id: "capo_b2bi.types.profile_id.ProfileId",
        *,
        config_overrides: Optional[Asyncb2biClientConfig] = None,
    ) -> None:
        """<p>Deletes the specified profile. A profile is the mechanism used to create the concept of a private network.</p>

        Args:
            profile_id: <p>Specifies the unique, system-generated identifier for the profile.</p>

        Raises:
            capo_b2bi.errors.access_denied_exception.AccessDeniedException: <p>You do not have sufficient access to perform this action.</p>
            capo_b2bi.errors.conflict_exception.ConflictException: <p>A conflict exception is thrown when you attempt to delete a resource (such as a profile or a capability) that is being used by other resources.</p>
            capo_b2bi.errors.internal_server_exception.InternalServerException: <p>This exception is thrown when an error occurs in the Amazon Web Services B2B Data Interchange service.</p>
            capo_b2bi.errors.resource_not_found_exception.ResourceNotFoundException: <p>Occurs when the requested resource does not exist, or cannot be found. In some cases, the resource exists in a region other than the region specified in the API call.</p>
            capo_b2bi.errors.throttling_exception.ThrottlingException: <p>The request was denied due to throttling: the data speed and rendering may be limited depending on various parameters and conditions.</p>
            capo_b2bi.errors.validation_exception.ValidationException: <p>Occurs when a B2BI object cannot be validated against a request from another object. This exception can be thrown during standard EDI validation or when custom validation rules fail, such as when element length constraints are violated, invalid codes are used in code list validations, or required elements are missing based on configured element requirement rules.</p>
            capo_b2bi.errors.UnknownServiceError: The service returned an error code this client does not model.

        Examples:
            Sample DeleteProfile call

            >>> await client.delete_profile(profile_id='p-60fbc37c87f04fce9')
        """

        async def _handler(
            req: "AsyncOperationRequest[capo_b2bi.types.delete_profile_request.DeleteProfileRequest]",
        ) -> AsyncOperationResponse[None]:
            import capo_b2bi._operations.b2_bi.delete_profile

            (
                output,
                http_response,
            ) = await capo_b2bi._operations.b2_bi.delete_profile.async_delete_profile(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_b2bi.types.delete_profile_request.DeleteProfileRequest = {
            "profile_id": profile_id
        }

        response = await aexecute_pipeline(
            AsyncOperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        await response.response.aclose()
        return response.output

    async def list_profiles(
        self,
        *,
        config_overrides: Optional[Asyncb2biClientConfig] = None,
        next_token: Optional["capo_b2bi.types.page_token.PageToken"] = None,
        max_results: Optional["capo_b2bi.types.max_results.MaxResults"] = None,
    ) -> "capo_b2bi.types.list_profiles_response.ListProfilesResponse":
        """<p>Lists the profiles associated with your Amazon Web Services account for your current or specified region. A profile is the mechanism used to create the concept of a private network.</p>

        Args:
            next_token: <p>When additional results are obtained from the command, a <code>NextToken</code> parameter is returned in the output. You can then pass the <code>NextToken</code> parameter in a subsequent command to continue listing additional resources.</p>
            max_results: <p>Specifies the maximum number of profiles to return.</p>

        Raises:
            capo_b2bi.errors.access_denied_exception.AccessDeniedException: <p>You do not have sufficient access to perform this action.</p>
            capo_b2bi.errors.internal_server_exception.InternalServerException: <p>This exception is thrown when an error occurs in the Amazon Web Services B2B Data Interchange service.</p>
            capo_b2bi.errors.throttling_exception.ThrottlingException: <p>The request was denied due to throttling: the data speed and rendering may be limited depending on various parameters and conditions.</p>
            capo_b2bi.errors.validation_exception.ValidationException: <p>Occurs when a B2BI object cannot be validated against a request from another object. This exception can be thrown during standard EDI validation or when custom validation rules fail, such as when element length constraints are violated, invalid codes are used in code list validations, or required elements are missing based on configured element requirement rules.</p>
            capo_b2bi.errors.UnknownServiceError: The service returned an error code this client does not model.

        Examples:
            Sample ListProfiles call

            >>> await client.list_profiles(max_results=50, next_token='foo')
        """

        async def _handler(
            req: "AsyncOperationRequest[capo_b2bi.types.list_profiles_request.ListProfilesRequest]",
        ) -> AsyncOperationResponse[
            "capo_b2bi.types.list_profiles_response.ListProfilesResponse"
        ]:
            import capo_b2bi._operations.b2_bi.list_profiles

            (
                output,
                http_response,
            ) = await capo_b2bi._operations.b2_bi.list_profiles.async_list_profiles(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_b2bi.types.list_profiles_request.ListProfilesRequest = {}
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

    async def iter_list_profiles(
        self,
        *,
        config_overrides: Optional[Asyncb2biClientConfig] = None,
        next_token: Optional["capo_b2bi.types.page_token.PageToken"] = None,
        max_results: Optional["capo_b2bi.types.max_results.MaxResults"] = None,
    ) -> "AsyncIterator[capo_b2bi.types.profile_summary.ProfileSummary]":
        _token = next_token
        while True:
            _response = await self.list_profiles(
                config_overrides=config_overrides,
                next_token=_token,
                max_results=max_results,
            )
            _page = _resolve_path(_response, ("profiles",))
            for _item in _page or []:
                yield _item
            _token = _resolve_path(_response, ("next_token",))
            if not _token:
                break

    async def create_transformer(
        self,
        name: "capo_b2bi.types.transformer_name.TransformerName",
        *,
        config_overrides: Optional[Asyncb2biClientConfig] = None,
        client_token: Optional[str] = None,
        tags: Optional["capo_b2bi.types.tag_list.TagList"] = None,
        file_format: Optional["capo_b2bi.types.file_format.FileFormat"] = None,
        mapping_template: Optional[
            "capo_b2bi.types.mapping_template.MappingTemplate"
        ] = None,
        edi_type: Optional["capo_b2bi.types.edi_type.EdiType"] = None,
        sample_document: Optional["capo_b2bi.types.file_location.FileLocation"] = None,
        input_conversion: Optional[
            "capo_b2bi.types.input_conversion.InputConversion"
        ] = None,
        mapping: Optional["capo_b2bi.types.mapping.Mapping"] = None,
        output_conversion: Optional[
            "capo_b2bi.types.output_conversion.OutputConversion"
        ] = None,
        sample_documents: Optional[
            "capo_b2bi.types.sample_documents.SampleDocuments"
        ] = None,
    ) -> "capo_b2bi.types.create_transformer_response.CreateTransformerResponse":
        """<p>Creates a transformer. Amazon Web Services B2B Data Interchange currently supports two scenarios:</p> <ul> <li> <p> <i>Inbound EDI</i>: the Amazon Web Services customer receives an EDI file from their trading partner. Amazon Web Services B2B Data Interchange converts this EDI file into a JSON or XML file with a service-defined structure. A mapping template provided by the customer, in JSONata or XSLT format, is optionally applied to this file to produce a JSON or XML file with the structure the customer requires.</p> </li> <li> <p> <i>Outbound EDI</i>: the Amazon Web Services customer has a JSON or XML file containing data that they wish to use in an EDI file. A mapping template, provided by the customer (in either JSONata or XSLT format) is applied to this file to generate a JSON or XML file in the service-defined structure. This file is then converted to an EDI file.</p> </li> </ul> <note> <p>The following fields are provided for backwards compatibility only: <code>fileFormat</code>, <code>mappingTemplate</code>, <code>ediType</code>, and <code>sampleDocument</code>.</p> <ul> <li> <p>Use the <code>mapping</code> data type in place of <code>mappingTemplate</code> and <code>fileFormat</code> </p> </li> <li> <p>Use the <code>sampleDocuments</code> data type in place of <code>sampleDocument</code> </p> </li> <li> <p>Use either the <code>inputConversion</code> or <code>outputConversion</code> in place of <code>ediType</code> </p> </li> </ul> </note>

        Args:
            name: <p>Specifies the name of the transformer, used to identify it.</p>
            client_token: <p>Reserved for future use.</p>
            tags: <p>Specifies the key-value pairs assigned to ARNs that you can use to group and search for resources by type. You can attach this metadata to resources (capabilities, partnerships, and so on) for any purpose.</p>
            file_format: <p>Specifies that the currently supported file formats for EDI transformations are <code>JSON</code> and <code>XML</code>.</p>
            mapping_template: <p>Specifies the mapping template for the transformer. This template is used to map the parsed EDI file using JSONata or XSLT.</p> <note> <p>This parameter is available for backwards compatibility. Use the <a href="https://docs.aws.amazon.com/b2bi/latest/APIReference/API_Mapping.html">Mapping</a> data type instead.</p> </note>
            edi_type: <p>Specifies the details for the EDI standard that is being used for the transformer. Currently, only X12 is supported. X12 is a set of standards and corresponding messages that define specific business documents.</p>
            sample_document: <p>Specifies a sample EDI document that is used by a transformer as a guide for processing the EDI data.</p>
            input_conversion: <p>Specify the <code>InputConversion</code> object, which contains the format options for the inbound transformation.</p>
            mapping: <p>Specify the structure that contains the mapping template and its language (either XSLT or JSONATA).</p>
            output_conversion: <p>A structure that contains the <code>OutputConversion</code> object, which contains the format options for the outbound transformation.</p>
            sample_documents: <p>Specify a structure that contains the Amazon S3 bucket and an array of the corresponding keys used to identify the location for your sample documents.</p>

        Raises:
            capo_b2bi.errors.access_denied_exception.AccessDeniedException: <p>You do not have sufficient access to perform this action.</p>
            capo_b2bi.errors.conflict_exception.ConflictException: <p>A conflict exception is thrown when you attempt to delete a resource (such as a profile or a capability) that is being used by other resources.</p>
            capo_b2bi.errors.internal_server_exception.InternalServerException: <p>This exception is thrown when an error occurs in the Amazon Web Services B2B Data Interchange service.</p>
            capo_b2bi.errors.resource_not_found_exception.ResourceNotFoundException: <p>Occurs when the requested resource does not exist, or cannot be found. In some cases, the resource exists in a region other than the region specified in the API call.</p>
            capo_b2bi.errors.service_quota_exceeded_exception.ServiceQuotaExceededException: <p>Occurs when the calling command attempts to exceed one of the service quotas, for example trying to create a capability when you already have the maximum number of capabilities allowed.</p>
            capo_b2bi.errors.throttling_exception.ThrottlingException: <p>The request was denied due to throttling: the data speed and rendering may be limited depending on various parameters and conditions.</p>
            capo_b2bi.errors.validation_exception.ValidationException: <p>Occurs when a B2BI object cannot be validated against a request from another object. This exception can be thrown during standard EDI validation or when custom validation rules fail, such as when element length constraints are violated, invalid codes are used in code list validations, or required elements are missing based on configured element requirement rules.</p>
            capo_b2bi.errors.UnknownServiceError: The service returned an error code this client does not model.

        Examples:
            Sample CreateTransformer call

            >>> await client.create_transformer(client_token='foo', name='transformX12', input_conversion={'fromFormat': 'X12', 'formatOptions': {'x12': {'transactionSet': 'X12_110', 'version': 'VERSION_4010'}}, 'advancedOptions': {'x12': {'splitOptions': {'splitBy': 'NONE'}, 'validationOptions': {'validationRules': [{'codeListValidationRule': {'elementId': '1234', 'codesToAdd': ['A', 'B', 'C'], 'codesToRemove': ['X', 'Y', 'Z']}}, {'elementRequirementValidationRule': {'elementPosition': 'NM1-01', 'requirement': 'MANDATORY'}}, {'elementLengthValidationRule': {'elementId': '5678', 'maxLength': 10, 'minLength': 2}}]}}}}, mapping={'templateLanguage': 'JSONATA', 'template': '{}'}, sample_documents={'bucketName': 'test-bucket', 'keys': [{'input': 'sampleDoc.txt'}]}, tags=[{'Key': 'sampleKey', 'Value': 'sampleValue'}])
        """

        async def _handler(
            req: "AsyncOperationRequest[capo_b2bi.types.create_transformer_request.CreateTransformerRequest]",
        ) -> AsyncOperationResponse[
            "capo_b2bi.types.create_transformer_response.CreateTransformerResponse"
        ]:
            import capo_b2bi._operations.b2_bi.create_transformer

            (
                output,
                http_response,
            ) = await capo_b2bi._operations.b2_bi.create_transformer.async_create_transformer(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_b2bi.types.create_transformer_request.CreateTransformerRequest = {
            "name": name
        }
        if client_token is None:
            client_token = str(uuid.uuid4())
        input_["client_token"] = client_token
        if tags is not None:
            input_["tags"] = tags
        if file_format is not None:
            input_["file_format"] = file_format
        if mapping_template is not None:
            input_["mapping_template"] = mapping_template
        if edi_type is not None:
            input_["edi_type"] = edi_type
        if sample_document is not None:
            input_["sample_document"] = sample_document
        if input_conversion is not None:
            input_["input_conversion"] = input_conversion
        if mapping is not None:
            input_["mapping"] = mapping
        if output_conversion is not None:
            input_["output_conversion"] = output_conversion
        if sample_documents is not None:
            input_["sample_documents"] = sample_documents

        response = await aexecute_pipeline(
            AsyncOperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        await response.response.aclose()
        return response.output

    async def get_transformer(
        self,
        transformer_id: "capo_b2bi.types.transformer_id.TransformerId",
        *,
        config_overrides: Optional[Asyncb2biClientConfig] = None,
    ) -> "capo_b2bi.types.get_transformer_response.GetTransformerResponse":
        """<p>Retrieves the details for the transformer specified by the transformer ID. A transformer can take an EDI file as input and transform it into a JSON-or XML-formatted document. Alternatively, a transformer can take a JSON-or XML-formatted document as input and transform it into an EDI file.</p>

        Args:
            transformer_id: <p>Specifies the system-assigned unique identifier for the transformer.</p>

        Raises:
            capo_b2bi.errors.access_denied_exception.AccessDeniedException: <p>You do not have sufficient access to perform this action.</p>
            capo_b2bi.errors.internal_server_exception.InternalServerException: <p>This exception is thrown when an error occurs in the Amazon Web Services B2B Data Interchange service.</p>
            capo_b2bi.errors.resource_not_found_exception.ResourceNotFoundException: <p>Occurs when the requested resource does not exist, or cannot be found. In some cases, the resource exists in a region other than the region specified in the API call.</p>
            capo_b2bi.errors.throttling_exception.ThrottlingException: <p>The request was denied due to throttling: the data speed and rendering may be limited depending on various parameters and conditions.</p>
            capo_b2bi.errors.validation_exception.ValidationException: <p>Occurs when a B2BI object cannot be validated against a request from another object. This exception can be thrown during standard EDI validation or when custom validation rules fail, such as when element length constraints are violated, invalid codes are used in code list validations, or required elements are missing based on configured element requirement rules.</p>
            capo_b2bi.errors.UnknownServiceError: The service returned an error code this client does not model.

        Examples:
            Sample GetTransformer call

            >>> await client.get_transformer(transformer_id='tr-974c129999f84d8c9')
        """

        async def _handler(
            req: "AsyncOperationRequest[capo_b2bi.types.get_transformer_request.GetTransformerRequest]",
        ) -> AsyncOperationResponse[
            "capo_b2bi.types.get_transformer_response.GetTransformerResponse"
        ]:
            import capo_b2bi._operations.b2_bi.get_transformer

            (
                output,
                http_response,
            ) = await capo_b2bi._operations.b2_bi.get_transformer.async_get_transformer(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_b2bi.types.get_transformer_request.GetTransformerRequest = {
            "transformer_id": transformer_id
        }

        response = await aexecute_pipeline(
            AsyncOperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        await response.response.aclose()
        return response.output

    async def update_transformer(
        self,
        transformer_id: "capo_b2bi.types.transformer_id.TransformerId",
        *,
        config_overrides: Optional[Asyncb2biClientConfig] = None,
        name: Optional["capo_b2bi.types.transformer_name.TransformerName"] = None,
        status: Optional["capo_b2bi.types.transformer_status.TransformerStatus"] = None,
        file_format: Optional["capo_b2bi.types.file_format.FileFormat"] = None,
        mapping_template: Optional[
            "capo_b2bi.types.mapping_template.MappingTemplate"
        ] = None,
        edi_type: Optional["capo_b2bi.types.edi_type.EdiType"] = None,
        sample_document: Optional["capo_b2bi.types.file_location.FileLocation"] = None,
        input_conversion: Optional[
            "capo_b2bi.types.input_conversion.InputConversion"
        ] = None,
        mapping: Optional["capo_b2bi.types.mapping.Mapping"] = None,
        output_conversion: Optional[
            "capo_b2bi.types.output_conversion.OutputConversion"
        ] = None,
        sample_documents: Optional[
            "capo_b2bi.types.sample_documents.SampleDocuments"
        ] = None,
    ) -> "capo_b2bi.types.update_transformer_response.UpdateTransformerResponse":
        """<p>Updates the specified parameters for a transformer. A transformer can take an EDI file as input and transform it into a JSON-or XML-formatted document. Alternatively, a transformer can take a JSON-or XML-formatted document as input and transform it into an EDI file.</p>

        Args:
            transformer_id: <p>Specifies the system-assigned unique identifier for the transformer.</p>
            name: <p>Specify a new name for the transformer, if you want to update it.</p>
            status: <p>Specifies the transformer's status. You can update the state of the transformer from <code>inactive</code> to <code>active</code>.</p>
            file_format: <p>Specifies that the currently supported file formats for EDI transformations are <code>JSON</code> and <code>XML</code>.</p>
            mapping_template: <p>Specifies the mapping template for the transformer. This template is used to map the parsed EDI file using JSONata or XSLT.</p> <note> <p>This parameter is available for backwards compatibility. Use the <a href="https://docs.aws.amazon.com/b2bi/latest/APIReference/API_Mapping.html">Mapping</a> data type instead.</p> </note>
            edi_type: <p>Specifies the details for the EDI standard that is being used for the transformer. Currently, only X12 is supported. X12 is a set of standards and corresponding messages that define specific business documents.</p>
            sample_document: <p>Specifies a sample EDI document that is used by a transformer as a guide for processing the EDI data.</p>
            input_conversion: <p>To update, specify the <code>InputConversion</code> object, which contains the format options for the inbound transformation.</p>
            mapping: <p>Specify the structure that contains the mapping template and its language (either XSLT or JSONATA).</p>
            output_conversion: <p>To update, specify the <code>OutputConversion</code> object, which contains the format options for the outbound transformation.</p>
            sample_documents: <p>Specify a structure that contains the Amazon S3 bucket and an array of the corresponding keys used to identify the location for your sample documents.</p>

        Raises:
            capo_b2bi.errors.access_denied_exception.AccessDeniedException: <p>You do not have sufficient access to perform this action.</p>
            capo_b2bi.errors.conflict_exception.ConflictException: <p>A conflict exception is thrown when you attempt to delete a resource (such as a profile or a capability) that is being used by other resources.</p>
            capo_b2bi.errors.internal_server_exception.InternalServerException: <p>This exception is thrown when an error occurs in the Amazon Web Services B2B Data Interchange service.</p>
            capo_b2bi.errors.resource_not_found_exception.ResourceNotFoundException: <p>Occurs when the requested resource does not exist, or cannot be found. In some cases, the resource exists in a region other than the region specified in the API call.</p>
            capo_b2bi.errors.service_quota_exceeded_exception.ServiceQuotaExceededException: <p>Occurs when the calling command attempts to exceed one of the service quotas, for example trying to create a capability when you already have the maximum number of capabilities allowed.</p>
            capo_b2bi.errors.throttling_exception.ThrottlingException: <p>The request was denied due to throttling: the data speed and rendering may be limited depending on various parameters and conditions.</p>
            capo_b2bi.errors.validation_exception.ValidationException: <p>Occurs when a B2BI object cannot be validated against a request from another object. This exception can be thrown during standard EDI validation or when custom validation rules fail, such as when element length constraints are violated, invalid codes are used in code list validations, or required elements are missing based on configured element requirement rules.</p>
            capo_b2bi.errors.UnknownServiceError: The service returned an error code this client does not model.

        Examples:
            Sample UpdateTransformer call

            >>> await client.update_transformer(input_conversion={'fromFormat': 'X12', 'formatOptions': {'x12': {'transactionSet': 'X12_110', 'version': 'VERSION_4010'}}, 'advancedOptions': {'x12': {'splitOptions': {'splitBy': 'NONE'}, 'validationOptions': {'validationRules': [{'codeListValidationRule': {'elementId': '1234', 'codesToAdd': ['A', 'B', 'C'], 'codesToRemove': ['X', 'Y', 'Z']}}, {'elementRequirementValidationRule': {'elementPosition': 'NM1-01', 'requirement': 'MANDATORY'}}, {'elementLengthValidationRule': {'elementId': '5678', 'maxLength': 10, 'minLength': 2}}]}}}}, mapping={'templateLanguage': 'JSONATA', 'template': '{}'}, sample_documents={'bucketName': 'test-bucket', 'keys': [{'input': 'sampleDoc.txt'}]}, name='transformX12', status='inactive', transformer_id='tr-974c129999f84d8c9')
        """

        async def _handler(
            req: "AsyncOperationRequest[capo_b2bi.types.update_transformer_request.UpdateTransformerRequest]",
        ) -> AsyncOperationResponse[
            "capo_b2bi.types.update_transformer_response.UpdateTransformerResponse"
        ]:
            import capo_b2bi._operations.b2_bi.update_transformer

            (
                output,
                http_response,
            ) = await capo_b2bi._operations.b2_bi.update_transformer.async_update_transformer(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_b2bi.types.update_transformer_request.UpdateTransformerRequest = {
            "transformer_id": transformer_id
        }
        if name is not None:
            input_["name"] = name
        if status is not None:
            input_["status"] = status
        if file_format is not None:
            input_["file_format"] = file_format
        if mapping_template is not None:
            input_["mapping_template"] = mapping_template
        if edi_type is not None:
            input_["edi_type"] = edi_type
        if sample_document is not None:
            input_["sample_document"] = sample_document
        if input_conversion is not None:
            input_["input_conversion"] = input_conversion
        if mapping is not None:
            input_["mapping"] = mapping
        if output_conversion is not None:
            input_["output_conversion"] = output_conversion
        if sample_documents is not None:
            input_["sample_documents"] = sample_documents

        response = await aexecute_pipeline(
            AsyncOperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        await response.response.aclose()
        return response.output

    async def delete_transformer(
        self,
        transformer_id: "capo_b2bi.types.transformer_id.TransformerId",
        *,
        config_overrides: Optional[Asyncb2biClientConfig] = None,
    ) -> None:
        """<p>Deletes the specified transformer. A transformer can take an EDI file as input and transform it into a JSON-or XML-formatted document. Alternatively, a transformer can take a JSON-or XML-formatted document as input and transform it into an EDI file.</p>

        Args:
            transformer_id: <p>Specifies the system-assigned unique identifier for the transformer.</p>

        Raises:
            capo_b2bi.errors.access_denied_exception.AccessDeniedException: <p>You do not have sufficient access to perform this action.</p>
            capo_b2bi.errors.conflict_exception.ConflictException: <p>A conflict exception is thrown when you attempt to delete a resource (such as a profile or a capability) that is being used by other resources.</p>
            capo_b2bi.errors.internal_server_exception.InternalServerException: <p>This exception is thrown when an error occurs in the Amazon Web Services B2B Data Interchange service.</p>
            capo_b2bi.errors.resource_not_found_exception.ResourceNotFoundException: <p>Occurs when the requested resource does not exist, or cannot be found. In some cases, the resource exists in a region other than the region specified in the API call.</p>
            capo_b2bi.errors.throttling_exception.ThrottlingException: <p>The request was denied due to throttling: the data speed and rendering may be limited depending on various parameters and conditions.</p>
            capo_b2bi.errors.validation_exception.ValidationException: <p>Occurs when a B2BI object cannot be validated against a request from another object. This exception can be thrown during standard EDI validation or when custom validation rules fail, such as when element length constraints are violated, invalid codes are used in code list validations, or required elements are missing based on configured element requirement rules.</p>
            capo_b2bi.errors.UnknownServiceError: The service returned an error code this client does not model.

        Examples:
            Sample DeleteTransformer call

            >>> await client.delete_transformer(transformer_id='tr-974c129999f84d8c9')
        """

        async def _handler(
            req: "AsyncOperationRequest[capo_b2bi.types.delete_transformer_request.DeleteTransformerRequest]",
        ) -> AsyncOperationResponse[None]:
            import capo_b2bi._operations.b2_bi.delete_transformer

            (
                output,
                http_response,
            ) = await capo_b2bi._operations.b2_bi.delete_transformer.async_delete_transformer(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_b2bi.types.delete_transformer_request.DeleteTransformerRequest = {
            "transformer_id": transformer_id
        }

        response = await aexecute_pipeline(
            AsyncOperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        await response.response.aclose()
        return response.output

    async def list_transformers(
        self,
        *,
        config_overrides: Optional[Asyncb2biClientConfig] = None,
        next_token: Optional["capo_b2bi.types.page_token.PageToken"] = None,
        max_results: Optional["capo_b2bi.types.max_results.MaxResults"] = None,
    ) -> "capo_b2bi.types.list_transformers_response.ListTransformersResponse":
        """<p>Lists the available transformers. A transformer can take an EDI file as input and transform it into a JSON-or XML-formatted document. Alternatively, a transformer can take a JSON-or XML-formatted document as input and transform it into an EDI file.</p>

        Args:
            next_token: <p>When additional results are obtained from the command, a <code>NextToken</code> parameter is returned in the output. You can then pass the <code>NextToken</code> parameter in a subsequent command to continue listing additional resources.</p>
            max_results: <p>Specifies the number of items to return for the API response.</p>

        Raises:
            capo_b2bi.errors.access_denied_exception.AccessDeniedException: <p>You do not have sufficient access to perform this action.</p>
            capo_b2bi.errors.internal_server_exception.InternalServerException: <p>This exception is thrown when an error occurs in the Amazon Web Services B2B Data Interchange service.</p>
            capo_b2bi.errors.throttling_exception.ThrottlingException: <p>The request was denied due to throttling: the data speed and rendering may be limited depending on various parameters and conditions.</p>
            capo_b2bi.errors.validation_exception.ValidationException: <p>Occurs when a B2BI object cannot be validated against a request from another object. This exception can be thrown during standard EDI validation or when custom validation rules fail, such as when element length constraints are violated, invalid codes are used in code list validations, or required elements are missing based on configured element requirement rules.</p>
            capo_b2bi.errors.UnknownServiceError: The service returned an error code this client does not model.

        Examples:
            Sample ListTransformers call

            >>> await client.list_transformers(max_results=50, next_token='foo')
        """

        async def _handler(
            req: "AsyncOperationRequest[capo_b2bi.types.list_transformers_request.ListTransformersRequest]",
        ) -> AsyncOperationResponse[
            "capo_b2bi.types.list_transformers_response.ListTransformersResponse"
        ]:
            import capo_b2bi._operations.b2_bi.list_transformers

            (
                output,
                http_response,
            ) = await capo_b2bi._operations.b2_bi.list_transformers.async_list_transformers(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_b2bi.types.list_transformers_request.ListTransformersRequest = {}
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

    async def iter_list_transformers(
        self,
        *,
        config_overrides: Optional[Asyncb2biClientConfig] = None,
        next_token: Optional["capo_b2bi.types.page_token.PageToken"] = None,
        max_results: Optional["capo_b2bi.types.max_results.MaxResults"] = None,
    ) -> "AsyncIterator[capo_b2bi.types.transformer_summary.TransformerSummary]":
        _token = next_token
        while True:
            _response = await self.list_transformers(
                config_overrides=config_overrides,
                next_token=_token,
                max_results=max_results,
            )
            _page = _resolve_path(_response, ("transformers",))
            for _item in _page or []:
                yield _item
            _token = _resolve_path(_response, ("next_token",))
            if not _token:
                break

    async def __aenter__(self) -> Self:
        return self

    async def __aexit__(self, exc_type: Any, exc: Any, tb: Any):
        await self._client.aclose()
