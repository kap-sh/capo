"""Generated from Smithy shape ``com.amazonaws.taxsettings#TaxSettings``."""

import warnings
from collections.abc import AsyncIterator
from typing import TYPE_CHECKING, Any, Iterable, Optional

from typing_extensions import Self, TypedDict
from zapros import AsyncBaseHandler, AsyncClient

import capo_taxsettings._auth._signers
import capo_taxsettings._auth._sigv4
from capo_taxsettings._auth._identity import Credentials
from capo_taxsettings._auth._providers import (
    CredentialsProvider,
    IdentityProvider,
    StaticAwsCredentialsProvider,
    default_aws_credentials_chain,
)
from capo_taxsettings._auth._zapros_handler import AuthMiddleware
from capo_taxsettings._pagination import resolve_path as _resolve_path
from capo_taxsettings._services._aws_config import aaws_config
from capo_taxsettings._services._pipeline import (
    AsyncInterceptor,
    AsyncOperationOptions,
    AsyncOperationRequest,
    AsyncOperationResponse,
    aexecute_pipeline,
    aretry,
)

if TYPE_CHECKING:
    import capo_taxsettings.types.account_details
    import capo_taxsettings.types.account_id
    import capo_taxsettings.types.account_ids
    import capo_taxsettings.types.authority
    import capo_taxsettings.types.batch_delete_tax_registration_request
    import capo_taxsettings.types.batch_delete_tax_registration_response
    import capo_taxsettings.types.batch_get_tax_exemptions_request
    import capo_taxsettings.types.batch_get_tax_exemptions_response
    import capo_taxsettings.types.batch_put_tax_registration_request
    import capo_taxsettings.types.batch_put_tax_registration_response
    import capo_taxsettings.types.delete_supplemental_tax_registration_request
    import capo_taxsettings.types.delete_supplemental_tax_registration_response
    import capo_taxsettings.types.delete_tax_registration_request
    import capo_taxsettings.types.delete_tax_registration_response
    import capo_taxsettings.types.destination_s3_location
    import capo_taxsettings.types.exemption_certificate
    import capo_taxsettings.types.generic_string
    import capo_taxsettings.types.get_tax_exemption_types_request
    import capo_taxsettings.types.get_tax_exemption_types_response
    import capo_taxsettings.types.get_tax_inheritance_request
    import capo_taxsettings.types.get_tax_inheritance_response
    import capo_taxsettings.types.get_tax_registration_document_request
    import capo_taxsettings.types.get_tax_registration_document_response
    import capo_taxsettings.types.get_tax_registration_request
    import capo_taxsettings.types.get_tax_registration_response
    import capo_taxsettings.types.heritage_status
    import capo_taxsettings.types.list_supplemental_tax_registrations_request
    import capo_taxsettings.types.list_supplemental_tax_registrations_response
    import capo_taxsettings.types.list_tax_exemptions_request
    import capo_taxsettings.types.list_tax_exemptions_response
    import capo_taxsettings.types.list_tax_registrations_request
    import capo_taxsettings.types.list_tax_registrations_response
    import capo_taxsettings.types.max_results
    import capo_taxsettings.types.pagination_token_string
    import capo_taxsettings.types.put_supplemental_tax_registration_request
    import capo_taxsettings.types.put_supplemental_tax_registration_response
    import capo_taxsettings.types.put_tax_exemption_request
    import capo_taxsettings.types.put_tax_exemption_response
    import capo_taxsettings.types.put_tax_inheritance_request
    import capo_taxsettings.types.put_tax_inheritance_response
    import capo_taxsettings.types.put_tax_registration_request
    import capo_taxsettings.types.put_tax_registration_response
    import capo_taxsettings.types.supplemental_tax_registration
    import capo_taxsettings.types.supplemental_tax_registration_entry
    import capo_taxsettings.types.tax_document_metadata
    import capo_taxsettings.types.tax_exemption_details
    import capo_taxsettings.types.tax_registration_entry


class AsyncTaxSettingsClientConfig(TypedDict, total=False, closed=True):
    operation_interceptors: Iterable[AsyncInterceptor[Any, Any]]
    retry_max_attempts: int | None
    use_dual_stack: bool | None
    use_fips: bool | None
    endpoint: str | None
    region: str | None
    credentials_provider: IdentityProvider[Credentials] | None
    anonymous: bool | None


class AsyncTaxSettingsClient:
    """A client for the ``TaxSettings`` service.

    Args:
        http_handler: HTTP handler for sending requests. If not provided, creates a default handler.
        operation_interceptors: Interceptors that wrap every operation call. If not provided, defaults to an empty list.
        retry_max_attempts: Maximum number of times to retry a failed operation. Defaults to 3.
        use_dual_stack: The value of the ``AWS::UseDualStack`` endpoint parameter.
        use_fips: The value of the ``AWS::UseFIPS`` endpoint parameter.
        endpoint: The value of the ``SDK::Endpoint`` endpoint parameter.
        region: The value of the ``AWS::Region`` endpoint parameter.
        credentials: AWS credentials for request signing.
        credentials_provider: Provider that resolves AWS credentials. Takes precedence over ``credentials``.
        anonymous: Send requests unsigned, without resolving credentials, even for operations that require authentication.
    """

    def __init__(
        self,
        http_handler: AsyncBaseHandler | None = None,
        operation_interceptors: Iterable[AsyncInterceptor[Any, Any]] | None = None,
        retry_max_attempts: int | None = None,
        use_dual_stack: bool | None = None,
        use_fips: bool | None = None,
        endpoint: str | None = None,
        region: str | None = None,
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
        self._config = AsyncTaxSettingsClientConfig(
            {
                "operation_interceptors": operation_interceptors or [],
                "retry_max_attempts": retry_max_attempts,
                "use_dual_stack": use_dual_stack,
                "use_fips": use_fips,
                "endpoint": endpoint,
                "region": region,
                "credentials_provider": resolved_credentials_provider,
                "anonymous": anonymous,
            }
        )

    def operation_options(
        self, config_overrides: Optional[AsyncTaxSettingsClientConfig] = None
    ) -> tuple[Iterable[AsyncInterceptor[Any, Any]], AsyncOperationOptions]:
        overrides: AsyncTaxSettingsClientConfig = config_overrides or {}
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
            use_dual_stack=overrides.get(
                "use_dual_stack", self._config.get("use_dual_stack")
            ),
            use_fips=overrides.get("use_fips", self._config.get("use_fips")),
            endpoint=overrides.get("endpoint", self._config.get("endpoint")),
            region=overrides.get("region", self._config.get("region")),
            credentials_provider=overrides.get(
                "credentials_provider", self._config.get("credentials_provider")
            ),
            anonymous=overrides.get("anonymous", self._config.get("anonymous")),
        )
        return interceptors_, options_

    async def batch_delete_tax_registration(
        self,
        account_ids: "capo_taxsettings.types.account_ids.AccountIds",
        *,
        config_overrides: Optional[AsyncTaxSettingsClientConfig] = None,
    ) -> "capo_taxsettings.types.batch_delete_tax_registration_response.BatchDeleteTaxRegistrationResponse":
        """<p>Deletes tax registration for multiple accounts in batch. This can be used to delete tax registrations for up to five accounts in one batch. </p> <note> <p>This API operation can't be used to delete your tax registration in Brazil. Use the <a href="https://console.aws.amazon.com/billing/home#/paymentpreferences/paymentmethods">Payment preferences</a> page in the Billing and Cost Management console instead.</p> </note>

        Args:
            account_ids: <p>List of unique account identifiers. </p>

        Raises:
            capo_taxsettings.errors.conflict_exception.ConflictException: <p>The exception when the input is creating conflict with the given state.</p>
            capo_taxsettings.errors.internal_server_exception.InternalServerException: <p>The exception thrown when an unexpected error occurs when processing a request.</p>
            capo_taxsettings.errors.validation_exception.ValidationException: <p>The exception when the input doesn't pass validation for at least one of the input parameters. </p>
            capo_taxsettings.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        async def _handler(
            req: "AsyncOperationRequest[capo_taxsettings.types.batch_delete_tax_registration_request.BatchDeleteTaxRegistrationRequest]",
        ) -> AsyncOperationResponse[
            "capo_taxsettings.types.batch_delete_tax_registration_response.BatchDeleteTaxRegistrationResponse"
        ]:
            import capo_taxsettings._operations.tax_settings.batch_delete_tax_registration

            (
                output,
                http_response,
            ) = await capo_taxsettings._operations.tax_settings.batch_delete_tax_registration.async_batch_delete_tax_registration(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_taxsettings.types.batch_delete_tax_registration_request.BatchDeleteTaxRegistrationRequest = {
            "account_ids": account_ids
        }

        response = await aexecute_pipeline(
            AsyncOperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        await response.response.aclose()
        return response.output

    async def batch_get_tax_exemptions(
        self,
        account_ids: "capo_taxsettings.types.account_ids.AccountIds",
        *,
        config_overrides: Optional[AsyncTaxSettingsClientConfig] = None,
    ) -> "capo_taxsettings.types.batch_get_tax_exemptions_response.BatchGetTaxExemptionsResponse":
        """<p>Get the active tax exemptions for a given list of accounts. The IAM action is <code>tax:GetExemptions</code>. </p>

        Args:
            account_ids: <p> List of unique account identifiers. </p>

        Raises:
            capo_taxsettings.errors.internal_server_exception.InternalServerException: <p>The exception thrown when an unexpected error occurs when processing a request.</p>
            capo_taxsettings.errors.resource_not_found_exception.ResourceNotFoundException: <p>The exception thrown when the input doesn't have a resource associated to it.</p>
            capo_taxsettings.errors.validation_exception.ValidationException: <p>The exception when the input doesn't pass validation for at least one of the input parameters. </p>
            capo_taxsettings.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        async def _handler(
            req: "AsyncOperationRequest[capo_taxsettings.types.batch_get_tax_exemptions_request.BatchGetTaxExemptionsRequest]",
        ) -> AsyncOperationResponse[
            "capo_taxsettings.types.batch_get_tax_exemptions_response.BatchGetTaxExemptionsResponse"
        ]:
            import capo_taxsettings._operations.tax_settings.batch_get_tax_exemptions

            (
                output,
                http_response,
            ) = await capo_taxsettings._operations.tax_settings.batch_get_tax_exemptions.async_batch_get_tax_exemptions(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_taxsettings.types.batch_get_tax_exemptions_request.BatchGetTaxExemptionsRequest = {
            "account_ids": account_ids
        }

        response = await aexecute_pipeline(
            AsyncOperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        await response.response.aclose()
        return response.output

    async def batch_put_tax_registration(
        self,
        account_ids: "capo_taxsettings.types.account_ids.AccountIds",
        tax_registration_entry: "capo_taxsettings.types.tax_registration_entry.TaxRegistrationEntry",
        *,
        config_overrides: Optional[AsyncTaxSettingsClientConfig] = None,
    ) -> "capo_taxsettings.types.batch_put_tax_registration_response.BatchPutTaxRegistrationResponse":
        """<p>Adds or updates tax registration for multiple accounts in batch. This can be used to add or update tax registrations for up to five accounts in one batch. You can't set a TRN if there's a pending TRN. You'll need to delete the pending TRN first.</p> <p>To call this API operation for specific countries, see the following country-specific requirements.</p> <p> <b>Bangladesh</b> </p> <ul> <li> <p>You must specify the tax registration certificate document in the <code>taxRegistrationDocuments</code> field of the <code>VerificationDetails</code> object.</p> </li> </ul> <p> <b>Brazil</b> </p> <ul> <li> <p>You must complete the tax registration process in the <a href="https://console.aws.amazon.com/billing/home#/paymentpreferences/paymentmethods">Payment preferences</a> page in the Billing and Cost Management console. After your TRN and billing address are verified, you can call this API operation.</p> </li> <li> <p>For Amazon Web Services accounts created through Organizations, you can call this API operation when you don't have a billing address.</p> </li> </ul> <p> <b>Georgia</b> </p> <ul> <li> <p>The valid <code>personType</code> values are <code>Physical Person</code> and <code>Business</code>.</p> </li> </ul> <p> <b>Indonesia</b> </p> <ul> <li> <p> <code>PutTaxRegistration</code>: The use of this operation to submit tax information is subject to the <a href="http://aws.amazon.com/service-terms/">Amazon Web Services service terms</a>. By submitting, you’re providing consent for Amazon Web Services to validate NIK, NPWP, and NITKU data, provided by you with the Directorate General of Taxes of Indonesia in accordance with the Minister of Finance Regulation (PMK) Number 112/PMK.03/2022.</p> </li> <li> <p> <code>BatchPutTaxRegistration</code>: The use of this operation to submit tax information is subject to the <a href="http://aws.amazon.com/service-terms/">Amazon Web Services service terms</a>. By submitting, you’re providing consent for Amazon Web Services to validate NIK, NPWP, and NITKU data, provided by you with the Directorate General of Taxes of Indonesia in accordance with the Minister of Finance Regulation (PMK) Number 112/PMK.03/2022, through our third-party partner PT Achilles Advanced Management (OnlinePajak).</p> </li> <li> <p>You must specify the <code>taxRegistrationNumberType</code> in the <code>indonesiaAdditionalInfo</code> field of the <code>additionalTaxInformation</code> object.</p> </li> <li> <p>If you specify <code>decisionNumber</code>, you must specify the <code>ppnExceptionDesignationCode</code> in the <code>indonesiaAdditionalInfo</code> field of the <code>additionalTaxInformation</code> object. If the <code>taxRegistrationNumberType</code> is set to NPWP or NITKU, valid values for <code>ppnExceptionDesignationCode</code> are either <code>01</code>, <code>02</code>, <code>03</code>, <code>07</code>, or <code>08</code>.</p> <p>For other <code>taxRegistrationNumberType</code> values, <code>ppnExceptionDesignationCode</code> must be either <code>01</code>, <code>07</code>, or <code>08</code>.</p> </li> <li> <p>If <code>ppnExceptionDesignationCode</code> is <code>07</code> or <code>08</code>, you must specify the <code>decisionNumber</code> in the <code>indonesiaAdditionalInfo</code> field of the <code>additionalTaxInformation</code> object.</p> </li> </ul> <p> <b>Kenya</b> </p> <ul> <li> <p>You must specify the <code>personType</code> in the <code>kenyaAdditionalInfo</code> field of the <code>additionalTaxInformation</code> object.</p> </li> <li> <p>If the <code>personType</code> is <code>Physical Person</code>, you must specify the tax registration certificate document in the <code>taxRegistrationDocuments</code> field of the <code>VerificationDetails</code> object.</p> </li> </ul> <p> <b>Malaysia</b> </p> <ul> <li> <p>The sector valid values are <code>Business</code> and <code>Individual</code>.</p> </li> <li> <p> <code>RegistrationType</code> valid values are <code>NRIC</code> for individual, and TIN and sales and service tax (SST) for Business.</p> </li> <li> <p>For individual, you can specify the <code>taxInformationNumber</code> in <code>MalaysiaAdditionalInfo</code> with NRIC type, and a valid <code>MyKad</code> or NRIC number.</p> </li> <li> <p>For business, you must specify a <code>businessRegistrationNumber</code> in <code>MalaysiaAdditionalInfo</code> with a TIN type and tax identification number.</p> </li> <li> <p>For business resellers, you must specify a <code>businessRegistrationNumber</code> and <code>taxInformationNumber</code> in <code>MalaysiaAdditionalInfo</code> with a sales and service tax (SST) type and a valid SST number.</p> </li> <li> <p>For business resellers with service codes, you must specify <code>businessRegistrationNumber</code>, <code>taxInformationNumber</code>, and distinct <code>serviceTaxCodes</code> in <code>MalaysiaAdditionalInfo</code> with a SST type and valid sales and service tax (SST) number. By using this API operation, Amazon Web Services registers your self-declaration that you’re an authorized business reseller registered with the Royal Malaysia Customs Department (RMCD), and have a valid SST number.</p> </li> <li> <p>Amazon Web Services reserves the right to seek additional information and/or take other actions to support your self-declaration as appropriate.</p> </li> <li> <p>Amazon Web Services is currently registered under the following service tax codes. You must include at least one of the service tax codes in the service tax code strings to declare yourself as an authorized registered business reseller.</p> <p>Taxable service and service tax codes:</p> <p>Consultancy - 9907061674</p> <p>Training or coaching service - 9907071685</p> <p>IT service - 9907101676</p> <p>Digital services and electronic medium - 9907121690</p> </li> </ul> <p> <b>Mexico</b> </p> <ul> <li> <p>You must provide a Constancia de Situación fiscal (CSF) document in the <b>verificationDetails</b> field.</p> </li> <li> <p>You do not need to provide address and legal name. These will be populated based on your tax registration number.</p> </li> </ul> <p> <b>Nepal</b> </p> <ul> <li> <p>The sector valid values are <code>Business</code> and <code>Individual</code>.</p> </li> </ul> <p> <b>Saudi Arabia</b> </p> <ul> <li> <p>For <code>address</code>, you must specify <code>addressLine3</code>.</p> </li> </ul> <p> <b>South Korea</b> </p> <ul> <li> <p>You must specify the <code>certifiedEmailId</code> and <code>legalName</code> in the <code>TaxRegistrationEntry</code> object. Use Korean characters for <code>legalName</code>.</p> </li> <li> <p>You must specify the <code>businessRepresentativeName</code>, <code>itemOfBusiness</code>, and <code>lineOfBusiness</code> in the <code>southKoreaAdditionalInfo</code> field of the <code>additionalTaxInformation</code> object. Use Korean characters for these fields.</p> </li> <li> <p>You must specify the tax registration certificate document in the <code>taxRegistrationDocuments</code> field of the <code>VerificationDetails</code> object.</p> </li> <li> <p>For the <code>address</code> object, use Korean characters for <code>addressLine1</code>, <code>addressLine2</code> <code>city</code>, <code>postalCode</code>, and <code>stateOrRegion</code>.</p> </li> </ul> <p> <b>Spain</b> </p> <ul> <li> <p>You must specify the <code>registrationType</code> in the <code>spainAdditionalInfo</code> field of the <code>additionalTaxInformation</code> object.</p> </li> <li> <p>If the <code>registrationType</code> is <code>Local</code>, you must specify the tax registration certificate document in the <code>taxRegistrationDocuments</code> field of the <code>VerificationDetails</code> object.</p> </li> </ul> <p> <b>Turkey</b> </p> <ul> <li> <p>You must specify the <code>sector</code> in the <code>taxRegistrationEntry</code> object.</p> </li> <li> <p>If your <code>sector</code> is <code>Business</code>, <code>Individual</code>, or <code>Government</code>:</p> <ul> <li> <p>Specify the <code>taxOffice</code>. If your <code>sector</code> is <code>Individual</code>, don't enter this value.</p> </li> <li> <p>(Optional) Specify the <code>kepEmailId</code>. If your <code>sector</code> is <code>Individual</code>, don't enter this value.</p> </li> <li> <p> <b>Note:</b> In the <b>Tax Settings</b> page of the Billing console, <code>Government</code> appears as <b>Public institutions</b> </p> </li> </ul> </li> <li> <p>If your <code>sector</code> is <code>Business</code> and you're subject to KDV tax, you must specify your industry in the <code>industries</code> field.</p> </li> <li> <p>For <code>address</code>, you must specify <code>districtOrCounty</code>.</p> </li> </ul> <p> <b>Ukraine</b> </p> <ul> <li> <p>The sector valid values are <code>Business</code> and <code>Individual</code>.</p> </li> </ul> <p> <b>Philippines</b> </p> <ul> <li> <p>You can optionally specify the <code>isVatRegistered</code> in the <code>philippinesAdditionalInfo</code> field of the <code>additionalTaxInformation</code> object to indicate your VAT registration status with the Bureau of Internal Revenue (BIR).</p> </li> </ul> <p> <b>Belgium</b> </p> <ul> <li> <p>You can optionally specify the <code>peppolId</code> in the <code>belgiumAdditionalInfo</code> field of the <code>additionalTaxInformation</code> object.</p> </li> </ul> <p> <b>Chile</b> </p> <ul> <li> <p>You can optionally specify the <code>documentType</code> and <code>businessActivity</code> in the <code>chileAdditionalInfo</code> field of the <code>additionalTaxInformation</code> object.</p> </li> </ul> <p> <b>France</b> </p> <ul> <li> <p>You must specify the <code>sirenNumber</code> in the <code>franceAdditionalInfo</code> field of the <code>additionalTaxInformation</code> object.</p> </li> <li> <p>You can optionally specify the <code>eInvoiceRoutingCode</code> in the <code>franceAdditionalInfo</code> field of the <code>additionalTaxInformation</code> object.</p> </li> </ul> <p> <b>Monaco</b> </p> <ul> <li> <p>You must specify the <code>businessNumber</code> in the <code>monacoAdditionalInfo</code> field of the <code>additionalTaxInformation</code> object.</p> </li> </ul> <p> <b>Poland</b> </p> <ul> <li> <p>You can optionally specify the <code>taxRegistrationNumberType</code> in the <code>polandAdditionalInfo</code> field of the <code>additionalTaxInformation</code> object. Valid values are <code>EUTaxRegistrationNumber</code>, <code>LocalTaxRegistrationNumber</code>, or <code>LocalRegistrationNumber</code>.</p> </li> </ul>

        Args:
            account_ids: <p> List of unique account identifiers.</p>
            tax_registration_entry: <p>Your TRN information that will be stored to the accounts mentioned in <code>putEntries</code>. </p>

        Raises:
            capo_taxsettings.errors.conflict_exception.ConflictException: <p>The exception when the input is creating conflict with the given state.</p>
            capo_taxsettings.errors.internal_server_exception.InternalServerException: <p>The exception thrown when an unexpected error occurs when processing a request.</p>
            capo_taxsettings.errors.validation_exception.ValidationException: <p>The exception when the input doesn't pass validation for at least one of the input parameters. </p>
            capo_taxsettings.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        async def _handler(
            req: "AsyncOperationRequest[capo_taxsettings.types.batch_put_tax_registration_request.BatchPutTaxRegistrationRequest]",
        ) -> AsyncOperationResponse[
            "capo_taxsettings.types.batch_put_tax_registration_response.BatchPutTaxRegistrationResponse"
        ]:
            import capo_taxsettings._operations.tax_settings.batch_put_tax_registration

            (
                output,
                http_response,
            ) = await capo_taxsettings._operations.tax_settings.batch_put_tax_registration.async_batch_put_tax_registration(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_taxsettings.types.batch_put_tax_registration_request.BatchPutTaxRegistrationRequest = {
            "account_ids": account_ids,
            "tax_registration_entry": tax_registration_entry,
        }

        response = await aexecute_pipeline(
            AsyncOperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        await response.response.aclose()
        return response.output

    async def delete_supplemental_tax_registration(
        self,
        authority_id: "capo_taxsettings.types.generic_string.GenericString",
        *,
        config_overrides: Optional[AsyncTaxSettingsClientConfig] = None,
    ) -> "capo_taxsettings.types.delete_supplemental_tax_registration_response.DeleteSupplementalTaxRegistrationResponse":
        """<p> Deletes a supplemental tax registration for a single account. </p>

        Args:
            authority_id: <p> The unique authority Id for the supplemental TRN information that needs to be deleted. </p>

        Raises:
            capo_taxsettings.errors.conflict_exception.ConflictException: <p>The exception when the input is creating conflict with the given state.</p>
            capo_taxsettings.errors.internal_server_exception.InternalServerException: <p>The exception thrown when an unexpected error occurs when processing a request.</p>
            capo_taxsettings.errors.resource_not_found_exception.ResourceNotFoundException: <p>The exception thrown when the input doesn't have a resource associated to it.</p>
            capo_taxsettings.errors.validation_exception.ValidationException: <p>The exception when the input doesn't pass validation for at least one of the input parameters. </p>
            capo_taxsettings.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        async def _handler(
            req: "AsyncOperationRequest[capo_taxsettings.types.delete_supplemental_tax_registration_request.DeleteSupplementalTaxRegistrationRequest]",
        ) -> AsyncOperationResponse[
            "capo_taxsettings.types.delete_supplemental_tax_registration_response.DeleteSupplementalTaxRegistrationResponse"
        ]:
            import capo_taxsettings._operations.tax_settings.delete_supplemental_tax_registration

            (
                output,
                http_response,
            ) = await capo_taxsettings._operations.tax_settings.delete_supplemental_tax_registration.async_delete_supplemental_tax_registration(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_taxsettings.types.delete_supplemental_tax_registration_request.DeleteSupplementalTaxRegistrationRequest = {
            "authority_id": authority_id
        }

        response = await aexecute_pipeline(
            AsyncOperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        await response.response.aclose()
        return response.output

    async def delete_tax_registration(
        self,
        *,
        config_overrides: Optional[AsyncTaxSettingsClientConfig] = None,
        account_id: Optional["capo_taxsettings.types.account_id.AccountId"] = None,
    ) -> "capo_taxsettings.types.delete_tax_registration_response.DeleteTaxRegistrationResponse":
        """<p>Deletes tax registration for a single account. </p> <note> <p>This API operation can't be used to delete your tax registration in Brazil. Use the <a href="https://console.aws.amazon.com/billing/home#/paymentpreferences/paymentmethods">Payment preferences</a> page in the Billing and Cost Management console instead.</p> </note>

        Args:
            account_id: <p>Unique account identifier for the TRN information that needs to be deleted. If this isn't passed, the account ID corresponding to the credentials of the API caller will be used for this parameter.</p>

        Raises:
            capo_taxsettings.errors.conflict_exception.ConflictException: <p>The exception when the input is creating conflict with the given state.</p>
            capo_taxsettings.errors.internal_server_exception.InternalServerException: <p>The exception thrown when an unexpected error occurs when processing a request.</p>
            capo_taxsettings.errors.resource_not_found_exception.ResourceNotFoundException: <p>The exception thrown when the input doesn't have a resource associated to it.</p>
            capo_taxsettings.errors.validation_exception.ValidationException: <p>The exception when the input doesn't pass validation for at least one of the input parameters. </p>
            capo_taxsettings.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        async def _handler(
            req: "AsyncOperationRequest[capo_taxsettings.types.delete_tax_registration_request.DeleteTaxRegistrationRequest]",
        ) -> AsyncOperationResponse[
            "capo_taxsettings.types.delete_tax_registration_response.DeleteTaxRegistrationResponse"
        ]:
            import capo_taxsettings._operations.tax_settings.delete_tax_registration

            (
                output,
                http_response,
            ) = await capo_taxsettings._operations.tax_settings.delete_tax_registration.async_delete_tax_registration(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_taxsettings.types.delete_tax_registration_request.DeleteTaxRegistrationRequest = {}
        if account_id is not None:
            input_["account_id"] = account_id

        response = await aexecute_pipeline(
            AsyncOperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        await response.response.aclose()
        return response.output

    async def get_tax_exemption_types(
        self, *, config_overrides: Optional[AsyncTaxSettingsClientConfig] = None
    ) -> "capo_taxsettings.types.get_tax_exemption_types_response.GetTaxExemptionTypesResponse":
        """<p>Get supported tax exemption types. The IAM action is <code>tax:GetExemptions</code>. </p>

        Raises:
            capo_taxsettings.errors.internal_server_exception.InternalServerException: <p>The exception thrown when an unexpected error occurs when processing a request.</p>
            capo_taxsettings.errors.resource_not_found_exception.ResourceNotFoundException: <p>The exception thrown when the input doesn't have a resource associated to it.</p>
            capo_taxsettings.errors.validation_exception.ValidationException: <p>The exception when the input doesn't pass validation for at least one of the input parameters. </p>
            capo_taxsettings.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        async def _handler(
            req: "AsyncOperationRequest[capo_taxsettings.types.get_tax_exemption_types_request.GetTaxExemptionTypesRequest]",
        ) -> AsyncOperationResponse[
            "capo_taxsettings.types.get_tax_exemption_types_response.GetTaxExemptionTypesResponse"
        ]:
            import capo_taxsettings._operations.tax_settings.get_tax_exemption_types

            (
                output,
                http_response,
            ) = await capo_taxsettings._operations.tax_settings.get_tax_exemption_types.async_get_tax_exemption_types(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_taxsettings.types.get_tax_exemption_types_request.GetTaxExemptionTypesRequest = {}

        response = await aexecute_pipeline(
            AsyncOperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        await response.response.aclose()
        return response.output

    async def get_tax_inheritance(
        self, *, config_overrides: Optional[AsyncTaxSettingsClientConfig] = None
    ) -> (
        "capo_taxsettings.types.get_tax_inheritance_response.GetTaxInheritanceResponse"
    ):
        """<p>The get account tax inheritance status. </p>

        Raises:
            capo_taxsettings.errors.internal_server_exception.InternalServerException: <p>The exception thrown when an unexpected error occurs when processing a request.</p>
            capo_taxsettings.errors.resource_not_found_exception.ResourceNotFoundException: <p>The exception thrown when the input doesn't have a resource associated to it.</p>
            capo_taxsettings.errors.validation_exception.ValidationException: <p>The exception when the input doesn't pass validation for at least one of the input parameters. </p>
            capo_taxsettings.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        async def _handler(
            req: "AsyncOperationRequest[capo_taxsettings.types.get_tax_inheritance_request.GetTaxInheritanceRequest]",
        ) -> AsyncOperationResponse[
            "capo_taxsettings.types.get_tax_inheritance_response.GetTaxInheritanceResponse"
        ]:
            import capo_taxsettings._operations.tax_settings.get_tax_inheritance

            (
                output,
                http_response,
            ) = await capo_taxsettings._operations.tax_settings.get_tax_inheritance.async_get_tax_inheritance(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_taxsettings.types.get_tax_inheritance_request.GetTaxInheritanceRequest = {}

        response = await aexecute_pipeline(
            AsyncOperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        await response.response.aclose()
        return response.output

    async def get_tax_registration(
        self,
        *,
        config_overrides: Optional[AsyncTaxSettingsClientConfig] = None,
        account_id: Optional["capo_taxsettings.types.account_id.AccountId"] = None,
    ) -> "capo_taxsettings.types.get_tax_registration_response.GetTaxRegistrationResponse":
        """<p>Retrieves tax registration for a single account.</p>

        Args:
            account_id: <p>Your unique account identifier.</p>

        Raises:
            capo_taxsettings.errors.internal_server_exception.InternalServerException: <p>The exception thrown when an unexpected error occurs when processing a request.</p>
            capo_taxsettings.errors.resource_not_found_exception.ResourceNotFoundException: <p>The exception thrown when the input doesn't have a resource associated to it.</p>
            capo_taxsettings.errors.validation_exception.ValidationException: <p>The exception when the input doesn't pass validation for at least one of the input parameters. </p>
            capo_taxsettings.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        async def _handler(
            req: "AsyncOperationRequest[capo_taxsettings.types.get_tax_registration_request.GetTaxRegistrationRequest]",
        ) -> AsyncOperationResponse[
            "capo_taxsettings.types.get_tax_registration_response.GetTaxRegistrationResponse"
        ]:
            import capo_taxsettings._operations.tax_settings.get_tax_registration

            (
                output,
                http_response,
            ) = await capo_taxsettings._operations.tax_settings.get_tax_registration.async_get_tax_registration(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_taxsettings.types.get_tax_registration_request.GetTaxRegistrationRequest = {}
        if account_id is not None:
            input_["account_id"] = account_id

        response = await aexecute_pipeline(
            AsyncOperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        await response.response.aclose()
        return response.output

    async def get_tax_registration_document(
        self,
        tax_document_metadata: "capo_taxsettings.types.tax_document_metadata.TaxDocumentMetadata",
        *,
        config_overrides: Optional[AsyncTaxSettingsClientConfig] = None,
        destination_s3_location: Optional[
            "capo_taxsettings.types.destination_s3_location.DestinationS3Location"
        ] = None,
    ) -> "capo_taxsettings.types.get_tax_registration_document_response.GetTaxRegistrationDocumentResponse":
        """<p>Downloads your tax documents to the Amazon S3 bucket that you specify in your request.</p>

        Args:
            destination_s3_location: <p>The Amazon S3 bucket that you specify to download your tax documents to.</p>
            tax_document_metadata: <p>The metadata for your tax document.</p>

        Raises:
            capo_taxsettings.errors.internal_server_exception.InternalServerException: <p>The exception thrown when an unexpected error occurs when processing a request.</p>
            capo_taxsettings.errors.validation_exception.ValidationException: <p>The exception when the input doesn't pass validation for at least one of the input parameters. </p>
            capo_taxsettings.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        async def _handler(
            req: "AsyncOperationRequest[capo_taxsettings.types.get_tax_registration_document_request.GetTaxRegistrationDocumentRequest]",
        ) -> AsyncOperationResponse[
            "capo_taxsettings.types.get_tax_registration_document_response.GetTaxRegistrationDocumentResponse"
        ]:
            import capo_taxsettings._operations.tax_settings.get_tax_registration_document

            (
                output,
                http_response,
            ) = await capo_taxsettings._operations.tax_settings.get_tax_registration_document.async_get_tax_registration_document(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_taxsettings.types.get_tax_registration_document_request.GetTaxRegistrationDocumentRequest = {
            "tax_document_metadata": tax_document_metadata
        }
        if destination_s3_location is not None:
            input_["destination_s3_location"] = destination_s3_location

        response = await aexecute_pipeline(
            AsyncOperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        await response.response.aclose()
        return response.output

    async def list_supplemental_tax_registrations(
        self,
        *,
        config_overrides: Optional[AsyncTaxSettingsClientConfig] = None,
        max_results: Optional["capo_taxsettings.types.max_results.MaxResults"] = None,
        next_token: Optional[
            "capo_taxsettings.types.pagination_token_string.PaginationTokenString"
        ] = None,
    ) -> "capo_taxsettings.types.list_supplemental_tax_registrations_response.ListSupplementalTaxRegistrationsResponse":
        """<p> Retrieves supplemental tax registrations for a single account. </p>

        Args:
            max_results: <p> The number of <code>taxRegistrations</code> results you want in one response. </p>
            next_token: <p> The token to retrieve the next set of results. </p>

        Raises:
            capo_taxsettings.errors.internal_server_exception.InternalServerException: <p>The exception thrown when an unexpected error occurs when processing a request.</p>
            capo_taxsettings.errors.resource_not_found_exception.ResourceNotFoundException: <p>The exception thrown when the input doesn't have a resource associated to it.</p>
            capo_taxsettings.errors.validation_exception.ValidationException: <p>The exception when the input doesn't pass validation for at least one of the input parameters. </p>
            capo_taxsettings.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        async def _handler(
            req: "AsyncOperationRequest[capo_taxsettings.types.list_supplemental_tax_registrations_request.ListSupplementalTaxRegistrationsRequest]",
        ) -> AsyncOperationResponse[
            "capo_taxsettings.types.list_supplemental_tax_registrations_response.ListSupplementalTaxRegistrationsResponse"
        ]:
            import capo_taxsettings._operations.tax_settings.list_supplemental_tax_registrations

            (
                output,
                http_response,
            ) = await capo_taxsettings._operations.tax_settings.list_supplemental_tax_registrations.async_list_supplemental_tax_registrations(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_taxsettings.types.list_supplemental_tax_registrations_request.ListSupplementalTaxRegistrationsRequest = {}
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

    async def iter_list_supplemental_tax_registrations(
        self,
        *,
        config_overrides: Optional[AsyncTaxSettingsClientConfig] = None,
        max_results: Optional["capo_taxsettings.types.max_results.MaxResults"] = None,
        next_token: Optional[
            "capo_taxsettings.types.pagination_token_string.PaginationTokenString"
        ] = None,
    ) -> "AsyncIterator[capo_taxsettings.types.supplemental_tax_registration.SupplementalTaxRegistration]":
        _token = next_token
        while True:
            _response = await self.list_supplemental_tax_registrations(
                config_overrides=config_overrides,
                max_results=max_results,
                next_token=_token,
            )
            _page = _resolve_path(_response, ("tax_registrations",))
            for _item in _page or []:
                yield _item
            _token = _resolve_path(_response, ("next_token",))
            if not _token:
                break

    async def list_tax_exemptions(
        self,
        *,
        config_overrides: Optional[AsyncTaxSettingsClientConfig] = None,
        max_results: Optional["capo_taxsettings.types.max_results.MaxResults"] = None,
        next_token: Optional[
            "capo_taxsettings.types.pagination_token_string.PaginationTokenString"
        ] = None,
    ) -> (
        "capo_taxsettings.types.list_tax_exemptions_response.ListTaxExemptionsResponse"
    ):
        """<p>Retrieves the tax exemption of accounts listed in a consolidated billing family. The IAM action is <code>tax:GetExemptions</code>.</p>

        Args:
            max_results: <p>The number of results you want in one response. </p>
            next_token: <p>The token to retrieve the next set of results. </p>

        Raises:
            capo_taxsettings.errors.internal_server_exception.InternalServerException: <p>The exception thrown when an unexpected error occurs when processing a request.</p>
            capo_taxsettings.errors.resource_not_found_exception.ResourceNotFoundException: <p>The exception thrown when the input doesn't have a resource associated to it.</p>
            capo_taxsettings.errors.validation_exception.ValidationException: <p>The exception when the input doesn't pass validation for at least one of the input parameters. </p>
            capo_taxsettings.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        async def _handler(
            req: "AsyncOperationRequest[capo_taxsettings.types.list_tax_exemptions_request.ListTaxExemptionsRequest]",
        ) -> AsyncOperationResponse[
            "capo_taxsettings.types.list_tax_exemptions_response.ListTaxExemptionsResponse"
        ]:
            import capo_taxsettings._operations.tax_settings.list_tax_exemptions

            (
                output,
                http_response,
            ) = await capo_taxsettings._operations.tax_settings.list_tax_exemptions.async_list_tax_exemptions(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_taxsettings.types.list_tax_exemptions_request.ListTaxExemptionsRequest = {}
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

    async def iter_list_tax_exemptions(
        self,
        *,
        config_overrides: Optional[AsyncTaxSettingsClientConfig] = None,
        max_results: Optional["capo_taxsettings.types.max_results.MaxResults"] = None,
        next_token: Optional[
            "capo_taxsettings.types.pagination_token_string.PaginationTokenString"
        ] = None,
    ) -> "AsyncIterator[tuple[capo_taxsettings.types.account_id.AccountId, capo_taxsettings.types.tax_exemption_details.TaxExemptionDetails]]":
        _token = next_token
        while True:
            _response = await self.list_tax_exemptions(
                config_overrides=config_overrides,
                max_results=max_results,
                next_token=_token,
            )
            _page = _resolve_path(_response, ("tax_exemption_details_map",))
            for _k, _v in (_page or {}).items():
                yield (_k, _v)
            _token = _resolve_path(_response, ("next_token",))
            if not _token:
                break

    async def list_tax_registrations(
        self,
        *,
        config_overrides: Optional[AsyncTaxSettingsClientConfig] = None,
        max_results: Optional["capo_taxsettings.types.max_results.MaxResults"] = None,
        next_token: Optional[
            "capo_taxsettings.types.pagination_token_string.PaginationTokenString"
        ] = None,
    ) -> "capo_taxsettings.types.list_tax_registrations_response.ListTaxRegistrationsResponse":
        """<p>Retrieves the tax registration of accounts listed in a consolidated billing family. This can be used to retrieve up to 100 accounts' tax registrations in one call (default 50). </p>

        Args:
            max_results: <p>Number of <code>accountDetails</code> results you want in one response. </p>
            next_token: <p>The token to retrieve the next set of results. </p>

        Raises:
            capo_taxsettings.errors.internal_server_exception.InternalServerException: <p>The exception thrown when an unexpected error occurs when processing a request.</p>
            capo_taxsettings.errors.resource_not_found_exception.ResourceNotFoundException: <p>The exception thrown when the input doesn't have a resource associated to it.</p>
            capo_taxsettings.errors.validation_exception.ValidationException: <p>The exception when the input doesn't pass validation for at least one of the input parameters. </p>
            capo_taxsettings.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        async def _handler(
            req: "AsyncOperationRequest[capo_taxsettings.types.list_tax_registrations_request.ListTaxRegistrationsRequest]",
        ) -> AsyncOperationResponse[
            "capo_taxsettings.types.list_tax_registrations_response.ListTaxRegistrationsResponse"
        ]:
            import capo_taxsettings._operations.tax_settings.list_tax_registrations

            (
                output,
                http_response,
            ) = await capo_taxsettings._operations.tax_settings.list_tax_registrations.async_list_tax_registrations(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_taxsettings.types.list_tax_registrations_request.ListTaxRegistrationsRequest = {}
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

    async def iter_list_tax_registrations(
        self,
        *,
        config_overrides: Optional[AsyncTaxSettingsClientConfig] = None,
        max_results: Optional["capo_taxsettings.types.max_results.MaxResults"] = None,
        next_token: Optional[
            "capo_taxsettings.types.pagination_token_string.PaginationTokenString"
        ] = None,
    ) -> "AsyncIterator[capo_taxsettings.types.account_details.AccountDetails]":
        _token = next_token
        while True:
            _response = await self.list_tax_registrations(
                config_overrides=config_overrides,
                max_results=max_results,
                next_token=_token,
            )
            _page = _resolve_path(_response, ("account_details",))
            for _item in _page or []:
                yield _item
            _token = _resolve_path(_response, ("next_token",))
            if not _token:
                break

    async def put_supplemental_tax_registration(
        self,
        tax_registration_entry: "capo_taxsettings.types.supplemental_tax_registration_entry.SupplementalTaxRegistrationEntry",
        *,
        config_overrides: Optional[AsyncTaxSettingsClientConfig] = None,
    ) -> "capo_taxsettings.types.put_supplemental_tax_registration_response.PutSupplementalTaxRegistrationResponse":
        """<p> Stores supplemental tax registration for a single account. </p>

        Args:
            tax_registration_entry: <p> The supplemental TRN information that will be stored for the caller account ID. </p>

        Raises:
            capo_taxsettings.errors.conflict_exception.ConflictException: <p>The exception when the input is creating conflict with the given state.</p>
            capo_taxsettings.errors.internal_server_exception.InternalServerException: <p>The exception thrown when an unexpected error occurs when processing a request.</p>
            capo_taxsettings.errors.validation_exception.ValidationException: <p>The exception when the input doesn't pass validation for at least one of the input parameters. </p>
            capo_taxsettings.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        async def _handler(
            req: "AsyncOperationRequest[capo_taxsettings.types.put_supplemental_tax_registration_request.PutSupplementalTaxRegistrationRequest]",
        ) -> AsyncOperationResponse[
            "capo_taxsettings.types.put_supplemental_tax_registration_response.PutSupplementalTaxRegistrationResponse"
        ]:
            import capo_taxsettings._operations.tax_settings.put_supplemental_tax_registration

            (
                output,
                http_response,
            ) = await capo_taxsettings._operations.tax_settings.put_supplemental_tax_registration.async_put_supplemental_tax_registration(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_taxsettings.types.put_supplemental_tax_registration_request.PutSupplementalTaxRegistrationRequest = {
            "tax_registration_entry": tax_registration_entry
        }

        response = await aexecute_pipeline(
            AsyncOperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        await response.response.aclose()
        return response.output

    async def put_tax_exemption(
        self,
        account_ids: "capo_taxsettings.types.account_ids.AccountIds",
        authority: "capo_taxsettings.types.authority.Authority",
        exemption_type: "capo_taxsettings.types.generic_string.GenericString",
        exemption_certificate: "capo_taxsettings.types.exemption_certificate.ExemptionCertificate",
        *,
        config_overrides: Optional[AsyncTaxSettingsClientConfig] = None,
    ) -> "capo_taxsettings.types.put_tax_exemption_response.PutTaxExemptionResponse":
        """<p>Adds the tax exemption for a single account or all accounts listed in a consolidated billing family. The IAM action is <code>tax:UpdateExemptions</code>. </p>

        Args:
            account_ids: <p> The list of unique account identifiers. </p>
            exemption_type: <p>The exemption type. Use the supported tax exemption type description. </p>

        Raises:
            capo_taxsettings.errors.access_denied_exception.AccessDeniedException: <p>The access is denied for the Amazon Web Services Support API. </p>
            capo_taxsettings.errors.attachment_upload_exception.AttachmentUploadException: <p>Failed to upload the tax exemption document to Amazon Web Services Support case. </p>
            capo_taxsettings.errors.case_creation_limit_exceeded_exception.CaseCreationLimitExceededException: <p>You've exceeded the Amazon Web Services Support case creation limit for your account. </p>
            capo_taxsettings.errors.internal_server_exception.InternalServerException: <p>The exception thrown when an unexpected error occurs when processing a request.</p>
            capo_taxsettings.errors.resource_not_found_exception.ResourceNotFoundException: <p>The exception thrown when the input doesn't have a resource associated to it.</p>
            capo_taxsettings.errors.validation_exception.ValidationException: <p>The exception when the input doesn't pass validation for at least one of the input parameters. </p>
            capo_taxsettings.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        async def _handler(
            req: "AsyncOperationRequest[capo_taxsettings.types.put_tax_exemption_request.PutTaxExemptionRequest]",
        ) -> AsyncOperationResponse[
            "capo_taxsettings.types.put_tax_exemption_response.PutTaxExemptionResponse"
        ]:
            import capo_taxsettings._operations.tax_settings.put_tax_exemption

            (
                output,
                http_response,
            ) = await capo_taxsettings._operations.tax_settings.put_tax_exemption.async_put_tax_exemption(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_taxsettings.types.put_tax_exemption_request.PutTaxExemptionRequest = {
            "account_ids": account_ids,
            "authority": authority,
            "exemption_type": exemption_type,
            "exemption_certificate": exemption_certificate,
        }

        response = await aexecute_pipeline(
            AsyncOperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        await response.response.aclose()
        return response.output

    async def put_tax_inheritance(
        self,
        *,
        config_overrides: Optional[AsyncTaxSettingsClientConfig] = None,
        heritage_status: Optional[
            "capo_taxsettings.types.heritage_status.HeritageStatus"
        ] = None,
    ) -> (
        "capo_taxsettings.types.put_tax_inheritance_response.PutTaxInheritanceResponse"
    ):
        """<p>The updated tax inheritance status. </p>

        Args:
            heritage_status: <p>The tax inheritance status. </p>

        Raises:
            capo_taxsettings.errors.conflict_exception.ConflictException: <p>The exception when the input is creating conflict with the given state.</p>
            capo_taxsettings.errors.internal_server_exception.InternalServerException: <p>The exception thrown when an unexpected error occurs when processing a request.</p>
            capo_taxsettings.errors.resource_not_found_exception.ResourceNotFoundException: <p>The exception thrown when the input doesn't have a resource associated to it.</p>
            capo_taxsettings.errors.validation_exception.ValidationException: <p>The exception when the input doesn't pass validation for at least one of the input parameters. </p>
            capo_taxsettings.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        async def _handler(
            req: "AsyncOperationRequest[capo_taxsettings.types.put_tax_inheritance_request.PutTaxInheritanceRequest]",
        ) -> AsyncOperationResponse[
            "capo_taxsettings.types.put_tax_inheritance_response.PutTaxInheritanceResponse"
        ]:
            import capo_taxsettings._operations.tax_settings.put_tax_inheritance

            (
                output,
                http_response,
            ) = await capo_taxsettings._operations.tax_settings.put_tax_inheritance.async_put_tax_inheritance(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_taxsettings.types.put_tax_inheritance_request.PutTaxInheritanceRequest = {}
        if heritage_status is not None:
            input_["heritage_status"] = heritage_status

        response = await aexecute_pipeline(
            AsyncOperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        await response.response.aclose()
        return response.output

    async def put_tax_registration(
        self,
        tax_registration_entry: "capo_taxsettings.types.tax_registration_entry.TaxRegistrationEntry",
        *,
        config_overrides: Optional[AsyncTaxSettingsClientConfig] = None,
        account_id: Optional["capo_taxsettings.types.account_id.AccountId"] = None,
    ) -> "capo_taxsettings.types.put_tax_registration_response.PutTaxRegistrationResponse":
        """<p>Adds or updates tax registration for a single account. You can't set a TRN if there's a pending TRN. You'll need to delete the pending TRN first.</p> <p>To call this API operation for specific countries, see the following country-specific requirements.</p> <p> <b>Bangladesh</b> </p> <ul> <li> <p>You must specify the tax registration certificate document in the <code>taxRegistrationDocuments</code> field of the <code>VerificationDetails</code> object.</p> </li> </ul> <p> <b>Brazil</b> </p> <ul> <li> <p>You must complete the tax registration process in the <a href="https://console.aws.amazon.com/billing/home#/paymentpreferences/paymentmethods">Payment preferences</a> page in the Billing and Cost Management console. After your TRN and billing address are verified, you can call this API operation.</p> </li> <li> <p>For Amazon Web Services accounts created through Organizations, you can call this API operation when you don't have a billing address.</p> </li> </ul> <p> <b>Georgia</b> </p> <ul> <li> <p>The valid <code>personType</code> values are <code>Physical Person</code> and <code>Business</code>.</p> </li> </ul> <p> <b>Indonesia</b> </p> <ul> <li> <p> <code>PutTaxRegistration</code>: The use of this operation to submit tax information is subject to the <a href="http://aws.amazon.com/service-terms/">Amazon Web Services service terms</a>. By submitting, you’re providing consent for Amazon Web Services to validate NIK, NPWP, and NITKU data, provided by you with the Directorate General of Taxes of Indonesia in accordance with the Minister of Finance Regulation (PMK) Number 112/PMK.03/2022.</p> </li> <li> <p> <code>BatchPutTaxRegistration</code>: The use of this operation to submit tax information is subject to the <a href="http://aws.amazon.com/service-terms/">Amazon Web Services service terms</a>. By submitting, you’re providing consent for Amazon Web Services to validate NIK, NPWP, and NITKU data, provided by you with the Directorate General of Taxes of Indonesia in accordance with the Minister of Finance Regulation (PMK) Number 112/PMK.03/2022, through our third-party partner PT Achilles Advanced Management (OnlinePajak).</p> </li> <li> <p>You must specify the <code>taxRegistrationNumberType</code> in the <code>indonesiaAdditionalInfo</code> field of the <code>additionalTaxInformation</code> object.</p> </li> <li> <p>If you specify <code>decisionNumber</code>, you must specify the <code>ppnExceptionDesignationCode</code> in the <code>indonesiaAdditionalInfo</code> field of the <code>additionalTaxInformation</code> object. If the <code>taxRegistrationNumberType</code> is set to NPWP or NITKU, valid values for <code>ppnExceptionDesignationCode</code> are either <code>01</code>, <code>02</code>, <code>03</code>, <code>07</code>, or <code>08</code>.</p> <p>For other <code>taxRegistrationNumberType</code> values, <code>ppnExceptionDesignationCode</code> must be either <code>01</code>, <code>07</code>, or <code>08</code>.</p> </li> <li> <p>If <code>ppnExceptionDesignationCode</code> is <code>07</code> or <code>08</code>, you must specify the <code>decisionNumber</code> in the <code>indonesiaAdditionalInfo</code> field of the <code>additionalTaxInformation</code> object.</p> </li> </ul> <p> <b>Kenya</b> </p> <ul> <li> <p>You must specify the <code>personType</code> in the <code>kenyaAdditionalInfo</code> field of the <code>additionalTaxInformation</code> object.</p> </li> <li> <p>If the <code>personType</code> is <code>Physical Person</code>, you must specify the tax registration certificate document in the <code>taxRegistrationDocuments</code> field of the <code>VerificationDetails</code> object.</p> </li> </ul> <p> <b>Malaysia</b> </p> <ul> <li> <p>The sector valid values are <code>Business</code> and <code>Individual</code>.</p> </li> <li> <p> <code>RegistrationType</code> valid values are <code>NRIC</code> for individual, and TIN and sales and service tax (SST) for Business.</p> </li> <li> <p>For individual, you can specify the <code>taxInformationNumber</code> in <code>MalaysiaAdditionalInfo</code> with NRIC type, and a valid <code>MyKad</code> or NRIC number.</p> </li> <li> <p>For business, you must specify a <code>businessRegistrationNumber</code> in <code>MalaysiaAdditionalInfo</code> with a TIN type and tax identification number.</p> </li> <li> <p>For business resellers, you must specify a <code>businessRegistrationNumber</code> and <code>taxInformationNumber</code> in <code>MalaysiaAdditionalInfo</code> with a sales and service tax (SST) type and a valid SST number.</p> </li> <li> <p>For business resellers with service codes, you must specify <code>businessRegistrationNumber</code>, <code>taxInformationNumber</code>, and distinct <code>serviceTaxCodes</code> in <code>MalaysiaAdditionalInfo</code> with a SST type and valid sales and service tax (SST) number. By using this API operation, Amazon Web Services registers your self-declaration that you’re an authorized business reseller registered with the Royal Malaysia Customs Department (RMCD), and have a valid SST number.</p> </li> <li> <p>Amazon Web Services reserves the right to seek additional information and/or take other actions to support your self-declaration as appropriate.</p> </li> <li> <p>Amazon Web Services is currently registered under the following service tax codes. You must include at least one of the service tax codes in the service tax code strings to declare yourself as an authorized registered business reseller.</p> <p>Taxable service and service tax codes:</p> <p>Consultancy - 9907061674</p> <p>Training or coaching service - 9907071685</p> <p>IT service - 9907101676</p> <p>Digital services and electronic medium - 9907121690</p> </li> </ul> <p> <b>Mexico</b> </p> <ul> <li> <p>You must provide a Constancia de Situación fiscal (CSF) document in the <b>verificationDetails</b> field.</p> </li> <li> <p>You do not need to provide address and legal name. These will be populated based on your tax registration number.</p> </li> </ul> <p> <b>Nepal</b> </p> <ul> <li> <p>The sector valid values are <code>Business</code> and <code>Individual</code>.</p> </li> </ul> <p> <b>Saudi Arabia</b> </p> <ul> <li> <p>For <code>address</code>, you must specify <code>addressLine3</code>.</p> </li> </ul> <p> <b>South Korea</b> </p> <ul> <li> <p>You must specify the <code>certifiedEmailId</code> and <code>legalName</code> in the <code>TaxRegistrationEntry</code> object. Use Korean characters for <code>legalName</code>.</p> </li> <li> <p>You must specify the <code>businessRepresentativeName</code>, <code>itemOfBusiness</code>, and <code>lineOfBusiness</code> in the <code>southKoreaAdditionalInfo</code> field of the <code>additionalTaxInformation</code> object. Use Korean characters for these fields.</p> </li> <li> <p>You must specify the tax registration certificate document in the <code>taxRegistrationDocuments</code> field of the <code>VerificationDetails</code> object.</p> </li> <li> <p>For the <code>address</code> object, use Korean characters for <code>addressLine1</code>, <code>addressLine2</code> <code>city</code>, <code>postalCode</code>, and <code>stateOrRegion</code>.</p> </li> </ul> <p> <b>Spain</b> </p> <ul> <li> <p>You must specify the <code>registrationType</code> in the <code>spainAdditionalInfo</code> field of the <code>additionalTaxInformation</code> object.</p> </li> <li> <p>If the <code>registrationType</code> is <code>Local</code>, you must specify the tax registration certificate document in the <code>taxRegistrationDocuments</code> field of the <code>VerificationDetails</code> object.</p> </li> </ul> <p> <b>Turkey</b> </p> <ul> <li> <p>You must specify the <code>sector</code> in the <code>taxRegistrationEntry</code> object.</p> </li> <li> <p>If your <code>sector</code> is <code>Business</code>, <code>Individual</code>, or <code>Government</code>:</p> <ul> <li> <p>Specify the <code>taxOffice</code>. If your <code>sector</code> is <code>Individual</code>, don't enter this value.</p> </li> <li> <p>(Optional) Specify the <code>kepEmailId</code>. If your <code>sector</code> is <code>Individual</code>, don't enter this value.</p> </li> <li> <p> <b>Note:</b> In the <b>Tax Settings</b> page of the Billing console, <code>Government</code> appears as <b>Public institutions</b> </p> </li> </ul> </li> <li> <p>If your <code>sector</code> is <code>Business</code> and you're subject to KDV tax, you must specify your industry in the <code>industries</code> field.</p> </li> <li> <p>For <code>address</code>, you must specify <code>districtOrCounty</code>.</p> </li> </ul> <p> <b>Ukraine</b> </p> <ul> <li> <p>The sector valid values are <code>Business</code> and <code>Individual</code>.</p> </li> </ul> <p> <b>Philippines</b> </p> <ul> <li> <p>You can optionally specify the <code>isVatRegistered</code> in the <code>philippinesAdditionalInfo</code> field of the <code>additionalTaxInformation</code> object to indicate your VAT registration status with the Bureau of Internal Revenue (BIR).</p> </li> </ul> <p> <b>Belgium</b> </p> <ul> <li> <p>You can optionally specify the <code>peppolId</code> in the <code>belgiumAdditionalInfo</code> field of the <code>additionalTaxInformation</code> object.</p> </li> </ul> <p> <b>Chile</b> </p> <ul> <li> <p>You can optionally specify the <code>documentType</code> and <code>businessActivity</code> in the <code>chileAdditionalInfo</code> field of the <code>additionalTaxInformation</code> object.</p> </li> </ul> <p> <b>France</b> </p> <ul> <li> <p>You must specify the <code>sirenNumber</code> in the <code>franceAdditionalInfo</code> field of the <code>additionalTaxInformation</code> object.</p> </li> <li> <p>You can optionally specify the <code>eInvoiceRoutingCode</code> in the <code>franceAdditionalInfo</code> field of the <code>additionalTaxInformation</code> object.</p> </li> </ul> <p> <b>Monaco</b> </p> <ul> <li> <p>You must specify the <code>businessNumber</code> in the <code>monacoAdditionalInfo</code> field of the <code>additionalTaxInformation</code> object.</p> </li> </ul> <p> <b>Poland</b> </p> <ul> <li> <p>You can optionally specify the <code>taxRegistrationNumberType</code> in the <code>polandAdditionalInfo</code> field of the <code>additionalTaxInformation</code> object. Valid values are <code>EUTaxRegistrationNumber</code>, <code>LocalTaxRegistrationNumber</code>, or <code>LocalRegistrationNumber</code>.</p> </li> </ul>

        Args:
            account_id: <p>Your unique account identifier. </p>
            tax_registration_entry: <p> Your TRN information that will be stored to the account mentioned in <code>accountId</code>. </p>

        Raises:
            capo_taxsettings.errors.conflict_exception.ConflictException: <p>The exception when the input is creating conflict with the given state.</p>
            capo_taxsettings.errors.internal_server_exception.InternalServerException: <p>The exception thrown when an unexpected error occurs when processing a request.</p>
            capo_taxsettings.errors.validation_exception.ValidationException: <p>The exception when the input doesn't pass validation for at least one of the input parameters. </p>
            capo_taxsettings.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        async def _handler(
            req: "AsyncOperationRequest[capo_taxsettings.types.put_tax_registration_request.PutTaxRegistrationRequest]",
        ) -> AsyncOperationResponse[
            "capo_taxsettings.types.put_tax_registration_response.PutTaxRegistrationResponse"
        ]:
            import capo_taxsettings._operations.tax_settings.put_tax_registration

            (
                output,
                http_response,
            ) = await capo_taxsettings._operations.tax_settings.put_tax_registration.async_put_tax_registration(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_taxsettings.types.put_tax_registration_request.PutTaxRegistrationRequest = {
            "tax_registration_entry": tax_registration_entry
        }
        if account_id is not None:
            input_["account_id"] = account_id

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
