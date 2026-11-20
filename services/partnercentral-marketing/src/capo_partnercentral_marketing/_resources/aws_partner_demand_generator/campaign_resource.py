from __future__ import annotations

import uuid
from typing import TYPE_CHECKING, Any, Optional

from capo_partnercentral_marketing._services._pipeline import (
    AsyncOperationRequest,
    AsyncOperationResponse,
    OperationLogging,
    OperationRequest,
    OperationResponse,
    aexecute_pipeline,
    execute_pipeline,
)

if TYPE_CHECKING:
    import capo_partnercentral_marketing.types.batch_create_campaign_asset_entries
    import capo_partnercentral_marketing.types.batch_create_campaign_asset_request
    import capo_partnercentral_marketing.types.batch_create_campaign_asset_response
    import capo_partnercentral_marketing.types.campaign_asset_export_task_id
    import capo_partnercentral_marketing.types.campaign_asset_id
    import capo_partnercentral_marketing.types.campaign_asset_identifiers
    import capo_partnercentral_marketing.types.campaign_asset_summary
    import capo_partnercentral_marketing.types.campaign_identifier
    import capo_partnercentral_marketing.types.campaign_identifier_list
    import capo_partnercentral_marketing.types.campaign_name
    import capo_partnercentral_marketing.types.campaign_social_connections
    import capo_partnercentral_marketing.types.campaign_sort
    import capo_partnercentral_marketing.types.campaign_state_list
    import capo_partnercentral_marketing.types.campaign_summary
    import capo_partnercentral_marketing.types.campaign_template_id
    import capo_partnercentral_marketing.types.catalog
    import capo_partnercentral_marketing.types.client_token
    import capo_partnercentral_marketing.types.create_campaign_request
    import capo_partnercentral_marketing.types.create_campaign_response
    import capo_partnercentral_marketing.types.deactivate_campaign_asset_request
    import capo_partnercentral_marketing.types.deactivate_campaign_asset_response
    import capo_partnercentral_marketing.types.delete_campaign_asset_request
    import capo_partnercentral_marketing.types.delete_campaign_request
    import capo_partnercentral_marketing.types.engagement_group_id_list
    import capo_partnercentral_marketing.types.field_value_input_list
    import capo_partnercentral_marketing.types.file_ref
    import capo_partnercentral_marketing.types.get_campaign_asset_activation_task_request
    import capo_partnercentral_marketing.types.get_campaign_asset_activation_task_response
    import capo_partnercentral_marketing.types.get_campaign_asset_export_task_request
    import capo_partnercentral_marketing.types.get_campaign_asset_export_task_response
    import capo_partnercentral_marketing.types.get_campaign_asset_request
    import capo_partnercentral_marketing.types.get_campaign_asset_response
    import capo_partnercentral_marketing.types.get_campaign_request
    import capo_partnercentral_marketing.types.get_campaign_response
    import capo_partnercentral_marketing.types.layout_option_value
    import capo_partnercentral_marketing.types.list_campaign_assets_request
    import capo_partnercentral_marketing.types.list_campaign_assets_response
    import capo_partnercentral_marketing.types.list_campaigns_request
    import capo_partnercentral_marketing.types.list_campaigns_response
    import capo_partnercentral_marketing.types.max_results
    import capo_partnercentral_marketing.types.monetary_value
    import capo_partnercentral_marketing.types.next_token
    import capo_partnercentral_marketing.types.partner_address
    import capo_partnercentral_marketing.types.privacy_policy_url
    import capo_partnercentral_marketing.types.send_mode
    import capo_partnercentral_marketing.types.sender_email
    import capo_partnercentral_marketing.types.start_campaign_asset_activation_task_request
    import capo_partnercentral_marketing.types.start_campaign_asset_activation_task_response
    import capo_partnercentral_marketing.types.start_campaign_asset_export_task_request
    import capo_partnercentral_marketing.types.start_campaign_asset_export_task_response
    import capo_partnercentral_marketing.types.tag_list
    import capo_partnercentral_marketing.types.target_audience
    import capo_partnercentral_marketing.types.timestamp
    import capo_partnercentral_marketing.types.update_campaign_asset_request
    import capo_partnercentral_marketing.types.update_campaign_asset_response
    import capo_partnercentral_marketing.types.update_campaign_request
    import capo_partnercentral_marketing.types.update_campaign_response
    import capo_partnercentral_marketing.types.utc_date
    from capo_partnercentral_marketing._services.async_partner_central_marketing import (
        AsyncPartnerCentralMarketingClient,
        AsyncPartnerCentralMarketingClientConfig,
    )
    from capo_partnercentral_marketing._services.partner_central_marketing import (
        PartnerCentralMarketingClient,
        PartnerCentralMarketingClientConfig,
    )


class CampaignResource:
    def __init__(self, service: PartnerCentralMarketingClient) -> None:
        self._service = service

    def create(
        self,
        catalog: "capo_partnercentral_marketing.types.catalog.Catalog",
        name: "capo_partnercentral_marketing.types.campaign_name.CampaignName",
        campaign_template_id: "capo_partnercentral_marketing.types.campaign_template_id.CampaignTemplateId",
        *,
        config_overrides: Optional[PartnerCentralMarketingClientConfig] = None,
        sender_email: Optional[
            "capo_partnercentral_marketing.types.sender_email.SenderEmail"
        ] = None,
        privacy_policy_url: Optional[
            "capo_partnercentral_marketing.types.privacy_policy_url.PrivacyPolicyUrl"
        ] = None,
        partner_address: Optional[
            "capo_partnercentral_marketing.types.partner_address.PartnerAddress"
        ] = None,
        partner_badge: Optional[
            "capo_partnercentral_marketing.types.file_ref.FileRef"
        ] = None,
        email_target: Optional[
            "capo_partnercentral_marketing.types.file_ref.FileRef"
        ] = None,
        email_target_engagement_group_ids: Optional[
            "capo_partnercentral_marketing.types.engagement_group_id_list.EngagementGroupIdList"
        ] = None,
        target_audience: Optional[
            "capo_partnercentral_marketing.types.target_audience.TargetAudience"
        ] = None,
        estimated_budget: Optional[
            "capo_partnercentral_marketing.types.monetary_value.MonetaryValue"
        ] = None,
        total_budget: Optional[
            "capo_partnercentral_marketing.types.monetary_value.MonetaryValue"
        ] = None,
        start_on: Optional[
            "capo_partnercentral_marketing.types.utc_date.UtcDate"
        ] = None,
        end_on: Optional["capo_partnercentral_marketing.types.utc_date.UtcDate"] = None,
        client_token: Optional[
            "capo_partnercentral_marketing.types.client_token.ClientToken"
        ] = None,
        tags: Optional["capo_partnercentral_marketing.types.tag_list.TagList"] = None,
    ) -> "capo_partnercentral_marketing.types.create_campaign_response.CreateCampaignResponse":
        """Creates a new marketing campaign. Returns the identity of the new campaign, not the campaign. Growing a response is backward compatible and shrinking one is not, and the caller's next step is a `GetCampaign` anyway — a write that supplies an audience cannot report its scan verdict, because that is decided after it commits.

        Args:
            catalog: The catalog (AWS or Sandbox).
            name: The display name.
            campaign_template_id: The campaign template this campaign draws its assets from. <p>Binds the campaign to a single source template: every asset must come from this template's asset templates, and one from another template is refused at `BatchCreateCampaignAsset`. Immutable once set. Every campaign has one: a campaign's language and its assets' blueprints both come from its template. <p>Templates are AWS-authored and read-only — they are discovered through `SearchCampaignTemplates` and `GetCampaignTemplate`, and there is no create, update or delete operation for one. <p>The template's id only: a campaign template has no ARN (DG-084). The member keeps the `<Resource>Id` name, which is the convention for referencing another resource from a body.
            sender_email: The address every email of this campaign is sent from. <p>Printable ASCII only, with no spaces or line breaks, or field code `PATTERN_MISMATCH`. Then three rules, all checked when the sender is set. Its domain must exactly match, ignoring case, the domain of the partner's alliance lead email in AWS Partner Central (a subdomain does not), or field code `SENDER_DOMAIN_NOT_ALLIANCE_LEAD`. Then, for a sender at example.com, DNS must hold the CNAME `dkim._domainkey.example.com` → `dkim._domainkey.md02.com` (field code `SENDER_DOMAIN_DKIM_MISSING`) and a DMARC record, one TXT `_dmarc.example.com` starting `v=DMARC1` with a `p` of `none`, `quarantine` or `reject` (field code `SENDER_DOMAIN_DMARC_MISSING`). Both DNS codes are reported together when both records are missing. <p>A partner who can't satisfy them can't set a sender, so can't run email campaigns. A shared mail provider's domain, such as gmail.com, can't carry the records. Optional here: a campaign with no sender can be created and edited, but its email assets cannot be activated until one is set.
            privacy_policy_url: The URL of the partner's privacy policy, linked from every email and landing page footer. Optional here: a campaign whose emails or landing pages show it cannot activate them until one is set.
            partner_address: The partner's physical postal address, shown in every email footer and as a landing page's contact line. Optional here: an email that shows it cannot activate until one is set. A landing page that shows it publishes it empty when it is unset, and a document's footer then prints the partner's name alone.
            partner_badge: The partner's badge — a tier or designation badge from AWS Partner Badge Manager — shown in every badge slot of the campaign's emails, landing pages and documents. Optional: until one is set, every badge slot shows the Standalone AWS Partner badge. <p>A PNG or JPEG of at most 2 MB, staged like an asset image and checked the same way: it must have passed the staging scan (`SCAN_REJECTED`, or `SCAN_IN_PROGRESS` while it is pending), and its bytes must be the format its name says (`IMAGE_FORMAT_NOT_SUPPORTED`). Any shape is accepted: a badge is drawn whole, never cropped. Content moderation judges it when an asset that shows it is activated.
            email_target: The campaign's send audience — a CSV of recipient email addresses. <p>The campaign's *target*: who the campaign is sent to, as distinct from a `CampaignAsset`, which is the content that is sent. It sits on the campaign and not on the activation call because a partner assembles it in the same wizard flow that sets the name and the dates — and because attaching it here means it is validated, staged and resolved to a count before anything is activated, rather than at the last click. <p>Required format: a header row naming the email column `Email`, `E-mail`, `Email Address` or `E-mail Address` — compared without case, spaces or punctuation. Other columns are permitted and ignored, and with two email columns the first is used. A file without such a header is refused with field code `EMAIL_COLUMN_MISSING`: the address column is never guessed. The rows reach the delivery platform's importer as the partner wrote them — a partner's audience is never rewritten. <p>At most 5 MB, checked against the object's size before anything is copied, and at most 10,000 distinct addresses, refused with `RECIPIENT_LIST_TOO_LARGE`. A file with no valid address at all is refused with `RECIPIENT_LIST_EMPTY`; otherwise rows without a usable address are not a refusal: they are skipped and counted, and `GetCampaign` reports the counts. Optional here, because a campaign is a container and holds no state to be incomplete in — but an email asset cannot be activated without it, so the requirement moved to the point of activation. <p>Editable at any time, and an edit reaches the delivery platform only when an asset is activated after it. Each email activation loads the audience into a contact list of its own, so an address taken off the file is not sent to by the next activation. <p>The bytes are write-only. No response returns a URL or an `S3Uri` for this file; `GetCampaign` returns the scan verdict, when the list was attached and how its rows resolved, and nothing more.
            email_target_engagement_group_ids: Engagement groups whose contacts the campaign's emails will also go to: the `Id`s `ListEngagementGroups` returns (AWS Partner Central Selling). 1–10, each named once. <p>Each group is named once: a repeated id is refused with field code `INVALID_VALUE`. Not checked against your groups when saved. StartCampaignAssetActivationTask resolves them to recipients. On a stage that can't resolve groups yet, Start refuses an email while groups are set (`ENGAGEMENT_GROUPS_UNAVAILABLE`), rather than send to `EmailTarget` alone.
            target_audience: Advisory targeting metadata. Refined later, and not validated here.
            estimated_budget: What the partner expects the campaign to cost.
            total_budget: The campaign's total budget.
            start_on: The first day of the campaign's run window. Not after `EndOn` (`ValidationException`, `INVALID_VALUE`).
            end_on: The last day of the campaign's run window, inclusive and in UTC. Not in the past: the campaign completes at the UTC midnight after it (see `CampaignState`). A scheduled send must fall on or before it. Optional here, but required before any asset activates: until it is set, GetCampaign's `ActivationIssues` reports `END_ON_MISSING` and StartCampaignAssetActivationTask refuses (`CAMPAIGN_INCOMPLETE`). Set it with UpdateCampaign.
            client_token: Idempotency token. Same token within 24h returns existing resource.
            tags: Tags to apply at creation. Tag-on-create rather than create-then-tag is a Tagris requirement, not a convenience: it is what lets a tag-based access control policy govern the creation itself. A campaign created untagged and tagged a moment later is briefly outside any such policy. <p>A key beginning `aws:` (any case) is reserved for AWS-applied system tags and is refused with `ValidationException`, as is a key repeated in the list; nothing is created. The tags are recorded before the campaign is written, so a create that cannot record them fails and creates nothing. A retry with the same `ClientToken` returns the campaign the first attempt created and does not re-apply tags — use `TagResource` to change them afterwards. `ListTagsForResource` returns them.

        Raises:
            capo_partnercentral_marketing.errors.access_denied_exception.AccessDeniedException: You do not have sufficient access to perform this action. An IAM denial carries no `Reason`. A refusal for the caller's Partner Central state carries one, so a client tells the two apart by its presence.
            capo_partnercentral_marketing.errors.internal_server_exception.InternalServerException: An unexpected error occurred during the processing of the request.
            capo_partnercentral_marketing.errors.throttling_exception.ThrottlingException: The request was denied due to request throttling.
            capo_partnercentral_marketing.errors.validation_exception.ValidationException: The input fails to satisfy the constraints specified by the service. A caller branches on `Reason`, and where the rejection is attributable to particular fields it reads `FieldList` rather than parsing `Message`, which is prose and may change.
            capo_partnercentral_marketing.errors.conflict_exception.ConflictException: The request conflicts with the current state of the resource.
            capo_partnercentral_marketing.errors.resource_not_found_exception.ResourceNotFoundException: The specified resource does not exist.
            capo_partnercentral_marketing.errors.service_quota_exceeded_exception.ServiceQuotaExceededException: The request exceeds a service quota.
            capo_partnercentral_marketing.errors.UnknownServiceError: The service returned an error code this client does not model.

        Examples:
            Create a campaign

            >>> client.create(catalog='AWS', name='Q4 GenAI Campaign', campaign_template_id='tmpl-a1b2c3d4e5f6g', total_budget={'Amount': '25000.00', 'CurrencyCode': 'USD'}, start_on='2026-11-01', end_on='2026-12-31')
        """

        def _handler(
            req: "OperationRequest[capo_partnercentral_marketing.types.create_campaign_request.CreateCampaignRequest]",
        ) -> OperationResponse[
            "capo_partnercentral_marketing.types.create_campaign_response.CreateCampaignResponse"
        ]:
            import capo_partnercentral_marketing._operations.aws_partner_demand_generator.create_campaign

            output, http_response = (
                capo_partnercentral_marketing._operations.aws_partner_demand_generator.create_campaign.create_campaign(
                    req.options, req.input
                )
            )
            return OperationResponse(output=output, response=http_response)

        def _redact_input(
            input_: "capo_partnercentral_marketing.types.create_campaign_request.CreateCampaignRequest",
        ) -> dict[str, Any]:
            import capo_partnercentral_marketing.types.create_campaign_request

            return capo_partnercentral_marketing.types.create_campaign_request.redact_sensitive(
                input_
            )

        interceptors_, options_ = self._service.operation_options(
            config_overrides,
            OperationLogging("CreateCampaign", redact_input=_redact_input),
        )
        input_: capo_partnercentral_marketing.types.create_campaign_request.CreateCampaignRequest = {
            "catalog": catalog,
            "name": name,
            "campaign_template_id": campaign_template_id,
        }
        if sender_email is not None:
            input_["sender_email"] = sender_email
        if privacy_policy_url is not None:
            input_["privacy_policy_url"] = privacy_policy_url
        if partner_address is not None:
            input_["partner_address"] = partner_address
        if partner_badge is not None:
            input_["partner_badge"] = partner_badge
        if email_target is not None:
            input_["email_target"] = email_target
        if email_target_engagement_group_ids is not None:
            input_["email_target_engagement_group_ids"] = (
                email_target_engagement_group_ids
            )
        if target_audience is not None:
            input_["target_audience"] = target_audience
        if estimated_budget is not None:
            input_["estimated_budget"] = estimated_budget
        if total_budget is not None:
            input_["total_budget"] = total_budget
        if start_on is not None:
            input_["start_on"] = start_on
        if end_on is not None:
            input_["end_on"] = end_on
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

    def read(
        self,
        catalog: "capo_partnercentral_marketing.types.catalog.Catalog",
        campaign_identifier: "capo_partnercentral_marketing.types.campaign_identifier.CampaignIdentifier",
        *,
        config_overrides: Optional[PartnerCentralMarketingClientConfig] = None,
    ) -> (
        "capo_partnercentral_marketing.types.get_campaign_response.GetCampaignResponse"
    ):
        """Retrieves a campaign by its identifier.

        Args:
            catalog: The catalog (AWS or Sandbox).
            campaign_identifier: The campaign identifier.

        Raises:
            capo_partnercentral_marketing.errors.access_denied_exception.AccessDeniedException: You do not have sufficient access to perform this action. An IAM denial carries no `Reason`. A refusal for the caller's Partner Central state carries one, so a client tells the two apart by its presence.
            capo_partnercentral_marketing.errors.internal_server_exception.InternalServerException: An unexpected error occurred during the processing of the request.
            capo_partnercentral_marketing.errors.throttling_exception.ThrottlingException: The request was denied due to request throttling.
            capo_partnercentral_marketing.errors.validation_exception.ValidationException: The input fails to satisfy the constraints specified by the service. A caller branches on `Reason`, and where the rejection is attributable to particular fields it reads `FieldList` rather than parsing `Message`, which is prose and may change.
            capo_partnercentral_marketing.errors.resource_not_found_exception.ResourceNotFoundException: The specified resource does not exist.
            capo_partnercentral_marketing.errors.UnknownServiceError: The service returned an error code this client does not model.

        Examples:
            Get a campaign

            >>> client.read(catalog='AWS', campaign_identifier='camp-5Hq2m8x4k1p9w')
        """

        def _handler(
            req: "OperationRequest[capo_partnercentral_marketing.types.get_campaign_request.GetCampaignRequest]",
        ) -> OperationResponse[
            "capo_partnercentral_marketing.types.get_campaign_response.GetCampaignResponse"
        ]:
            import capo_partnercentral_marketing._operations.aws_partner_demand_generator.get_campaign

            output, http_response = (
                capo_partnercentral_marketing._operations.aws_partner_demand_generator.get_campaign.get_campaign(
                    req.options, req.input
                )
            )
            return OperationResponse(output=output, response=http_response)

        def _redact_output(
            output: "capo_partnercentral_marketing.types.get_campaign_response.GetCampaignResponse",
        ) -> dict[str, Any]:
            import capo_partnercentral_marketing.types.get_campaign_response

            return capo_partnercentral_marketing.types.get_campaign_response.redact_sensitive(
                output
            )

        interceptors_, options_ = self._service.operation_options(
            config_overrides,
            OperationLogging("GetCampaign", redact_output=_redact_output),
        )
        input_: capo_partnercentral_marketing.types.get_campaign_request.GetCampaignRequest = {
            "catalog": catalog,
            "campaign_identifier": campaign_identifier,
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
        catalog: "capo_partnercentral_marketing.types.catalog.Catalog",
        campaign_identifier: "capo_partnercentral_marketing.types.campaign_identifier.CampaignIdentifier",
        *,
        config_overrides: Optional[PartnerCentralMarketingClientConfig] = None,
        name: Optional[
            "capo_partnercentral_marketing.types.campaign_name.CampaignName"
        ] = None,
        sender_email: Optional[
            "capo_partnercentral_marketing.types.sender_email.SenderEmail"
        ] = None,
        privacy_policy_url: Optional[
            "capo_partnercentral_marketing.types.privacy_policy_url.PrivacyPolicyUrl"
        ] = None,
        partner_address: Optional[
            "capo_partnercentral_marketing.types.partner_address.PartnerAddress"
        ] = None,
        partner_badge: Optional[
            "capo_partnercentral_marketing.types.file_ref.FileRef"
        ] = None,
        email_target: Optional[
            "capo_partnercentral_marketing.types.file_ref.FileRef"
        ] = None,
        email_target_engagement_group_ids: Optional[
            "capo_partnercentral_marketing.types.engagement_group_id_list.EngagementGroupIdList"
        ] = None,
        social_connections: Optional[
            "capo_partnercentral_marketing.types.campaign_social_connections.CampaignSocialConnections"
        ] = None,
        estimated_budget: Optional[
            "capo_partnercentral_marketing.types.monetary_value.MonetaryValue"
        ] = None,
        total_budget: Optional[
            "capo_partnercentral_marketing.types.monetary_value.MonetaryValue"
        ] = None,
        target_audience: Optional[
            "capo_partnercentral_marketing.types.target_audience.TargetAudience"
        ] = None,
        client_token: Optional[
            "capo_partnercentral_marketing.types.client_token.ClientToken"
        ] = None,
        start_on: Optional[
            "capo_partnercentral_marketing.types.utc_date.UtcDate"
        ] = None,
        end_on: Optional["capo_partnercentral_marketing.types.utc_date.UtcDate"] = None,
    ) -> "capo_partnercentral_marketing.types.update_campaign_response.UpdateCampaignResponse":
        """Edits a campaign in place. Partial update: an omitted field is left unchanged, which is the standard meaning of an `Update` verb — a full replacement would be a `Put`. Change-only, with no way to clear a field back to empty, because the campaign's file members cannot round-trip: they are written as an `s3://` reference and read back as a URL or as metadata, so a replacement payload could not resend an unchanged recipient list without re-uploading it. Refused while an activation task runs (`CAMPAIGN_ACTIVATION_IN_PROGRESS`) and once the campaign is completed (`CAMPAIGN_COMPLETED`, the UTC date is after its `EndOn`). Last-writer-wins, with no concurrency token: this is low-contention metadata owned by one partner.

        Args:
            catalog: The catalog (AWS or Sandbox).
            campaign_identifier: The campaign identifier.
            name: The display name.
            sender_email: Sets or replaces the address the campaign's emails are sent from. Checked by the same three rules as on `CreateCampaign`, with the same codes, but only when it differs, ignoring case, from the stored sender: re-sending the stored one is not checked, and `StartCampaignAssetActivationTask` re-checks it before an email activates. <p>Replaces, never clears: like every member of this operation, an omitted value leaves the sender as it was, and there is no way to remove one once set.
            privacy_policy_url: Sets or replaces the URL of the partner's privacy policy. Replaces, never clears.
            partner_address: Sets or replaces the partner's postal address. Replaces, never clears.
            partner_badge: Sets or replaces the partner's badge, checked exactly as on `CreateCampaign`. Replaces, never clears: upload the Standalone AWS Partner badge to show it again. The badge an asset already published keeps showing on it until that asset is activated again.
            email_target: Replaces the campaign's attached recipient list. <p>The referenced object is copied and pinned again on every call that supplies it, so the pinned copy always reflects the *last* `UpdateCampaign` that named one. Editing the source object in your own bucket without calling this operation again has no effect. <p>Replaces, never detaches: a partner can swap the list but cannot remove it.
            email_target_engagement_group_ids: Engagement groups whose contacts the campaign's emails will also go to (see `CreateCampaign`). Replaces the stored list; never clears it. <p>As on `CreateCampaign`: each group once (`INVALID_VALUE` otherwise), not checked against your groups when saved, and resolved at Start where the stage can (`ENGAGEMENT_GROUPS_UNAVAILABLE` where it can't).
            social_connections: Sets the account the campaign's social posts publish from, per platform. Each platform named replaces that platform's choice; a platform not named keeps its own. Replaces, never clears. <p>Not checked against your connections here: a connection can be deleted at any time, so the activation checks the choice. See `Campaign$SocialConnections`.
            estimated_budget: What the partner expects the campaign to cost.
            total_budget: The campaign's total budget.
            target_audience: Target audience configuration.
            client_token: Idempotency token. Accepted and not stored: this is a change-only partial update with last-writer-wins, so re-applying the same call produces the same result and the same response. There is nothing a replay cache would protect.
            start_on: The first day of the campaign's run window. Not after `EndOn` (`ValidationException`, `INVALID_VALUE`).
            end_on: The last day of the campaign's run window, inclusive and in UTC. Editable only while the campaign is open, like everything else here: once the stored `EndOn` has passed the campaign is completed and this update is refused (`CAMPAIGN_COMPLETED`). Refused with `ValidationException` (`INVALID_VALUE`) when it is in the past, or earlier than the day of a scheduled send on one of the campaign's assets: move or cancel that send first. Setting it to today ends the campaign at the next UTC midnight.

        Raises:
            capo_partnercentral_marketing.errors.access_denied_exception.AccessDeniedException: You do not have sufficient access to perform this action. An IAM denial carries no `Reason`. A refusal for the caller's Partner Central state carries one, so a client tells the two apart by its presence.
            capo_partnercentral_marketing.errors.internal_server_exception.InternalServerException: An unexpected error occurred during the processing of the request.
            capo_partnercentral_marketing.errors.throttling_exception.ThrottlingException: The request was denied due to request throttling.
            capo_partnercentral_marketing.errors.validation_exception.ValidationException: The input fails to satisfy the constraints specified by the service. A caller branches on `Reason`, and where the rejection is attributable to particular fields it reads `FieldList` rather than parsing `Message`, which is prose and may change.
            capo_partnercentral_marketing.errors.conflict_exception.ConflictException: The request conflicts with the current state of the resource.
            capo_partnercentral_marketing.errors.resource_not_found_exception.ResourceNotFoundException: The specified resource does not exist.
            capo_partnercentral_marketing.errors.UnknownServiceError: The service returned an error code this client does not model.

        Examples:
            Rename a campaign and raise its budget

            >>> client.update(catalog='AWS', campaign_identifier='camp-5Hq2m8x4k1p9w', name='Q4 GenAI Campaign (EMEA)', total_budget={'Amount': '40000.00', 'CurrencyCode': 'USD'})
        """

        def _handler(
            req: "OperationRequest[capo_partnercentral_marketing.types.update_campaign_request.UpdateCampaignRequest]",
        ) -> OperationResponse[
            "capo_partnercentral_marketing.types.update_campaign_response.UpdateCampaignResponse"
        ]:
            import capo_partnercentral_marketing._operations.aws_partner_demand_generator.update_campaign

            output, http_response = (
                capo_partnercentral_marketing._operations.aws_partner_demand_generator.update_campaign.update_campaign(
                    req.options, req.input
                )
            )
            return OperationResponse(output=output, response=http_response)

        def _redact_input(
            input_: "capo_partnercentral_marketing.types.update_campaign_request.UpdateCampaignRequest",
        ) -> dict[str, Any]:
            import capo_partnercentral_marketing.types.update_campaign_request

            return capo_partnercentral_marketing.types.update_campaign_request.redact_sensitive(
                input_
            )

        interceptors_, options_ = self._service.operation_options(
            config_overrides,
            OperationLogging("UpdateCampaign", redact_input=_redact_input),
        )
        input_: capo_partnercentral_marketing.types.update_campaign_request.UpdateCampaignRequest = {
            "catalog": catalog,
            "campaign_identifier": campaign_identifier,
        }
        if name is not None:
            input_["name"] = name
        if sender_email is not None:
            input_["sender_email"] = sender_email
        if privacy_policy_url is not None:
            input_["privacy_policy_url"] = privacy_policy_url
        if partner_address is not None:
            input_["partner_address"] = partner_address
        if partner_badge is not None:
            input_["partner_badge"] = partner_badge
        if email_target is not None:
            input_["email_target"] = email_target
        if email_target_engagement_group_ids is not None:
            input_["email_target_engagement_group_ids"] = (
                email_target_engagement_group_ids
            )
        if social_connections is not None:
            input_["social_connections"] = social_connections
        if estimated_budget is not None:
            input_["estimated_budget"] = estimated_budget
        if total_budget is not None:
            input_["total_budget"] = total_budget
        if target_audience is not None:
            input_["target_audience"] = target_audience
        if client_token is None:
            client_token = str(uuid.uuid4())
        input_["client_token"] = client_token
        if start_on is not None:
            input_["start_on"] = start_on
        if end_on is not None:
            input_["end_on"] = end_on

        response = execute_pipeline(
            OperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        response.response.close()
        return response.output

    def delete(
        self,
        catalog: "capo_partnercentral_marketing.types.catalog.Catalog",
        campaign_identifier: "capo_partnercentral_marketing.types.campaign_identifier.CampaignIdentifier",
        *,
        config_overrides: Optional[PartnerCentralMarketingClientConfig] = None,
    ) -> None:
        """Permanently deletes a campaign, its assets and their stored files. A hard delete with no undo: the campaign leaves ListCampaigns and every read of it returns ResourceNotFoundException. Its tags are removed with it. Refused with ConflictException while the campaign has a live asset (`CAMPAIGN_HAS_ACTIVE_ASSETS`), because deleting the record would orphan what the delivery platform still serves or sends: deactivate those assets first. Also refused while an activation task is running (`CAMPAIGN_ACTIVATION_IN_PROGRESS`). A completed campaign can be deleted. Idempotent in effect: deleting a campaign that is already gone returns ResourceNotFoundException, and nothing is left behind by a retry.

        Args:
            catalog: The catalog (AWS or Sandbox).
            campaign_identifier: The campaign to delete.

        Raises:
            capo_partnercentral_marketing.errors.access_denied_exception.AccessDeniedException: You do not have sufficient access to perform this action. An IAM denial carries no `Reason`. A refusal for the caller's Partner Central state carries one, so a client tells the two apart by its presence.
            capo_partnercentral_marketing.errors.internal_server_exception.InternalServerException: An unexpected error occurred during the processing of the request.
            capo_partnercentral_marketing.errors.throttling_exception.ThrottlingException: The request was denied due to request throttling.
            capo_partnercentral_marketing.errors.validation_exception.ValidationException: The input fails to satisfy the constraints specified by the service. A caller branches on `Reason`, and where the rejection is attributable to particular fields it reads `FieldList` rather than parsing `Message`, which is prose and may change.
            capo_partnercentral_marketing.errors.conflict_exception.ConflictException: The request conflicts with the current state of the resource.
            capo_partnercentral_marketing.errors.resource_not_found_exception.ResourceNotFoundException: The specified resource does not exist.
            capo_partnercentral_marketing.errors.UnknownServiceError: The service returned an error code this client does not model.

        Examples:
            Delete a campaign

            >>> client.delete(catalog='AWS', campaign_identifier='camp-5Hq2m8x4k1p9w')
        """

        def _handler(
            req: "OperationRequest[capo_partnercentral_marketing.types.delete_campaign_request.DeleteCampaignRequest]",
        ) -> OperationResponse[None]:
            import capo_partnercentral_marketing._operations.aws_partner_demand_generator.delete_campaign

            output, http_response = (
                capo_partnercentral_marketing._operations.aws_partner_demand_generator.delete_campaign.delete_campaign(
                    req.options, req.input
                )
            )
            return OperationResponse(output=output, response=http_response)

        interceptors_, options_ = self._service.operation_options(
            config_overrides, OperationLogging("DeleteCampaign")
        )
        input_: capo_partnercentral_marketing.types.delete_campaign_request.DeleteCampaignRequest = {
            "catalog": catalog,
            "campaign_identifier": campaign_identifier,
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
        catalog: "capo_partnercentral_marketing.types.catalog.Catalog",
        *,
        config_overrides: Optional[PartnerCentralMarketingClientConfig] = None,
        campaign_identifiers: Optional[
            "capo_partnercentral_marketing.types.campaign_identifier_list.CampaignIdentifierList"
        ] = None,
        name: Optional[
            "capo_partnercentral_marketing.types.campaign_name.CampaignName"
        ] = None,
        states: Optional[
            "capo_partnercentral_marketing.types.campaign_state_list.CampaignStateList"
        ] = None,
        sort: Optional[
            "capo_partnercentral_marketing.types.campaign_sort.CampaignSort"
        ] = None,
        max_results: Optional[
            "capo_partnercentral_marketing.types.max_results.MaxResults"
        ] = None,
        next_token: Optional[
            "capo_partnercentral_marketing.types.next_token.NextToken"
        ] = None,
    ) -> "capo_partnercentral_marketing.types.list_campaigns_response.ListCampaignsResponse":
        """Lists campaigns with optional filters and pagination.

        Args:
            catalog: The catalog (AWS or Sandbox).
            campaign_identifiers: Only these campaigns, each named by its id or its campaign ARN. A campaign that does not exist, was deleted, or whose ARN names another account or catalog is left out rather than refused.
            name: Only campaigns whose name contains this, compared case-insensitively.
            states: Only campaigns in one of these states.
            sort: The order of the results. Default: `CREATED_AT`, `DESCENDING`.
            max_results: Maximum results per page.
            next_token: Pagination token. Bound to the filters and sort it was issued for: a request that changes `CampaignIdentifiers`, `Name`, `States` or `Sort` between pages is refused with `ValidationException`. `MaxResults` may change.

        Raises:
            capo_partnercentral_marketing.errors.access_denied_exception.AccessDeniedException: You do not have sufficient access to perform this action. An IAM denial carries no `Reason`. A refusal for the caller's Partner Central state carries one, so a client tells the two apart by its presence.
            capo_partnercentral_marketing.errors.internal_server_exception.InternalServerException: An unexpected error occurred during the processing of the request.
            capo_partnercentral_marketing.errors.throttling_exception.ThrottlingException: The request was denied due to request throttling.
            capo_partnercentral_marketing.errors.validation_exception.ValidationException: The input fails to satisfy the constraints specified by the service. A caller branches on `Reason`, and where the rejection is attributable to particular fields it reads `FieldList` rather than parsing `Message`, which is prose and may change.
            capo_partnercentral_marketing.errors.UnknownServiceError: The service returned an error code this client does not model.

        Examples:
            List campaigns

            >>> client.list(catalog='AWS')
            Name the campaigns a page links to

            >>> client.list(catalog='AWS', campaign_identifiers=['arn:aws:partnercentral:us-east-1:123456789012:catalog/AWS/campaign/camp-5Hq2m8x4k1p9w', 'camp-8Rt3w6y1n4b2v'])
            Search active campaigns by name, by launch date

            >>> client.list(catalog='AWS', name='genai', states=['ACTIVE'], sort={'SortBy': 'START_ON', 'SortOrder': 'ASCENDING'}, max_results=20)
        """

        def _handler(
            req: "OperationRequest[capo_partnercentral_marketing.types.list_campaigns_request.ListCampaignsRequest]",
        ) -> OperationResponse[
            "capo_partnercentral_marketing.types.list_campaigns_response.ListCampaignsResponse"
        ]:
            import capo_partnercentral_marketing._operations.aws_partner_demand_generator.list_campaigns

            output, http_response = (
                capo_partnercentral_marketing._operations.aws_partner_demand_generator.list_campaigns.list_campaigns(
                    req.options, req.input
                )
            )
            return OperationResponse(output=output, response=http_response)

        interceptors_, options_ = self._service.operation_options(
            config_overrides, OperationLogging("ListCampaigns")
        )
        input_: capo_partnercentral_marketing.types.list_campaigns_request.ListCampaignsRequest = {
            "catalog": catalog
        }
        if campaign_identifiers is not None:
            input_["campaign_identifiers"] = campaign_identifiers
        if name is not None:
            input_["name"] = name
        if states is not None:
            input_["states"] = states
        if sort is not None:
            input_["sort"] = sort
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

    def batch_create_campaign_asset(
        self,
        catalog: "capo_partnercentral_marketing.types.catalog.Catalog",
        campaign_identifier: "capo_partnercentral_marketing.types.campaign_identifier.CampaignIdentifier",
        entries: "capo_partnercentral_marketing.types.batch_create_campaign_asset_entries.BatchCreateCampaignAssetEntries",
        *,
        config_overrides: Optional[PartnerCentralMarketingClientConfig] = None,
    ) -> "capo_partnercentral_marketing.types.batch_create_campaign_asset_response.BatchCreateCampaignAssetResponse":
        """Instantiates one or more of the campaign template's blueprints as assets of this campaign. The only asset-create operation: DG-038 deleted the singular CreateCampaignAsset, and AWS Batch Operations makes exposing a singular alongside a batch optional ("which MAY actually be exposed in addition"). It also replaced kit instantiation -- CreateCampaign creates zero assets, so this is the only path by which an asset comes into existence. Errors here are whole-request only, and nothing is written when one is thrown. Per-entry failures ride in the response's `Errors` list with a 200. ServiceQuotaExceededException is deliberately absent: a campaign holds at most one asset per blueprint (I-15), so the ceiling is the size of the bound kit and a request of unique valid entries cannot exceed it.

        Args:
            catalog: The catalog (AWS or Sandbox).
            campaign_identifier: The campaign identifier.
            entries: The blueprints to instantiate, one entry each.

        Raises:
            capo_partnercentral_marketing.errors.access_denied_exception.AccessDeniedException: You do not have sufficient access to perform this action. An IAM denial carries no `Reason`. A refusal for the caller's Partner Central state carries one, so a client tells the two apart by its presence.
            capo_partnercentral_marketing.errors.internal_server_exception.InternalServerException: An unexpected error occurred during the processing of the request.
            capo_partnercentral_marketing.errors.throttling_exception.ThrottlingException: The request was denied due to request throttling.
            capo_partnercentral_marketing.errors.validation_exception.ValidationException: The input fails to satisfy the constraints specified by the service. A caller branches on `Reason`, and where the rejection is attributable to particular fields it reads `FieldList` rather than parsing `Message`, which is prose and may change.
            capo_partnercentral_marketing.errors.conflict_exception.ConflictException: The request conflicts with the current state of the resource.
            capo_partnercentral_marketing.errors.resource_not_found_exception.ResourceNotFoundException: The specified resource does not exist.
            capo_partnercentral_marketing.errors.UnknownServiceError: The service returned an error code this client does not model.

        Examples:
            Instantiate two of the kit's blueprints

            >>> client.batch_create_campaign_asset(catalog='AWS', campaign_identifier='camp-5Hq2m8x4k1p9w', entries=[{'SourceAssetTemplateIdentifier': 'ta000000email'}, {'SourceAssetTemplateIdentifier': 'ta0000000lp01'}])
            A partial batch: one entry names a blueprint the campaign's template does not carry

            >>> client.batch_create_campaign_asset(catalog='AWS', campaign_identifier='camp-5Hq2m8x4k1p9w', entries=[{'SourceAssetTemplateIdentifier': 'ta000000email'}, {'SourceAssetTemplateIdentifier': 'ta00000absent'}])
        """

        def _handler(
            req: "OperationRequest[capo_partnercentral_marketing.types.batch_create_campaign_asset_request.BatchCreateCampaignAssetRequest]",
        ) -> OperationResponse[
            "capo_partnercentral_marketing.types.batch_create_campaign_asset_response.BatchCreateCampaignAssetResponse"
        ]:
            import capo_partnercentral_marketing._operations.aws_partner_demand_generator.batch_create_campaign_asset

            output, http_response = (
                capo_partnercentral_marketing._operations.aws_partner_demand_generator.batch_create_campaign_asset.batch_create_campaign_asset(
                    req.options, req.input
                )
            )
            return OperationResponse(output=output, response=http_response)

        interceptors_, options_ = self._service.operation_options(
            config_overrides, OperationLogging("BatchCreateCampaignAsset")
        )
        input_: capo_partnercentral_marketing.types.batch_create_campaign_asset_request.BatchCreateCampaignAssetRequest = {
            "catalog": catalog,
            "campaign_identifier": campaign_identifier,
            "entries": entries,
        }

        response = execute_pipeline(
            OperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        response.response.close()
        return response.output

    def deactivate_campaign_asset(
        self,
        catalog: "capo_partnercentral_marketing.types.catalog.Catalog",
        campaign_identifier: "capo_partnercentral_marketing.types.campaign_identifier.CampaignIdentifier",
        campaign_asset_identifier: "capo_partnercentral_marketing.types.campaign_asset_id.CampaignAssetId",
        *,
        config_overrides: Optional[PartnerCentralMarketingClientConfig] = None,
    ) -> "capo_partnercentral_marketing.types.deactivate_campaign_asset_response.DeactivateCampaignAssetResponse":
        """Stops a live campaign asset: an email's scheduled send is withdrawn, a social post is removed before it publishes. On a completed campaign, it also removes a published document, banner or landing page. Synchronous, and safe to repeat. Does not delete the asset record, so a stopped email or social post can be started again. Not every asset can be stopped, and the reasons differ in kind. An email that has begun sending **cannot** be recalled: the send is gone. A document, a banner or a landing page is **refused** with `ASSET_NOT_DEACTIVATABLE` until the campaign has completed (the UTC date is after its `EndOn`). Until then the partner fixes one in place by updating it and activating it again, which keeps its URL, so every email that already linked to it keeps working. Once the campaign has completed, the removal is permanent, because a completed campaign can't activate anything again: - A document's published PDF is deleted. Its URL stops serving within about a minute (the CDN revalidates), and `PublicUrl` is no longer returned. Anything that linked to it, such as a landing page's download button or a sent email, reaches an error page. The export still contains the document. - A banner's or landing page's published object is taken down at the delivery platform, and the images the partner put on it are deleted. A landing page stops capturing leads, and its `PublicUrl` is no longer returned. A partner site that embedded a banner shows nothing there. The platform's own CDN can keep serving a copy a visitor already cached, which collects nothing. A landing page and a document it links to can be removed in either order.

        Args:
            catalog: The catalog (AWS or Sandbox).
            campaign_identifier: The campaign identifier.
            campaign_asset_identifier: The asset identifier.

        Raises:
            capo_partnercentral_marketing.errors.access_denied_exception.AccessDeniedException: You do not have sufficient access to perform this action. An IAM denial carries no `Reason`. A refusal for the caller's Partner Central state carries one, so a client tells the two apart by its presence.
            capo_partnercentral_marketing.errors.internal_server_exception.InternalServerException: An unexpected error occurred during the processing of the request.
            capo_partnercentral_marketing.errors.throttling_exception.ThrottlingException: The request was denied due to request throttling.
            capo_partnercentral_marketing.errors.validation_exception.ValidationException: The input fails to satisfy the constraints specified by the service. A caller branches on `Reason`, and where the rejection is attributable to particular fields it reads `FieldList` rather than parsing `Message`, which is prose and may change.
            capo_partnercentral_marketing.errors.conflict_exception.ConflictException: The request conflicts with the current state of the resource.
            capo_partnercentral_marketing.errors.resource_not_found_exception.ResourceNotFoundException: The specified resource does not exist.
            capo_partnercentral_marketing.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        def _handler(
            req: "OperationRequest[capo_partnercentral_marketing.types.deactivate_campaign_asset_request.DeactivateCampaignAssetRequest]",
        ) -> OperationResponse[
            "capo_partnercentral_marketing.types.deactivate_campaign_asset_response.DeactivateCampaignAssetResponse"
        ]:
            import capo_partnercentral_marketing._operations.aws_partner_demand_generator.deactivate_campaign_asset

            output, http_response = (
                capo_partnercentral_marketing._operations.aws_partner_demand_generator.deactivate_campaign_asset.deactivate_campaign_asset(
                    req.options, req.input
                )
            )
            return OperationResponse(output=output, response=http_response)

        interceptors_, options_ = self._service.operation_options(
            config_overrides, OperationLogging("DeactivateCampaignAsset")
        )
        input_: capo_partnercentral_marketing.types.deactivate_campaign_asset_request.DeactivateCampaignAssetRequest = {
            "catalog": catalog,
            "campaign_identifier": campaign_identifier,
            "campaign_asset_identifier": campaign_asset_identifier,
        }

        response = execute_pipeline(
            OperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        response.response.close()
        return response.output

    def delete_campaign_asset(
        self,
        catalog: "capo_partnercentral_marketing.types.catalog.Catalog",
        campaign_identifier: "capo_partnercentral_marketing.types.campaign_identifier.CampaignIdentifier",
        campaign_asset_identifier: "capo_partnercentral_marketing.types.campaign_asset_id.CampaignAssetId",
        *,
        config_overrides: Optional[PartnerCentralMarketingClientConfig] = None,
    ) -> None:
        """Permanently deletes a campaign asset.

        Args:
            catalog: The catalog (AWS or Sandbox).
            campaign_identifier: The campaign identifier.
            campaign_asset_identifier: The asset identifier.

        Raises:
            capo_partnercentral_marketing.errors.access_denied_exception.AccessDeniedException: You do not have sufficient access to perform this action. An IAM denial carries no `Reason`. A refusal for the caller's Partner Central state carries one, so a client tells the two apart by its presence.
            capo_partnercentral_marketing.errors.internal_server_exception.InternalServerException: An unexpected error occurred during the processing of the request.
            capo_partnercentral_marketing.errors.throttling_exception.ThrottlingException: The request was denied due to request throttling.
            capo_partnercentral_marketing.errors.validation_exception.ValidationException: The input fails to satisfy the constraints specified by the service. A caller branches on `Reason`, and where the rejection is attributable to particular fields it reads `FieldList` rather than parsing `Message`, which is prose and may change.
            capo_partnercentral_marketing.errors.conflict_exception.ConflictException: The request conflicts with the current state of the resource.
            capo_partnercentral_marketing.errors.resource_not_found_exception.ResourceNotFoundException: The specified resource does not exist.
            capo_partnercentral_marketing.errors.UnknownServiceError: The service returned an error code this client does not model.

        Examples:
            Delete an asset

            >>> client.delete_campaign_asset(catalog='AWS', campaign_identifier='camp-5Hq2m8x4k1p9w', campaign_asset_identifier='ast-4b81e0c9f2a7b')
        """

        def _handler(
            req: "OperationRequest[capo_partnercentral_marketing.types.delete_campaign_asset_request.DeleteCampaignAssetRequest]",
        ) -> OperationResponse[None]:
            import capo_partnercentral_marketing._operations.aws_partner_demand_generator.delete_campaign_asset

            output, http_response = (
                capo_partnercentral_marketing._operations.aws_partner_demand_generator.delete_campaign_asset.delete_campaign_asset(
                    req.options, req.input
                )
            )
            return OperationResponse(output=output, response=http_response)

        interceptors_, options_ = self._service.operation_options(
            config_overrides, OperationLogging("DeleteCampaignAsset")
        )
        input_: capo_partnercentral_marketing.types.delete_campaign_asset_request.DeleteCampaignAssetRequest = {
            "catalog": catalog,
            "campaign_identifier": campaign_identifier,
            "campaign_asset_identifier": campaign_asset_identifier,
        }

        response = execute_pipeline(
            OperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        response.response.close()
        return response.output

    def get_campaign_asset(
        self,
        catalog: "capo_partnercentral_marketing.types.catalog.Catalog",
        campaign_identifier: "capo_partnercentral_marketing.types.campaign_identifier.CampaignIdentifier",
        campaign_asset_identifier: "capo_partnercentral_marketing.types.campaign_asset_id.CampaignAssetId",
        *,
        config_overrides: Optional[PartnerCentralMarketingClientConfig] = None,
    ) -> "capo_partnercentral_marketing.types.get_campaign_asset_response.GetCampaignAssetResponse":
        """Retrieves an asset by its identifier.

        Args:
            catalog: The catalog (AWS or Sandbox).
            campaign_identifier: The campaign identifier.
            campaign_asset_identifier: The asset identifier.

        Raises:
            capo_partnercentral_marketing.errors.access_denied_exception.AccessDeniedException: You do not have sufficient access to perform this action. An IAM denial carries no `Reason`. A refusal for the caller's Partner Central state carries one, so a client tells the two apart by its presence.
            capo_partnercentral_marketing.errors.internal_server_exception.InternalServerException: An unexpected error occurred during the processing of the request.
            capo_partnercentral_marketing.errors.throttling_exception.ThrottlingException: The request was denied due to request throttling.
            capo_partnercentral_marketing.errors.validation_exception.ValidationException: The input fails to satisfy the constraints specified by the service. A caller branches on `Reason`, and where the rejection is attributable to particular fields it reads `FieldList` rather than parsing `Message`, which is prose and may change.
            capo_partnercentral_marketing.errors.resource_not_found_exception.ResourceNotFoundException: The specified resource does not exist.
            capo_partnercentral_marketing.errors.UnknownServiceError: The service returned an error code this client does not model.

        Examples:
            Get an asset

            >>> client.get_campaign_asset(catalog='AWS', campaign_identifier='camp-5Hq2m8x4k1p9w', campaign_asset_identifier='ast-4b81e0c9f2a7b')
        """

        def _handler(
            req: "OperationRequest[capo_partnercentral_marketing.types.get_campaign_asset_request.GetCampaignAssetRequest]",
        ) -> OperationResponse[
            "capo_partnercentral_marketing.types.get_campaign_asset_response.GetCampaignAssetResponse"
        ]:
            import capo_partnercentral_marketing._operations.aws_partner_demand_generator.get_campaign_asset

            output, http_response = (
                capo_partnercentral_marketing._operations.aws_partner_demand_generator.get_campaign_asset.get_campaign_asset(
                    req.options, req.input
                )
            )
            return OperationResponse(output=output, response=http_response)

        def _redact_output(
            output: "capo_partnercentral_marketing.types.get_campaign_asset_response.GetCampaignAssetResponse",
        ) -> dict[str, Any]:
            import capo_partnercentral_marketing.types.get_campaign_asset_response

            return capo_partnercentral_marketing.types.get_campaign_asset_response.redact_sensitive(
                output
            )

        interceptors_, options_ = self._service.operation_options(
            config_overrides,
            OperationLogging("GetCampaignAsset", redact_output=_redact_output),
        )
        input_: capo_partnercentral_marketing.types.get_campaign_asset_request.GetCampaignAssetRequest = {
            "catalog": catalog,
            "campaign_identifier": campaign_identifier,
            "campaign_asset_identifier": campaign_asset_identifier,
        }

        response = execute_pipeline(
            OperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        response.response.close()
        return response.output

    def get_campaign_asset_activation_task(
        self,
        catalog: "capo_partnercentral_marketing.types.catalog.Catalog",
        campaign_identifier: "capo_partnercentral_marketing.types.campaign_identifier.CampaignIdentifier",
        *,
        config_overrides: Optional[PartnerCentralMarketingClientConfig] = None,
    ) -> "capo_partnercentral_marketing.types.get_campaign_asset_activation_task_response.GetCampaignAssetActivationTaskResponse":
        """Reads a campaign's current activation task. Keyed on the **campaign**, with no task identifier, because a campaign has at most one activation task: runs are serialised, so there is no collection to address into. The caller always holds the task id anyway, because Start returned it — the id is a correlation value, not an address. Returns the campaign's most recent task. A new task overwrites the previous one, so this is not a history: the durable per-asset record is on the assets themselves. Returns ResourceNotFoundException when the campaign has never had a task, or when its last one has expired.

        Args:
            catalog: The catalog (AWS or Sandbox).
            campaign_identifier: The campaign whose current task to read. This addresses the task, and also authorizes the call.

        Raises:
            capo_partnercentral_marketing.errors.access_denied_exception.AccessDeniedException: You do not have sufficient access to perform this action. An IAM denial carries no `Reason`. A refusal for the caller's Partner Central state carries one, so a client tells the two apart by its presence.
            capo_partnercentral_marketing.errors.internal_server_exception.InternalServerException: An unexpected error occurred during the processing of the request.
            capo_partnercentral_marketing.errors.throttling_exception.ThrottlingException: The request was denied due to request throttling.
            capo_partnercentral_marketing.errors.validation_exception.ValidationException: The input fails to satisfy the constraints specified by the service. A caller branches on `Reason`, and where the rejection is attributable to particular fields it reads `FieldList` rather than parsing `Message`, which is prose and may change.
            capo_partnercentral_marketing.errors.resource_not_found_exception.ResourceNotFoundException: The specified resource does not exist.
            capo_partnercentral_marketing.errors.UnknownServiceError: The service returned an error code this client does not model.

        Examples:
            Read a finished task where one asset failed

            >>> client.get_campaign_asset_activation_task(catalog='AWS', campaign_identifier='camp-5Hq2m8x4k1p9w')
        """

        def _handler(
            req: "OperationRequest[capo_partnercentral_marketing.types.get_campaign_asset_activation_task_request.GetCampaignAssetActivationTaskRequest]",
        ) -> OperationResponse[
            "capo_partnercentral_marketing.types.get_campaign_asset_activation_task_response.GetCampaignAssetActivationTaskResponse"
        ]:
            import capo_partnercentral_marketing._operations.aws_partner_demand_generator.get_campaign_asset_activation_task

            output, http_response = (
                capo_partnercentral_marketing._operations.aws_partner_demand_generator.get_campaign_asset_activation_task.get_campaign_asset_activation_task(
                    req.options, req.input
                )
            )
            return OperationResponse(output=output, response=http_response)

        interceptors_, options_ = self._service.operation_options(
            config_overrides, OperationLogging("GetCampaignAssetActivationTask")
        )
        input_: capo_partnercentral_marketing.types.get_campaign_asset_activation_task_request.GetCampaignAssetActivationTaskRequest = {
            "catalog": catalog,
            "campaign_identifier": campaign_identifier,
        }

        response = execute_pipeline(
            OperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        response.response.close()
        return response.output

    def get_campaign_asset_export_task(
        self,
        catalog: "capo_partnercentral_marketing.types.catalog.Catalog",
        campaign_identifier: "capo_partnercentral_marketing.types.campaign_identifier.CampaignIdentifier",
        campaign_asset_export_task_identifier: "capo_partnercentral_marketing.types.campaign_asset_export_task_id.CampaignAssetExportTaskId",
        *,
        config_overrides: Optional[PartnerCentralMarketingClientConfig] = None,
    ) -> "capo_partnercentral_marketing.types.get_campaign_asset_export_task_response.GetCampaignAssetExportTaskResponse":
        """Retrieves a campaign asset export task by its identifier, reporting its status and, when the task is COMPLETED, a freshly minted short-lived presigned URL for downloading the ZIP archive. The download URL is minted on each call and is valid for at most 15 minutes; clients should download promptly rather than caching it. When the task has FAILED, FailureReason explains why. Poll this operation (roughly every 2-5 seconds) until the task reaches a terminal state.

        Args:
            catalog: The catalog (AWS or Sandbox).
            campaign_identifier: The campaign that owns the export task. Accepts the campaign id or ARN. Required so the read is authorized on campaign/{CampaignId}; the task must belong to this campaign or the request resolves to not-found.
            campaign_asset_export_task_identifier: The export task to retrieve: the `Id` StartCampaignAssetExportTask returned (`etsk-…`). An id only. An export task has no ARN: none is returned, recorded or authorized on (the read authorizes on its campaign), so there is no ARN to accept (DG-063 D-35).

        Raises:
            capo_partnercentral_marketing.errors.access_denied_exception.AccessDeniedException: You do not have sufficient access to perform this action. An IAM denial carries no `Reason`. A refusal for the caller's Partner Central state carries one, so a client tells the two apart by its presence.
            capo_partnercentral_marketing.errors.internal_server_exception.InternalServerException: An unexpected error occurred during the processing of the request.
            capo_partnercentral_marketing.errors.throttling_exception.ThrottlingException: The request was denied due to request throttling.
            capo_partnercentral_marketing.errors.validation_exception.ValidationException: The input fails to satisfy the constraints specified by the service. A caller branches on `Reason`, and where the rejection is attributable to particular fields it reads `FieldList` rather than parsing `Message`, which is prose and may change.
            capo_partnercentral_marketing.errors.resource_not_found_exception.ResourceNotFoundException: The specified resource does not exist.
            capo_partnercentral_marketing.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        def _handler(
            req: "OperationRequest[capo_partnercentral_marketing.types.get_campaign_asset_export_task_request.GetCampaignAssetExportTaskRequest]",
        ) -> OperationResponse[
            "capo_partnercentral_marketing.types.get_campaign_asset_export_task_response.GetCampaignAssetExportTaskResponse"
        ]:
            import capo_partnercentral_marketing._operations.aws_partner_demand_generator.get_campaign_asset_export_task

            output, http_response = (
                capo_partnercentral_marketing._operations.aws_partner_demand_generator.get_campaign_asset_export_task.get_campaign_asset_export_task(
                    req.options, req.input
                )
            )
            return OperationResponse(output=output, response=http_response)

        interceptors_, options_ = self._service.operation_options(
            config_overrides, OperationLogging("GetCampaignAssetExportTask")
        )
        input_: capo_partnercentral_marketing.types.get_campaign_asset_export_task_request.GetCampaignAssetExportTaskRequest = {
            "catalog": catalog,
            "campaign_identifier": campaign_identifier,
            "campaign_asset_export_task_identifier": campaign_asset_export_task_identifier,
        }

        response = execute_pipeline(
            OperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        response.response.close()
        return response.output

    def list_campaign_assets(
        self,
        catalog: "capo_partnercentral_marketing.types.catalog.Catalog",
        campaign_identifier: "capo_partnercentral_marketing.types.campaign_identifier.CampaignIdentifier",
        *,
        config_overrides: Optional[PartnerCentralMarketingClientConfig] = None,
        max_results: Optional[
            "capo_partnercentral_marketing.types.max_results.MaxResults"
        ] = None,
        next_token: Optional[
            "capo_partnercentral_marketing.types.next_token.NextToken"
        ] = None,
    ) -> "capo_partnercentral_marketing.types.list_campaign_assets_response.ListCampaignAssetsResponse":
        """Lists assets for a campaign with pagination.

        Args:
            catalog: The catalog (AWS or Sandbox).
            campaign_identifier: The campaign identifier.
            max_results: Maximum results per page.
            next_token: Pagination token.

        Raises:
            capo_partnercentral_marketing.errors.access_denied_exception.AccessDeniedException: You do not have sufficient access to perform this action. An IAM denial carries no `Reason`. A refusal for the caller's Partner Central state carries one, so a client tells the two apart by its presence.
            capo_partnercentral_marketing.errors.internal_server_exception.InternalServerException: An unexpected error occurred during the processing of the request.
            capo_partnercentral_marketing.errors.throttling_exception.ThrottlingException: The request was denied due to request throttling.
            capo_partnercentral_marketing.errors.validation_exception.ValidationException: The input fails to satisfy the constraints specified by the service. A caller branches on `Reason`, and where the rejection is attributable to particular fields it reads `FieldList` rather than parsing `Message`, which is prose and may change.
            capo_partnercentral_marketing.errors.resource_not_found_exception.ResourceNotFoundException: The specified resource does not exist.
            capo_partnercentral_marketing.errors.UnknownServiceError: The service returned an error code this client does not model.

        Examples:
            List assets for a campaign

            >>> client.list_campaign_assets(catalog='AWS', campaign_identifier='camp-5Hq2m8x4k1p9w')
        """

        def _handler(
            req: "OperationRequest[capo_partnercentral_marketing.types.list_campaign_assets_request.ListCampaignAssetsRequest]",
        ) -> OperationResponse[
            "capo_partnercentral_marketing.types.list_campaign_assets_response.ListCampaignAssetsResponse"
        ]:
            import capo_partnercentral_marketing._operations.aws_partner_demand_generator.list_campaign_assets

            output, http_response = (
                capo_partnercentral_marketing._operations.aws_partner_demand_generator.list_campaign_assets.list_campaign_assets(
                    req.options, req.input
                )
            )
            return OperationResponse(output=output, response=http_response)

        interceptors_, options_ = self._service.operation_options(
            config_overrides, OperationLogging("ListCampaignAssets")
        )
        input_: capo_partnercentral_marketing.types.list_campaign_assets_request.ListCampaignAssetsRequest = {
            "catalog": catalog,
            "campaign_identifier": campaign_identifier,
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

    def start_campaign_asset_activation_task(
        self,
        catalog: "capo_partnercentral_marketing.types.catalog.Catalog",
        campaign_identifier: "capo_partnercentral_marketing.types.campaign_identifier.CampaignIdentifier",
        campaign_asset_identifiers: "capo_partnercentral_marketing.types.campaign_asset_identifiers.CampaignAssetIdentifiers",
        *,
        config_overrides: Optional[PartnerCentralMarketingClientConfig] = None,
        client_token: Optional[
            "capo_partnercentral_marketing.types.client_token.ClientToken"
        ] = None,
    ) -> "capo_partnercentral_marketing.types.start_campaign_asset_activation_task_response.StartCampaignAssetActivationTaskResponse":
        """Activates 1–25 of a campaign's assets as one ordered unit, and returns a task to poll. Takes a **list** because the service owns the ordering. Assets link to one another by URL — an email's call-to-action carries the landing page's URL, the landing page's download field carries the document's — and a URL does not exist until the asset it points at is activated. Those edges are derived by the service from the campaign's pinned template, so reconstructing and topologically sorting them is work the service has already done, and getting it wrong arms an email with a dead link. Name every asset you want live and the service sequences them; "activate everything" is the list with every id in it, which ListCampaignAssets already gave you. Asynchronous, because activating an asset installs or arms behaviour that runs later and an email activation bulk-loads its audience into the delivery platform. Everything decidable **without** a write to the delivery platform is evaluated before this returns; everything else lands on the task. A refusal that applies to one asset does not fail the request: that asset is on the task already FAILED, with its reason, and the rest run. A refusal that applies to the whole request — a malformed list, an unknown campaign, another task already running on this campaign, this service's service-linked role being deleted (ConflictException `SERVICE_LINKED_ROLE_DELETION_IN_PROGRESS`), a campaign setting an asset in the request needs (ValidationException `CAMPAIGN_INCOMPLETE`), a campaign sender that no longer passes `CreateCampaign`'s sender rules while the request names an email (ValidationException with no `FieldList`, whose message ends with one `Reason: <code>` token per failed rule: `PATTERN_MISMATCH`, `SENDER_DOMAIN_NOT_ALLIANCE_LEAD`, or `SENDER_DOMAIN_DKIM_MISSING` and/or `SENDER_DOMAIN_DMARC_MISSING`) — is thrown, and nothing starts. One task runs on a campaign at a time. A second concurrent call is refused with ConflictException / CAMPAIGN_ACTIVATION_IN_PROGRESS, whose `ResourceId` names the task already holding the campaign. Two tasks over *disjoint* asset sets are refused too: the guard is deliberately campaign-wide, because overlapping runs made the per-asset status misleading rather than merely contended.

        Args:
            catalog: The catalog (AWS or Sandbox).
            campaign_identifier: The campaign identifier, which also authorizes the call.
            campaign_asset_identifiers: The assets to activate, in any order — the service derives the dependency order and ignores the order given here.
            client_token: Idempotency token. Two requests carrying the same token are one request, and the second returns the first one's task rather than starting a second. The deduplication window is the **life of the task record**, not a fixed number of hours: replaying a token after the task has expired starts a new task. Stated because a caller would otherwise assume the usual few-hour guarantee.

        Raises:
            capo_partnercentral_marketing.errors.access_denied_exception.AccessDeniedException: You do not have sufficient access to perform this action. An IAM denial carries no `Reason`. A refusal for the caller's Partner Central state carries one, so a client tells the two apart by its presence.
            capo_partnercentral_marketing.errors.internal_server_exception.InternalServerException: An unexpected error occurred during the processing of the request.
            capo_partnercentral_marketing.errors.throttling_exception.ThrottlingException: The request was denied due to request throttling.
            capo_partnercentral_marketing.errors.validation_exception.ValidationException: The input fails to satisfy the constraints specified by the service. A caller branches on `Reason`, and where the rejection is attributable to particular fields it reads `FieldList` rather than parsing `Message`, which is prose and may change.
            capo_partnercentral_marketing.errors.conflict_exception.ConflictException: The request conflicts with the current state of the resource.
            capo_partnercentral_marketing.errors.resource_not_found_exception.ResourceNotFoundException: The specified resource does not exist.
            capo_partnercentral_marketing.errors.UnknownServiceError: The service returned an error code this client does not model.

        Examples:
            Activate a whole campaign kit

            >>> client.start_campaign_asset_activation_task(catalog='AWS', campaign_identifier='camp-5Hq2m8x4k1p9w', campaign_asset_identifiers=['ast-4b81e0c9f2a7b', 'ast-9f3c1a2b7d40e', 'ast-2k7m4p9x1c6qd', 'ast-7w3n8r5t2h1ya'])
            Some assets refused, the rest started anyway

            >>> client.start_campaign_asset_activation_task(catalog='AWS', campaign_identifier='camp-5Hq2m8x4k1p9w', campaign_asset_identifiers=['ast-4b81e0c9f2a7b', 'ast-9f3c1a2b7d40e', 'ast-2k7m4p9x1c6qd', 'ast-7w3n8r5t2h1ya'])
            Every asset refused, so the task is FAILED at once

            >>> client.start_campaign_asset_activation_task(catalog='AWS', campaign_identifier='camp-5Hq2m8x4k1p9w', campaign_asset_identifiers=['ast-2k7m4p9x1c6qd'])
        """

        def _handler(
            req: "OperationRequest[capo_partnercentral_marketing.types.start_campaign_asset_activation_task_request.StartCampaignAssetActivationTaskRequest]",
        ) -> OperationResponse[
            "capo_partnercentral_marketing.types.start_campaign_asset_activation_task_response.StartCampaignAssetActivationTaskResponse"
        ]:
            import capo_partnercentral_marketing._operations.aws_partner_demand_generator.start_campaign_asset_activation_task

            output, http_response = (
                capo_partnercentral_marketing._operations.aws_partner_demand_generator.start_campaign_asset_activation_task.start_campaign_asset_activation_task(
                    req.options, req.input
                )
            )
            return OperationResponse(output=output, response=http_response)

        interceptors_, options_ = self._service.operation_options(
            config_overrides, OperationLogging("StartCampaignAssetActivationTask")
        )
        input_: capo_partnercentral_marketing.types.start_campaign_asset_activation_task_request.StartCampaignAssetActivationTaskRequest = {
            "catalog": catalog,
            "campaign_identifier": campaign_identifier,
            "campaign_asset_identifiers": campaign_asset_identifiers,
        }
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

    def start_campaign_asset_export_task(
        self,
        catalog: "capo_partnercentral_marketing.types.catalog.Catalog",
        campaign_identifier: "capo_partnercentral_marketing.types.campaign_identifier.CampaignIdentifier",
        *,
        config_overrides: Optional[PartnerCentralMarketingClientConfig] = None,
        client_token: Optional[
            "capo_partnercentral_marketing.types.client_token.ClientToken"
        ] = None,
    ) -> "capo_partnercentral_marketing.types.start_campaign_asset_export_task_response.StartCampaignAssetExportTaskResponse":
        """Starts an asynchronous task that packages a campaign's assets into a single downloadable ZIP archive. Fire-and-return: the campaign is validated (it must exist and not be cancelled), a task record is persisted, an asynchronous execution is started, and the task id is returned with status IN_PROGRESS. This operation does not inspect assets — all resolution, exclusion, and failure are determined by the execution and surfaced only by GetCampaignAssetExportTask. Every campaign is exportable, including one never activated, because renderable assets are composed on demand at export time rather than requiring finished, launched deliverables.

        Args:
            catalog: The catalog (AWS or Sandbox).
            campaign_identifier: The campaign whose assets are exported. Accepts the campaign id or ARN.
            client_token: Idempotency token. Two requests carrying the same token within the dedup window are one request and return the same task id.

        Raises:
            capo_partnercentral_marketing.errors.access_denied_exception.AccessDeniedException: You do not have sufficient access to perform this action. An IAM denial carries no `Reason`. A refusal for the caller's Partner Central state carries one, so a client tells the two apart by its presence.
            capo_partnercentral_marketing.errors.internal_server_exception.InternalServerException: An unexpected error occurred during the processing of the request.
            capo_partnercentral_marketing.errors.throttling_exception.ThrottlingException: The request was denied due to request throttling.
            capo_partnercentral_marketing.errors.validation_exception.ValidationException: The input fails to satisfy the constraints specified by the service. A caller branches on `Reason`, and where the rejection is attributable to particular fields it reads `FieldList` rather than parsing `Message`, which is prose and may change.
            capo_partnercentral_marketing.errors.resource_not_found_exception.ResourceNotFoundException: The specified resource does not exist.
            capo_partnercentral_marketing.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        def _handler(
            req: "OperationRequest[capo_partnercentral_marketing.types.start_campaign_asset_export_task_request.StartCampaignAssetExportTaskRequest]",
        ) -> OperationResponse[
            "capo_partnercentral_marketing.types.start_campaign_asset_export_task_response.StartCampaignAssetExportTaskResponse"
        ]:
            import capo_partnercentral_marketing._operations.aws_partner_demand_generator.start_campaign_asset_export_task

            output, http_response = (
                capo_partnercentral_marketing._operations.aws_partner_demand_generator.start_campaign_asset_export_task.start_campaign_asset_export_task(
                    req.options, req.input
                )
            )
            return OperationResponse(output=output, response=http_response)

        interceptors_, options_ = self._service.operation_options(
            config_overrides, OperationLogging("StartCampaignAssetExportTask")
        )
        input_: capo_partnercentral_marketing.types.start_campaign_asset_export_task_request.StartCampaignAssetExportTaskRequest = {
            "catalog": catalog,
            "campaign_identifier": campaign_identifier,
        }
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

    def update_campaign_asset(
        self,
        catalog: "capo_partnercentral_marketing.types.catalog.Catalog",
        campaign_identifier: "capo_partnercentral_marketing.types.campaign_identifier.CampaignIdentifier",
        campaign_asset_identifier: "capo_partnercentral_marketing.types.campaign_asset_id.CampaignAssetId",
        *,
        config_overrides: Optional[PartnerCentralMarketingClientConfig] = None,
        field_values: Optional[
            "capo_partnercentral_marketing.types.field_value_input_list.FieldValueInputList"
        ] = None,
        layout: Optional[
            "capo_partnercentral_marketing.types.layout_option_value.LayoutOptionValue"
        ] = None,
        send_mode: Optional[
            "capo_partnercentral_marketing.types.send_mode.SendMode"
        ] = None,
        scheduled_send_at: Optional[
            "capo_partnercentral_marketing.types.timestamp.Timestamp"
        ] = None,
        client_token: Optional[
            "capo_partnercentral_marketing.types.client_token.ClientToken"
        ] = None,
    ) -> "capo_partnercentral_marketing.types.update_campaign_asset_response.UpdateCampaignAssetResponse":
        """Updates an asset's field values, layout or send time. Refused with `ConflictException` while the campaign's running activation task still owns the asset (`ASSET_START_IN_PROGRESS`), and for a live email or social post (`ASSET_ALREADY_ACTIVE`): deactivate it first.

                Args:
                    catalog: The catalog (AWS or Sandbox).
                    campaign_identifier: The campaign identifier.
                    campaign_asset_identifier: The asset identifier.
                    field_values: Value-only updates to the asset's pinned template fields, keyed by FieldId. The field schema (labels, descriptions, constraints, placeholders, image defaults) is service-owned and pinned at instantiation, so clients send only the values they are changing. Fields omitted keep their stored values; send the entry with `Value` omitted to clear one. Named `FieldValues` to match the member it edits on `CampaignAsset`, which is the same concept read back. It was `templateFieldUpdates`; the two names for one concept were the defect, not the length.
                    layout: Selects a multi-layout asset's layout: one of the values in `CampaignAsset.layout.options`. PATCH: omitted leaves the selection unchanged, and there is no way to clear it. A value that is not one of the asset's options — or any value on a single-layout asset — is a plain `ValidationException`, and nothing in the call is applied. Every pinned field stays writable whichever layout is selected.
                    send_mode: When a **sendable** asset (`EMAIL`, `SOCIAL_POST`) sends: on activation, or at `ScheduledSendAt`. A mode beside a value rather than a union, on purpose: `ScheduledSendAt` stays a plain `Timestamp`, and the precedent is EventBridge Scheduler's `FlexibleTimeWindow { Mode, MaximumWindowInMinutes }`. The pair is checked as one, and a request where they disagree is refused with `ValidationException` (`INVALID_VALUE`, naming the member) and applies nothing: - `SCHEDULED` requires `ScheduledSendAt`; a reschedule resends `SCHEDULED` with the new time; - `ON_ACTIVATION` forbids `ScheduledSendAt`, and drops any time already stored; - `ScheduledSendAt` without `SendMode` is refused. PATCH: omitted leaves both unchanged. Until a mode is chosen the asset reports `SEND_MODE_MISSING` and does not activate: no default, because an unchosen send mails the real audience. Rejected with `ValidationException` (`NOT_SUPPORTED_FOR_CATEGORY`) for a category that has no send (`LANDING_PAGE`, `DOCUMENT`, `BANNER_AD`). Like every other edit, it reaches the delivery platform at the asset's next activation, and a live email or social post refuses it (`ASSET_ALREADY_ACTIVE`): deactivate first.
                    scheduled_send_at: The send time, with `SendMode: SCHEDULED` and only then. See `SendMode`. Must be at least an hour out (`SEND_WINDOW_TOO_SOON`), unless it is the time already stored: resending the stored mode and time changes nothing and is accepted, so a form that always resubmits does not trip the window. Must also fall on or before the campaign's `EndOn` (by the end of that UTC day): refused with `ValidationException` (`INVALID_VALUE`) otherwise, so nothing is scheduled to send after the campaign completes. Was `scheduleDate`, a `YYYY-MM-DD` string. Retyped because a date alone cannot express a send *time*, which is the whole point of a schedule — and because the resource already spelled the same concept `ScheduledSendAt` on the activation responses. Two spellings of one concept on one resource was the defect.
                    client_token: Idempotency token. Retry-safety only — this is **not** a concurrency token, and sequential edits to one field are last-writer-wins.

                Raises:
                    capo_partnercentral_marketing.errors.access_denied_exception.AccessDeniedException: You do not have sufficient access to perform this action. An IAM denial carries no `Reason`. A refusal for the caller's Partner Central state carries one, so a client tells the two apart by its presence.
                    capo_partnercentral_marketing.errors.internal_server_exception.InternalServerException: An unexpected error occurred during the processing of the request.
                    capo_partnercentral_marketing.errors.throttling_exception.ThrottlingException: The request was denied due to request throttling.
                    capo_partnercentral_marketing.errors.validation_exception.ValidationException: The input fails to satisfy the constraints specified by the service. A caller branches on `Reason`, and where the rejection is attributable to particular fields it reads `FieldList` rather than parsing `Message`, which is prose and may change.
                    capo_partnercentral_marketing.errors.conflict_exception.ConflictException: The request conflicts with the current state of the resource.
                    capo_partnercentral_marketing.errors.resource_not_found_exception.ResourceNotFoundException: The specified resource does not exist.
                    capo_partnercentral_marketing.errors.UnknownServiceError: The service returned an error code this client does not model.

                Examples:
                    Update asset content

                    >>> client.update_campaign_asset(catalog='AWS', campaign_identifier='camp-5Hq2m8x4k1p9w', campaign_asset_identifier='ast-4b81e0c9f2a7b', field_values=[{'FieldId': 'Subject', 'Value': {'Text': 'New subject line'}}])
                    Reschedule a sendable asset

                    >>> client.update_campaign_asset(catalog='AWS', campaign_identifier='camp-5Hq2m8x4k1p9w', campaign_asset_identifier='ast-4b81e0c9f2a7b', send_mode='SCHEDULED', scheduled_send_at=1793491200, client_token='f2a7c1e4-9b3d-4a51-8e6f-0c2d5b8a7e13')
                    Copy an image from a previous campaign's asset
                    The image already stored on another of your assets is copied into this field. It is checked
        against this field's constraints and not scanned again. The call also needs
        partnercentral:GetCampaignAsset on the source campaign.

                    >>> client.update_campaign_asset(catalog='AWS', campaign_identifier='camp-5Hq2m8x4k1p9w', campaign_asset_identifier='ast-4b81e0c9f2a7b', field_values=[{'FieldId': 'HeaderImage', 'Value': {'CampaignAssetImage': {'CampaignIdentifier': 'camp-2Lp7d9f3j6s1z', 'CampaignAssetIdentifier': 'ast-0f9e8d7c6b5a2', 'FieldId': 'HeaderImage'}}}])
                    Use a suggested image from Build with AI
                    The URL Build with AI returned for a suggested image is sent unchanged as imageReference. The
        image is copied into this asset and not scanned. Any other URL is refused.

                    >>> client.update_campaign_asset(catalog='AWS', campaign_identifier='camp-5Hq2m8x4k1p9w', campaign_asset_identifier='ast-4b81e0c9f2a7b', field_values=[{'FieldId': 'HeaderImage', 'Value': {'ImageReference': 'https://d111111abcdef8.cloudfront.net/suggested-image-url-from-build-with-ai.jpg'}}])
                    An update refused for two fields at once
                    Every failed field is reported in one refusal, and nothing applies — a declined image and an
        over-long headline arrive together in `fieldList`, each with its own `code`. This replaced a
        read-path `fileDetails[]` report (DG-040 Decision 11), so a partner handles image and text
        failures the same way.

                    >>> client.update_campaign_asset(catalog='AWS', campaign_identifier='camp-5Hq2m8x4k1p9w', campaign_asset_identifier='ast-4b81e0c9f2a7b', field_values=[{'FieldId': 'HeaderImage', 'Value': {'ImageReference': 's3://staging-bucket/123456789012/hero.png?versionId=v1'}}, {'FieldId': 'Headline', 'Value': {'Text': 'This headline is far longer than the field allows'}}])
        """

        def _handler(
            req: "OperationRequest[capo_partnercentral_marketing.types.update_campaign_asset_request.UpdateCampaignAssetRequest]",
        ) -> OperationResponse[
            "capo_partnercentral_marketing.types.update_campaign_asset_response.UpdateCampaignAssetResponse"
        ]:
            import capo_partnercentral_marketing._operations.aws_partner_demand_generator.update_campaign_asset

            output, http_response = (
                capo_partnercentral_marketing._operations.aws_partner_demand_generator.update_campaign_asset.update_campaign_asset(
                    req.options, req.input
                )
            )
            return OperationResponse(output=output, response=http_response)

        def _redact_input(
            input_: "capo_partnercentral_marketing.types.update_campaign_asset_request.UpdateCampaignAssetRequest",
        ) -> dict[str, Any]:
            import capo_partnercentral_marketing.types.update_campaign_asset_request

            return capo_partnercentral_marketing.types.update_campaign_asset_request.redact_sensitive(
                input_
            )

        interceptors_, options_ = self._service.operation_options(
            config_overrides,
            OperationLogging("UpdateCampaignAsset", redact_input=_redact_input),
        )
        input_: capo_partnercentral_marketing.types.update_campaign_asset_request.UpdateCampaignAssetRequest = {
            "catalog": catalog,
            "campaign_identifier": campaign_identifier,
            "campaign_asset_identifier": campaign_asset_identifier,
        }
        if field_values is not None:
            input_["field_values"] = field_values
        if layout is not None:
            input_["layout"] = layout
        if send_mode is not None:
            input_["send_mode"] = send_mode
        if scheduled_send_at is not None:
            input_["scheduled_send_at"] = scheduled_send_at
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


class AsyncCampaignResource:
    def __init__(self, service: AsyncPartnerCentralMarketingClient) -> None:
        self._service = service

    async def create(
        self,
        catalog: "capo_partnercentral_marketing.types.catalog.Catalog",
        name: "capo_partnercentral_marketing.types.campaign_name.CampaignName",
        campaign_template_id: "capo_partnercentral_marketing.types.campaign_template_id.CampaignTemplateId",
        *,
        config_overrides: Optional[AsyncPartnerCentralMarketingClientConfig] = None,
        sender_email: Optional[
            "capo_partnercentral_marketing.types.sender_email.SenderEmail"
        ] = None,
        privacy_policy_url: Optional[
            "capo_partnercentral_marketing.types.privacy_policy_url.PrivacyPolicyUrl"
        ] = None,
        partner_address: Optional[
            "capo_partnercentral_marketing.types.partner_address.PartnerAddress"
        ] = None,
        partner_badge: Optional[
            "capo_partnercentral_marketing.types.file_ref.FileRef"
        ] = None,
        email_target: Optional[
            "capo_partnercentral_marketing.types.file_ref.FileRef"
        ] = None,
        email_target_engagement_group_ids: Optional[
            "capo_partnercentral_marketing.types.engagement_group_id_list.EngagementGroupIdList"
        ] = None,
        target_audience: Optional[
            "capo_partnercentral_marketing.types.target_audience.TargetAudience"
        ] = None,
        estimated_budget: Optional[
            "capo_partnercentral_marketing.types.monetary_value.MonetaryValue"
        ] = None,
        total_budget: Optional[
            "capo_partnercentral_marketing.types.monetary_value.MonetaryValue"
        ] = None,
        start_on: Optional[
            "capo_partnercentral_marketing.types.utc_date.UtcDate"
        ] = None,
        end_on: Optional["capo_partnercentral_marketing.types.utc_date.UtcDate"] = None,
        client_token: Optional[
            "capo_partnercentral_marketing.types.client_token.ClientToken"
        ] = None,
        tags: Optional["capo_partnercentral_marketing.types.tag_list.TagList"] = None,
    ) -> "capo_partnercentral_marketing.types.create_campaign_response.CreateCampaignResponse":
        """Creates a new marketing campaign. Returns the identity of the new campaign, not the campaign. Growing a response is backward compatible and shrinking one is not, and the caller's next step is a `GetCampaign` anyway — a write that supplies an audience cannot report its scan verdict, because that is decided after it commits.

        Args:
            catalog: The catalog (AWS or Sandbox).
            name: The display name.
            campaign_template_id: The campaign template this campaign draws its assets from. <p>Binds the campaign to a single source template: every asset must come from this template's asset templates, and one from another template is refused at `BatchCreateCampaignAsset`. Immutable once set. Every campaign has one: a campaign's language and its assets' blueprints both come from its template. <p>Templates are AWS-authored and read-only — they are discovered through `SearchCampaignTemplates` and `GetCampaignTemplate`, and there is no create, update or delete operation for one. <p>The template's id only: a campaign template has no ARN (DG-084). The member keeps the `<Resource>Id` name, which is the convention for referencing another resource from a body.
            sender_email: The address every email of this campaign is sent from. <p>Printable ASCII only, with no spaces or line breaks, or field code `PATTERN_MISMATCH`. Then three rules, all checked when the sender is set. Its domain must exactly match, ignoring case, the domain of the partner's alliance lead email in AWS Partner Central (a subdomain does not), or field code `SENDER_DOMAIN_NOT_ALLIANCE_LEAD`. Then, for a sender at example.com, DNS must hold the CNAME `dkim._domainkey.example.com` → `dkim._domainkey.md02.com` (field code `SENDER_DOMAIN_DKIM_MISSING`) and a DMARC record, one TXT `_dmarc.example.com` starting `v=DMARC1` with a `p` of `none`, `quarantine` or `reject` (field code `SENDER_DOMAIN_DMARC_MISSING`). Both DNS codes are reported together when both records are missing. <p>A partner who can't satisfy them can't set a sender, so can't run email campaigns. A shared mail provider's domain, such as gmail.com, can't carry the records. Optional here: a campaign with no sender can be created and edited, but its email assets cannot be activated until one is set.
            privacy_policy_url: The URL of the partner's privacy policy, linked from every email and landing page footer. Optional here: a campaign whose emails or landing pages show it cannot activate them until one is set.
            partner_address: The partner's physical postal address, shown in every email footer and as a landing page's contact line. Optional here: an email that shows it cannot activate until one is set. A landing page that shows it publishes it empty when it is unset, and a document's footer then prints the partner's name alone.
            partner_badge: The partner's badge — a tier or designation badge from AWS Partner Badge Manager — shown in every badge slot of the campaign's emails, landing pages and documents. Optional: until one is set, every badge slot shows the Standalone AWS Partner badge. <p>A PNG or JPEG of at most 2 MB, staged like an asset image and checked the same way: it must have passed the staging scan (`SCAN_REJECTED`, or `SCAN_IN_PROGRESS` while it is pending), and its bytes must be the format its name says (`IMAGE_FORMAT_NOT_SUPPORTED`). Any shape is accepted: a badge is drawn whole, never cropped. Content moderation judges it when an asset that shows it is activated.
            email_target: The campaign's send audience — a CSV of recipient email addresses. <p>The campaign's *target*: who the campaign is sent to, as distinct from a `CampaignAsset`, which is the content that is sent. It sits on the campaign and not on the activation call because a partner assembles it in the same wizard flow that sets the name and the dates — and because attaching it here means it is validated, staged and resolved to a count before anything is activated, rather than at the last click. <p>Required format: a header row naming the email column `Email`, `E-mail`, `Email Address` or `E-mail Address` — compared without case, spaces or punctuation. Other columns are permitted and ignored, and with two email columns the first is used. A file without such a header is refused with field code `EMAIL_COLUMN_MISSING`: the address column is never guessed. The rows reach the delivery platform's importer as the partner wrote them — a partner's audience is never rewritten. <p>At most 5 MB, checked against the object's size before anything is copied, and at most 10,000 distinct addresses, refused with `RECIPIENT_LIST_TOO_LARGE`. A file with no valid address at all is refused with `RECIPIENT_LIST_EMPTY`; otherwise rows without a usable address are not a refusal: they are skipped and counted, and `GetCampaign` reports the counts. Optional here, because a campaign is a container and holds no state to be incomplete in — but an email asset cannot be activated without it, so the requirement moved to the point of activation. <p>Editable at any time, and an edit reaches the delivery platform only when an asset is activated after it. Each email activation loads the audience into a contact list of its own, so an address taken off the file is not sent to by the next activation. <p>The bytes are write-only. No response returns a URL or an `S3Uri` for this file; `GetCampaign` returns the scan verdict, when the list was attached and how its rows resolved, and nothing more.
            email_target_engagement_group_ids: Engagement groups whose contacts the campaign's emails will also go to: the `Id`s `ListEngagementGroups` returns (AWS Partner Central Selling). 1–10, each named once. <p>Each group is named once: a repeated id is refused with field code `INVALID_VALUE`. Not checked against your groups when saved. StartCampaignAssetActivationTask resolves them to recipients. On a stage that can't resolve groups yet, Start refuses an email while groups are set (`ENGAGEMENT_GROUPS_UNAVAILABLE`), rather than send to `EmailTarget` alone.
            target_audience: Advisory targeting metadata. Refined later, and not validated here.
            estimated_budget: What the partner expects the campaign to cost.
            total_budget: The campaign's total budget.
            start_on: The first day of the campaign's run window. Not after `EndOn` (`ValidationException`, `INVALID_VALUE`).
            end_on: The last day of the campaign's run window, inclusive and in UTC. Not in the past: the campaign completes at the UTC midnight after it (see `CampaignState`). A scheduled send must fall on or before it. Optional here, but required before any asset activates: until it is set, GetCampaign's `ActivationIssues` reports `END_ON_MISSING` and StartCampaignAssetActivationTask refuses (`CAMPAIGN_INCOMPLETE`). Set it with UpdateCampaign.
            client_token: Idempotency token. Same token within 24h returns existing resource.
            tags: Tags to apply at creation. Tag-on-create rather than create-then-tag is a Tagris requirement, not a convenience: it is what lets a tag-based access control policy govern the creation itself. A campaign created untagged and tagged a moment later is briefly outside any such policy. <p>A key beginning `aws:` (any case) is reserved for AWS-applied system tags and is refused with `ValidationException`, as is a key repeated in the list; nothing is created. The tags are recorded before the campaign is written, so a create that cannot record them fails and creates nothing. A retry with the same `ClientToken` returns the campaign the first attempt created and does not re-apply tags — use `TagResource` to change them afterwards. `ListTagsForResource` returns them.

        Raises:
            capo_partnercentral_marketing.errors.access_denied_exception.AccessDeniedException: You do not have sufficient access to perform this action. An IAM denial carries no `Reason`. A refusal for the caller's Partner Central state carries one, so a client tells the two apart by its presence.
            capo_partnercentral_marketing.errors.internal_server_exception.InternalServerException: An unexpected error occurred during the processing of the request.
            capo_partnercentral_marketing.errors.throttling_exception.ThrottlingException: The request was denied due to request throttling.
            capo_partnercentral_marketing.errors.validation_exception.ValidationException: The input fails to satisfy the constraints specified by the service. A caller branches on `Reason`, and where the rejection is attributable to particular fields it reads `FieldList` rather than parsing `Message`, which is prose and may change.
            capo_partnercentral_marketing.errors.conflict_exception.ConflictException: The request conflicts with the current state of the resource.
            capo_partnercentral_marketing.errors.resource_not_found_exception.ResourceNotFoundException: The specified resource does not exist.
            capo_partnercentral_marketing.errors.service_quota_exceeded_exception.ServiceQuotaExceededException: The request exceeds a service quota.
            capo_partnercentral_marketing.errors.UnknownServiceError: The service returned an error code this client does not model.

        Examples:
            Create a campaign

            >>> await client.create(catalog='AWS', name='Q4 GenAI Campaign', campaign_template_id='tmpl-a1b2c3d4e5f6g', total_budget={'Amount': '25000.00', 'CurrencyCode': 'USD'}, start_on='2026-11-01', end_on='2026-12-31')
        """

        async def _handler(
            req: "AsyncOperationRequest[capo_partnercentral_marketing.types.create_campaign_request.CreateCampaignRequest]",
        ) -> AsyncOperationResponse[
            "capo_partnercentral_marketing.types.create_campaign_response.CreateCampaignResponse"
        ]:
            import capo_partnercentral_marketing._operations.aws_partner_demand_generator.create_campaign

            (
                output,
                http_response,
            ) = await capo_partnercentral_marketing._operations.aws_partner_demand_generator.create_campaign.async_create_campaign(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        def _redact_input(
            input_: "capo_partnercentral_marketing.types.create_campaign_request.CreateCampaignRequest",
        ) -> dict[str, Any]:
            import capo_partnercentral_marketing.types.create_campaign_request

            return capo_partnercentral_marketing.types.create_campaign_request.redact_sensitive(
                input_
            )

        interceptors_, options_ = self._service.operation_options(
            config_overrides,
            OperationLogging("CreateCampaign", redact_input=_redact_input),
        )
        input_: capo_partnercentral_marketing.types.create_campaign_request.CreateCampaignRequest = {
            "catalog": catalog,
            "name": name,
            "campaign_template_id": campaign_template_id,
        }
        if sender_email is not None:
            input_["sender_email"] = sender_email
        if privacy_policy_url is not None:
            input_["privacy_policy_url"] = privacy_policy_url
        if partner_address is not None:
            input_["partner_address"] = partner_address
        if partner_badge is not None:
            input_["partner_badge"] = partner_badge
        if email_target is not None:
            input_["email_target"] = email_target
        if email_target_engagement_group_ids is not None:
            input_["email_target_engagement_group_ids"] = (
                email_target_engagement_group_ids
            )
        if target_audience is not None:
            input_["target_audience"] = target_audience
        if estimated_budget is not None:
            input_["estimated_budget"] = estimated_budget
        if total_budget is not None:
            input_["total_budget"] = total_budget
        if start_on is not None:
            input_["start_on"] = start_on
        if end_on is not None:
            input_["end_on"] = end_on
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

    async def read(
        self,
        catalog: "capo_partnercentral_marketing.types.catalog.Catalog",
        campaign_identifier: "capo_partnercentral_marketing.types.campaign_identifier.CampaignIdentifier",
        *,
        config_overrides: Optional[AsyncPartnerCentralMarketingClientConfig] = None,
    ) -> (
        "capo_partnercentral_marketing.types.get_campaign_response.GetCampaignResponse"
    ):
        """Retrieves a campaign by its identifier.

        Args:
            catalog: The catalog (AWS or Sandbox).
            campaign_identifier: The campaign identifier.

        Raises:
            capo_partnercentral_marketing.errors.access_denied_exception.AccessDeniedException: You do not have sufficient access to perform this action. An IAM denial carries no `Reason`. A refusal for the caller's Partner Central state carries one, so a client tells the two apart by its presence.
            capo_partnercentral_marketing.errors.internal_server_exception.InternalServerException: An unexpected error occurred during the processing of the request.
            capo_partnercentral_marketing.errors.throttling_exception.ThrottlingException: The request was denied due to request throttling.
            capo_partnercentral_marketing.errors.validation_exception.ValidationException: The input fails to satisfy the constraints specified by the service. A caller branches on `Reason`, and where the rejection is attributable to particular fields it reads `FieldList` rather than parsing `Message`, which is prose and may change.
            capo_partnercentral_marketing.errors.resource_not_found_exception.ResourceNotFoundException: The specified resource does not exist.
            capo_partnercentral_marketing.errors.UnknownServiceError: The service returned an error code this client does not model.

        Examples:
            Get a campaign

            >>> await client.read(catalog='AWS', campaign_identifier='camp-5Hq2m8x4k1p9w')
        """

        async def _handler(
            req: "AsyncOperationRequest[capo_partnercentral_marketing.types.get_campaign_request.GetCampaignRequest]",
        ) -> AsyncOperationResponse[
            "capo_partnercentral_marketing.types.get_campaign_response.GetCampaignResponse"
        ]:
            import capo_partnercentral_marketing._operations.aws_partner_demand_generator.get_campaign

            (
                output,
                http_response,
            ) = await capo_partnercentral_marketing._operations.aws_partner_demand_generator.get_campaign.async_get_campaign(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        def _redact_output(
            output: "capo_partnercentral_marketing.types.get_campaign_response.GetCampaignResponse",
        ) -> dict[str, Any]:
            import capo_partnercentral_marketing.types.get_campaign_response

            return capo_partnercentral_marketing.types.get_campaign_response.redact_sensitive(
                output
            )

        interceptors_, options_ = self._service.operation_options(
            config_overrides,
            OperationLogging("GetCampaign", redact_output=_redact_output),
        )
        input_: capo_partnercentral_marketing.types.get_campaign_request.GetCampaignRequest = {
            "catalog": catalog,
            "campaign_identifier": campaign_identifier,
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
        catalog: "capo_partnercentral_marketing.types.catalog.Catalog",
        campaign_identifier: "capo_partnercentral_marketing.types.campaign_identifier.CampaignIdentifier",
        *,
        config_overrides: Optional[AsyncPartnerCentralMarketingClientConfig] = None,
        name: Optional[
            "capo_partnercentral_marketing.types.campaign_name.CampaignName"
        ] = None,
        sender_email: Optional[
            "capo_partnercentral_marketing.types.sender_email.SenderEmail"
        ] = None,
        privacy_policy_url: Optional[
            "capo_partnercentral_marketing.types.privacy_policy_url.PrivacyPolicyUrl"
        ] = None,
        partner_address: Optional[
            "capo_partnercentral_marketing.types.partner_address.PartnerAddress"
        ] = None,
        partner_badge: Optional[
            "capo_partnercentral_marketing.types.file_ref.FileRef"
        ] = None,
        email_target: Optional[
            "capo_partnercentral_marketing.types.file_ref.FileRef"
        ] = None,
        email_target_engagement_group_ids: Optional[
            "capo_partnercentral_marketing.types.engagement_group_id_list.EngagementGroupIdList"
        ] = None,
        social_connections: Optional[
            "capo_partnercentral_marketing.types.campaign_social_connections.CampaignSocialConnections"
        ] = None,
        estimated_budget: Optional[
            "capo_partnercentral_marketing.types.monetary_value.MonetaryValue"
        ] = None,
        total_budget: Optional[
            "capo_partnercentral_marketing.types.monetary_value.MonetaryValue"
        ] = None,
        target_audience: Optional[
            "capo_partnercentral_marketing.types.target_audience.TargetAudience"
        ] = None,
        client_token: Optional[
            "capo_partnercentral_marketing.types.client_token.ClientToken"
        ] = None,
        start_on: Optional[
            "capo_partnercentral_marketing.types.utc_date.UtcDate"
        ] = None,
        end_on: Optional["capo_partnercentral_marketing.types.utc_date.UtcDate"] = None,
    ) -> "capo_partnercentral_marketing.types.update_campaign_response.UpdateCampaignResponse":
        """Edits a campaign in place. Partial update: an omitted field is left unchanged, which is the standard meaning of an `Update` verb — a full replacement would be a `Put`. Change-only, with no way to clear a field back to empty, because the campaign's file members cannot round-trip: they are written as an `s3://` reference and read back as a URL or as metadata, so a replacement payload could not resend an unchanged recipient list without re-uploading it. Refused while an activation task runs (`CAMPAIGN_ACTIVATION_IN_PROGRESS`) and once the campaign is completed (`CAMPAIGN_COMPLETED`, the UTC date is after its `EndOn`). Last-writer-wins, with no concurrency token: this is low-contention metadata owned by one partner.

        Args:
            catalog: The catalog (AWS or Sandbox).
            campaign_identifier: The campaign identifier.
            name: The display name.
            sender_email: Sets or replaces the address the campaign's emails are sent from. Checked by the same three rules as on `CreateCampaign`, with the same codes, but only when it differs, ignoring case, from the stored sender: re-sending the stored one is not checked, and `StartCampaignAssetActivationTask` re-checks it before an email activates. <p>Replaces, never clears: like every member of this operation, an omitted value leaves the sender as it was, and there is no way to remove one once set.
            privacy_policy_url: Sets or replaces the URL of the partner's privacy policy. Replaces, never clears.
            partner_address: Sets or replaces the partner's postal address. Replaces, never clears.
            partner_badge: Sets or replaces the partner's badge, checked exactly as on `CreateCampaign`. Replaces, never clears: upload the Standalone AWS Partner badge to show it again. The badge an asset already published keeps showing on it until that asset is activated again.
            email_target: Replaces the campaign's attached recipient list. <p>The referenced object is copied and pinned again on every call that supplies it, so the pinned copy always reflects the *last* `UpdateCampaign` that named one. Editing the source object in your own bucket without calling this operation again has no effect. <p>Replaces, never detaches: a partner can swap the list but cannot remove it.
            email_target_engagement_group_ids: Engagement groups whose contacts the campaign's emails will also go to (see `CreateCampaign`). Replaces the stored list; never clears it. <p>As on `CreateCampaign`: each group once (`INVALID_VALUE` otherwise), not checked against your groups when saved, and resolved at Start where the stage can (`ENGAGEMENT_GROUPS_UNAVAILABLE` where it can't).
            social_connections: Sets the account the campaign's social posts publish from, per platform. Each platform named replaces that platform's choice; a platform not named keeps its own. Replaces, never clears. <p>Not checked against your connections here: a connection can be deleted at any time, so the activation checks the choice. See `Campaign$SocialConnections`.
            estimated_budget: What the partner expects the campaign to cost.
            total_budget: The campaign's total budget.
            target_audience: Target audience configuration.
            client_token: Idempotency token. Accepted and not stored: this is a change-only partial update with last-writer-wins, so re-applying the same call produces the same result and the same response. There is nothing a replay cache would protect.
            start_on: The first day of the campaign's run window. Not after `EndOn` (`ValidationException`, `INVALID_VALUE`).
            end_on: The last day of the campaign's run window, inclusive and in UTC. Editable only while the campaign is open, like everything else here: once the stored `EndOn` has passed the campaign is completed and this update is refused (`CAMPAIGN_COMPLETED`). Refused with `ValidationException` (`INVALID_VALUE`) when it is in the past, or earlier than the day of a scheduled send on one of the campaign's assets: move or cancel that send first. Setting it to today ends the campaign at the next UTC midnight.

        Raises:
            capo_partnercentral_marketing.errors.access_denied_exception.AccessDeniedException: You do not have sufficient access to perform this action. An IAM denial carries no `Reason`. A refusal for the caller's Partner Central state carries one, so a client tells the two apart by its presence.
            capo_partnercentral_marketing.errors.internal_server_exception.InternalServerException: An unexpected error occurred during the processing of the request.
            capo_partnercentral_marketing.errors.throttling_exception.ThrottlingException: The request was denied due to request throttling.
            capo_partnercentral_marketing.errors.validation_exception.ValidationException: The input fails to satisfy the constraints specified by the service. A caller branches on `Reason`, and where the rejection is attributable to particular fields it reads `FieldList` rather than parsing `Message`, which is prose and may change.
            capo_partnercentral_marketing.errors.conflict_exception.ConflictException: The request conflicts with the current state of the resource.
            capo_partnercentral_marketing.errors.resource_not_found_exception.ResourceNotFoundException: The specified resource does not exist.
            capo_partnercentral_marketing.errors.UnknownServiceError: The service returned an error code this client does not model.

        Examples:
            Rename a campaign and raise its budget

            >>> await client.update(catalog='AWS', campaign_identifier='camp-5Hq2m8x4k1p9w', name='Q4 GenAI Campaign (EMEA)', total_budget={'Amount': '40000.00', 'CurrencyCode': 'USD'})
        """

        async def _handler(
            req: "AsyncOperationRequest[capo_partnercentral_marketing.types.update_campaign_request.UpdateCampaignRequest]",
        ) -> AsyncOperationResponse[
            "capo_partnercentral_marketing.types.update_campaign_response.UpdateCampaignResponse"
        ]:
            import capo_partnercentral_marketing._operations.aws_partner_demand_generator.update_campaign

            (
                output,
                http_response,
            ) = await capo_partnercentral_marketing._operations.aws_partner_demand_generator.update_campaign.async_update_campaign(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        def _redact_input(
            input_: "capo_partnercentral_marketing.types.update_campaign_request.UpdateCampaignRequest",
        ) -> dict[str, Any]:
            import capo_partnercentral_marketing.types.update_campaign_request

            return capo_partnercentral_marketing.types.update_campaign_request.redact_sensitive(
                input_
            )

        interceptors_, options_ = self._service.operation_options(
            config_overrides,
            OperationLogging("UpdateCampaign", redact_input=_redact_input),
        )
        input_: capo_partnercentral_marketing.types.update_campaign_request.UpdateCampaignRequest = {
            "catalog": catalog,
            "campaign_identifier": campaign_identifier,
        }
        if name is not None:
            input_["name"] = name
        if sender_email is not None:
            input_["sender_email"] = sender_email
        if privacy_policy_url is not None:
            input_["privacy_policy_url"] = privacy_policy_url
        if partner_address is not None:
            input_["partner_address"] = partner_address
        if partner_badge is not None:
            input_["partner_badge"] = partner_badge
        if email_target is not None:
            input_["email_target"] = email_target
        if email_target_engagement_group_ids is not None:
            input_["email_target_engagement_group_ids"] = (
                email_target_engagement_group_ids
            )
        if social_connections is not None:
            input_["social_connections"] = social_connections
        if estimated_budget is not None:
            input_["estimated_budget"] = estimated_budget
        if total_budget is not None:
            input_["total_budget"] = total_budget
        if target_audience is not None:
            input_["target_audience"] = target_audience
        if client_token is None:
            client_token = str(uuid.uuid4())
        input_["client_token"] = client_token
        if start_on is not None:
            input_["start_on"] = start_on
        if end_on is not None:
            input_["end_on"] = end_on

        response = await aexecute_pipeline(
            AsyncOperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        await response.response.aclose()
        return response.output

    async def delete(
        self,
        catalog: "capo_partnercentral_marketing.types.catalog.Catalog",
        campaign_identifier: "capo_partnercentral_marketing.types.campaign_identifier.CampaignIdentifier",
        *,
        config_overrides: Optional[AsyncPartnerCentralMarketingClientConfig] = None,
    ) -> None:
        """Permanently deletes a campaign, its assets and their stored files. A hard delete with no undo: the campaign leaves ListCampaigns and every read of it returns ResourceNotFoundException. Its tags are removed with it. Refused with ConflictException while the campaign has a live asset (`CAMPAIGN_HAS_ACTIVE_ASSETS`), because deleting the record would orphan what the delivery platform still serves or sends: deactivate those assets first. Also refused while an activation task is running (`CAMPAIGN_ACTIVATION_IN_PROGRESS`). A completed campaign can be deleted. Idempotent in effect: deleting a campaign that is already gone returns ResourceNotFoundException, and nothing is left behind by a retry.

        Args:
            catalog: The catalog (AWS or Sandbox).
            campaign_identifier: The campaign to delete.

        Raises:
            capo_partnercentral_marketing.errors.access_denied_exception.AccessDeniedException: You do not have sufficient access to perform this action. An IAM denial carries no `Reason`. A refusal for the caller's Partner Central state carries one, so a client tells the two apart by its presence.
            capo_partnercentral_marketing.errors.internal_server_exception.InternalServerException: An unexpected error occurred during the processing of the request.
            capo_partnercentral_marketing.errors.throttling_exception.ThrottlingException: The request was denied due to request throttling.
            capo_partnercentral_marketing.errors.validation_exception.ValidationException: The input fails to satisfy the constraints specified by the service. A caller branches on `Reason`, and where the rejection is attributable to particular fields it reads `FieldList` rather than parsing `Message`, which is prose and may change.
            capo_partnercentral_marketing.errors.conflict_exception.ConflictException: The request conflicts with the current state of the resource.
            capo_partnercentral_marketing.errors.resource_not_found_exception.ResourceNotFoundException: The specified resource does not exist.
            capo_partnercentral_marketing.errors.UnknownServiceError: The service returned an error code this client does not model.

        Examples:
            Delete a campaign

            >>> await client.delete(catalog='AWS', campaign_identifier='camp-5Hq2m8x4k1p9w')
        """

        async def _handler(
            req: "AsyncOperationRequest[capo_partnercentral_marketing.types.delete_campaign_request.DeleteCampaignRequest]",
        ) -> AsyncOperationResponse[None]:
            import capo_partnercentral_marketing._operations.aws_partner_demand_generator.delete_campaign

            (
                output,
                http_response,
            ) = await capo_partnercentral_marketing._operations.aws_partner_demand_generator.delete_campaign.async_delete_campaign(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self._service.operation_options(
            config_overrides, OperationLogging("DeleteCampaign")
        )
        input_: capo_partnercentral_marketing.types.delete_campaign_request.DeleteCampaignRequest = {
            "catalog": catalog,
            "campaign_identifier": campaign_identifier,
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
        catalog: "capo_partnercentral_marketing.types.catalog.Catalog",
        *,
        config_overrides: Optional[AsyncPartnerCentralMarketingClientConfig] = None,
        campaign_identifiers: Optional[
            "capo_partnercentral_marketing.types.campaign_identifier_list.CampaignIdentifierList"
        ] = None,
        name: Optional[
            "capo_partnercentral_marketing.types.campaign_name.CampaignName"
        ] = None,
        states: Optional[
            "capo_partnercentral_marketing.types.campaign_state_list.CampaignStateList"
        ] = None,
        sort: Optional[
            "capo_partnercentral_marketing.types.campaign_sort.CampaignSort"
        ] = None,
        max_results: Optional[
            "capo_partnercentral_marketing.types.max_results.MaxResults"
        ] = None,
        next_token: Optional[
            "capo_partnercentral_marketing.types.next_token.NextToken"
        ] = None,
    ) -> "capo_partnercentral_marketing.types.list_campaigns_response.ListCampaignsResponse":
        """Lists campaigns with optional filters and pagination.

        Args:
            catalog: The catalog (AWS or Sandbox).
            campaign_identifiers: Only these campaigns, each named by its id or its campaign ARN. A campaign that does not exist, was deleted, or whose ARN names another account or catalog is left out rather than refused.
            name: Only campaigns whose name contains this, compared case-insensitively.
            states: Only campaigns in one of these states.
            sort: The order of the results. Default: `CREATED_AT`, `DESCENDING`.
            max_results: Maximum results per page.
            next_token: Pagination token. Bound to the filters and sort it was issued for: a request that changes `CampaignIdentifiers`, `Name`, `States` or `Sort` between pages is refused with `ValidationException`. `MaxResults` may change.

        Raises:
            capo_partnercentral_marketing.errors.access_denied_exception.AccessDeniedException: You do not have sufficient access to perform this action. An IAM denial carries no `Reason`. A refusal for the caller's Partner Central state carries one, so a client tells the two apart by its presence.
            capo_partnercentral_marketing.errors.internal_server_exception.InternalServerException: An unexpected error occurred during the processing of the request.
            capo_partnercentral_marketing.errors.throttling_exception.ThrottlingException: The request was denied due to request throttling.
            capo_partnercentral_marketing.errors.validation_exception.ValidationException: The input fails to satisfy the constraints specified by the service. A caller branches on `Reason`, and where the rejection is attributable to particular fields it reads `FieldList` rather than parsing `Message`, which is prose and may change.
            capo_partnercentral_marketing.errors.UnknownServiceError: The service returned an error code this client does not model.

        Examples:
            List campaigns

            >>> await client.list(catalog='AWS')
            Name the campaigns a page links to

            >>> await client.list(catalog='AWS', campaign_identifiers=['arn:aws:partnercentral:us-east-1:123456789012:catalog/AWS/campaign/camp-5Hq2m8x4k1p9w', 'camp-8Rt3w6y1n4b2v'])
            Search active campaigns by name, by launch date

            >>> await client.list(catalog='AWS', name='genai', states=['ACTIVE'], sort={'SortBy': 'START_ON', 'SortOrder': 'ASCENDING'}, max_results=20)
        """

        async def _handler(
            req: "AsyncOperationRequest[capo_partnercentral_marketing.types.list_campaigns_request.ListCampaignsRequest]",
        ) -> AsyncOperationResponse[
            "capo_partnercentral_marketing.types.list_campaigns_response.ListCampaignsResponse"
        ]:
            import capo_partnercentral_marketing._operations.aws_partner_demand_generator.list_campaigns

            (
                output,
                http_response,
            ) = await capo_partnercentral_marketing._operations.aws_partner_demand_generator.list_campaigns.async_list_campaigns(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self._service.operation_options(
            config_overrides, OperationLogging("ListCampaigns")
        )
        input_: capo_partnercentral_marketing.types.list_campaigns_request.ListCampaignsRequest = {
            "catalog": catalog
        }
        if campaign_identifiers is not None:
            input_["campaign_identifiers"] = campaign_identifiers
        if name is not None:
            input_["name"] = name
        if states is not None:
            input_["states"] = states
        if sort is not None:
            input_["sort"] = sort
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

    async def batch_create_campaign_asset(
        self,
        catalog: "capo_partnercentral_marketing.types.catalog.Catalog",
        campaign_identifier: "capo_partnercentral_marketing.types.campaign_identifier.CampaignIdentifier",
        entries: "capo_partnercentral_marketing.types.batch_create_campaign_asset_entries.BatchCreateCampaignAssetEntries",
        *,
        config_overrides: Optional[AsyncPartnerCentralMarketingClientConfig] = None,
    ) -> "capo_partnercentral_marketing.types.batch_create_campaign_asset_response.BatchCreateCampaignAssetResponse":
        """Instantiates one or more of the campaign template's blueprints as assets of this campaign. The only asset-create operation: DG-038 deleted the singular CreateCampaignAsset, and AWS Batch Operations makes exposing a singular alongside a batch optional ("which MAY actually be exposed in addition"). It also replaced kit instantiation -- CreateCampaign creates zero assets, so this is the only path by which an asset comes into existence. Errors here are whole-request only, and nothing is written when one is thrown. Per-entry failures ride in the response's `Errors` list with a 200. ServiceQuotaExceededException is deliberately absent: a campaign holds at most one asset per blueprint (I-15), so the ceiling is the size of the bound kit and a request of unique valid entries cannot exceed it.

        Args:
            catalog: The catalog (AWS or Sandbox).
            campaign_identifier: The campaign identifier.
            entries: The blueprints to instantiate, one entry each.

        Raises:
            capo_partnercentral_marketing.errors.access_denied_exception.AccessDeniedException: You do not have sufficient access to perform this action. An IAM denial carries no `Reason`. A refusal for the caller's Partner Central state carries one, so a client tells the two apart by its presence.
            capo_partnercentral_marketing.errors.internal_server_exception.InternalServerException: An unexpected error occurred during the processing of the request.
            capo_partnercentral_marketing.errors.throttling_exception.ThrottlingException: The request was denied due to request throttling.
            capo_partnercentral_marketing.errors.validation_exception.ValidationException: The input fails to satisfy the constraints specified by the service. A caller branches on `Reason`, and where the rejection is attributable to particular fields it reads `FieldList` rather than parsing `Message`, which is prose and may change.
            capo_partnercentral_marketing.errors.conflict_exception.ConflictException: The request conflicts with the current state of the resource.
            capo_partnercentral_marketing.errors.resource_not_found_exception.ResourceNotFoundException: The specified resource does not exist.
            capo_partnercentral_marketing.errors.UnknownServiceError: The service returned an error code this client does not model.

        Examples:
            Instantiate two of the kit's blueprints

            >>> await client.batch_create_campaign_asset(catalog='AWS', campaign_identifier='camp-5Hq2m8x4k1p9w', entries=[{'SourceAssetTemplateIdentifier': 'ta000000email'}, {'SourceAssetTemplateIdentifier': 'ta0000000lp01'}])
            A partial batch: one entry names a blueprint the campaign's template does not carry

            >>> await client.batch_create_campaign_asset(catalog='AWS', campaign_identifier='camp-5Hq2m8x4k1p9w', entries=[{'SourceAssetTemplateIdentifier': 'ta000000email'}, {'SourceAssetTemplateIdentifier': 'ta00000absent'}])
        """

        async def _handler(
            req: "AsyncOperationRequest[capo_partnercentral_marketing.types.batch_create_campaign_asset_request.BatchCreateCampaignAssetRequest]",
        ) -> AsyncOperationResponse[
            "capo_partnercentral_marketing.types.batch_create_campaign_asset_response.BatchCreateCampaignAssetResponse"
        ]:
            import capo_partnercentral_marketing._operations.aws_partner_demand_generator.batch_create_campaign_asset

            (
                output,
                http_response,
            ) = await capo_partnercentral_marketing._operations.aws_partner_demand_generator.batch_create_campaign_asset.async_batch_create_campaign_asset(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self._service.operation_options(
            config_overrides, OperationLogging("BatchCreateCampaignAsset")
        )
        input_: capo_partnercentral_marketing.types.batch_create_campaign_asset_request.BatchCreateCampaignAssetRequest = {
            "catalog": catalog,
            "campaign_identifier": campaign_identifier,
            "entries": entries,
        }

        response = await aexecute_pipeline(
            AsyncOperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        await response.response.aclose()
        return response.output

    async def deactivate_campaign_asset(
        self,
        catalog: "capo_partnercentral_marketing.types.catalog.Catalog",
        campaign_identifier: "capo_partnercentral_marketing.types.campaign_identifier.CampaignIdentifier",
        campaign_asset_identifier: "capo_partnercentral_marketing.types.campaign_asset_id.CampaignAssetId",
        *,
        config_overrides: Optional[AsyncPartnerCentralMarketingClientConfig] = None,
    ) -> "capo_partnercentral_marketing.types.deactivate_campaign_asset_response.DeactivateCampaignAssetResponse":
        """Stops a live campaign asset: an email's scheduled send is withdrawn, a social post is removed before it publishes. On a completed campaign, it also removes a published document, banner or landing page. Synchronous, and safe to repeat. Does not delete the asset record, so a stopped email or social post can be started again. Not every asset can be stopped, and the reasons differ in kind. An email that has begun sending **cannot** be recalled: the send is gone. A document, a banner or a landing page is **refused** with `ASSET_NOT_DEACTIVATABLE` until the campaign has completed (the UTC date is after its `EndOn`). Until then the partner fixes one in place by updating it and activating it again, which keeps its URL, so every email that already linked to it keeps working. Once the campaign has completed, the removal is permanent, because a completed campaign can't activate anything again: - A document's published PDF is deleted. Its URL stops serving within about a minute (the CDN revalidates), and `PublicUrl` is no longer returned. Anything that linked to it, such as a landing page's download button or a sent email, reaches an error page. The export still contains the document. - A banner's or landing page's published object is taken down at the delivery platform, and the images the partner put on it are deleted. A landing page stops capturing leads, and its `PublicUrl` is no longer returned. A partner site that embedded a banner shows nothing there. The platform's own CDN can keep serving a copy a visitor already cached, which collects nothing. A landing page and a document it links to can be removed in either order.

        Args:
            catalog: The catalog (AWS or Sandbox).
            campaign_identifier: The campaign identifier.
            campaign_asset_identifier: The asset identifier.

        Raises:
            capo_partnercentral_marketing.errors.access_denied_exception.AccessDeniedException: You do not have sufficient access to perform this action. An IAM denial carries no `Reason`. A refusal for the caller's Partner Central state carries one, so a client tells the two apart by its presence.
            capo_partnercentral_marketing.errors.internal_server_exception.InternalServerException: An unexpected error occurred during the processing of the request.
            capo_partnercentral_marketing.errors.throttling_exception.ThrottlingException: The request was denied due to request throttling.
            capo_partnercentral_marketing.errors.validation_exception.ValidationException: The input fails to satisfy the constraints specified by the service. A caller branches on `Reason`, and where the rejection is attributable to particular fields it reads `FieldList` rather than parsing `Message`, which is prose and may change.
            capo_partnercentral_marketing.errors.conflict_exception.ConflictException: The request conflicts with the current state of the resource.
            capo_partnercentral_marketing.errors.resource_not_found_exception.ResourceNotFoundException: The specified resource does not exist.
            capo_partnercentral_marketing.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        async def _handler(
            req: "AsyncOperationRequest[capo_partnercentral_marketing.types.deactivate_campaign_asset_request.DeactivateCampaignAssetRequest]",
        ) -> AsyncOperationResponse[
            "capo_partnercentral_marketing.types.deactivate_campaign_asset_response.DeactivateCampaignAssetResponse"
        ]:
            import capo_partnercentral_marketing._operations.aws_partner_demand_generator.deactivate_campaign_asset

            (
                output,
                http_response,
            ) = await capo_partnercentral_marketing._operations.aws_partner_demand_generator.deactivate_campaign_asset.async_deactivate_campaign_asset(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self._service.operation_options(
            config_overrides, OperationLogging("DeactivateCampaignAsset")
        )
        input_: capo_partnercentral_marketing.types.deactivate_campaign_asset_request.DeactivateCampaignAssetRequest = {
            "catalog": catalog,
            "campaign_identifier": campaign_identifier,
            "campaign_asset_identifier": campaign_asset_identifier,
        }

        response = await aexecute_pipeline(
            AsyncOperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        await response.response.aclose()
        return response.output

    async def delete_campaign_asset(
        self,
        catalog: "capo_partnercentral_marketing.types.catalog.Catalog",
        campaign_identifier: "capo_partnercentral_marketing.types.campaign_identifier.CampaignIdentifier",
        campaign_asset_identifier: "capo_partnercentral_marketing.types.campaign_asset_id.CampaignAssetId",
        *,
        config_overrides: Optional[AsyncPartnerCentralMarketingClientConfig] = None,
    ) -> None:
        """Permanently deletes a campaign asset.

        Args:
            catalog: The catalog (AWS or Sandbox).
            campaign_identifier: The campaign identifier.
            campaign_asset_identifier: The asset identifier.

        Raises:
            capo_partnercentral_marketing.errors.access_denied_exception.AccessDeniedException: You do not have sufficient access to perform this action. An IAM denial carries no `Reason`. A refusal for the caller's Partner Central state carries one, so a client tells the two apart by its presence.
            capo_partnercentral_marketing.errors.internal_server_exception.InternalServerException: An unexpected error occurred during the processing of the request.
            capo_partnercentral_marketing.errors.throttling_exception.ThrottlingException: The request was denied due to request throttling.
            capo_partnercentral_marketing.errors.validation_exception.ValidationException: The input fails to satisfy the constraints specified by the service. A caller branches on `Reason`, and where the rejection is attributable to particular fields it reads `FieldList` rather than parsing `Message`, which is prose and may change.
            capo_partnercentral_marketing.errors.conflict_exception.ConflictException: The request conflicts with the current state of the resource.
            capo_partnercentral_marketing.errors.resource_not_found_exception.ResourceNotFoundException: The specified resource does not exist.
            capo_partnercentral_marketing.errors.UnknownServiceError: The service returned an error code this client does not model.

        Examples:
            Delete an asset

            >>> await client.delete_campaign_asset(catalog='AWS', campaign_identifier='camp-5Hq2m8x4k1p9w', campaign_asset_identifier='ast-4b81e0c9f2a7b')
        """

        async def _handler(
            req: "AsyncOperationRequest[capo_partnercentral_marketing.types.delete_campaign_asset_request.DeleteCampaignAssetRequest]",
        ) -> AsyncOperationResponse[None]:
            import capo_partnercentral_marketing._operations.aws_partner_demand_generator.delete_campaign_asset

            (
                output,
                http_response,
            ) = await capo_partnercentral_marketing._operations.aws_partner_demand_generator.delete_campaign_asset.async_delete_campaign_asset(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self._service.operation_options(
            config_overrides, OperationLogging("DeleteCampaignAsset")
        )
        input_: capo_partnercentral_marketing.types.delete_campaign_asset_request.DeleteCampaignAssetRequest = {
            "catalog": catalog,
            "campaign_identifier": campaign_identifier,
            "campaign_asset_identifier": campaign_asset_identifier,
        }

        response = await aexecute_pipeline(
            AsyncOperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        await response.response.aclose()
        return response.output

    async def get_campaign_asset(
        self,
        catalog: "capo_partnercentral_marketing.types.catalog.Catalog",
        campaign_identifier: "capo_partnercentral_marketing.types.campaign_identifier.CampaignIdentifier",
        campaign_asset_identifier: "capo_partnercentral_marketing.types.campaign_asset_id.CampaignAssetId",
        *,
        config_overrides: Optional[AsyncPartnerCentralMarketingClientConfig] = None,
    ) -> "capo_partnercentral_marketing.types.get_campaign_asset_response.GetCampaignAssetResponse":
        """Retrieves an asset by its identifier.

        Args:
            catalog: The catalog (AWS or Sandbox).
            campaign_identifier: The campaign identifier.
            campaign_asset_identifier: The asset identifier.

        Raises:
            capo_partnercentral_marketing.errors.access_denied_exception.AccessDeniedException: You do not have sufficient access to perform this action. An IAM denial carries no `Reason`. A refusal for the caller's Partner Central state carries one, so a client tells the two apart by its presence.
            capo_partnercentral_marketing.errors.internal_server_exception.InternalServerException: An unexpected error occurred during the processing of the request.
            capo_partnercentral_marketing.errors.throttling_exception.ThrottlingException: The request was denied due to request throttling.
            capo_partnercentral_marketing.errors.validation_exception.ValidationException: The input fails to satisfy the constraints specified by the service. A caller branches on `Reason`, and where the rejection is attributable to particular fields it reads `FieldList` rather than parsing `Message`, which is prose and may change.
            capo_partnercentral_marketing.errors.resource_not_found_exception.ResourceNotFoundException: The specified resource does not exist.
            capo_partnercentral_marketing.errors.UnknownServiceError: The service returned an error code this client does not model.

        Examples:
            Get an asset

            >>> await client.get_campaign_asset(catalog='AWS', campaign_identifier='camp-5Hq2m8x4k1p9w', campaign_asset_identifier='ast-4b81e0c9f2a7b')
        """

        async def _handler(
            req: "AsyncOperationRequest[capo_partnercentral_marketing.types.get_campaign_asset_request.GetCampaignAssetRequest]",
        ) -> AsyncOperationResponse[
            "capo_partnercentral_marketing.types.get_campaign_asset_response.GetCampaignAssetResponse"
        ]:
            import capo_partnercentral_marketing._operations.aws_partner_demand_generator.get_campaign_asset

            (
                output,
                http_response,
            ) = await capo_partnercentral_marketing._operations.aws_partner_demand_generator.get_campaign_asset.async_get_campaign_asset(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        def _redact_output(
            output: "capo_partnercentral_marketing.types.get_campaign_asset_response.GetCampaignAssetResponse",
        ) -> dict[str, Any]:
            import capo_partnercentral_marketing.types.get_campaign_asset_response

            return capo_partnercentral_marketing.types.get_campaign_asset_response.redact_sensitive(
                output
            )

        interceptors_, options_ = self._service.operation_options(
            config_overrides,
            OperationLogging("GetCampaignAsset", redact_output=_redact_output),
        )
        input_: capo_partnercentral_marketing.types.get_campaign_asset_request.GetCampaignAssetRequest = {
            "catalog": catalog,
            "campaign_identifier": campaign_identifier,
            "campaign_asset_identifier": campaign_asset_identifier,
        }

        response = await aexecute_pipeline(
            AsyncOperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        await response.response.aclose()
        return response.output

    async def get_campaign_asset_activation_task(
        self,
        catalog: "capo_partnercentral_marketing.types.catalog.Catalog",
        campaign_identifier: "capo_partnercentral_marketing.types.campaign_identifier.CampaignIdentifier",
        *,
        config_overrides: Optional[AsyncPartnerCentralMarketingClientConfig] = None,
    ) -> "capo_partnercentral_marketing.types.get_campaign_asset_activation_task_response.GetCampaignAssetActivationTaskResponse":
        """Reads a campaign's current activation task. Keyed on the **campaign**, with no task identifier, because a campaign has at most one activation task: runs are serialised, so there is no collection to address into. The caller always holds the task id anyway, because Start returned it — the id is a correlation value, not an address. Returns the campaign's most recent task. A new task overwrites the previous one, so this is not a history: the durable per-asset record is on the assets themselves. Returns ResourceNotFoundException when the campaign has never had a task, or when its last one has expired.

        Args:
            catalog: The catalog (AWS or Sandbox).
            campaign_identifier: The campaign whose current task to read. This addresses the task, and also authorizes the call.

        Raises:
            capo_partnercentral_marketing.errors.access_denied_exception.AccessDeniedException: You do not have sufficient access to perform this action. An IAM denial carries no `Reason`. A refusal for the caller's Partner Central state carries one, so a client tells the two apart by its presence.
            capo_partnercentral_marketing.errors.internal_server_exception.InternalServerException: An unexpected error occurred during the processing of the request.
            capo_partnercentral_marketing.errors.throttling_exception.ThrottlingException: The request was denied due to request throttling.
            capo_partnercentral_marketing.errors.validation_exception.ValidationException: The input fails to satisfy the constraints specified by the service. A caller branches on `Reason`, and where the rejection is attributable to particular fields it reads `FieldList` rather than parsing `Message`, which is prose and may change.
            capo_partnercentral_marketing.errors.resource_not_found_exception.ResourceNotFoundException: The specified resource does not exist.
            capo_partnercentral_marketing.errors.UnknownServiceError: The service returned an error code this client does not model.

        Examples:
            Read a finished task where one asset failed

            >>> await client.get_campaign_asset_activation_task(catalog='AWS', campaign_identifier='camp-5Hq2m8x4k1p9w')
        """

        async def _handler(
            req: "AsyncOperationRequest[capo_partnercentral_marketing.types.get_campaign_asset_activation_task_request.GetCampaignAssetActivationTaskRequest]",
        ) -> AsyncOperationResponse[
            "capo_partnercentral_marketing.types.get_campaign_asset_activation_task_response.GetCampaignAssetActivationTaskResponse"
        ]:
            import capo_partnercentral_marketing._operations.aws_partner_demand_generator.get_campaign_asset_activation_task

            (
                output,
                http_response,
            ) = await capo_partnercentral_marketing._operations.aws_partner_demand_generator.get_campaign_asset_activation_task.async_get_campaign_asset_activation_task(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self._service.operation_options(
            config_overrides, OperationLogging("GetCampaignAssetActivationTask")
        )
        input_: capo_partnercentral_marketing.types.get_campaign_asset_activation_task_request.GetCampaignAssetActivationTaskRequest = {
            "catalog": catalog,
            "campaign_identifier": campaign_identifier,
        }

        response = await aexecute_pipeline(
            AsyncOperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        await response.response.aclose()
        return response.output

    async def get_campaign_asset_export_task(
        self,
        catalog: "capo_partnercentral_marketing.types.catalog.Catalog",
        campaign_identifier: "capo_partnercentral_marketing.types.campaign_identifier.CampaignIdentifier",
        campaign_asset_export_task_identifier: "capo_partnercentral_marketing.types.campaign_asset_export_task_id.CampaignAssetExportTaskId",
        *,
        config_overrides: Optional[AsyncPartnerCentralMarketingClientConfig] = None,
    ) -> "capo_partnercentral_marketing.types.get_campaign_asset_export_task_response.GetCampaignAssetExportTaskResponse":
        """Retrieves a campaign asset export task by its identifier, reporting its status and, when the task is COMPLETED, a freshly minted short-lived presigned URL for downloading the ZIP archive. The download URL is minted on each call and is valid for at most 15 minutes; clients should download promptly rather than caching it. When the task has FAILED, FailureReason explains why. Poll this operation (roughly every 2-5 seconds) until the task reaches a terminal state.

        Args:
            catalog: The catalog (AWS or Sandbox).
            campaign_identifier: The campaign that owns the export task. Accepts the campaign id or ARN. Required so the read is authorized on campaign/{CampaignId}; the task must belong to this campaign or the request resolves to not-found.
            campaign_asset_export_task_identifier: The export task to retrieve: the `Id` StartCampaignAssetExportTask returned (`etsk-…`). An id only. An export task has no ARN: none is returned, recorded or authorized on (the read authorizes on its campaign), so there is no ARN to accept (DG-063 D-35).

        Raises:
            capo_partnercentral_marketing.errors.access_denied_exception.AccessDeniedException: You do not have sufficient access to perform this action. An IAM denial carries no `Reason`. A refusal for the caller's Partner Central state carries one, so a client tells the two apart by its presence.
            capo_partnercentral_marketing.errors.internal_server_exception.InternalServerException: An unexpected error occurred during the processing of the request.
            capo_partnercentral_marketing.errors.throttling_exception.ThrottlingException: The request was denied due to request throttling.
            capo_partnercentral_marketing.errors.validation_exception.ValidationException: The input fails to satisfy the constraints specified by the service. A caller branches on `Reason`, and where the rejection is attributable to particular fields it reads `FieldList` rather than parsing `Message`, which is prose and may change.
            capo_partnercentral_marketing.errors.resource_not_found_exception.ResourceNotFoundException: The specified resource does not exist.
            capo_partnercentral_marketing.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        async def _handler(
            req: "AsyncOperationRequest[capo_partnercentral_marketing.types.get_campaign_asset_export_task_request.GetCampaignAssetExportTaskRequest]",
        ) -> AsyncOperationResponse[
            "capo_partnercentral_marketing.types.get_campaign_asset_export_task_response.GetCampaignAssetExportTaskResponse"
        ]:
            import capo_partnercentral_marketing._operations.aws_partner_demand_generator.get_campaign_asset_export_task

            (
                output,
                http_response,
            ) = await capo_partnercentral_marketing._operations.aws_partner_demand_generator.get_campaign_asset_export_task.async_get_campaign_asset_export_task(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self._service.operation_options(
            config_overrides, OperationLogging("GetCampaignAssetExportTask")
        )
        input_: capo_partnercentral_marketing.types.get_campaign_asset_export_task_request.GetCampaignAssetExportTaskRequest = {
            "catalog": catalog,
            "campaign_identifier": campaign_identifier,
            "campaign_asset_export_task_identifier": campaign_asset_export_task_identifier,
        }

        response = await aexecute_pipeline(
            AsyncOperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        await response.response.aclose()
        return response.output

    async def list_campaign_assets(
        self,
        catalog: "capo_partnercentral_marketing.types.catalog.Catalog",
        campaign_identifier: "capo_partnercentral_marketing.types.campaign_identifier.CampaignIdentifier",
        *,
        config_overrides: Optional[AsyncPartnerCentralMarketingClientConfig] = None,
        max_results: Optional[
            "capo_partnercentral_marketing.types.max_results.MaxResults"
        ] = None,
        next_token: Optional[
            "capo_partnercentral_marketing.types.next_token.NextToken"
        ] = None,
    ) -> "capo_partnercentral_marketing.types.list_campaign_assets_response.ListCampaignAssetsResponse":
        """Lists assets for a campaign with pagination.

        Args:
            catalog: The catalog (AWS or Sandbox).
            campaign_identifier: The campaign identifier.
            max_results: Maximum results per page.
            next_token: Pagination token.

        Raises:
            capo_partnercentral_marketing.errors.access_denied_exception.AccessDeniedException: You do not have sufficient access to perform this action. An IAM denial carries no `Reason`. A refusal for the caller's Partner Central state carries one, so a client tells the two apart by its presence.
            capo_partnercentral_marketing.errors.internal_server_exception.InternalServerException: An unexpected error occurred during the processing of the request.
            capo_partnercentral_marketing.errors.throttling_exception.ThrottlingException: The request was denied due to request throttling.
            capo_partnercentral_marketing.errors.validation_exception.ValidationException: The input fails to satisfy the constraints specified by the service. A caller branches on `Reason`, and where the rejection is attributable to particular fields it reads `FieldList` rather than parsing `Message`, which is prose and may change.
            capo_partnercentral_marketing.errors.resource_not_found_exception.ResourceNotFoundException: The specified resource does not exist.
            capo_partnercentral_marketing.errors.UnknownServiceError: The service returned an error code this client does not model.

        Examples:
            List assets for a campaign

            >>> await client.list_campaign_assets(catalog='AWS', campaign_identifier='camp-5Hq2m8x4k1p9w')
        """

        async def _handler(
            req: "AsyncOperationRequest[capo_partnercentral_marketing.types.list_campaign_assets_request.ListCampaignAssetsRequest]",
        ) -> AsyncOperationResponse[
            "capo_partnercentral_marketing.types.list_campaign_assets_response.ListCampaignAssetsResponse"
        ]:
            import capo_partnercentral_marketing._operations.aws_partner_demand_generator.list_campaign_assets

            (
                output,
                http_response,
            ) = await capo_partnercentral_marketing._operations.aws_partner_demand_generator.list_campaign_assets.async_list_campaign_assets(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self._service.operation_options(
            config_overrides, OperationLogging("ListCampaignAssets")
        )
        input_: capo_partnercentral_marketing.types.list_campaign_assets_request.ListCampaignAssetsRequest = {
            "catalog": catalog,
            "campaign_identifier": campaign_identifier,
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

    async def start_campaign_asset_activation_task(
        self,
        catalog: "capo_partnercentral_marketing.types.catalog.Catalog",
        campaign_identifier: "capo_partnercentral_marketing.types.campaign_identifier.CampaignIdentifier",
        campaign_asset_identifiers: "capo_partnercentral_marketing.types.campaign_asset_identifiers.CampaignAssetIdentifiers",
        *,
        config_overrides: Optional[AsyncPartnerCentralMarketingClientConfig] = None,
        client_token: Optional[
            "capo_partnercentral_marketing.types.client_token.ClientToken"
        ] = None,
    ) -> "capo_partnercentral_marketing.types.start_campaign_asset_activation_task_response.StartCampaignAssetActivationTaskResponse":
        """Activates 1–25 of a campaign's assets as one ordered unit, and returns a task to poll. Takes a **list** because the service owns the ordering. Assets link to one another by URL — an email's call-to-action carries the landing page's URL, the landing page's download field carries the document's — and a URL does not exist until the asset it points at is activated. Those edges are derived by the service from the campaign's pinned template, so reconstructing and topologically sorting them is work the service has already done, and getting it wrong arms an email with a dead link. Name every asset you want live and the service sequences them; "activate everything" is the list with every id in it, which ListCampaignAssets already gave you. Asynchronous, because activating an asset installs or arms behaviour that runs later and an email activation bulk-loads its audience into the delivery platform. Everything decidable **without** a write to the delivery platform is evaluated before this returns; everything else lands on the task. A refusal that applies to one asset does not fail the request: that asset is on the task already FAILED, with its reason, and the rest run. A refusal that applies to the whole request — a malformed list, an unknown campaign, another task already running on this campaign, this service's service-linked role being deleted (ConflictException `SERVICE_LINKED_ROLE_DELETION_IN_PROGRESS`), a campaign setting an asset in the request needs (ValidationException `CAMPAIGN_INCOMPLETE`), a campaign sender that no longer passes `CreateCampaign`'s sender rules while the request names an email (ValidationException with no `FieldList`, whose message ends with one `Reason: <code>` token per failed rule: `PATTERN_MISMATCH`, `SENDER_DOMAIN_NOT_ALLIANCE_LEAD`, or `SENDER_DOMAIN_DKIM_MISSING` and/or `SENDER_DOMAIN_DMARC_MISSING`) — is thrown, and nothing starts. One task runs on a campaign at a time. A second concurrent call is refused with ConflictException / CAMPAIGN_ACTIVATION_IN_PROGRESS, whose `ResourceId` names the task already holding the campaign. Two tasks over *disjoint* asset sets are refused too: the guard is deliberately campaign-wide, because overlapping runs made the per-asset status misleading rather than merely contended.

        Args:
            catalog: The catalog (AWS or Sandbox).
            campaign_identifier: The campaign identifier, which also authorizes the call.
            campaign_asset_identifiers: The assets to activate, in any order — the service derives the dependency order and ignores the order given here.
            client_token: Idempotency token. Two requests carrying the same token are one request, and the second returns the first one's task rather than starting a second. The deduplication window is the **life of the task record**, not a fixed number of hours: replaying a token after the task has expired starts a new task. Stated because a caller would otherwise assume the usual few-hour guarantee.

        Raises:
            capo_partnercentral_marketing.errors.access_denied_exception.AccessDeniedException: You do not have sufficient access to perform this action. An IAM denial carries no `Reason`. A refusal for the caller's Partner Central state carries one, so a client tells the two apart by its presence.
            capo_partnercentral_marketing.errors.internal_server_exception.InternalServerException: An unexpected error occurred during the processing of the request.
            capo_partnercentral_marketing.errors.throttling_exception.ThrottlingException: The request was denied due to request throttling.
            capo_partnercentral_marketing.errors.validation_exception.ValidationException: The input fails to satisfy the constraints specified by the service. A caller branches on `Reason`, and where the rejection is attributable to particular fields it reads `FieldList` rather than parsing `Message`, which is prose and may change.
            capo_partnercentral_marketing.errors.conflict_exception.ConflictException: The request conflicts with the current state of the resource.
            capo_partnercentral_marketing.errors.resource_not_found_exception.ResourceNotFoundException: The specified resource does not exist.
            capo_partnercentral_marketing.errors.UnknownServiceError: The service returned an error code this client does not model.

        Examples:
            Activate a whole campaign kit

            >>> await client.start_campaign_asset_activation_task(catalog='AWS', campaign_identifier='camp-5Hq2m8x4k1p9w', campaign_asset_identifiers=['ast-4b81e0c9f2a7b', 'ast-9f3c1a2b7d40e', 'ast-2k7m4p9x1c6qd', 'ast-7w3n8r5t2h1ya'])
            Some assets refused, the rest started anyway

            >>> await client.start_campaign_asset_activation_task(catalog='AWS', campaign_identifier='camp-5Hq2m8x4k1p9w', campaign_asset_identifiers=['ast-4b81e0c9f2a7b', 'ast-9f3c1a2b7d40e', 'ast-2k7m4p9x1c6qd', 'ast-7w3n8r5t2h1ya'])
            Every asset refused, so the task is FAILED at once

            >>> await client.start_campaign_asset_activation_task(catalog='AWS', campaign_identifier='camp-5Hq2m8x4k1p9w', campaign_asset_identifiers=['ast-2k7m4p9x1c6qd'])
        """

        async def _handler(
            req: "AsyncOperationRequest[capo_partnercentral_marketing.types.start_campaign_asset_activation_task_request.StartCampaignAssetActivationTaskRequest]",
        ) -> AsyncOperationResponse[
            "capo_partnercentral_marketing.types.start_campaign_asset_activation_task_response.StartCampaignAssetActivationTaskResponse"
        ]:
            import capo_partnercentral_marketing._operations.aws_partner_demand_generator.start_campaign_asset_activation_task

            (
                output,
                http_response,
            ) = await capo_partnercentral_marketing._operations.aws_partner_demand_generator.start_campaign_asset_activation_task.async_start_campaign_asset_activation_task(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self._service.operation_options(
            config_overrides, OperationLogging("StartCampaignAssetActivationTask")
        )
        input_: capo_partnercentral_marketing.types.start_campaign_asset_activation_task_request.StartCampaignAssetActivationTaskRequest = {
            "catalog": catalog,
            "campaign_identifier": campaign_identifier,
            "campaign_asset_identifiers": campaign_asset_identifiers,
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

    async def start_campaign_asset_export_task(
        self,
        catalog: "capo_partnercentral_marketing.types.catalog.Catalog",
        campaign_identifier: "capo_partnercentral_marketing.types.campaign_identifier.CampaignIdentifier",
        *,
        config_overrides: Optional[AsyncPartnerCentralMarketingClientConfig] = None,
        client_token: Optional[
            "capo_partnercentral_marketing.types.client_token.ClientToken"
        ] = None,
    ) -> "capo_partnercentral_marketing.types.start_campaign_asset_export_task_response.StartCampaignAssetExportTaskResponse":
        """Starts an asynchronous task that packages a campaign's assets into a single downloadable ZIP archive. Fire-and-return: the campaign is validated (it must exist and not be cancelled), a task record is persisted, an asynchronous execution is started, and the task id is returned with status IN_PROGRESS. This operation does not inspect assets — all resolution, exclusion, and failure are determined by the execution and surfaced only by GetCampaignAssetExportTask. Every campaign is exportable, including one never activated, because renderable assets are composed on demand at export time rather than requiring finished, launched deliverables.

        Args:
            catalog: The catalog (AWS or Sandbox).
            campaign_identifier: The campaign whose assets are exported. Accepts the campaign id or ARN.
            client_token: Idempotency token. Two requests carrying the same token within the dedup window are one request and return the same task id.

        Raises:
            capo_partnercentral_marketing.errors.access_denied_exception.AccessDeniedException: You do not have sufficient access to perform this action. An IAM denial carries no `Reason`. A refusal for the caller's Partner Central state carries one, so a client tells the two apart by its presence.
            capo_partnercentral_marketing.errors.internal_server_exception.InternalServerException: An unexpected error occurred during the processing of the request.
            capo_partnercentral_marketing.errors.throttling_exception.ThrottlingException: The request was denied due to request throttling.
            capo_partnercentral_marketing.errors.validation_exception.ValidationException: The input fails to satisfy the constraints specified by the service. A caller branches on `Reason`, and where the rejection is attributable to particular fields it reads `FieldList` rather than parsing `Message`, which is prose and may change.
            capo_partnercentral_marketing.errors.resource_not_found_exception.ResourceNotFoundException: The specified resource does not exist.
            capo_partnercentral_marketing.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        async def _handler(
            req: "AsyncOperationRequest[capo_partnercentral_marketing.types.start_campaign_asset_export_task_request.StartCampaignAssetExportTaskRequest]",
        ) -> AsyncOperationResponse[
            "capo_partnercentral_marketing.types.start_campaign_asset_export_task_response.StartCampaignAssetExportTaskResponse"
        ]:
            import capo_partnercentral_marketing._operations.aws_partner_demand_generator.start_campaign_asset_export_task

            (
                output,
                http_response,
            ) = await capo_partnercentral_marketing._operations.aws_partner_demand_generator.start_campaign_asset_export_task.async_start_campaign_asset_export_task(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self._service.operation_options(
            config_overrides, OperationLogging("StartCampaignAssetExportTask")
        )
        input_: capo_partnercentral_marketing.types.start_campaign_asset_export_task_request.StartCampaignAssetExportTaskRequest = {
            "catalog": catalog,
            "campaign_identifier": campaign_identifier,
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

    async def update_campaign_asset(
        self,
        catalog: "capo_partnercentral_marketing.types.catalog.Catalog",
        campaign_identifier: "capo_partnercentral_marketing.types.campaign_identifier.CampaignIdentifier",
        campaign_asset_identifier: "capo_partnercentral_marketing.types.campaign_asset_id.CampaignAssetId",
        *,
        config_overrides: Optional[AsyncPartnerCentralMarketingClientConfig] = None,
        field_values: Optional[
            "capo_partnercentral_marketing.types.field_value_input_list.FieldValueInputList"
        ] = None,
        layout: Optional[
            "capo_partnercentral_marketing.types.layout_option_value.LayoutOptionValue"
        ] = None,
        send_mode: Optional[
            "capo_partnercentral_marketing.types.send_mode.SendMode"
        ] = None,
        scheduled_send_at: Optional[
            "capo_partnercentral_marketing.types.timestamp.Timestamp"
        ] = None,
        client_token: Optional[
            "capo_partnercentral_marketing.types.client_token.ClientToken"
        ] = None,
    ) -> "capo_partnercentral_marketing.types.update_campaign_asset_response.UpdateCampaignAssetResponse":
        """Updates an asset's field values, layout or send time. Refused with `ConflictException` while the campaign's running activation task still owns the asset (`ASSET_START_IN_PROGRESS`), and for a live email or social post (`ASSET_ALREADY_ACTIVE`): deactivate it first.

                Args:
                    catalog: The catalog (AWS or Sandbox).
                    campaign_identifier: The campaign identifier.
                    campaign_asset_identifier: The asset identifier.
                    field_values: Value-only updates to the asset's pinned template fields, keyed by FieldId. The field schema (labels, descriptions, constraints, placeholders, image defaults) is service-owned and pinned at instantiation, so clients send only the values they are changing. Fields omitted keep their stored values; send the entry with `Value` omitted to clear one. Named `FieldValues` to match the member it edits on `CampaignAsset`, which is the same concept read back. It was `templateFieldUpdates`; the two names for one concept were the defect, not the length.
                    layout: Selects a multi-layout asset's layout: one of the values in `CampaignAsset.layout.options`. PATCH: omitted leaves the selection unchanged, and there is no way to clear it. A value that is not one of the asset's options — or any value on a single-layout asset — is a plain `ValidationException`, and nothing in the call is applied. Every pinned field stays writable whichever layout is selected.
                    send_mode: When a **sendable** asset (`EMAIL`, `SOCIAL_POST`) sends: on activation, or at `ScheduledSendAt`. A mode beside a value rather than a union, on purpose: `ScheduledSendAt` stays a plain `Timestamp`, and the precedent is EventBridge Scheduler's `FlexibleTimeWindow { Mode, MaximumWindowInMinutes }`. The pair is checked as one, and a request where they disagree is refused with `ValidationException` (`INVALID_VALUE`, naming the member) and applies nothing: - `SCHEDULED` requires `ScheduledSendAt`; a reschedule resends `SCHEDULED` with the new time; - `ON_ACTIVATION` forbids `ScheduledSendAt`, and drops any time already stored; - `ScheduledSendAt` without `SendMode` is refused. PATCH: omitted leaves both unchanged. Until a mode is chosen the asset reports `SEND_MODE_MISSING` and does not activate: no default, because an unchosen send mails the real audience. Rejected with `ValidationException` (`NOT_SUPPORTED_FOR_CATEGORY`) for a category that has no send (`LANDING_PAGE`, `DOCUMENT`, `BANNER_AD`). Like every other edit, it reaches the delivery platform at the asset's next activation, and a live email or social post refuses it (`ASSET_ALREADY_ACTIVE`): deactivate first.
                    scheduled_send_at: The send time, with `SendMode: SCHEDULED` and only then. See `SendMode`. Must be at least an hour out (`SEND_WINDOW_TOO_SOON`), unless it is the time already stored: resending the stored mode and time changes nothing and is accepted, so a form that always resubmits does not trip the window. Must also fall on or before the campaign's `EndOn` (by the end of that UTC day): refused with `ValidationException` (`INVALID_VALUE`) otherwise, so nothing is scheduled to send after the campaign completes. Was `scheduleDate`, a `YYYY-MM-DD` string. Retyped because a date alone cannot express a send *time*, which is the whole point of a schedule — and because the resource already spelled the same concept `ScheduledSendAt` on the activation responses. Two spellings of one concept on one resource was the defect.
                    client_token: Idempotency token. Retry-safety only — this is **not** a concurrency token, and sequential edits to one field are last-writer-wins.

                Raises:
                    capo_partnercentral_marketing.errors.access_denied_exception.AccessDeniedException: You do not have sufficient access to perform this action. An IAM denial carries no `Reason`. A refusal for the caller's Partner Central state carries one, so a client tells the two apart by its presence.
                    capo_partnercentral_marketing.errors.internal_server_exception.InternalServerException: An unexpected error occurred during the processing of the request.
                    capo_partnercentral_marketing.errors.throttling_exception.ThrottlingException: The request was denied due to request throttling.
                    capo_partnercentral_marketing.errors.validation_exception.ValidationException: The input fails to satisfy the constraints specified by the service. A caller branches on `Reason`, and where the rejection is attributable to particular fields it reads `FieldList` rather than parsing `Message`, which is prose and may change.
                    capo_partnercentral_marketing.errors.conflict_exception.ConflictException: The request conflicts with the current state of the resource.
                    capo_partnercentral_marketing.errors.resource_not_found_exception.ResourceNotFoundException: The specified resource does not exist.
                    capo_partnercentral_marketing.errors.UnknownServiceError: The service returned an error code this client does not model.

                Examples:
                    Update asset content

                    >>> await client.update_campaign_asset(catalog='AWS', campaign_identifier='camp-5Hq2m8x4k1p9w', campaign_asset_identifier='ast-4b81e0c9f2a7b', field_values=[{'FieldId': 'Subject', 'Value': {'Text': 'New subject line'}}])
                    Reschedule a sendable asset

                    >>> await client.update_campaign_asset(catalog='AWS', campaign_identifier='camp-5Hq2m8x4k1p9w', campaign_asset_identifier='ast-4b81e0c9f2a7b', send_mode='SCHEDULED', scheduled_send_at=1793491200, client_token='f2a7c1e4-9b3d-4a51-8e6f-0c2d5b8a7e13')
                    Copy an image from a previous campaign's asset
                    The image already stored on another of your assets is copied into this field. It is checked
        against this field's constraints and not scanned again. The call also needs
        partnercentral:GetCampaignAsset on the source campaign.

                    >>> await client.update_campaign_asset(catalog='AWS', campaign_identifier='camp-5Hq2m8x4k1p9w', campaign_asset_identifier='ast-4b81e0c9f2a7b', field_values=[{'FieldId': 'HeaderImage', 'Value': {'CampaignAssetImage': {'CampaignIdentifier': 'camp-2Lp7d9f3j6s1z', 'CampaignAssetIdentifier': 'ast-0f9e8d7c6b5a2', 'FieldId': 'HeaderImage'}}}])
                    Use a suggested image from Build with AI
                    The URL Build with AI returned for a suggested image is sent unchanged as imageReference. The
        image is copied into this asset and not scanned. Any other URL is refused.

                    >>> await client.update_campaign_asset(catalog='AWS', campaign_identifier='camp-5Hq2m8x4k1p9w', campaign_asset_identifier='ast-4b81e0c9f2a7b', field_values=[{'FieldId': 'HeaderImage', 'Value': {'ImageReference': 'https://d111111abcdef8.cloudfront.net/suggested-image-url-from-build-with-ai.jpg'}}])
                    An update refused for two fields at once
                    Every failed field is reported in one refusal, and nothing applies — a declined image and an
        over-long headline arrive together in `fieldList`, each with its own `code`. This replaced a
        read-path `fileDetails[]` report (DG-040 Decision 11), so a partner handles image and text
        failures the same way.

                    >>> await client.update_campaign_asset(catalog='AWS', campaign_identifier='camp-5Hq2m8x4k1p9w', campaign_asset_identifier='ast-4b81e0c9f2a7b', field_values=[{'FieldId': 'HeaderImage', 'Value': {'ImageReference': 's3://staging-bucket/123456789012/hero.png?versionId=v1'}}, {'FieldId': 'Headline', 'Value': {'Text': 'This headline is far longer than the field allows'}}])
        """

        async def _handler(
            req: "AsyncOperationRequest[capo_partnercentral_marketing.types.update_campaign_asset_request.UpdateCampaignAssetRequest]",
        ) -> AsyncOperationResponse[
            "capo_partnercentral_marketing.types.update_campaign_asset_response.UpdateCampaignAssetResponse"
        ]:
            import capo_partnercentral_marketing._operations.aws_partner_demand_generator.update_campaign_asset

            (
                output,
                http_response,
            ) = await capo_partnercentral_marketing._operations.aws_partner_demand_generator.update_campaign_asset.async_update_campaign_asset(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        def _redact_input(
            input_: "capo_partnercentral_marketing.types.update_campaign_asset_request.UpdateCampaignAssetRequest",
        ) -> dict[str, Any]:
            import capo_partnercentral_marketing.types.update_campaign_asset_request

            return capo_partnercentral_marketing.types.update_campaign_asset_request.redact_sensitive(
                input_
            )

        interceptors_, options_ = self._service.operation_options(
            config_overrides,
            OperationLogging("UpdateCampaignAsset", redact_input=_redact_input),
        )
        input_: capo_partnercentral_marketing.types.update_campaign_asset_request.UpdateCampaignAssetRequest = {
            "catalog": catalog,
            "campaign_identifier": campaign_identifier,
            "campaign_asset_identifier": campaign_asset_identifier,
        }
        if field_values is not None:
            input_["field_values"] = field_values
        if layout is not None:
            input_["layout"] = layout
        if send_mode is not None:
            input_["send_mode"] = send_mode
        if scheduled_send_at is not None:
            input_["scheduled_send_at"] = scheduled_send_at
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
