"""Generated from Smithy shape ``com.amazonaws.datazone#DataZone``."""

import datetime
import uuid
import warnings
from collections.abc import AsyncIterator
from typing import TYPE_CHECKING, Any, Iterable, Optional

from typing_extensions import Self, TypedDict
from zapros import AsyncBaseHandler, AsyncClient

import capo_datazone._auth._signers
import capo_datazone._auth._sigv4
from capo_datazone._auth._identity import Credentials
from capo_datazone._auth._providers import (
    CredentialsProvider,
    IdentityProvider,
    StaticAwsCredentialsProvider,
    default_aws_credentials_chain,
)
from capo_datazone._auth._zapros_handler import AuthMiddleware
from capo_datazone._pagination import resolve_path as _resolve_path
from capo_datazone._resources.data_zone.asset import AsyncAsset
from capo_datazone._resources.data_zone.asset_type import AsyncAssetType
from capo_datazone._resources.data_zone.data_product import AsyncDataProduct
from capo_datazone._resources.data_zone.data_source import AsyncDataSource
from capo_datazone._resources.data_zone.data_source_run import AsyncDataSourceRun
from capo_datazone._resources.data_zone.domain import AsyncDomain
from capo_datazone._resources.data_zone.domain_unit import AsyncDomainUnit
from capo_datazone._resources.data_zone.environment_blueprint_configuration import (
    AsyncEnvironmentBlueprintConfiguration,
)
from capo_datazone._resources.data_zone.form_type import AsyncFormType
from capo_datazone._resources.data_zone.glossary import AsyncGlossary
from capo_datazone._resources.data_zone.glossary_term import AsyncGlossaryTerm
from capo_datazone._resources.data_zone.listing import AsyncListing
from capo_datazone._resources.data_zone.metadata_generation_run import (
    AsyncMetadataGenerationRun,
)
from capo_datazone._resources.data_zone.notebook import AsyncNotebook
from capo_datazone._resources.data_zone.notebook_export import AsyncNotebookExport
from capo_datazone._resources.data_zone.notebook_run import AsyncNotebookRun
from capo_datazone._resources.data_zone.rule import AsyncRule
from capo_datazone._services._aws_config import aaws_config
from capo_datazone._services._pipeline import (
    AsyncInterceptor,
    AsyncOperationOptions,
    AsyncOperationRequest,
    AsyncOperationResponse,
    aexecute_pipeline,
    aretry,
)

if TYPE_CHECKING:
    import capo_datazone.types.accept_choices
    import capo_datazone.types.accept_predictions_input
    import capo_datazone.types.accept_predictions_output
    import capo_datazone.types.accept_rule
    import capo_datazone.types.accept_subscription_request_input
    import capo_datazone.types.accept_subscription_request_output
    import capo_datazone.types.accepted_asset_scopes
    import capo_datazone.types.account_info
    import capo_datazone.types.account_pool_id
    import capo_datazone.types.account_pool_name
    import capo_datazone.types.account_pool_summary
    import capo_datazone.types.account_source
    import capo_datazone.types.action_parameters
    import capo_datazone.types.add_entity_owner_input
    import capo_datazone.types.add_entity_owner_output
    import capo_datazone.types.add_policy_grant_input
    import capo_datazone.types.add_policy_grant_output
    import capo_datazone.types.additional_attributes
    import capo_datazone.types.aggregation_list
    import capo_datazone.types.applicable_asset_types
    import capo_datazone.types.asset_filter_configuration
    import capo_datazone.types.asset_filter_summary
    import capo_datazone.types.asset_id
    import capo_datazone.types.asset_identifier
    import capo_datazone.types.asset_name
    import capo_datazone.types.asset_permissions
    import capo_datazone.types.asset_target_names
    import capo_datazone.types.asset_type_identifier
    import capo_datazone.types.asset_type_identifiers
    import capo_datazone.types.associate_environment_role_input
    import capo_datazone.types.associate_environment_role_output
    import capo_datazone.types.associate_governed_terms_input
    import capo_datazone.types.associate_governed_terms_output
    import capo_datazone.types.attribute_entity_type
    import capo_datazone.types.attributes
    import capo_datazone.types.attributes_list
    import capo_datazone.types.authorized_principal_identifiers
    import capo_datazone.types.aws_account_id
    import capo_datazone.types.aws_location
    import capo_datazone.types.aws_region
    import capo_datazone.types.batch_get_attributes_metadata_input
    import capo_datazone.types.batch_get_attributes_metadata_output
    import capo_datazone.types.batch_put_attributes_metadata_input
    import capo_datazone.types.batch_put_attributes_metadata_output
    import capo_datazone.types.blueprint_category
    import capo_datazone.types.cancel_metadata_generation_run_input
    import capo_datazone.types.cancel_metadata_generation_run_output
    import capo_datazone.types.cancel_subscription_input
    import capo_datazone.types.cancel_subscription_output
    import capo_datazone.types.cell_order
    import capo_datazone.types.change_action
    import capo_datazone.types.client_token
    import capo_datazone.types.compute_config
    import capo_datazone.types.configurations
    import capo_datazone.types.connection_id
    import capo_datazone.types.connection_name
    import capo_datazone.types.connection_properties_input
    import capo_datazone.types.connection_properties_patch
    import capo_datazone.types.connection_scope
    import capo_datazone.types.connection_summary
    import capo_datazone.types.connection_type
    import capo_datazone.types.create_account_pool_input
    import capo_datazone.types.create_account_pool_output
    import capo_datazone.types.create_asset_filter_input
    import capo_datazone.types.create_asset_filter_output
    import capo_datazone.types.create_asset_input
    import capo_datazone.types.create_asset_output
    import capo_datazone.types.create_asset_revision_input
    import capo_datazone.types.create_asset_revision_output
    import capo_datazone.types.create_asset_type_input
    import capo_datazone.types.create_asset_type_output
    import capo_datazone.types.create_connection_input
    import capo_datazone.types.create_connection_output
    import capo_datazone.types.create_data_product_input
    import capo_datazone.types.create_data_product_output
    import capo_datazone.types.create_data_product_revision_input
    import capo_datazone.types.create_data_product_revision_output
    import capo_datazone.types.create_data_source_input
    import capo_datazone.types.create_data_source_output
    import capo_datazone.types.create_domain_input
    import capo_datazone.types.create_domain_output
    import capo_datazone.types.create_domain_unit_input
    import capo_datazone.types.create_domain_unit_output
    import capo_datazone.types.create_environment_action_input
    import capo_datazone.types.create_environment_action_output
    import capo_datazone.types.create_environment_blueprint_input
    import capo_datazone.types.create_environment_blueprint_output
    import capo_datazone.types.create_environment_input
    import capo_datazone.types.create_environment_output
    import capo_datazone.types.create_environment_profile_input
    import capo_datazone.types.create_environment_profile_output
    import capo_datazone.types.create_form_type_input
    import capo_datazone.types.create_form_type_output
    import capo_datazone.types.create_glossary_input
    import capo_datazone.types.create_glossary_output
    import capo_datazone.types.create_glossary_term_input
    import capo_datazone.types.create_glossary_term_output
    import capo_datazone.types.create_group_profile_input
    import capo_datazone.types.create_group_profile_output
    import capo_datazone.types.create_listing_change_set_input
    import capo_datazone.types.create_listing_change_set_output
    import capo_datazone.types.create_notebook_input
    import capo_datazone.types.create_notebook_output
    import capo_datazone.types.create_project_input
    import capo_datazone.types.create_project_membership_input
    import capo_datazone.types.create_project_membership_output
    import capo_datazone.types.create_project_output
    import capo_datazone.types.create_project_profile_input
    import capo_datazone.types.create_project_profile_output
    import capo_datazone.types.create_rule_input
    import capo_datazone.types.create_rule_output
    import capo_datazone.types.create_subscription_grant_input
    import capo_datazone.types.create_subscription_grant_output
    import capo_datazone.types.create_subscription_request_input
    import capo_datazone.types.create_subscription_request_output
    import capo_datazone.types.create_subscription_target_input
    import capo_datazone.types.create_subscription_target_output
    import capo_datazone.types.create_user_profile_input
    import capo_datazone.types.create_user_profile_output
    import capo_datazone.types.custom_parameter_list
    import capo_datazone.types.data_asset_activity_status
    import capo_datazone.types.data_product_description
    import capo_datazone.types.data_product_id
    import capo_datazone.types.data_product_items
    import capo_datazone.types.data_product_name
    import capo_datazone.types.data_product_revision
    import capo_datazone.types.data_source_configuration_input
    import capo_datazone.types.data_source_id
    import capo_datazone.types.data_source_run_activity
    import capo_datazone.types.data_source_run_id
    import capo_datazone.types.data_source_run_status
    import capo_datazone.types.data_source_run_summary
    import capo_datazone.types.data_source_status
    import capo_datazone.types.data_source_summary
    import capo_datazone.types.data_source_type
    import capo_datazone.types.data_zone_entity_type
    import capo_datazone.types.decision_comment
    import capo_datazone.types.delete_account_pool_input
    import capo_datazone.types.delete_account_pool_output
    import capo_datazone.types.delete_asset_filter_input
    import capo_datazone.types.delete_asset_input
    import capo_datazone.types.delete_asset_output
    import capo_datazone.types.delete_asset_type_input
    import capo_datazone.types.delete_asset_type_output
    import capo_datazone.types.delete_connection_input
    import capo_datazone.types.delete_connection_output
    import capo_datazone.types.delete_data_export_configuration_input
    import capo_datazone.types.delete_data_export_configuration_output
    import capo_datazone.types.delete_data_product_input
    import capo_datazone.types.delete_data_product_output
    import capo_datazone.types.delete_data_source_input
    import capo_datazone.types.delete_data_source_output
    import capo_datazone.types.delete_domain_input
    import capo_datazone.types.delete_domain_output
    import capo_datazone.types.delete_domain_unit_input
    import capo_datazone.types.delete_domain_unit_output
    import capo_datazone.types.delete_environment_action_input
    import capo_datazone.types.delete_environment_blueprint_configuration_input
    import capo_datazone.types.delete_environment_blueprint_configuration_output
    import capo_datazone.types.delete_environment_blueprint_input
    import capo_datazone.types.delete_environment_input
    import capo_datazone.types.delete_environment_profile_input
    import capo_datazone.types.delete_form_type_input
    import capo_datazone.types.delete_form_type_output
    import capo_datazone.types.delete_glossary_input
    import capo_datazone.types.delete_glossary_output
    import capo_datazone.types.delete_glossary_term_input
    import capo_datazone.types.delete_glossary_term_output
    import capo_datazone.types.delete_lineage_event_input
    import capo_datazone.types.delete_lineage_event_output
    import capo_datazone.types.delete_listing_input
    import capo_datazone.types.delete_listing_output
    import capo_datazone.types.delete_notebook_input
    import capo_datazone.types.delete_notebook_output
    import capo_datazone.types.delete_project_input
    import capo_datazone.types.delete_project_membership_input
    import capo_datazone.types.delete_project_membership_output
    import capo_datazone.types.delete_project_output
    import capo_datazone.types.delete_project_profile_input
    import capo_datazone.types.delete_project_profile_output
    import capo_datazone.types.delete_rule_input
    import capo_datazone.types.delete_rule_output
    import capo_datazone.types.delete_subscription_grant_input
    import capo_datazone.types.delete_subscription_grant_output
    import capo_datazone.types.delete_subscription_request_input
    import capo_datazone.types.delete_subscription_target_input
    import capo_datazone.types.delete_time_series_data_points_input
    import capo_datazone.types.delete_time_series_data_points_output
    import capo_datazone.types.description
    import capo_datazone.types.disassociate_environment_role_input
    import capo_datazone.types.disassociate_environment_role_output
    import capo_datazone.types.disassociate_governed_terms_input
    import capo_datazone.types.disassociate_governed_terms_output
    import capo_datazone.types.domain_id
    import capo_datazone.types.domain_status
    import capo_datazone.types.domain_summary
    import capo_datazone.types.domain_unit_description
    import capo_datazone.types.domain_unit_id
    import capo_datazone.types.domain_unit_name
    import capo_datazone.types.domain_unit_summary
    import capo_datazone.types.domain_version
    import capo_datazone.types.edge_direction
    import capo_datazone.types.enable_setting
    import capo_datazone.types.enabled_region_list
    import capo_datazone.types.encryption_configuration
    import capo_datazone.types.entity_id
    import capo_datazone.types.entity_identifier
    import capo_datazone.types.entity_type
    import capo_datazone.types.environment_action_summary
    import capo_datazone.types.environment_blueprint_configuration_item
    import capo_datazone.types.environment_blueprint_id
    import capo_datazone.types.environment_blueprint_name
    import capo_datazone.types.environment_blueprint_summary
    import capo_datazone.types.environment_config
    import capo_datazone.types.environment_configuration_name
    import capo_datazone.types.environment_configuration_user_parameters_list
    import capo_datazone.types.environment_configurations_list
    import capo_datazone.types.environment_deployment_details
    import capo_datazone.types.environment_id
    import capo_datazone.types.environment_parameters_list
    import capo_datazone.types.environment_profile_id
    import capo_datazone.types.environment_profile_name
    import capo_datazone.types.environment_profile_summary
    import capo_datazone.types.environment_status
    import capo_datazone.types.environment_summary
    import capo_datazone.types.export_id
    import capo_datazone.types.external_identifier
    import capo_datazone.types.failure_cause
    import capo_datazone.types.file_format
    import capo_datazone.types.filter_clause
    import capo_datazone.types.filter_id
    import capo_datazone.types.filter_name
    import capo_datazone.types.filter_status
    import capo_datazone.types.form_input_list
    import capo_datazone.types.form_type_identifier
    import capo_datazone.types.form_type_name
    import capo_datazone.types.form_type_status
    import capo_datazone.types.forms_input_map
    import capo_datazone.types.get_account_pool_input
    import capo_datazone.types.get_account_pool_output
    import capo_datazone.types.get_asset_filter_input
    import capo_datazone.types.get_asset_filter_output
    import capo_datazone.types.get_asset_input
    import capo_datazone.types.get_asset_output
    import capo_datazone.types.get_asset_type_input
    import capo_datazone.types.get_asset_type_output
    import capo_datazone.types.get_connection_input
    import capo_datazone.types.get_connection_output
    import capo_datazone.types.get_data_export_configuration_input
    import capo_datazone.types.get_data_export_configuration_output
    import capo_datazone.types.get_data_product_input
    import capo_datazone.types.get_data_product_output
    import capo_datazone.types.get_data_source_input
    import capo_datazone.types.get_data_source_output
    import capo_datazone.types.get_data_source_run_input
    import capo_datazone.types.get_data_source_run_output
    import capo_datazone.types.get_domain_input
    import capo_datazone.types.get_domain_output
    import capo_datazone.types.get_domain_unit_input
    import capo_datazone.types.get_domain_unit_output
    import capo_datazone.types.get_environment_action_input
    import capo_datazone.types.get_environment_action_output
    import capo_datazone.types.get_environment_blueprint_configuration_input
    import capo_datazone.types.get_environment_blueprint_configuration_output
    import capo_datazone.types.get_environment_blueprint_input
    import capo_datazone.types.get_environment_blueprint_output
    import capo_datazone.types.get_environment_credentials_input
    import capo_datazone.types.get_environment_credentials_output
    import capo_datazone.types.get_environment_input
    import capo_datazone.types.get_environment_output
    import capo_datazone.types.get_environment_profile_input
    import capo_datazone.types.get_environment_profile_output
    import capo_datazone.types.get_form_type_input
    import capo_datazone.types.get_form_type_output
    import capo_datazone.types.get_glossary_input
    import capo_datazone.types.get_glossary_output
    import capo_datazone.types.get_glossary_term_input
    import capo_datazone.types.get_glossary_term_output
    import capo_datazone.types.get_group_profile_input
    import capo_datazone.types.get_group_profile_output
    import capo_datazone.types.get_iam_portal_login_url_input
    import capo_datazone.types.get_iam_portal_login_url_output
    import capo_datazone.types.get_job_run_input
    import capo_datazone.types.get_job_run_output
    import capo_datazone.types.get_lineage_event_input
    import capo_datazone.types.get_lineage_event_output
    import capo_datazone.types.get_lineage_node_input
    import capo_datazone.types.get_lineage_node_output
    import capo_datazone.types.get_listing_input
    import capo_datazone.types.get_listing_output
    import capo_datazone.types.get_metadata_generation_run_input
    import capo_datazone.types.get_metadata_generation_run_output
    import capo_datazone.types.get_notebook_export_input
    import capo_datazone.types.get_notebook_export_output
    import capo_datazone.types.get_notebook_input
    import capo_datazone.types.get_notebook_output
    import capo_datazone.types.get_notebook_run_input
    import capo_datazone.types.get_notebook_run_output
    import capo_datazone.types.get_project_input
    import capo_datazone.types.get_project_output
    import capo_datazone.types.get_project_profile_input
    import capo_datazone.types.get_project_profile_output
    import capo_datazone.types.get_rule_input
    import capo_datazone.types.get_rule_output
    import capo_datazone.types.get_subscription_grant_input
    import capo_datazone.types.get_subscription_grant_output
    import capo_datazone.types.get_subscription_input
    import capo_datazone.types.get_subscription_output
    import capo_datazone.types.get_subscription_request_details_input
    import capo_datazone.types.get_subscription_request_details_output
    import capo_datazone.types.get_subscription_target_input
    import capo_datazone.types.get_subscription_target_output
    import capo_datazone.types.get_time_series_data_point_input
    import capo_datazone.types.get_time_series_data_point_output
    import capo_datazone.types.get_user_profile_input
    import capo_datazone.types.get_user_profile_output
    import capo_datazone.types.git_metadata
    import capo_datazone.types.global_parameter_map
    import capo_datazone.types.glossary_description
    import capo_datazone.types.glossary_id
    import capo_datazone.types.glossary_name
    import capo_datazone.types.glossary_status
    import capo_datazone.types.glossary_term_id
    import capo_datazone.types.glossary_term_name
    import capo_datazone.types.glossary_term_status
    import capo_datazone.types.glossary_terms
    import capo_datazone.types.glossary_usage_restrictions
    import capo_datazone.types.governed_entity_type
    import capo_datazone.types.governed_glossary_terms
    import capo_datazone.types.grant_identifier
    import capo_datazone.types.granted_entity_input
    import capo_datazone.types.group_identifier
    import capo_datazone.types.group_profile_id
    import capo_datazone.types.group_profile_status
    import capo_datazone.types.group_profile_summary
    import capo_datazone.types.group_search_text
    import capo_datazone.types.group_search_type
    import capo_datazone.types.iam_principal_arn
    import capo_datazone.types.iam_role_arn
    import capo_datazone.types.inventory_search_scope
    import capo_datazone.types.job_run_status
    import capo_datazone.types.job_run_summary
    import capo_datazone.types.kms_key_arn
    import capo_datazone.types.lineage_event
    import capo_datazone.types.lineage_event_identifier
    import capo_datazone.types.lineage_event_processing_status
    import capo_datazone.types.lineage_event_summary
    import capo_datazone.types.lineage_node_identifier
    import capo_datazone.types.lineage_node_summary
    import capo_datazone.types.list_account_pools_input
    import capo_datazone.types.list_account_pools_output
    import capo_datazone.types.list_accounts_in_account_pool_input
    import capo_datazone.types.list_accounts_in_account_pool_output
    import capo_datazone.types.list_asset_filters_input
    import capo_datazone.types.list_asset_filters_output
    import capo_datazone.types.list_asset_revisions_input
    import capo_datazone.types.list_asset_revisions_output
    import capo_datazone.types.list_connections_input
    import capo_datazone.types.list_connections_output
    import capo_datazone.types.list_data_product_revisions_input
    import capo_datazone.types.list_data_product_revisions_output
    import capo_datazone.types.list_data_source_run_activities_input
    import capo_datazone.types.list_data_source_run_activities_output
    import capo_datazone.types.list_data_source_runs_input
    import capo_datazone.types.list_data_source_runs_output
    import capo_datazone.types.list_data_sources_input
    import capo_datazone.types.list_data_sources_output
    import capo_datazone.types.list_domain_units_for_parent_input
    import capo_datazone.types.list_domain_units_for_parent_output
    import capo_datazone.types.list_domains_input
    import capo_datazone.types.list_domains_output
    import capo_datazone.types.list_entity_owners_input
    import capo_datazone.types.list_entity_owners_output
    import capo_datazone.types.list_environment_actions_input
    import capo_datazone.types.list_environment_actions_output
    import capo_datazone.types.list_environment_blueprint_configurations_input
    import capo_datazone.types.list_environment_blueprint_configurations_output
    import capo_datazone.types.list_environment_blueprints_input
    import capo_datazone.types.list_environment_blueprints_output
    import capo_datazone.types.list_environment_profiles_input
    import capo_datazone.types.list_environment_profiles_output
    import capo_datazone.types.list_environments_input
    import capo_datazone.types.list_environments_output
    import capo_datazone.types.list_job_runs_input
    import capo_datazone.types.list_job_runs_output
    import capo_datazone.types.list_lineage_events_input
    import capo_datazone.types.list_lineage_events_output
    import capo_datazone.types.list_lineage_node_history_input
    import capo_datazone.types.list_lineage_node_history_output
    import capo_datazone.types.list_metadata_generation_runs_input
    import capo_datazone.types.list_metadata_generation_runs_output
    import capo_datazone.types.list_notebook_runs_input
    import capo_datazone.types.list_notebook_runs_output
    import capo_datazone.types.list_notebooks_input
    import capo_datazone.types.list_notebooks_output
    import capo_datazone.types.list_notifications_input
    import capo_datazone.types.list_notifications_output
    import capo_datazone.types.list_policy_grants_input
    import capo_datazone.types.list_policy_grants_output
    import capo_datazone.types.list_project_memberships_input
    import capo_datazone.types.list_project_memberships_output
    import capo_datazone.types.list_project_profiles_input
    import capo_datazone.types.list_project_profiles_output
    import capo_datazone.types.list_projects_input
    import capo_datazone.types.list_projects_output
    import capo_datazone.types.list_rules_input
    import capo_datazone.types.list_rules_output
    import capo_datazone.types.list_subscription_grants_input
    import capo_datazone.types.list_subscription_grants_output
    import capo_datazone.types.list_subscription_requests_input
    import capo_datazone.types.list_subscription_requests_output
    import capo_datazone.types.list_subscription_targets_input
    import capo_datazone.types.list_subscription_targets_output
    import capo_datazone.types.list_subscriptions_input
    import capo_datazone.types.list_subscriptions_output
    import capo_datazone.types.list_tags_for_resource_request
    import capo_datazone.types.list_tags_for_resource_response
    import capo_datazone.types.list_time_series_data_points_input
    import capo_datazone.types.list_time_series_data_points_output
    import capo_datazone.types.listing_id
    import capo_datazone.types.long_description
    import capo_datazone.types.managed_policy_type
    import capo_datazone.types.match_clauses
    import capo_datazone.types.max_results
    import capo_datazone.types.max_results_for_list_domains
    import capo_datazone.types.member
    import capo_datazone.types.metadata
    import capo_datazone.types.metadata_form_inputs
    import capo_datazone.types.metadata_generation_run_identifier
    import capo_datazone.types.metadata_generation_run_item
    import capo_datazone.types.metadata_generation_run_status
    import capo_datazone.types.metadata_generation_run_target
    import capo_datazone.types.metadata_generation_run_type
    import capo_datazone.types.metadata_generation_run_types
    import capo_datazone.types.model
    import capo_datazone.types.name
    import capo_datazone.types.network_config
    import capo_datazone.types.notebook_id
    import capo_datazone.types.notebook_name
    import capo_datazone.types.notebook_run_id
    import capo_datazone.types.notebook_run_status
    import capo_datazone.types.notebook_run_summary
    import capo_datazone.types.notebook_status
    import capo_datazone.types.notebook_summary
    import capo_datazone.types.notebook_type
    import capo_datazone.types.notification_output
    import capo_datazone.types.notification_subjects
    import capo_datazone.types.notification_type
    import capo_datazone.types.owner_properties
    import capo_datazone.types.owner_properties_output
    import capo_datazone.types.pagination_token
    import capo_datazone.types.parameters
    import capo_datazone.types.policy_arn
    import capo_datazone.types.policy_grant_detail
    import capo_datazone.types.policy_grant_member
    import capo_datazone.types.policy_grant_principal
    import capo_datazone.types.post_lineage_event_input
    import capo_datazone.types.post_lineage_event_output
    import capo_datazone.types.post_time_series_data_points_input
    import capo_datazone.types.post_time_series_data_points_output
    import capo_datazone.types.prediction_configuration
    import capo_datazone.types.project_id
    import capo_datazone.types.project_ids
    import capo_datazone.types.project_member
    import capo_datazone.types.project_membership_assignments
    import capo_datazone.types.project_name
    import capo_datazone.types.project_profile_id
    import capo_datazone.types.project_profile_name
    import capo_datazone.types.project_profile_summary
    import capo_datazone.types.project_resource_tag_parameters
    import capo_datazone.types.project_summary
    import capo_datazone.types.provisioning_configuration_list
    import capo_datazone.types.provisioning_properties
    import capo_datazone.types.put_data_export_configuration_input
    import capo_datazone.types.put_data_export_configuration_output
    import capo_datazone.types.put_environment_blueprint_configuration_input
    import capo_datazone.types.put_environment_blueprint_configuration_output
    import capo_datazone.types.put_resource_configurations
    import capo_datazone.types.query_graph_input
    import capo_datazone.types.query_graph_output
    import capo_datazone.types.recommendation_configuration
    import capo_datazone.types.regional_parameter_map
    import capo_datazone.types.reject_choices
    import capo_datazone.types.reject_predictions_input
    import capo_datazone.types.reject_predictions_output
    import capo_datazone.types.reject_rule
    import capo_datazone.types.reject_subscription_request_input
    import capo_datazone.types.reject_subscription_request_output
    import capo_datazone.types.remove_entity_owner_input
    import capo_datazone.types.remove_entity_owner_output
    import capo_datazone.types.remove_policy_grant_input
    import capo_datazone.types.remove_policy_grant_output
    import capo_datazone.types.request_reason
    import capo_datazone.types.resolution_strategy
    import capo_datazone.types.result_item
    import capo_datazone.types.revision
    import capo_datazone.types.revoke_subscription_input
    import capo_datazone.types.revoke_subscription_output
    import capo_datazone.types.role_arn
    import capo_datazone.types.rule_action
    import capo_datazone.types.rule_detail
    import capo_datazone.types.rule_id
    import capo_datazone.types.rule_name
    import capo_datazone.types.rule_scope
    import capo_datazone.types.rule_summary
    import capo_datazone.types.rule_target
    import capo_datazone.types.rule_target_type
    import capo_datazone.types.rule_type
    import capo_datazone.types.run_identifier
    import capo_datazone.types.schedule_configuration
    import capo_datazone.types.schedule_id
    import capo_datazone.types.search_group_profiles_input
    import capo_datazone.types.search_group_profiles_output
    import capo_datazone.types.search_in_list
    import capo_datazone.types.search_input
    import capo_datazone.types.search_inventory_result_item
    import capo_datazone.types.search_listings_input
    import capo_datazone.types.search_listings_output
    import capo_datazone.types.search_output
    import capo_datazone.types.search_output_additional_attributes
    import capo_datazone.types.search_result_item
    import capo_datazone.types.search_sort
    import capo_datazone.types.search_text
    import capo_datazone.types.search_types_input
    import capo_datazone.types.search_types_output
    import capo_datazone.types.search_types_result_item
    import capo_datazone.types.search_user_profiles_input
    import capo_datazone.types.search_user_profiles_output
    import capo_datazone.types.short_description
    import capo_datazone.types.single_sign_on
    import capo_datazone.types.sort_field_account_pool
    import capo_datazone.types.sort_field_connection
    import capo_datazone.types.sort_field_project
    import capo_datazone.types.sort_key
    import capo_datazone.types.sort_order
    import capo_datazone.types.source_location
    import capo_datazone.types.start_data_source_run_input
    import capo_datazone.types.start_data_source_run_output
    import capo_datazone.types.start_metadata_generation_run_input
    import capo_datazone.types.start_metadata_generation_run_output
    import capo_datazone.types.start_notebook_export_input
    import capo_datazone.types.start_notebook_export_output
    import capo_datazone.types.start_notebook_import_input
    import capo_datazone.types.start_notebook_import_output
    import capo_datazone.types.start_notebook_run_input
    import capo_datazone.types.start_notebook_run_output
    import capo_datazone.types.start_notebook_sync_input
    import capo_datazone.types.start_notebook_sync_output
    import capo_datazone.types.status
    import capo_datazone.types.stop_notebook_run_input
    import capo_datazone.types.stop_notebook_run_output
    import capo_datazone.types.subscribed_listing_inputs
    import capo_datazone.types.subscribed_principal_inputs
    import capo_datazone.types.subscription_grant_creation_mode
    import capo_datazone.types.subscription_grant_id
    import capo_datazone.types.subscription_grant_status
    import capo_datazone.types.subscription_grant_summary
    import capo_datazone.types.subscription_id
    import capo_datazone.types.subscription_request_id
    import capo_datazone.types.subscription_request_status
    import capo_datazone.types.subscription_request_summary
    import capo_datazone.types.subscription_status
    import capo_datazone.types.subscription_summary
    import capo_datazone.types.subscription_target_forms
    import capo_datazone.types.subscription_target_id
    import capo_datazone.types.subscription_target_name
    import capo_datazone.types.subscription_target_summary
    import capo_datazone.types.tag_key_list
    import capo_datazone.types.tag_resource_request
    import capo_datazone.types.tag_resource_response
    import capo_datazone.types.tags
    import capo_datazone.types.target_entity_type
    import capo_datazone.types.task_status
    import capo_datazone.types.term_relations
    import capo_datazone.types.time_series_data_point_form_input_list
    import capo_datazone.types.time_series_data_point_identifier
    import capo_datazone.types.time_series_data_point_summary_form_output
    import capo_datazone.types.time_series_entity_type
    import capo_datazone.types.time_series_form_name
    import capo_datazone.types.timeout_config
    import capo_datazone.types.trigger_source
    import capo_datazone.types.type_name
    import capo_datazone.types.types_search_scope
    import capo_datazone.types.untag_resource_request
    import capo_datazone.types.untag_resource_response
    import capo_datazone.types.update_account_pool_input
    import capo_datazone.types.update_account_pool_output
    import capo_datazone.types.update_asset_filter_input
    import capo_datazone.types.update_asset_filter_output
    import capo_datazone.types.update_connection_input
    import capo_datazone.types.update_connection_output
    import capo_datazone.types.update_data_source_input
    import capo_datazone.types.update_data_source_output
    import capo_datazone.types.update_domain_input
    import capo_datazone.types.update_domain_output
    import capo_datazone.types.update_domain_unit_input
    import capo_datazone.types.update_domain_unit_output
    import capo_datazone.types.update_environment_action_input
    import capo_datazone.types.update_environment_action_output
    import capo_datazone.types.update_environment_blueprint_input
    import capo_datazone.types.update_environment_blueprint_output
    import capo_datazone.types.update_environment_input
    import capo_datazone.types.update_environment_output
    import capo_datazone.types.update_environment_profile_input
    import capo_datazone.types.update_environment_profile_output
    import capo_datazone.types.update_glossary_input
    import capo_datazone.types.update_glossary_output
    import capo_datazone.types.update_glossary_term_input
    import capo_datazone.types.update_glossary_term_output
    import capo_datazone.types.update_group_profile_input
    import capo_datazone.types.update_group_profile_output
    import capo_datazone.types.update_notebook_input
    import capo_datazone.types.update_notebook_output
    import capo_datazone.types.update_project_input
    import capo_datazone.types.update_project_output
    import capo_datazone.types.update_project_profile_input
    import capo_datazone.types.update_project_profile_output
    import capo_datazone.types.update_root_domain_unit_owner_input
    import capo_datazone.types.update_root_domain_unit_owner_output
    import capo_datazone.types.update_rule_input
    import capo_datazone.types.update_rule_output
    import capo_datazone.types.update_subscription_grant_status_input
    import capo_datazone.types.update_subscription_grant_status_output
    import capo_datazone.types.update_subscription_request_input
    import capo_datazone.types.update_subscription_request_output
    import capo_datazone.types.update_subscription_target_input
    import capo_datazone.types.update_subscription_target_output
    import capo_datazone.types.update_user_profile_input
    import capo_datazone.types.update_user_profile_output
    import capo_datazone.types.user_designation
    import capo_datazone.types.user_identifier
    import capo_datazone.types.user_profile_id
    import capo_datazone.types.user_profile_status
    import capo_datazone.types.user_profile_summary
    import capo_datazone.types.user_profile_type
    import capo_datazone.types.user_search_text
    import capo_datazone.types.user_search_type
    import capo_datazone.types.user_type


class AsyncDataZoneClientConfig(TypedDict, total=False, closed=True):
    operation_interceptors: Iterable[AsyncInterceptor[Any, Any]]
    retry_max_attempts: int | None
    region: str | None
    use_fips: bool | None
    endpoint: str | None
    credentials_provider: IdentityProvider[Credentials] | None


class AsyncDataZoneClient:
    """A client for the ``DataZone`` service.

    Args:
        http_handler: HTTP handler for sending requests. If not provided, creates a default handler.
        operation_interceptors: Interceptors that wrap every operation call. If not provided, defaults to an empty list.
        retry_max_attempts: Maximum number of times to retry a failed operation. Defaults to 3.
        region: The value of the ``AWS::Region`` endpoint parameter.
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
        self._config = AsyncDataZoneClientConfig(
            {
                "operation_interceptors": operation_interceptors or [],
                "retry_max_attempts": retry_max_attempts,
                "region": region,
                "use_fips": use_fips,
                "endpoint": endpoint,
                "credentials_provider": resolved_credentials_provider,
            }
        )

        # resources
        self.asset = AsyncAsset(self)
        self.asset_type = AsyncAssetType(self)
        self.data_product = AsyncDataProduct(self)
        self.data_source = AsyncDataSource(self)
        self.data_source_run = AsyncDataSourceRun(self)
        self.domain = AsyncDomain(self)
        self.domain_unit = AsyncDomainUnit(self)
        self.environment_blueprint_configuration = (
            AsyncEnvironmentBlueprintConfiguration(self)
        )
        self.form_type = AsyncFormType(self)
        self.glossary = AsyncGlossary(self)
        self.glossary_term = AsyncGlossaryTerm(self)
        self.listing = AsyncListing(self)
        self.metadata_generation_run = AsyncMetadataGenerationRun(self)
        self.notebook = AsyncNotebook(self)
        self.notebook_export = AsyncNotebookExport(self)
        self.notebook_run = AsyncNotebookRun(self)
        self.rule = AsyncRule(self)

    def operation_options(
        self, config_overrides: Optional[AsyncDataZoneClientConfig] = None
    ) -> tuple[Iterable[AsyncInterceptor[Any, Any]], AsyncOperationOptions]:
        overrides: AsyncDataZoneClientConfig = config_overrides or {}
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
            use_fips=overrides.get("use_fips", self._config.get("use_fips")),
            endpoint=overrides.get("endpoint", self._config.get("endpoint")),
            credentials_provider=overrides.get(
                "credentials_provider", self._config.get("credentials_provider")
            ),
        )
        return interceptors_, options_

    async def accept_predictions(
        self,
        domain_identifier: "capo_datazone.types.domain_id.DomainId",
        identifier: "capo_datazone.types.asset_identifier.AssetIdentifier",
        *,
        config_overrides: Optional[AsyncDataZoneClientConfig] = None,
        revision: Optional["capo_datazone.types.revision.Revision"] = None,
        accept_rule: Optional["capo_datazone.types.accept_rule.AcceptRule"] = None,
        accept_choices: Optional[
            "capo_datazone.types.accept_choices.AcceptChoices"
        ] = None,
        client_token: Optional["capo_datazone.types.client_token.ClientToken"] = None,
    ) -> "capo_datazone.types.accept_predictions_output.AcceptPredictionsOutput":
        """<p>Accepts automatically generated business-friendly metadata for your Amazon DataZone assets.</p>

        Args:
            domain_identifier: <p>The identifier of the Amazon DataZone domain.</p>
            identifier: <p>The identifier of the asset.</p>
            revision: <p>The revision that is to be made to the asset.</p>
            accept_rule: <p>Specifies the rule (or the conditions) under which a prediction can be accepted.</p>
            accept_choices: <p>Specifies the prediction (aka, the automatically generated piece of metadata) and the target (for example, a column name) that can be accepted.</p>
            client_token: <p>A unique, case-sensitive identifier to ensure idempotency of the request. This field is automatically populated if not provided.</p>

        Raises:
            capo_datazone.errors.access_denied_exception.AccessDeniedException: <p>You do not have sufficient access to perform this action.</p>
            capo_datazone.errors.throttling_exception.ThrottlingException: <p>The request was denied due to request throttling.</p>
            capo_datazone.errors.unauthorized_exception.UnauthorizedException: <p>You do not have permission to perform this action.</p>
            capo_datazone.errors.conflict_exception.ConflictException: <p>There is a conflict while performing this action.</p>
            capo_datazone.errors.internal_server_exception.InternalServerException: <p>The request has failed because of an unknown error, exception or failure.</p>
            capo_datazone.errors.resource_not_found_exception.ResourceNotFoundException: <p>The specified resource cannot be found.</p>
            capo_datazone.errors.validation_exception.ValidationException: <p>The input fails to satisfy the constraints specified by the Amazon Web Services service.</p>
            capo_datazone.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        async def _handler(
            req: "AsyncOperationRequest[capo_datazone.types.accept_predictions_input.AcceptPredictionsInput]",
        ) -> AsyncOperationResponse[
            "capo_datazone.types.accept_predictions_output.AcceptPredictionsOutput"
        ]:
            import capo_datazone._operations.data_zone.accept_predictions

            (
                output,
                http_response,
            ) = await capo_datazone._operations.data_zone.accept_predictions.async_accept_predictions(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_datazone.types.accept_predictions_input.AcceptPredictionsInput = {
            "domain_identifier": domain_identifier,
            "identifier": identifier,
        }
        if revision is not None:
            input_["revision"] = revision
        if accept_rule is not None:
            input_["accept_rule"] = accept_rule
        if accept_choices is not None:
            input_["accept_choices"] = accept_choices
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

    async def accept_subscription_request(
        self,
        domain_identifier: "capo_datazone.types.domain_id.DomainId",
        identifier: "capo_datazone.types.subscription_request_id.SubscriptionRequestId",
        *,
        config_overrides: Optional[AsyncDataZoneClientConfig] = None,
        decision_comment: Optional[
            "capo_datazone.types.decision_comment.DecisionComment"
        ] = None,
        asset_scopes: Optional[
            "capo_datazone.types.accepted_asset_scopes.AcceptedAssetScopes"
        ] = None,
        asset_permissions: Optional[
            "capo_datazone.types.asset_permissions.AssetPermissions"
        ] = None,
    ) -> "capo_datazone.types.accept_subscription_request_output.AcceptSubscriptionRequestOutput":
        """<p>Accepts a subscription request to a specific asset. </p>

        Args:
            domain_identifier: <p>The Amazon DataZone domain where the specified subscription request is being accepted.</p>
            identifier: <p>The unique identifier of the subscription request that is to be accepted.</p>
            decision_comment: <p>A description that specifies the reason for accepting the specified subscription request.</p>
            asset_scopes: <p>The asset scopes of the accept subscription request.</p>
            asset_permissions: <p>The asset permissions of the accept subscription request.</p>

        Raises:
            capo_datazone.errors.access_denied_exception.AccessDeniedException: <p>You do not have sufficient access to perform this action.</p>
            capo_datazone.errors.throttling_exception.ThrottlingException: <p>The request was denied due to request throttling.</p>
            capo_datazone.errors.unauthorized_exception.UnauthorizedException: <p>You do not have permission to perform this action.</p>
            capo_datazone.errors.conflict_exception.ConflictException: <p>There is a conflict while performing this action.</p>
            capo_datazone.errors.internal_server_exception.InternalServerException: <p>The request has failed because of an unknown error, exception or failure.</p>
            capo_datazone.errors.resource_not_found_exception.ResourceNotFoundException: <p>The specified resource cannot be found.</p>
            capo_datazone.errors.service_quota_exceeded_exception.ServiceQuotaExceededException: <p>The request has exceeded the specified service quota.</p>
            capo_datazone.errors.validation_exception.ValidationException: <p>The input fails to satisfy the constraints specified by the Amazon Web Services service.</p>
            capo_datazone.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        async def _handler(
            req: "AsyncOperationRequest[capo_datazone.types.accept_subscription_request_input.AcceptSubscriptionRequestInput]",
        ) -> AsyncOperationResponse[
            "capo_datazone.types.accept_subscription_request_output.AcceptSubscriptionRequestOutput"
        ]:
            import capo_datazone._operations.data_zone.accept_subscription_request

            (
                output,
                http_response,
            ) = await capo_datazone._operations.data_zone.accept_subscription_request.async_accept_subscription_request(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_datazone.types.accept_subscription_request_input.AcceptSubscriptionRequestInput = {
            "domain_identifier": domain_identifier,
            "identifier": identifier,
        }
        if decision_comment is not None:
            input_["decision_comment"] = decision_comment
        if asset_scopes is not None:
            input_["asset_scopes"] = asset_scopes
        if asset_permissions is not None:
            input_["asset_permissions"] = asset_permissions

        response = await aexecute_pipeline(
            AsyncOperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        await response.response.aclose()
        return response.output

    async def add_entity_owner(
        self,
        domain_identifier: "capo_datazone.types.domain_id.DomainId",
        entity_type: "capo_datazone.types.data_zone_entity_type.DataZoneEntityType",
        entity_identifier: str,
        owner: "capo_datazone.types.owner_properties.OwnerProperties",
        *,
        config_overrides: Optional[AsyncDataZoneClientConfig] = None,
        client_token: Optional["capo_datazone.types.client_token.ClientToken"] = None,
    ) -> "capo_datazone.types.add_entity_owner_output.AddEntityOwnerOutput":
        """<p>Adds the owner of an entity (a domain unit).</p>

        Args:
            domain_identifier: <p>The ID of the domain in which you want to add the entity owner.</p>
            entity_type: <p>The type of an entity.</p>
            entity_identifier: <p>The ID of the entity to which you want to add an owner.</p>
            owner: <p>The owner that you want to add to the entity.</p>
            client_token: <p>A unique, case-sensitive identifier that is provided to ensure the idempotency of the request.</p>

        Raises:
            capo_datazone.errors.access_denied_exception.AccessDeniedException: <p>You do not have sufficient access to perform this action.</p>
            capo_datazone.errors.throttling_exception.ThrottlingException: <p>The request was denied due to request throttling.</p>
            capo_datazone.errors.unauthorized_exception.UnauthorizedException: <p>You do not have permission to perform this action.</p>
            capo_datazone.errors.conflict_exception.ConflictException: <p>There is a conflict while performing this action.</p>
            capo_datazone.errors.internal_server_exception.InternalServerException: <p>The request has failed because of an unknown error, exception or failure.</p>
            capo_datazone.errors.resource_not_found_exception.ResourceNotFoundException: <p>The specified resource cannot be found.</p>
            capo_datazone.errors.service_quota_exceeded_exception.ServiceQuotaExceededException: <p>The request has exceeded the specified service quota.</p>
            capo_datazone.errors.validation_exception.ValidationException: <p>The input fails to satisfy the constraints specified by the Amazon Web Services service.</p>
            capo_datazone.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        async def _handler(
            req: "AsyncOperationRequest[capo_datazone.types.add_entity_owner_input.AddEntityOwnerInput]",
        ) -> AsyncOperationResponse[
            "capo_datazone.types.add_entity_owner_output.AddEntityOwnerOutput"
        ]:
            import capo_datazone._operations.data_zone.add_entity_owner

            (
                output,
                http_response,
            ) = await capo_datazone._operations.data_zone.add_entity_owner.async_add_entity_owner(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_datazone.types.add_entity_owner_input.AddEntityOwnerInput = {
            "domain_identifier": domain_identifier,
            "entity_type": entity_type,
            "entity_identifier": entity_identifier,
            "owner": owner,
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

    async def add_policy_grant(
        self,
        domain_identifier: "capo_datazone.types.domain_id.DomainId",
        entity_type: "capo_datazone.types.target_entity_type.TargetEntityType",
        entity_identifier: str,
        policy_type: "capo_datazone.types.managed_policy_type.ManagedPolicyType",
        principal: "capo_datazone.types.policy_grant_principal.PolicyGrantPrincipal",
        detail: "capo_datazone.types.policy_grant_detail.PolicyGrantDetail",
        *,
        config_overrides: Optional[AsyncDataZoneClientConfig] = None,
        client_token: Optional["capo_datazone.types.client_token.ClientToken"] = None,
    ) -> "capo_datazone.types.add_policy_grant_output.AddPolicyGrantOutput":
        """<p>Adds a policy grant (an authorization policy) to a specified entity, including domain units, environment blueprint configurations, or environment profiles.</p>

        Args:
            domain_identifier: <p>The ID of the domain where you want to add a policy grant.</p>
            entity_type: <p>The type of entity (resource) to which the grant is added.</p>
            entity_identifier: <p>The ID of the entity (resource) to which you want to add a policy grant.</p>
            policy_type: <p>The type of policy that you want to grant.</p>
            principal: <p>The principal to whom the permissions are granted.</p>
            detail: <p>The details of the policy grant.</p>
            client_token: <p>A unique, case-sensitive identifier that is provided to ensure the idempotency of the request.</p>

        Raises:
            capo_datazone.errors.access_denied_exception.AccessDeniedException: <p>You do not have sufficient access to perform this action.</p>
            capo_datazone.errors.throttling_exception.ThrottlingException: <p>The request was denied due to request throttling.</p>
            capo_datazone.errors.unauthorized_exception.UnauthorizedException: <p>You do not have permission to perform this action.</p>
            capo_datazone.errors.conflict_exception.ConflictException: <p>There is a conflict while performing this action.</p>
            capo_datazone.errors.internal_server_exception.InternalServerException: <p>The request has failed because of an unknown error, exception or failure.</p>
            capo_datazone.errors.service_quota_exceeded_exception.ServiceQuotaExceededException: <p>The request has exceeded the specified service quota.</p>
            capo_datazone.errors.validation_exception.ValidationException: <p>The input fails to satisfy the constraints specified by the Amazon Web Services service.</p>
            capo_datazone.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        async def _handler(
            req: "AsyncOperationRequest[capo_datazone.types.add_policy_grant_input.AddPolicyGrantInput]",
        ) -> AsyncOperationResponse[
            "capo_datazone.types.add_policy_grant_output.AddPolicyGrantOutput"
        ]:
            import capo_datazone._operations.data_zone.add_policy_grant

            (
                output,
                http_response,
            ) = await capo_datazone._operations.data_zone.add_policy_grant.async_add_policy_grant(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_datazone.types.add_policy_grant_input.AddPolicyGrantInput = {
            "domain_identifier": domain_identifier,
            "entity_type": entity_type,
            "entity_identifier": entity_identifier,
            "policy_type": policy_type,
            "principal": principal,
            "detail": detail,
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

    async def associate_environment_role(
        self,
        domain_identifier: "capo_datazone.types.domain_id.DomainId",
        environment_identifier: "capo_datazone.types.environment_id.EnvironmentId",
        environment_role_arn: str,
        *,
        config_overrides: Optional[AsyncDataZoneClientConfig] = None,
    ) -> "capo_datazone.types.associate_environment_role_output.AssociateEnvironmentRoleOutput":
        """<p>Associates the environment role in Amazon DataZone.</p>

        Args:
            domain_identifier: <p>The ID of the Amazon DataZone domain in which the environment role is associated.</p>
            environment_identifier: <p>The ID of the Amazon DataZone environment.</p>
            environment_role_arn: <p>The ARN of the environment role.</p>

        Raises:
            capo_datazone.errors.access_denied_exception.AccessDeniedException: <p>You do not have sufficient access to perform this action.</p>
            capo_datazone.errors.throttling_exception.ThrottlingException: <p>The request was denied due to request throttling.</p>
            capo_datazone.errors.unauthorized_exception.UnauthorizedException: <p>You do not have permission to perform this action.</p>
            capo_datazone.errors.conflict_exception.ConflictException: <p>There is a conflict while performing this action.</p>
            capo_datazone.errors.internal_server_exception.InternalServerException: <p>The request has failed because of an unknown error, exception or failure.</p>
            capo_datazone.errors.resource_not_found_exception.ResourceNotFoundException: <p>The specified resource cannot be found.</p>
            capo_datazone.errors.validation_exception.ValidationException: <p>The input fails to satisfy the constraints specified by the Amazon Web Services service.</p>
            capo_datazone.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        async def _handler(
            req: "AsyncOperationRequest[capo_datazone.types.associate_environment_role_input.AssociateEnvironmentRoleInput]",
        ) -> AsyncOperationResponse[
            "capo_datazone.types.associate_environment_role_output.AssociateEnvironmentRoleOutput"
        ]:
            import capo_datazone._operations.data_zone.associate_environment_role

            (
                output,
                http_response,
            ) = await capo_datazone._operations.data_zone.associate_environment_role.async_associate_environment_role(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_datazone.types.associate_environment_role_input.AssociateEnvironmentRoleInput = {
            "domain_identifier": domain_identifier,
            "environment_identifier": environment_identifier,
            "environment_role_arn": environment_role_arn,
        }

        response = await aexecute_pipeline(
            AsyncOperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        await response.response.aclose()
        return response.output

    async def associate_governed_terms(
        self,
        domain_identifier: "capo_datazone.types.domain_id.DomainId",
        entity_identifier: "capo_datazone.types.entity_identifier.EntityIdentifier",
        entity_type: "capo_datazone.types.governed_entity_type.GovernedEntityType",
        governed_glossary_terms: "capo_datazone.types.governed_glossary_terms.GovernedGlossaryTerms",
        *,
        config_overrides: Optional[AsyncDataZoneClientConfig] = None,
    ) -> "capo_datazone.types.associate_governed_terms_output.AssociateGovernedTermsOutput":
        """<p>Associates governed terms with an asset.</p>

        Args:
            domain_identifier: <p>The ID of the domain where governed terms are to be associated with an asset.</p>
            entity_identifier: <p>The ID of the asset with which you want to associate a governed term.</p>
            entity_type: <p>The type of the asset with which you want to associate a governed term.</p>
            governed_glossary_terms: <p>The glossary terms in a restricted glossary.</p>

        Raises:
            capo_datazone.errors.access_denied_exception.AccessDeniedException: <p>You do not have sufficient access to perform this action.</p>
            capo_datazone.errors.throttling_exception.ThrottlingException: <p>The request was denied due to request throttling.</p>
            capo_datazone.errors.unauthorized_exception.UnauthorizedException: <p>You do not have permission to perform this action.</p>
            capo_datazone.errors.conflict_exception.ConflictException: <p>There is a conflict while performing this action.</p>
            capo_datazone.errors.internal_server_exception.InternalServerException: <p>The request has failed because of an unknown error, exception or failure.</p>
            capo_datazone.errors.resource_not_found_exception.ResourceNotFoundException: <p>The specified resource cannot be found.</p>
            capo_datazone.errors.validation_exception.ValidationException: <p>The input fails to satisfy the constraints specified by the Amazon Web Services service.</p>
            capo_datazone.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        async def _handler(
            req: "AsyncOperationRequest[capo_datazone.types.associate_governed_terms_input.AssociateGovernedTermsInput]",
        ) -> AsyncOperationResponse[
            "capo_datazone.types.associate_governed_terms_output.AssociateGovernedTermsOutput"
        ]:
            import capo_datazone._operations.data_zone.associate_governed_terms

            (
                output,
                http_response,
            ) = await capo_datazone._operations.data_zone.associate_governed_terms.async_associate_governed_terms(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_datazone.types.associate_governed_terms_input.AssociateGovernedTermsInput = {
            "domain_identifier": domain_identifier,
            "entity_identifier": entity_identifier,
            "entity_type": entity_type,
            "governed_glossary_terms": governed_glossary_terms,
        }

        response = await aexecute_pipeline(
            AsyncOperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        await response.response.aclose()
        return response.output

    async def batch_get_attributes_metadata(
        self,
        domain_identifier: "capo_datazone.types.domain_id.DomainId",
        entity_type: "capo_datazone.types.attribute_entity_type.AttributeEntityType",
        entity_identifier: "capo_datazone.types.entity_id.EntityId",
        attribute_identifiers: "capo_datazone.types.attributes_list.AttributesList",
        *,
        config_overrides: Optional[AsyncDataZoneClientConfig] = None,
        entity_revision: Optional["capo_datazone.types.revision.Revision"] = None,
    ) -> "capo_datazone.types.batch_get_attributes_metadata_output.BatchGetAttributesMetadataOutput":
        """<p>Gets the attribute metadata.</p>

        Args:
            domain_identifier: <p>The domain ID where you want to get the attribute metadata.</p>
            entity_type: <p>The entity type for which you want to get attribute metadata.</p>
            entity_identifier: <p>The entity ID for which you want to get attribute metadata.</p>
            entity_revision: <p>The entity revision for which you want to get attribute metadata.</p>
            attribute_identifiers: <p>The attribute identifier.</p>

        Raises:
            capo_datazone.errors.access_denied_exception.AccessDeniedException: <p>You do not have sufficient access to perform this action.</p>
            capo_datazone.errors.throttling_exception.ThrottlingException: <p>The request was denied due to request throttling.</p>
            capo_datazone.errors.unauthorized_exception.UnauthorizedException: <p>You do not have permission to perform this action.</p>
            capo_datazone.errors.internal_server_exception.InternalServerException: <p>The request has failed because of an unknown error, exception or failure.</p>
            capo_datazone.errors.resource_not_found_exception.ResourceNotFoundException: <p>The specified resource cannot be found.</p>
            capo_datazone.errors.validation_exception.ValidationException: <p>The input fails to satisfy the constraints specified by the Amazon Web Services service.</p>
            capo_datazone.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        async def _handler(
            req: "AsyncOperationRequest[capo_datazone.types.batch_get_attributes_metadata_input.BatchGetAttributesMetadataInput]",
        ) -> AsyncOperationResponse[
            "capo_datazone.types.batch_get_attributes_metadata_output.BatchGetAttributesMetadataOutput"
        ]:
            import capo_datazone._operations.data_zone.batch_get_attributes_metadata

            (
                output,
                http_response,
            ) = await capo_datazone._operations.data_zone.batch_get_attributes_metadata.async_batch_get_attributes_metadata(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_datazone.types.batch_get_attributes_metadata_input.BatchGetAttributesMetadataInput = {
            "domain_identifier": domain_identifier,
            "entity_type": entity_type,
            "entity_identifier": entity_identifier,
            "attribute_identifiers": attribute_identifiers,
        }
        if entity_revision is not None:
            input_["entity_revision"] = entity_revision

        response = await aexecute_pipeline(
            AsyncOperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        await response.response.aclose()
        return response.output

    async def batch_put_attributes_metadata(
        self,
        domain_identifier: "capo_datazone.types.domain_id.DomainId",
        entity_type: "capo_datazone.types.attribute_entity_type.AttributeEntityType",
        entity_identifier: "capo_datazone.types.entity_id.EntityId",
        attributes: "capo_datazone.types.attributes.Attributes",
        *,
        config_overrides: Optional[AsyncDataZoneClientConfig] = None,
        client_token: Optional["capo_datazone.types.client_token.ClientToken"] = None,
    ) -> "capo_datazone.types.batch_put_attributes_metadata_output.BatchPutAttributesMetadataOutput":
        """<p>Writes the attribute metadata.</p>

        Args:
            domain_identifier: <p>The domain ID where you want to write the attribute metadata.</p>
            entity_type: <p>The entity type for which you want to write the attribute metadata.</p>
            entity_identifier: <p>The entity ID for which you want to write the attribute metadata.</p>
            client_token: <p>A unique, case-sensitive identifier to ensure idempotency of the request. This field is automatically populated if not provided.</p>
            attributes: <p>The attributes of the metadata.</p>

        Raises:
            capo_datazone.errors.access_denied_exception.AccessDeniedException: <p>You do not have sufficient access to perform this action.</p>
            capo_datazone.errors.throttling_exception.ThrottlingException: <p>The request was denied due to request throttling.</p>
            capo_datazone.errors.unauthorized_exception.UnauthorizedException: <p>You do not have permission to perform this action.</p>
            capo_datazone.errors.conflict_exception.ConflictException: <p>There is a conflict while performing this action.</p>
            capo_datazone.errors.internal_server_exception.InternalServerException: <p>The request has failed because of an unknown error, exception or failure.</p>
            capo_datazone.errors.resource_not_found_exception.ResourceNotFoundException: <p>The specified resource cannot be found.</p>
            capo_datazone.errors.validation_exception.ValidationException: <p>The input fails to satisfy the constraints specified by the Amazon Web Services service.</p>
            capo_datazone.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        async def _handler(
            req: "AsyncOperationRequest[capo_datazone.types.batch_put_attributes_metadata_input.BatchPutAttributesMetadataInput]",
        ) -> AsyncOperationResponse[
            "capo_datazone.types.batch_put_attributes_metadata_output.BatchPutAttributesMetadataOutput"
        ]:
            import capo_datazone._operations.data_zone.batch_put_attributes_metadata

            (
                output,
                http_response,
            ) = await capo_datazone._operations.data_zone.batch_put_attributes_metadata.async_batch_put_attributes_metadata(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_datazone.types.batch_put_attributes_metadata_input.BatchPutAttributesMetadataInput = {
            "domain_identifier": domain_identifier,
            "entity_type": entity_type,
            "entity_identifier": entity_identifier,
            "attributes": attributes,
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

    async def cancel_subscription(
        self,
        domain_identifier: "capo_datazone.types.domain_id.DomainId",
        identifier: "capo_datazone.types.subscription_id.SubscriptionId",
        *,
        config_overrides: Optional[AsyncDataZoneClientConfig] = None,
    ) -> "capo_datazone.types.cancel_subscription_output.CancelSubscriptionOutput":
        """<p>Cancels the subscription to the specified asset.</p>

        Args:
            domain_identifier: <p>The unique identifier of the Amazon DataZone domain where the subscription request is being cancelled.</p>
            identifier: <p>The unique identifier of the subscription that is being cancelled.</p>

        Raises:
            capo_datazone.errors.access_denied_exception.AccessDeniedException: <p>You do not have sufficient access to perform this action.</p>
            capo_datazone.errors.throttling_exception.ThrottlingException: <p>The request was denied due to request throttling.</p>
            capo_datazone.errors.unauthorized_exception.UnauthorizedException: <p>You do not have permission to perform this action.</p>
            capo_datazone.errors.conflict_exception.ConflictException: <p>There is a conflict while performing this action.</p>
            capo_datazone.errors.internal_server_exception.InternalServerException: <p>The request has failed because of an unknown error, exception or failure.</p>
            capo_datazone.errors.resource_not_found_exception.ResourceNotFoundException: <p>The specified resource cannot be found.</p>
            capo_datazone.errors.validation_exception.ValidationException: <p>The input fails to satisfy the constraints specified by the Amazon Web Services service.</p>
            capo_datazone.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        async def _handler(
            req: "AsyncOperationRequest[capo_datazone.types.cancel_subscription_input.CancelSubscriptionInput]",
        ) -> AsyncOperationResponse[
            "capo_datazone.types.cancel_subscription_output.CancelSubscriptionOutput"
        ]:
            import capo_datazone._operations.data_zone.cancel_subscription

            (
                output,
                http_response,
            ) = await capo_datazone._operations.data_zone.cancel_subscription.async_cancel_subscription(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_datazone.types.cancel_subscription_input.CancelSubscriptionInput = {
            "domain_identifier": domain_identifier,
            "identifier": identifier,
        }

        response = await aexecute_pipeline(
            AsyncOperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        await response.response.aclose()
        return response.output

    async def create_account_pool(
        self,
        domain_identifier: "capo_datazone.types.domain_id.DomainId",
        name: "capo_datazone.types.account_pool_name.AccountPoolName",
        resolution_strategy: "capo_datazone.types.resolution_strategy.ResolutionStrategy",
        account_source: "capo_datazone.types.account_source.AccountSource",
        *,
        config_overrides: Optional[AsyncDataZoneClientConfig] = None,
        description: Optional["capo_datazone.types.description.Description"] = None,
    ) -> "capo_datazone.types.create_account_pool_output.CreateAccountPoolOutput":
        """<p>Creates an account pool. </p>

        Args:
            domain_identifier: <p>The ID of the domain where the account pool is created.</p>
            name: <p>The name of the account pool.</p>
            description: <p>The description of the account pool.</p>
            resolution_strategy: <p>The mechanism used to resolve the account selection from the account pool.</p>
            account_source: <p>The source of accounts for the account pool. In the current release, it's either a static list of accounts provided by the customer or a custom Amazon Web Services Lambda handler. </p>

        Raises:
            capo_datazone.errors.access_denied_exception.AccessDeniedException: <p>You do not have sufficient access to perform this action.</p>
            capo_datazone.errors.throttling_exception.ThrottlingException: <p>The request was denied due to request throttling.</p>
            capo_datazone.errors.unauthorized_exception.UnauthorizedException: <p>You do not have permission to perform this action.</p>
            capo_datazone.errors.conflict_exception.ConflictException: <p>There is a conflict while performing this action.</p>
            capo_datazone.errors.internal_server_exception.InternalServerException: <p>The request has failed because of an unknown error, exception or failure.</p>
            capo_datazone.errors.resource_not_found_exception.ResourceNotFoundException: <p>The specified resource cannot be found.</p>
            capo_datazone.errors.service_quota_exceeded_exception.ServiceQuotaExceededException: <p>The request has exceeded the specified service quota.</p>
            capo_datazone.errors.validation_exception.ValidationException: <p>The input fails to satisfy the constraints specified by the Amazon Web Services service.</p>
            capo_datazone.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        async def _handler(
            req: "AsyncOperationRequest[capo_datazone.types.create_account_pool_input.CreateAccountPoolInput]",
        ) -> AsyncOperationResponse[
            "capo_datazone.types.create_account_pool_output.CreateAccountPoolOutput"
        ]:
            import capo_datazone._operations.data_zone.create_account_pool

            (
                output,
                http_response,
            ) = await capo_datazone._operations.data_zone.create_account_pool.async_create_account_pool(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_datazone.types.create_account_pool_input.CreateAccountPoolInput = {
            "domain_identifier": domain_identifier,
            "name": name,
            "resolution_strategy": resolution_strategy,
            "account_source": account_source,
        }
        if description is not None:
            input_["description"] = description

        response = await aexecute_pipeline(
            AsyncOperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        await response.response.aclose()
        return response.output

    async def create_asset_filter(
        self,
        domain_identifier: "capo_datazone.types.domain_id.DomainId",
        asset_identifier: "capo_datazone.types.asset_id.AssetId",
        name: "capo_datazone.types.filter_name.FilterName",
        configuration: "capo_datazone.types.asset_filter_configuration.AssetFilterConfiguration",
        *,
        config_overrides: Optional[AsyncDataZoneClientConfig] = None,
        description: Optional["capo_datazone.types.description.Description"] = None,
        client_token: Optional[str] = None,
    ) -> "capo_datazone.types.create_asset_filter_output.CreateAssetFilterOutput":
        """<p>Creates a data asset filter.</p> <p>Asset filters provide a sophisticated way to create controlled views of data assets by selecting specific columns or applying row-level filters. This capability is crucial for organizations that need to share data while maintaining security and privacy controls. For example, your database might be filtered to show only non-PII fields to certain users, or sales data might be filtered by region for different regional teams. Asset filters enable fine-grained access control while maintaining a single source of truth.</p> <p>Prerequisites:</p> <ul> <li> <p>A valid domain (<code>--domain-identifier</code>) must exist. </p> </li> <li> <p>A data asset (<code>--asset-identifier</code>) must already be created under that domain.</p> </li> <li> <p>The asset must have the referenced columns available in its schema for column-based filtering.</p> </li> <li> <p>You cannot specify both (<code>columnConfiguration</code>, <code>rowConfiguration</code>)at the same time.</p> </li> </ul>

        Args:
            domain_identifier: <p>The ID of the domain in which you want to create an asset filter.</p>
            asset_identifier: <p>The ID of the data asset.</p>
            name: <p>The name of the asset filter.</p>
            description: <p>The description of the asset filter.</p>
            configuration: <p>The configuration of the asset filter.</p>
            client_token: <p>A unique, case-sensitive identifier that is provided to ensure the idempotency of the request.</p>

        Raises:
            capo_datazone.errors.access_denied_exception.AccessDeniedException: <p>You do not have sufficient access to perform this action.</p>
            capo_datazone.errors.throttling_exception.ThrottlingException: <p>The request was denied due to request throttling.</p>
            capo_datazone.errors.unauthorized_exception.UnauthorizedException: <p>You do not have permission to perform this action.</p>
            capo_datazone.errors.conflict_exception.ConflictException: <p>There is a conflict while performing this action.</p>
            capo_datazone.errors.internal_server_exception.InternalServerException: <p>The request has failed because of an unknown error, exception or failure.</p>
            capo_datazone.errors.resource_not_found_exception.ResourceNotFoundException: <p>The specified resource cannot be found.</p>
            capo_datazone.errors.service_quota_exceeded_exception.ServiceQuotaExceededException: <p>The request has exceeded the specified service quota.</p>
            capo_datazone.errors.validation_exception.ValidationException: <p>The input fails to satisfy the constraints specified by the Amazon Web Services service.</p>
            capo_datazone.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        async def _handler(
            req: "AsyncOperationRequest[capo_datazone.types.create_asset_filter_input.CreateAssetFilterInput]",
        ) -> AsyncOperationResponse[
            "capo_datazone.types.create_asset_filter_output.CreateAssetFilterOutput"
        ]:
            import capo_datazone._operations.data_zone.create_asset_filter

            (
                output,
                http_response,
            ) = await capo_datazone._operations.data_zone.create_asset_filter.async_create_asset_filter(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_datazone.types.create_asset_filter_input.CreateAssetFilterInput = {
            "domain_identifier": domain_identifier,
            "asset_identifier": asset_identifier,
            "name": name,
            "configuration": configuration,
        }
        if description is not None:
            input_["description"] = description
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

    async def create_connection(
        self,
        domain_identifier: "capo_datazone.types.domain_id.DomainId",
        name: "capo_datazone.types.connection_name.ConnectionName",
        *,
        config_overrides: Optional[AsyncDataZoneClientConfig] = None,
        aws_location: Optional["capo_datazone.types.aws_location.AwsLocation"] = None,
        client_token: Optional[str] = None,
        configurations: Optional[
            "capo_datazone.types.configurations.Configurations"
        ] = None,
        description: Optional["capo_datazone.types.description.Description"] = None,
        environment_identifier: Optional[
            "capo_datazone.types.environment_id.EnvironmentId"
        ] = None,
        props: Optional[
            "capo_datazone.types.connection_properties_input.ConnectionPropertiesInput"
        ] = None,
        enable_trusted_identity_propagation: Optional[bool] = None,
        scope: Optional["capo_datazone.types.connection_scope.ConnectionScope"] = None,
    ) -> "capo_datazone.types.create_connection_output.CreateConnectionOutput":
        """<p>Creates a new connection. In Amazon DataZone, a connection enables you to connect your resources (domains, projects, and environments) to external resources and services.</p>

        Args:
            aws_location: <p>The location where the connection is created.</p>
            client_token: <p>A unique, case-sensitive identifier that is provided to ensure the idempotency of the request.</p>
            configurations: <p>The configurations of the connection.</p>
            description: <p>A connection description.</p>
            domain_identifier: <p>The ID of the domain where the connection is created.</p>
            environment_identifier: <p>The ID of the environment where the connection is created.</p>
            name: <p>The connection name.</p>
            props: <p>The connection props.</p>
            enable_trusted_identity_propagation: <p>Specifies whether the trusted identity propagation is enabled.</p>
            scope: <p>The scope of the connection.</p>

        Raises:
            capo_datazone.errors.access_denied_exception.AccessDeniedException: <p>You do not have sufficient access to perform this action.</p>
            capo_datazone.errors.throttling_exception.ThrottlingException: <p>The request was denied due to request throttling.</p>
            capo_datazone.errors.unauthorized_exception.UnauthorizedException: <p>You do not have permission to perform this action.</p>
            capo_datazone.errors.conflict_exception.ConflictException: <p>There is a conflict while performing this action.</p>
            capo_datazone.errors.internal_server_exception.InternalServerException: <p>The request has failed because of an unknown error, exception or failure.</p>
            capo_datazone.errors.resource_not_found_exception.ResourceNotFoundException: <p>The specified resource cannot be found.</p>
            capo_datazone.errors.service_quota_exceeded_exception.ServiceQuotaExceededException: <p>The request has exceeded the specified service quota.</p>
            capo_datazone.errors.validation_exception.ValidationException: <p>The input fails to satisfy the constraints specified by the Amazon Web Services service.</p>
            capo_datazone.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        async def _handler(
            req: "AsyncOperationRequest[capo_datazone.types.create_connection_input.CreateConnectionInput]",
        ) -> AsyncOperationResponse[
            "capo_datazone.types.create_connection_output.CreateConnectionOutput"
        ]:
            import capo_datazone._operations.data_zone.create_connection

            (
                output,
                http_response,
            ) = await capo_datazone._operations.data_zone.create_connection.async_create_connection(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_datazone.types.create_connection_input.CreateConnectionInput = {
            "domain_identifier": domain_identifier,
            "name": name,
        }
        if aws_location is not None:
            input_["aws_location"] = aws_location
        if client_token is None:
            client_token = str(uuid.uuid4())
        input_["client_token"] = client_token
        if configurations is not None:
            input_["configurations"] = configurations
        if description is not None:
            input_["description"] = description
        if environment_identifier is not None:
            input_["environment_identifier"] = environment_identifier
        if props is not None:
            input_["props"] = props
        if enable_trusted_identity_propagation is not None:
            input_["enable_trusted_identity_propagation"] = (
                enable_trusted_identity_propagation
            )
        if scope is not None:
            input_["scope"] = scope

        response = await aexecute_pipeline(
            AsyncOperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        await response.response.aclose()
        return response.output

    async def create_environment(
        self,
        project_identifier: "capo_datazone.types.project_id.ProjectId",
        domain_identifier: "capo_datazone.types.domain_id.DomainId",
        name: str,
        *,
        config_overrides: Optional[AsyncDataZoneClientConfig] = None,
        description: Optional[str] = None,
        environment_profile_identifier: Optional[
            "capo_datazone.types.environment_profile_id.EnvironmentProfileId"
        ] = None,
        user_parameters: Optional[
            "capo_datazone.types.environment_parameters_list.EnvironmentParametersList"
        ] = None,
        glossary_terms: Optional[
            "capo_datazone.types.glossary_terms.GlossaryTerms"
        ] = None,
        environment_account_identifier: Optional[str] = None,
        environment_account_region: Optional[str] = None,
        environment_blueprint_identifier: Optional[str] = None,
        deployment_order: Optional[int] = None,
        environment_configuration_id: Optional[str] = None,
        environment_configuration_name: Optional[
            "capo_datazone.types.environment_configuration_name.EnvironmentConfigurationName"
        ] = None,
    ) -> "capo_datazone.types.create_environment_output.CreateEnvironmentOutput":
        """<p>Create an Amazon DataZone environment.</p>

        Args:
            project_identifier: <p>The identifier of the Amazon DataZone project in which this environment is created.</p>
            domain_identifier: <p>The identifier of the Amazon DataZone domain in which the environment is created.</p>
            description: <p>The description of the Amazon DataZone environment.</p>
            name: <p>The name of the Amazon DataZone environment.</p>
            environment_profile_identifier: <p>The identifier of the environment profile that is used to create this Amazon DataZone environment.</p>
            user_parameters: <p>The user parameters of this Amazon DataZone environment.</p>
            glossary_terms: <p>The glossary terms that can be used in this Amazon DataZone environment.</p>
            environment_account_identifier: <p>The ID of the account in which the environment is being created.</p>
            environment_account_region: <p>The region of the account in which the environment is being created.</p>
            environment_blueprint_identifier: <p>The ID of the blueprint with which the environment is being created.</p> <note> <p>This parameter is only valid for V1 domains. If provided for a V2 domain, the service returns a ValidationException.</p> </note>
            deployment_order: <p>The deployment order of the environment.</p>
            environment_configuration_id: <p>The configuration ID of the environment.</p>
            environment_configuration_name: <p>The configuration name of the environment.</p>

        Raises:
            capo_datazone.errors.access_denied_exception.AccessDeniedException: <p>You do not have sufficient access to perform this action.</p>
            capo_datazone.errors.throttling_exception.ThrottlingException: <p>The request was denied due to request throttling.</p>
            capo_datazone.errors.unauthorized_exception.UnauthorizedException: <p>You do not have permission to perform this action.</p>
            capo_datazone.errors.conflict_exception.ConflictException: <p>There is a conflict while performing this action.</p>
            capo_datazone.errors.internal_server_exception.InternalServerException: <p>The request has failed because of an unknown error, exception or failure.</p>
            capo_datazone.errors.resource_not_found_exception.ResourceNotFoundException: <p>The specified resource cannot be found.</p>
            capo_datazone.errors.validation_exception.ValidationException: <p>The input fails to satisfy the constraints specified by the Amazon Web Services service.</p>
            capo_datazone.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        async def _handler(
            req: "AsyncOperationRequest[capo_datazone.types.create_environment_input.CreateEnvironmentInput]",
        ) -> AsyncOperationResponse[
            "capo_datazone.types.create_environment_output.CreateEnvironmentOutput"
        ]:
            import capo_datazone._operations.data_zone.create_environment

            (
                output,
                http_response,
            ) = await capo_datazone._operations.data_zone.create_environment.async_create_environment(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_datazone.types.create_environment_input.CreateEnvironmentInput = {
            "project_identifier": project_identifier,
            "domain_identifier": domain_identifier,
            "name": name,
        }
        if description is not None:
            input_["description"] = description
        if environment_profile_identifier is not None:
            input_["environment_profile_identifier"] = environment_profile_identifier
        if user_parameters is not None:
            input_["user_parameters"] = user_parameters
        if glossary_terms is not None:
            input_["glossary_terms"] = glossary_terms
        if environment_account_identifier is not None:
            input_["environment_account_identifier"] = environment_account_identifier
        if environment_account_region is not None:
            input_["environment_account_region"] = environment_account_region
        if environment_blueprint_identifier is not None:
            input_["environment_blueprint_identifier"] = (
                environment_blueprint_identifier
            )
        if deployment_order is not None:
            input_["deployment_order"] = deployment_order
        if environment_configuration_id is not None:
            input_["environment_configuration_id"] = environment_configuration_id
        if environment_configuration_name is not None:
            input_["environment_configuration_name"] = environment_configuration_name

        response = await aexecute_pipeline(
            AsyncOperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        await response.response.aclose()
        return response.output

    async def create_environment_action(
        self,
        domain_identifier: "capo_datazone.types.domain_id.DomainId",
        environment_identifier: "capo_datazone.types.environment_id.EnvironmentId",
        name: str,
        parameters: "capo_datazone.types.action_parameters.ActionParameters",
        *,
        config_overrides: Optional[AsyncDataZoneClientConfig] = None,
        description: Optional[str] = None,
    ) -> "capo_datazone.types.create_environment_action_output.CreateEnvironmentActionOutput":
        """<p>Creates an action for the environment, for example, creates a console link for an analytics tool that is available in this environment.</p>

        Args:
            domain_identifier: <p>The ID of the Amazon DataZone domain in which the environment action is created.</p>
            environment_identifier: <p>The ID of the environment in which the environment action is created.</p>
            name: <p>The name of the environment action.</p>
            parameters: <p>The parameters of the environment action.</p>
            description: <p>The description of the environment action that is being created in the environment.</p>

        Raises:
            capo_datazone.errors.access_denied_exception.AccessDeniedException: <p>You do not have sufficient access to perform this action.</p>
            capo_datazone.errors.throttling_exception.ThrottlingException: <p>The request was denied due to request throttling.</p>
            capo_datazone.errors.unauthorized_exception.UnauthorizedException: <p>You do not have permission to perform this action.</p>
            capo_datazone.errors.conflict_exception.ConflictException: <p>There is a conflict while performing this action.</p>
            capo_datazone.errors.internal_server_exception.InternalServerException: <p>The request has failed because of an unknown error, exception or failure.</p>
            capo_datazone.errors.resource_not_found_exception.ResourceNotFoundException: <p>The specified resource cannot be found.</p>
            capo_datazone.errors.validation_exception.ValidationException: <p>The input fails to satisfy the constraints specified by the Amazon Web Services service.</p>
            capo_datazone.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        async def _handler(
            req: "AsyncOperationRequest[capo_datazone.types.create_environment_action_input.CreateEnvironmentActionInput]",
        ) -> AsyncOperationResponse[
            "capo_datazone.types.create_environment_action_output.CreateEnvironmentActionOutput"
        ]:
            import capo_datazone._operations.data_zone.create_environment_action

            (
                output,
                http_response,
            ) = await capo_datazone._operations.data_zone.create_environment_action.async_create_environment_action(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_datazone.types.create_environment_action_input.CreateEnvironmentActionInput = {
            "domain_identifier": domain_identifier,
            "environment_identifier": environment_identifier,
            "name": name,
            "parameters": parameters,
        }
        if description is not None:
            input_["description"] = description

        response = await aexecute_pipeline(
            AsyncOperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        await response.response.aclose()
        return response.output

    async def create_environment_blueprint(
        self,
        domain_identifier: "capo_datazone.types.domain_id.DomainId",
        name: "capo_datazone.types.environment_blueprint_name.EnvironmentBlueprintName",
        provisioning_properties: "capo_datazone.types.provisioning_properties.ProvisioningProperties",
        *,
        config_overrides: Optional[AsyncDataZoneClientConfig] = None,
        description: Optional["capo_datazone.types.description.Description"] = None,
        user_parameters: Optional[
            "capo_datazone.types.custom_parameter_list.CustomParameterList"
        ] = None,
        blueprint_category: Optional[
            "capo_datazone.types.blueprint_category.BlueprintCategory"
        ] = None,
    ) -> "capo_datazone.types.create_environment_blueprint_output.CreateEnvironmentBlueprintOutput":
        """<p>Creates a Amazon DataZone blueprint.</p>

        Args:
            domain_identifier: <p>The identifier of the domain in which this blueprint is created.</p>
            name: <p>The name of this Amazon DataZone blueprint.</p>
            description: <p>The description of the Amazon DataZone blueprint.</p>
            provisioning_properties: <p>The provisioning properties of this Amazon DataZone blueprint.</p>
            user_parameters: <p>The user parameters of this Amazon DataZone blueprint.</p>
            blueprint_category: <p>The category of the Amazon DataZone blueprint. The only valid value is <code>TOOLING</code>, which creates a blueprint that provisions the tooling resources of a project.</p>

        Raises:
            capo_datazone.errors.access_denied_exception.AccessDeniedException: <p>You do not have sufficient access to perform this action.</p>
            capo_datazone.errors.throttling_exception.ThrottlingException: <p>The request was denied due to request throttling.</p>
            capo_datazone.errors.unauthorized_exception.UnauthorizedException: <p>You do not have permission to perform this action.</p>
            capo_datazone.errors.conflict_exception.ConflictException: <p>There is a conflict while performing this action.</p>
            capo_datazone.errors.internal_server_exception.InternalServerException: <p>The request has failed because of an unknown error, exception or failure.</p>
            capo_datazone.errors.resource_not_found_exception.ResourceNotFoundException: <p>The specified resource cannot be found.</p>
            capo_datazone.errors.service_quota_exceeded_exception.ServiceQuotaExceededException: <p>The request has exceeded the specified service quota.</p>
            capo_datazone.errors.validation_exception.ValidationException: <p>The input fails to satisfy the constraints specified by the Amazon Web Services service.</p>
            capo_datazone.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        async def _handler(
            req: "AsyncOperationRequest[capo_datazone.types.create_environment_blueprint_input.CreateEnvironmentBlueprintInput]",
        ) -> AsyncOperationResponse[
            "capo_datazone.types.create_environment_blueprint_output.CreateEnvironmentBlueprintOutput"
        ]:
            import capo_datazone._operations.data_zone.create_environment_blueprint

            (
                output,
                http_response,
            ) = await capo_datazone._operations.data_zone.create_environment_blueprint.async_create_environment_blueprint(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_datazone.types.create_environment_blueprint_input.CreateEnvironmentBlueprintInput = {
            "domain_identifier": domain_identifier,
            "name": name,
            "provisioning_properties": provisioning_properties,
        }
        if description is not None:
            input_["description"] = description
        if user_parameters is not None:
            input_["user_parameters"] = user_parameters
        if blueprint_category is not None:
            input_["blueprint_category"] = blueprint_category

        response = await aexecute_pipeline(
            AsyncOperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        await response.response.aclose()
        return response.output

    async def create_environment_profile(
        self,
        domain_identifier: "capo_datazone.types.domain_id.DomainId",
        name: "capo_datazone.types.environment_profile_name.EnvironmentProfileName",
        environment_blueprint_identifier: "capo_datazone.types.environment_blueprint_id.EnvironmentBlueprintId",
        project_identifier: "capo_datazone.types.project_id.ProjectId",
        *,
        config_overrides: Optional[AsyncDataZoneClientConfig] = None,
        description: Optional["capo_datazone.types.description.Description"] = None,
        user_parameters: Optional[
            "capo_datazone.types.environment_parameters_list.EnvironmentParametersList"
        ] = None,
        aws_account_id: Optional[
            "capo_datazone.types.aws_account_id.AwsAccountId"
        ] = None,
        aws_account_region: Optional["capo_datazone.types.aws_region.AwsRegion"] = None,
    ) -> "capo_datazone.types.create_environment_profile_output.CreateEnvironmentProfileOutput":
        """<p>Creates an Amazon DataZone environment profile.</p>

        Args:
            domain_identifier: <p>The ID of the Amazon DataZone domain in which this environment profile is created.</p>
            name: <p>The name of this Amazon DataZone environment profile.</p>
            description: <p>The description of this Amazon DataZone environment profile.</p>
            environment_blueprint_identifier: <p>The ID of the blueprint with which this environment profile is created.</p>
            project_identifier: <p>The identifier of the project in which to create the environment profile.</p>
            user_parameters: <p>The user parameters of this Amazon DataZone environment profile.</p>
            aws_account_id: <p>The Amazon Web Services account in which the Amazon DataZone environment is created.</p>
            aws_account_region: <p>The Amazon Web Services region in which this environment profile is created.</p>

        Raises:
            capo_datazone.errors.access_denied_exception.AccessDeniedException: <p>You do not have sufficient access to perform this action.</p>
            capo_datazone.errors.throttling_exception.ThrottlingException: <p>The request was denied due to request throttling.</p>
            capo_datazone.errors.unauthorized_exception.UnauthorizedException: <p>You do not have permission to perform this action.</p>
            capo_datazone.errors.conflict_exception.ConflictException: <p>There is a conflict while performing this action.</p>
            capo_datazone.errors.internal_server_exception.InternalServerException: <p>The request has failed because of an unknown error, exception or failure.</p>
            capo_datazone.errors.resource_not_found_exception.ResourceNotFoundException: <p>The specified resource cannot be found.</p>
            capo_datazone.errors.service_quota_exceeded_exception.ServiceQuotaExceededException: <p>The request has exceeded the specified service quota.</p>
            capo_datazone.errors.validation_exception.ValidationException: <p>The input fails to satisfy the constraints specified by the Amazon Web Services service.</p>
            capo_datazone.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        async def _handler(
            req: "AsyncOperationRequest[capo_datazone.types.create_environment_profile_input.CreateEnvironmentProfileInput]",
        ) -> AsyncOperationResponse[
            "capo_datazone.types.create_environment_profile_output.CreateEnvironmentProfileOutput"
        ]:
            import capo_datazone._operations.data_zone.create_environment_profile

            (
                output,
                http_response,
            ) = await capo_datazone._operations.data_zone.create_environment_profile.async_create_environment_profile(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_datazone.types.create_environment_profile_input.CreateEnvironmentProfileInput = {
            "domain_identifier": domain_identifier,
            "name": name,
            "environment_blueprint_identifier": environment_blueprint_identifier,
            "project_identifier": project_identifier,
        }
        if description is not None:
            input_["description"] = description
        if user_parameters is not None:
            input_["user_parameters"] = user_parameters
        if aws_account_id is not None:
            input_["aws_account_id"] = aws_account_id
        if aws_account_region is not None:
            input_["aws_account_region"] = aws_account_region

        response = await aexecute_pipeline(
            AsyncOperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        await response.response.aclose()
        return response.output

    async def create_group_profile(
        self,
        domain_identifier: "capo_datazone.types.domain_id.DomainId",
        *,
        config_overrides: Optional[AsyncDataZoneClientConfig] = None,
        group_identifier: Optional[
            "capo_datazone.types.group_identifier.GroupIdentifier"
        ] = None,
        role_principal_arn: Optional[str] = None,
        client_token: Optional[str] = None,
    ) -> "capo_datazone.types.create_group_profile_output.CreateGroupProfileOutput":
        """<p>Creates a group profile in Amazon DataZone.</p>

        Args:
            domain_identifier: <p>The identifier of the Amazon DataZone domain in which the group profile is created.</p>
            group_identifier: <p>The identifier of the group for which the group profile is created.</p>
            role_principal_arn: <p>The ARN of the IAM role that will be associated with the group profile. This role defines the permissions that group members will assume when accessing Amazon DataZone resources.</p>
            client_token: <p> A unique, case-sensitive identifier that is provided to ensure the idempotency of the request.</p>

        Raises:
            capo_datazone.errors.access_denied_exception.AccessDeniedException: <p>You do not have sufficient access to perform this action.</p>
            capo_datazone.errors.throttling_exception.ThrottlingException: <p>The request was denied due to request throttling.</p>
            capo_datazone.errors.unauthorized_exception.UnauthorizedException: <p>You do not have permission to perform this action.</p>
            capo_datazone.errors.internal_server_exception.InternalServerException: <p>The request has failed because of an unknown error, exception or failure.</p>
            capo_datazone.errors.resource_not_found_exception.ResourceNotFoundException: <p>The specified resource cannot be found.</p>
            capo_datazone.errors.validation_exception.ValidationException: <p>The input fails to satisfy the constraints specified by the Amazon Web Services service.</p>
            capo_datazone.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        async def _handler(
            req: "AsyncOperationRequest[capo_datazone.types.create_group_profile_input.CreateGroupProfileInput]",
        ) -> AsyncOperationResponse[
            "capo_datazone.types.create_group_profile_output.CreateGroupProfileOutput"
        ]:
            import capo_datazone._operations.data_zone.create_group_profile

            (
                output,
                http_response,
            ) = await capo_datazone._operations.data_zone.create_group_profile.async_create_group_profile(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_datazone.types.create_group_profile_input.CreateGroupProfileInput = {
            "domain_identifier": domain_identifier
        }
        if group_identifier is not None:
            input_["group_identifier"] = group_identifier
        if role_principal_arn is not None:
            input_["role_principal_arn"] = role_principal_arn
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

    async def create_listing_change_set(
        self,
        domain_identifier: "capo_datazone.types.domain_id.DomainId",
        entity_identifier: "capo_datazone.types.entity_identifier.EntityIdentifier",
        entity_type: "capo_datazone.types.entity_type.EntityType",
        action: "capo_datazone.types.change_action.ChangeAction",
        *,
        config_overrides: Optional[AsyncDataZoneClientConfig] = None,
        entity_revision: Optional["capo_datazone.types.revision.Revision"] = None,
        client_token: Optional["capo_datazone.types.client_token.ClientToken"] = None,
    ) -> "capo_datazone.types.create_listing_change_set_output.CreateListingChangeSetOutput":
        """<p>Publishes a listing (a record of an asset at a given time) or removes a listing from the catalog. </p>

        Args:
            domain_identifier: <p>The ID of the Amazon DataZone domain.</p>
            entity_identifier: <p>The ID of the asset.</p>
            entity_type: <p>The type of an entity.</p>
            entity_revision: <p>The revision of an asset.</p>
            action: <p>Specifies whether to publish or unpublish a listing.</p>
            client_token: <p>A unique, case-sensitive identifier that is provided to ensure the idempotency of the request.</p>

        Raises:
            capo_datazone.errors.access_denied_exception.AccessDeniedException: <p>You do not have sufficient access to perform this action.</p>
            capo_datazone.errors.throttling_exception.ThrottlingException: <p>The request was denied due to request throttling.</p>
            capo_datazone.errors.unauthorized_exception.UnauthorizedException: <p>You do not have permission to perform this action.</p>
            capo_datazone.errors.conflict_exception.ConflictException: <p>There is a conflict while performing this action.</p>
            capo_datazone.errors.internal_server_exception.InternalServerException: <p>The request has failed because of an unknown error, exception or failure.</p>
            capo_datazone.errors.resource_not_found_exception.ResourceNotFoundException: <p>The specified resource cannot be found.</p>
            capo_datazone.errors.service_quota_exceeded_exception.ServiceQuotaExceededException: <p>The request has exceeded the specified service quota.</p>
            capo_datazone.errors.validation_exception.ValidationException: <p>The input fails to satisfy the constraints specified by the Amazon Web Services service.</p>
            capo_datazone.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        async def _handler(
            req: "AsyncOperationRequest[capo_datazone.types.create_listing_change_set_input.CreateListingChangeSetInput]",
        ) -> AsyncOperationResponse[
            "capo_datazone.types.create_listing_change_set_output.CreateListingChangeSetOutput"
        ]:
            import capo_datazone._operations.data_zone.create_listing_change_set

            (
                output,
                http_response,
            ) = await capo_datazone._operations.data_zone.create_listing_change_set.async_create_listing_change_set(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_datazone.types.create_listing_change_set_input.CreateListingChangeSetInput = {
            "domain_identifier": domain_identifier,
            "entity_identifier": entity_identifier,
            "entity_type": entity_type,
            "action": action,
        }
        if entity_revision is not None:
            input_["entity_revision"] = entity_revision
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

    async def create_project(
        self,
        domain_identifier: "capo_datazone.types.domain_id.DomainId",
        name: "capo_datazone.types.project_name.ProjectName",
        *,
        config_overrides: Optional[AsyncDataZoneClientConfig] = None,
        description: Optional["capo_datazone.types.description.Description"] = None,
        resource_tags: Optional["capo_datazone.types.tags.Tags"] = None,
        glossary_terms: Optional[
            "capo_datazone.types.glossary_terms.GlossaryTerms"
        ] = None,
        domain_unit_id: Optional[
            "capo_datazone.types.domain_unit_id.DomainUnitId"
        ] = None,
        project_profile_id: Optional[
            "capo_datazone.types.project_profile_id.ProjectProfileId"
        ] = None,
        user_parameters: Optional[
            "capo_datazone.types.environment_configuration_user_parameters_list.EnvironmentConfigurationUserParametersList"
        ] = None,
        project_category: Optional[str] = None,
        project_execution_role: Optional["capo_datazone.types.role_arn.RoleArn"] = None,
        membership_assignments: Optional[
            "capo_datazone.types.project_membership_assignments.ProjectMembershipAssignments"
        ] = None,
    ) -> "capo_datazone.types.create_project_output.CreateProjectOutput":
        """<p>Creates an Amazon DataZone project.</p>

        Args:
            domain_identifier: <p>The ID of the Amazon DataZone domain in which this project is created.</p>
            name: <p>The name of the Amazon DataZone project.</p>
            description: <p>The description of the Amazon DataZone project.</p>
            resource_tags: <p>The resource tags of the project.</p>
            glossary_terms: <p>The glossary terms that can be used in this Amazon DataZone project.</p>
            domain_unit_id: <p>The ID of the domain unit. This parameter is not required and if it is not specified, then the project is created at the root domain unit level.</p>
            project_profile_id: <p>The ID of the project profile.</p>
            user_parameters: <p>The user parameters of the project.</p>
            project_category: <p>The category of the project. Set to 'ADMIN' designates this as an administrative project for the Amazon DataZone domain.</p>
            project_execution_role: <p>The default project IAM role that is used to access project resources and run computes such as Glue and Sagemaker.</p>
            membership_assignments: <p>The members to be assigned to the project.</p>

        Raises:
            capo_datazone.errors.access_denied_exception.AccessDeniedException: <p>You do not have sufficient access to perform this action.</p>
            capo_datazone.errors.throttling_exception.ThrottlingException: <p>The request was denied due to request throttling.</p>
            capo_datazone.errors.unauthorized_exception.UnauthorizedException: <p>You do not have permission to perform this action.</p>
            capo_datazone.errors.conflict_exception.ConflictException: <p>There is a conflict while performing this action.</p>
            capo_datazone.errors.internal_server_exception.InternalServerException: <p>The request has failed because of an unknown error, exception or failure.</p>
            capo_datazone.errors.resource_not_found_exception.ResourceNotFoundException: <p>The specified resource cannot be found.</p>
            capo_datazone.errors.service_quota_exceeded_exception.ServiceQuotaExceededException: <p>The request has exceeded the specified service quota.</p>
            capo_datazone.errors.validation_exception.ValidationException: <p>The input fails to satisfy the constraints specified by the Amazon Web Services service.</p>
            capo_datazone.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        async def _handler(
            req: "AsyncOperationRequest[capo_datazone.types.create_project_input.CreateProjectInput]",
        ) -> AsyncOperationResponse[
            "capo_datazone.types.create_project_output.CreateProjectOutput"
        ]:
            import capo_datazone._operations.data_zone.create_project

            (
                output,
                http_response,
            ) = await capo_datazone._operations.data_zone.create_project.async_create_project(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_datazone.types.create_project_input.CreateProjectInput = {
            "domain_identifier": domain_identifier,
            "name": name,
        }
        if description is not None:
            input_["description"] = description
        if resource_tags is not None:
            input_["resource_tags"] = resource_tags
        if glossary_terms is not None:
            input_["glossary_terms"] = glossary_terms
        if domain_unit_id is not None:
            input_["domain_unit_id"] = domain_unit_id
        if project_profile_id is not None:
            input_["project_profile_id"] = project_profile_id
        if user_parameters is not None:
            input_["user_parameters"] = user_parameters
        if project_category is not None:
            input_["project_category"] = project_category
        if project_execution_role is not None:
            input_["project_execution_role"] = project_execution_role
        if membership_assignments is not None:
            input_["membership_assignments"] = membership_assignments

        response = await aexecute_pipeline(
            AsyncOperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        await response.response.aclose()
        return response.output

    async def create_project_membership(
        self,
        domain_identifier: "capo_datazone.types.domain_id.DomainId",
        project_identifier: "capo_datazone.types.project_id.ProjectId",
        member: "capo_datazone.types.member.Member",
        designation: "capo_datazone.types.user_designation.UserDesignation",
        *,
        config_overrides: Optional[AsyncDataZoneClientConfig] = None,
    ) -> "capo_datazone.types.create_project_membership_output.CreateProjectMembershipOutput":
        """<p>Creates a project membership in Amazon DataZone.</p>

        Args:
            domain_identifier: <p>The ID of the Amazon DataZone domain in which project membership is created.</p>
            project_identifier: <p>The ID of the project for which this project membership was created.</p>
            member: <p>The project member whose project membership was created.</p>
            designation: <p>The designation of the project membership.</p>

        Raises:
            capo_datazone.errors.access_denied_exception.AccessDeniedException: <p>You do not have sufficient access to perform this action.</p>
            capo_datazone.errors.throttling_exception.ThrottlingException: <p>The request was denied due to request throttling.</p>
            capo_datazone.errors.unauthorized_exception.UnauthorizedException: <p>You do not have permission to perform this action.</p>
            capo_datazone.errors.internal_server_exception.InternalServerException: <p>The request has failed because of an unknown error, exception or failure.</p>
            capo_datazone.errors.resource_not_found_exception.ResourceNotFoundException: <p>The specified resource cannot be found.</p>
            capo_datazone.errors.validation_exception.ValidationException: <p>The input fails to satisfy the constraints specified by the Amazon Web Services service.</p>
            capo_datazone.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        async def _handler(
            req: "AsyncOperationRequest[capo_datazone.types.create_project_membership_input.CreateProjectMembershipInput]",
        ) -> AsyncOperationResponse[
            "capo_datazone.types.create_project_membership_output.CreateProjectMembershipOutput"
        ]:
            import capo_datazone._operations.data_zone.create_project_membership

            (
                output,
                http_response,
            ) = await capo_datazone._operations.data_zone.create_project_membership.async_create_project_membership(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_datazone.types.create_project_membership_input.CreateProjectMembershipInput = {
            "domain_identifier": domain_identifier,
            "project_identifier": project_identifier,
            "member": member,
            "designation": designation,
        }

        response = await aexecute_pipeline(
            AsyncOperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        await response.response.aclose()
        return response.output

    async def create_project_profile(
        self,
        domain_identifier: "capo_datazone.types.domain_id.DomainId",
        name: "capo_datazone.types.project_profile_name.ProjectProfileName",
        *,
        config_overrides: Optional[AsyncDataZoneClientConfig] = None,
        description: Optional["capo_datazone.types.description.Description"] = None,
        status: Optional["capo_datazone.types.status.Status"] = None,
        project_resource_tags: Optional[
            "capo_datazone.types.project_resource_tag_parameters.ProjectResourceTagParameters"
        ] = None,
        allow_custom_project_resource_tags: Optional[bool] = None,
        project_resource_tags_description: Optional[
            "capo_datazone.types.description.Description"
        ] = None,
        environment_configurations: Optional[
            "capo_datazone.types.environment_configurations_list.EnvironmentConfigurationsList"
        ] = None,
        domain_unit_identifier: Optional[
            "capo_datazone.types.domain_unit_id.DomainUnitId"
        ] = None,
    ) -> "capo_datazone.types.create_project_profile_output.CreateProjectProfileOutput":
        """<p>Creates a project profile.</p>

        Args:
            domain_identifier: <p>A domain ID of the project profile.</p>
            name: <p>Project profile name.</p>
            description: <p>A description of a project profile.</p>
            status: <p>Project profile status.</p>
            project_resource_tags: <p>The resource tags of the project profile.</p>
            allow_custom_project_resource_tags: <p>Specifies whether custom project resource tags are supported.</p>
            project_resource_tags_description: <p>Field viewable through the UI that provides a project user with the allowed resource tag specifications.</p>
            environment_configurations: <p>Environment configurations of the project profile.</p>
            domain_unit_identifier: <p>A domain unit ID of the project profile.</p>

        Raises:
            capo_datazone.errors.access_denied_exception.AccessDeniedException: <p>You do not have sufficient access to perform this action.</p>
            capo_datazone.errors.throttling_exception.ThrottlingException: <p>The request was denied due to request throttling.</p>
            capo_datazone.errors.unauthorized_exception.UnauthorizedException: <p>You do not have permission to perform this action.</p>
            capo_datazone.errors.conflict_exception.ConflictException: <p>There is a conflict while performing this action.</p>
            capo_datazone.errors.internal_server_exception.InternalServerException: <p>The request has failed because of an unknown error, exception or failure.</p>
            capo_datazone.errors.resource_not_found_exception.ResourceNotFoundException: <p>The specified resource cannot be found.</p>
            capo_datazone.errors.service_quota_exceeded_exception.ServiceQuotaExceededException: <p>The request has exceeded the specified service quota.</p>
            capo_datazone.errors.validation_exception.ValidationException: <p>The input fails to satisfy the constraints specified by the Amazon Web Services service.</p>
            capo_datazone.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        async def _handler(
            req: "AsyncOperationRequest[capo_datazone.types.create_project_profile_input.CreateProjectProfileInput]",
        ) -> AsyncOperationResponse[
            "capo_datazone.types.create_project_profile_output.CreateProjectProfileOutput"
        ]:
            import capo_datazone._operations.data_zone.create_project_profile

            (
                output,
                http_response,
            ) = await capo_datazone._operations.data_zone.create_project_profile.async_create_project_profile(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_datazone.types.create_project_profile_input.CreateProjectProfileInput = {
            "domain_identifier": domain_identifier,
            "name": name,
        }
        if description is not None:
            input_["description"] = description
        if status is not None:
            input_["status"] = status
        if project_resource_tags is not None:
            input_["project_resource_tags"] = project_resource_tags
        if allow_custom_project_resource_tags is not None:
            input_["allow_custom_project_resource_tags"] = (
                allow_custom_project_resource_tags
            )
        if project_resource_tags_description is not None:
            input_["project_resource_tags_description"] = (
                project_resource_tags_description
            )
        if environment_configurations is not None:
            input_["environment_configurations"] = environment_configurations
        if domain_unit_identifier is not None:
            input_["domain_unit_identifier"] = domain_unit_identifier

        response = await aexecute_pipeline(
            AsyncOperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        await response.response.aclose()
        return response.output

    async def create_subscription_grant(
        self,
        domain_identifier: "capo_datazone.types.domain_id.DomainId",
        environment_identifier: "capo_datazone.types.environment_id.EnvironmentId",
        granted_entity: "capo_datazone.types.granted_entity_input.GrantedEntityInput",
        *,
        config_overrides: Optional[AsyncDataZoneClientConfig] = None,
        subscription_target_identifier: Optional[
            "capo_datazone.types.subscription_target_id.SubscriptionTargetId"
        ] = None,
        asset_target_names: Optional[
            "capo_datazone.types.asset_target_names.AssetTargetNames"
        ] = None,
        client_token: Optional[str] = None,
    ) -> "capo_datazone.types.create_subscription_grant_output.CreateSubscriptionGrantOutput":
        """<p>Creates a subsscription grant in Amazon DataZone.</p>

        Args:
            domain_identifier: <p>The ID of the Amazon DataZone domain in which the subscription grant is created.</p>
            environment_identifier: <p>The ID of the environment in which the subscription grant is created.</p>
            subscription_target_identifier: <p>The ID of the subscription target for which the subscription grant is created.</p>
            granted_entity: <p>The entity to which the subscription is to be granted.</p>
            asset_target_names: <p>The names of the assets for which the subscription grant is created.</p>
            client_token: <p>A unique, case-sensitive identifier that is provided to ensure the idempotency of the request.</p>

        Raises:
            capo_datazone.errors.access_denied_exception.AccessDeniedException: <p>You do not have sufficient access to perform this action.</p>
            capo_datazone.errors.throttling_exception.ThrottlingException: <p>The request was denied due to request throttling.</p>
            capo_datazone.errors.unauthorized_exception.UnauthorizedException: <p>You do not have permission to perform this action.</p>
            capo_datazone.errors.conflict_exception.ConflictException: <p>There is a conflict while performing this action.</p>
            capo_datazone.errors.internal_server_exception.InternalServerException: <p>The request has failed because of an unknown error, exception or failure.</p>
            capo_datazone.errors.resource_not_found_exception.ResourceNotFoundException: <p>The specified resource cannot be found.</p>
            capo_datazone.errors.validation_exception.ValidationException: <p>The input fails to satisfy the constraints specified by the Amazon Web Services service.</p>
            capo_datazone.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        async def _handler(
            req: "AsyncOperationRequest[capo_datazone.types.create_subscription_grant_input.CreateSubscriptionGrantInput]",
        ) -> AsyncOperationResponse[
            "capo_datazone.types.create_subscription_grant_output.CreateSubscriptionGrantOutput"
        ]:
            import capo_datazone._operations.data_zone.create_subscription_grant

            (
                output,
                http_response,
            ) = await capo_datazone._operations.data_zone.create_subscription_grant.async_create_subscription_grant(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_datazone.types.create_subscription_grant_input.CreateSubscriptionGrantInput = {
            "domain_identifier": domain_identifier,
            "environment_identifier": environment_identifier,
            "granted_entity": granted_entity,
        }
        if subscription_target_identifier is not None:
            input_["subscription_target_identifier"] = subscription_target_identifier
        if asset_target_names is not None:
            input_["asset_target_names"] = asset_target_names
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

    async def create_subscription_request(
        self,
        domain_identifier: "capo_datazone.types.domain_id.DomainId",
        subscribed_principals: "capo_datazone.types.subscribed_principal_inputs.SubscribedPrincipalInputs",
        subscribed_listings: "capo_datazone.types.subscribed_listing_inputs.SubscribedListingInputs",
        request_reason: "capo_datazone.types.request_reason.RequestReason",
        *,
        config_overrides: Optional[AsyncDataZoneClientConfig] = None,
        client_token: Optional[str] = None,
        metadata_forms: Optional[
            "capo_datazone.types.metadata_form_inputs.MetadataFormInputs"
        ] = None,
        asset_permissions: Optional[
            "capo_datazone.types.asset_permissions.AssetPermissions"
        ] = None,
        asset_scopes: Optional[
            "capo_datazone.types.accepted_asset_scopes.AcceptedAssetScopes"
        ] = None,
    ) -> "capo_datazone.types.create_subscription_request_output.CreateSubscriptionRequestOutput":
        """<p>Creates a subscription request in Amazon DataZone.</p>

        Args:
            domain_identifier: <p>The ID of the Amazon DataZone domain in which the subscription request is created.</p>
            subscribed_principals: <p>The Amazon DataZone principals for whom the subscription request is created.</p>
            subscribed_listings: <p>The published asset for which the subscription grant is to be created.</p>
            request_reason: <p>The reason for the subscription request.</p>
            client_token: <p>A unique, case-sensitive identifier that is provided to ensure the idempotency of the request.</p>
            metadata_forms: <p>The metadata form included in the subscription request.</p>
            asset_permissions: <p>The asset permissions of the subscription request.</p>
            asset_scopes: <p>The asset scopes of the subscription request.</p>

        Raises:
            capo_datazone.errors.access_denied_exception.AccessDeniedException: <p>You do not have sufficient access to perform this action.</p>
            capo_datazone.errors.throttling_exception.ThrottlingException: <p>The request was denied due to request throttling.</p>
            capo_datazone.errors.unauthorized_exception.UnauthorizedException: <p>You do not have permission to perform this action.</p>
            capo_datazone.errors.conflict_exception.ConflictException: <p>There is a conflict while performing this action.</p>
            capo_datazone.errors.internal_server_exception.InternalServerException: <p>The request has failed because of an unknown error, exception or failure.</p>
            capo_datazone.errors.resource_not_found_exception.ResourceNotFoundException: <p>The specified resource cannot be found.</p>
            capo_datazone.errors.service_quota_exceeded_exception.ServiceQuotaExceededException: <p>The request has exceeded the specified service quota.</p>
            capo_datazone.errors.validation_exception.ValidationException: <p>The input fails to satisfy the constraints specified by the Amazon Web Services service.</p>
            capo_datazone.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        async def _handler(
            req: "AsyncOperationRequest[capo_datazone.types.create_subscription_request_input.CreateSubscriptionRequestInput]",
        ) -> AsyncOperationResponse[
            "capo_datazone.types.create_subscription_request_output.CreateSubscriptionRequestOutput"
        ]:
            import capo_datazone._operations.data_zone.create_subscription_request

            (
                output,
                http_response,
            ) = await capo_datazone._operations.data_zone.create_subscription_request.async_create_subscription_request(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_datazone.types.create_subscription_request_input.CreateSubscriptionRequestInput = {
            "domain_identifier": domain_identifier,
            "subscribed_principals": subscribed_principals,
            "subscribed_listings": subscribed_listings,
            "request_reason": request_reason,
        }
        if client_token is None:
            client_token = str(uuid.uuid4())
        input_["client_token"] = client_token
        if metadata_forms is not None:
            input_["metadata_forms"] = metadata_forms
        if asset_permissions is not None:
            input_["asset_permissions"] = asset_permissions
        if asset_scopes is not None:
            input_["asset_scopes"] = asset_scopes

        response = await aexecute_pipeline(
            AsyncOperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        await response.response.aclose()
        return response.output

    async def create_subscription_target(
        self,
        domain_identifier: "capo_datazone.types.domain_id.DomainId",
        environment_identifier: "capo_datazone.types.environment_id.EnvironmentId",
        name: "capo_datazone.types.subscription_target_name.SubscriptionTargetName",
        type: str,
        subscription_target_config: "capo_datazone.types.subscription_target_forms.SubscriptionTargetForms",
        authorized_principals: "capo_datazone.types.authorized_principal_identifiers.AuthorizedPrincipalIdentifiers",
        manage_access_role: "capo_datazone.types.iam_role_arn.IamRoleArn",
        applicable_asset_types: "capo_datazone.types.applicable_asset_types.ApplicableAssetTypes",
        *,
        config_overrides: Optional[AsyncDataZoneClientConfig] = None,
        provider: Optional[str] = None,
        client_token: Optional[str] = None,
        subscription_grant_creation_mode: Optional[
            "capo_datazone.types.subscription_grant_creation_mode.SubscriptionGrantCreationMode"
        ] = None,
    ) -> "capo_datazone.types.create_subscription_target_output.CreateSubscriptionTargetOutput":
        """<p>Creates a subscription target in Amazon DataZone.</p>

        Args:
            domain_identifier: <p>The ID of the Amazon DataZone domain in which subscription target is created.</p>
            environment_identifier: <p>The ID of the environment in which subscription target is created.</p>
            name: <p>The name of the subscription target.</p>
            type: <p>The type of the subscription target.</p>
            subscription_target_config: <p>The configuration of the subscription target.</p>
            authorized_principals: <p>The authorized principals of the subscription target.</p>
            manage_access_role: <p>The manage access role that is used to create the subscription target.</p>
            applicable_asset_types: <p>The asset types that can be included in the subscription target.</p>
            provider: <p>The provider of the subscription target.</p>
            client_token: <p>A unique, case-sensitive identifier that is provided to ensure the idempotency of the request.</p>
            subscription_grant_creation_mode: <p> Determines the subscription grant creation mode for this target, defining if grants are auto-created upon subscription approval or managed manually. </p>

        Raises:
            capo_datazone.errors.access_denied_exception.AccessDeniedException: <p>You do not have sufficient access to perform this action.</p>
            capo_datazone.errors.throttling_exception.ThrottlingException: <p>The request was denied due to request throttling.</p>
            capo_datazone.errors.unauthorized_exception.UnauthorizedException: <p>You do not have permission to perform this action.</p>
            capo_datazone.errors.conflict_exception.ConflictException: <p>There is a conflict while performing this action.</p>
            capo_datazone.errors.internal_server_exception.InternalServerException: <p>The request has failed because of an unknown error, exception or failure.</p>
            capo_datazone.errors.resource_not_found_exception.ResourceNotFoundException: <p>The specified resource cannot be found.</p>
            capo_datazone.errors.validation_exception.ValidationException: <p>The input fails to satisfy the constraints specified by the Amazon Web Services service.</p>
            capo_datazone.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        async def _handler(
            req: "AsyncOperationRequest[capo_datazone.types.create_subscription_target_input.CreateSubscriptionTargetInput]",
        ) -> AsyncOperationResponse[
            "capo_datazone.types.create_subscription_target_output.CreateSubscriptionTargetOutput"
        ]:
            import capo_datazone._operations.data_zone.create_subscription_target

            (
                output,
                http_response,
            ) = await capo_datazone._operations.data_zone.create_subscription_target.async_create_subscription_target(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_datazone.types.create_subscription_target_input.CreateSubscriptionTargetInput = {
            "domain_identifier": domain_identifier,
            "environment_identifier": environment_identifier,
            "name": name,
            "type": type,
            "subscription_target_config": subscription_target_config,
            "authorized_principals": authorized_principals,
            "manage_access_role": manage_access_role,
            "applicable_asset_types": applicable_asset_types,
        }
        if provider is not None:
            input_["provider"] = provider
        if client_token is None:
            client_token = str(uuid.uuid4())
        input_["client_token"] = client_token
        if subscription_grant_creation_mode is not None:
            input_["subscription_grant_creation_mode"] = (
                subscription_grant_creation_mode
            )

        response = await aexecute_pipeline(
            AsyncOperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        await response.response.aclose()
        return response.output

    async def create_user_profile(
        self,
        domain_identifier: "capo_datazone.types.domain_id.DomainId",
        user_identifier: "capo_datazone.types.user_identifier.UserIdentifier",
        *,
        config_overrides: Optional[AsyncDataZoneClientConfig] = None,
        user_type: Optional["capo_datazone.types.user_type.UserType"] = None,
        session_name: Optional[str] = None,
        client_token: Optional[str] = None,
    ) -> "capo_datazone.types.create_user_profile_output.CreateUserProfileOutput":
        """<p>Creates a user profile in Amazon DataZone.</p>

        Args:
            domain_identifier: <p>The identifier of the Amazon DataZone domain in which a user profile is created.</p>
            user_identifier: <p>The identifier of the user for which the user profile is created.</p>
            user_type: <p>The user type of the user for which the user profile is created.</p>
            session_name: <p>The session name for IAM role sessions.</p>
            client_token: <p>A unique, case-sensitive identifier that is provided to ensure the idempotency of the request.</p>

        Raises:
            capo_datazone.errors.access_denied_exception.AccessDeniedException: <p>You do not have sufficient access to perform this action.</p>
            capo_datazone.errors.throttling_exception.ThrottlingException: <p>The request was denied due to request throttling.</p>
            capo_datazone.errors.unauthorized_exception.UnauthorizedException: <p>You do not have permission to perform this action.</p>
            capo_datazone.errors.internal_server_exception.InternalServerException: <p>The request has failed because of an unknown error, exception or failure.</p>
            capo_datazone.errors.resource_not_found_exception.ResourceNotFoundException: <p>The specified resource cannot be found.</p>
            capo_datazone.errors.validation_exception.ValidationException: <p>The input fails to satisfy the constraints specified by the Amazon Web Services service.</p>
            capo_datazone.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        async def _handler(
            req: "AsyncOperationRequest[capo_datazone.types.create_user_profile_input.CreateUserProfileInput]",
        ) -> AsyncOperationResponse[
            "capo_datazone.types.create_user_profile_output.CreateUserProfileOutput"
        ]:
            import capo_datazone._operations.data_zone.create_user_profile

            (
                output,
                http_response,
            ) = await capo_datazone._operations.data_zone.create_user_profile.async_create_user_profile(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_datazone.types.create_user_profile_input.CreateUserProfileInput = {
            "domain_identifier": domain_identifier,
            "user_identifier": user_identifier,
        }
        if user_type is not None:
            input_["user_type"] = user_type
        if session_name is not None:
            input_["session_name"] = session_name
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

    async def delete_account_pool(
        self,
        domain_identifier: "capo_datazone.types.domain_id.DomainId",
        identifier: "capo_datazone.types.account_pool_id.AccountPoolId",
        *,
        config_overrides: Optional[AsyncDataZoneClientConfig] = None,
    ) -> "capo_datazone.types.delete_account_pool_output.DeleteAccountPoolOutput":
        """<p>Deletes an account pool.</p>

        Args:
            domain_identifier: <p>The ID of the domain where the account pool is deleted.</p>
            identifier: <p>The ID of the account pool to be deleted.</p>

        Raises:
            capo_datazone.errors.access_denied_exception.AccessDeniedException: <p>You do not have sufficient access to perform this action.</p>
            capo_datazone.errors.throttling_exception.ThrottlingException: <p>The request was denied due to request throttling.</p>
            capo_datazone.errors.unauthorized_exception.UnauthorizedException: <p>You do not have permission to perform this action.</p>
            capo_datazone.errors.internal_server_exception.InternalServerException: <p>The request has failed because of an unknown error, exception or failure.</p>
            capo_datazone.errors.resource_not_found_exception.ResourceNotFoundException: <p>The specified resource cannot be found.</p>
            capo_datazone.errors.validation_exception.ValidationException: <p>The input fails to satisfy the constraints specified by the Amazon Web Services service.</p>
            capo_datazone.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        async def _handler(
            req: "AsyncOperationRequest[capo_datazone.types.delete_account_pool_input.DeleteAccountPoolInput]",
        ) -> AsyncOperationResponse[
            "capo_datazone.types.delete_account_pool_output.DeleteAccountPoolOutput"
        ]:
            import capo_datazone._operations.data_zone.delete_account_pool

            (
                output,
                http_response,
            ) = await capo_datazone._operations.data_zone.delete_account_pool.async_delete_account_pool(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_datazone.types.delete_account_pool_input.DeleteAccountPoolInput = {
            "domain_identifier": domain_identifier,
            "identifier": identifier,
        }

        response = await aexecute_pipeline(
            AsyncOperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        await response.response.aclose()
        return response.output

    async def delete_asset_filter(
        self,
        domain_identifier: "capo_datazone.types.domain_id.DomainId",
        asset_identifier: "capo_datazone.types.asset_id.AssetId",
        identifier: "capo_datazone.types.filter_id.FilterId",
        *,
        config_overrides: Optional[AsyncDataZoneClientConfig] = None,
    ) -> None:
        """<p>Deletes an asset filter.</p> <p>Prerequisites:</p> <ul> <li> <p>The asset filter must exist. </p> </li> <li> <p>The domain and asset must not have been deleted.</p> </li> <li> <p>Ensure the --identifier refers to a valid filter ID.</p> </li> </ul>

        Args:
            domain_identifier: <p>The ID of the domain where you want to delete an asset filter.</p>
            asset_identifier: <p>The ID of the data asset.</p>
            identifier: <p>The ID of the asset filter that you want to delete.</p>

        Raises:
            capo_datazone.errors.access_denied_exception.AccessDeniedException: <p>You do not have sufficient access to perform this action.</p>
            capo_datazone.errors.throttling_exception.ThrottlingException: <p>The request was denied due to request throttling.</p>
            capo_datazone.errors.unauthorized_exception.UnauthorizedException: <p>You do not have permission to perform this action.</p>
            capo_datazone.errors.conflict_exception.ConflictException: <p>There is a conflict while performing this action.</p>
            capo_datazone.errors.internal_server_exception.InternalServerException: <p>The request has failed because of an unknown error, exception or failure.</p>
            capo_datazone.errors.resource_not_found_exception.ResourceNotFoundException: <p>The specified resource cannot be found.</p>
            capo_datazone.errors.validation_exception.ValidationException: <p>The input fails to satisfy the constraints specified by the Amazon Web Services service.</p>
            capo_datazone.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        async def _handler(
            req: "AsyncOperationRequest[capo_datazone.types.delete_asset_filter_input.DeleteAssetFilterInput]",
        ) -> AsyncOperationResponse[None]:
            import capo_datazone._operations.data_zone.delete_asset_filter

            (
                output,
                http_response,
            ) = await capo_datazone._operations.data_zone.delete_asset_filter.async_delete_asset_filter(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_datazone.types.delete_asset_filter_input.DeleteAssetFilterInput = {
            "domain_identifier": domain_identifier,
            "asset_identifier": asset_identifier,
            "identifier": identifier,
        }

        response = await aexecute_pipeline(
            AsyncOperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        await response.response.aclose()
        return response.output

    async def delete_connection(
        self,
        domain_identifier: "capo_datazone.types.domain_id.DomainId",
        identifier: "capo_datazone.types.connection_id.ConnectionId",
        *,
        config_overrides: Optional[AsyncDataZoneClientConfig] = None,
    ) -> "capo_datazone.types.delete_connection_output.DeleteConnectionOutput":
        """<p>Deletes and connection. In Amazon DataZone, a connection enables you to connect your resources (domains, projects, and environments) to external resources and services.</p>

        Args:
            domain_identifier: <p>The ID of the domain where the connection is deleted.</p>
            identifier: <p>The ID of the connection that is deleted.</p>

        Raises:
            capo_datazone.errors.access_denied_exception.AccessDeniedException: <p>You do not have sufficient access to perform this action.</p>
            capo_datazone.errors.throttling_exception.ThrottlingException: <p>The request was denied due to request throttling.</p>
            capo_datazone.errors.unauthorized_exception.UnauthorizedException: <p>You do not have permission to perform this action.</p>
            capo_datazone.errors.internal_server_exception.InternalServerException: <p>The request has failed because of an unknown error, exception or failure.</p>
            capo_datazone.errors.resource_not_found_exception.ResourceNotFoundException: <p>The specified resource cannot be found.</p>
            capo_datazone.errors.validation_exception.ValidationException: <p>The input fails to satisfy the constraints specified by the Amazon Web Services service.</p>
            capo_datazone.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        async def _handler(
            req: "AsyncOperationRequest[capo_datazone.types.delete_connection_input.DeleteConnectionInput]",
        ) -> AsyncOperationResponse[
            "capo_datazone.types.delete_connection_output.DeleteConnectionOutput"
        ]:
            import capo_datazone._operations.data_zone.delete_connection

            (
                output,
                http_response,
            ) = await capo_datazone._operations.data_zone.delete_connection.async_delete_connection(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_datazone.types.delete_connection_input.DeleteConnectionInput = {
            "domain_identifier": domain_identifier,
            "identifier": identifier,
        }

        response = await aexecute_pipeline(
            AsyncOperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        await response.response.aclose()
        return response.output

    async def delete_data_export_configuration(
        self,
        domain_identifier: "capo_datazone.types.domain_id.DomainId",
        *,
        config_overrides: Optional[AsyncDataZoneClientConfig] = None,
    ) -> "capo_datazone.types.delete_data_export_configuration_output.DeleteDataExportConfigurationOutput":
        """<p>Deletes data export configuration for a domain.</p> <p>This operation does not delete the S3 table created by the PutDataExportConfiguration operation.</p> <p>To temporarily disable export without deleting the configuration, use the PutDataExportConfiguration operation with the <code>--no-enable-export</code> flag instead. This allows you to re-enable export for the same domain using the <code>--enable-export</code> flag without deleting S3 table.</p>

        Args:
            domain_identifier: <p>The domain ID for which you want to delete the data export configuration.</p>

        Raises:
            capo_datazone.errors.access_denied_exception.AccessDeniedException: <p>You do not have sufficient access to perform this action.</p>
            capo_datazone.errors.throttling_exception.ThrottlingException: <p>The request was denied due to request throttling.</p>
            capo_datazone.errors.unauthorized_exception.UnauthorizedException: <p>You do not have permission to perform this action.</p>
            capo_datazone.errors.conflict_exception.ConflictException: <p>There is a conflict while performing this action.</p>
            capo_datazone.errors.internal_server_exception.InternalServerException: <p>The request has failed because of an unknown error, exception or failure.</p>
            capo_datazone.errors.resource_not_found_exception.ResourceNotFoundException: <p>The specified resource cannot be found.</p>
            capo_datazone.errors.validation_exception.ValidationException: <p>The input fails to satisfy the constraints specified by the Amazon Web Services service.</p>
            capo_datazone.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        async def _handler(
            req: "AsyncOperationRequest[capo_datazone.types.delete_data_export_configuration_input.DeleteDataExportConfigurationInput]",
        ) -> AsyncOperationResponse[
            "capo_datazone.types.delete_data_export_configuration_output.DeleteDataExportConfigurationOutput"
        ]:
            import capo_datazone._operations.data_zone.delete_data_export_configuration

            (
                output,
                http_response,
            ) = await capo_datazone._operations.data_zone.delete_data_export_configuration.async_delete_data_export_configuration(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_datazone.types.delete_data_export_configuration_input.DeleteDataExportConfigurationInput = {
            "domain_identifier": domain_identifier
        }

        response = await aexecute_pipeline(
            AsyncOperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        await response.response.aclose()
        return response.output

    async def delete_environment(
        self,
        domain_identifier: "capo_datazone.types.domain_id.DomainId",
        identifier: "capo_datazone.types.environment_id.EnvironmentId",
        *,
        config_overrides: Optional[AsyncDataZoneClientConfig] = None,
    ) -> None:
        """<p>Deletes an environment in Amazon DataZone.</p>

        Args:
            domain_identifier: <p>The ID of the Amazon DataZone domain in which the environment is deleted.</p>
            identifier: <p>The identifier of the environment that is to be deleted.</p>

        Raises:
            capo_datazone.errors.access_denied_exception.AccessDeniedException: <p>You do not have sufficient access to perform this action.</p>
            capo_datazone.errors.throttling_exception.ThrottlingException: <p>The request was denied due to request throttling.</p>
            capo_datazone.errors.unauthorized_exception.UnauthorizedException: <p>You do not have permission to perform this action.</p>
            capo_datazone.errors.internal_server_exception.InternalServerException: <p>The request has failed because of an unknown error, exception or failure.</p>
            capo_datazone.errors.resource_not_found_exception.ResourceNotFoundException: <p>The specified resource cannot be found.</p>
            capo_datazone.errors.validation_exception.ValidationException: <p>The input fails to satisfy the constraints specified by the Amazon Web Services service.</p>
            capo_datazone.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        async def _handler(
            req: "AsyncOperationRequest[capo_datazone.types.delete_environment_input.DeleteEnvironmentInput]",
        ) -> AsyncOperationResponse[None]:
            import capo_datazone._operations.data_zone.delete_environment

            (
                output,
                http_response,
            ) = await capo_datazone._operations.data_zone.delete_environment.async_delete_environment(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_datazone.types.delete_environment_input.DeleteEnvironmentInput = {
            "domain_identifier": domain_identifier,
            "identifier": identifier,
        }

        response = await aexecute_pipeline(
            AsyncOperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        await response.response.aclose()
        return response.output

    async def delete_environment_action(
        self,
        domain_identifier: "capo_datazone.types.domain_id.DomainId",
        environment_identifier: "capo_datazone.types.environment_id.EnvironmentId",
        identifier: str,
        *,
        config_overrides: Optional[AsyncDataZoneClientConfig] = None,
    ) -> None:
        """<p>Deletes an action for the environment, for example, deletes a console link for an analytics tool that is available in this environment.</p>

        Args:
            domain_identifier: <p>The ID of the Amazon DataZone domain in which an environment action is deleted.</p>
            environment_identifier: <p>The ID of the environment where an environment action is deleted.</p>
            identifier: <p>The ID of the environment action that is deleted.</p>

        Raises:
            capo_datazone.errors.access_denied_exception.AccessDeniedException: <p>You do not have sufficient access to perform this action.</p>
            capo_datazone.errors.throttling_exception.ThrottlingException: <p>The request was denied due to request throttling.</p>
            capo_datazone.errors.unauthorized_exception.UnauthorizedException: <p>You do not have permission to perform this action.</p>
            capo_datazone.errors.conflict_exception.ConflictException: <p>There is a conflict while performing this action.</p>
            capo_datazone.errors.internal_server_exception.InternalServerException: <p>The request has failed because of an unknown error, exception or failure.</p>
            capo_datazone.errors.resource_not_found_exception.ResourceNotFoundException: <p>The specified resource cannot be found.</p>
            capo_datazone.errors.validation_exception.ValidationException: <p>The input fails to satisfy the constraints specified by the Amazon Web Services service.</p>
            capo_datazone.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        async def _handler(
            req: "AsyncOperationRequest[capo_datazone.types.delete_environment_action_input.DeleteEnvironmentActionInput]",
        ) -> AsyncOperationResponse[None]:
            import capo_datazone._operations.data_zone.delete_environment_action

            (
                output,
                http_response,
            ) = await capo_datazone._operations.data_zone.delete_environment_action.async_delete_environment_action(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_datazone.types.delete_environment_action_input.DeleteEnvironmentActionInput = {
            "domain_identifier": domain_identifier,
            "environment_identifier": environment_identifier,
            "identifier": identifier,
        }

        response = await aexecute_pipeline(
            AsyncOperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        await response.response.aclose()
        return response.output

    async def delete_environment_blueprint(
        self,
        domain_identifier: "capo_datazone.types.domain_id.DomainId",
        identifier: "capo_datazone.types.environment_blueprint_id.EnvironmentBlueprintId",
        *,
        config_overrides: Optional[AsyncDataZoneClientConfig] = None,
    ) -> None:
        """<p>Deletes a blueprint in Amazon DataZone.</p>

        Args:
            domain_identifier: <p>The ID of the Amazon DataZone domain in which the blueprint is deleted.</p>
            identifier: <p>The ID of the blueprint that is deleted.</p>

        Raises:
            capo_datazone.errors.access_denied_exception.AccessDeniedException: <p>You do not have sufficient access to perform this action.</p>
            capo_datazone.errors.throttling_exception.ThrottlingException: <p>The request was denied due to request throttling.</p>
            capo_datazone.errors.unauthorized_exception.UnauthorizedException: <p>You do not have permission to perform this action.</p>
            capo_datazone.errors.conflict_exception.ConflictException: <p>There is a conflict while performing this action.</p>
            capo_datazone.errors.internal_server_exception.InternalServerException: <p>The request has failed because of an unknown error, exception or failure.</p>
            capo_datazone.errors.resource_not_found_exception.ResourceNotFoundException: <p>The specified resource cannot be found.</p>
            capo_datazone.errors.validation_exception.ValidationException: <p>The input fails to satisfy the constraints specified by the Amazon Web Services service.</p>
            capo_datazone.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        async def _handler(
            req: "AsyncOperationRequest[capo_datazone.types.delete_environment_blueprint_input.DeleteEnvironmentBlueprintInput]",
        ) -> AsyncOperationResponse[None]:
            import capo_datazone._operations.data_zone.delete_environment_blueprint

            (
                output,
                http_response,
            ) = await capo_datazone._operations.data_zone.delete_environment_blueprint.async_delete_environment_blueprint(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_datazone.types.delete_environment_blueprint_input.DeleteEnvironmentBlueprintInput = {
            "domain_identifier": domain_identifier,
            "identifier": identifier,
        }

        response = await aexecute_pipeline(
            AsyncOperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        await response.response.aclose()
        return response.output

    async def delete_environment_profile(
        self,
        domain_identifier: "capo_datazone.types.domain_id.DomainId",
        identifier: "capo_datazone.types.environment_profile_id.EnvironmentProfileId",
        *,
        config_overrides: Optional[AsyncDataZoneClientConfig] = None,
    ) -> None:
        """<p>Deletes an environment profile in Amazon DataZone.</p>

        Args:
            domain_identifier: <p>The ID of the Amazon DataZone domain in which the environment profile is deleted.</p>
            identifier: <p>The ID of the environment profile that is deleted.</p>

        Raises:
            capo_datazone.errors.access_denied_exception.AccessDeniedException: <p>You do not have sufficient access to perform this action.</p>
            capo_datazone.errors.throttling_exception.ThrottlingException: <p>The request was denied due to request throttling.</p>
            capo_datazone.errors.unauthorized_exception.UnauthorizedException: <p>You do not have permission to perform this action.</p>
            capo_datazone.errors.internal_server_exception.InternalServerException: <p>The request has failed because of an unknown error, exception or failure.</p>
            capo_datazone.errors.resource_not_found_exception.ResourceNotFoundException: <p>The specified resource cannot be found.</p>
            capo_datazone.errors.validation_exception.ValidationException: <p>The input fails to satisfy the constraints specified by the Amazon Web Services service.</p>
            capo_datazone.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        async def _handler(
            req: "AsyncOperationRequest[capo_datazone.types.delete_environment_profile_input.DeleteEnvironmentProfileInput]",
        ) -> AsyncOperationResponse[None]:
            import capo_datazone._operations.data_zone.delete_environment_profile

            (
                output,
                http_response,
            ) = await capo_datazone._operations.data_zone.delete_environment_profile.async_delete_environment_profile(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_datazone.types.delete_environment_profile_input.DeleteEnvironmentProfileInput = {
            "domain_identifier": domain_identifier,
            "identifier": identifier,
        }

        response = await aexecute_pipeline(
            AsyncOperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        await response.response.aclose()
        return response.output

    async def delete_lineage_event(
        self,
        domain_identifier: "capo_datazone.types.domain_id.DomainId",
        identifier: "capo_datazone.types.lineage_event_identifier.LineageEventIdentifier",
        *,
        config_overrides: Optional[AsyncDataZoneClientConfig] = None,
    ) -> "capo_datazone.types.delete_lineage_event_output.DeleteLineageEventOutput":
        """<p>Deletes the specified lineage event.</p>

        Args:
            domain_identifier: <p>The ID of the domain.</p>
            identifier: <p>The ID of the lineage event.</p>

        Raises:
            capo_datazone.errors.access_denied_exception.AccessDeniedException: <p>You do not have sufficient access to perform this action.</p>
            capo_datazone.errors.throttling_exception.ThrottlingException: <p>The request was denied due to request throttling.</p>
            capo_datazone.errors.unauthorized_exception.UnauthorizedException: <p>You do not have permission to perform this action.</p>
            capo_datazone.errors.internal_server_exception.InternalServerException: <p>The request has failed because of an unknown error, exception or failure.</p>
            capo_datazone.errors.resource_not_found_exception.ResourceNotFoundException: <p>The specified resource cannot be found.</p>
            capo_datazone.errors.validation_exception.ValidationException: <p>The input fails to satisfy the constraints specified by the Amazon Web Services service.</p>
            capo_datazone.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        async def _handler(
            req: "AsyncOperationRequest[capo_datazone.types.delete_lineage_event_input.DeleteLineageEventInput]",
        ) -> AsyncOperationResponse[
            "capo_datazone.types.delete_lineage_event_output.DeleteLineageEventOutput"
        ]:
            import capo_datazone._operations.data_zone.delete_lineage_event

            (
                output,
                http_response,
            ) = await capo_datazone._operations.data_zone.delete_lineage_event.async_delete_lineage_event(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_datazone.types.delete_lineage_event_input.DeleteLineageEventInput = {
            "domain_identifier": domain_identifier,
            "identifier": identifier,
        }

        response = await aexecute_pipeline(
            AsyncOperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        await response.response.aclose()
        return response.output

    async def delete_project(
        self,
        domain_identifier: "capo_datazone.types.domain_id.DomainId",
        identifier: "capo_datazone.types.project_id.ProjectId",
        *,
        config_overrides: Optional[AsyncDataZoneClientConfig] = None,
        skip_deletion_check: Optional[bool] = None,
    ) -> "capo_datazone.types.delete_project_output.DeleteProjectOutput":
        """<p>Deletes a project in Amazon DataZone. </p>

        Args:
            domain_identifier: <p>The ID of the Amazon DataZone domain in which the project is deleted.</p>
            identifier: <p>The identifier of the project that is to be deleted.</p>
            skip_deletion_check: <p>Specifies the optional flag to delete all child entities within the project.</p>

        Raises:
            capo_datazone.errors.access_denied_exception.AccessDeniedException: <p>You do not have sufficient access to perform this action.</p>
            capo_datazone.errors.throttling_exception.ThrottlingException: <p>The request was denied due to request throttling.</p>
            capo_datazone.errors.unauthorized_exception.UnauthorizedException: <p>You do not have permission to perform this action.</p>
            capo_datazone.errors.internal_server_exception.InternalServerException: <p>The request has failed because of an unknown error, exception or failure.</p>
            capo_datazone.errors.resource_not_found_exception.ResourceNotFoundException: <p>The specified resource cannot be found.</p>
            capo_datazone.errors.validation_exception.ValidationException: <p>The input fails to satisfy the constraints specified by the Amazon Web Services service.</p>
            capo_datazone.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        async def _handler(
            req: "AsyncOperationRequest[capo_datazone.types.delete_project_input.DeleteProjectInput]",
        ) -> AsyncOperationResponse[
            "capo_datazone.types.delete_project_output.DeleteProjectOutput"
        ]:
            import capo_datazone._operations.data_zone.delete_project

            (
                output,
                http_response,
            ) = await capo_datazone._operations.data_zone.delete_project.async_delete_project(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_datazone.types.delete_project_input.DeleteProjectInput = {
            "domain_identifier": domain_identifier,
            "identifier": identifier,
        }
        if skip_deletion_check is not None:
            input_["skip_deletion_check"] = skip_deletion_check

        response = await aexecute_pipeline(
            AsyncOperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        await response.response.aclose()
        return response.output

    async def delete_project_membership(
        self,
        domain_identifier: "capo_datazone.types.domain_id.DomainId",
        project_identifier: "capo_datazone.types.project_id.ProjectId",
        member: "capo_datazone.types.member.Member",
        *,
        config_overrides: Optional[AsyncDataZoneClientConfig] = None,
    ) -> "capo_datazone.types.delete_project_membership_output.DeleteProjectMembershipOutput":
        """<p>Deletes project membership in Amazon DataZone.</p>

        Args:
            domain_identifier: <p>The ID of the Amazon DataZone domain where project membership is deleted.</p>
            project_identifier: <p>The ID of the Amazon DataZone project the membership to which is deleted.</p>
            member: <p>The project member whose project membership is deleted.</p>

        Raises:
            capo_datazone.errors.access_denied_exception.AccessDeniedException: <p>You do not have sufficient access to perform this action.</p>
            capo_datazone.errors.throttling_exception.ThrottlingException: <p>The request was denied due to request throttling.</p>
            capo_datazone.errors.unauthorized_exception.UnauthorizedException: <p>You do not have permission to perform this action.</p>
            capo_datazone.errors.internal_server_exception.InternalServerException: <p>The request has failed because of an unknown error, exception or failure.</p>
            capo_datazone.errors.resource_not_found_exception.ResourceNotFoundException: <p>The specified resource cannot be found.</p>
            capo_datazone.errors.service_quota_exceeded_exception.ServiceQuotaExceededException: <p>The request has exceeded the specified service quota.</p>
            capo_datazone.errors.validation_exception.ValidationException: <p>The input fails to satisfy the constraints specified by the Amazon Web Services service.</p>
            capo_datazone.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        async def _handler(
            req: "AsyncOperationRequest[capo_datazone.types.delete_project_membership_input.DeleteProjectMembershipInput]",
        ) -> AsyncOperationResponse[
            "capo_datazone.types.delete_project_membership_output.DeleteProjectMembershipOutput"
        ]:
            import capo_datazone._operations.data_zone.delete_project_membership

            (
                output,
                http_response,
            ) = await capo_datazone._operations.data_zone.delete_project_membership.async_delete_project_membership(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_datazone.types.delete_project_membership_input.DeleteProjectMembershipInput = {
            "domain_identifier": domain_identifier,
            "project_identifier": project_identifier,
            "member": member,
        }

        response = await aexecute_pipeline(
            AsyncOperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        await response.response.aclose()
        return response.output

    async def delete_project_profile(
        self,
        domain_identifier: "capo_datazone.types.domain_id.DomainId",
        identifier: "capo_datazone.types.project_profile_id.ProjectProfileId",
        *,
        config_overrides: Optional[AsyncDataZoneClientConfig] = None,
    ) -> "capo_datazone.types.delete_project_profile_output.DeleteProjectProfileOutput":
        """<p>Deletes a project profile.</p>

        Args:
            domain_identifier: <p>The ID of the domain where a project profile is deleted.</p>
            identifier: <p>The ID of the project profile that is deleted.</p>

        Raises:
            capo_datazone.errors.access_denied_exception.AccessDeniedException: <p>You do not have sufficient access to perform this action.</p>
            capo_datazone.errors.throttling_exception.ThrottlingException: <p>The request was denied due to request throttling.</p>
            capo_datazone.errors.unauthorized_exception.UnauthorizedException: <p>You do not have permission to perform this action.</p>
            capo_datazone.errors.internal_server_exception.InternalServerException: <p>The request has failed because of an unknown error, exception or failure.</p>
            capo_datazone.errors.resource_not_found_exception.ResourceNotFoundException: <p>The specified resource cannot be found.</p>
            capo_datazone.errors.validation_exception.ValidationException: <p>The input fails to satisfy the constraints specified by the Amazon Web Services service.</p>
            capo_datazone.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        async def _handler(
            req: "AsyncOperationRequest[capo_datazone.types.delete_project_profile_input.DeleteProjectProfileInput]",
        ) -> AsyncOperationResponse[
            "capo_datazone.types.delete_project_profile_output.DeleteProjectProfileOutput"
        ]:
            import capo_datazone._operations.data_zone.delete_project_profile

            (
                output,
                http_response,
            ) = await capo_datazone._operations.data_zone.delete_project_profile.async_delete_project_profile(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_datazone.types.delete_project_profile_input.DeleteProjectProfileInput = {
            "domain_identifier": domain_identifier,
            "identifier": identifier,
        }

        response = await aexecute_pipeline(
            AsyncOperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        await response.response.aclose()
        return response.output

    async def delete_subscription_grant(
        self,
        domain_identifier: "capo_datazone.types.domain_id.DomainId",
        identifier: "capo_datazone.types.subscription_grant_id.SubscriptionGrantId",
        *,
        config_overrides: Optional[AsyncDataZoneClientConfig] = None,
    ) -> "capo_datazone.types.delete_subscription_grant_output.DeleteSubscriptionGrantOutput":
        """<p>Deletes and subscription grant in Amazon DataZone.</p>

        Args:
            domain_identifier: <p>The ID of the Amazon DataZone domain where the subscription grant is deleted.</p>
            identifier: <p>The ID of the subscription grant that is deleted.</p>

        Raises:
            capo_datazone.errors.access_denied_exception.AccessDeniedException: <p>You do not have sufficient access to perform this action.</p>
            capo_datazone.errors.throttling_exception.ThrottlingException: <p>The request was denied due to request throttling.</p>
            capo_datazone.errors.unauthorized_exception.UnauthorizedException: <p>You do not have permission to perform this action.</p>
            capo_datazone.errors.conflict_exception.ConflictException: <p>There is a conflict while performing this action.</p>
            capo_datazone.errors.internal_server_exception.InternalServerException: <p>The request has failed because of an unknown error, exception or failure.</p>
            capo_datazone.errors.resource_not_found_exception.ResourceNotFoundException: <p>The specified resource cannot be found.</p>
            capo_datazone.errors.validation_exception.ValidationException: <p>The input fails to satisfy the constraints specified by the Amazon Web Services service.</p>
            capo_datazone.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        async def _handler(
            req: "AsyncOperationRequest[capo_datazone.types.delete_subscription_grant_input.DeleteSubscriptionGrantInput]",
        ) -> AsyncOperationResponse[
            "capo_datazone.types.delete_subscription_grant_output.DeleteSubscriptionGrantOutput"
        ]:
            import capo_datazone._operations.data_zone.delete_subscription_grant

            (
                output,
                http_response,
            ) = await capo_datazone._operations.data_zone.delete_subscription_grant.async_delete_subscription_grant(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_datazone.types.delete_subscription_grant_input.DeleteSubscriptionGrantInput = {
            "domain_identifier": domain_identifier,
            "identifier": identifier,
        }

        response = await aexecute_pipeline(
            AsyncOperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        await response.response.aclose()
        return response.output

    async def delete_subscription_request(
        self,
        domain_identifier: "capo_datazone.types.domain_id.DomainId",
        identifier: "capo_datazone.types.subscription_request_id.SubscriptionRequestId",
        *,
        config_overrides: Optional[AsyncDataZoneClientConfig] = None,
    ) -> None:
        """<p>Deletes a subscription request in Amazon DataZone.</p>

        Args:
            domain_identifier: <p>The ID of the Amazon DataZone domain in which the subscription request is deleted.</p>
            identifier: <p>The ID of the subscription request that is deleted.</p>

        Raises:
            capo_datazone.errors.access_denied_exception.AccessDeniedException: <p>You do not have sufficient access to perform this action.</p>
            capo_datazone.errors.throttling_exception.ThrottlingException: <p>The request was denied due to request throttling.</p>
            capo_datazone.errors.unauthorized_exception.UnauthorizedException: <p>You do not have permission to perform this action.</p>
            capo_datazone.errors.conflict_exception.ConflictException: <p>There is a conflict while performing this action.</p>
            capo_datazone.errors.internal_server_exception.InternalServerException: <p>The request has failed because of an unknown error, exception or failure.</p>
            capo_datazone.errors.resource_not_found_exception.ResourceNotFoundException: <p>The specified resource cannot be found.</p>
            capo_datazone.errors.validation_exception.ValidationException: <p>The input fails to satisfy the constraints specified by the Amazon Web Services service.</p>
            capo_datazone.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        async def _handler(
            req: "AsyncOperationRequest[capo_datazone.types.delete_subscription_request_input.DeleteSubscriptionRequestInput]",
        ) -> AsyncOperationResponse[None]:
            import capo_datazone._operations.data_zone.delete_subscription_request

            (
                output,
                http_response,
            ) = await capo_datazone._operations.data_zone.delete_subscription_request.async_delete_subscription_request(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_datazone.types.delete_subscription_request_input.DeleteSubscriptionRequestInput = {
            "domain_identifier": domain_identifier,
            "identifier": identifier,
        }

        response = await aexecute_pipeline(
            AsyncOperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        await response.response.aclose()
        return response.output

    async def delete_subscription_target(
        self,
        domain_identifier: "capo_datazone.types.domain_id.DomainId",
        environment_identifier: "capo_datazone.types.environment_id.EnvironmentId",
        identifier: "capo_datazone.types.subscription_target_id.SubscriptionTargetId",
        *,
        config_overrides: Optional[AsyncDataZoneClientConfig] = None,
    ) -> None:
        """<p>Deletes a subscription target in Amazon DataZone.</p>

        Args:
            domain_identifier: <p>The ID of the Amazon DataZone domain in which the subscription target is deleted.</p>
            environment_identifier: <p>The ID of the Amazon DataZone environment in which the subscription target is deleted.</p>
            identifier: <p>The ID of the subscription target that is deleted.</p>

        Raises:
            capo_datazone.errors.access_denied_exception.AccessDeniedException: <p>You do not have sufficient access to perform this action.</p>
            capo_datazone.errors.throttling_exception.ThrottlingException: <p>The request was denied due to request throttling.</p>
            capo_datazone.errors.unauthorized_exception.UnauthorizedException: <p>You do not have permission to perform this action.</p>
            capo_datazone.errors.conflict_exception.ConflictException: <p>There is a conflict while performing this action.</p>
            capo_datazone.errors.internal_server_exception.InternalServerException: <p>The request has failed because of an unknown error, exception or failure.</p>
            capo_datazone.errors.resource_not_found_exception.ResourceNotFoundException: <p>The specified resource cannot be found.</p>
            capo_datazone.errors.validation_exception.ValidationException: <p>The input fails to satisfy the constraints specified by the Amazon Web Services service.</p>
            capo_datazone.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        async def _handler(
            req: "AsyncOperationRequest[capo_datazone.types.delete_subscription_target_input.DeleteSubscriptionTargetInput]",
        ) -> AsyncOperationResponse[None]:
            import capo_datazone._operations.data_zone.delete_subscription_target

            (
                output,
                http_response,
            ) = await capo_datazone._operations.data_zone.delete_subscription_target.async_delete_subscription_target(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_datazone.types.delete_subscription_target_input.DeleteSubscriptionTargetInput = {
            "domain_identifier": domain_identifier,
            "environment_identifier": environment_identifier,
            "identifier": identifier,
        }

        response = await aexecute_pipeline(
            AsyncOperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        await response.response.aclose()
        return response.output

    async def delete_time_series_data_points(
        self,
        domain_identifier: "capo_datazone.types.domain_id.DomainId",
        entity_identifier: "capo_datazone.types.entity_identifier.EntityIdentifier",
        entity_type: "capo_datazone.types.time_series_entity_type.TimeSeriesEntityType",
        form_name: "capo_datazone.types.time_series_form_name.TimeSeriesFormName",
        *,
        config_overrides: Optional[AsyncDataZoneClientConfig] = None,
        client_token: Optional["capo_datazone.types.client_token.ClientToken"] = None,
    ) -> "capo_datazone.types.delete_time_series_data_points_output.DeleteTimeSeriesDataPointsOutput":
        """<p>Deletes the specified time series form for the specified asset. </p>

        Args:
            domain_identifier: <p>The ID of the Amazon DataZone domain that houses the asset for which you want to delete a time series form.</p>
            entity_identifier: <p>The ID of the asset for which you want to delete a time series form.</p>
            entity_type: <p>The type of the asset for which you want to delete a time series form.</p>
            form_name: <p>The name of the time series form that you want to delete.</p>
            client_token: <p>A unique, case-sensitive identifier to ensure idempotency of the request. This field is automatically populated if not provided.</p>

        Raises:
            capo_datazone.errors.access_denied_exception.AccessDeniedException: <p>You do not have sufficient access to perform this action.</p>
            capo_datazone.errors.throttling_exception.ThrottlingException: <p>The request was denied due to request throttling.</p>
            capo_datazone.errors.unauthorized_exception.UnauthorizedException: <p>You do not have permission to perform this action.</p>
            capo_datazone.errors.internal_server_exception.InternalServerException: <p>The request has failed because of an unknown error, exception or failure.</p>
            capo_datazone.errors.resource_not_found_exception.ResourceNotFoundException: <p>The specified resource cannot be found.</p>
            capo_datazone.errors.validation_exception.ValidationException: <p>The input fails to satisfy the constraints specified by the Amazon Web Services service.</p>
            capo_datazone.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        async def _handler(
            req: "AsyncOperationRequest[capo_datazone.types.delete_time_series_data_points_input.DeleteTimeSeriesDataPointsInput]",
        ) -> AsyncOperationResponse[
            "capo_datazone.types.delete_time_series_data_points_output.DeleteTimeSeriesDataPointsOutput"
        ]:
            import capo_datazone._operations.data_zone.delete_time_series_data_points

            (
                output,
                http_response,
            ) = await capo_datazone._operations.data_zone.delete_time_series_data_points.async_delete_time_series_data_points(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_datazone.types.delete_time_series_data_points_input.DeleteTimeSeriesDataPointsInput = {
            "domain_identifier": domain_identifier,
            "entity_identifier": entity_identifier,
            "entity_type": entity_type,
            "form_name": form_name,
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

    async def disassociate_environment_role(
        self,
        domain_identifier: "capo_datazone.types.domain_id.DomainId",
        environment_identifier: "capo_datazone.types.environment_id.EnvironmentId",
        environment_role_arn: str,
        *,
        config_overrides: Optional[AsyncDataZoneClientConfig] = None,
    ) -> "capo_datazone.types.disassociate_environment_role_output.DisassociateEnvironmentRoleOutput":
        """<p>Disassociates the environment role in Amazon DataZone.</p>

        Args:
            domain_identifier: <p>The ID of the Amazon DataZone domain in which an environment role is disassociated.</p>
            environment_identifier: <p>The ID of the environment.</p>
            environment_role_arn: <p>The ARN of the environment role.</p>

        Raises:
            capo_datazone.errors.access_denied_exception.AccessDeniedException: <p>You do not have sufficient access to perform this action.</p>
            capo_datazone.errors.throttling_exception.ThrottlingException: <p>The request was denied due to request throttling.</p>
            capo_datazone.errors.unauthorized_exception.UnauthorizedException: <p>You do not have permission to perform this action.</p>
            capo_datazone.errors.conflict_exception.ConflictException: <p>There is a conflict while performing this action.</p>
            capo_datazone.errors.internal_server_exception.InternalServerException: <p>The request has failed because of an unknown error, exception or failure.</p>
            capo_datazone.errors.resource_not_found_exception.ResourceNotFoundException: <p>The specified resource cannot be found.</p>
            capo_datazone.errors.validation_exception.ValidationException: <p>The input fails to satisfy the constraints specified by the Amazon Web Services service.</p>
            capo_datazone.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        async def _handler(
            req: "AsyncOperationRequest[capo_datazone.types.disassociate_environment_role_input.DisassociateEnvironmentRoleInput]",
        ) -> AsyncOperationResponse[
            "capo_datazone.types.disassociate_environment_role_output.DisassociateEnvironmentRoleOutput"
        ]:
            import capo_datazone._operations.data_zone.disassociate_environment_role

            (
                output,
                http_response,
            ) = await capo_datazone._operations.data_zone.disassociate_environment_role.async_disassociate_environment_role(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_datazone.types.disassociate_environment_role_input.DisassociateEnvironmentRoleInput = {
            "domain_identifier": domain_identifier,
            "environment_identifier": environment_identifier,
            "environment_role_arn": environment_role_arn,
        }

        response = await aexecute_pipeline(
            AsyncOperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        await response.response.aclose()
        return response.output

    async def disassociate_governed_terms(
        self,
        domain_identifier: "capo_datazone.types.domain_id.DomainId",
        entity_identifier: "capo_datazone.types.entity_identifier.EntityIdentifier",
        entity_type: "capo_datazone.types.governed_entity_type.GovernedEntityType",
        governed_glossary_terms: "capo_datazone.types.governed_glossary_terms.GovernedGlossaryTerms",
        *,
        config_overrides: Optional[AsyncDataZoneClientConfig] = None,
    ) -> "capo_datazone.types.disassociate_governed_terms_output.DisassociateGovernedTermsOutput":
        """<p>Disassociates restricted terms from an asset.</p>

        Args:
            domain_identifier: <p>The ID of the domain where you want to disassociate restricted terms from an asset.</p>
            entity_identifier: <p>The ID of an asset from which you want to disassociate restricted terms.</p>
            entity_type: <p>The type of the asset from which you want to disassociate restricted terms.</p>
            governed_glossary_terms: <p>The restricted glossary terms that you want to disassociate from an asset.</p>

        Raises:
            capo_datazone.errors.access_denied_exception.AccessDeniedException: <p>You do not have sufficient access to perform this action.</p>
            capo_datazone.errors.throttling_exception.ThrottlingException: <p>The request was denied due to request throttling.</p>
            capo_datazone.errors.unauthorized_exception.UnauthorizedException: <p>You do not have permission to perform this action.</p>
            capo_datazone.errors.conflict_exception.ConflictException: <p>There is a conflict while performing this action.</p>
            capo_datazone.errors.internal_server_exception.InternalServerException: <p>The request has failed because of an unknown error, exception or failure.</p>
            capo_datazone.errors.resource_not_found_exception.ResourceNotFoundException: <p>The specified resource cannot be found.</p>
            capo_datazone.errors.validation_exception.ValidationException: <p>The input fails to satisfy the constraints specified by the Amazon Web Services service.</p>
            capo_datazone.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        async def _handler(
            req: "AsyncOperationRequest[capo_datazone.types.disassociate_governed_terms_input.DisassociateGovernedTermsInput]",
        ) -> AsyncOperationResponse[
            "capo_datazone.types.disassociate_governed_terms_output.DisassociateGovernedTermsOutput"
        ]:
            import capo_datazone._operations.data_zone.disassociate_governed_terms

            (
                output,
                http_response,
            ) = await capo_datazone._operations.data_zone.disassociate_governed_terms.async_disassociate_governed_terms(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_datazone.types.disassociate_governed_terms_input.DisassociateGovernedTermsInput = {
            "domain_identifier": domain_identifier,
            "entity_identifier": entity_identifier,
            "entity_type": entity_type,
            "governed_glossary_terms": governed_glossary_terms,
        }

        response = await aexecute_pipeline(
            AsyncOperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        await response.response.aclose()
        return response.output

    async def get_account_pool(
        self,
        domain_identifier: "capo_datazone.types.domain_id.DomainId",
        identifier: "capo_datazone.types.account_pool_id.AccountPoolId",
        *,
        config_overrides: Optional[AsyncDataZoneClientConfig] = None,
    ) -> "capo_datazone.types.get_account_pool_output.GetAccountPoolOutput":
        """<p>Gets the details of the account pool.</p>

        Args:
            domain_identifier: <p>The ID of the domain in which the account pool lives whose details are to be displayed.</p>
            identifier: <p>The ID of the account pool whose details are to be displayed.</p>

        Raises:
            capo_datazone.errors.access_denied_exception.AccessDeniedException: <p>You do not have sufficient access to perform this action.</p>
            capo_datazone.errors.throttling_exception.ThrottlingException: <p>The request was denied due to request throttling.</p>
            capo_datazone.errors.unauthorized_exception.UnauthorizedException: <p>You do not have permission to perform this action.</p>
            capo_datazone.errors.internal_server_exception.InternalServerException: <p>The request has failed because of an unknown error, exception or failure.</p>
            capo_datazone.errors.resource_not_found_exception.ResourceNotFoundException: <p>The specified resource cannot be found.</p>
            capo_datazone.errors.validation_exception.ValidationException: <p>The input fails to satisfy the constraints specified by the Amazon Web Services service.</p>
            capo_datazone.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        async def _handler(
            req: "AsyncOperationRequest[capo_datazone.types.get_account_pool_input.GetAccountPoolInput]",
        ) -> AsyncOperationResponse[
            "capo_datazone.types.get_account_pool_output.GetAccountPoolOutput"
        ]:
            import capo_datazone._operations.data_zone.get_account_pool

            (
                output,
                http_response,
            ) = await capo_datazone._operations.data_zone.get_account_pool.async_get_account_pool(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_datazone.types.get_account_pool_input.GetAccountPoolInput = {
            "domain_identifier": domain_identifier,
            "identifier": identifier,
        }

        response = await aexecute_pipeline(
            AsyncOperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        await response.response.aclose()
        return response.output

    async def get_asset_filter(
        self,
        domain_identifier: "capo_datazone.types.domain_id.DomainId",
        asset_identifier: "capo_datazone.types.asset_id.AssetId",
        identifier: "capo_datazone.types.filter_id.FilterId",
        *,
        config_overrides: Optional[AsyncDataZoneClientConfig] = None,
    ) -> "capo_datazone.types.get_asset_filter_output.GetAssetFilterOutput":
        """<p>Gets an asset filter.</p> <p>Prerequisites:</p> <ul> <li> <p>Domain (<code>--domain-identifier</code>), asset (<code>--asset-identifier</code>), and filter (<code>--identifier</code>) must all exist. </p> </li> <li> <p>The asset filter should not have been deleted.</p> </li> <li> <p>The asset must still exist (since the filter is linked to it).</p> </li> </ul>

        Args:
            domain_identifier: <p>The ID of the domain where you want to get an asset filter.</p>
            asset_identifier: <p>The ID of the data asset.</p>
            identifier: <p>The ID of the asset filter.</p>

        Raises:
            capo_datazone.errors.access_denied_exception.AccessDeniedException: <p>You do not have sufficient access to perform this action.</p>
            capo_datazone.errors.throttling_exception.ThrottlingException: <p>The request was denied due to request throttling.</p>
            capo_datazone.errors.unauthorized_exception.UnauthorizedException: <p>You do not have permission to perform this action.</p>
            capo_datazone.errors.internal_server_exception.InternalServerException: <p>The request has failed because of an unknown error, exception or failure.</p>
            capo_datazone.errors.resource_not_found_exception.ResourceNotFoundException: <p>The specified resource cannot be found.</p>
            capo_datazone.errors.validation_exception.ValidationException: <p>The input fails to satisfy the constraints specified by the Amazon Web Services service.</p>
            capo_datazone.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        async def _handler(
            req: "AsyncOperationRequest[capo_datazone.types.get_asset_filter_input.GetAssetFilterInput]",
        ) -> AsyncOperationResponse[
            "capo_datazone.types.get_asset_filter_output.GetAssetFilterOutput"
        ]:
            import capo_datazone._operations.data_zone.get_asset_filter

            (
                output,
                http_response,
            ) = await capo_datazone._operations.data_zone.get_asset_filter.async_get_asset_filter(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_datazone.types.get_asset_filter_input.GetAssetFilterInput = {
            "domain_identifier": domain_identifier,
            "asset_identifier": asset_identifier,
            "identifier": identifier,
        }

        response = await aexecute_pipeline(
            AsyncOperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        await response.response.aclose()
        return response.output

    async def get_connection(
        self,
        domain_identifier: "capo_datazone.types.domain_id.DomainId",
        identifier: "capo_datazone.types.connection_id.ConnectionId",
        *,
        config_overrides: Optional[AsyncDataZoneClientConfig] = None,
        with_secret: Optional[bool] = None,
    ) -> "capo_datazone.types.get_connection_output.GetConnectionOutput":
        """<p>Gets a connection. In Amazon DataZone, a connection enables you to connect your resources (domains, projects, and environments) to external resources and services.</p>

        Args:
            domain_identifier: <p>The ID of the domain where we get the connection.</p>
            identifier: <p>The connection ID.</p>
            with_secret: <p>Specifies whether a connection has a secret.</p>

        Raises:
            capo_datazone.errors.access_denied_exception.AccessDeniedException: <p>You do not have sufficient access to perform this action.</p>
            capo_datazone.errors.throttling_exception.ThrottlingException: <p>The request was denied due to request throttling.</p>
            capo_datazone.errors.unauthorized_exception.UnauthorizedException: <p>You do not have permission to perform this action.</p>
            capo_datazone.errors.internal_server_exception.InternalServerException: <p>The request has failed because of an unknown error, exception or failure.</p>
            capo_datazone.errors.resource_not_found_exception.ResourceNotFoundException: <p>The specified resource cannot be found.</p>
            capo_datazone.errors.validation_exception.ValidationException: <p>The input fails to satisfy the constraints specified by the Amazon Web Services service.</p>
            capo_datazone.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        async def _handler(
            req: "AsyncOperationRequest[capo_datazone.types.get_connection_input.GetConnectionInput]",
        ) -> AsyncOperationResponse[
            "capo_datazone.types.get_connection_output.GetConnectionOutput"
        ]:
            import capo_datazone._operations.data_zone.get_connection

            (
                output,
                http_response,
            ) = await capo_datazone._operations.data_zone.get_connection.async_get_connection(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_datazone.types.get_connection_input.GetConnectionInput = {
            "domain_identifier": domain_identifier,
            "identifier": identifier,
        }
        if with_secret is not None:
            input_["with_secret"] = with_secret

        response = await aexecute_pipeline(
            AsyncOperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        await response.response.aclose()
        return response.output

    async def get_data_export_configuration(
        self,
        domain_identifier: "capo_datazone.types.domain_id.DomainId",
        *,
        config_overrides: Optional[AsyncDataZoneClientConfig] = None,
    ) -> "capo_datazone.types.get_data_export_configuration_output.GetDataExportConfigurationOutput":
        """<p>Gets data export configuration details.</p>

        Args:
            domain_identifier: <p>The ID of the domain where you want to get the data export configuration details.</p>

        Raises:
            capo_datazone.errors.access_denied_exception.AccessDeniedException: <p>You do not have sufficient access to perform this action.</p>
            capo_datazone.errors.throttling_exception.ThrottlingException: <p>The request was denied due to request throttling.</p>
            capo_datazone.errors.unauthorized_exception.UnauthorizedException: <p>You do not have permission to perform this action.</p>
            capo_datazone.errors.internal_server_exception.InternalServerException: <p>The request has failed because of an unknown error, exception or failure.</p>
            capo_datazone.errors.resource_not_found_exception.ResourceNotFoundException: <p>The specified resource cannot be found.</p>
            capo_datazone.errors.validation_exception.ValidationException: <p>The input fails to satisfy the constraints specified by the Amazon Web Services service.</p>
            capo_datazone.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        async def _handler(
            req: "AsyncOperationRequest[capo_datazone.types.get_data_export_configuration_input.GetDataExportConfigurationInput]",
        ) -> AsyncOperationResponse[
            "capo_datazone.types.get_data_export_configuration_output.GetDataExportConfigurationOutput"
        ]:
            import capo_datazone._operations.data_zone.get_data_export_configuration

            (
                output,
                http_response,
            ) = await capo_datazone._operations.data_zone.get_data_export_configuration.async_get_data_export_configuration(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_datazone.types.get_data_export_configuration_input.GetDataExportConfigurationInput = {
            "domain_identifier": domain_identifier
        }

        response = await aexecute_pipeline(
            AsyncOperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        await response.response.aclose()
        return response.output

    async def get_environment(
        self,
        domain_identifier: "capo_datazone.types.domain_id.DomainId",
        identifier: "capo_datazone.types.environment_id.EnvironmentId",
        *,
        config_overrides: Optional[AsyncDataZoneClientConfig] = None,
    ) -> "capo_datazone.types.get_environment_output.GetEnvironmentOutput":
        """<p>Gets an Amazon DataZone environment.</p>

        Args:
            domain_identifier: <p>The ID of the Amazon DataZone domain where the environment exists.</p>
            identifier: <p>The ID of the Amazon DataZone environment.</p>

        Raises:
            capo_datazone.errors.access_denied_exception.AccessDeniedException: <p>You do not have sufficient access to perform this action.</p>
            capo_datazone.errors.throttling_exception.ThrottlingException: <p>The request was denied due to request throttling.</p>
            capo_datazone.errors.unauthorized_exception.UnauthorizedException: <p>You do not have permission to perform this action.</p>
            capo_datazone.errors.internal_server_exception.InternalServerException: <p>The request has failed because of an unknown error, exception or failure.</p>
            capo_datazone.errors.resource_not_found_exception.ResourceNotFoundException: <p>The specified resource cannot be found.</p>
            capo_datazone.errors.validation_exception.ValidationException: <p>The input fails to satisfy the constraints specified by the Amazon Web Services service.</p>
            capo_datazone.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        async def _handler(
            req: "AsyncOperationRequest[capo_datazone.types.get_environment_input.GetEnvironmentInput]",
        ) -> AsyncOperationResponse[
            "capo_datazone.types.get_environment_output.GetEnvironmentOutput"
        ]:
            import capo_datazone._operations.data_zone.get_environment

            (
                output,
                http_response,
            ) = await capo_datazone._operations.data_zone.get_environment.async_get_environment(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_datazone.types.get_environment_input.GetEnvironmentInput = {
            "domain_identifier": domain_identifier,
            "identifier": identifier,
        }

        response = await aexecute_pipeline(
            AsyncOperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        await response.response.aclose()
        return response.output

    async def get_environment_action(
        self,
        domain_identifier: "capo_datazone.types.domain_id.DomainId",
        environment_identifier: "capo_datazone.types.environment_id.EnvironmentId",
        identifier: str,
        *,
        config_overrides: Optional[AsyncDataZoneClientConfig] = None,
    ) -> "capo_datazone.types.get_environment_action_output.GetEnvironmentActionOutput":
        """<p>Gets the specified environment action.</p>

        Args:
            domain_identifier: <p>The ID of the Amazon DataZone domain in which the <code>GetEnvironmentAction</code> API is invoked. </p>
            environment_identifier: <p>The environment ID of the environment action.</p>
            identifier: <p>The ID of the environment action</p>

        Raises:
            capo_datazone.errors.access_denied_exception.AccessDeniedException: <p>You do not have sufficient access to perform this action.</p>
            capo_datazone.errors.throttling_exception.ThrottlingException: <p>The request was denied due to request throttling.</p>
            capo_datazone.errors.unauthorized_exception.UnauthorizedException: <p>You do not have permission to perform this action.</p>
            capo_datazone.errors.internal_server_exception.InternalServerException: <p>The request has failed because of an unknown error, exception or failure.</p>
            capo_datazone.errors.resource_not_found_exception.ResourceNotFoundException: <p>The specified resource cannot be found.</p>
            capo_datazone.errors.validation_exception.ValidationException: <p>The input fails to satisfy the constraints specified by the Amazon Web Services service.</p>
            capo_datazone.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        async def _handler(
            req: "AsyncOperationRequest[capo_datazone.types.get_environment_action_input.GetEnvironmentActionInput]",
        ) -> AsyncOperationResponse[
            "capo_datazone.types.get_environment_action_output.GetEnvironmentActionOutput"
        ]:
            import capo_datazone._operations.data_zone.get_environment_action

            (
                output,
                http_response,
            ) = await capo_datazone._operations.data_zone.get_environment_action.async_get_environment_action(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_datazone.types.get_environment_action_input.GetEnvironmentActionInput = {
            "domain_identifier": domain_identifier,
            "environment_identifier": environment_identifier,
            "identifier": identifier,
        }

        response = await aexecute_pipeline(
            AsyncOperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        await response.response.aclose()
        return response.output

    async def get_environment_blueprint(
        self,
        domain_identifier: "capo_datazone.types.domain_id.DomainId",
        identifier: "capo_datazone.types.environment_blueprint_id.EnvironmentBlueprintId",
        *,
        config_overrides: Optional[AsyncDataZoneClientConfig] = None,
    ) -> "capo_datazone.types.get_environment_blueprint_output.GetEnvironmentBlueprintOutput":
        """<p>Gets an Amazon DataZone blueprint.</p>

        Args:
            domain_identifier: <p>The identifier of the domain in which this blueprint exists.</p>
            identifier: <p>The ID of this Amazon DataZone blueprint.</p>

        Raises:
            capo_datazone.errors.access_denied_exception.AccessDeniedException: <p>You do not have sufficient access to perform this action.</p>
            capo_datazone.errors.throttling_exception.ThrottlingException: <p>The request was denied due to request throttling.</p>
            capo_datazone.errors.unauthorized_exception.UnauthorizedException: <p>You do not have permission to perform this action.</p>
            capo_datazone.errors.internal_server_exception.InternalServerException: <p>The request has failed because of an unknown error, exception or failure.</p>
            capo_datazone.errors.resource_not_found_exception.ResourceNotFoundException: <p>The specified resource cannot be found.</p>
            capo_datazone.errors.validation_exception.ValidationException: <p>The input fails to satisfy the constraints specified by the Amazon Web Services service.</p>
            capo_datazone.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        async def _handler(
            req: "AsyncOperationRequest[capo_datazone.types.get_environment_blueprint_input.GetEnvironmentBlueprintInput]",
        ) -> AsyncOperationResponse[
            "capo_datazone.types.get_environment_blueprint_output.GetEnvironmentBlueprintOutput"
        ]:
            import capo_datazone._operations.data_zone.get_environment_blueprint

            (
                output,
                http_response,
            ) = await capo_datazone._operations.data_zone.get_environment_blueprint.async_get_environment_blueprint(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_datazone.types.get_environment_blueprint_input.GetEnvironmentBlueprintInput = {
            "domain_identifier": domain_identifier,
            "identifier": identifier,
        }

        response = await aexecute_pipeline(
            AsyncOperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        await response.response.aclose()
        return response.output

    async def get_environment_credentials(
        self,
        domain_identifier: "capo_datazone.types.domain_id.DomainId",
        environment_identifier: "capo_datazone.types.environment_id.EnvironmentId",
        *,
        config_overrides: Optional[AsyncDataZoneClientConfig] = None,
    ) -> "capo_datazone.types.get_environment_credentials_output.GetEnvironmentCredentialsOutput":
        """<p>Gets the credentials of an environment in Amazon DataZone.</p>

        Args:
            domain_identifier: <p>The ID of the Amazon DataZone domain in which this environment and its credentials exist.</p>
            environment_identifier: <p>The ID of the environment whose credentials this operation gets.</p>

        Raises:
            capo_datazone.errors.access_denied_exception.AccessDeniedException: <p>You do not have sufficient access to perform this action.</p>
            capo_datazone.errors.throttling_exception.ThrottlingException: <p>The request was denied due to request throttling.</p>
            capo_datazone.errors.unauthorized_exception.UnauthorizedException: <p>You do not have permission to perform this action.</p>
            capo_datazone.errors.internal_server_exception.InternalServerException: <p>The request has failed because of an unknown error, exception or failure.</p>
            capo_datazone.errors.resource_not_found_exception.ResourceNotFoundException: <p>The specified resource cannot be found.</p>
            capo_datazone.errors.validation_exception.ValidationException: <p>The input fails to satisfy the constraints specified by the Amazon Web Services service.</p>
            capo_datazone.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        async def _handler(
            req: "AsyncOperationRequest[capo_datazone.types.get_environment_credentials_input.GetEnvironmentCredentialsInput]",
        ) -> AsyncOperationResponse[
            "capo_datazone.types.get_environment_credentials_output.GetEnvironmentCredentialsOutput"
        ]:
            import capo_datazone._operations.data_zone.get_environment_credentials

            (
                output,
                http_response,
            ) = await capo_datazone._operations.data_zone.get_environment_credentials.async_get_environment_credentials(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_datazone.types.get_environment_credentials_input.GetEnvironmentCredentialsInput = {
            "domain_identifier": domain_identifier,
            "environment_identifier": environment_identifier,
        }

        response = await aexecute_pipeline(
            AsyncOperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        await response.response.aclose()
        return response.output

    async def get_environment_profile(
        self,
        domain_identifier: "capo_datazone.types.domain_id.DomainId",
        identifier: "capo_datazone.types.environment_profile_id.EnvironmentProfileId",
        *,
        config_overrides: Optional[AsyncDataZoneClientConfig] = None,
    ) -> (
        "capo_datazone.types.get_environment_profile_output.GetEnvironmentProfileOutput"
    ):
        """<p>Gets an evinronment profile in Amazon DataZone.</p>

        Args:
            domain_identifier: <p>The ID of the Amazon DataZone domain in which this environment profile exists.</p>
            identifier: <p>The ID of the environment profile.</p>

        Raises:
            capo_datazone.errors.access_denied_exception.AccessDeniedException: <p>You do not have sufficient access to perform this action.</p>
            capo_datazone.errors.throttling_exception.ThrottlingException: <p>The request was denied due to request throttling.</p>
            capo_datazone.errors.unauthorized_exception.UnauthorizedException: <p>You do not have permission to perform this action.</p>
            capo_datazone.errors.internal_server_exception.InternalServerException: <p>The request has failed because of an unknown error, exception or failure.</p>
            capo_datazone.errors.resource_not_found_exception.ResourceNotFoundException: <p>The specified resource cannot be found.</p>
            capo_datazone.errors.validation_exception.ValidationException: <p>The input fails to satisfy the constraints specified by the Amazon Web Services service.</p>
            capo_datazone.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        async def _handler(
            req: "AsyncOperationRequest[capo_datazone.types.get_environment_profile_input.GetEnvironmentProfileInput]",
        ) -> AsyncOperationResponse[
            "capo_datazone.types.get_environment_profile_output.GetEnvironmentProfileOutput"
        ]:
            import capo_datazone._operations.data_zone.get_environment_profile

            (
                output,
                http_response,
            ) = await capo_datazone._operations.data_zone.get_environment_profile.async_get_environment_profile(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_datazone.types.get_environment_profile_input.GetEnvironmentProfileInput = {
            "domain_identifier": domain_identifier,
            "identifier": identifier,
        }

        response = await aexecute_pipeline(
            AsyncOperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        await response.response.aclose()
        return response.output

    async def get_group_profile(
        self,
        domain_identifier: "capo_datazone.types.domain_id.DomainId",
        group_identifier: "capo_datazone.types.group_identifier.GroupIdentifier",
        *,
        config_overrides: Optional[AsyncDataZoneClientConfig] = None,
    ) -> "capo_datazone.types.get_group_profile_output.GetGroupProfileOutput":
        """<p>Gets a group profile in Amazon DataZone.</p>

        Args:
            domain_identifier: <p>The identifier of the Amazon DataZone domain in which the group profile exists.</p>
            group_identifier: <p>The identifier of the group profile.</p>

        Raises:
            capo_datazone.errors.access_denied_exception.AccessDeniedException: <p>You do not have sufficient access to perform this action.</p>
            capo_datazone.errors.throttling_exception.ThrottlingException: <p>The request was denied due to request throttling.</p>
            capo_datazone.errors.unauthorized_exception.UnauthorizedException: <p>You do not have permission to perform this action.</p>
            capo_datazone.errors.internal_server_exception.InternalServerException: <p>The request has failed because of an unknown error, exception or failure.</p>
            capo_datazone.errors.resource_not_found_exception.ResourceNotFoundException: <p>The specified resource cannot be found.</p>
            capo_datazone.errors.validation_exception.ValidationException: <p>The input fails to satisfy the constraints specified by the Amazon Web Services service.</p>
            capo_datazone.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        async def _handler(
            req: "AsyncOperationRequest[capo_datazone.types.get_group_profile_input.GetGroupProfileInput]",
        ) -> AsyncOperationResponse[
            "capo_datazone.types.get_group_profile_output.GetGroupProfileOutput"
        ]:
            import capo_datazone._operations.data_zone.get_group_profile

            (
                output,
                http_response,
            ) = await capo_datazone._operations.data_zone.get_group_profile.async_get_group_profile(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_datazone.types.get_group_profile_input.GetGroupProfileInput = {
            "domain_identifier": domain_identifier,
            "group_identifier": group_identifier,
        }

        response = await aexecute_pipeline(
            AsyncOperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        await response.response.aclose()
        return response.output

    async def get_iam_portal_login_url(
        self,
        domain_identifier: "capo_datazone.types.domain_id.DomainId",
        *,
        config_overrides: Optional[AsyncDataZoneClientConfig] = None,
    ) -> (
        "capo_datazone.types.get_iam_portal_login_url_output.GetIamPortalLoginUrlOutput"
    ):
        """<p>Gets the data portal URL for the specified Amazon DataZone domain.</p>

        Args:
            domain_identifier: <p>the ID of the Amazon DataZone domain the data portal of which you want to get.</p>

        Raises:
            capo_datazone.errors.access_denied_exception.AccessDeniedException: <p>You do not have sufficient access to perform this action.</p>
            capo_datazone.errors.throttling_exception.ThrottlingException: <p>The request was denied due to request throttling.</p>
            capo_datazone.errors.unauthorized_exception.UnauthorizedException: <p>You do not have permission to perform this action.</p>
            capo_datazone.errors.conflict_exception.ConflictException: <p>There is a conflict while performing this action.</p>
            capo_datazone.errors.internal_server_exception.InternalServerException: <p>The request has failed because of an unknown error, exception or failure.</p>
            capo_datazone.errors.resource_not_found_exception.ResourceNotFoundException: <p>The specified resource cannot be found.</p>
            capo_datazone.errors.validation_exception.ValidationException: <p>The input fails to satisfy the constraints specified by the Amazon Web Services service.</p>
            capo_datazone.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        async def _handler(
            req: "AsyncOperationRequest[capo_datazone.types.get_iam_portal_login_url_input.GetIamPortalLoginUrlInput]",
        ) -> AsyncOperationResponse[
            "capo_datazone.types.get_iam_portal_login_url_output.GetIamPortalLoginUrlOutput"
        ]:
            import capo_datazone._operations.data_zone.get_iam_portal_login_url

            (
                output,
                http_response,
            ) = await capo_datazone._operations.data_zone.get_iam_portal_login_url.async_get_iam_portal_login_url(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_datazone.types.get_iam_portal_login_url_input.GetIamPortalLoginUrlInput = {
            "domain_identifier": domain_identifier
        }

        response = await aexecute_pipeline(
            AsyncOperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        await response.response.aclose()
        return response.output

    async def get_job_run(
        self,
        domain_identifier: "capo_datazone.types.domain_id.DomainId",
        identifier: "capo_datazone.types.run_identifier.RunIdentifier",
        *,
        config_overrides: Optional[AsyncDataZoneClientConfig] = None,
    ) -> "capo_datazone.types.get_job_run_output.GetJobRunOutput":
        """<p>The details of the job run.</p>

        Args:
            domain_identifier: <p>The ID of the domain.</p>
            identifier: <p>The ID of the job run.</p>

        Raises:
            capo_datazone.errors.access_denied_exception.AccessDeniedException: <p>You do not have sufficient access to perform this action.</p>
            capo_datazone.errors.throttling_exception.ThrottlingException: <p>The request was denied due to request throttling.</p>
            capo_datazone.errors.unauthorized_exception.UnauthorizedException: <p>You do not have permission to perform this action.</p>
            capo_datazone.errors.internal_server_exception.InternalServerException: <p>The request has failed because of an unknown error, exception or failure.</p>
            capo_datazone.errors.resource_not_found_exception.ResourceNotFoundException: <p>The specified resource cannot be found.</p>
            capo_datazone.errors.validation_exception.ValidationException: <p>The input fails to satisfy the constraints specified by the Amazon Web Services service.</p>
            capo_datazone.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        async def _handler(
            req: "AsyncOperationRequest[capo_datazone.types.get_job_run_input.GetJobRunInput]",
        ) -> AsyncOperationResponse[
            "capo_datazone.types.get_job_run_output.GetJobRunOutput"
        ]:
            import capo_datazone._operations.data_zone.get_job_run

            (
                output,
                http_response,
            ) = await capo_datazone._operations.data_zone.get_job_run.async_get_job_run(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_datazone.types.get_job_run_input.GetJobRunInput = {
            "domain_identifier": domain_identifier,
            "identifier": identifier,
        }

        response = await aexecute_pipeline(
            AsyncOperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        await response.response.aclose()
        return response.output

    async def get_lineage_event(
        self,
        domain_identifier: "capo_datazone.types.domain_id.DomainId",
        identifier: "capo_datazone.types.lineage_event_identifier.LineageEventIdentifier",
        *,
        config_overrides: Optional[AsyncDataZoneClientConfig] = None,
    ) -> "capo_datazone.types.get_lineage_event_output.GetLineageEventOutput":
        """<p>Describes the lineage event.</p>

        Args:
            domain_identifier: <p>The ID of the domain.</p>
            identifier: <p>The ID of the lineage event.</p>

        Raises:
            capo_datazone.errors.access_denied_exception.AccessDeniedException: <p>You do not have sufficient access to perform this action.</p>
            capo_datazone.errors.throttling_exception.ThrottlingException: <p>The request was denied due to request throttling.</p>
            capo_datazone.errors.unauthorized_exception.UnauthorizedException: <p>You do not have permission to perform this action.</p>
            capo_datazone.errors.internal_server_exception.InternalServerException: <p>The request has failed because of an unknown error, exception or failure.</p>
            capo_datazone.errors.resource_not_found_exception.ResourceNotFoundException: <p>The specified resource cannot be found.</p>
            capo_datazone.errors.validation_exception.ValidationException: <p>The input fails to satisfy the constraints specified by the Amazon Web Services service.</p>
            capo_datazone.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        async def _handler(
            req: "AsyncOperationRequest[capo_datazone.types.get_lineage_event_input.GetLineageEventInput]",
        ) -> AsyncOperationResponse[
            "capo_datazone.types.get_lineage_event_output.GetLineageEventOutput"
        ]:
            import capo_datazone._operations.data_zone.get_lineage_event

            (
                output,
                http_response,
            ) = await capo_datazone._operations.data_zone.get_lineage_event.async_get_lineage_event(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_datazone.types.get_lineage_event_input.GetLineageEventInput = {
            "domain_identifier": domain_identifier,
            "identifier": identifier,
        }

        response = await aexecute_pipeline(
            AsyncOperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        await response.response.aclose()
        return response.output

    async def get_lineage_node(
        self,
        domain_identifier: "capo_datazone.types.domain_id.DomainId",
        identifier: "capo_datazone.types.lineage_node_identifier.LineageNodeIdentifier",
        *,
        config_overrides: Optional[AsyncDataZoneClientConfig] = None,
        event_timestamp: Optional[datetime.datetime] = None,
    ) -> "capo_datazone.types.get_lineage_node_output.GetLineageNodeOutput":
        """<p>Gets the data lineage node.</p>

        Args:
            domain_identifier: <p>The ID of the domain in which you want to get the data lineage node.</p>
            identifier: <p>The ID of the data lineage node that you want to get.</p> <p>Both, a lineage node identifier generated by Amazon DataZone and a <code>sourceIdentifier</code> of the lineage node are supported. If <code>sourceIdentifier</code> is greater than 1800 characters, you can use lineage node identifier generated by Amazon DataZone to get the node details.</p>
            event_timestamp: <p>The event time stamp for which you want to get the data lineage node.</p>

        Raises:
            capo_datazone.errors.access_denied_exception.AccessDeniedException: <p>You do not have sufficient access to perform this action.</p>
            capo_datazone.errors.throttling_exception.ThrottlingException: <p>The request was denied due to request throttling.</p>
            capo_datazone.errors.unauthorized_exception.UnauthorizedException: <p>You do not have permission to perform this action.</p>
            capo_datazone.errors.internal_server_exception.InternalServerException: <p>The request has failed because of an unknown error, exception or failure.</p>
            capo_datazone.errors.resource_not_found_exception.ResourceNotFoundException: <p>The specified resource cannot be found.</p>
            capo_datazone.errors.validation_exception.ValidationException: <p>The input fails to satisfy the constraints specified by the Amazon Web Services service.</p>
            capo_datazone.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        async def _handler(
            req: "AsyncOperationRequest[capo_datazone.types.get_lineage_node_input.GetLineageNodeInput]",
        ) -> AsyncOperationResponse[
            "capo_datazone.types.get_lineage_node_output.GetLineageNodeOutput"
        ]:
            import capo_datazone._operations.data_zone.get_lineage_node

            (
                output,
                http_response,
            ) = await capo_datazone._operations.data_zone.get_lineage_node.async_get_lineage_node(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_datazone.types.get_lineage_node_input.GetLineageNodeInput = {
            "domain_identifier": domain_identifier,
            "identifier": identifier,
        }
        if event_timestamp is not None:
            input_["event_timestamp"] = event_timestamp

        response = await aexecute_pipeline(
            AsyncOperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        await response.response.aclose()
        return response.output

    async def get_project(
        self,
        domain_identifier: "capo_datazone.types.domain_id.DomainId",
        identifier: "capo_datazone.types.project_id.ProjectId",
        *,
        config_overrides: Optional[AsyncDataZoneClientConfig] = None,
    ) -> "capo_datazone.types.get_project_output.GetProjectOutput":
        """<p>Gets a project in Amazon DataZone.</p>

        Args:
            domain_identifier: <p>The ID of the Amazon DataZone domain in which the project exists.</p>
            identifier: <p>The ID of the project.</p>

        Raises:
            capo_datazone.errors.access_denied_exception.AccessDeniedException: <p>You do not have sufficient access to perform this action.</p>
            capo_datazone.errors.throttling_exception.ThrottlingException: <p>The request was denied due to request throttling.</p>
            capo_datazone.errors.unauthorized_exception.UnauthorizedException: <p>You do not have permission to perform this action.</p>
            capo_datazone.errors.internal_server_exception.InternalServerException: <p>The request has failed because of an unknown error, exception or failure.</p>
            capo_datazone.errors.resource_not_found_exception.ResourceNotFoundException: <p>The specified resource cannot be found.</p>
            capo_datazone.errors.validation_exception.ValidationException: <p>The input fails to satisfy the constraints specified by the Amazon Web Services service.</p>
            capo_datazone.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        async def _handler(
            req: "AsyncOperationRequest[capo_datazone.types.get_project_input.GetProjectInput]",
        ) -> AsyncOperationResponse[
            "capo_datazone.types.get_project_output.GetProjectOutput"
        ]:
            import capo_datazone._operations.data_zone.get_project

            (
                output,
                http_response,
            ) = await capo_datazone._operations.data_zone.get_project.async_get_project(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_datazone.types.get_project_input.GetProjectInput = {
            "domain_identifier": domain_identifier,
            "identifier": identifier,
        }

        response = await aexecute_pipeline(
            AsyncOperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        await response.response.aclose()
        return response.output

    async def get_project_profile(
        self,
        domain_identifier: "capo_datazone.types.domain_id.DomainId",
        identifier: "capo_datazone.types.project_profile_id.ProjectProfileId",
        *,
        config_overrides: Optional[AsyncDataZoneClientConfig] = None,
    ) -> "capo_datazone.types.get_project_profile_output.GetProjectProfileOutput":
        """<p>The details of the project profile.</p>

        Args:
            domain_identifier: <p>The ID of the domain.</p>
            identifier: <p>The ID of the project profile.</p>

        Raises:
            capo_datazone.errors.access_denied_exception.AccessDeniedException: <p>You do not have sufficient access to perform this action.</p>
            capo_datazone.errors.throttling_exception.ThrottlingException: <p>The request was denied due to request throttling.</p>
            capo_datazone.errors.unauthorized_exception.UnauthorizedException: <p>You do not have permission to perform this action.</p>
            capo_datazone.errors.internal_server_exception.InternalServerException: <p>The request has failed because of an unknown error, exception or failure.</p>
            capo_datazone.errors.resource_not_found_exception.ResourceNotFoundException: <p>The specified resource cannot be found.</p>
            capo_datazone.errors.validation_exception.ValidationException: <p>The input fails to satisfy the constraints specified by the Amazon Web Services service.</p>
            capo_datazone.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        async def _handler(
            req: "AsyncOperationRequest[capo_datazone.types.get_project_profile_input.GetProjectProfileInput]",
        ) -> AsyncOperationResponse[
            "capo_datazone.types.get_project_profile_output.GetProjectProfileOutput"
        ]:
            import capo_datazone._operations.data_zone.get_project_profile

            (
                output,
                http_response,
            ) = await capo_datazone._operations.data_zone.get_project_profile.async_get_project_profile(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_datazone.types.get_project_profile_input.GetProjectProfileInput = {
            "domain_identifier": domain_identifier,
            "identifier": identifier,
        }

        response = await aexecute_pipeline(
            AsyncOperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        await response.response.aclose()
        return response.output

    async def get_subscription(
        self,
        domain_identifier: "capo_datazone.types.domain_id.DomainId",
        identifier: "capo_datazone.types.subscription_id.SubscriptionId",
        *,
        config_overrides: Optional[AsyncDataZoneClientConfig] = None,
    ) -> "capo_datazone.types.get_subscription_output.GetSubscriptionOutput":
        """<p>Gets a subscription in Amazon DataZone.</p>

        Args:
            domain_identifier: <p>The ID of the Amazon DataZone domain in which the subscription exists.</p>
            identifier: <p>The ID of the subscription.</p>

        Raises:
            capo_datazone.errors.access_denied_exception.AccessDeniedException: <p>You do not have sufficient access to perform this action.</p>
            capo_datazone.errors.throttling_exception.ThrottlingException: <p>The request was denied due to request throttling.</p>
            capo_datazone.errors.unauthorized_exception.UnauthorizedException: <p>You do not have permission to perform this action.</p>
            capo_datazone.errors.internal_server_exception.InternalServerException: <p>The request has failed because of an unknown error, exception or failure.</p>
            capo_datazone.errors.resource_not_found_exception.ResourceNotFoundException: <p>The specified resource cannot be found.</p>
            capo_datazone.errors.validation_exception.ValidationException: <p>The input fails to satisfy the constraints specified by the Amazon Web Services service.</p>
            capo_datazone.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        async def _handler(
            req: "AsyncOperationRequest[capo_datazone.types.get_subscription_input.GetSubscriptionInput]",
        ) -> AsyncOperationResponse[
            "capo_datazone.types.get_subscription_output.GetSubscriptionOutput"
        ]:
            import capo_datazone._operations.data_zone.get_subscription

            (
                output,
                http_response,
            ) = await capo_datazone._operations.data_zone.get_subscription.async_get_subscription(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_datazone.types.get_subscription_input.GetSubscriptionInput = {
            "domain_identifier": domain_identifier,
            "identifier": identifier,
        }

        response = await aexecute_pipeline(
            AsyncOperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        await response.response.aclose()
        return response.output

    async def get_subscription_grant(
        self,
        domain_identifier: "capo_datazone.types.domain_id.DomainId",
        identifier: "capo_datazone.types.subscription_grant_id.SubscriptionGrantId",
        *,
        config_overrides: Optional[AsyncDataZoneClientConfig] = None,
    ) -> "capo_datazone.types.get_subscription_grant_output.GetSubscriptionGrantOutput":
        """<p>Gets the subscription grant in Amazon DataZone.</p>

        Args:
            domain_identifier: <p>The ID of the Amazon DataZone domain in which the subscription grant exists.</p>
            identifier: <p>The ID of the subscription grant.</p>

        Raises:
            capo_datazone.errors.access_denied_exception.AccessDeniedException: <p>You do not have sufficient access to perform this action.</p>
            capo_datazone.errors.throttling_exception.ThrottlingException: <p>The request was denied due to request throttling.</p>
            capo_datazone.errors.unauthorized_exception.UnauthorizedException: <p>You do not have permission to perform this action.</p>
            capo_datazone.errors.internal_server_exception.InternalServerException: <p>The request has failed because of an unknown error, exception or failure.</p>
            capo_datazone.errors.resource_not_found_exception.ResourceNotFoundException: <p>The specified resource cannot be found.</p>
            capo_datazone.errors.validation_exception.ValidationException: <p>The input fails to satisfy the constraints specified by the Amazon Web Services service.</p>
            capo_datazone.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        async def _handler(
            req: "AsyncOperationRequest[capo_datazone.types.get_subscription_grant_input.GetSubscriptionGrantInput]",
        ) -> AsyncOperationResponse[
            "capo_datazone.types.get_subscription_grant_output.GetSubscriptionGrantOutput"
        ]:
            import capo_datazone._operations.data_zone.get_subscription_grant

            (
                output,
                http_response,
            ) = await capo_datazone._operations.data_zone.get_subscription_grant.async_get_subscription_grant(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_datazone.types.get_subscription_grant_input.GetSubscriptionGrantInput = {
            "domain_identifier": domain_identifier,
            "identifier": identifier,
        }

        response = await aexecute_pipeline(
            AsyncOperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        await response.response.aclose()
        return response.output

    async def get_subscription_request_details(
        self,
        domain_identifier: "capo_datazone.types.domain_id.DomainId",
        identifier: "capo_datazone.types.subscription_request_id.SubscriptionRequestId",
        *,
        config_overrides: Optional[AsyncDataZoneClientConfig] = None,
    ) -> "capo_datazone.types.get_subscription_request_details_output.GetSubscriptionRequestDetailsOutput":
        """<p>Gets the details of the specified subscription request.</p>

        Args:
            domain_identifier: <p>The identifier of the Amazon DataZone domain in which to get the subscription request details.</p>
            identifier: <p>The identifier of the subscription request the details of which to get.</p>

        Raises:
            capo_datazone.errors.access_denied_exception.AccessDeniedException: <p>You do not have sufficient access to perform this action.</p>
            capo_datazone.errors.throttling_exception.ThrottlingException: <p>The request was denied due to request throttling.</p>
            capo_datazone.errors.unauthorized_exception.UnauthorizedException: <p>You do not have permission to perform this action.</p>
            capo_datazone.errors.internal_server_exception.InternalServerException: <p>The request has failed because of an unknown error, exception or failure.</p>
            capo_datazone.errors.resource_not_found_exception.ResourceNotFoundException: <p>The specified resource cannot be found.</p>
            capo_datazone.errors.validation_exception.ValidationException: <p>The input fails to satisfy the constraints specified by the Amazon Web Services service.</p>
            capo_datazone.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        async def _handler(
            req: "AsyncOperationRequest[capo_datazone.types.get_subscription_request_details_input.GetSubscriptionRequestDetailsInput]",
        ) -> AsyncOperationResponse[
            "capo_datazone.types.get_subscription_request_details_output.GetSubscriptionRequestDetailsOutput"
        ]:
            import capo_datazone._operations.data_zone.get_subscription_request_details

            (
                output,
                http_response,
            ) = await capo_datazone._operations.data_zone.get_subscription_request_details.async_get_subscription_request_details(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_datazone.types.get_subscription_request_details_input.GetSubscriptionRequestDetailsInput = {
            "domain_identifier": domain_identifier,
            "identifier": identifier,
        }

        response = await aexecute_pipeline(
            AsyncOperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        await response.response.aclose()
        return response.output

    async def get_subscription_target(
        self,
        domain_identifier: "capo_datazone.types.domain_id.DomainId",
        environment_identifier: "capo_datazone.types.environment_id.EnvironmentId",
        identifier: "capo_datazone.types.subscription_target_id.SubscriptionTargetId",
        *,
        config_overrides: Optional[AsyncDataZoneClientConfig] = None,
    ) -> (
        "capo_datazone.types.get_subscription_target_output.GetSubscriptionTargetOutput"
    ):
        """<p>Gets the subscription target in Amazon DataZone.</p>

        Args:
            domain_identifier: <p>The ID of the Amazon DataZone domain in which the subscription target exists.</p>
            environment_identifier: <p>The ID of the environment associated with the subscription target.</p>
            identifier: <p>The ID of the subscription target.</p>

        Raises:
            capo_datazone.errors.access_denied_exception.AccessDeniedException: <p>You do not have sufficient access to perform this action.</p>
            capo_datazone.errors.throttling_exception.ThrottlingException: <p>The request was denied due to request throttling.</p>
            capo_datazone.errors.unauthorized_exception.UnauthorizedException: <p>You do not have permission to perform this action.</p>
            capo_datazone.errors.internal_server_exception.InternalServerException: <p>The request has failed because of an unknown error, exception or failure.</p>
            capo_datazone.errors.resource_not_found_exception.ResourceNotFoundException: <p>The specified resource cannot be found.</p>
            capo_datazone.errors.validation_exception.ValidationException: <p>The input fails to satisfy the constraints specified by the Amazon Web Services service.</p>
            capo_datazone.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        async def _handler(
            req: "AsyncOperationRequest[capo_datazone.types.get_subscription_target_input.GetSubscriptionTargetInput]",
        ) -> AsyncOperationResponse[
            "capo_datazone.types.get_subscription_target_output.GetSubscriptionTargetOutput"
        ]:
            import capo_datazone._operations.data_zone.get_subscription_target

            (
                output,
                http_response,
            ) = await capo_datazone._operations.data_zone.get_subscription_target.async_get_subscription_target(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_datazone.types.get_subscription_target_input.GetSubscriptionTargetInput = {
            "domain_identifier": domain_identifier,
            "environment_identifier": environment_identifier,
            "identifier": identifier,
        }

        response = await aexecute_pipeline(
            AsyncOperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        await response.response.aclose()
        return response.output

    async def get_time_series_data_point(
        self,
        domain_identifier: "capo_datazone.types.domain_id.DomainId",
        entity_identifier: "capo_datazone.types.entity_identifier.EntityIdentifier",
        entity_type: "capo_datazone.types.time_series_entity_type.TimeSeriesEntityType",
        identifier: "capo_datazone.types.time_series_data_point_identifier.TimeSeriesDataPointIdentifier",
        form_name: "capo_datazone.types.time_series_form_name.TimeSeriesFormName",
        *,
        config_overrides: Optional[AsyncDataZoneClientConfig] = None,
    ) -> "capo_datazone.types.get_time_series_data_point_output.GetTimeSeriesDataPointOutput":
        """<p>Gets the existing data point for the asset.</p>

        Args:
            domain_identifier: <p>The ID of the Amazon DataZone domain that houses the asset for which you want to get the data point.</p>
            entity_identifier: <p>The ID of the asset for which you want to get the data point.</p>
            entity_type: <p>The type of the asset for which you want to get the data point.</p>
            identifier: <p>The ID of the data point that you want to get.</p>
            form_name: <p>The name of the time series form that houses the data point that you want to get.</p>

        Raises:
            capo_datazone.errors.access_denied_exception.AccessDeniedException: <p>You do not have sufficient access to perform this action.</p>
            capo_datazone.errors.throttling_exception.ThrottlingException: <p>The request was denied due to request throttling.</p>
            capo_datazone.errors.unauthorized_exception.UnauthorizedException: <p>You do not have permission to perform this action.</p>
            capo_datazone.errors.internal_server_exception.InternalServerException: <p>The request has failed because of an unknown error, exception or failure.</p>
            capo_datazone.errors.resource_not_found_exception.ResourceNotFoundException: <p>The specified resource cannot be found.</p>
            capo_datazone.errors.validation_exception.ValidationException: <p>The input fails to satisfy the constraints specified by the Amazon Web Services service.</p>
            capo_datazone.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        async def _handler(
            req: "AsyncOperationRequest[capo_datazone.types.get_time_series_data_point_input.GetTimeSeriesDataPointInput]",
        ) -> AsyncOperationResponse[
            "capo_datazone.types.get_time_series_data_point_output.GetTimeSeriesDataPointOutput"
        ]:
            import capo_datazone._operations.data_zone.get_time_series_data_point

            (
                output,
                http_response,
            ) = await capo_datazone._operations.data_zone.get_time_series_data_point.async_get_time_series_data_point(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_datazone.types.get_time_series_data_point_input.GetTimeSeriesDataPointInput = {
            "domain_identifier": domain_identifier,
            "entity_identifier": entity_identifier,
            "entity_type": entity_type,
            "identifier": identifier,
            "form_name": form_name,
        }

        response = await aexecute_pipeline(
            AsyncOperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        await response.response.aclose()
        return response.output

    async def get_user_profile(
        self,
        domain_identifier: "capo_datazone.types.domain_id.DomainId",
        user_identifier: "capo_datazone.types.user_identifier.UserIdentifier",
        *,
        config_overrides: Optional[AsyncDataZoneClientConfig] = None,
        type: Optional["capo_datazone.types.user_profile_type.UserProfileType"] = None,
        session_name: Optional[str] = None,
    ) -> "capo_datazone.types.get_user_profile_output.GetUserProfileOutput":
        """<p>Gets a user profile in Amazon DataZone.</p>

        Args:
            domain_identifier: <p>the ID of the Amazon DataZone domain the data portal of which you want to get.</p>
            user_identifier: <p>The identifier of the user for which you want to get the user profile.</p>
            type: <p>The type of the user profile.</p>
            session_name: <p>The session name for IAM role sessions.</p>

        Raises:
            capo_datazone.errors.access_denied_exception.AccessDeniedException: <p>You do not have sufficient access to perform this action.</p>
            capo_datazone.errors.throttling_exception.ThrottlingException: <p>The request was denied due to request throttling.</p>
            capo_datazone.errors.unauthorized_exception.UnauthorizedException: <p>You do not have permission to perform this action.</p>
            capo_datazone.errors.internal_server_exception.InternalServerException: <p>The request has failed because of an unknown error, exception or failure.</p>
            capo_datazone.errors.resource_not_found_exception.ResourceNotFoundException: <p>The specified resource cannot be found.</p>
            capo_datazone.errors.validation_exception.ValidationException: <p>The input fails to satisfy the constraints specified by the Amazon Web Services service.</p>
            capo_datazone.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        async def _handler(
            req: "AsyncOperationRequest[capo_datazone.types.get_user_profile_input.GetUserProfileInput]",
        ) -> AsyncOperationResponse[
            "capo_datazone.types.get_user_profile_output.GetUserProfileOutput"
        ]:
            import capo_datazone._operations.data_zone.get_user_profile

            (
                output,
                http_response,
            ) = await capo_datazone._operations.data_zone.get_user_profile.async_get_user_profile(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_datazone.types.get_user_profile_input.GetUserProfileInput = {
            "domain_identifier": domain_identifier,
            "user_identifier": user_identifier,
        }
        if type is not None:
            input_["type"] = type
        if session_name is not None:
            input_["session_name"] = session_name

        response = await aexecute_pipeline(
            AsyncOperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        await response.response.aclose()
        return response.output

    async def list_account_pools(
        self,
        domain_identifier: "capo_datazone.types.domain_id.DomainId",
        *,
        config_overrides: Optional[AsyncDataZoneClientConfig] = None,
        name: Optional["capo_datazone.types.account_pool_name.AccountPoolName"] = None,
        sort_by: Optional[
            "capo_datazone.types.sort_field_account_pool.SortFieldAccountPool"
        ] = None,
        sort_order: Optional["capo_datazone.types.sort_order.SortOrder"] = None,
        next_token: Optional[
            "capo_datazone.types.pagination_token.PaginationToken"
        ] = None,
        max_results: Optional["capo_datazone.types.max_results.MaxResults"] = None,
    ) -> "capo_datazone.types.list_account_pools_output.ListAccountPoolsOutput":
        """<p>Lists existing account pools.</p>

        Args:
            domain_identifier: <p>The ID of the domain where exsting account pools are to be listed.</p>
            name: <p>The name of the account pool to be listed.</p>
            sort_by: <p>The sort by mechanism in which the existing account pools are to be listed.</p>
            sort_order: <p>The sort order in which the existing account pools are to be listed.</p>
            next_token: <p>When the number of account pools is greater than the default value for the MaxResults parameter, or if you explicitly specify a value for MaxResults that is less than the number of account pools, the response includes a pagination token named NextToken. You can specify this NextToken value in a subsequent call to ListAccountPools to list the next set of account pools.</p>
            max_results: <p>The maximum number of account pools to return in a single call to ListAccountPools. When the number of account pools to be listed is greater than the value of MaxResults, the response contains a NextToken value that you can use in a subsequent call to ListAccountPools to list the next set of account pools.</p>

        Raises:
            capo_datazone.errors.access_denied_exception.AccessDeniedException: <p>You do not have sufficient access to perform this action.</p>
            capo_datazone.errors.throttling_exception.ThrottlingException: <p>The request was denied due to request throttling.</p>
            capo_datazone.errors.unauthorized_exception.UnauthorizedException: <p>You do not have permission to perform this action.</p>
            capo_datazone.errors.internal_server_exception.InternalServerException: <p>The request has failed because of an unknown error, exception or failure.</p>
            capo_datazone.errors.validation_exception.ValidationException: <p>The input fails to satisfy the constraints specified by the Amazon Web Services service.</p>
            capo_datazone.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        async def _handler(
            req: "AsyncOperationRequest[capo_datazone.types.list_account_pools_input.ListAccountPoolsInput]",
        ) -> AsyncOperationResponse[
            "capo_datazone.types.list_account_pools_output.ListAccountPoolsOutput"
        ]:
            import capo_datazone._operations.data_zone.list_account_pools

            (
                output,
                http_response,
            ) = await capo_datazone._operations.data_zone.list_account_pools.async_list_account_pools(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_datazone.types.list_account_pools_input.ListAccountPoolsInput = {
            "domain_identifier": domain_identifier
        }
        if name is not None:
            input_["name"] = name
        if sort_by is not None:
            input_["sort_by"] = sort_by
        if sort_order is not None:
            input_["sort_order"] = sort_order
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

    async def iter_list_account_pools(
        self,
        domain_identifier: "capo_datazone.types.domain_id.DomainId",
        *,
        config_overrides: Optional[AsyncDataZoneClientConfig] = None,
        name: Optional["capo_datazone.types.account_pool_name.AccountPoolName"] = None,
        sort_by: Optional[
            "capo_datazone.types.sort_field_account_pool.SortFieldAccountPool"
        ] = None,
        sort_order: Optional["capo_datazone.types.sort_order.SortOrder"] = None,
        next_token: Optional[
            "capo_datazone.types.pagination_token.PaginationToken"
        ] = None,
        max_results: Optional["capo_datazone.types.max_results.MaxResults"] = None,
    ) -> "AsyncIterator[capo_datazone.types.account_pool_summary.AccountPoolSummary]":
        _token = next_token
        while True:
            _response = await self.list_account_pools(
                domain_identifier,
                config_overrides=config_overrides,
                name=name,
                sort_by=sort_by,
                sort_order=sort_order,
                next_token=_token,
                max_results=max_results,
            )
            _page = _resolve_path(_response, ("items",))
            for _item in _page or []:
                yield _item
            _token = _resolve_path(_response, ("next_token",))
            if not _token:
                break

    async def list_accounts_in_account_pool(
        self,
        domain_identifier: "capo_datazone.types.domain_id.DomainId",
        identifier: "capo_datazone.types.account_pool_id.AccountPoolId",
        *,
        config_overrides: Optional[AsyncDataZoneClientConfig] = None,
        next_token: Optional[
            "capo_datazone.types.pagination_token.PaginationToken"
        ] = None,
        max_results: Optional["capo_datazone.types.max_results.MaxResults"] = None,
    ) -> "capo_datazone.types.list_accounts_in_account_pool_output.ListAccountsInAccountPoolOutput":
        """<p>Lists the accounts in the specified account pool.</p>

        Args:
            domain_identifier: <p>The ID of the domain in which the accounts in the specified account pool are to be listed.</p>
            identifier: <p>The ID of the account pool whose accounts are to be listed.</p>
            next_token: <p>When the number of accounts is greater than the default value for the MaxResults parameter, or if you explicitly specify a value for MaxResults that is less than the number of accounts, the response includes a pagination token named NextToken. You can specify this NextToken value in a subsequent call to ListAccountsInAccountPool to list the next set of accounts.</p>
            max_results: <p>The maximum number of accounts to return in a single call to ListAccountsInAccountPool. When the number of accounts to be listed is greater than the value of MaxResults, the response contains a NextToken value that you can use in a subsequent call to ListAccountsInAccountPool to list the next set of accounts.</p>

        Raises:
            capo_datazone.errors.access_denied_exception.AccessDeniedException: <p>You do not have sufficient access to perform this action.</p>
            capo_datazone.errors.throttling_exception.ThrottlingException: <p>The request was denied due to request throttling.</p>
            capo_datazone.errors.unauthorized_exception.UnauthorizedException: <p>You do not have permission to perform this action.</p>
            capo_datazone.errors.internal_server_exception.InternalServerException: <p>The request has failed because of an unknown error, exception or failure.</p>
            capo_datazone.errors.resource_not_found_exception.ResourceNotFoundException: <p>The specified resource cannot be found.</p>
            capo_datazone.errors.validation_exception.ValidationException: <p>The input fails to satisfy the constraints specified by the Amazon Web Services service.</p>
            capo_datazone.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        async def _handler(
            req: "AsyncOperationRequest[capo_datazone.types.list_accounts_in_account_pool_input.ListAccountsInAccountPoolInput]",
        ) -> AsyncOperationResponse[
            "capo_datazone.types.list_accounts_in_account_pool_output.ListAccountsInAccountPoolOutput"
        ]:
            import capo_datazone._operations.data_zone.list_accounts_in_account_pool

            (
                output,
                http_response,
            ) = await capo_datazone._operations.data_zone.list_accounts_in_account_pool.async_list_accounts_in_account_pool(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_datazone.types.list_accounts_in_account_pool_input.ListAccountsInAccountPoolInput = {
            "domain_identifier": domain_identifier,
            "identifier": identifier,
        }
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

    async def iter_list_accounts_in_account_pool(
        self,
        domain_identifier: "capo_datazone.types.domain_id.DomainId",
        identifier: "capo_datazone.types.account_pool_id.AccountPoolId",
        *,
        config_overrides: Optional[AsyncDataZoneClientConfig] = None,
        next_token: Optional[
            "capo_datazone.types.pagination_token.PaginationToken"
        ] = None,
        max_results: Optional["capo_datazone.types.max_results.MaxResults"] = None,
    ) -> "AsyncIterator[capo_datazone.types.account_info.AccountInfo]":
        _token = next_token
        while True:
            _response = await self.list_accounts_in_account_pool(
                domain_identifier,
                identifier,
                config_overrides=config_overrides,
                next_token=_token,
                max_results=max_results,
            )
            _page = _resolve_path(_response, ("items",))
            for _item in _page or []:
                yield _item
            _token = _resolve_path(_response, ("next_token",))
            if not _token:
                break

    async def list_asset_filters(
        self,
        domain_identifier: "capo_datazone.types.domain_id.DomainId",
        asset_identifier: "capo_datazone.types.asset_id.AssetId",
        *,
        config_overrides: Optional[AsyncDataZoneClientConfig] = None,
        status: Optional["capo_datazone.types.filter_status.FilterStatus"] = None,
        next_token: Optional[
            "capo_datazone.types.pagination_token.PaginationToken"
        ] = None,
        max_results: Optional["capo_datazone.types.max_results.MaxResults"] = None,
    ) -> "capo_datazone.types.list_asset_filters_output.ListAssetFiltersOutput":
        """<p>Lists asset filters.</p> <p>Prerequisites:</p> <ul> <li> <p>A valid domain and asset must exist. </p> </li> <li> <p>The asset must have at least one filter created to return results. </p> </li> </ul>

        Args:
            domain_identifier: <p>The ID of the domain where you want to list asset filters.</p>
            asset_identifier: <p>The ID of the data asset.</p>
            status: <p>The status of the asset filter.</p>
            next_token: <p>When the number of asset filters is greater than the default value for the <code>MaxResults</code> parameter, or if you explicitly specify a value for <code>MaxResults</code> that is less than the number of asset filters, the response includes a pagination token named <code>NextToken</code>. You can specify this <code>NextToken</code> value in a subsequent call to <code>ListAssetFilters</code> to list the next set of asset filters.</p>
            max_results: <p>The maximum number of asset filters to return in a single call to <code>ListAssetFilters</code>. When the number of asset filters to be listed is greater than the value of <code>MaxResults</code>, the response contains a <code>NextToken</code> value that you can use in a subsequent call to <code>ListAssetFilters</code> to list the next set of asset filters.</p>

        Raises:
            capo_datazone.errors.access_denied_exception.AccessDeniedException: <p>You do not have sufficient access to perform this action.</p>
            capo_datazone.errors.throttling_exception.ThrottlingException: <p>The request was denied due to request throttling.</p>
            capo_datazone.errors.unauthorized_exception.UnauthorizedException: <p>You do not have permission to perform this action.</p>
            capo_datazone.errors.internal_server_exception.InternalServerException: <p>The request has failed because of an unknown error, exception or failure.</p>
            capo_datazone.errors.resource_not_found_exception.ResourceNotFoundException: <p>The specified resource cannot be found.</p>
            capo_datazone.errors.validation_exception.ValidationException: <p>The input fails to satisfy the constraints specified by the Amazon Web Services service.</p>
            capo_datazone.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        async def _handler(
            req: "AsyncOperationRequest[capo_datazone.types.list_asset_filters_input.ListAssetFiltersInput]",
        ) -> AsyncOperationResponse[
            "capo_datazone.types.list_asset_filters_output.ListAssetFiltersOutput"
        ]:
            import capo_datazone._operations.data_zone.list_asset_filters

            (
                output,
                http_response,
            ) = await capo_datazone._operations.data_zone.list_asset_filters.async_list_asset_filters(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_datazone.types.list_asset_filters_input.ListAssetFiltersInput = {
            "domain_identifier": domain_identifier,
            "asset_identifier": asset_identifier,
        }
        if status is not None:
            input_["status"] = status
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

    async def iter_list_asset_filters(
        self,
        domain_identifier: "capo_datazone.types.domain_id.DomainId",
        asset_identifier: "capo_datazone.types.asset_id.AssetId",
        *,
        config_overrides: Optional[AsyncDataZoneClientConfig] = None,
        status: Optional["capo_datazone.types.filter_status.FilterStatus"] = None,
        next_token: Optional[
            "capo_datazone.types.pagination_token.PaginationToken"
        ] = None,
        max_results: Optional["capo_datazone.types.max_results.MaxResults"] = None,
    ) -> "AsyncIterator[capo_datazone.types.asset_filter_summary.AssetFilterSummary]":
        _token = next_token
        while True:
            _response = await self.list_asset_filters(
                domain_identifier,
                asset_identifier,
                config_overrides=config_overrides,
                status=status,
                next_token=_token,
                max_results=max_results,
            )
            _page = _resolve_path(_response, ("items",))
            for _item in _page or []:
                yield _item
            _token = _resolve_path(_response, ("next_token",))
            if not _token:
                break

    async def list_asset_revisions(
        self,
        domain_identifier: "capo_datazone.types.domain_id.DomainId",
        identifier: "capo_datazone.types.asset_identifier.AssetIdentifier",
        *,
        config_overrides: Optional[AsyncDataZoneClientConfig] = None,
        next_token: Optional[
            "capo_datazone.types.pagination_token.PaginationToken"
        ] = None,
        max_results: Optional["capo_datazone.types.max_results.MaxResults"] = None,
    ) -> "capo_datazone.types.list_asset_revisions_output.ListAssetRevisionsOutput":
        """<p>Lists the revisions for the asset.</p> <p>Prerequisites:</p> <ul> <li> <p>The asset must exist in the domain. </p> </li> <li> <p>There must be at least one revision of the asset (which happens automatically after creation).</p> </li> <li> <p>The domain must be valid and active.</p> </li> <li> <p>User must have permissions on the asset and domain.</p> </li> </ul>

        Args:
            domain_identifier: <p>The identifier of the domain.</p>
            identifier: <p>The identifier of the asset.</p>
            next_token: <p>When the number of revisions is greater than the default value for the <code>MaxResults</code> parameter, or if you explicitly specify a value for <code>MaxResults</code> that is less than the number of revisions, the response includes a pagination token named <code>NextToken</code>. You can specify this <code>NextToken</code> value in a subsequent call to <code>ListAssetRevisions</code> to list the next set of revisions.</p>
            max_results: <p>The maximum number of revisions to return in a single call to <code>ListAssetRevisions</code>. When the number of revisions to be listed is greater than the value of <code>MaxResults</code>, the response contains a <code>NextToken</code> value that you can use in a subsequent call to <code>ListAssetRevisions</code> to list the next set of revisions.</p>

        Raises:
            capo_datazone.errors.access_denied_exception.AccessDeniedException: <p>You do not have sufficient access to perform this action.</p>
            capo_datazone.errors.throttling_exception.ThrottlingException: <p>The request was denied due to request throttling.</p>
            capo_datazone.errors.unauthorized_exception.UnauthorizedException: <p>You do not have permission to perform this action.</p>
            capo_datazone.errors.internal_server_exception.InternalServerException: <p>The request has failed because of an unknown error, exception or failure.</p>
            capo_datazone.errors.resource_not_found_exception.ResourceNotFoundException: <p>The specified resource cannot be found.</p>
            capo_datazone.errors.validation_exception.ValidationException: <p>The input fails to satisfy the constraints specified by the Amazon Web Services service.</p>
            capo_datazone.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        async def _handler(
            req: "AsyncOperationRequest[capo_datazone.types.list_asset_revisions_input.ListAssetRevisionsInput]",
        ) -> AsyncOperationResponse[
            "capo_datazone.types.list_asset_revisions_output.ListAssetRevisionsOutput"
        ]:
            import capo_datazone._operations.data_zone.list_asset_revisions

            (
                output,
                http_response,
            ) = await capo_datazone._operations.data_zone.list_asset_revisions.async_list_asset_revisions(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_datazone.types.list_asset_revisions_input.ListAssetRevisionsInput = {
            "domain_identifier": domain_identifier,
            "identifier": identifier,
        }
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

    async def list_connections(
        self,
        domain_identifier: "capo_datazone.types.domain_id.DomainId",
        *,
        config_overrides: Optional[AsyncDataZoneClientConfig] = None,
        max_results: Optional["capo_datazone.types.max_results.MaxResults"] = None,
        next_token: Optional[
            "capo_datazone.types.pagination_token.PaginationToken"
        ] = None,
        sort_by: Optional[
            "capo_datazone.types.sort_field_connection.SortFieldConnection"
        ] = None,
        sort_order: Optional["capo_datazone.types.sort_order.SortOrder"] = None,
        name: Optional["capo_datazone.types.connection_name.ConnectionName"] = None,
        environment_identifier: Optional[
            "capo_datazone.types.environment_id.EnvironmentId"
        ] = None,
        project_identifier: Optional["capo_datazone.types.project_id.ProjectId"] = None,
        type: Optional["capo_datazone.types.connection_type.ConnectionType"] = None,
        scope: Optional["capo_datazone.types.connection_scope.ConnectionScope"] = None,
    ) -> "capo_datazone.types.list_connections_output.ListConnectionsOutput":
        """<p>Lists connections. In Amazon DataZone, a connection enables you to connect your resources (domains, projects, and environments) to external resources and services.</p>

        Args:
            domain_identifier: <p>The ID of the domain where you want to list connections.</p>
            max_results: <p>The maximum number of connections to return in a single call to ListConnections. When the number of connections to be listed is greater than the value of MaxResults, the response contains a NextToken value that you can use in a subsequent call to ListConnections to list the next set of connections.</p>
            next_token: <p>When the number of connections is greater than the default value for the MaxResults parameter, or if you explicitly specify a value for MaxResults that is less than the number of connections, the response includes a pagination token named NextToken. You can specify this NextToken value in a subsequent call to ListConnections to list the next set of connections.</p>
            sort_by: <p>Specifies how you want to sort the listed connections.</p>
            sort_order: <p>Specifies the sort order for the listed connections.</p>
            name: <p>The name of the connection.</p>
            environment_identifier: <p>The ID of the environment where you want to list connections.</p>
            project_identifier: <p>The ID of the project where you want to list connections.</p>
            type: <p>The type of connection.</p>
            scope: <p>The scope of the connection.</p>

        Raises:
            capo_datazone.errors.access_denied_exception.AccessDeniedException: <p>You do not have sufficient access to perform this action.</p>
            capo_datazone.errors.throttling_exception.ThrottlingException: <p>The request was denied due to request throttling.</p>
            capo_datazone.errors.unauthorized_exception.UnauthorizedException: <p>You do not have permission to perform this action.</p>
            capo_datazone.errors.internal_server_exception.InternalServerException: <p>The request has failed because of an unknown error, exception or failure.</p>
            capo_datazone.errors.validation_exception.ValidationException: <p>The input fails to satisfy the constraints specified by the Amazon Web Services service.</p>
            capo_datazone.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        async def _handler(
            req: "AsyncOperationRequest[capo_datazone.types.list_connections_input.ListConnectionsInput]",
        ) -> AsyncOperationResponse[
            "capo_datazone.types.list_connections_output.ListConnectionsOutput"
        ]:
            import capo_datazone._operations.data_zone.list_connections

            (
                output,
                http_response,
            ) = await capo_datazone._operations.data_zone.list_connections.async_list_connections(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_datazone.types.list_connections_input.ListConnectionsInput = {
            "domain_identifier": domain_identifier
        }
        if max_results is not None:
            input_["max_results"] = max_results
        if next_token is not None:
            input_["next_token"] = next_token
        if sort_by is not None:
            input_["sort_by"] = sort_by
        if sort_order is not None:
            input_["sort_order"] = sort_order
        if name is not None:
            input_["name"] = name
        if environment_identifier is not None:
            input_["environment_identifier"] = environment_identifier
        if project_identifier is not None:
            input_["project_identifier"] = project_identifier
        if type is not None:
            input_["type"] = type
        if scope is not None:
            input_["scope"] = scope

        response = await aexecute_pipeline(
            AsyncOperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        await response.response.aclose()
        return response.output

    async def iter_list_connections(
        self,
        domain_identifier: "capo_datazone.types.domain_id.DomainId",
        *,
        config_overrides: Optional[AsyncDataZoneClientConfig] = None,
        max_results: Optional["capo_datazone.types.max_results.MaxResults"] = None,
        next_token: Optional[
            "capo_datazone.types.pagination_token.PaginationToken"
        ] = None,
        sort_by: Optional[
            "capo_datazone.types.sort_field_connection.SortFieldConnection"
        ] = None,
        sort_order: Optional["capo_datazone.types.sort_order.SortOrder"] = None,
        name: Optional["capo_datazone.types.connection_name.ConnectionName"] = None,
        environment_identifier: Optional[
            "capo_datazone.types.environment_id.EnvironmentId"
        ] = None,
        project_identifier: Optional["capo_datazone.types.project_id.ProjectId"] = None,
        type: Optional["capo_datazone.types.connection_type.ConnectionType"] = None,
        scope: Optional["capo_datazone.types.connection_scope.ConnectionScope"] = None,
    ) -> "AsyncIterator[capo_datazone.types.connection_summary.ConnectionSummary]":
        _token = next_token
        while True:
            _response = await self.list_connections(
                domain_identifier,
                config_overrides=config_overrides,
                max_results=max_results,
                next_token=_token,
                sort_by=sort_by,
                sort_order=sort_order,
                name=name,
                environment_identifier=environment_identifier,
                project_identifier=project_identifier,
                type=type,
                scope=scope,
            )
            _page = _resolve_path(_response, ("items",))
            for _item in _page or []:
                yield _item
            _token = _resolve_path(_response, ("next_token",))
            if not _token:
                break

    async def list_data_product_revisions(
        self,
        domain_identifier: "capo_datazone.types.domain_id.DomainId",
        identifier: "capo_datazone.types.data_product_id.DataProductId",
        *,
        config_overrides: Optional[AsyncDataZoneClientConfig] = None,
        max_results: Optional["capo_datazone.types.max_results.MaxResults"] = None,
        next_token: Optional[
            "capo_datazone.types.pagination_token.PaginationToken"
        ] = None,
    ) -> "capo_datazone.types.list_data_product_revisions_output.ListDataProductRevisionsOutput":
        """<p>Lists data product revisions.</p> <p>Prerequisites:</p> <ul> <li> <p>The data product ID must exist within the domain. </p> </li> <li> <p>User must have view permissions on the data product.</p> </li> <li> <p>The domain must be in a valid and accessible state.</p> </li> </ul>

        Args:
            domain_identifier: <p>The ID of the domain of the data product revisions that you want to list.</p>
            identifier: <p>The ID of the data product revision.</p>
            max_results: <p>The maximum number of asset filters to return in a single call to <code>ListDataProductRevisions</code>. When the number of data product revisions to be listed is greater than the value of <code>MaxResults</code>, the response contains a <code>NextToken</code> value that you can use in a subsequent call to <code>ListDataProductRevisions</code> to list the next set of data product revisions.</p>
            next_token: <p>When the number of data product revisions is greater than the default value for the <code>MaxResults</code> parameter, or if you explicitly specify a value for <code>MaxResults</code> that is less than the number of data product revisions, the response includes a pagination token named <code>NextToken</code>. You can specify this <code>NextToken</code> value in a subsequent call to <code>ListDataProductRevisions</code> to list the next set of data product revisions.</p>

        Raises:
            capo_datazone.errors.access_denied_exception.AccessDeniedException: <p>You do not have sufficient access to perform this action.</p>
            capo_datazone.errors.throttling_exception.ThrottlingException: <p>The request was denied due to request throttling.</p>
            capo_datazone.errors.unauthorized_exception.UnauthorizedException: <p>You do not have permission to perform this action.</p>
            capo_datazone.errors.internal_server_exception.InternalServerException: <p>The request has failed because of an unknown error, exception or failure.</p>
            capo_datazone.errors.resource_not_found_exception.ResourceNotFoundException: <p>The specified resource cannot be found.</p>
            capo_datazone.errors.validation_exception.ValidationException: <p>The input fails to satisfy the constraints specified by the Amazon Web Services service.</p>
            capo_datazone.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        async def _handler(
            req: "AsyncOperationRequest[capo_datazone.types.list_data_product_revisions_input.ListDataProductRevisionsInput]",
        ) -> AsyncOperationResponse[
            "capo_datazone.types.list_data_product_revisions_output.ListDataProductRevisionsOutput"
        ]:
            import capo_datazone._operations.data_zone.list_data_product_revisions

            (
                output,
                http_response,
            ) = await capo_datazone._operations.data_zone.list_data_product_revisions.async_list_data_product_revisions(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_datazone.types.list_data_product_revisions_input.ListDataProductRevisionsInput = {
            "domain_identifier": domain_identifier,
            "identifier": identifier,
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

    async def iter_list_data_product_revisions(
        self,
        domain_identifier: "capo_datazone.types.domain_id.DomainId",
        identifier: "capo_datazone.types.data_product_id.DataProductId",
        *,
        config_overrides: Optional[AsyncDataZoneClientConfig] = None,
        max_results: Optional["capo_datazone.types.max_results.MaxResults"] = None,
        next_token: Optional[
            "capo_datazone.types.pagination_token.PaginationToken"
        ] = None,
    ) -> "AsyncIterator[capo_datazone.types.data_product_revision.DataProductRevision]":
        _token = next_token
        while True:
            _response = await self.list_data_product_revisions(
                domain_identifier,
                identifier,
                config_overrides=config_overrides,
                max_results=max_results,
                next_token=_token,
            )
            _page = _resolve_path(_response, ("items",))
            for _item in _page or []:
                yield _item
            _token = _resolve_path(_response, ("next_token",))
            if not _token:
                break

    async def list_data_source_run_activities(
        self,
        domain_identifier: "capo_datazone.types.domain_id.DomainId",
        identifier: "capo_datazone.types.data_source_run_id.DataSourceRunId",
        *,
        config_overrides: Optional[AsyncDataZoneClientConfig] = None,
        status: Optional[
            "capo_datazone.types.data_asset_activity_status.DataAssetActivityStatus"
        ] = None,
        next_token: Optional[
            "capo_datazone.types.pagination_token.PaginationToken"
        ] = None,
        max_results: Optional["capo_datazone.types.max_results.MaxResults"] = None,
    ) -> "capo_datazone.types.list_data_source_run_activities_output.ListDataSourceRunActivitiesOutput":
        """<p>Lists data source run activities.</p>

        Args:
            domain_identifier: <p>The identifier of the Amazon DataZone domain in which to list data source run activities.</p>
            identifier: <p>The identifier of the data source run.</p>
            status: <p>The status of the data source run.</p>
            next_token: <p>When the number of activities is greater than the default value for the <code>MaxResults</code> parameter, or if you explicitly specify a value for <code>MaxResults</code> that is less than the number of activities, the response includes a pagination token named <code>NextToken</code>. You can specify this <code>NextToken</code> value in a subsequent call to <code>ListDataSourceRunActivities</code> to list the next set of activities.</p>
            max_results: <p>The maximum number of activities to return in a single call to <code>ListDataSourceRunActivities</code>. When the number of activities to be listed is greater than the value of <code>MaxResults</code>, the response contains a <code>NextToken</code> value that you can use in a subsequent call to <code>ListDataSourceRunActivities</code> to list the next set of activities.</p>

        Raises:
            capo_datazone.errors.access_denied_exception.AccessDeniedException: <p>You do not have sufficient access to perform this action.</p>
            capo_datazone.errors.throttling_exception.ThrottlingException: <p>The request was denied due to request throttling.</p>
            capo_datazone.errors.unauthorized_exception.UnauthorizedException: <p>You do not have permission to perform this action.</p>
            capo_datazone.errors.conflict_exception.ConflictException: <p>There is a conflict while performing this action.</p>
            capo_datazone.errors.internal_server_exception.InternalServerException: <p>The request has failed because of an unknown error, exception or failure.</p>
            capo_datazone.errors.resource_not_found_exception.ResourceNotFoundException: <p>The specified resource cannot be found.</p>
            capo_datazone.errors.service_quota_exceeded_exception.ServiceQuotaExceededException: <p>The request has exceeded the specified service quota.</p>
            capo_datazone.errors.validation_exception.ValidationException: <p>The input fails to satisfy the constraints specified by the Amazon Web Services service.</p>
            capo_datazone.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        async def _handler(
            req: "AsyncOperationRequest[capo_datazone.types.list_data_source_run_activities_input.ListDataSourceRunActivitiesInput]",
        ) -> AsyncOperationResponse[
            "capo_datazone.types.list_data_source_run_activities_output.ListDataSourceRunActivitiesOutput"
        ]:
            import capo_datazone._operations.data_zone.list_data_source_run_activities

            (
                output,
                http_response,
            ) = await capo_datazone._operations.data_zone.list_data_source_run_activities.async_list_data_source_run_activities(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_datazone.types.list_data_source_run_activities_input.ListDataSourceRunActivitiesInput = {
            "domain_identifier": domain_identifier,
            "identifier": identifier,
        }
        if status is not None:
            input_["status"] = status
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

    async def iter_list_data_source_run_activities(
        self,
        domain_identifier: "capo_datazone.types.domain_id.DomainId",
        identifier: "capo_datazone.types.data_source_run_id.DataSourceRunId",
        *,
        config_overrides: Optional[AsyncDataZoneClientConfig] = None,
        status: Optional[
            "capo_datazone.types.data_asset_activity_status.DataAssetActivityStatus"
        ] = None,
        next_token: Optional[
            "capo_datazone.types.pagination_token.PaginationToken"
        ] = None,
        max_results: Optional["capo_datazone.types.max_results.MaxResults"] = None,
    ) -> "AsyncIterator[capo_datazone.types.data_source_run_activity.DataSourceRunActivity]":
        _token = next_token
        while True:
            _response = await self.list_data_source_run_activities(
                domain_identifier,
                identifier,
                config_overrides=config_overrides,
                status=status,
                next_token=_token,
                max_results=max_results,
            )
            _page = _resolve_path(_response, ("items",))
            for _item in _page or []:
                yield _item
            _token = _resolve_path(_response, ("next_token",))
            if not _token:
                break

    async def list_entity_owners(
        self,
        domain_identifier: "capo_datazone.types.domain_id.DomainId",
        entity_type: "capo_datazone.types.data_zone_entity_type.DataZoneEntityType",
        entity_identifier: str,
        *,
        config_overrides: Optional[AsyncDataZoneClientConfig] = None,
        max_results: Optional[
            "capo_datazone.types.max_results_for_list_domains.MaxResultsForListDomains"
        ] = None,
        next_token: Optional[
            "capo_datazone.types.pagination_token.PaginationToken"
        ] = None,
    ) -> "capo_datazone.types.list_entity_owners_output.ListEntityOwnersOutput":
        """<p>Lists the entity (domain units) owners.</p>

        Args:
            domain_identifier: <p>The ID of the domain where you want to list entity owners.</p>
            entity_type: <p>The type of the entity that you want to list.</p>
            entity_identifier: <p>The ID of the entity that you want to list.</p>
            max_results: <p>The maximum number of entities to return in a single call to <code>ListEntityOwners</code>. When the number of entities to be listed is greater than the value of <code>MaxResults</code>, the response contains a <code>NextToken</code> value that you can use in a subsequent call to <code>ListEntityOwners</code> to list the next set of entities.</p>
            next_token: <p>When the number of entities is greater than the default value for the <code>MaxResults</code> parameter, or if you explicitly specify a value for <code>MaxResults</code> that is less than the number of entities, the response includes a pagination token named <code>NextToken</code>. You can specify this <code>NextToken</code> value in a subsequent call to <code>ListEntityOwners</code> to list the next set of entities.</p>

        Raises:
            capo_datazone.errors.access_denied_exception.AccessDeniedException: <p>You do not have sufficient access to perform this action.</p>
            capo_datazone.errors.throttling_exception.ThrottlingException: <p>The request was denied due to request throttling.</p>
            capo_datazone.errors.unauthorized_exception.UnauthorizedException: <p>You do not have permission to perform this action.</p>
            capo_datazone.errors.internal_server_exception.InternalServerException: <p>The request has failed because of an unknown error, exception or failure.</p>
            capo_datazone.errors.validation_exception.ValidationException: <p>The input fails to satisfy the constraints specified by the Amazon Web Services service.</p>
            capo_datazone.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        async def _handler(
            req: "AsyncOperationRequest[capo_datazone.types.list_entity_owners_input.ListEntityOwnersInput]",
        ) -> AsyncOperationResponse[
            "capo_datazone.types.list_entity_owners_output.ListEntityOwnersOutput"
        ]:
            import capo_datazone._operations.data_zone.list_entity_owners

            (
                output,
                http_response,
            ) = await capo_datazone._operations.data_zone.list_entity_owners.async_list_entity_owners(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_datazone.types.list_entity_owners_input.ListEntityOwnersInput = {
            "domain_identifier": domain_identifier,
            "entity_type": entity_type,
            "entity_identifier": entity_identifier,
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

    async def iter_list_entity_owners(
        self,
        domain_identifier: "capo_datazone.types.domain_id.DomainId",
        entity_type: "capo_datazone.types.data_zone_entity_type.DataZoneEntityType",
        entity_identifier: str,
        *,
        config_overrides: Optional[AsyncDataZoneClientConfig] = None,
        max_results: Optional[
            "capo_datazone.types.max_results_for_list_domains.MaxResultsForListDomains"
        ] = None,
        next_token: Optional[
            "capo_datazone.types.pagination_token.PaginationToken"
        ] = None,
    ) -> "AsyncIterator[capo_datazone.types.owner_properties_output.OwnerPropertiesOutput]":
        _token = next_token
        while True:
            _response = await self.list_entity_owners(
                domain_identifier,
                entity_type,
                entity_identifier,
                config_overrides=config_overrides,
                max_results=max_results,
                next_token=_token,
            )
            _page = _resolve_path(_response, ("owners",))
            for _item in _page or []:
                yield _item
            _token = _resolve_path(_response, ("next_token",))
            if not _token:
                break

    async def list_environment_actions(
        self,
        domain_identifier: "capo_datazone.types.domain_id.DomainId",
        environment_identifier: "capo_datazone.types.environment_id.EnvironmentId",
        *,
        config_overrides: Optional[AsyncDataZoneClientConfig] = None,
        next_token: Optional[
            "capo_datazone.types.pagination_token.PaginationToken"
        ] = None,
        max_results: Optional["capo_datazone.types.max_results.MaxResults"] = None,
    ) -> "capo_datazone.types.list_environment_actions_output.ListEnvironmentActionsOutput":
        """<p>Lists existing environment actions.</p>

        Args:
            domain_identifier: <p>The ID of the Amazon DataZone domain in which the environment actions are listed.</p>
            environment_identifier: <p>The ID of the envrironment whose environment actions are listed.</p>
            next_token: <p>When the number of environment actions is greater than the default value for the <code>MaxResults</code> parameter, or if you explicitly specify a value for <code>MaxResults</code> that is less than the number of environment actions, the response includes a pagination token named <code>NextToken</code>. You can specify this <code>NextToken</code> value in a subsequent call to <code>ListEnvironmentActions</code> to list the next set of environment actions.</p>
            max_results: <p>The maximum number of environment actions to return in a single call to <code>ListEnvironmentActions</code>. When the number of environment actions to be listed is greater than the value of <code>MaxResults</code>, the response contains a <code>NextToken</code> value that you can use in a subsequent call to <code>ListEnvironmentActions</code> to list the next set of environment actions.</p>

        Raises:
            capo_datazone.errors.access_denied_exception.AccessDeniedException: <p>You do not have sufficient access to perform this action.</p>
            capo_datazone.errors.throttling_exception.ThrottlingException: <p>The request was denied due to request throttling.</p>
            capo_datazone.errors.unauthorized_exception.UnauthorizedException: <p>You do not have permission to perform this action.</p>
            capo_datazone.errors.internal_server_exception.InternalServerException: <p>The request has failed because of an unknown error, exception or failure.</p>
            capo_datazone.errors.validation_exception.ValidationException: <p>The input fails to satisfy the constraints specified by the Amazon Web Services service.</p>
            capo_datazone.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        async def _handler(
            req: "AsyncOperationRequest[capo_datazone.types.list_environment_actions_input.ListEnvironmentActionsInput]",
        ) -> AsyncOperationResponse[
            "capo_datazone.types.list_environment_actions_output.ListEnvironmentActionsOutput"
        ]:
            import capo_datazone._operations.data_zone.list_environment_actions

            (
                output,
                http_response,
            ) = await capo_datazone._operations.data_zone.list_environment_actions.async_list_environment_actions(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_datazone.types.list_environment_actions_input.ListEnvironmentActionsInput = {
            "domain_identifier": domain_identifier,
            "environment_identifier": environment_identifier,
        }
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

    async def iter_list_environment_actions(
        self,
        domain_identifier: "capo_datazone.types.domain_id.DomainId",
        environment_identifier: "capo_datazone.types.environment_id.EnvironmentId",
        *,
        config_overrides: Optional[AsyncDataZoneClientConfig] = None,
        next_token: Optional[
            "capo_datazone.types.pagination_token.PaginationToken"
        ] = None,
        max_results: Optional["capo_datazone.types.max_results.MaxResults"] = None,
    ) -> "AsyncIterator[capo_datazone.types.environment_action_summary.EnvironmentActionSummary]":
        _token = next_token
        while True:
            _response = await self.list_environment_actions(
                domain_identifier,
                environment_identifier,
                config_overrides=config_overrides,
                next_token=_token,
                max_results=max_results,
            )
            _page = _resolve_path(_response, ("items",))
            for _item in _page or []:
                yield _item
            _token = _resolve_path(_response, ("next_token",))
            if not _token:
                break

    async def list_environment_blueprints(
        self,
        domain_identifier: "capo_datazone.types.domain_id.DomainId",
        *,
        config_overrides: Optional[AsyncDataZoneClientConfig] = None,
        max_results: Optional["capo_datazone.types.max_results.MaxResults"] = None,
        next_token: Optional[
            "capo_datazone.types.pagination_token.PaginationToken"
        ] = None,
        name: Optional[
            "capo_datazone.types.environment_blueprint_name.EnvironmentBlueprintName"
        ] = None,
        managed: Optional[bool] = None,
    ) -> "capo_datazone.types.list_environment_blueprints_output.ListEnvironmentBlueprintsOutput":
        """<p>Lists blueprints in an Amazon DataZone environment.</p>

        Args:
            domain_identifier: <p>The identifier of the Amazon DataZone domain.</p>
            max_results: <p>The maximum number of blueprints to return in a single call to <code>ListEnvironmentBlueprints</code>. When the number of blueprints to be listed is greater than the value of <code>MaxResults</code>, the response contains a <code>NextToken</code> value that you can use in a subsequent call to <code>ListEnvironmentBlueprints</code> to list the next set of blueprints.</p>
            next_token: <p>When the number of blueprints in the environment is greater than the default value for the <code>MaxResults</code> parameter, or if you explicitly specify a value for <code>MaxResults</code> that is less than the number of blueprints in the environment, the response includes a pagination token named <code>NextToken</code>. You can specify this <code>NextToken</code> value in a subsequent call to <code>ListEnvironmentBlueprints</code>to list the next set of blueprints.</p>
            name: <p>The name of the Amazon DataZone environment.</p>
            managed: <p>Specifies whether the environment blueprint is managed by Amazon DataZone.</p>

        Raises:
            capo_datazone.errors.access_denied_exception.AccessDeniedException: <p>You do not have sufficient access to perform this action.</p>
            capo_datazone.errors.throttling_exception.ThrottlingException: <p>The request was denied due to request throttling.</p>
            capo_datazone.errors.unauthorized_exception.UnauthorizedException: <p>You do not have permission to perform this action.</p>
            capo_datazone.errors.internal_server_exception.InternalServerException: <p>The request has failed because of an unknown error, exception or failure.</p>
            capo_datazone.errors.resource_not_found_exception.ResourceNotFoundException: <p>The specified resource cannot be found.</p>
            capo_datazone.errors.validation_exception.ValidationException: <p>The input fails to satisfy the constraints specified by the Amazon Web Services service.</p>
            capo_datazone.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        async def _handler(
            req: "AsyncOperationRequest[capo_datazone.types.list_environment_blueprints_input.ListEnvironmentBlueprintsInput]",
        ) -> AsyncOperationResponse[
            "capo_datazone.types.list_environment_blueprints_output.ListEnvironmentBlueprintsOutput"
        ]:
            import capo_datazone._operations.data_zone.list_environment_blueprints

            (
                output,
                http_response,
            ) = await capo_datazone._operations.data_zone.list_environment_blueprints.async_list_environment_blueprints(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_datazone.types.list_environment_blueprints_input.ListEnvironmentBlueprintsInput = {
            "domain_identifier": domain_identifier
        }
        if max_results is not None:
            input_["max_results"] = max_results
        if next_token is not None:
            input_["next_token"] = next_token
        if name is not None:
            input_["name"] = name
        if managed is not None:
            input_["managed"] = managed

        response = await aexecute_pipeline(
            AsyncOperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        await response.response.aclose()
        return response.output

    async def iter_list_environment_blueprints(
        self,
        domain_identifier: "capo_datazone.types.domain_id.DomainId",
        *,
        config_overrides: Optional[AsyncDataZoneClientConfig] = None,
        max_results: Optional["capo_datazone.types.max_results.MaxResults"] = None,
        next_token: Optional[
            "capo_datazone.types.pagination_token.PaginationToken"
        ] = None,
        name: Optional[
            "capo_datazone.types.environment_blueprint_name.EnvironmentBlueprintName"
        ] = None,
        managed: Optional[bool] = None,
    ) -> "AsyncIterator[capo_datazone.types.environment_blueprint_summary.EnvironmentBlueprintSummary]":
        _token = next_token
        while True:
            _response = await self.list_environment_blueprints(
                domain_identifier,
                config_overrides=config_overrides,
                max_results=max_results,
                next_token=_token,
                name=name,
                managed=managed,
            )
            _page = _resolve_path(_response, ("items",))
            for _item in _page or []:
                yield _item
            _token = _resolve_path(_response, ("next_token",))
            if not _token:
                break

    async def list_environment_profiles(
        self,
        domain_identifier: "capo_datazone.types.domain_id.DomainId",
        *,
        config_overrides: Optional[AsyncDataZoneClientConfig] = None,
        aws_account_id: Optional[
            "capo_datazone.types.aws_account_id.AwsAccountId"
        ] = None,
        aws_account_region: Optional["capo_datazone.types.aws_region.AwsRegion"] = None,
        environment_blueprint_identifier: Optional[
            "capo_datazone.types.environment_blueprint_id.EnvironmentBlueprintId"
        ] = None,
        project_identifier: Optional["capo_datazone.types.project_id.ProjectId"] = None,
        name: Optional[
            "capo_datazone.types.environment_profile_name.EnvironmentProfileName"
        ] = None,
        next_token: Optional[
            "capo_datazone.types.pagination_token.PaginationToken"
        ] = None,
        max_results: Optional["capo_datazone.types.max_results.MaxResults"] = None,
    ) -> "capo_datazone.types.list_environment_profiles_output.ListEnvironmentProfilesOutput":
        """<p>Lists Amazon DataZone environment profiles.</p>

        Args:
            domain_identifier: <p>The identifier of the Amazon DataZone domain.</p>
            aws_account_id: <p>The identifier of the Amazon Web Services account where you want to list environment profiles.</p>
            aws_account_region: <p>The Amazon Web Services region where you want to list environment profiles.</p>
            environment_blueprint_identifier: <p>The identifier of the blueprint that was used to create the environment profiles that you want to list.</p>
            project_identifier: <p>The identifier of the Amazon DataZone project.</p>
            name: <p/>
            next_token: <p>When the number of environment profiles is greater than the default value for the <code>MaxResults</code> parameter, or if you explicitly specify a value for <code>MaxResults</code> that is less than the number of environment profiles, the response includes a pagination token named <code>NextToken</code>. You can specify this <code>NextToken</code> value in a subsequent call to <code>ListEnvironmentProfiles</code> to list the next set of environment profiles.</p>
            max_results: <p>The maximum number of environment profiles to return in a single call to <code>ListEnvironmentProfiles</code>. When the number of environment profiles to be listed is greater than the value of <code>MaxResults</code>, the response contains a <code>NextToken</code> value that you can use in a subsequent call to <code>ListEnvironmentProfiles</code> to list the next set of environment profiles.</p>

        Raises:
            capo_datazone.errors.access_denied_exception.AccessDeniedException: <p>You do not have sufficient access to perform this action.</p>
            capo_datazone.errors.throttling_exception.ThrottlingException: <p>The request was denied due to request throttling.</p>
            capo_datazone.errors.unauthorized_exception.UnauthorizedException: <p>You do not have permission to perform this action.</p>
            capo_datazone.errors.internal_server_exception.InternalServerException: <p>The request has failed because of an unknown error, exception or failure.</p>
            capo_datazone.errors.validation_exception.ValidationException: <p>The input fails to satisfy the constraints specified by the Amazon Web Services service.</p>
            capo_datazone.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        async def _handler(
            req: "AsyncOperationRequest[capo_datazone.types.list_environment_profiles_input.ListEnvironmentProfilesInput]",
        ) -> AsyncOperationResponse[
            "capo_datazone.types.list_environment_profiles_output.ListEnvironmentProfilesOutput"
        ]:
            import capo_datazone._operations.data_zone.list_environment_profiles

            (
                output,
                http_response,
            ) = await capo_datazone._operations.data_zone.list_environment_profiles.async_list_environment_profiles(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_datazone.types.list_environment_profiles_input.ListEnvironmentProfilesInput = {
            "domain_identifier": domain_identifier
        }
        if aws_account_id is not None:
            input_["aws_account_id"] = aws_account_id
        if aws_account_region is not None:
            input_["aws_account_region"] = aws_account_region
        if environment_blueprint_identifier is not None:
            input_["environment_blueprint_identifier"] = (
                environment_blueprint_identifier
            )
        if project_identifier is not None:
            input_["project_identifier"] = project_identifier
        if name is not None:
            input_["name"] = name
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

    async def iter_list_environment_profiles(
        self,
        domain_identifier: "capo_datazone.types.domain_id.DomainId",
        *,
        config_overrides: Optional[AsyncDataZoneClientConfig] = None,
        aws_account_id: Optional[
            "capo_datazone.types.aws_account_id.AwsAccountId"
        ] = None,
        aws_account_region: Optional["capo_datazone.types.aws_region.AwsRegion"] = None,
        environment_blueprint_identifier: Optional[
            "capo_datazone.types.environment_blueprint_id.EnvironmentBlueprintId"
        ] = None,
        project_identifier: Optional["capo_datazone.types.project_id.ProjectId"] = None,
        name: Optional[
            "capo_datazone.types.environment_profile_name.EnvironmentProfileName"
        ] = None,
        next_token: Optional[
            "capo_datazone.types.pagination_token.PaginationToken"
        ] = None,
        max_results: Optional["capo_datazone.types.max_results.MaxResults"] = None,
    ) -> "AsyncIterator[capo_datazone.types.environment_profile_summary.EnvironmentProfileSummary]":
        _token = next_token
        while True:
            _response = await self.list_environment_profiles(
                domain_identifier,
                config_overrides=config_overrides,
                aws_account_id=aws_account_id,
                aws_account_region=aws_account_region,
                environment_blueprint_identifier=environment_blueprint_identifier,
                project_identifier=project_identifier,
                name=name,
                next_token=_token,
                max_results=max_results,
            )
            _page = _resolve_path(_response, ("items",))
            for _item in _page or []:
                yield _item
            _token = _resolve_path(_response, ("next_token",))
            if not _token:
                break

    async def list_environments(
        self,
        domain_identifier: "capo_datazone.types.domain_id.DomainId",
        project_identifier: "capo_datazone.types.project_id.ProjectId",
        *,
        config_overrides: Optional[AsyncDataZoneClientConfig] = None,
        aws_account_id: Optional[
            "capo_datazone.types.aws_account_id.AwsAccountId"
        ] = None,
        status: Optional[
            "capo_datazone.types.environment_status.EnvironmentStatus"
        ] = None,
        aws_account_region: Optional["capo_datazone.types.aws_region.AwsRegion"] = None,
        environment_profile_identifier: Optional[
            "capo_datazone.types.environment_profile_id.EnvironmentProfileId"
        ] = None,
        environment_blueprint_identifier: Optional[
            "capo_datazone.types.environment_blueprint_id.EnvironmentBlueprintId"
        ] = None,
        provider: Optional[str] = None,
        name: Optional[str] = None,
        max_results: Optional["capo_datazone.types.max_results.MaxResults"] = None,
        next_token: Optional[
            "capo_datazone.types.pagination_token.PaginationToken"
        ] = None,
    ) -> "capo_datazone.types.list_environments_output.ListEnvironmentsOutput":
        """<p>Lists Amazon DataZone environments.</p>

        Args:
            domain_identifier: <p>The identifier of the Amazon DataZone domain.</p>
            aws_account_id: <p>The identifier of the Amazon Web Services account where you want to list environments.</p>
            status: <p>The status of the environments that you want to list.</p>
            aws_account_region: <p>The Amazon Web Services region where you want to list environments.</p>
            project_identifier: <p>The identifier of the Amazon DataZone project.</p>
            environment_profile_identifier: <p>The identifier of the environment profile.</p>
            environment_blueprint_identifier: <p>The identifier of the Amazon DataZone blueprint.</p>
            provider: <p>The provider of the environment.</p>
            name: <p>The name of the environment.</p>
            max_results: <p>The maximum number of environments to return in a single call to <code>ListEnvironments</code>. When the number of environments to be listed is greater than the value of <code>MaxResults</code>, the response contains a <code>NextToken</code> value that you can use in a subsequent call to <code>ListEnvironments</code> to list the next set of environments.</p>
            next_token: <p>When the number of environments is greater than the default value for the <code>MaxResults</code> parameter, or if you explicitly specify a value for <code>MaxResults</code> that is less than the number of environments, the response includes a pagination token named <code>NextToken</code>. You can specify this <code>NextToken</code> value in a subsequent call to <code>ListEnvironments</code> to list the next set of environments.</p>

        Raises:
            capo_datazone.errors.access_denied_exception.AccessDeniedException: <p>You do not have sufficient access to perform this action.</p>
            capo_datazone.errors.throttling_exception.ThrottlingException: <p>The request was denied due to request throttling.</p>
            capo_datazone.errors.unauthorized_exception.UnauthorizedException: <p>You do not have permission to perform this action.</p>
            capo_datazone.errors.internal_server_exception.InternalServerException: <p>The request has failed because of an unknown error, exception or failure.</p>
            capo_datazone.errors.validation_exception.ValidationException: <p>The input fails to satisfy the constraints specified by the Amazon Web Services service.</p>
            capo_datazone.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        async def _handler(
            req: "AsyncOperationRequest[capo_datazone.types.list_environments_input.ListEnvironmentsInput]",
        ) -> AsyncOperationResponse[
            "capo_datazone.types.list_environments_output.ListEnvironmentsOutput"
        ]:
            import capo_datazone._operations.data_zone.list_environments

            (
                output,
                http_response,
            ) = await capo_datazone._operations.data_zone.list_environments.async_list_environments(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_datazone.types.list_environments_input.ListEnvironmentsInput = {
            "domain_identifier": domain_identifier,
            "project_identifier": project_identifier,
        }
        if aws_account_id is not None:
            input_["aws_account_id"] = aws_account_id
        if status is not None:
            input_["status"] = status
        if aws_account_region is not None:
            input_["aws_account_region"] = aws_account_region
        if environment_profile_identifier is not None:
            input_["environment_profile_identifier"] = environment_profile_identifier
        if environment_blueprint_identifier is not None:
            input_["environment_blueprint_identifier"] = (
                environment_blueprint_identifier
            )
        if provider is not None:
            input_["provider"] = provider
        if name is not None:
            input_["name"] = name
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

    async def iter_list_environments(
        self,
        domain_identifier: "capo_datazone.types.domain_id.DomainId",
        project_identifier: "capo_datazone.types.project_id.ProjectId",
        *,
        config_overrides: Optional[AsyncDataZoneClientConfig] = None,
        aws_account_id: Optional[
            "capo_datazone.types.aws_account_id.AwsAccountId"
        ] = None,
        status: Optional[
            "capo_datazone.types.environment_status.EnvironmentStatus"
        ] = None,
        aws_account_region: Optional["capo_datazone.types.aws_region.AwsRegion"] = None,
        environment_profile_identifier: Optional[
            "capo_datazone.types.environment_profile_id.EnvironmentProfileId"
        ] = None,
        environment_blueprint_identifier: Optional[
            "capo_datazone.types.environment_blueprint_id.EnvironmentBlueprintId"
        ] = None,
        provider: Optional[str] = None,
        name: Optional[str] = None,
        max_results: Optional["capo_datazone.types.max_results.MaxResults"] = None,
        next_token: Optional[
            "capo_datazone.types.pagination_token.PaginationToken"
        ] = None,
    ) -> "AsyncIterator[capo_datazone.types.environment_summary.EnvironmentSummary]":
        _token = next_token
        while True:
            _response = await self.list_environments(
                domain_identifier,
                project_identifier,
                config_overrides=config_overrides,
                aws_account_id=aws_account_id,
                status=status,
                aws_account_region=aws_account_region,
                environment_profile_identifier=environment_profile_identifier,
                environment_blueprint_identifier=environment_blueprint_identifier,
                provider=provider,
                name=name,
                max_results=max_results,
                next_token=_token,
            )
            _page = _resolve_path(_response, ("items",))
            for _item in _page or []:
                yield _item
            _token = _resolve_path(_response, ("next_token",))
            if not _token:
                break

    async def list_job_runs(
        self,
        domain_identifier: "capo_datazone.types.domain_id.DomainId",
        job_identifier: str,
        *,
        config_overrides: Optional[AsyncDataZoneClientConfig] = None,
        status: Optional["capo_datazone.types.job_run_status.JobRunStatus"] = None,
        sort_order: Optional["capo_datazone.types.sort_order.SortOrder"] = None,
        next_token: Optional[
            "capo_datazone.types.pagination_token.PaginationToken"
        ] = None,
        max_results: Optional["capo_datazone.types.max_results.MaxResults"] = None,
    ) -> "capo_datazone.types.list_job_runs_output.ListJobRunsOutput":
        """<p>Lists job runs.</p>

        Args:
            domain_identifier: <p>The ID of the domain where you want to list job runs.</p>
            job_identifier: <p>The ID of the job run.</p>
            status: <p>The status of a job run.</p>
            sort_order: <p>Specifies the order in which job runs are to be sorted.</p>
            next_token: <p>When the number of job runs is greater than the default value for the MaxResults parameter, or if you explicitly specify a value for MaxResults that is less than the number of job runs, the response includes a pagination token named NextToken. You can specify this NextToken value in a subsequent call to ListJobRuns to list the next set of job runs.</p>
            max_results: <p>The maximum number of job runs to return in a single call to ListJobRuns. When the number of job runs to be listed is greater than the value of MaxResults, the response contains a NextToken value that you can use in a subsequent call to ListJobRuns to list the next set of job runs.</p>

        Raises:
            capo_datazone.errors.access_denied_exception.AccessDeniedException: <p>You do not have sufficient access to perform this action.</p>
            capo_datazone.errors.throttling_exception.ThrottlingException: <p>The request was denied due to request throttling.</p>
            capo_datazone.errors.unauthorized_exception.UnauthorizedException: <p>You do not have permission to perform this action.</p>
            capo_datazone.errors.internal_server_exception.InternalServerException: <p>The request has failed because of an unknown error, exception or failure.</p>
            capo_datazone.errors.resource_not_found_exception.ResourceNotFoundException: <p>The specified resource cannot be found.</p>
            capo_datazone.errors.validation_exception.ValidationException: <p>The input fails to satisfy the constraints specified by the Amazon Web Services service.</p>
            capo_datazone.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        async def _handler(
            req: "AsyncOperationRequest[capo_datazone.types.list_job_runs_input.ListJobRunsInput]",
        ) -> AsyncOperationResponse[
            "capo_datazone.types.list_job_runs_output.ListJobRunsOutput"
        ]:
            import capo_datazone._operations.data_zone.list_job_runs

            (
                output,
                http_response,
            ) = await capo_datazone._operations.data_zone.list_job_runs.async_list_job_runs(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_datazone.types.list_job_runs_input.ListJobRunsInput = {
            "domain_identifier": domain_identifier,
            "job_identifier": job_identifier,
        }
        if status is not None:
            input_["status"] = status
        if sort_order is not None:
            input_["sort_order"] = sort_order
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

    async def iter_list_job_runs(
        self,
        domain_identifier: "capo_datazone.types.domain_id.DomainId",
        job_identifier: str,
        *,
        config_overrides: Optional[AsyncDataZoneClientConfig] = None,
        status: Optional["capo_datazone.types.job_run_status.JobRunStatus"] = None,
        sort_order: Optional["capo_datazone.types.sort_order.SortOrder"] = None,
        next_token: Optional[
            "capo_datazone.types.pagination_token.PaginationToken"
        ] = None,
        max_results: Optional["capo_datazone.types.max_results.MaxResults"] = None,
    ) -> "AsyncIterator[capo_datazone.types.job_run_summary.JobRunSummary]":
        _token = next_token
        while True:
            _response = await self.list_job_runs(
                domain_identifier,
                job_identifier,
                config_overrides=config_overrides,
                status=status,
                sort_order=sort_order,
                next_token=_token,
                max_results=max_results,
            )
            _page = _resolve_path(_response, ("items",))
            for _item in _page or []:
                yield _item
            _token = _resolve_path(_response, ("next_token",))
            if not _token:
                break

    async def list_lineage_events(
        self,
        domain_identifier: "capo_datazone.types.domain_id.DomainId",
        *,
        config_overrides: Optional[AsyncDataZoneClientConfig] = None,
        max_results: Optional["capo_datazone.types.max_results.MaxResults"] = None,
        timestamp_after: Optional[datetime.datetime] = None,
        timestamp_before: Optional[datetime.datetime] = None,
        processing_status: Optional[
            "capo_datazone.types.lineage_event_processing_status.LineageEventProcessingStatus"
        ] = None,
        sort_order: Optional["capo_datazone.types.sort_order.SortOrder"] = None,
        next_token: Optional[
            "capo_datazone.types.pagination_token.PaginationToken"
        ] = None,
    ) -> "capo_datazone.types.list_lineage_events_output.ListLineageEventsOutput":
        """<p>Lists lineage events.</p>

        Args:
            domain_identifier: <p>The ID of the domain where you want to list lineage events.</p>
            max_results: <p>The maximum number of lineage events to return in a single call to ListLineageEvents. When the number of lineage events to be listed is greater than the value of MaxResults, the response contains a NextToken value that you can use in a subsequent call to ListLineageEvents to list the next set of lineage events.</p>
            timestamp_after: <p>The after timestamp of a lineage event.</p>
            timestamp_before: <p>The before timestamp of a lineage event.</p>
            processing_status: <p>The processing status of a lineage event.</p>
            sort_order: <p>The sort order of the lineage events.</p>
            next_token: <p>When the number of lineage events is greater than the default value for the MaxResults parameter, or if you explicitly specify a value for MaxResults that is less than the number of lineage events, the response includes a pagination token named NextToken. You can specify this NextToken value in a subsequent call to ListLineageEvents to list the next set of lineage events.</p>

        Raises:
            capo_datazone.errors.access_denied_exception.AccessDeniedException: <p>You do not have sufficient access to perform this action.</p>
            capo_datazone.errors.throttling_exception.ThrottlingException: <p>The request was denied due to request throttling.</p>
            capo_datazone.errors.unauthorized_exception.UnauthorizedException: <p>You do not have permission to perform this action.</p>
            capo_datazone.errors.internal_server_exception.InternalServerException: <p>The request has failed because of an unknown error, exception or failure.</p>
            capo_datazone.errors.validation_exception.ValidationException: <p>The input fails to satisfy the constraints specified by the Amazon Web Services service.</p>
            capo_datazone.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        async def _handler(
            req: "AsyncOperationRequest[capo_datazone.types.list_lineage_events_input.ListLineageEventsInput]",
        ) -> AsyncOperationResponse[
            "capo_datazone.types.list_lineage_events_output.ListLineageEventsOutput"
        ]:
            import capo_datazone._operations.data_zone.list_lineage_events

            (
                output,
                http_response,
            ) = await capo_datazone._operations.data_zone.list_lineage_events.async_list_lineage_events(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_datazone.types.list_lineage_events_input.ListLineageEventsInput = {
            "domain_identifier": domain_identifier
        }
        if max_results is not None:
            input_["max_results"] = max_results
        if timestamp_after is not None:
            input_["timestamp_after"] = timestamp_after
        if timestamp_before is not None:
            input_["timestamp_before"] = timestamp_before
        if processing_status is not None:
            input_["processing_status"] = processing_status
        if sort_order is not None:
            input_["sort_order"] = sort_order
        if next_token is not None:
            input_["next_token"] = next_token

        response = await aexecute_pipeline(
            AsyncOperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        await response.response.aclose()
        return response.output

    async def iter_list_lineage_events(
        self,
        domain_identifier: "capo_datazone.types.domain_id.DomainId",
        *,
        config_overrides: Optional[AsyncDataZoneClientConfig] = None,
        max_results: Optional["capo_datazone.types.max_results.MaxResults"] = None,
        timestamp_after: Optional[datetime.datetime] = None,
        timestamp_before: Optional[datetime.datetime] = None,
        processing_status: Optional[
            "capo_datazone.types.lineage_event_processing_status.LineageEventProcessingStatus"
        ] = None,
        sort_order: Optional["capo_datazone.types.sort_order.SortOrder"] = None,
        next_token: Optional[
            "capo_datazone.types.pagination_token.PaginationToken"
        ] = None,
    ) -> "AsyncIterator[capo_datazone.types.lineage_event_summary.LineageEventSummary]":
        _token = next_token
        while True:
            _response = await self.list_lineage_events(
                domain_identifier,
                config_overrides=config_overrides,
                max_results=max_results,
                timestamp_after=timestamp_after,
                timestamp_before=timestamp_before,
                processing_status=processing_status,
                sort_order=sort_order,
                next_token=_token,
            )
            _page = _resolve_path(_response, ("items",))
            for _item in _page or []:
                yield _item
            _token = _resolve_path(_response, ("next_token",))
            if not _token:
                break

    async def list_lineage_node_history(
        self,
        domain_identifier: "capo_datazone.types.domain_id.DomainId",
        identifier: "capo_datazone.types.lineage_node_identifier.LineageNodeIdentifier",
        *,
        config_overrides: Optional[AsyncDataZoneClientConfig] = None,
        max_results: Optional["capo_datazone.types.max_results.MaxResults"] = None,
        next_token: Optional[
            "capo_datazone.types.pagination_token.PaginationToken"
        ] = None,
        direction: Optional["capo_datazone.types.edge_direction.EdgeDirection"] = None,
        event_timestamp_gte: Optional[datetime.datetime] = None,
        event_timestamp_lte: Optional[datetime.datetime] = None,
        sort_order: Optional["capo_datazone.types.sort_order.SortOrder"] = None,
    ) -> "capo_datazone.types.list_lineage_node_history_output.ListLineageNodeHistoryOutput":
        """<p>Lists the history of the specified data lineage node.</p>

        Args:
            domain_identifier: <p>The ID of the domain where you want to list the history of the specified data lineage node.</p>
            max_results: <p>The maximum number of history items to return in a single call to ListLineageNodeHistory. When the number of memberships to be listed is greater than the value of MaxResults, the response contains a NextToken value that you can use in a subsequent call to ListLineageNodeHistory to list the next set of items.</p>
            next_token: <p>When the number of history items is greater than the default value for the MaxResults parameter, or if you explicitly specify a value for MaxResults that is less than the number of items, the response includes a pagination token named NextToken. You can specify this NextToken value in a subsequent call to ListLineageNodeHistory to list the next set of items.</p>
            identifier: <p>The ID of the data lineage node whose history you want to list.</p>
            direction: <p>The direction of the data lineage node refers to the lineage node having neighbors in that direction. For example, if direction is <code>UPSTREAM</code>, the <code>ListLineageNodeHistory</code> API responds with historical versions with upstream neighbors only.</p>
            event_timestamp_gte: <p>Specifies whether the action is to return data lineage node history from the time after the event timestamp.</p>
            event_timestamp_lte: <p>Specifies whether the action is to return data lineage node history from the time prior of the event timestamp.</p>
            sort_order: <p>The order by which you want data lineage node history to be sorted.</p>

        Raises:
            capo_datazone.errors.access_denied_exception.AccessDeniedException: <p>You do not have sufficient access to perform this action.</p>
            capo_datazone.errors.throttling_exception.ThrottlingException: <p>The request was denied due to request throttling.</p>
            capo_datazone.errors.unauthorized_exception.UnauthorizedException: <p>You do not have permission to perform this action.</p>
            capo_datazone.errors.internal_server_exception.InternalServerException: <p>The request has failed because of an unknown error, exception or failure.</p>
            capo_datazone.errors.resource_not_found_exception.ResourceNotFoundException: <p>The specified resource cannot be found.</p>
            capo_datazone.errors.validation_exception.ValidationException: <p>The input fails to satisfy the constraints specified by the Amazon Web Services service.</p>
            capo_datazone.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        async def _handler(
            req: "AsyncOperationRequest[capo_datazone.types.list_lineage_node_history_input.ListLineageNodeHistoryInput]",
        ) -> AsyncOperationResponse[
            "capo_datazone.types.list_lineage_node_history_output.ListLineageNodeHistoryOutput"
        ]:
            import capo_datazone._operations.data_zone.list_lineage_node_history

            (
                output,
                http_response,
            ) = await capo_datazone._operations.data_zone.list_lineage_node_history.async_list_lineage_node_history(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_datazone.types.list_lineage_node_history_input.ListLineageNodeHistoryInput = {
            "domain_identifier": domain_identifier,
            "identifier": identifier,
        }
        if max_results is not None:
            input_["max_results"] = max_results
        if next_token is not None:
            input_["next_token"] = next_token
        if direction is not None:
            input_["direction"] = direction
        if event_timestamp_gte is not None:
            input_["event_timestamp_gte"] = event_timestamp_gte
        if event_timestamp_lte is not None:
            input_["event_timestamp_lte"] = event_timestamp_lte
        if sort_order is not None:
            input_["sort_order"] = sort_order

        response = await aexecute_pipeline(
            AsyncOperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        await response.response.aclose()
        return response.output

    async def iter_list_lineage_node_history(
        self,
        domain_identifier: "capo_datazone.types.domain_id.DomainId",
        identifier: "capo_datazone.types.lineage_node_identifier.LineageNodeIdentifier",
        *,
        config_overrides: Optional[AsyncDataZoneClientConfig] = None,
        max_results: Optional["capo_datazone.types.max_results.MaxResults"] = None,
        next_token: Optional[
            "capo_datazone.types.pagination_token.PaginationToken"
        ] = None,
        direction: Optional["capo_datazone.types.edge_direction.EdgeDirection"] = None,
        event_timestamp_gte: Optional[datetime.datetime] = None,
        event_timestamp_lte: Optional[datetime.datetime] = None,
        sort_order: Optional["capo_datazone.types.sort_order.SortOrder"] = None,
    ) -> "AsyncIterator[capo_datazone.types.lineage_node_summary.LineageNodeSummary]":
        _token = next_token
        while True:
            _response = await self.list_lineage_node_history(
                domain_identifier,
                identifier,
                config_overrides=config_overrides,
                max_results=max_results,
                next_token=_token,
                direction=direction,
                event_timestamp_gte=event_timestamp_gte,
                event_timestamp_lte=event_timestamp_lte,
                sort_order=sort_order,
            )
            _page = _resolve_path(_response, ("nodes",))
            for _item in _page or []:
                yield _item
            _token = _resolve_path(_response, ("next_token",))
            if not _token:
                break

    async def list_notifications(
        self,
        domain_identifier: "capo_datazone.types.domain_id.DomainId",
        type: "capo_datazone.types.notification_type.NotificationType",
        *,
        config_overrides: Optional[AsyncDataZoneClientConfig] = None,
        after_timestamp: Optional[datetime.datetime] = None,
        before_timestamp: Optional[datetime.datetime] = None,
        subjects: Optional[
            "capo_datazone.types.notification_subjects.NotificationSubjects"
        ] = None,
        task_status: Optional["capo_datazone.types.task_status.TaskStatus"] = None,
        max_results: Optional["capo_datazone.types.max_results.MaxResults"] = None,
        next_token: Optional[
            "capo_datazone.types.pagination_token.PaginationToken"
        ] = None,
    ) -> "capo_datazone.types.list_notifications_output.ListNotificationsOutput":
        """<p>Lists all Amazon DataZone notifications.</p>

        Args:
            domain_identifier: <p>The identifier of the Amazon DataZone domain.</p>
            type: <p>The type of notifications.</p>
            after_timestamp: <p>The time after which you want to list notifications.</p>
            before_timestamp: <p>The time before which you want to list notifications.</p>
            subjects: <p>The subjects of notifications.</p>
            task_status: <p>The task status of notifications.</p>
            max_results: <p>The maximum number of notifications to return in a single call to <code>ListNotifications</code>. When the number of notifications to be listed is greater than the value of <code>MaxResults</code>, the response contains a <code>NextToken</code> value that you can use in a subsequent call to <code>ListNotifications</code> to list the next set of notifications.</p>
            next_token: <p>When the number of notifications is greater than the default value for the <code>MaxResults</code> parameter, or if you explicitly specify a value for <code>MaxResults</code> that is less than the number of notifications, the response includes a pagination token named <code>NextToken</code>. You can specify this <code>NextToken</code> value in a subsequent call to <code>ListNotifications</code> to list the next set of notifications.</p>

        Raises:
            capo_datazone.errors.access_denied_exception.AccessDeniedException: <p>You do not have sufficient access to perform this action.</p>
            capo_datazone.errors.throttling_exception.ThrottlingException: <p>The request was denied due to request throttling.</p>
            capo_datazone.errors.unauthorized_exception.UnauthorizedException: <p>You do not have permission to perform this action.</p>
            capo_datazone.errors.internal_server_exception.InternalServerException: <p>The request has failed because of an unknown error, exception or failure.</p>
            capo_datazone.errors.resource_not_found_exception.ResourceNotFoundException: <p>The specified resource cannot be found.</p>
            capo_datazone.errors.validation_exception.ValidationException: <p>The input fails to satisfy the constraints specified by the Amazon Web Services service.</p>
            capo_datazone.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        async def _handler(
            req: "AsyncOperationRequest[capo_datazone.types.list_notifications_input.ListNotificationsInput]",
        ) -> AsyncOperationResponse[
            "capo_datazone.types.list_notifications_output.ListNotificationsOutput"
        ]:
            import capo_datazone._operations.data_zone.list_notifications

            (
                output,
                http_response,
            ) = await capo_datazone._operations.data_zone.list_notifications.async_list_notifications(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_datazone.types.list_notifications_input.ListNotificationsInput = {
            "domain_identifier": domain_identifier,
            "type": type,
        }
        if after_timestamp is not None:
            input_["after_timestamp"] = after_timestamp
        if before_timestamp is not None:
            input_["before_timestamp"] = before_timestamp
        if subjects is not None:
            input_["subjects"] = subjects
        if task_status is not None:
            input_["task_status"] = task_status
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

    async def iter_list_notifications(
        self,
        domain_identifier: "capo_datazone.types.domain_id.DomainId",
        type: "capo_datazone.types.notification_type.NotificationType",
        *,
        config_overrides: Optional[AsyncDataZoneClientConfig] = None,
        after_timestamp: Optional[datetime.datetime] = None,
        before_timestamp: Optional[datetime.datetime] = None,
        subjects: Optional[
            "capo_datazone.types.notification_subjects.NotificationSubjects"
        ] = None,
        task_status: Optional["capo_datazone.types.task_status.TaskStatus"] = None,
        max_results: Optional["capo_datazone.types.max_results.MaxResults"] = None,
        next_token: Optional[
            "capo_datazone.types.pagination_token.PaginationToken"
        ] = None,
    ) -> "AsyncIterator[capo_datazone.types.notification_output.NotificationOutput]":
        _token = next_token
        while True:
            _response = await self.list_notifications(
                domain_identifier,
                type,
                config_overrides=config_overrides,
                after_timestamp=after_timestamp,
                before_timestamp=before_timestamp,
                subjects=subjects,
                task_status=task_status,
                max_results=max_results,
                next_token=_token,
            )
            _page = _resolve_path(_response, ("notifications",))
            for _item in _page or []:
                yield _item
            _token = _resolve_path(_response, ("next_token",))
            if not _token:
                break

    async def list_policy_grants(
        self,
        domain_identifier: "capo_datazone.types.domain_id.DomainId",
        entity_type: "capo_datazone.types.target_entity_type.TargetEntityType",
        entity_identifier: str,
        policy_type: "capo_datazone.types.managed_policy_type.ManagedPolicyType",
        *,
        config_overrides: Optional[AsyncDataZoneClientConfig] = None,
        max_results: Optional[
            "capo_datazone.types.max_results_for_list_domains.MaxResultsForListDomains"
        ] = None,
        next_token: Optional[
            "capo_datazone.types.pagination_token.PaginationToken"
        ] = None,
    ) -> "capo_datazone.types.list_policy_grants_output.ListPolicyGrantsOutput":
        """<p>Lists policy grants.</p>

        Args:
            domain_identifier: <p>The ID of the domain where you want to list policy grants.</p>
            entity_type: <p>The type of entity for which you want to list policy grants.</p>
            entity_identifier: <p>The ID of the entity for which you want to list policy grants.</p>
            policy_type: <p>The type of policy that you want to list.</p>
            max_results: <p>The maximum number of grants to return in a single call to <code>ListPolicyGrants</code>. When the number of grants to be listed is greater than the value of <code>MaxResults</code>, the response contains a <code>NextToken</code> value that you can use in a subsequent call to <code>ListPolicyGrants</code> to list the next set of grants.</p>
            next_token: <p>When the number of grants is greater than the default value for the <code>MaxResults</code> parameter, or if you explicitly specify a value for <code>MaxResults</code> that is less than the number of grants, the response includes a pagination token named <code>NextToken</code>. You can specify this <code>NextToken</code> value in a subsequent call to <code>ListPolicyGrants</code> to list the next set of grants.</p>

        Raises:
            capo_datazone.errors.access_denied_exception.AccessDeniedException: <p>You do not have sufficient access to perform this action.</p>
            capo_datazone.errors.throttling_exception.ThrottlingException: <p>The request was denied due to request throttling.</p>
            capo_datazone.errors.unauthorized_exception.UnauthorizedException: <p>You do not have permission to perform this action.</p>
            capo_datazone.errors.internal_server_exception.InternalServerException: <p>The request has failed because of an unknown error, exception or failure.</p>
            capo_datazone.errors.validation_exception.ValidationException: <p>The input fails to satisfy the constraints specified by the Amazon Web Services service.</p>
            capo_datazone.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        async def _handler(
            req: "AsyncOperationRequest[capo_datazone.types.list_policy_grants_input.ListPolicyGrantsInput]",
        ) -> AsyncOperationResponse[
            "capo_datazone.types.list_policy_grants_output.ListPolicyGrantsOutput"
        ]:
            import capo_datazone._operations.data_zone.list_policy_grants

            (
                output,
                http_response,
            ) = await capo_datazone._operations.data_zone.list_policy_grants.async_list_policy_grants(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_datazone.types.list_policy_grants_input.ListPolicyGrantsInput = {
            "domain_identifier": domain_identifier,
            "entity_type": entity_type,
            "entity_identifier": entity_identifier,
            "policy_type": policy_type,
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

    async def iter_list_policy_grants(
        self,
        domain_identifier: "capo_datazone.types.domain_id.DomainId",
        entity_type: "capo_datazone.types.target_entity_type.TargetEntityType",
        entity_identifier: str,
        policy_type: "capo_datazone.types.managed_policy_type.ManagedPolicyType",
        *,
        config_overrides: Optional[AsyncDataZoneClientConfig] = None,
        max_results: Optional[
            "capo_datazone.types.max_results_for_list_domains.MaxResultsForListDomains"
        ] = None,
        next_token: Optional[
            "capo_datazone.types.pagination_token.PaginationToken"
        ] = None,
    ) -> "AsyncIterator[capo_datazone.types.policy_grant_member.PolicyGrantMember]":
        _token = next_token
        while True:
            _response = await self.list_policy_grants(
                domain_identifier,
                entity_type,
                entity_identifier,
                policy_type,
                config_overrides=config_overrides,
                max_results=max_results,
                next_token=_token,
            )
            _page = _resolve_path(_response, ("grant_list",))
            for _item in _page or []:
                yield _item
            _token = _resolve_path(_response, ("next_token",))
            if not _token:
                break

    async def list_project_memberships(
        self,
        domain_identifier: "capo_datazone.types.domain_id.DomainId",
        project_identifier: "capo_datazone.types.project_id.ProjectId",
        *,
        config_overrides: Optional[AsyncDataZoneClientConfig] = None,
        sort_by: Optional[
            "capo_datazone.types.sort_field_project.SortFieldProject"
        ] = None,
        sort_order: Optional["capo_datazone.types.sort_order.SortOrder"] = None,
        next_token: Optional[
            "capo_datazone.types.pagination_token.PaginationToken"
        ] = None,
        max_results: Optional["capo_datazone.types.max_results.MaxResults"] = None,
    ) -> "capo_datazone.types.list_project_memberships_output.ListProjectMembershipsOutput":
        """<p>Lists all members of the specified project.</p>

        Args:
            domain_identifier: <p>The identifier of the Amazon DataZone domain in which you want to list project memberships.</p>
            project_identifier: <p>The identifier of the project whose memberships you want to list.</p>
            sort_by: <p>The method by which you want to sort the project memberships.</p>
            sort_order: <p>The sort order of the project memberships.</p>
            next_token: <p>When the number of memberships is greater than the default value for the <code>MaxResults</code> parameter, or if you explicitly specify a value for <code>MaxResults</code> that is less than the number of memberships, the response includes a pagination token named <code>NextToken</code>. You can specify this <code>NextToken</code> value in a subsequent call to <code>ListProjectMemberships</code> to list the next set of memberships.</p>
            max_results: <p>The maximum number of memberships to return in a single call to <code>ListProjectMemberships</code>. When the number of memberships to be listed is greater than the value of <code>MaxResults</code>, the response contains a <code>NextToken</code> value that you can use in a subsequent call to <code>ListProjectMemberships</code> to list the next set of memberships.</p>

        Raises:
            capo_datazone.errors.access_denied_exception.AccessDeniedException: <p>You do not have sufficient access to perform this action.</p>
            capo_datazone.errors.throttling_exception.ThrottlingException: <p>The request was denied due to request throttling.</p>
            capo_datazone.errors.unauthorized_exception.UnauthorizedException: <p>You do not have permission to perform this action.</p>
            capo_datazone.errors.internal_server_exception.InternalServerException: <p>The request has failed because of an unknown error, exception or failure.</p>
            capo_datazone.errors.resource_not_found_exception.ResourceNotFoundException: <p>The specified resource cannot be found.</p>
            capo_datazone.errors.validation_exception.ValidationException: <p>The input fails to satisfy the constraints specified by the Amazon Web Services service.</p>
            capo_datazone.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        async def _handler(
            req: "AsyncOperationRequest[capo_datazone.types.list_project_memberships_input.ListProjectMembershipsInput]",
        ) -> AsyncOperationResponse[
            "capo_datazone.types.list_project_memberships_output.ListProjectMembershipsOutput"
        ]:
            import capo_datazone._operations.data_zone.list_project_memberships

            (
                output,
                http_response,
            ) = await capo_datazone._operations.data_zone.list_project_memberships.async_list_project_memberships(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_datazone.types.list_project_memberships_input.ListProjectMembershipsInput = {
            "domain_identifier": domain_identifier,
            "project_identifier": project_identifier,
        }
        if sort_by is not None:
            input_["sort_by"] = sort_by
        if sort_order is not None:
            input_["sort_order"] = sort_order
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

    async def iter_list_project_memberships(
        self,
        domain_identifier: "capo_datazone.types.domain_id.DomainId",
        project_identifier: "capo_datazone.types.project_id.ProjectId",
        *,
        config_overrides: Optional[AsyncDataZoneClientConfig] = None,
        sort_by: Optional[
            "capo_datazone.types.sort_field_project.SortFieldProject"
        ] = None,
        sort_order: Optional["capo_datazone.types.sort_order.SortOrder"] = None,
        next_token: Optional[
            "capo_datazone.types.pagination_token.PaginationToken"
        ] = None,
        max_results: Optional["capo_datazone.types.max_results.MaxResults"] = None,
    ) -> "AsyncIterator[capo_datazone.types.project_member.ProjectMember]":
        _token = next_token
        while True:
            _response = await self.list_project_memberships(
                domain_identifier,
                project_identifier,
                config_overrides=config_overrides,
                sort_by=sort_by,
                sort_order=sort_order,
                next_token=_token,
                max_results=max_results,
            )
            _page = _resolve_path(_response, ("members",))
            for _item in _page or []:
                yield _item
            _token = _resolve_path(_response, ("next_token",))
            if not _token:
                break

    async def list_project_profiles(
        self,
        domain_identifier: "capo_datazone.types.domain_id.DomainId",
        *,
        config_overrides: Optional[AsyncDataZoneClientConfig] = None,
        name: Optional[
            "capo_datazone.types.project_profile_name.ProjectProfileName"
        ] = None,
        sort_by: Optional[
            "capo_datazone.types.sort_field_project.SortFieldProject"
        ] = None,
        sort_order: Optional["capo_datazone.types.sort_order.SortOrder"] = None,
        next_token: Optional[
            "capo_datazone.types.pagination_token.PaginationToken"
        ] = None,
        max_results: Optional["capo_datazone.types.max_results.MaxResults"] = None,
    ) -> "capo_datazone.types.list_project_profiles_output.ListProjectProfilesOutput":
        """<p>Lists project profiles.</p>

        Args:
            domain_identifier: <p>The ID of the domain where you want to list project profiles.</p>
            name: <p>The name of a project profile.</p>
            sort_by: <p>Specifies by what to sort project profiles.</p>
            sort_order: <p>Specifies the sort order of the project profiles.</p>
            next_token: <p>When the number of project profiles is greater than the default value for the MaxResults parameter, or if you explicitly specify a value for MaxResults that is less than the number of project profiles, the response includes a pagination token named NextToken. You can specify this NextToken value in a subsequent call to ListProjectProfiles to list the next set of project profiles.</p>
            max_results: <p>The maximum number of project profiles to return in a single call to ListProjectProfiles. When the number of project profiles to be listed is greater than the value of MaxResults, the response contains a NextToken value that you can use in a subsequent call to ListProjectProfiles to list the next set of project profiles.</p>

        Raises:
            capo_datazone.errors.access_denied_exception.AccessDeniedException: <p>You do not have sufficient access to perform this action.</p>
            capo_datazone.errors.throttling_exception.ThrottlingException: <p>The request was denied due to request throttling.</p>
            capo_datazone.errors.unauthorized_exception.UnauthorizedException: <p>You do not have permission to perform this action.</p>
            capo_datazone.errors.internal_server_exception.InternalServerException: <p>The request has failed because of an unknown error, exception or failure.</p>
            capo_datazone.errors.validation_exception.ValidationException: <p>The input fails to satisfy the constraints specified by the Amazon Web Services service.</p>
            capo_datazone.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        async def _handler(
            req: "AsyncOperationRequest[capo_datazone.types.list_project_profiles_input.ListProjectProfilesInput]",
        ) -> AsyncOperationResponse[
            "capo_datazone.types.list_project_profiles_output.ListProjectProfilesOutput"
        ]:
            import capo_datazone._operations.data_zone.list_project_profiles

            (
                output,
                http_response,
            ) = await capo_datazone._operations.data_zone.list_project_profiles.async_list_project_profiles(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_datazone.types.list_project_profiles_input.ListProjectProfilesInput = {
            "domain_identifier": domain_identifier
        }
        if name is not None:
            input_["name"] = name
        if sort_by is not None:
            input_["sort_by"] = sort_by
        if sort_order is not None:
            input_["sort_order"] = sort_order
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

    async def iter_list_project_profiles(
        self,
        domain_identifier: "capo_datazone.types.domain_id.DomainId",
        *,
        config_overrides: Optional[AsyncDataZoneClientConfig] = None,
        name: Optional[
            "capo_datazone.types.project_profile_name.ProjectProfileName"
        ] = None,
        sort_by: Optional[
            "capo_datazone.types.sort_field_project.SortFieldProject"
        ] = None,
        sort_order: Optional["capo_datazone.types.sort_order.SortOrder"] = None,
        next_token: Optional[
            "capo_datazone.types.pagination_token.PaginationToken"
        ] = None,
        max_results: Optional["capo_datazone.types.max_results.MaxResults"] = None,
    ) -> "AsyncIterator[capo_datazone.types.project_profile_summary.ProjectProfileSummary]":
        _token = next_token
        while True:
            _response = await self.list_project_profiles(
                domain_identifier,
                config_overrides=config_overrides,
                name=name,
                sort_by=sort_by,
                sort_order=sort_order,
                next_token=_token,
                max_results=max_results,
            )
            _page = _resolve_path(_response, ("items",))
            for _item in _page or []:
                yield _item
            _token = _resolve_path(_response, ("next_token",))
            if not _token:
                break

    async def list_projects(
        self,
        domain_identifier: "capo_datazone.types.domain_id.DomainId",
        *,
        config_overrides: Optional[AsyncDataZoneClientConfig] = None,
        user_identifier: Optional[str] = None,
        group_identifier: Optional[str] = None,
        name: Optional["capo_datazone.types.project_name.ProjectName"] = None,
        project_category: Optional[str] = None,
        next_token: Optional[
            "capo_datazone.types.pagination_token.PaginationToken"
        ] = None,
        max_results: Optional["capo_datazone.types.max_results.MaxResults"] = None,
    ) -> "capo_datazone.types.list_projects_output.ListProjectsOutput":
        """<p>Lists Amazon DataZone projects.</p>

        Args:
            domain_identifier: <p>The identifier of the Amazon DataZone domain.</p>
            user_identifier: <p>The identifier of the Amazon DataZone user.</p>
            group_identifier: <p>The identifier of a group.</p>
            name: <p>The name of the project.</p>
            project_category: <p>A parameter to filter projects by their category.</p>
            next_token: <p>When the number of projects is greater than the default value for the <code>MaxResults</code> parameter, or if you explicitly specify a value for <code>MaxResults</code> that is less than the number of projects, the response includes a pagination token named <code>NextToken</code>. You can specify this <code>NextToken</code> value in a subsequent call to <code>ListProjects</code> to list the next set of projects.</p>
            max_results: <p>The maximum number of projects to return in a single call to <code>ListProjects</code>. When the number of projects to be listed is greater than the value of <code>MaxResults</code>, the response contains a <code>NextToken</code> value that you can use in a subsequent call to <code>ListProjects</code> to list the next set of projects.</p>

        Raises:
            capo_datazone.errors.access_denied_exception.AccessDeniedException: <p>You do not have sufficient access to perform this action.</p>
            capo_datazone.errors.throttling_exception.ThrottlingException: <p>The request was denied due to request throttling.</p>
            capo_datazone.errors.unauthorized_exception.UnauthorizedException: <p>You do not have permission to perform this action.</p>
            capo_datazone.errors.internal_server_exception.InternalServerException: <p>The request has failed because of an unknown error, exception or failure.</p>
            capo_datazone.errors.validation_exception.ValidationException: <p>The input fails to satisfy the constraints specified by the Amazon Web Services service.</p>
            capo_datazone.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        async def _handler(
            req: "AsyncOperationRequest[capo_datazone.types.list_projects_input.ListProjectsInput]",
        ) -> AsyncOperationResponse[
            "capo_datazone.types.list_projects_output.ListProjectsOutput"
        ]:
            import capo_datazone._operations.data_zone.list_projects

            (
                output,
                http_response,
            ) = await capo_datazone._operations.data_zone.list_projects.async_list_projects(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_datazone.types.list_projects_input.ListProjectsInput = {
            "domain_identifier": domain_identifier
        }
        if user_identifier is not None:
            input_["user_identifier"] = user_identifier
        if group_identifier is not None:
            input_["group_identifier"] = group_identifier
        if name is not None:
            input_["name"] = name
        if project_category is not None:
            input_["project_category"] = project_category
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

    async def iter_list_projects(
        self,
        domain_identifier: "capo_datazone.types.domain_id.DomainId",
        *,
        config_overrides: Optional[AsyncDataZoneClientConfig] = None,
        user_identifier: Optional[str] = None,
        group_identifier: Optional[str] = None,
        name: Optional["capo_datazone.types.project_name.ProjectName"] = None,
        project_category: Optional[str] = None,
        next_token: Optional[
            "capo_datazone.types.pagination_token.PaginationToken"
        ] = None,
        max_results: Optional["capo_datazone.types.max_results.MaxResults"] = None,
    ) -> "AsyncIterator[capo_datazone.types.project_summary.ProjectSummary]":
        _token = next_token
        while True:
            _response = await self.list_projects(
                domain_identifier,
                config_overrides=config_overrides,
                user_identifier=user_identifier,
                group_identifier=group_identifier,
                name=name,
                project_category=project_category,
                next_token=_token,
                max_results=max_results,
            )
            _page = _resolve_path(_response, ("items",))
            for _item in _page or []:
                yield _item
            _token = _resolve_path(_response, ("next_token",))
            if not _token:
                break

    async def list_subscription_grants(
        self,
        domain_identifier: "capo_datazone.types.domain_id.DomainId",
        *,
        config_overrides: Optional[AsyncDataZoneClientConfig] = None,
        environment_id: Optional[
            "capo_datazone.types.environment_id.EnvironmentId"
        ] = None,
        subscription_target_id: Optional[
            "capo_datazone.types.subscription_target_id.SubscriptionTargetId"
        ] = None,
        subscribed_listing_id: Optional[
            "capo_datazone.types.listing_id.ListingId"
        ] = None,
        subscription_id: Optional[
            "capo_datazone.types.subscription_id.SubscriptionId"
        ] = None,
        owning_project_id: Optional["capo_datazone.types.project_id.ProjectId"] = None,
        owning_iam_principal_arn: Optional[
            "capo_datazone.types.iam_principal_arn.IamPrincipalArn"
        ] = None,
        owning_user_id: Optional[
            "capo_datazone.types.user_profile_id.UserProfileId"
        ] = None,
        owning_group_id: Optional[
            "capo_datazone.types.group_profile_id.GroupProfileId"
        ] = None,
        sort_by: Optional["capo_datazone.types.sort_key.SortKey"] = None,
        sort_order: Optional["capo_datazone.types.sort_order.SortOrder"] = None,
        max_results: Optional["capo_datazone.types.max_results.MaxResults"] = None,
        next_token: Optional[
            "capo_datazone.types.pagination_token.PaginationToken"
        ] = None,
    ) -> "capo_datazone.types.list_subscription_grants_output.ListSubscriptionGrantsOutput":
        """<p>Lists subscription grants.</p>

        Args:
            domain_identifier: <p>The identifier of the Amazon DataZone domain.</p>
            environment_id: <p>The identifier of the Amazon DataZone environment.</p>
            subscription_target_id: <p>The identifier of the subscription target.</p>
            subscribed_listing_id: <p>The identifier of the subscribed listing.</p>
            subscription_id: <p>The identifier of the subscription.</p>
            owning_project_id: <p>The ID of the owning project of the subscription grants.</p>
            owning_iam_principal_arn: <p>The ARN of the owning IAM principal.</p>
            owning_user_id: <p>The ID of the owning user.</p>
            owning_group_id: <p>The ID of the owning group.</p>
            sort_by: <p>Specifies the way of sorting the results of this action.</p>
            sort_order: <p>Specifies the sort order of this action.</p>
            max_results: <p>The maximum number of subscription grants to return in a single call to <code>ListSubscriptionGrants</code>. When the number of subscription grants to be listed is greater than the value of <code>MaxResults</code>, the response contains a <code>NextToken</code> value that you can use in a subsequent call to <code>ListSubscriptionGrants</code> to list the next set of subscription grants.</p>
            next_token: <p>When the number of subscription grants is greater than the default value for the <code>MaxResults</code> parameter, or if you explicitly specify a value for <code>MaxResults</code> that is less than the number of subscription grants, the response includes a pagination token named <code>NextToken</code>. You can specify this <code>NextToken</code> value in a subsequent call to <code>ListSubscriptionGrants</code> to list the next set of subscription grants.</p>

        Raises:
            capo_datazone.errors.access_denied_exception.AccessDeniedException: <p>You do not have sufficient access to perform this action.</p>
            capo_datazone.errors.throttling_exception.ThrottlingException: <p>The request was denied due to request throttling.</p>
            capo_datazone.errors.unauthorized_exception.UnauthorizedException: <p>You do not have permission to perform this action.</p>
            capo_datazone.errors.internal_server_exception.InternalServerException: <p>The request has failed because of an unknown error, exception or failure.</p>
            capo_datazone.errors.resource_not_found_exception.ResourceNotFoundException: <p>The specified resource cannot be found.</p>
            capo_datazone.errors.validation_exception.ValidationException: <p>The input fails to satisfy the constraints specified by the Amazon Web Services service.</p>
            capo_datazone.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        async def _handler(
            req: "AsyncOperationRequest[capo_datazone.types.list_subscription_grants_input.ListSubscriptionGrantsInput]",
        ) -> AsyncOperationResponse[
            "capo_datazone.types.list_subscription_grants_output.ListSubscriptionGrantsOutput"
        ]:
            import capo_datazone._operations.data_zone.list_subscription_grants

            (
                output,
                http_response,
            ) = await capo_datazone._operations.data_zone.list_subscription_grants.async_list_subscription_grants(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_datazone.types.list_subscription_grants_input.ListSubscriptionGrantsInput = {
            "domain_identifier": domain_identifier
        }
        if environment_id is not None:
            input_["environment_id"] = environment_id
        if subscription_target_id is not None:
            input_["subscription_target_id"] = subscription_target_id
        if subscribed_listing_id is not None:
            input_["subscribed_listing_id"] = subscribed_listing_id
        if subscription_id is not None:
            input_["subscription_id"] = subscription_id
        if owning_project_id is not None:
            input_["owning_project_id"] = owning_project_id
        if owning_iam_principal_arn is not None:
            input_["owning_iam_principal_arn"] = owning_iam_principal_arn
        if owning_user_id is not None:
            input_["owning_user_id"] = owning_user_id
        if owning_group_id is not None:
            input_["owning_group_id"] = owning_group_id
        if sort_by is not None:
            input_["sort_by"] = sort_by
        if sort_order is not None:
            input_["sort_order"] = sort_order
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

    async def iter_list_subscription_grants(
        self,
        domain_identifier: "capo_datazone.types.domain_id.DomainId",
        *,
        config_overrides: Optional[AsyncDataZoneClientConfig] = None,
        environment_id: Optional[
            "capo_datazone.types.environment_id.EnvironmentId"
        ] = None,
        subscription_target_id: Optional[
            "capo_datazone.types.subscription_target_id.SubscriptionTargetId"
        ] = None,
        subscribed_listing_id: Optional[
            "capo_datazone.types.listing_id.ListingId"
        ] = None,
        subscription_id: Optional[
            "capo_datazone.types.subscription_id.SubscriptionId"
        ] = None,
        owning_project_id: Optional["capo_datazone.types.project_id.ProjectId"] = None,
        owning_iam_principal_arn: Optional[
            "capo_datazone.types.iam_principal_arn.IamPrincipalArn"
        ] = None,
        owning_user_id: Optional[
            "capo_datazone.types.user_profile_id.UserProfileId"
        ] = None,
        owning_group_id: Optional[
            "capo_datazone.types.group_profile_id.GroupProfileId"
        ] = None,
        sort_by: Optional["capo_datazone.types.sort_key.SortKey"] = None,
        sort_order: Optional["capo_datazone.types.sort_order.SortOrder"] = None,
        max_results: Optional["capo_datazone.types.max_results.MaxResults"] = None,
        next_token: Optional[
            "capo_datazone.types.pagination_token.PaginationToken"
        ] = None,
    ) -> "AsyncIterator[capo_datazone.types.subscription_grant_summary.SubscriptionGrantSummary]":
        _token = next_token
        while True:
            _response = await self.list_subscription_grants(
                domain_identifier,
                config_overrides=config_overrides,
                environment_id=environment_id,
                subscription_target_id=subscription_target_id,
                subscribed_listing_id=subscribed_listing_id,
                subscription_id=subscription_id,
                owning_project_id=owning_project_id,
                owning_iam_principal_arn=owning_iam_principal_arn,
                owning_user_id=owning_user_id,
                owning_group_id=owning_group_id,
                sort_by=sort_by,
                sort_order=sort_order,
                max_results=max_results,
                next_token=_token,
            )
            _page = _resolve_path(_response, ("items",))
            for _item in _page or []:
                yield _item
            _token = _resolve_path(_response, ("next_token",))
            if not _token:
                break

    async def list_subscription_requests(
        self,
        domain_identifier: "capo_datazone.types.domain_id.DomainId",
        *,
        config_overrides: Optional[AsyncDataZoneClientConfig] = None,
        status: Optional[
            "capo_datazone.types.subscription_request_status.SubscriptionRequestStatus"
        ] = None,
        subscribed_listing_id: Optional[
            "capo_datazone.types.listing_id.ListingId"
        ] = None,
        owning_project_id: Optional["capo_datazone.types.project_id.ProjectId"] = None,
        owning_iam_principal_arn: Optional[
            "capo_datazone.types.iam_principal_arn.IamPrincipalArn"
        ] = None,
        approver_project_id: Optional[
            "capo_datazone.types.project_id.ProjectId"
        ] = None,
        owning_user_id: Optional[
            "capo_datazone.types.user_profile_id.UserProfileId"
        ] = None,
        owning_group_id: Optional[
            "capo_datazone.types.group_profile_id.GroupProfileId"
        ] = None,
        sort_by: Optional["capo_datazone.types.sort_key.SortKey"] = None,
        sort_order: Optional["capo_datazone.types.sort_order.SortOrder"] = None,
        max_results: Optional["capo_datazone.types.max_results.MaxResults"] = None,
        next_token: Optional[
            "capo_datazone.types.pagination_token.PaginationToken"
        ] = None,
    ) -> "capo_datazone.types.list_subscription_requests_output.ListSubscriptionRequestsOutput":
        """<p>Lists Amazon DataZone subscription requests.</p>

        Args:
            domain_identifier: <p>The identifier of the Amazon DataZone domain.</p>
            status: <p>Specifies the status of the subscription requests.</p> <note> <p>This is not a required parameter, but if not specified, by default, Amazon DataZone returns only <code>PENDING</code> subscription requests. </p> </note>
            subscribed_listing_id: <p>The identifier of the subscribed listing.</p>
            owning_project_id: <p>The identifier of the project for the subscription requests.</p>
            owning_iam_principal_arn: <p>The ARN of the owning IAM principal.</p>
            approver_project_id: <p>The identifier of the subscription request approver's project.</p>
            owning_user_id: <p>The ID of the owning user.</p>
            owning_group_id: <p>The ID of the owning group.</p>
            sort_by: <p>Specifies the way to sort the results of this action.</p>
            sort_order: <p>Specifies the sort order for the results of this action.</p>
            max_results: <p>The maximum number of subscription requests to return in a single call to <code>ListSubscriptionRequests</code>. When the number of subscription requests to be listed is greater than the value of <code>MaxResults</code>, the response contains a <code>NextToken</code> value that you can use in a subsequent call to <code>ListSubscriptionRequests</code> to list the next set of subscription requests.</p>
            next_token: <p>When the number of subscription requests is greater than the default value for the <code>MaxResults</code> parameter, or if you explicitly specify a value for <code>MaxResults</code> that is less than the number of subscription requests, the response includes a pagination token named <code>NextToken</code>. You can specify this <code>NextToken</code> value in a subsequent call to <code>ListSubscriptionRequests</code> to list the next set of subscription requests.</p>

        Raises:
            capo_datazone.errors.access_denied_exception.AccessDeniedException: <p>You do not have sufficient access to perform this action.</p>
            capo_datazone.errors.throttling_exception.ThrottlingException: <p>The request was denied due to request throttling.</p>
            capo_datazone.errors.unauthorized_exception.UnauthorizedException: <p>You do not have permission to perform this action.</p>
            capo_datazone.errors.internal_server_exception.InternalServerException: <p>The request has failed because of an unknown error, exception or failure.</p>
            capo_datazone.errors.resource_not_found_exception.ResourceNotFoundException: <p>The specified resource cannot be found.</p>
            capo_datazone.errors.validation_exception.ValidationException: <p>The input fails to satisfy the constraints specified by the Amazon Web Services service.</p>
            capo_datazone.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        async def _handler(
            req: "AsyncOperationRequest[capo_datazone.types.list_subscription_requests_input.ListSubscriptionRequestsInput]",
        ) -> AsyncOperationResponse[
            "capo_datazone.types.list_subscription_requests_output.ListSubscriptionRequestsOutput"
        ]:
            import capo_datazone._operations.data_zone.list_subscription_requests

            (
                output,
                http_response,
            ) = await capo_datazone._operations.data_zone.list_subscription_requests.async_list_subscription_requests(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_datazone.types.list_subscription_requests_input.ListSubscriptionRequestsInput = {
            "domain_identifier": domain_identifier
        }
        if status is not None:
            input_["status"] = status
        if subscribed_listing_id is not None:
            input_["subscribed_listing_id"] = subscribed_listing_id
        if owning_project_id is not None:
            input_["owning_project_id"] = owning_project_id
        if owning_iam_principal_arn is not None:
            input_["owning_iam_principal_arn"] = owning_iam_principal_arn
        if approver_project_id is not None:
            input_["approver_project_id"] = approver_project_id
        if owning_user_id is not None:
            input_["owning_user_id"] = owning_user_id
        if owning_group_id is not None:
            input_["owning_group_id"] = owning_group_id
        if sort_by is not None:
            input_["sort_by"] = sort_by
        if sort_order is not None:
            input_["sort_order"] = sort_order
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

    async def iter_list_subscription_requests(
        self,
        domain_identifier: "capo_datazone.types.domain_id.DomainId",
        *,
        config_overrides: Optional[AsyncDataZoneClientConfig] = None,
        status: Optional[
            "capo_datazone.types.subscription_request_status.SubscriptionRequestStatus"
        ] = None,
        subscribed_listing_id: Optional[
            "capo_datazone.types.listing_id.ListingId"
        ] = None,
        owning_project_id: Optional["capo_datazone.types.project_id.ProjectId"] = None,
        owning_iam_principal_arn: Optional[
            "capo_datazone.types.iam_principal_arn.IamPrincipalArn"
        ] = None,
        approver_project_id: Optional[
            "capo_datazone.types.project_id.ProjectId"
        ] = None,
        owning_user_id: Optional[
            "capo_datazone.types.user_profile_id.UserProfileId"
        ] = None,
        owning_group_id: Optional[
            "capo_datazone.types.group_profile_id.GroupProfileId"
        ] = None,
        sort_by: Optional["capo_datazone.types.sort_key.SortKey"] = None,
        sort_order: Optional["capo_datazone.types.sort_order.SortOrder"] = None,
        max_results: Optional["capo_datazone.types.max_results.MaxResults"] = None,
        next_token: Optional[
            "capo_datazone.types.pagination_token.PaginationToken"
        ] = None,
    ) -> "AsyncIterator[capo_datazone.types.subscription_request_summary.SubscriptionRequestSummary]":
        _token = next_token
        while True:
            _response = await self.list_subscription_requests(
                domain_identifier,
                config_overrides=config_overrides,
                status=status,
                subscribed_listing_id=subscribed_listing_id,
                owning_project_id=owning_project_id,
                owning_iam_principal_arn=owning_iam_principal_arn,
                approver_project_id=approver_project_id,
                owning_user_id=owning_user_id,
                owning_group_id=owning_group_id,
                sort_by=sort_by,
                sort_order=sort_order,
                max_results=max_results,
                next_token=_token,
            )
            _page = _resolve_path(_response, ("items",))
            for _item in _page or []:
                yield _item
            _token = _resolve_path(_response, ("next_token",))
            if not _token:
                break

    async def list_subscriptions(
        self,
        domain_identifier: "capo_datazone.types.domain_id.DomainId",
        *,
        config_overrides: Optional[AsyncDataZoneClientConfig] = None,
        subscription_request_identifier: Optional[
            "capo_datazone.types.subscription_request_id.SubscriptionRequestId"
        ] = None,
        status: Optional[
            "capo_datazone.types.subscription_status.SubscriptionStatus"
        ] = None,
        subscribed_listing_id: Optional[
            "capo_datazone.types.listing_id.ListingId"
        ] = None,
        owning_project_id: Optional["capo_datazone.types.project_id.ProjectId"] = None,
        owning_iam_principal_arn: Optional[
            "capo_datazone.types.iam_principal_arn.IamPrincipalArn"
        ] = None,
        owning_user_id: Optional[
            "capo_datazone.types.user_profile_id.UserProfileId"
        ] = None,
        owning_group_id: Optional[
            "capo_datazone.types.group_profile_id.GroupProfileId"
        ] = None,
        approver_project_id: Optional[
            "capo_datazone.types.project_id.ProjectId"
        ] = None,
        sort_by: Optional["capo_datazone.types.sort_key.SortKey"] = None,
        sort_order: Optional["capo_datazone.types.sort_order.SortOrder"] = None,
        max_results: Optional["capo_datazone.types.max_results.MaxResults"] = None,
        next_token: Optional[
            "capo_datazone.types.pagination_token.PaginationToken"
        ] = None,
    ) -> "capo_datazone.types.list_subscriptions_output.ListSubscriptionsOutput":
        """<p>Lists subscriptions in Amazon DataZone.</p>

        Args:
            domain_identifier: <p>The identifier of the Amazon DataZone domain.</p>
            subscription_request_identifier: <p>The identifier of the subscription request for the subscriptions that you want to list.</p>
            status: <p>The status of the subscriptions that you want to list.</p> <note> <p>This is not a required parameter, but if not provided, by default, Amazon DataZone returns only <code>APPROVED</code> subscriptions. </p> </note>
            subscribed_listing_id: <p>The identifier of the subscribed listing for the subscriptions that you want to list.</p>
            owning_project_id: <p>The identifier of the owning project.</p>
            owning_iam_principal_arn: <p>The ARN of the owning IAM principal.</p>
            owning_user_id: <p>The ID of the owning user.</p>
            owning_group_id: <p>The ID of the owning group.</p>
            approver_project_id: <p>The identifier of the project for the subscription's approver.</p>
            sort_by: <p>Specifies the way in which the results of this action are to be sorted.</p>
            sort_order: <p>Specifies the sort order for the results of this action.</p>
            max_results: <p>The maximum number of subscriptions to return in a single call to <code>ListSubscriptions</code>. When the number of subscriptions to be listed is greater than the value of <code>MaxResults</code>, the response contains a <code>NextToken</code> value that you can use in a subsequent call to <code>ListSubscriptions</code> to list the next set of Subscriptions. </p>
            next_token: <p>When the number of subscriptions is greater than the default value for the <code>MaxResults</code> parameter, or if you explicitly specify a value for <code>MaxResults</code> that is less than the number of subscriptions, the response includes a pagination token named <code>NextToken</code>. You can specify this <code>NextToken</code> value in a subsequent call to <code>ListSubscriptions</code> to list the next set of subscriptions.</p>

        Raises:
            capo_datazone.errors.access_denied_exception.AccessDeniedException: <p>You do not have sufficient access to perform this action.</p>
            capo_datazone.errors.throttling_exception.ThrottlingException: <p>The request was denied due to request throttling.</p>
            capo_datazone.errors.unauthorized_exception.UnauthorizedException: <p>You do not have permission to perform this action.</p>
            capo_datazone.errors.internal_server_exception.InternalServerException: <p>The request has failed because of an unknown error, exception or failure.</p>
            capo_datazone.errors.resource_not_found_exception.ResourceNotFoundException: <p>The specified resource cannot be found.</p>
            capo_datazone.errors.validation_exception.ValidationException: <p>The input fails to satisfy the constraints specified by the Amazon Web Services service.</p>
            capo_datazone.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        async def _handler(
            req: "AsyncOperationRequest[capo_datazone.types.list_subscriptions_input.ListSubscriptionsInput]",
        ) -> AsyncOperationResponse[
            "capo_datazone.types.list_subscriptions_output.ListSubscriptionsOutput"
        ]:
            import capo_datazone._operations.data_zone.list_subscriptions

            (
                output,
                http_response,
            ) = await capo_datazone._operations.data_zone.list_subscriptions.async_list_subscriptions(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_datazone.types.list_subscriptions_input.ListSubscriptionsInput = {
            "domain_identifier": domain_identifier
        }
        if subscription_request_identifier is not None:
            input_["subscription_request_identifier"] = subscription_request_identifier
        if status is not None:
            input_["status"] = status
        if subscribed_listing_id is not None:
            input_["subscribed_listing_id"] = subscribed_listing_id
        if owning_project_id is not None:
            input_["owning_project_id"] = owning_project_id
        if owning_iam_principal_arn is not None:
            input_["owning_iam_principal_arn"] = owning_iam_principal_arn
        if owning_user_id is not None:
            input_["owning_user_id"] = owning_user_id
        if owning_group_id is not None:
            input_["owning_group_id"] = owning_group_id
        if approver_project_id is not None:
            input_["approver_project_id"] = approver_project_id
        if sort_by is not None:
            input_["sort_by"] = sort_by
        if sort_order is not None:
            input_["sort_order"] = sort_order
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

    async def iter_list_subscriptions(
        self,
        domain_identifier: "capo_datazone.types.domain_id.DomainId",
        *,
        config_overrides: Optional[AsyncDataZoneClientConfig] = None,
        subscription_request_identifier: Optional[
            "capo_datazone.types.subscription_request_id.SubscriptionRequestId"
        ] = None,
        status: Optional[
            "capo_datazone.types.subscription_status.SubscriptionStatus"
        ] = None,
        subscribed_listing_id: Optional[
            "capo_datazone.types.listing_id.ListingId"
        ] = None,
        owning_project_id: Optional["capo_datazone.types.project_id.ProjectId"] = None,
        owning_iam_principal_arn: Optional[
            "capo_datazone.types.iam_principal_arn.IamPrincipalArn"
        ] = None,
        owning_user_id: Optional[
            "capo_datazone.types.user_profile_id.UserProfileId"
        ] = None,
        owning_group_id: Optional[
            "capo_datazone.types.group_profile_id.GroupProfileId"
        ] = None,
        approver_project_id: Optional[
            "capo_datazone.types.project_id.ProjectId"
        ] = None,
        sort_by: Optional["capo_datazone.types.sort_key.SortKey"] = None,
        sort_order: Optional["capo_datazone.types.sort_order.SortOrder"] = None,
        max_results: Optional["capo_datazone.types.max_results.MaxResults"] = None,
        next_token: Optional[
            "capo_datazone.types.pagination_token.PaginationToken"
        ] = None,
    ) -> "AsyncIterator[capo_datazone.types.subscription_summary.SubscriptionSummary]":
        _token = next_token
        while True:
            _response = await self.list_subscriptions(
                domain_identifier,
                config_overrides=config_overrides,
                subscription_request_identifier=subscription_request_identifier,
                status=status,
                subscribed_listing_id=subscribed_listing_id,
                owning_project_id=owning_project_id,
                owning_iam_principal_arn=owning_iam_principal_arn,
                owning_user_id=owning_user_id,
                owning_group_id=owning_group_id,
                approver_project_id=approver_project_id,
                sort_by=sort_by,
                sort_order=sort_order,
                max_results=max_results,
                next_token=_token,
            )
            _page = _resolve_path(_response, ("items",))
            for _item in _page or []:
                yield _item
            _token = _resolve_path(_response, ("next_token",))
            if not _token:
                break

    async def list_subscription_targets(
        self,
        domain_identifier: "capo_datazone.types.domain_id.DomainId",
        environment_identifier: "capo_datazone.types.environment_id.EnvironmentId",
        *,
        config_overrides: Optional[AsyncDataZoneClientConfig] = None,
        sort_by: Optional["capo_datazone.types.sort_key.SortKey"] = None,
        sort_order: Optional["capo_datazone.types.sort_order.SortOrder"] = None,
        max_results: Optional["capo_datazone.types.max_results.MaxResults"] = None,
        next_token: Optional[
            "capo_datazone.types.pagination_token.PaginationToken"
        ] = None,
    ) -> "capo_datazone.types.list_subscription_targets_output.ListSubscriptionTargetsOutput":
        """<p>Lists subscription targets in Amazon DataZone.</p>

        Args:
            domain_identifier: <p>The identifier of the Amazon DataZone domain where you want to list subscription targets.</p>
            environment_identifier: <p>The identifier of the environment where you want to list subscription targets.</p>
            sort_by: <p>Specifies the way in which the results of this action are to be sorted.</p>
            sort_order: <p>Specifies the sort order for the results of this action.</p>
            max_results: <p>The maximum number of subscription targets to return in a single call to <code>ListSubscriptionTargets</code>. When the number of subscription targets to be listed is greater than the value of <code>MaxResults</code>, the response contains a <code>NextToken</code> value that you can use in a subsequent call to <code>ListSubscriptionTargets</code> to list the next set of subscription targets. </p>
            next_token: <p>When the number of subscription targets is greater than the default value for the <code>MaxResults</code> parameter, or if you explicitly specify a value for <code>MaxResults</code> that is less than the number of subscription targets, the response includes a pagination token named <code>NextToken</code>. You can specify this <code>NextToken</code> value in a subsequent call to <code>ListSubscriptionTargets</code> to list the next set of subscription targets.</p>

        Raises:
            capo_datazone.errors.access_denied_exception.AccessDeniedException: <p>You do not have sufficient access to perform this action.</p>
            capo_datazone.errors.throttling_exception.ThrottlingException: <p>The request was denied due to request throttling.</p>
            capo_datazone.errors.unauthorized_exception.UnauthorizedException: <p>You do not have permission to perform this action.</p>
            capo_datazone.errors.internal_server_exception.InternalServerException: <p>The request has failed because of an unknown error, exception or failure.</p>
            capo_datazone.errors.resource_not_found_exception.ResourceNotFoundException: <p>The specified resource cannot be found.</p>
            capo_datazone.errors.validation_exception.ValidationException: <p>The input fails to satisfy the constraints specified by the Amazon Web Services service.</p>
            capo_datazone.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        async def _handler(
            req: "AsyncOperationRequest[capo_datazone.types.list_subscription_targets_input.ListSubscriptionTargetsInput]",
        ) -> AsyncOperationResponse[
            "capo_datazone.types.list_subscription_targets_output.ListSubscriptionTargetsOutput"
        ]:
            import capo_datazone._operations.data_zone.list_subscription_targets

            (
                output,
                http_response,
            ) = await capo_datazone._operations.data_zone.list_subscription_targets.async_list_subscription_targets(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_datazone.types.list_subscription_targets_input.ListSubscriptionTargetsInput = {
            "domain_identifier": domain_identifier,
            "environment_identifier": environment_identifier,
        }
        if sort_by is not None:
            input_["sort_by"] = sort_by
        if sort_order is not None:
            input_["sort_order"] = sort_order
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

    async def iter_list_subscription_targets(
        self,
        domain_identifier: "capo_datazone.types.domain_id.DomainId",
        environment_identifier: "capo_datazone.types.environment_id.EnvironmentId",
        *,
        config_overrides: Optional[AsyncDataZoneClientConfig] = None,
        sort_by: Optional["capo_datazone.types.sort_key.SortKey"] = None,
        sort_order: Optional["capo_datazone.types.sort_order.SortOrder"] = None,
        max_results: Optional["capo_datazone.types.max_results.MaxResults"] = None,
        next_token: Optional[
            "capo_datazone.types.pagination_token.PaginationToken"
        ] = None,
    ) -> "AsyncIterator[capo_datazone.types.subscription_target_summary.SubscriptionTargetSummary]":
        _token = next_token
        while True:
            _response = await self.list_subscription_targets(
                domain_identifier,
                environment_identifier,
                config_overrides=config_overrides,
                sort_by=sort_by,
                sort_order=sort_order,
                max_results=max_results,
                next_token=_token,
            )
            _page = _resolve_path(_response, ("items",))
            for _item in _page or []:
                yield _item
            _token = _resolve_path(_response, ("next_token",))
            if not _token:
                break

    async def list_tags_for_resource(
        self,
        resource_arn: str,
        *,
        config_overrides: Optional[AsyncDataZoneClientConfig] = None,
    ) -> "capo_datazone.types.list_tags_for_resource_response.ListTagsForResourceResponse":
        """<p>Lists tags for the specified resource in Amazon DataZone.</p>

        Args:
            resource_arn: <p>The ARN of the resource whose tags you want to list.</p>

        Raises:
            capo_datazone.errors.access_denied_exception.AccessDeniedException: <p>You do not have sufficient access to perform this action.</p>
            capo_datazone.errors.throttling_exception.ThrottlingException: <p>The request was denied due to request throttling.</p>
            capo_datazone.errors.unauthorized_exception.UnauthorizedException: <p>You do not have permission to perform this action.</p>
            capo_datazone.errors.internal_server_exception.InternalServerException: <p>The request has failed because of an unknown error, exception or failure.</p>
            capo_datazone.errors.resource_not_found_exception.ResourceNotFoundException: <p>The specified resource cannot be found.</p>
            capo_datazone.errors.validation_exception.ValidationException: <p>The input fails to satisfy the constraints specified by the Amazon Web Services service.</p>
            capo_datazone.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        async def _handler(
            req: "AsyncOperationRequest[capo_datazone.types.list_tags_for_resource_request.ListTagsForResourceRequest]",
        ) -> AsyncOperationResponse[
            "capo_datazone.types.list_tags_for_resource_response.ListTagsForResourceResponse"
        ]:
            import capo_datazone._operations.data_zone.list_tags_for_resource

            (
                output,
                http_response,
            ) = await capo_datazone._operations.data_zone.list_tags_for_resource.async_list_tags_for_resource(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_datazone.types.list_tags_for_resource_request.ListTagsForResourceRequest = {
            "resource_arn": resource_arn
        }

        response = await aexecute_pipeline(
            AsyncOperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        await response.response.aclose()
        return response.output

    async def list_time_series_data_points(
        self,
        domain_identifier: "capo_datazone.types.domain_id.DomainId",
        entity_identifier: "capo_datazone.types.entity_identifier.EntityIdentifier",
        entity_type: "capo_datazone.types.time_series_entity_type.TimeSeriesEntityType",
        form_name: "capo_datazone.types.time_series_form_name.TimeSeriesFormName",
        *,
        config_overrides: Optional[AsyncDataZoneClientConfig] = None,
        started_at: Optional[datetime.datetime] = None,
        ended_at: Optional[datetime.datetime] = None,
        next_token: Optional[
            "capo_datazone.types.pagination_token.PaginationToken"
        ] = None,
        max_results: Optional["capo_datazone.types.max_results.MaxResults"] = None,
    ) -> "capo_datazone.types.list_time_series_data_points_output.ListTimeSeriesDataPointsOutput":
        """<p>Lists time series data points.</p>

        Args:
            domain_identifier: <p>The ID of the Amazon DataZone domain that houses the assets for which you want to list time series data points.</p>
            entity_identifier: <p>The ID of the asset for which you want to list data points.</p>
            entity_type: <p>The type of the asset for which you want to list data points.</p>
            form_name: <p>The name of the time series data points form.</p>
            started_at: <p>The timestamp at which the data points that you want to list started.</p>
            ended_at: <p>The timestamp at which the data points that you wanted to list ended.</p>
            next_token: <p>When the number of data points is greater than the default value for the MaxResults parameter, or if you explicitly specify a value for MaxResults that is less than the number of data points, the response includes a pagination token named NextToken. You can specify this NextToken value in a subsequent call to ListTimeSeriesDataPoints to list the next set of data points.</p>
            max_results: <p>The maximum number of data points to return in a single call to ListTimeSeriesDataPoints. When the number of data points to be listed is greater than the value of MaxResults, the response contains a NextToken value that you can use in a subsequent call to ListTimeSeriesDataPoints to list the next set of data points.</p>

        Raises:
            capo_datazone.errors.access_denied_exception.AccessDeniedException: <p>You do not have sufficient access to perform this action.</p>
            capo_datazone.errors.throttling_exception.ThrottlingException: <p>The request was denied due to request throttling.</p>
            capo_datazone.errors.unauthorized_exception.UnauthorizedException: <p>You do not have permission to perform this action.</p>
            capo_datazone.errors.internal_server_exception.InternalServerException: <p>The request has failed because of an unknown error, exception or failure.</p>
            capo_datazone.errors.resource_not_found_exception.ResourceNotFoundException: <p>The specified resource cannot be found.</p>
            capo_datazone.errors.validation_exception.ValidationException: <p>The input fails to satisfy the constraints specified by the Amazon Web Services service.</p>
            capo_datazone.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        async def _handler(
            req: "AsyncOperationRequest[capo_datazone.types.list_time_series_data_points_input.ListTimeSeriesDataPointsInput]",
        ) -> AsyncOperationResponse[
            "capo_datazone.types.list_time_series_data_points_output.ListTimeSeriesDataPointsOutput"
        ]:
            import capo_datazone._operations.data_zone.list_time_series_data_points

            (
                output,
                http_response,
            ) = await capo_datazone._operations.data_zone.list_time_series_data_points.async_list_time_series_data_points(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_datazone.types.list_time_series_data_points_input.ListTimeSeriesDataPointsInput = {
            "domain_identifier": domain_identifier,
            "entity_identifier": entity_identifier,
            "entity_type": entity_type,
            "form_name": form_name,
        }
        if started_at is not None:
            input_["started_at"] = started_at
        if ended_at is not None:
            input_["ended_at"] = ended_at
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

    async def iter_list_time_series_data_points(
        self,
        domain_identifier: "capo_datazone.types.domain_id.DomainId",
        entity_identifier: "capo_datazone.types.entity_identifier.EntityIdentifier",
        entity_type: "capo_datazone.types.time_series_entity_type.TimeSeriesEntityType",
        form_name: "capo_datazone.types.time_series_form_name.TimeSeriesFormName",
        *,
        config_overrides: Optional[AsyncDataZoneClientConfig] = None,
        started_at: Optional[datetime.datetime] = None,
        ended_at: Optional[datetime.datetime] = None,
        next_token: Optional[
            "capo_datazone.types.pagination_token.PaginationToken"
        ] = None,
        max_results: Optional["capo_datazone.types.max_results.MaxResults"] = None,
    ) -> "AsyncIterator[capo_datazone.types.time_series_data_point_summary_form_output.TimeSeriesDataPointSummaryFormOutput]":
        _token = next_token
        while True:
            _response = await self.list_time_series_data_points(
                domain_identifier,
                entity_identifier,
                entity_type,
                form_name,
                config_overrides=config_overrides,
                started_at=started_at,
                ended_at=ended_at,
                next_token=_token,
                max_results=max_results,
            )
            _page = _resolve_path(_response, ("items",))
            for _item in _page or []:
                yield _item
            _token = _resolve_path(_response, ("next_token",))
            if not _token:
                break

    async def post_lineage_event(
        self,
        domain_identifier: "capo_datazone.types.domain_id.DomainId",
        event: "capo_datazone.types.lineage_event.LineageEvent",
        *,
        config_overrides: Optional[AsyncDataZoneClientConfig] = None,
        client_token: Optional["capo_datazone.types.client_token.ClientToken"] = None,
    ) -> "capo_datazone.types.post_lineage_event_output.PostLineageEventOutput":
        """<p>Posts a data lineage event.</p>

        Args:
            domain_identifier: <p>The ID of the domain where you want to post a data lineage event.</p>
            event: <p>The data lineage event that you want to post. Only open-lineage run event are supported as events. </p>
            client_token: <p>A unique, case-sensitive identifier that is provided to ensure the idempotency of the request.</p>

        Raises:
            capo_datazone.errors.access_denied_exception.AccessDeniedException: <p>You do not have sufficient access to perform this action.</p>
            capo_datazone.errors.throttling_exception.ThrottlingException: <p>The request was denied due to request throttling.</p>
            capo_datazone.errors.unauthorized_exception.UnauthorizedException: <p>You do not have permission to perform this action.</p>
            capo_datazone.errors.conflict_exception.ConflictException: <p>There is a conflict while performing this action.</p>
            capo_datazone.errors.internal_server_exception.InternalServerException: <p>The request has failed because of an unknown error, exception or failure.</p>
            capo_datazone.errors.resource_not_found_exception.ResourceNotFoundException: <p>The specified resource cannot be found.</p>
            capo_datazone.errors.service_quota_exceeded_exception.ServiceQuotaExceededException: <p>The request has exceeded the specified service quota.</p>
            capo_datazone.errors.validation_exception.ValidationException: <p>The input fails to satisfy the constraints specified by the Amazon Web Services service.</p>
            capo_datazone.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        async def _handler(
            req: "AsyncOperationRequest[capo_datazone.types.post_lineage_event_input.PostLineageEventInput]",
        ) -> AsyncOperationResponse[
            "capo_datazone.types.post_lineage_event_output.PostLineageEventOutput"
        ]:
            import capo_datazone._operations.data_zone.post_lineage_event

            (
                output,
                http_response,
            ) = await capo_datazone._operations.data_zone.post_lineage_event.async_post_lineage_event(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_datazone.types.post_lineage_event_input.PostLineageEventInput = {
            "domain_identifier": domain_identifier,
            "event": event,
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

    async def post_time_series_data_points(
        self,
        domain_identifier: "capo_datazone.types.domain_id.DomainId",
        entity_identifier: "capo_datazone.types.entity_identifier.EntityIdentifier",
        entity_type: "capo_datazone.types.time_series_entity_type.TimeSeriesEntityType",
        forms: "capo_datazone.types.time_series_data_point_form_input_list.TimeSeriesDataPointFormInputList",
        *,
        config_overrides: Optional[AsyncDataZoneClientConfig] = None,
        client_token: Optional["capo_datazone.types.client_token.ClientToken"] = None,
    ) -> "capo_datazone.types.post_time_series_data_points_output.PostTimeSeriesDataPointsOutput":
        """<p>Posts time series data points to Amazon DataZone for the specified asset.</p>

        Args:
            domain_identifier: <p>The ID of the Amazon DataZone domain in which you want to post time series data points.</p>
            entity_identifier: <p>The ID of the asset for which you want to post time series data points.</p>
            entity_type: <p>The type of the asset for which you want to post data points.</p>
            forms: <p>The forms that contain the data points that you want to post.</p>
            client_token: <p>A unique, case-sensitive identifier that is provided to ensure the idempotency of the request.</p>

        Raises:
            capo_datazone.errors.access_denied_exception.AccessDeniedException: <p>You do not have sufficient access to perform this action.</p>
            capo_datazone.errors.throttling_exception.ThrottlingException: <p>The request was denied due to request throttling.</p>
            capo_datazone.errors.unauthorized_exception.UnauthorizedException: <p>You do not have permission to perform this action.</p>
            capo_datazone.errors.conflict_exception.ConflictException: <p>There is a conflict while performing this action.</p>
            capo_datazone.errors.internal_server_exception.InternalServerException: <p>The request has failed because of an unknown error, exception or failure.</p>
            capo_datazone.errors.resource_not_found_exception.ResourceNotFoundException: <p>The specified resource cannot be found.</p>
            capo_datazone.errors.service_quota_exceeded_exception.ServiceQuotaExceededException: <p>The request has exceeded the specified service quota.</p>
            capo_datazone.errors.validation_exception.ValidationException: <p>The input fails to satisfy the constraints specified by the Amazon Web Services service.</p>
            capo_datazone.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        async def _handler(
            req: "AsyncOperationRequest[capo_datazone.types.post_time_series_data_points_input.PostTimeSeriesDataPointsInput]",
        ) -> AsyncOperationResponse[
            "capo_datazone.types.post_time_series_data_points_output.PostTimeSeriesDataPointsOutput"
        ]:
            import capo_datazone._operations.data_zone.post_time_series_data_points

            (
                output,
                http_response,
            ) = await capo_datazone._operations.data_zone.post_time_series_data_points.async_post_time_series_data_points(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_datazone.types.post_time_series_data_points_input.PostTimeSeriesDataPointsInput = {
            "domain_identifier": domain_identifier,
            "entity_identifier": entity_identifier,
            "entity_type": entity_type,
            "forms": forms,
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

    async def put_data_export_configuration(
        self,
        domain_identifier: "capo_datazone.types.domain_id.DomainId",
        enable_export: bool,
        *,
        config_overrides: Optional[AsyncDataZoneClientConfig] = None,
        encryption_configuration: Optional[
            "capo_datazone.types.encryption_configuration.EncryptionConfiguration"
        ] = None,
        client_token: Optional["capo_datazone.types.client_token.ClientToken"] = None,
    ) -> "capo_datazone.types.put_data_export_configuration_output.PutDataExportConfigurationOutput":
        """<p>Creates data export configuration details.</p> <p>If you want to temporarily disable export and later re-enable it for the same domain, use the <code>--no-enable-export</code> flag to disable and the <code>--enable-export</code> flag to re-enable. This preserves the configuration and allows you to re-enable export without deleting S3 table.</p> <note> <p>You can enable asset metadata export for only one domain per account per Region. To enable export for a different domain, complete the following steps:</p> <ol> <li> <p>Delete the export configuration for the currently enabled domain using the DeleteDataExportConfiguration operation.</p> </li> <li> <p>Delete the asset S3 table under the aws-sagemaker-catalog S3 table bucket. We recommend backing up the S3 table before deletion.</p> </li> <li> <p>Call the PutDataExportConfiguration API to enable export for the new domain.</p> </li> </ol> </note>

        Args:
            domain_identifier: <p>The domain ID for which you want to create data export configuration details.</p>
            enable_export: <p>Specifies that the export is to be enabled as part of creating data export configuration details.</p>
            encryption_configuration: <p>The encryption configuration as part of creating data export configuration details.</p> <p>The KMS key provided here as part of encryptionConfiguration must have the required permissions as described in <a href="https://docs.aws.amazon.com/sagemaker-unified-studio/latest/adminguide/sagemaker-unified-studio-export-asset-metadata-kms-permissions.html">KMS permissions for exporting asset metadata in Amazon SageMaker Unified Studio</a>.</p>
            client_token: <p>A unique, case-sensitive identifier to ensure idempotency of the request. This field is automatically populated if not provided.</p>

        Raises:
            capo_datazone.errors.access_denied_exception.AccessDeniedException: <p>You do not have sufficient access to perform this action.</p>
            capo_datazone.errors.throttling_exception.ThrottlingException: <p>The request was denied due to request throttling.</p>
            capo_datazone.errors.unauthorized_exception.UnauthorizedException: <p>You do not have permission to perform this action.</p>
            capo_datazone.errors.conflict_exception.ConflictException: <p>There is a conflict while performing this action.</p>
            capo_datazone.errors.internal_server_exception.InternalServerException: <p>The request has failed because of an unknown error, exception or failure.</p>
            capo_datazone.errors.resource_not_found_exception.ResourceNotFoundException: <p>The specified resource cannot be found.</p>
            capo_datazone.errors.service_quota_exceeded_exception.ServiceQuotaExceededException: <p>The request has exceeded the specified service quota.</p>
            capo_datazone.errors.validation_exception.ValidationException: <p>The input fails to satisfy the constraints specified by the Amazon Web Services service.</p>
            capo_datazone.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        async def _handler(
            req: "AsyncOperationRequest[capo_datazone.types.put_data_export_configuration_input.PutDataExportConfigurationInput]",
        ) -> AsyncOperationResponse[
            "capo_datazone.types.put_data_export_configuration_output.PutDataExportConfigurationOutput"
        ]:
            import capo_datazone._operations.data_zone.put_data_export_configuration

            (
                output,
                http_response,
            ) = await capo_datazone._operations.data_zone.put_data_export_configuration.async_put_data_export_configuration(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_datazone.types.put_data_export_configuration_input.PutDataExportConfigurationInput = {
            "domain_identifier": domain_identifier,
            "enable_export": enable_export,
        }
        if encryption_configuration is not None:
            input_["encryption_configuration"] = encryption_configuration
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

    async def query_graph(
        self,
        domain_identifier: "capo_datazone.types.domain_id.DomainId",
        match: "capo_datazone.types.match_clauses.MatchClauses",
        *,
        config_overrides: Optional[AsyncDataZoneClientConfig] = None,
        max_results: Optional["capo_datazone.types.max_results.MaxResults"] = None,
        next_token: Optional[
            "capo_datazone.types.pagination_token.PaginationToken"
        ] = None,
        additional_attributes: Optional[
            "capo_datazone.types.additional_attributes.AdditionalAttributes"
        ] = None,
    ) -> "capo_datazone.types.query_graph_output.QueryGraphOutput":
        """<p>Queries entities in the graph store.</p>

        Args:
            domain_identifier: <p>The identifier of the Amazon DataZone domain.</p>
            match: <p>List of query match clauses.</p>
            max_results: <p>The maximum number of entities to return in a single call to <code>QueryGraph</code>. When the number of entities to be listed is greater than the value of <code>MaxResults</code>, the response contains a <code>NextToken</code> value that you can use in a subsequent call to <code>QueryGraph</code> to list the next set of entities.</p>
            next_token: <p>When the number of entities is greater than the default value for the <code>MaxResults</code> parameter, or if you explicitly specify a value for <code>MaxResults</code> that is less than the number of entities, the response includes a pagination token named <code>NextToken</code>. You can specify this <code>NextToken</code> value in a subsequent call to <code>QueryGraph</code> to list the next set of entities.</p>
            additional_attributes: <p>Additional details on the queried entity that can be requested in the response.</p>

        Raises:
            capo_datazone.errors.access_denied_exception.AccessDeniedException: <p>You do not have sufficient access to perform this action.</p>
            capo_datazone.errors.throttling_exception.ThrottlingException: <p>The request was denied due to request throttling.</p>
            capo_datazone.errors.unauthorized_exception.UnauthorizedException: <p>You do not have permission to perform this action.</p>
            capo_datazone.errors.internal_server_exception.InternalServerException: <p>The request has failed because of an unknown error, exception or failure.</p>
            capo_datazone.errors.validation_exception.ValidationException: <p>The input fails to satisfy the constraints specified by the Amazon Web Services service.</p>
            capo_datazone.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        async def _handler(
            req: "AsyncOperationRequest[capo_datazone.types.query_graph_input.QueryGraphInput]",
        ) -> AsyncOperationResponse[
            "capo_datazone.types.query_graph_output.QueryGraphOutput"
        ]:
            import capo_datazone._operations.data_zone.query_graph

            (
                output,
                http_response,
            ) = await capo_datazone._operations.data_zone.query_graph.async_query_graph(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_datazone.types.query_graph_input.QueryGraphInput = {
            "domain_identifier": domain_identifier,
            "match": match,
        }
        if max_results is not None:
            input_["max_results"] = max_results
        if next_token is not None:
            input_["next_token"] = next_token
        if additional_attributes is not None:
            input_["additional_attributes"] = additional_attributes

        response = await aexecute_pipeline(
            AsyncOperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        await response.response.aclose()
        return response.output

    async def iter_query_graph(
        self,
        domain_identifier: "capo_datazone.types.domain_id.DomainId",
        match: "capo_datazone.types.match_clauses.MatchClauses",
        *,
        config_overrides: Optional[AsyncDataZoneClientConfig] = None,
        max_results: Optional["capo_datazone.types.max_results.MaxResults"] = None,
        next_token: Optional[
            "capo_datazone.types.pagination_token.PaginationToken"
        ] = None,
        additional_attributes: Optional[
            "capo_datazone.types.additional_attributes.AdditionalAttributes"
        ] = None,
    ) -> "AsyncIterator[capo_datazone.types.result_item.ResultItem]":
        _token = next_token
        while True:
            _response = await self.query_graph(
                domain_identifier,
                match,
                config_overrides=config_overrides,
                max_results=max_results,
                next_token=_token,
                additional_attributes=additional_attributes,
            )
            _page = _resolve_path(_response, ("items",))
            for _item in _page or []:
                yield _item
            _token = _resolve_path(_response, ("next_token",))
            if not _token:
                break

    async def reject_predictions(
        self,
        domain_identifier: "capo_datazone.types.domain_id.DomainId",
        identifier: "capo_datazone.types.asset_identifier.AssetIdentifier",
        *,
        config_overrides: Optional[AsyncDataZoneClientConfig] = None,
        revision: Optional["capo_datazone.types.revision.Revision"] = None,
        reject_rule: Optional["capo_datazone.types.reject_rule.RejectRule"] = None,
        reject_choices: Optional[
            "capo_datazone.types.reject_choices.RejectChoices"
        ] = None,
        client_token: Optional["capo_datazone.types.client_token.ClientToken"] = None,
    ) -> "capo_datazone.types.reject_predictions_output.RejectPredictionsOutput":
        """<p>Rejects automatically generated business-friendly metadata for your Amazon DataZone assets.</p>

        Args:
            domain_identifier: <p>The identifier of the Amazon DataZone domain.</p>
            identifier: <p>The identifier of the prediction.</p>
            revision: <p>The revision that is to be made to the asset.</p>
            reject_rule: <p>Specifies the rule (or the conditions) under which a prediction can be rejected.</p>
            reject_choices: <p>Specifies the prediction (aka, the automatically generated piece of metadata) and the target (for example, a column name) that can be rejected.</p>
            client_token: <p>A unique, case-sensitive identifier that is provided to ensure the idempotency of the request.</p>

        Raises:
            capo_datazone.errors.access_denied_exception.AccessDeniedException: <p>You do not have sufficient access to perform this action.</p>
            capo_datazone.errors.throttling_exception.ThrottlingException: <p>The request was denied due to request throttling.</p>
            capo_datazone.errors.unauthorized_exception.UnauthorizedException: <p>You do not have permission to perform this action.</p>
            capo_datazone.errors.conflict_exception.ConflictException: <p>There is a conflict while performing this action.</p>
            capo_datazone.errors.internal_server_exception.InternalServerException: <p>The request has failed because of an unknown error, exception or failure.</p>
            capo_datazone.errors.resource_not_found_exception.ResourceNotFoundException: <p>The specified resource cannot be found.</p>
            capo_datazone.errors.validation_exception.ValidationException: <p>The input fails to satisfy the constraints specified by the Amazon Web Services service.</p>
            capo_datazone.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        async def _handler(
            req: "AsyncOperationRequest[capo_datazone.types.reject_predictions_input.RejectPredictionsInput]",
        ) -> AsyncOperationResponse[
            "capo_datazone.types.reject_predictions_output.RejectPredictionsOutput"
        ]:
            import capo_datazone._operations.data_zone.reject_predictions

            (
                output,
                http_response,
            ) = await capo_datazone._operations.data_zone.reject_predictions.async_reject_predictions(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_datazone.types.reject_predictions_input.RejectPredictionsInput = {
            "domain_identifier": domain_identifier,
            "identifier": identifier,
        }
        if revision is not None:
            input_["revision"] = revision
        if reject_rule is not None:
            input_["reject_rule"] = reject_rule
        if reject_choices is not None:
            input_["reject_choices"] = reject_choices
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

    async def reject_subscription_request(
        self,
        domain_identifier: "capo_datazone.types.domain_id.DomainId",
        identifier: "capo_datazone.types.subscription_request_id.SubscriptionRequestId",
        *,
        config_overrides: Optional[AsyncDataZoneClientConfig] = None,
        decision_comment: Optional[
            "capo_datazone.types.decision_comment.DecisionComment"
        ] = None,
    ) -> "capo_datazone.types.reject_subscription_request_output.RejectSubscriptionRequestOutput":
        """<p>Rejects the specified subscription request.</p>

        Args:
            domain_identifier: <p>The identifier of the Amazon DataZone domain in which the subscription request was rejected.</p>
            identifier: <p>The identifier of the subscription request that was rejected.</p>
            decision_comment: <p>The decision comment of the rejected subscription request.</p>

        Raises:
            capo_datazone.errors.access_denied_exception.AccessDeniedException: <p>You do not have sufficient access to perform this action.</p>
            capo_datazone.errors.throttling_exception.ThrottlingException: <p>The request was denied due to request throttling.</p>
            capo_datazone.errors.unauthorized_exception.UnauthorizedException: <p>You do not have permission to perform this action.</p>
            capo_datazone.errors.conflict_exception.ConflictException: <p>There is a conflict while performing this action.</p>
            capo_datazone.errors.internal_server_exception.InternalServerException: <p>The request has failed because of an unknown error, exception or failure.</p>
            capo_datazone.errors.resource_not_found_exception.ResourceNotFoundException: <p>The specified resource cannot be found.</p>
            capo_datazone.errors.validation_exception.ValidationException: <p>The input fails to satisfy the constraints specified by the Amazon Web Services service.</p>
            capo_datazone.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        async def _handler(
            req: "AsyncOperationRequest[capo_datazone.types.reject_subscription_request_input.RejectSubscriptionRequestInput]",
        ) -> AsyncOperationResponse[
            "capo_datazone.types.reject_subscription_request_output.RejectSubscriptionRequestOutput"
        ]:
            import capo_datazone._operations.data_zone.reject_subscription_request

            (
                output,
                http_response,
            ) = await capo_datazone._operations.data_zone.reject_subscription_request.async_reject_subscription_request(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_datazone.types.reject_subscription_request_input.RejectSubscriptionRequestInput = {
            "domain_identifier": domain_identifier,
            "identifier": identifier,
        }
        if decision_comment is not None:
            input_["decision_comment"] = decision_comment

        response = await aexecute_pipeline(
            AsyncOperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        await response.response.aclose()
        return response.output

    async def remove_entity_owner(
        self,
        domain_identifier: "capo_datazone.types.domain_id.DomainId",
        entity_type: "capo_datazone.types.data_zone_entity_type.DataZoneEntityType",
        entity_identifier: str,
        owner: "capo_datazone.types.owner_properties.OwnerProperties",
        *,
        config_overrides: Optional[AsyncDataZoneClientConfig] = None,
        client_token: Optional["capo_datazone.types.client_token.ClientToken"] = None,
    ) -> "capo_datazone.types.remove_entity_owner_output.RemoveEntityOwnerOutput":
        """<p>Removes an owner from an entity.</p>

        Args:
            domain_identifier: <p>The ID of the domain where you want to remove an owner from an entity.</p>
            entity_type: <p>The type of the entity from which you want to remove an owner.</p>
            entity_identifier: <p>The ID of the entity from which you want to remove an owner.</p>
            owner: <p>The owner that you want to remove from an entity.</p>
            client_token: <p>A unique, case-sensitive identifier that is provided to ensure the idempotency of the request.</p>

        Raises:
            capo_datazone.errors.access_denied_exception.AccessDeniedException: <p>You do not have sufficient access to perform this action.</p>
            capo_datazone.errors.throttling_exception.ThrottlingException: <p>The request was denied due to request throttling.</p>
            capo_datazone.errors.unauthorized_exception.UnauthorizedException: <p>You do not have permission to perform this action.</p>
            capo_datazone.errors.internal_server_exception.InternalServerException: <p>The request has failed because of an unknown error, exception or failure.</p>
            capo_datazone.errors.resource_not_found_exception.ResourceNotFoundException: <p>The specified resource cannot be found.</p>
            capo_datazone.errors.validation_exception.ValidationException: <p>The input fails to satisfy the constraints specified by the Amazon Web Services service.</p>
            capo_datazone.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        async def _handler(
            req: "AsyncOperationRequest[capo_datazone.types.remove_entity_owner_input.RemoveEntityOwnerInput]",
        ) -> AsyncOperationResponse[
            "capo_datazone.types.remove_entity_owner_output.RemoveEntityOwnerOutput"
        ]:
            import capo_datazone._operations.data_zone.remove_entity_owner

            (
                output,
                http_response,
            ) = await capo_datazone._operations.data_zone.remove_entity_owner.async_remove_entity_owner(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_datazone.types.remove_entity_owner_input.RemoveEntityOwnerInput = {
            "domain_identifier": domain_identifier,
            "entity_type": entity_type,
            "entity_identifier": entity_identifier,
            "owner": owner,
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

    async def remove_policy_grant(
        self,
        domain_identifier: "capo_datazone.types.domain_id.DomainId",
        entity_type: "capo_datazone.types.target_entity_type.TargetEntityType",
        entity_identifier: str,
        policy_type: "capo_datazone.types.managed_policy_type.ManagedPolicyType",
        principal: "capo_datazone.types.policy_grant_principal.PolicyGrantPrincipal",
        *,
        config_overrides: Optional[AsyncDataZoneClientConfig] = None,
        grant_identifier: Optional[
            "capo_datazone.types.grant_identifier.GrantIdentifier"
        ] = None,
        client_token: Optional["capo_datazone.types.client_token.ClientToken"] = None,
    ) -> "capo_datazone.types.remove_policy_grant_output.RemovePolicyGrantOutput":
        """<p>Removes a policy grant.</p>

        Args:
            domain_identifier: <p>The ID of the domain where you want to remove a policy grant.</p>
            entity_type: <p>The type of the entity from which you want to remove a policy grant.</p>
            entity_identifier: <p>The ID of the entity from which you want to remove a policy grant.</p>
            policy_type: <p>The type of the policy that you want to remove.</p>
            principal: <p>The principal from which you want to remove a policy grant.</p>
            grant_identifier: <p>The ID of the policy grant that is to be removed from a specified entity.</p>
            client_token: <p>A unique, case-sensitive identifier that is provided to ensure the idempotency of the request.</p>

        Raises:
            capo_datazone.errors.access_denied_exception.AccessDeniedException: <p>You do not have sufficient access to perform this action.</p>
            capo_datazone.errors.throttling_exception.ThrottlingException: <p>The request was denied due to request throttling.</p>
            capo_datazone.errors.unauthorized_exception.UnauthorizedException: <p>You do not have permission to perform this action.</p>
            capo_datazone.errors.internal_server_exception.InternalServerException: <p>The request has failed because of an unknown error, exception or failure.</p>
            capo_datazone.errors.validation_exception.ValidationException: <p>The input fails to satisfy the constraints specified by the Amazon Web Services service.</p>
            capo_datazone.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        async def _handler(
            req: "AsyncOperationRequest[capo_datazone.types.remove_policy_grant_input.RemovePolicyGrantInput]",
        ) -> AsyncOperationResponse[
            "capo_datazone.types.remove_policy_grant_output.RemovePolicyGrantOutput"
        ]:
            import capo_datazone._operations.data_zone.remove_policy_grant

            (
                output,
                http_response,
            ) = await capo_datazone._operations.data_zone.remove_policy_grant.async_remove_policy_grant(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_datazone.types.remove_policy_grant_input.RemovePolicyGrantInput = {
            "domain_identifier": domain_identifier,
            "entity_type": entity_type,
            "entity_identifier": entity_identifier,
            "policy_type": policy_type,
            "principal": principal,
        }
        if grant_identifier is not None:
            input_["grant_identifier"] = grant_identifier
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

    async def revoke_subscription(
        self,
        domain_identifier: "capo_datazone.types.domain_id.DomainId",
        identifier: "capo_datazone.types.subscription_id.SubscriptionId",
        *,
        config_overrides: Optional[AsyncDataZoneClientConfig] = None,
        retain_permissions: Optional[bool] = None,
    ) -> "capo_datazone.types.revoke_subscription_output.RevokeSubscriptionOutput":
        """<p>Revokes a specified subscription in Amazon DataZone.</p>

        Args:
            domain_identifier: <p>The identifier of the Amazon DataZone domain where you want to revoke a subscription.</p>
            identifier: <p>The identifier of the revoked subscription.</p>
            retain_permissions: <p>Specifies whether permissions are retained when the subscription is revoked.</p>

        Raises:
            capo_datazone.errors.access_denied_exception.AccessDeniedException: <p>You do not have sufficient access to perform this action.</p>
            capo_datazone.errors.throttling_exception.ThrottlingException: <p>The request was denied due to request throttling.</p>
            capo_datazone.errors.unauthorized_exception.UnauthorizedException: <p>You do not have permission to perform this action.</p>
            capo_datazone.errors.conflict_exception.ConflictException: <p>There is a conflict while performing this action.</p>
            capo_datazone.errors.internal_server_exception.InternalServerException: <p>The request has failed because of an unknown error, exception or failure.</p>
            capo_datazone.errors.resource_not_found_exception.ResourceNotFoundException: <p>The specified resource cannot be found.</p>
            capo_datazone.errors.validation_exception.ValidationException: <p>The input fails to satisfy the constraints specified by the Amazon Web Services service.</p>
            capo_datazone.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        async def _handler(
            req: "AsyncOperationRequest[capo_datazone.types.revoke_subscription_input.RevokeSubscriptionInput]",
        ) -> AsyncOperationResponse[
            "capo_datazone.types.revoke_subscription_output.RevokeSubscriptionOutput"
        ]:
            import capo_datazone._operations.data_zone.revoke_subscription

            (
                output,
                http_response,
            ) = await capo_datazone._operations.data_zone.revoke_subscription.async_revoke_subscription(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_datazone.types.revoke_subscription_input.RevokeSubscriptionInput = {
            "domain_identifier": domain_identifier,
            "identifier": identifier,
        }
        if retain_permissions is not None:
            input_["retain_permissions"] = retain_permissions

        response = await aexecute_pipeline(
            AsyncOperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        await response.response.aclose()
        return response.output

    async def search(
        self,
        domain_identifier: "capo_datazone.types.domain_id.DomainId",
        search_scope: "capo_datazone.types.inventory_search_scope.InventorySearchScope",
        *,
        config_overrides: Optional[AsyncDataZoneClientConfig] = None,
        owning_project_identifier: Optional[
            "capo_datazone.types.project_id.ProjectId"
        ] = None,
        max_results: Optional["capo_datazone.types.max_results.MaxResults"] = None,
        next_token: Optional[
            "capo_datazone.types.pagination_token.PaginationToken"
        ] = None,
        search_text: Optional["capo_datazone.types.search_text.SearchText"] = None,
        search_in: Optional["capo_datazone.types.search_in_list.SearchInList"] = None,
        filters: Optional["capo_datazone.types.filter_clause.FilterClause"] = None,
        sort: Optional["capo_datazone.types.search_sort.SearchSort"] = None,
        additional_attributes: Optional[
            "capo_datazone.types.search_output_additional_attributes.SearchOutputAdditionalAttributes"
        ] = None,
    ) -> "capo_datazone.types.search_output.SearchOutput":
        """<p>Searches for assets in Amazon DataZone.</p> <p>Search in Amazon DataZone is a powerful capability that enables users to discover and explore data assets, glossary terms, and data products across their organization. It provides both basic and advanced search functionality, allowing users to find resources based on names, descriptions, metadata, and other attributes. Search can be scoped to specific types of resources (like assets, glossary terms, or data products) and can be filtered using various criteria such as creation date, owner, or status. The search functionality is essential for making the wealth of data resources in an organization discoverable and usable, helping users find the right data for their needs quickly and efficiently.</p> <p>Many search commands in Amazon DataZone are paginated, including <code>search</code> and <code>search-types</code>. When the result set is large, Amazon DataZone returns a <code>nextToken</code> in the response. This token can be used to retrieve the next page of results. </p> <p>Prerequisites:</p> <ul> <li> <p>The --domain-identifier must refer to an existing Amazon DataZone domain. </p> </li> <li> <p>--search-scope must be one of: ASSET, GLOSSARY_TERM, DATA_PRODUCT, or GLOSSARY.</p> </li> <li> <p>The user must have search permissions in the specified domain.</p> </li> <li> <p>If using --filters, ensure that the JSON is well-formed and that each filter includes valid attribute and value keys. </p> </li> <li> <p>For paginated results, be prepared to use --next-token to fetch additional pages.</p> </li> </ul> <p>To run a standard free-text search, the <code>searchText</code> parameter must be supplied. By default, all searchable fields are indexed for semantic search and will return semantic matches for SearchListings queries. To prevent semantic search indexing for a custom form attribute, see the <a href="https://docs.aws.amazon.com/datazone/latest/APIReference/API_CreateFormType.html">CreateFormType API documentation</a>. To run a lexical search query, enclose the query with double quotes (""). This will disable semantic search even for fields that have semantic search enabled and will only return results that contain the keywords wrapped by double quotes (order of tokens in the query is not enforced). Free-text search is supported for all attributes annotated with @amazon.datazone#searchable.</p> <p>To run a filtered search, provide filter clause using the <code>filters</code> parameter. To filter on glossary terms, use the special attribute <code>__DataZoneGlossaryTerms</code>. To filter on an indexed numeric attribute (i.e., a numeric attribute annotated with <code>@amazon.datazone#sortable</code>), provide a filter using the <code>intValue</code> parameter. The filters parameter can also be used to run more advanced free-text searches that target specific attributes (attributes must be annotated with <code>@amazon.datazone#searchable</code> for free-text search). Create/update timestamp filtering is supported using the special <code>creationTime</code>/<code>lastUpdatedTime</code> attributes. Filter types can be mixed and matched to power complex queries.</p> <p> To find out whether an attribute has been annotated and indexed for a given search type, use the GetFormType API to retrieve the form containing the attribute.</p>

        Args:
            domain_identifier: <p>The identifier of the Amazon DataZone domain.</p>
            owning_project_identifier: <p>The identifier of the owning project specified for the search.</p>
            max_results: <p>The maximum number of results to return in a single call to <code>Search</code>. When the number of results to be listed is greater than the value of <code>MaxResults</code>, the response contains a <code>NextToken</code> value that you can use in a subsequent call to <code>Search</code> to list the next set of results.</p>
            next_token: <p>When the number of results is greater than the default value for the <code>MaxResults</code> parameter, or if you explicitly specify a value for <code>MaxResults</code> that is less than the number of results, the response includes a pagination token named <code>NextToken</code>. You can specify this <code>NextToken</code> value in a subsequent call to <code>Search</code> to list the next set of results.</p>
            search_scope: <p>The scope of the search.</p>
            search_text: <p>Specifies the text for which to search.</p>
            search_in: <p>The details of the search.</p>
            filters: <p>Specifies the search filters.</p>
            sort: <p>Specifies the way in which the search results are to be sorted.</p>
            additional_attributes: <p>Specifies additional attributes for the <code>Search</code> action.</p>

        Raises:
            capo_datazone.errors.access_denied_exception.AccessDeniedException: <p>You do not have sufficient access to perform this action.</p>
            capo_datazone.errors.throttling_exception.ThrottlingException: <p>The request was denied due to request throttling.</p>
            capo_datazone.errors.unauthorized_exception.UnauthorizedException: <p>You do not have permission to perform this action.</p>
            capo_datazone.errors.internal_server_exception.InternalServerException: <p>The request has failed because of an unknown error, exception or failure.</p>
            capo_datazone.errors.validation_exception.ValidationException: <p>The input fails to satisfy the constraints specified by the Amazon Web Services service.</p>
            capo_datazone.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        async def _handler(
            req: "AsyncOperationRequest[capo_datazone.types.search_input.SearchInput]",
        ) -> AsyncOperationResponse["capo_datazone.types.search_output.SearchOutput"]:
            import capo_datazone._operations.data_zone.search

            (
                output,
                http_response,
            ) = await capo_datazone._operations.data_zone.search.async_search(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_datazone.types.search_input.SearchInput = {
            "domain_identifier": domain_identifier,
            "search_scope": search_scope,
        }
        if owning_project_identifier is not None:
            input_["owning_project_identifier"] = owning_project_identifier
        if max_results is not None:
            input_["max_results"] = max_results
        if next_token is not None:
            input_["next_token"] = next_token
        if search_text is not None:
            input_["search_text"] = search_text
        if search_in is not None:
            input_["search_in"] = search_in
        if filters is not None:
            input_["filters"] = filters
        if sort is not None:
            input_["sort"] = sort
        if additional_attributes is not None:
            input_["additional_attributes"] = additional_attributes

        response = await aexecute_pipeline(
            AsyncOperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        await response.response.aclose()
        return response.output

    async def iter_search(
        self,
        domain_identifier: "capo_datazone.types.domain_id.DomainId",
        search_scope: "capo_datazone.types.inventory_search_scope.InventorySearchScope",
        *,
        config_overrides: Optional[AsyncDataZoneClientConfig] = None,
        owning_project_identifier: Optional[
            "capo_datazone.types.project_id.ProjectId"
        ] = None,
        max_results: Optional["capo_datazone.types.max_results.MaxResults"] = None,
        next_token: Optional[
            "capo_datazone.types.pagination_token.PaginationToken"
        ] = None,
        search_text: Optional["capo_datazone.types.search_text.SearchText"] = None,
        search_in: Optional["capo_datazone.types.search_in_list.SearchInList"] = None,
        filters: Optional["capo_datazone.types.filter_clause.FilterClause"] = None,
        sort: Optional["capo_datazone.types.search_sort.SearchSort"] = None,
        additional_attributes: Optional[
            "capo_datazone.types.search_output_additional_attributes.SearchOutputAdditionalAttributes"
        ] = None,
    ) -> "AsyncIterator[capo_datazone.types.search_inventory_result_item.SearchInventoryResultItem]":
        _token = next_token
        while True:
            _response = await self.search(
                domain_identifier,
                search_scope,
                config_overrides=config_overrides,
                owning_project_identifier=owning_project_identifier,
                max_results=max_results,
                next_token=_token,
                search_text=search_text,
                search_in=search_in,
                filters=filters,
                sort=sort,
                additional_attributes=additional_attributes,
            )
            _page = _resolve_path(_response, ("items",))
            for _item in _page or []:
                yield _item
            _token = _resolve_path(_response, ("next_token",))
            if not _token:
                break

    async def search_group_profiles(
        self,
        domain_identifier: "capo_datazone.types.domain_id.DomainId",
        group_type: "capo_datazone.types.group_search_type.GroupSearchType",
        *,
        config_overrides: Optional[AsyncDataZoneClientConfig] = None,
        search_text: Optional[
            "capo_datazone.types.group_search_text.GroupSearchText"
        ] = None,
        max_results: Optional["capo_datazone.types.max_results.MaxResults"] = None,
        next_token: Optional[
            "capo_datazone.types.pagination_token.PaginationToken"
        ] = None,
    ) -> "capo_datazone.types.search_group_profiles_output.SearchGroupProfilesOutput":
        """<p>Searches group profiles in Amazon DataZone.</p>

        Args:
            domain_identifier: <p>The identifier of the Amazon DataZone domain in which you want to search group profiles.</p>
            group_type: <p>The group type for which to search.</p>
            search_text: <p>Specifies the text for which to search.</p>
            max_results: <p>The maximum number of results to return in a single call to <code>SearchGroupProfiles</code>. When the number of results to be listed is greater than the value of <code>MaxResults</code>, the response contains a <code>NextToken</code> value that you can use in a subsequent call to <code>SearchGroupProfiles</code> to list the next set of results. </p>
            next_token: <p>When the number of results is greater than the default value for the <code>MaxResults</code> parameter, or if you explicitly specify a value for <code>MaxResults</code> that is less than the number of results, the response includes a pagination token named <code>NextToken</code>. You can specify this <code>NextToken</code> value in a subsequent call to <code>SearchGroupProfiles</code> to list the next set of results.</p>

        Raises:
            capo_datazone.errors.access_denied_exception.AccessDeniedException: <p>You do not have sufficient access to perform this action.</p>
            capo_datazone.errors.throttling_exception.ThrottlingException: <p>The request was denied due to request throttling.</p>
            capo_datazone.errors.unauthorized_exception.UnauthorizedException: <p>You do not have permission to perform this action.</p>
            capo_datazone.errors.internal_server_exception.InternalServerException: <p>The request has failed because of an unknown error, exception or failure.</p>
            capo_datazone.errors.resource_not_found_exception.ResourceNotFoundException: <p>The specified resource cannot be found.</p>
            capo_datazone.errors.validation_exception.ValidationException: <p>The input fails to satisfy the constraints specified by the Amazon Web Services service.</p>
            capo_datazone.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        async def _handler(
            req: "AsyncOperationRequest[capo_datazone.types.search_group_profiles_input.SearchGroupProfilesInput]",
        ) -> AsyncOperationResponse[
            "capo_datazone.types.search_group_profiles_output.SearchGroupProfilesOutput"
        ]:
            import capo_datazone._operations.data_zone.search_group_profiles

            (
                output,
                http_response,
            ) = await capo_datazone._operations.data_zone.search_group_profiles.async_search_group_profiles(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_datazone.types.search_group_profiles_input.SearchGroupProfilesInput = {
            "domain_identifier": domain_identifier,
            "group_type": group_type,
        }
        if search_text is not None:
            input_["search_text"] = search_text
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

    async def iter_search_group_profiles(
        self,
        domain_identifier: "capo_datazone.types.domain_id.DomainId",
        group_type: "capo_datazone.types.group_search_type.GroupSearchType",
        *,
        config_overrides: Optional[AsyncDataZoneClientConfig] = None,
        search_text: Optional[
            "capo_datazone.types.group_search_text.GroupSearchText"
        ] = None,
        max_results: Optional["capo_datazone.types.max_results.MaxResults"] = None,
        next_token: Optional[
            "capo_datazone.types.pagination_token.PaginationToken"
        ] = None,
    ) -> "AsyncIterator[capo_datazone.types.group_profile_summary.GroupProfileSummary]":
        _token = next_token
        while True:
            _response = await self.search_group_profiles(
                domain_identifier,
                group_type,
                config_overrides=config_overrides,
                search_text=search_text,
                max_results=max_results,
                next_token=_token,
            )
            _page = _resolve_path(_response, ("items",))
            for _item in _page or []:
                yield _item
            _token = _resolve_path(_response, ("next_token",))
            if not _token:
                break

    async def search_listings(
        self,
        domain_identifier: "capo_datazone.types.domain_id.DomainId",
        *,
        config_overrides: Optional[AsyncDataZoneClientConfig] = None,
        search_text: Optional[str] = None,
        search_in: Optional["capo_datazone.types.search_in_list.SearchInList"] = None,
        max_results: Optional["capo_datazone.types.max_results.MaxResults"] = None,
        next_token: Optional[
            "capo_datazone.types.pagination_token.PaginationToken"
        ] = None,
        filters: Optional["capo_datazone.types.filter_clause.FilterClause"] = None,
        aggregations: Optional[
            "capo_datazone.types.aggregation_list.AggregationList"
        ] = None,
        sort: Optional["capo_datazone.types.search_sort.SearchSort"] = None,
        additional_attributes: Optional[
            "capo_datazone.types.search_output_additional_attributes.SearchOutputAdditionalAttributes"
        ] = None,
    ) -> "capo_datazone.types.search_listings_output.SearchListingsOutput":
        """<p>Searches listings in Amazon DataZone.</p> <p>SearchListings is a powerful capability that enables users to discover and explore published assets and data products across their organization. It provides both basic and advanced search functionality, allowing users to find resources based on names, descriptions, metadata, and other attributes. SearchListings also supports filtering using various criteria such as creation date, owner, or status. This API is essential for making the wealth of data resources in an organization discoverable and usable, helping users find the right data for their needs quickly and efficiently.</p> <p>SearchListings returns results in a paginated format. When the result set is large, the response will include a nextToken, which can be used to retrieve the next page of results.</p> <p>The SearchListings API gives users flexibility in specifying what kind of search is run.</p> <p>To run a standard free-text search, the <code>searchText</code> parameter must be supplied. By default, all searchable fields are indexed for semantic search and will return semantic matches for SearchListings queries. To prevent semantic search indexing for a custom form attribute, see the <a href="https://docs.aws.amazon.com/datazone/latest/APIReference/API_CreateFormType.html">CreateFormType API documentation</a>. To run a lexical search query, enclose the query with double quotes (""). This will disable semantic search even for fields that have semantic search enabled and will only return results that contain the keywords wrapped by double quotes (order of tokens in the query is not enforced). Free-text search is supported for all attributes annotated with @amazon.datazone#searchable.</p> <p>To run a filtered search, provide filter clause using the <code>filters</code> parameter. To filter on glossary terms, use the special attribute <code>__DataZoneGlossaryTerms</code>. To filter on an indexed numeric attribute (i.e., a numeric attribute annotated with <code>@amazon.datazone#sortable</code>), provide a filter using the <code>intValue</code> parameter. The filters parameter can also be used to run more advanced free-text searches that target specific attributes (attributes must be annotated with <code>@amazon.datazone#searchable</code> for free-text search). Create/update timestamp filtering is supported using the special <code>creationTime</code>/<code>lastUpdatedTime</code> attributes. Filter types can be mixed and matched to power complex queries.</p> <p> To find out whether an attribute has been annotated and indexed for a given search type, use the GetFormType API to retrieve the form containing the attribute.</p>

        Args:
            domain_identifier: <p>The identifier of the domain in which to search listings.</p>
            search_text: <p>Specifies the text for which to search.</p>
            search_in: <p>The details of the search.</p>
            max_results: <p>The maximum number of results to return in a single call to <code>SearchListings</code>. When the number of results to be listed is greater than the value of <code>MaxResults</code>, the response contains a <code>NextToken</code> value that you can use in a subsequent call to <code>SearchListings</code> to list the next set of results. </p>
            next_token: <p>When the number of results is greater than the default value for the <code>MaxResults</code> parameter, or if you explicitly specify a value for <code>MaxResults</code> that is less than the number of results, the response includes a pagination token named <code>NextToken</code>. You can specify this <code>NextToken</code> value in a subsequent call to <code>SearchListings</code> to list the next set of results.</p>
            filters: <p>Specifies the filters for the search of listings.</p>
            aggregations: <p>Enables you to specify one or more attributes to compute and return counts grouped by field values.</p>
            sort: <p>Specifies the way for sorting the search results.</p>
            additional_attributes: <p>Specifies additional attributes for the search.</p>

        Raises:
            capo_datazone.errors.access_denied_exception.AccessDeniedException: <p>You do not have sufficient access to perform this action.</p>
            capo_datazone.errors.throttling_exception.ThrottlingException: <p>The request was denied due to request throttling.</p>
            capo_datazone.errors.unauthorized_exception.UnauthorizedException: <p>You do not have permission to perform this action.</p>
            capo_datazone.errors.internal_server_exception.InternalServerException: <p>The request has failed because of an unknown error, exception or failure.</p>
            capo_datazone.errors.validation_exception.ValidationException: <p>The input fails to satisfy the constraints specified by the Amazon Web Services service.</p>
            capo_datazone.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        async def _handler(
            req: "AsyncOperationRequest[capo_datazone.types.search_listings_input.SearchListingsInput]",
        ) -> AsyncOperationResponse[
            "capo_datazone.types.search_listings_output.SearchListingsOutput"
        ]:
            import capo_datazone._operations.data_zone.search_listings

            (
                output,
                http_response,
            ) = await capo_datazone._operations.data_zone.search_listings.async_search_listings(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_datazone.types.search_listings_input.SearchListingsInput = {
            "domain_identifier": domain_identifier
        }
        if search_text is not None:
            input_["search_text"] = search_text
        if search_in is not None:
            input_["search_in"] = search_in
        if max_results is not None:
            input_["max_results"] = max_results
        if next_token is not None:
            input_["next_token"] = next_token
        if filters is not None:
            input_["filters"] = filters
        if aggregations is not None:
            input_["aggregations"] = aggregations
        if sort is not None:
            input_["sort"] = sort
        if additional_attributes is not None:
            input_["additional_attributes"] = additional_attributes

        response = await aexecute_pipeline(
            AsyncOperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        await response.response.aclose()
        return response.output

    async def iter_search_listings(
        self,
        domain_identifier: "capo_datazone.types.domain_id.DomainId",
        *,
        config_overrides: Optional[AsyncDataZoneClientConfig] = None,
        search_text: Optional[str] = None,
        search_in: Optional["capo_datazone.types.search_in_list.SearchInList"] = None,
        max_results: Optional["capo_datazone.types.max_results.MaxResults"] = None,
        next_token: Optional[
            "capo_datazone.types.pagination_token.PaginationToken"
        ] = None,
        filters: Optional["capo_datazone.types.filter_clause.FilterClause"] = None,
        aggregations: Optional[
            "capo_datazone.types.aggregation_list.AggregationList"
        ] = None,
        sort: Optional["capo_datazone.types.search_sort.SearchSort"] = None,
        additional_attributes: Optional[
            "capo_datazone.types.search_output_additional_attributes.SearchOutputAdditionalAttributes"
        ] = None,
    ) -> "AsyncIterator[capo_datazone.types.search_result_item.SearchResultItem]":
        _token = next_token
        while True:
            _response = await self.search_listings(
                domain_identifier,
                config_overrides=config_overrides,
                search_text=search_text,
                search_in=search_in,
                max_results=max_results,
                next_token=_token,
                filters=filters,
                aggregations=aggregations,
                sort=sort,
                additional_attributes=additional_attributes,
            )
            _page = _resolve_path(_response, ("items",))
            for _item in _page or []:
                yield _item
            _token = _resolve_path(_response, ("next_token",))
            if not _token:
                break

    async def search_types(
        self,
        domain_identifier: "capo_datazone.types.domain_id.DomainId",
        search_scope: "capo_datazone.types.types_search_scope.TypesSearchScope",
        managed: bool,
        *,
        config_overrides: Optional[AsyncDataZoneClientConfig] = None,
        max_results: Optional["capo_datazone.types.max_results.MaxResults"] = None,
        next_token: Optional[
            "capo_datazone.types.pagination_token.PaginationToken"
        ] = None,
        search_text: Optional["capo_datazone.types.search_text.SearchText"] = None,
        search_in: Optional["capo_datazone.types.search_in_list.SearchInList"] = None,
        filters: Optional["capo_datazone.types.filter_clause.FilterClause"] = None,
        sort: Optional["capo_datazone.types.search_sort.SearchSort"] = None,
    ) -> "capo_datazone.types.search_types_output.SearchTypesOutput":
        """<p>Searches for types in Amazon DataZone.</p> <p>Prerequisites:</p> <ul> <li> <p>The --domain-identifier must refer to an existing Amazon DataZone domain. </p> </li> <li> <p>--search-scope must be one of the valid values including: ASSET_TYPE, GLOSSARY_TERM_TYPE, DATA_PRODUCT_TYPE.</p> </li> <li> <p>The --managed flag must be present without a value.</p> </li> <li> <p>The user must have permissions for form or asset types in the domain.</p> </li> <li> <p>If using --filters, ensure that the JSON is valid.</p> </li> <li> <p>Filters contain correct structure (attribute, value, operator).</p> </li> </ul>

        Args:
            domain_identifier: <p>The identifier of the Amazon DataZone domain in which to invoke the <code>SearchTypes</code> action.</p>
            max_results: <p>The maximum number of results to return in a single call to <code>SearchTypes</code>. When the number of results to be listed is greater than the value of <code>MaxResults</code>, the response contains a <code>NextToken</code> value that you can use in a subsequent call to <code>SearchTypes</code> to list the next set of results. </p>
            next_token: <p>When the number of results is greater than the default value for the <code>MaxResults</code> parameter, or if you explicitly specify a value for <code>MaxResults</code> that is less than the number of results, the response includes a pagination token named <code>NextToken</code>. You can specify this <code>NextToken</code> value in a subsequent call to <code>SearchTypes</code> to list the next set of results.</p>
            search_scope: <p>Specifies the scope of the search for types.</p>
            search_text: <p>Specifies the text for which to search.</p>
            search_in: <p>The details of the search.</p>
            filters: <p>The filters for the <code>SearchTypes</code> action.</p>
            sort: <p>The specifies the way to sort the <code>SearchTypes</code> results.</p>
            managed: <p>Specifies whether the search is managed.</p>

        Raises:
            capo_datazone.errors.access_denied_exception.AccessDeniedException: <p>You do not have sufficient access to perform this action.</p>
            capo_datazone.errors.throttling_exception.ThrottlingException: <p>The request was denied due to request throttling.</p>
            capo_datazone.errors.unauthorized_exception.UnauthorizedException: <p>You do not have permission to perform this action.</p>
            capo_datazone.errors.internal_server_exception.InternalServerException: <p>The request has failed because of an unknown error, exception or failure.</p>
            capo_datazone.errors.validation_exception.ValidationException: <p>The input fails to satisfy the constraints specified by the Amazon Web Services service.</p>
            capo_datazone.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        async def _handler(
            req: "AsyncOperationRequest[capo_datazone.types.search_types_input.SearchTypesInput]",
        ) -> AsyncOperationResponse[
            "capo_datazone.types.search_types_output.SearchTypesOutput"
        ]:
            import capo_datazone._operations.data_zone.search_types

            (
                output,
                http_response,
            ) = await capo_datazone._operations.data_zone.search_types.async_search_types(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_datazone.types.search_types_input.SearchTypesInput = {
            "domain_identifier": domain_identifier,
            "search_scope": search_scope,
            "managed": managed,
        }
        if max_results is not None:
            input_["max_results"] = max_results
        if next_token is not None:
            input_["next_token"] = next_token
        if search_text is not None:
            input_["search_text"] = search_text
        if search_in is not None:
            input_["search_in"] = search_in
        if filters is not None:
            input_["filters"] = filters
        if sort is not None:
            input_["sort"] = sort

        response = await aexecute_pipeline(
            AsyncOperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        await response.response.aclose()
        return response.output

    async def iter_search_types(
        self,
        domain_identifier: "capo_datazone.types.domain_id.DomainId",
        search_scope: "capo_datazone.types.types_search_scope.TypesSearchScope",
        managed: bool,
        *,
        config_overrides: Optional[AsyncDataZoneClientConfig] = None,
        max_results: Optional["capo_datazone.types.max_results.MaxResults"] = None,
        next_token: Optional[
            "capo_datazone.types.pagination_token.PaginationToken"
        ] = None,
        search_text: Optional["capo_datazone.types.search_text.SearchText"] = None,
        search_in: Optional["capo_datazone.types.search_in_list.SearchInList"] = None,
        filters: Optional["capo_datazone.types.filter_clause.FilterClause"] = None,
        sort: Optional["capo_datazone.types.search_sort.SearchSort"] = None,
    ) -> "AsyncIterator[capo_datazone.types.search_types_result_item.SearchTypesResultItem]":
        _token = next_token
        while True:
            _response = await self.search_types(
                domain_identifier,
                search_scope,
                managed,
                config_overrides=config_overrides,
                max_results=max_results,
                next_token=_token,
                search_text=search_text,
                search_in=search_in,
                filters=filters,
                sort=sort,
            )
            _page = _resolve_path(_response, ("items",))
            for _item in _page or []:
                yield _item
            _token = _resolve_path(_response, ("next_token",))
            if not _token:
                break

    async def search_user_profiles(
        self,
        domain_identifier: "capo_datazone.types.domain_id.DomainId",
        user_type: "capo_datazone.types.user_search_type.UserSearchType",
        *,
        config_overrides: Optional[AsyncDataZoneClientConfig] = None,
        search_text: Optional[
            "capo_datazone.types.user_search_text.UserSearchText"
        ] = None,
        max_results: Optional["capo_datazone.types.max_results.MaxResults"] = None,
        next_token: Optional[
            "capo_datazone.types.pagination_token.PaginationToken"
        ] = None,
    ) -> "capo_datazone.types.search_user_profiles_output.SearchUserProfilesOutput":
        """<p>Searches user profiles in Amazon DataZone.</p>

        Args:
            domain_identifier: <p>The identifier of the Amazon DataZone domain in which you want to search user profiles.</p>
            user_type: <p>Specifies the user type for the <code>SearchUserProfiles</code> action.</p>
            search_text: <p>Specifies the text for which to search.</p>
            max_results: <p>The maximum number of results to return in a single call to <code>SearchUserProfiles</code>. When the number of results to be listed is greater than the value of <code>MaxResults</code>, the response contains a <code>NextToken</code> value that you can use in a subsequent call to <code>SearchUserProfiles</code> to list the next set of results. </p>
            next_token: <p>When the number of results is greater than the default value for the <code>MaxResults</code> parameter, or if you explicitly specify a value for <code>MaxResults</code> that is less than the number of results, the response includes a pagination token named <code>NextToken</code>. You can specify this <code>NextToken</code> value in a subsequent call to <code>SearchUserProfiles</code> to list the next set of results.</p>

        Raises:
            capo_datazone.errors.access_denied_exception.AccessDeniedException: <p>You do not have sufficient access to perform this action.</p>
            capo_datazone.errors.throttling_exception.ThrottlingException: <p>The request was denied due to request throttling.</p>
            capo_datazone.errors.unauthorized_exception.UnauthorizedException: <p>You do not have permission to perform this action.</p>
            capo_datazone.errors.internal_server_exception.InternalServerException: <p>The request has failed because of an unknown error, exception or failure.</p>
            capo_datazone.errors.resource_not_found_exception.ResourceNotFoundException: <p>The specified resource cannot be found.</p>
            capo_datazone.errors.validation_exception.ValidationException: <p>The input fails to satisfy the constraints specified by the Amazon Web Services service.</p>
            capo_datazone.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        async def _handler(
            req: "AsyncOperationRequest[capo_datazone.types.search_user_profiles_input.SearchUserProfilesInput]",
        ) -> AsyncOperationResponse[
            "capo_datazone.types.search_user_profiles_output.SearchUserProfilesOutput"
        ]:
            import capo_datazone._operations.data_zone.search_user_profiles

            (
                output,
                http_response,
            ) = await capo_datazone._operations.data_zone.search_user_profiles.async_search_user_profiles(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_datazone.types.search_user_profiles_input.SearchUserProfilesInput = {
            "domain_identifier": domain_identifier,
            "user_type": user_type,
        }
        if search_text is not None:
            input_["search_text"] = search_text
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

    async def iter_search_user_profiles(
        self,
        domain_identifier: "capo_datazone.types.domain_id.DomainId",
        user_type: "capo_datazone.types.user_search_type.UserSearchType",
        *,
        config_overrides: Optional[AsyncDataZoneClientConfig] = None,
        search_text: Optional[
            "capo_datazone.types.user_search_text.UserSearchText"
        ] = None,
        max_results: Optional["capo_datazone.types.max_results.MaxResults"] = None,
        next_token: Optional[
            "capo_datazone.types.pagination_token.PaginationToken"
        ] = None,
    ) -> "AsyncIterator[capo_datazone.types.user_profile_summary.UserProfileSummary]":
        _token = next_token
        while True:
            _response = await self.search_user_profiles(
                domain_identifier,
                user_type,
                config_overrides=config_overrides,
                search_text=search_text,
                max_results=max_results,
                next_token=_token,
            )
            _page = _resolve_path(_response, ("items",))
            for _item in _page or []:
                yield _item
            _token = _resolve_path(_response, ("next_token",))
            if not _token:
                break

    async def start_notebook_import(
        self,
        domain_identifier: "capo_datazone.types.domain_id.DomainId",
        owning_project_identifier: "capo_datazone.types.project_id.ProjectId",
        source_location: "capo_datazone.types.source_location.SourceLocation",
        name: "capo_datazone.types.notebook_name.NotebookName",
        *,
        config_overrides: Optional[AsyncDataZoneClientConfig] = None,
        description: Optional["capo_datazone.types.description.Description"] = None,
        client_token: Optional["capo_datazone.types.client_token.ClientToken"] = None,
    ) -> "capo_datazone.types.start_notebook_import_output.StartNotebookImportOutput":
        """<p>Starts a notebook import in Amazon SageMaker Unified Studio. This operation imports a notebook from an Amazon Simple Storage Service location into a project.</p>

        Args:
            domain_identifier: <p>The identifier of the Amazon SageMaker Unified Studio domain in which to import the notebook.</p>
            owning_project_identifier: <p>The identifier of the project that will own the imported notebook.</p>
            source_location: <p>The source location of the notebook to import. This specifies the Amazon Simple Storage Service URI of the notebook file.</p>
            name: <p>The name of the imported notebook. The name must be between 1 and 256 characters.</p>
            description: <p>The description of the imported notebook.</p>
            client_token: <p>A unique, case-sensitive identifier to ensure idempotency of the request. This field is automatically populated if not provided.</p>

        Raises:
            capo_datazone.errors.access_denied_exception.AccessDeniedException: <p>You do not have sufficient access to perform this action.</p>
            capo_datazone.errors.throttling_exception.ThrottlingException: <p>The request was denied due to request throttling.</p>
            capo_datazone.errors.unauthorized_exception.UnauthorizedException: <p>You do not have permission to perform this action.</p>
            capo_datazone.errors.conflict_exception.ConflictException: <p>There is a conflict while performing this action.</p>
            capo_datazone.errors.internal_server_exception.InternalServerException: <p>The request has failed because of an unknown error, exception or failure.</p>
            capo_datazone.errors.resource_not_found_exception.ResourceNotFoundException: <p>The specified resource cannot be found.</p>
            capo_datazone.errors.service_quota_exceeded_exception.ServiceQuotaExceededException: <p>The request has exceeded the specified service quota.</p>
            capo_datazone.errors.validation_exception.ValidationException: <p>The input fails to satisfy the constraints specified by the Amazon Web Services service.</p>
            capo_datazone.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        async def _handler(
            req: "AsyncOperationRequest[capo_datazone.types.start_notebook_import_input.StartNotebookImportInput]",
        ) -> AsyncOperationResponse[
            "capo_datazone.types.start_notebook_import_output.StartNotebookImportOutput"
        ]:
            import capo_datazone._operations.data_zone.start_notebook_import

            (
                output,
                http_response,
            ) = await capo_datazone._operations.data_zone.start_notebook_import.async_start_notebook_import(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_datazone.types.start_notebook_import_input.StartNotebookImportInput = {
            "domain_identifier": domain_identifier,
            "owning_project_identifier": owning_project_identifier,
            "source_location": source_location,
            "name": name,
        }
        if description is not None:
            input_["description"] = description
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

    async def start_notebook_sync(
        self,
        domain_identifier: "capo_datazone.types.domain_id.DomainId",
        owning_project_identifier: "capo_datazone.types.project_id.ProjectId",
        source_location: "capo_datazone.types.source_location.SourceLocation",
        *,
        config_overrides: Optional[AsyncDataZoneClientConfig] = None,
        git_metadata: Optional["capo_datazone.types.git_metadata.GitMetadata"] = None,
        notebook_id: Optional["capo_datazone.types.notebook_id.NotebookId"] = None,
        name: Optional["capo_datazone.types.notebook_name.NotebookName"] = None,
        description: Optional["capo_datazone.types.description.Description"] = None,
        client_token: Optional["capo_datazone.types.client_token.ClientToken"] = None,
    ) -> "capo_datazone.types.start_notebook_sync_output.StartNotebookSyncOutput":
        """<p>Starts a notebook sync in Amazon SageMaker Unified Studio. This operation syncs a notebook from a Git repository into a project.</p>

        Args:
            domain_identifier: <p>The identifier of the Amazon SageMaker Unified Studio domain in which to sync the notebook.</p>
            owning_project_identifier: <p>The identifier of the project that will own the synced notebook.</p>
            source_location: <p>The source location of the notebook to sync. This specifies the Amazon Simple Storage Service URI of the notebook file.</p>
            git_metadata: <p>The Git metadata for the notebook sync, including repository, branch, and commit information.</p>
            notebook_id: <p>The identifier of an existing notebook to sync. If not specified, a new notebook is created.</p>
            name: <p>The name of the notebook. The name must be between 1 and 256 characters.</p>
            description: <p>The description of the notebook.</p>
            client_token: <p>A unique, case-sensitive identifier to ensure idempotency of the request. This field is automatically populated if not provided.</p>

        Raises:
            capo_datazone.errors.access_denied_exception.AccessDeniedException: <p>You do not have sufficient access to perform this action.</p>
            capo_datazone.errors.throttling_exception.ThrottlingException: <p>The request was denied due to request throttling.</p>
            capo_datazone.errors.unauthorized_exception.UnauthorizedException: <p>You do not have permission to perform this action.</p>
            capo_datazone.errors.conflict_exception.ConflictException: <p>There is a conflict while performing this action.</p>
            capo_datazone.errors.internal_server_exception.InternalServerException: <p>The request has failed because of an unknown error, exception or failure.</p>
            capo_datazone.errors.resource_not_found_exception.ResourceNotFoundException: <p>The specified resource cannot be found.</p>
            capo_datazone.errors.service_quota_exceeded_exception.ServiceQuotaExceededException: <p>The request has exceeded the specified service quota.</p>
            capo_datazone.errors.validation_exception.ValidationException: <p>The input fails to satisfy the constraints specified by the Amazon Web Services service.</p>
            capo_datazone.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        async def _handler(
            req: "AsyncOperationRequest[capo_datazone.types.start_notebook_sync_input.StartNotebookSyncInput]",
        ) -> AsyncOperationResponse[
            "capo_datazone.types.start_notebook_sync_output.StartNotebookSyncOutput"
        ]:
            import capo_datazone._operations.data_zone.start_notebook_sync

            (
                output,
                http_response,
            ) = await capo_datazone._operations.data_zone.start_notebook_sync.async_start_notebook_sync(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_datazone.types.start_notebook_sync_input.StartNotebookSyncInput = {
            "domain_identifier": domain_identifier,
            "owning_project_identifier": owning_project_identifier,
            "source_location": source_location,
        }
        if git_metadata is not None:
            input_["git_metadata"] = git_metadata
        if notebook_id is not None:
            input_["notebook_id"] = notebook_id
        if name is not None:
            input_["name"] = name
        if description is not None:
            input_["description"] = description
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
        resource_arn: str,
        tags: "capo_datazone.types.tags.Tags",
        *,
        config_overrides: Optional[AsyncDataZoneClientConfig] = None,
    ) -> "capo_datazone.types.tag_resource_response.TagResourceResponse":
        """<p>Tags a resource in Amazon DataZone.</p>

        Args:
            resource_arn: <p>The ARN of the resource to be tagged in Amazon DataZone.</p>
            tags: <p>Specifies the tags for the <code>TagResource</code> action.</p>

        Raises:
            capo_datazone.errors.access_denied_exception.AccessDeniedException: <p>You do not have sufficient access to perform this action.</p>
            capo_datazone.errors.throttling_exception.ThrottlingException: <p>The request was denied due to request throttling.</p>
            capo_datazone.errors.unauthorized_exception.UnauthorizedException: <p>You do not have permission to perform this action.</p>
            capo_datazone.errors.internal_server_exception.InternalServerException: <p>The request has failed because of an unknown error, exception or failure.</p>
            capo_datazone.errors.resource_not_found_exception.ResourceNotFoundException: <p>The specified resource cannot be found.</p>
            capo_datazone.errors.validation_exception.ValidationException: <p>The input fails to satisfy the constraints specified by the Amazon Web Services service.</p>
            capo_datazone.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        async def _handler(
            req: "AsyncOperationRequest[capo_datazone.types.tag_resource_request.TagResourceRequest]",
        ) -> AsyncOperationResponse[
            "capo_datazone.types.tag_resource_response.TagResourceResponse"
        ]:
            import capo_datazone._operations.data_zone.tag_resource

            (
                output,
                http_response,
            ) = await capo_datazone._operations.data_zone.tag_resource.async_tag_resource(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_datazone.types.tag_resource_request.TagResourceRequest = {
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

    async def untag_resource(
        self,
        resource_arn: str,
        tag_keys: "capo_datazone.types.tag_key_list.TagKeyList",
        *,
        config_overrides: Optional[AsyncDataZoneClientConfig] = None,
    ) -> "capo_datazone.types.untag_resource_response.UntagResourceResponse":
        """<p>Untags a resource in Amazon DataZone.</p>

        Args:
            resource_arn: <p>The ARN of the resource to be untagged in Amazon DataZone.</p>
            tag_keys: <p>Specifies the tag keys for the <code>UntagResource</code> action.</p>

        Raises:
            capo_datazone.errors.access_denied_exception.AccessDeniedException: <p>You do not have sufficient access to perform this action.</p>
            capo_datazone.errors.throttling_exception.ThrottlingException: <p>The request was denied due to request throttling.</p>
            capo_datazone.errors.unauthorized_exception.UnauthorizedException: <p>You do not have permission to perform this action.</p>
            capo_datazone.errors.internal_server_exception.InternalServerException: <p>The request has failed because of an unknown error, exception or failure.</p>
            capo_datazone.errors.resource_not_found_exception.ResourceNotFoundException: <p>The specified resource cannot be found.</p>
            capo_datazone.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        async def _handler(
            req: "AsyncOperationRequest[capo_datazone.types.untag_resource_request.UntagResourceRequest]",
        ) -> AsyncOperationResponse[
            "capo_datazone.types.untag_resource_response.UntagResourceResponse"
        ]:
            import capo_datazone._operations.data_zone.untag_resource

            (
                output,
                http_response,
            ) = await capo_datazone._operations.data_zone.untag_resource.async_untag_resource(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_datazone.types.untag_resource_request.UntagResourceRequest = {
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

    async def update_account_pool(
        self,
        domain_identifier: "capo_datazone.types.domain_id.DomainId",
        identifier: "capo_datazone.types.account_pool_id.AccountPoolId",
        *,
        config_overrides: Optional[AsyncDataZoneClientConfig] = None,
        name: Optional["capo_datazone.types.account_pool_name.AccountPoolName"] = None,
        description: Optional["capo_datazone.types.description.Description"] = None,
        resolution_strategy: Optional[
            "capo_datazone.types.resolution_strategy.ResolutionStrategy"
        ] = None,
        account_source: Optional[
            "capo_datazone.types.account_source.AccountSource"
        ] = None,
    ) -> "capo_datazone.types.update_account_pool_output.UpdateAccountPoolOutput":
        """<p>Updates the account pool.</p>

        Args:
            domain_identifier: <p>The domain ID where the account pool that is to be updated lives.</p>
            identifier: <p>The ID of the account pool that is to be updated.</p>
            name: <p>The name of the account pool that is to be updated.</p>
            description: <p>The description of the account pool that is to be udpated.</p>
            resolution_strategy: <p>The mechanism used to resolve the account selection from the account pool.</p>
            account_source: <p>The source of accounts for the account pool. In the current release, it's either a static list of accounts provided by the customer or a custom Amazon Web Services Lambda handler. </p>

        Raises:
            capo_datazone.errors.access_denied_exception.AccessDeniedException: <p>You do not have sufficient access to perform this action.</p>
            capo_datazone.errors.throttling_exception.ThrottlingException: <p>The request was denied due to request throttling.</p>
            capo_datazone.errors.unauthorized_exception.UnauthorizedException: <p>You do not have permission to perform this action.</p>
            capo_datazone.errors.conflict_exception.ConflictException: <p>There is a conflict while performing this action.</p>
            capo_datazone.errors.internal_server_exception.InternalServerException: <p>The request has failed because of an unknown error, exception or failure.</p>
            capo_datazone.errors.resource_not_found_exception.ResourceNotFoundException: <p>The specified resource cannot be found.</p>
            capo_datazone.errors.service_quota_exceeded_exception.ServiceQuotaExceededException: <p>The request has exceeded the specified service quota.</p>
            capo_datazone.errors.validation_exception.ValidationException: <p>The input fails to satisfy the constraints specified by the Amazon Web Services service.</p>
            capo_datazone.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        async def _handler(
            req: "AsyncOperationRequest[capo_datazone.types.update_account_pool_input.UpdateAccountPoolInput]",
        ) -> AsyncOperationResponse[
            "capo_datazone.types.update_account_pool_output.UpdateAccountPoolOutput"
        ]:
            import capo_datazone._operations.data_zone.update_account_pool

            (
                output,
                http_response,
            ) = await capo_datazone._operations.data_zone.update_account_pool.async_update_account_pool(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_datazone.types.update_account_pool_input.UpdateAccountPoolInput = {
            "domain_identifier": domain_identifier,
            "identifier": identifier,
        }
        if name is not None:
            input_["name"] = name
        if description is not None:
            input_["description"] = description
        if resolution_strategy is not None:
            input_["resolution_strategy"] = resolution_strategy
        if account_source is not None:
            input_["account_source"] = account_source

        response = await aexecute_pipeline(
            AsyncOperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        await response.response.aclose()
        return response.output

    async def update_asset_filter(
        self,
        domain_identifier: "capo_datazone.types.domain_id.DomainId",
        asset_identifier: "capo_datazone.types.asset_id.AssetId",
        identifier: "capo_datazone.types.filter_id.FilterId",
        *,
        config_overrides: Optional[AsyncDataZoneClientConfig] = None,
        name: Optional[str] = None,
        description: Optional["capo_datazone.types.description.Description"] = None,
        configuration: Optional[
            "capo_datazone.types.asset_filter_configuration.AssetFilterConfiguration"
        ] = None,
    ) -> "capo_datazone.types.update_asset_filter_output.UpdateAssetFilterOutput":
        """<p>Updates an asset filter.</p> <p>Prerequisites:</p> <ul> <li> <p>The domain, asset, and asset filter identifier must all exist. </p> </li> <li> <p>The asset must contain the columns being referenced in the update.</p> </li> <li> <p>If applying a row filter, ensure the column referenced in the expression exists in the asset schema.</p> </li> </ul>

        Args:
            domain_identifier: <p>The ID of the domain where you want to update an asset filter.</p>
            asset_identifier: <p>The ID of the data asset.</p>
            identifier: <p>The ID of the asset filter.</p>
            name: <p>The name of the asset filter.</p>
            description: <p>The description of the asset filter.</p>
            configuration: <p>The configuration of the asset filter.</p>

        Raises:
            capo_datazone.errors.access_denied_exception.AccessDeniedException: <p>You do not have sufficient access to perform this action.</p>
            capo_datazone.errors.throttling_exception.ThrottlingException: <p>The request was denied due to request throttling.</p>
            capo_datazone.errors.unauthorized_exception.UnauthorizedException: <p>You do not have permission to perform this action.</p>
            capo_datazone.errors.conflict_exception.ConflictException: <p>There is a conflict while performing this action.</p>
            capo_datazone.errors.internal_server_exception.InternalServerException: <p>The request has failed because of an unknown error, exception or failure.</p>
            capo_datazone.errors.resource_not_found_exception.ResourceNotFoundException: <p>The specified resource cannot be found.</p>
            capo_datazone.errors.validation_exception.ValidationException: <p>The input fails to satisfy the constraints specified by the Amazon Web Services service.</p>
            capo_datazone.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        async def _handler(
            req: "AsyncOperationRequest[capo_datazone.types.update_asset_filter_input.UpdateAssetFilterInput]",
        ) -> AsyncOperationResponse[
            "capo_datazone.types.update_asset_filter_output.UpdateAssetFilterOutput"
        ]:
            import capo_datazone._operations.data_zone.update_asset_filter

            (
                output,
                http_response,
            ) = await capo_datazone._operations.data_zone.update_asset_filter.async_update_asset_filter(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_datazone.types.update_asset_filter_input.UpdateAssetFilterInput = {
            "domain_identifier": domain_identifier,
            "asset_identifier": asset_identifier,
            "identifier": identifier,
        }
        if name is not None:
            input_["name"] = name
        if description is not None:
            input_["description"] = description
        if configuration is not None:
            input_["configuration"] = configuration

        response = await aexecute_pipeline(
            AsyncOperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        await response.response.aclose()
        return response.output

    async def update_connection(
        self,
        domain_identifier: "capo_datazone.types.domain_id.DomainId",
        identifier: "capo_datazone.types.connection_id.ConnectionId",
        *,
        config_overrides: Optional[AsyncDataZoneClientConfig] = None,
        configurations: Optional[
            "capo_datazone.types.configurations.Configurations"
        ] = None,
        description: Optional["capo_datazone.types.description.Description"] = None,
        aws_location: Optional["capo_datazone.types.aws_location.AwsLocation"] = None,
        props: Optional[
            "capo_datazone.types.connection_properties_patch.ConnectionPropertiesPatch"
        ] = None,
    ) -> "capo_datazone.types.update_connection_output.UpdateConnectionOutput":
        """<p>Updates a connection. In Amazon DataZone, a connection enables you to connect your resources (domains, projects, and environments) to external resources and services.</p>

        Args:
            configurations: <p>The configurations of the connection.</p>
            domain_identifier: <p>The ID of the domain where a connection is to be updated.</p>
            identifier: <p>The ID of the connection to be updated.</p>
            description: <p>The description of a connection.</p>
            aws_location: <p>The location where a connection is to be updated.</p>
            props: <p>The connection props.</p>

        Raises:
            capo_datazone.errors.access_denied_exception.AccessDeniedException: <p>You do not have sufficient access to perform this action.</p>
            capo_datazone.errors.throttling_exception.ThrottlingException: <p>The request was denied due to request throttling.</p>
            capo_datazone.errors.unauthorized_exception.UnauthorizedException: <p>You do not have permission to perform this action.</p>
            capo_datazone.errors.conflict_exception.ConflictException: <p>There is a conflict while performing this action.</p>
            capo_datazone.errors.internal_server_exception.InternalServerException: <p>The request has failed because of an unknown error, exception or failure.</p>
            capo_datazone.errors.resource_not_found_exception.ResourceNotFoundException: <p>The specified resource cannot be found.</p>
            capo_datazone.errors.service_quota_exceeded_exception.ServiceQuotaExceededException: <p>The request has exceeded the specified service quota.</p>
            capo_datazone.errors.validation_exception.ValidationException: <p>The input fails to satisfy the constraints specified by the Amazon Web Services service.</p>
            capo_datazone.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        async def _handler(
            req: "AsyncOperationRequest[capo_datazone.types.update_connection_input.UpdateConnectionInput]",
        ) -> AsyncOperationResponse[
            "capo_datazone.types.update_connection_output.UpdateConnectionOutput"
        ]:
            import capo_datazone._operations.data_zone.update_connection

            (
                output,
                http_response,
            ) = await capo_datazone._operations.data_zone.update_connection.async_update_connection(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_datazone.types.update_connection_input.UpdateConnectionInput = {
            "domain_identifier": domain_identifier,
            "identifier": identifier,
        }
        if configurations is not None:
            input_["configurations"] = configurations
        if description is not None:
            input_["description"] = description
        if aws_location is not None:
            input_["aws_location"] = aws_location
        if props is not None:
            input_["props"] = props

        response = await aexecute_pipeline(
            AsyncOperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        await response.response.aclose()
        return response.output

    async def update_environment(
        self,
        domain_identifier: "capo_datazone.types.domain_id.DomainId",
        identifier: "capo_datazone.types.environment_id.EnvironmentId",
        *,
        config_overrides: Optional[AsyncDataZoneClientConfig] = None,
        name: Optional[str] = None,
        description: Optional[str] = None,
        glossary_terms: Optional[
            "capo_datazone.types.glossary_terms.GlossaryTerms"
        ] = None,
        blueprint_version: Optional[str] = None,
        user_parameters: Optional[
            "capo_datazone.types.environment_parameters_list.EnvironmentParametersList"
        ] = None,
        environment_configuration_name: Optional[
            "capo_datazone.types.environment_configuration_name.EnvironmentConfigurationName"
        ] = None,
    ) -> "capo_datazone.types.update_environment_output.UpdateEnvironmentOutput":
        """<p>Updates the specified environment in Amazon DataZone.</p>

        Args:
            domain_identifier: <p>The identifier of the domain in which the environment is to be updated.</p>
            identifier: <p>The identifier of the environment that is to be updated.</p>
            name: <p>The name to be updated as part of the <code>UpdateEnvironment</code> action.</p>
            description: <p>The description to be updated as part of the <code>UpdateEnvironment</code> action.</p>
            glossary_terms: <p>The glossary terms to be updated as part of the <code>UpdateEnvironment</code> action.</p>
            blueprint_version: <p>The blueprint version to which the environment should be updated. You can only specify the following string for this parameter: <code>latest</code>.</p>
            user_parameters: <p>The user parameters of the environment.</p>
            environment_configuration_name: <p>The configuration name of the environment.</p>

        Raises:
            capo_datazone.errors.access_denied_exception.AccessDeniedException: <p>You do not have sufficient access to perform this action.</p>
            capo_datazone.errors.throttling_exception.ThrottlingException: <p>The request was denied due to request throttling.</p>
            capo_datazone.errors.unauthorized_exception.UnauthorizedException: <p>You do not have permission to perform this action.</p>
            capo_datazone.errors.conflict_exception.ConflictException: <p>There is a conflict while performing this action.</p>
            capo_datazone.errors.internal_server_exception.InternalServerException: <p>The request has failed because of an unknown error, exception or failure.</p>
            capo_datazone.errors.service_quota_exceeded_exception.ServiceQuotaExceededException: <p>The request has exceeded the specified service quota.</p>
            capo_datazone.errors.validation_exception.ValidationException: <p>The input fails to satisfy the constraints specified by the Amazon Web Services service.</p>
            capo_datazone.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        async def _handler(
            req: "AsyncOperationRequest[capo_datazone.types.update_environment_input.UpdateEnvironmentInput]",
        ) -> AsyncOperationResponse[
            "capo_datazone.types.update_environment_output.UpdateEnvironmentOutput"
        ]:
            import capo_datazone._operations.data_zone.update_environment

            (
                output,
                http_response,
            ) = await capo_datazone._operations.data_zone.update_environment.async_update_environment(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_datazone.types.update_environment_input.UpdateEnvironmentInput = {
            "domain_identifier": domain_identifier,
            "identifier": identifier,
        }
        if name is not None:
            input_["name"] = name
        if description is not None:
            input_["description"] = description
        if glossary_terms is not None:
            input_["glossary_terms"] = glossary_terms
        if blueprint_version is not None:
            input_["blueprint_version"] = blueprint_version
        if user_parameters is not None:
            input_["user_parameters"] = user_parameters
        if environment_configuration_name is not None:
            input_["environment_configuration_name"] = environment_configuration_name

        response = await aexecute_pipeline(
            AsyncOperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        await response.response.aclose()
        return response.output

    async def update_environment_action(
        self,
        domain_identifier: "capo_datazone.types.domain_id.DomainId",
        environment_identifier: "capo_datazone.types.environment_id.EnvironmentId",
        identifier: str,
        *,
        config_overrides: Optional[AsyncDataZoneClientConfig] = None,
        parameters: Optional[
            "capo_datazone.types.action_parameters.ActionParameters"
        ] = None,
        name: Optional[str] = None,
        description: Optional[str] = None,
    ) -> "capo_datazone.types.update_environment_action_output.UpdateEnvironmentActionOutput":
        """<p>Updates an environment action.</p>

        Args:
            domain_identifier: <p>The domain ID of the environment action.</p>
            environment_identifier: <p>The environment ID of the environment action.</p>
            identifier: <p>The ID of the environment action.</p>
            parameters: <p>The parameters of the environment action.</p>
            name: <p>The name of the environment action.</p>
            description: <p>The description of the environment action.</p>

        Raises:
            capo_datazone.errors.access_denied_exception.AccessDeniedException: <p>You do not have sufficient access to perform this action.</p>
            capo_datazone.errors.throttling_exception.ThrottlingException: <p>The request was denied due to request throttling.</p>
            capo_datazone.errors.unauthorized_exception.UnauthorizedException: <p>You do not have permission to perform this action.</p>
            capo_datazone.errors.conflict_exception.ConflictException: <p>There is a conflict while performing this action.</p>
            capo_datazone.errors.internal_server_exception.InternalServerException: <p>The request has failed because of an unknown error, exception or failure.</p>
            capo_datazone.errors.resource_not_found_exception.ResourceNotFoundException: <p>The specified resource cannot be found.</p>
            capo_datazone.errors.validation_exception.ValidationException: <p>The input fails to satisfy the constraints specified by the Amazon Web Services service.</p>
            capo_datazone.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        async def _handler(
            req: "AsyncOperationRequest[capo_datazone.types.update_environment_action_input.UpdateEnvironmentActionInput]",
        ) -> AsyncOperationResponse[
            "capo_datazone.types.update_environment_action_output.UpdateEnvironmentActionOutput"
        ]:
            import capo_datazone._operations.data_zone.update_environment_action

            (
                output,
                http_response,
            ) = await capo_datazone._operations.data_zone.update_environment_action.async_update_environment_action(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_datazone.types.update_environment_action_input.UpdateEnvironmentActionInput = {
            "domain_identifier": domain_identifier,
            "environment_identifier": environment_identifier,
            "identifier": identifier,
        }
        if parameters is not None:
            input_["parameters"] = parameters
        if name is not None:
            input_["name"] = name
        if description is not None:
            input_["description"] = description

        response = await aexecute_pipeline(
            AsyncOperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        await response.response.aclose()
        return response.output

    async def update_environment_blueprint(
        self,
        domain_identifier: "capo_datazone.types.domain_id.DomainId",
        identifier: "capo_datazone.types.environment_blueprint_id.EnvironmentBlueprintId",
        *,
        config_overrides: Optional[AsyncDataZoneClientConfig] = None,
        description: Optional[str] = None,
        provisioning_properties: Optional[
            "capo_datazone.types.provisioning_properties.ProvisioningProperties"
        ] = None,
        user_parameters: Optional[
            "capo_datazone.types.custom_parameter_list.CustomParameterList"
        ] = None,
        blueprint_category: Optional[
            "capo_datazone.types.blueprint_category.BlueprintCategory"
        ] = None,
    ) -> "capo_datazone.types.update_environment_blueprint_output.UpdateEnvironmentBlueprintOutput":
        """<p>Updates an environment blueprint in Amazon DataZone.</p>

        Args:
            domain_identifier: <p>The identifier of the Amazon DataZone domain in which an environment blueprint is to be updated.</p>
            identifier: <p>The identifier of the environment blueprint to be updated.</p>
            description: <p>The description to be updated as part of the <code>UpdateEnvironmentBlueprint</code> action.</p>
            provisioning_properties: <p>The provisioning properties to be updated as part of the <code>UpdateEnvironmentBlueprint</code> action.</p>
            user_parameters: <p>The user parameters to be updated as part of the <code>UpdateEnvironmentBlueprint</code> action.</p>
            blueprint_category: <p>The category to update. The only valid value is <code>TOOLING</code>.</p>

        Raises:
            capo_datazone.errors.access_denied_exception.AccessDeniedException: <p>You do not have sufficient access to perform this action.</p>
            capo_datazone.errors.throttling_exception.ThrottlingException: <p>The request was denied due to request throttling.</p>
            capo_datazone.errors.unauthorized_exception.UnauthorizedException: <p>You do not have permission to perform this action.</p>
            capo_datazone.errors.conflict_exception.ConflictException: <p>There is a conflict while performing this action.</p>
            capo_datazone.errors.internal_server_exception.InternalServerException: <p>The request has failed because of an unknown error, exception or failure.</p>
            capo_datazone.errors.resource_not_found_exception.ResourceNotFoundException: <p>The specified resource cannot be found.</p>
            capo_datazone.errors.service_quota_exceeded_exception.ServiceQuotaExceededException: <p>The request has exceeded the specified service quota.</p>
            capo_datazone.errors.validation_exception.ValidationException: <p>The input fails to satisfy the constraints specified by the Amazon Web Services service.</p>
            capo_datazone.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        async def _handler(
            req: "AsyncOperationRequest[capo_datazone.types.update_environment_blueprint_input.UpdateEnvironmentBlueprintInput]",
        ) -> AsyncOperationResponse[
            "capo_datazone.types.update_environment_blueprint_output.UpdateEnvironmentBlueprintOutput"
        ]:
            import capo_datazone._operations.data_zone.update_environment_blueprint

            (
                output,
                http_response,
            ) = await capo_datazone._operations.data_zone.update_environment_blueprint.async_update_environment_blueprint(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_datazone.types.update_environment_blueprint_input.UpdateEnvironmentBlueprintInput = {
            "domain_identifier": domain_identifier,
            "identifier": identifier,
        }
        if description is not None:
            input_["description"] = description
        if provisioning_properties is not None:
            input_["provisioning_properties"] = provisioning_properties
        if user_parameters is not None:
            input_["user_parameters"] = user_parameters
        if blueprint_category is not None:
            input_["blueprint_category"] = blueprint_category

        response = await aexecute_pipeline(
            AsyncOperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        await response.response.aclose()
        return response.output

    async def update_environment_profile(
        self,
        domain_identifier: "capo_datazone.types.domain_id.DomainId",
        identifier: "capo_datazone.types.environment_profile_id.EnvironmentProfileId",
        *,
        config_overrides: Optional[AsyncDataZoneClientConfig] = None,
        name: Optional[
            "capo_datazone.types.environment_profile_name.EnvironmentProfileName"
        ] = None,
        description: Optional[str] = None,
        user_parameters: Optional[
            "capo_datazone.types.environment_parameters_list.EnvironmentParametersList"
        ] = None,
        aws_account_id: Optional[
            "capo_datazone.types.aws_account_id.AwsAccountId"
        ] = None,
        aws_account_region: Optional["capo_datazone.types.aws_region.AwsRegion"] = None,
    ) -> "capo_datazone.types.update_environment_profile_output.UpdateEnvironmentProfileOutput":
        """<p>Updates the specified environment profile in Amazon DataZone.</p>

        Args:
            domain_identifier: <p>The identifier of the Amazon DataZone domain in which an environment profile is to be updated.</p>
            identifier: <p>The identifier of the environment profile that is to be updated.</p>
            name: <p>The name to be updated as part of the <code>UpdateEnvironmentProfile</code> action.</p>
            description: <p>The description to be updated as part of the <code>UpdateEnvironmentProfile</code> action.</p>
            user_parameters: <p>The user parameters to be updated as part of the <code>UpdateEnvironmentProfile</code> action.</p>
            aws_account_id: <p>The Amazon Web Services account in which a specified environment profile is to be udpated.</p>
            aws_account_region: <p>The Amazon Web Services Region in which a specified environment profile is to be updated.</p>

        Raises:
            capo_datazone.errors.access_denied_exception.AccessDeniedException: <p>You do not have sufficient access to perform this action.</p>
            capo_datazone.errors.throttling_exception.ThrottlingException: <p>The request was denied due to request throttling.</p>
            capo_datazone.errors.unauthorized_exception.UnauthorizedException: <p>You do not have permission to perform this action.</p>
            capo_datazone.errors.conflict_exception.ConflictException: <p>There is a conflict while performing this action.</p>
            capo_datazone.errors.internal_server_exception.InternalServerException: <p>The request has failed because of an unknown error, exception or failure.</p>
            capo_datazone.errors.resource_not_found_exception.ResourceNotFoundException: <p>The specified resource cannot be found.</p>
            capo_datazone.errors.service_quota_exceeded_exception.ServiceQuotaExceededException: <p>The request has exceeded the specified service quota.</p>
            capo_datazone.errors.validation_exception.ValidationException: <p>The input fails to satisfy the constraints specified by the Amazon Web Services service.</p>
            capo_datazone.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        async def _handler(
            req: "AsyncOperationRequest[capo_datazone.types.update_environment_profile_input.UpdateEnvironmentProfileInput]",
        ) -> AsyncOperationResponse[
            "capo_datazone.types.update_environment_profile_output.UpdateEnvironmentProfileOutput"
        ]:
            import capo_datazone._operations.data_zone.update_environment_profile

            (
                output,
                http_response,
            ) = await capo_datazone._operations.data_zone.update_environment_profile.async_update_environment_profile(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_datazone.types.update_environment_profile_input.UpdateEnvironmentProfileInput = {
            "domain_identifier": domain_identifier,
            "identifier": identifier,
        }
        if name is not None:
            input_["name"] = name
        if description is not None:
            input_["description"] = description
        if user_parameters is not None:
            input_["user_parameters"] = user_parameters
        if aws_account_id is not None:
            input_["aws_account_id"] = aws_account_id
        if aws_account_region is not None:
            input_["aws_account_region"] = aws_account_region

        response = await aexecute_pipeline(
            AsyncOperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        await response.response.aclose()
        return response.output

    async def update_group_profile(
        self,
        domain_identifier: "capo_datazone.types.domain_id.DomainId",
        group_identifier: "capo_datazone.types.group_identifier.GroupIdentifier",
        status: "capo_datazone.types.group_profile_status.GroupProfileStatus",
        *,
        config_overrides: Optional[AsyncDataZoneClientConfig] = None,
    ) -> "capo_datazone.types.update_group_profile_output.UpdateGroupProfileOutput":
        """<p>Updates the specified group profile in Amazon DataZone.</p>

        Args:
            domain_identifier: <p>The identifier of the Amazon DataZone domain in which a group profile is updated.</p>
            group_identifier: <p>The identifier of the group profile that is updated.</p>
            status: <p>The status of the group profile that is updated.</p>

        Raises:
            capo_datazone.errors.access_denied_exception.AccessDeniedException: <p>You do not have sufficient access to perform this action.</p>
            capo_datazone.errors.throttling_exception.ThrottlingException: <p>The request was denied due to request throttling.</p>
            capo_datazone.errors.unauthorized_exception.UnauthorizedException: <p>You do not have permission to perform this action.</p>
            capo_datazone.errors.internal_server_exception.InternalServerException: <p>The request has failed because of an unknown error, exception or failure.</p>
            capo_datazone.errors.resource_not_found_exception.ResourceNotFoundException: <p>The specified resource cannot be found.</p>
            capo_datazone.errors.validation_exception.ValidationException: <p>The input fails to satisfy the constraints specified by the Amazon Web Services service.</p>
            capo_datazone.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        async def _handler(
            req: "AsyncOperationRequest[capo_datazone.types.update_group_profile_input.UpdateGroupProfileInput]",
        ) -> AsyncOperationResponse[
            "capo_datazone.types.update_group_profile_output.UpdateGroupProfileOutput"
        ]:
            import capo_datazone._operations.data_zone.update_group_profile

            (
                output,
                http_response,
            ) = await capo_datazone._operations.data_zone.update_group_profile.async_update_group_profile(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_datazone.types.update_group_profile_input.UpdateGroupProfileInput = {
            "domain_identifier": domain_identifier,
            "group_identifier": group_identifier,
            "status": status,
        }

        response = await aexecute_pipeline(
            AsyncOperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        await response.response.aclose()
        return response.output

    async def update_project(
        self,
        domain_identifier: "capo_datazone.types.domain_id.DomainId",
        identifier: "capo_datazone.types.project_id.ProjectId",
        *,
        config_overrides: Optional[AsyncDataZoneClientConfig] = None,
        name: Optional["capo_datazone.types.project_name.ProjectName"] = None,
        description: Optional["capo_datazone.types.description.Description"] = None,
        resource_tags: Optional["capo_datazone.types.tags.Tags"] = None,
        glossary_terms: Optional[
            "capo_datazone.types.glossary_terms.GlossaryTerms"
        ] = None,
        domain_unit_id: Optional[
            "capo_datazone.types.domain_unit_id.DomainUnitId"
        ] = None,
        environment_deployment_details: Optional[
            "capo_datazone.types.environment_deployment_details.EnvironmentDeploymentDetails"
        ] = None,
        user_parameters: Optional[
            "capo_datazone.types.environment_configuration_user_parameters_list.EnvironmentConfigurationUserParametersList"
        ] = None,
        project_profile_version: Optional[str] = None,
    ) -> "capo_datazone.types.update_project_output.UpdateProjectOutput":
        """<p>Updates the specified project in Amazon DataZone.</p>

        Args:
            domain_identifier: <p>The ID of the Amazon DataZone domain where a project is being updated.</p>
            identifier: <p>The identifier of the project that is to be updated.</p>
            name: <p>The name to be updated as part of the <code>UpdateProject</code> action.</p>
            description: <p>The description to be updated as part of the <code>UpdateProject</code> action.</p>
            resource_tags: <p>The resource tags of the project.</p>
            glossary_terms: <p>The glossary terms to be updated as part of the <code>UpdateProject</code> action.</p>
            domain_unit_id: <p>The ID of the domain unit.</p>
            environment_deployment_details: <p>The environment deployment details of the project.</p>
            user_parameters: <p>The user parameters of the project.</p>
            project_profile_version: <p>The project profile version to which the project should be updated. You can only specify the following string for this parameter: <code>latest</code>.</p>

        Raises:
            capo_datazone.errors.access_denied_exception.AccessDeniedException: <p>You do not have sufficient access to perform this action.</p>
            capo_datazone.errors.throttling_exception.ThrottlingException: <p>The request was denied due to request throttling.</p>
            capo_datazone.errors.unauthorized_exception.UnauthorizedException: <p>You do not have permission to perform this action.</p>
            capo_datazone.errors.conflict_exception.ConflictException: <p>There is a conflict while performing this action.</p>
            capo_datazone.errors.internal_server_exception.InternalServerException: <p>The request has failed because of an unknown error, exception or failure.</p>
            capo_datazone.errors.resource_not_found_exception.ResourceNotFoundException: <p>The specified resource cannot be found.</p>
            capo_datazone.errors.service_quota_exceeded_exception.ServiceQuotaExceededException: <p>The request has exceeded the specified service quota.</p>
            capo_datazone.errors.validation_exception.ValidationException: <p>The input fails to satisfy the constraints specified by the Amazon Web Services service.</p>
            capo_datazone.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        async def _handler(
            req: "AsyncOperationRequest[capo_datazone.types.update_project_input.UpdateProjectInput]",
        ) -> AsyncOperationResponse[
            "capo_datazone.types.update_project_output.UpdateProjectOutput"
        ]:
            import capo_datazone._operations.data_zone.update_project

            (
                output,
                http_response,
            ) = await capo_datazone._operations.data_zone.update_project.async_update_project(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_datazone.types.update_project_input.UpdateProjectInput = {
            "domain_identifier": domain_identifier,
            "identifier": identifier,
        }
        if name is not None:
            input_["name"] = name
        if description is not None:
            input_["description"] = description
        if resource_tags is not None:
            input_["resource_tags"] = resource_tags
        if glossary_terms is not None:
            input_["glossary_terms"] = glossary_terms
        if domain_unit_id is not None:
            input_["domain_unit_id"] = domain_unit_id
        if environment_deployment_details is not None:
            input_["environment_deployment_details"] = environment_deployment_details
        if user_parameters is not None:
            input_["user_parameters"] = user_parameters
        if project_profile_version is not None:
            input_["project_profile_version"] = project_profile_version

        response = await aexecute_pipeline(
            AsyncOperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        await response.response.aclose()
        return response.output

    async def update_project_profile(
        self,
        domain_identifier: "capo_datazone.types.domain_id.DomainId",
        identifier: "capo_datazone.types.project_profile_id.ProjectProfileId",
        *,
        config_overrides: Optional[AsyncDataZoneClientConfig] = None,
        name: Optional[
            "capo_datazone.types.project_profile_name.ProjectProfileName"
        ] = None,
        description: Optional["capo_datazone.types.description.Description"] = None,
        status: Optional["capo_datazone.types.status.Status"] = None,
        project_resource_tags: Optional[
            "capo_datazone.types.project_resource_tag_parameters.ProjectResourceTagParameters"
        ] = None,
        allow_custom_project_resource_tags: Optional[bool] = None,
        project_resource_tags_description: Optional[
            "capo_datazone.types.description.Description"
        ] = None,
        environment_configurations: Optional[
            "capo_datazone.types.environment_configurations_list.EnvironmentConfigurationsList"
        ] = None,
        domain_unit_identifier: Optional[
            "capo_datazone.types.domain_unit_id.DomainUnitId"
        ] = None,
    ) -> "capo_datazone.types.update_project_profile_output.UpdateProjectProfileOutput":
        """<p>Updates a project profile.</p>

        Args:
            domain_identifier: <p>The ID of the domain where a project profile is to be updated.</p>
            identifier: <p>The ID of a project profile that is to be updated.</p>
            name: <p>The name of a project profile.</p>
            description: <p>The description of a project profile.</p>
            status: <p>The status of a project profile.</p>
            project_resource_tags: <p>The resource tags of the project profile.</p>
            allow_custom_project_resource_tags: <p>Specifies whether custom project resource tags are supported.</p>
            project_resource_tags_description: <p>Field viewable through the UI that provides a project user with the allowed resource tag specifications.</p>
            environment_configurations: <p>The environment configurations of a project profile.</p>
            domain_unit_identifier: <p>The ID of the domain unit where a project profile is to be updated.</p>

        Raises:
            capo_datazone.errors.access_denied_exception.AccessDeniedException: <p>You do not have sufficient access to perform this action.</p>
            capo_datazone.errors.throttling_exception.ThrottlingException: <p>The request was denied due to request throttling.</p>
            capo_datazone.errors.unauthorized_exception.UnauthorizedException: <p>You do not have permission to perform this action.</p>
            capo_datazone.errors.conflict_exception.ConflictException: <p>There is a conflict while performing this action.</p>
            capo_datazone.errors.internal_server_exception.InternalServerException: <p>The request has failed because of an unknown error, exception or failure.</p>
            capo_datazone.errors.resource_not_found_exception.ResourceNotFoundException: <p>The specified resource cannot be found.</p>
            capo_datazone.errors.service_quota_exceeded_exception.ServiceQuotaExceededException: <p>The request has exceeded the specified service quota.</p>
            capo_datazone.errors.validation_exception.ValidationException: <p>The input fails to satisfy the constraints specified by the Amazon Web Services service.</p>
            capo_datazone.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        async def _handler(
            req: "AsyncOperationRequest[capo_datazone.types.update_project_profile_input.UpdateProjectProfileInput]",
        ) -> AsyncOperationResponse[
            "capo_datazone.types.update_project_profile_output.UpdateProjectProfileOutput"
        ]:
            import capo_datazone._operations.data_zone.update_project_profile

            (
                output,
                http_response,
            ) = await capo_datazone._operations.data_zone.update_project_profile.async_update_project_profile(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_datazone.types.update_project_profile_input.UpdateProjectProfileInput = {
            "domain_identifier": domain_identifier,
            "identifier": identifier,
        }
        if name is not None:
            input_["name"] = name
        if description is not None:
            input_["description"] = description
        if status is not None:
            input_["status"] = status
        if project_resource_tags is not None:
            input_["project_resource_tags"] = project_resource_tags
        if allow_custom_project_resource_tags is not None:
            input_["allow_custom_project_resource_tags"] = (
                allow_custom_project_resource_tags
            )
        if project_resource_tags_description is not None:
            input_["project_resource_tags_description"] = (
                project_resource_tags_description
            )
        if environment_configurations is not None:
            input_["environment_configurations"] = environment_configurations
        if domain_unit_identifier is not None:
            input_["domain_unit_identifier"] = domain_unit_identifier

        response = await aexecute_pipeline(
            AsyncOperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        await response.response.aclose()
        return response.output

    async def update_root_domain_unit_owner(
        self,
        domain_identifier: "capo_datazone.types.domain_id.DomainId",
        current_owner: "capo_datazone.types.user_identifier.UserIdentifier",
        new_owner: str,
        *,
        config_overrides: Optional[AsyncDataZoneClientConfig] = None,
        client_token: Optional["capo_datazone.types.client_token.ClientToken"] = None,
    ) -> "capo_datazone.types.update_root_domain_unit_owner_output.UpdateRootDomainUnitOwnerOutput":
        """<p>Updates the owner of the root domain unit.</p>

        Args:
            domain_identifier: <p>The ID of the domain where the root domain unit owner is to be updated.</p>
            current_owner: <p>The current owner of the root domain unit.</p>
            new_owner: <p>The new owner of the root domain unit.</p>
            client_token: <p>A unique, case-sensitive identifier to ensure idempotency of the request. This field is automatically populated if not provided.</p>

        Raises:
            capo_datazone.errors.access_denied_exception.AccessDeniedException: <p>You do not have sufficient access to perform this action.</p>
            capo_datazone.errors.throttling_exception.ThrottlingException: <p>The request was denied due to request throttling.</p>
            capo_datazone.errors.unauthorized_exception.UnauthorizedException: <p>You do not have permission to perform this action.</p>
            capo_datazone.errors.conflict_exception.ConflictException: <p>There is a conflict while performing this action.</p>
            capo_datazone.errors.internal_server_exception.InternalServerException: <p>The request has failed because of an unknown error, exception or failure.</p>
            capo_datazone.errors.resource_not_found_exception.ResourceNotFoundException: <p>The specified resource cannot be found.</p>
            capo_datazone.errors.validation_exception.ValidationException: <p>The input fails to satisfy the constraints specified by the Amazon Web Services service.</p>
            capo_datazone.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        async def _handler(
            req: "AsyncOperationRequest[capo_datazone.types.update_root_domain_unit_owner_input.UpdateRootDomainUnitOwnerInput]",
        ) -> AsyncOperationResponse[
            "capo_datazone.types.update_root_domain_unit_owner_output.UpdateRootDomainUnitOwnerOutput"
        ]:
            import capo_datazone._operations.data_zone.update_root_domain_unit_owner

            (
                output,
                http_response,
            ) = await capo_datazone._operations.data_zone.update_root_domain_unit_owner.async_update_root_domain_unit_owner(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_datazone.types.update_root_domain_unit_owner_input.UpdateRootDomainUnitOwnerInput = {
            "domain_identifier": domain_identifier,
            "current_owner": current_owner,
            "new_owner": new_owner,
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

    async def update_subscription_grant_status(
        self,
        domain_identifier: "capo_datazone.types.domain_id.DomainId",
        identifier: "capo_datazone.types.subscription_grant_id.SubscriptionGrantId",
        asset_identifier: "capo_datazone.types.asset_id.AssetId",
        status: "capo_datazone.types.subscription_grant_status.SubscriptionGrantStatus",
        *,
        config_overrides: Optional[AsyncDataZoneClientConfig] = None,
        failure_cause: Optional[
            "capo_datazone.types.failure_cause.FailureCause"
        ] = None,
        target_name: Optional[str] = None,
    ) -> "capo_datazone.types.update_subscription_grant_status_output.UpdateSubscriptionGrantStatusOutput":
        """<p>Updates the status of the specified subscription grant status in Amazon DataZone.</p>

        Args:
            domain_identifier: <p>The identifier of the Amazon DataZone domain in which a subscription grant status is to be updated.</p>
            identifier: <p>The identifier of the subscription grant the status of which is to be updated.</p>
            asset_identifier: <p>The identifier of the asset the subscription grant status of which is to be updated.</p>
            status: <p>The status to be updated as part of the <code>UpdateSubscriptionGrantStatus</code> action.</p>
            failure_cause: <p>Specifies the error message that is returned if the operation cannot be successfully completed.</p>
            target_name: <p>The target name to be updated as part of the <code>UpdateSubscriptionGrantStatus</code> action.</p>

        Raises:
            capo_datazone.errors.access_denied_exception.AccessDeniedException: <p>You do not have sufficient access to perform this action.</p>
            capo_datazone.errors.throttling_exception.ThrottlingException: <p>The request was denied due to request throttling.</p>
            capo_datazone.errors.unauthorized_exception.UnauthorizedException: <p>You do not have permission to perform this action.</p>
            capo_datazone.errors.conflict_exception.ConflictException: <p>There is a conflict while performing this action.</p>
            capo_datazone.errors.internal_server_exception.InternalServerException: <p>The request has failed because of an unknown error, exception or failure.</p>
            capo_datazone.errors.resource_not_found_exception.ResourceNotFoundException: <p>The specified resource cannot be found.</p>
            capo_datazone.errors.validation_exception.ValidationException: <p>The input fails to satisfy the constraints specified by the Amazon Web Services service.</p>
            capo_datazone.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        async def _handler(
            req: "AsyncOperationRequest[capo_datazone.types.update_subscription_grant_status_input.UpdateSubscriptionGrantStatusInput]",
        ) -> AsyncOperationResponse[
            "capo_datazone.types.update_subscription_grant_status_output.UpdateSubscriptionGrantStatusOutput"
        ]:
            import capo_datazone._operations.data_zone.update_subscription_grant_status

            (
                output,
                http_response,
            ) = await capo_datazone._operations.data_zone.update_subscription_grant_status.async_update_subscription_grant_status(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_datazone.types.update_subscription_grant_status_input.UpdateSubscriptionGrantStatusInput = {
            "domain_identifier": domain_identifier,
            "identifier": identifier,
            "asset_identifier": asset_identifier,
            "status": status,
        }
        if failure_cause is not None:
            input_["failure_cause"] = failure_cause
        if target_name is not None:
            input_["target_name"] = target_name

        response = await aexecute_pipeline(
            AsyncOperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        await response.response.aclose()
        return response.output

    async def update_subscription_request(
        self,
        domain_identifier: "capo_datazone.types.domain_id.DomainId",
        identifier: "capo_datazone.types.subscription_request_id.SubscriptionRequestId",
        request_reason: "capo_datazone.types.request_reason.RequestReason",
        *,
        config_overrides: Optional[AsyncDataZoneClientConfig] = None,
    ) -> "capo_datazone.types.update_subscription_request_output.UpdateSubscriptionRequestOutput":
        """<p>Updates a specified subscription request in Amazon DataZone.</p>

        Args:
            domain_identifier: <p>The identifier of the Amazon DataZone domain in which a subscription request is to be updated.</p>
            identifier: <p>The identifier of the subscription request that is to be updated.</p>
            request_reason: <p>The reason for the <code>UpdateSubscriptionRequest</code> action.</p>

        Raises:
            capo_datazone.errors.access_denied_exception.AccessDeniedException: <p>You do not have sufficient access to perform this action.</p>
            capo_datazone.errors.throttling_exception.ThrottlingException: <p>The request was denied due to request throttling.</p>
            capo_datazone.errors.unauthorized_exception.UnauthorizedException: <p>You do not have permission to perform this action.</p>
            capo_datazone.errors.conflict_exception.ConflictException: <p>There is a conflict while performing this action.</p>
            capo_datazone.errors.internal_server_exception.InternalServerException: <p>The request has failed because of an unknown error, exception or failure.</p>
            capo_datazone.errors.resource_not_found_exception.ResourceNotFoundException: <p>The specified resource cannot be found.</p>
            capo_datazone.errors.validation_exception.ValidationException: <p>The input fails to satisfy the constraints specified by the Amazon Web Services service.</p>
            capo_datazone.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        async def _handler(
            req: "AsyncOperationRequest[capo_datazone.types.update_subscription_request_input.UpdateSubscriptionRequestInput]",
        ) -> AsyncOperationResponse[
            "capo_datazone.types.update_subscription_request_output.UpdateSubscriptionRequestOutput"
        ]:
            import capo_datazone._operations.data_zone.update_subscription_request

            (
                output,
                http_response,
            ) = await capo_datazone._operations.data_zone.update_subscription_request.async_update_subscription_request(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_datazone.types.update_subscription_request_input.UpdateSubscriptionRequestInput = {
            "domain_identifier": domain_identifier,
            "identifier": identifier,
            "request_reason": request_reason,
        }

        response = await aexecute_pipeline(
            AsyncOperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        await response.response.aclose()
        return response.output

    async def update_subscription_target(
        self,
        domain_identifier: "capo_datazone.types.domain_id.DomainId",
        environment_identifier: "capo_datazone.types.environment_id.EnvironmentId",
        identifier: "capo_datazone.types.subscription_target_id.SubscriptionTargetId",
        *,
        config_overrides: Optional[AsyncDataZoneClientConfig] = None,
        name: Optional[
            "capo_datazone.types.subscription_target_name.SubscriptionTargetName"
        ] = None,
        authorized_principals: Optional[
            "capo_datazone.types.authorized_principal_identifiers.AuthorizedPrincipalIdentifiers"
        ] = None,
        applicable_asset_types: Optional[
            "capo_datazone.types.applicable_asset_types.ApplicableAssetTypes"
        ] = None,
        subscription_target_config: Optional[
            "capo_datazone.types.subscription_target_forms.SubscriptionTargetForms"
        ] = None,
        manage_access_role: Optional[
            "capo_datazone.types.iam_role_arn.IamRoleArn"
        ] = None,
        provider: Optional[str] = None,
        subscription_grant_creation_mode: Optional[
            "capo_datazone.types.subscription_grant_creation_mode.SubscriptionGrantCreationMode"
        ] = None,
    ) -> "capo_datazone.types.update_subscription_target_output.UpdateSubscriptionTargetOutput":
        """<p>Updates the specified subscription target in Amazon DataZone.</p>

        Args:
            domain_identifier: <p>The identifier of the Amazon DataZone domain in which a subscription target is to be updated.</p>
            environment_identifier: <p>The identifier of the environment in which a subscription target is to be updated.</p>
            identifier: <p>Identifier of the subscription target that is to be updated.</p>
            name: <p>The name to be updated as part of the <code>UpdateSubscriptionTarget</code> action.</p>
            authorized_principals: <p>The authorized principals to be updated as part of the <code>UpdateSubscriptionTarget</code> action.</p>
            applicable_asset_types: <p>The applicable asset types to be updated as part of the <code>UpdateSubscriptionTarget</code> action.</p>
            subscription_target_config: <p>The configuration to be updated as part of the <code>UpdateSubscriptionTarget</code> action.</p>
            manage_access_role: <p>The manage access role to be updated as part of the <code>UpdateSubscriptionTarget</code> action.</p>
            provider: <p>The provider to be updated as part of the <code>UpdateSubscriptionTarget</code> action.</p>
            subscription_grant_creation_mode: <p> Determines the subscription grant creation mode for this target, defining if grants are auto-created upon subscription approval or managed manually. </p>

        Raises:
            capo_datazone.errors.access_denied_exception.AccessDeniedException: <p>You do not have sufficient access to perform this action.</p>
            capo_datazone.errors.throttling_exception.ThrottlingException: <p>The request was denied due to request throttling.</p>
            capo_datazone.errors.unauthorized_exception.UnauthorizedException: <p>You do not have permission to perform this action.</p>
            capo_datazone.errors.conflict_exception.ConflictException: <p>There is a conflict while performing this action.</p>
            capo_datazone.errors.internal_server_exception.InternalServerException: <p>The request has failed because of an unknown error, exception or failure.</p>
            capo_datazone.errors.resource_not_found_exception.ResourceNotFoundException: <p>The specified resource cannot be found.</p>
            capo_datazone.errors.validation_exception.ValidationException: <p>The input fails to satisfy the constraints specified by the Amazon Web Services service.</p>
            capo_datazone.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        async def _handler(
            req: "AsyncOperationRequest[capo_datazone.types.update_subscription_target_input.UpdateSubscriptionTargetInput]",
        ) -> AsyncOperationResponse[
            "capo_datazone.types.update_subscription_target_output.UpdateSubscriptionTargetOutput"
        ]:
            import capo_datazone._operations.data_zone.update_subscription_target

            (
                output,
                http_response,
            ) = await capo_datazone._operations.data_zone.update_subscription_target.async_update_subscription_target(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_datazone.types.update_subscription_target_input.UpdateSubscriptionTargetInput = {
            "domain_identifier": domain_identifier,
            "environment_identifier": environment_identifier,
            "identifier": identifier,
        }
        if name is not None:
            input_["name"] = name
        if authorized_principals is not None:
            input_["authorized_principals"] = authorized_principals
        if applicable_asset_types is not None:
            input_["applicable_asset_types"] = applicable_asset_types
        if subscription_target_config is not None:
            input_["subscription_target_config"] = subscription_target_config
        if manage_access_role is not None:
            input_["manage_access_role"] = manage_access_role
        if provider is not None:
            input_["provider"] = provider
        if subscription_grant_creation_mode is not None:
            input_["subscription_grant_creation_mode"] = (
                subscription_grant_creation_mode
            )

        response = await aexecute_pipeline(
            AsyncOperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        await response.response.aclose()
        return response.output

    async def update_user_profile(
        self,
        domain_identifier: "capo_datazone.types.domain_id.DomainId",
        user_identifier: "capo_datazone.types.user_identifier.UserIdentifier",
        status: "capo_datazone.types.user_profile_status.UserProfileStatus",
        *,
        config_overrides: Optional[AsyncDataZoneClientConfig] = None,
        type: Optional["capo_datazone.types.user_profile_type.UserProfileType"] = None,
        session_name: Optional[str] = None,
    ) -> "capo_datazone.types.update_user_profile_output.UpdateUserProfileOutput":
        """<p>Updates the specified user profile in Amazon DataZone.</p>

        Args:
            domain_identifier: <p>The identifier of the Amazon DataZone domain in which a user profile is updated.</p>
            user_identifier: <p>The identifier of the user whose user profile is to be updated.</p>
            type: <p>The type of the user profile that are to be updated.</p>
            status: <p>The status of the user profile that are to be updated.</p>
            session_name: <p>The session name for IAM role sessions.</p>

        Raises:
            capo_datazone.errors.access_denied_exception.AccessDeniedException: <p>You do not have sufficient access to perform this action.</p>
            capo_datazone.errors.throttling_exception.ThrottlingException: <p>The request was denied due to request throttling.</p>
            capo_datazone.errors.unauthorized_exception.UnauthorizedException: <p>You do not have permission to perform this action.</p>
            capo_datazone.errors.internal_server_exception.InternalServerException: <p>The request has failed because of an unknown error, exception or failure.</p>
            capo_datazone.errors.resource_not_found_exception.ResourceNotFoundException: <p>The specified resource cannot be found.</p>
            capo_datazone.errors.validation_exception.ValidationException: <p>The input fails to satisfy the constraints specified by the Amazon Web Services service.</p>
            capo_datazone.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        async def _handler(
            req: "AsyncOperationRequest[capo_datazone.types.update_user_profile_input.UpdateUserProfileInput]",
        ) -> AsyncOperationResponse[
            "capo_datazone.types.update_user_profile_output.UpdateUserProfileOutput"
        ]:
            import capo_datazone._operations.data_zone.update_user_profile

            (
                output,
                http_response,
            ) = await capo_datazone._operations.data_zone.update_user_profile.async_update_user_profile(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_datazone.types.update_user_profile_input.UpdateUserProfileInput = {
            "domain_identifier": domain_identifier,
            "user_identifier": user_identifier,
            "status": status,
        }
        if type is not None:
            input_["type"] = type
        if session_name is not None:
            input_["session_name"] = session_name

        response = await aexecute_pipeline(
            AsyncOperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        await response.response.aclose()
        return response.output

    async def create_asset(
        self,
        name: "capo_datazone.types.asset_name.AssetName",
        domain_identifier: "capo_datazone.types.domain_id.DomainId",
        type_identifier: "capo_datazone.types.asset_type_identifier.AssetTypeIdentifier",
        owning_project_identifier: "capo_datazone.types.project_id.ProjectId",
        *,
        config_overrides: Optional[AsyncDataZoneClientConfig] = None,
        external_identifier: Optional[
            "capo_datazone.types.external_identifier.ExternalIdentifier"
        ] = None,
        type_revision: Optional["capo_datazone.types.revision.Revision"] = None,
        description: Optional["capo_datazone.types.description.Description"] = None,
        glossary_terms: Optional[
            "capo_datazone.types.glossary_terms.GlossaryTerms"
        ] = None,
        forms_input: Optional[
            "capo_datazone.types.form_input_list.FormInputList"
        ] = None,
        prediction_configuration: Optional[
            "capo_datazone.types.prediction_configuration.PredictionConfiguration"
        ] = None,
        client_token: Optional["capo_datazone.types.client_token.ClientToken"] = None,
    ) -> "capo_datazone.types.create_asset_output.CreateAssetOutput":
        """<p>Creates an asset in Amazon DataZone catalog.</p> <p>Before creating assets, make sure that the following requirements are met:</p> <ul> <li> <p> <code>--domain-identifier</code> must refer to an existing domain.</p> </li> <li> <p> <code>--owning-project-identifier</code> must be a valid project within the domain.</p> </li> <li> <p>Asset type must be created beforehand using <code>create-asset-type</code>, or be a supported system-defined type. For more information, see <a href="https://docs.aws.amazon.com/cli/latest/reference/datazone/create-asset-type.html">create-asset-type</a>.</p> </li> <li> <p> <code>--type-revision</code> (if used) must match a valid revision of the asset type.</p> </li> <li> <p> <code>formsInput</code> is required when it is associated as required in the <code>asset-type</code>. For more information, see <a href="https://docs.aws.amazon.com/cli/latest/reference/datazone/create-form-type.html">create-form-type</a>.</p> </li> <li> <p>Form content must include all required fields as per the form schema (e.g., <code>bucketArn</code>).</p> </li> </ul> <p>You must invoke the following pre-requisite commands before invoking this API:</p> <ul> <li> <p> <a href="https://docs.aws.amazon.com/datazone/latest/APIReference/API_CreateFormType.html">CreateFormType</a> </p> </li> <li> <p> <a href="https://docs.aws.amazon.com/datazone/latest/APIReference/API_CreateAssetType.html">CreateAssetType</a> </p> </li> </ul>

        Args:
            name: <p>Asset name.</p>
            domain_identifier: <p>Amazon DataZone domain where the asset is created.</p>
            external_identifier: <p>The external identifier of the asset.</p> <p>If the value for the <code>externalIdentifier</code> parameter is specified, it must be a unique value.</p>
            type_identifier: <p>The unique identifier of this asset's type.</p>
            type_revision: <p>The revision of this asset's type.</p>
            description: <p>Asset description.</p>
            glossary_terms: <p>Glossary terms attached to the asset.</p>
            forms_input: <p>Metadata forms attached to the asset.</p>
            owning_project_identifier: <p>The unique identifier of the project that owns this asset.</p>
            prediction_configuration: <p>The configuration of the automatically generated business-friendly metadata for the asset.</p>
            client_token: <p>A unique, case-sensitive identifier that is provided to ensure the idempotency of the request.</p>

        Raises:
            capo_datazone.errors.access_denied_exception.AccessDeniedException: <p>You do not have sufficient access to perform this action.</p>
            capo_datazone.errors.throttling_exception.ThrottlingException: <p>The request was denied due to request throttling.</p>
            capo_datazone.errors.unauthorized_exception.UnauthorizedException: <p>You do not have permission to perform this action.</p>
            capo_datazone.errors.conflict_exception.ConflictException: <p>There is a conflict while performing this action.</p>
            capo_datazone.errors.internal_server_exception.InternalServerException: <p>The request has failed because of an unknown error, exception or failure.</p>
            capo_datazone.errors.resource_not_found_exception.ResourceNotFoundException: <p>The specified resource cannot be found.</p>
            capo_datazone.errors.service_quota_exceeded_exception.ServiceQuotaExceededException: <p>The request has exceeded the specified service quota.</p>
            capo_datazone.errors.validation_exception.ValidationException: <p>The input fails to satisfy the constraints specified by the Amazon Web Services service.</p>
            capo_datazone.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        async def _handler(
            req: "AsyncOperationRequest[capo_datazone.types.create_asset_input.CreateAssetInput]",
        ) -> AsyncOperationResponse[
            "capo_datazone.types.create_asset_output.CreateAssetOutput"
        ]:
            import capo_datazone._operations.data_zone.create_asset

            (
                output,
                http_response,
            ) = await capo_datazone._operations.data_zone.create_asset.async_create_asset(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_datazone.types.create_asset_input.CreateAssetInput = {
            "name": name,
            "domain_identifier": domain_identifier,
            "type_identifier": type_identifier,
            "owning_project_identifier": owning_project_identifier,
        }
        if external_identifier is not None:
            input_["external_identifier"] = external_identifier
        if type_revision is not None:
            input_["type_revision"] = type_revision
        if description is not None:
            input_["description"] = description
        if glossary_terms is not None:
            input_["glossary_terms"] = glossary_terms
        if forms_input is not None:
            input_["forms_input"] = forms_input
        if prediction_configuration is not None:
            input_["prediction_configuration"] = prediction_configuration
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

    async def get_asset(
        self,
        domain_identifier: "capo_datazone.types.domain_id.DomainId",
        identifier: "capo_datazone.types.asset_identifier.AssetIdentifier",
        *,
        config_overrides: Optional[AsyncDataZoneClientConfig] = None,
        revision: Optional["capo_datazone.types.revision.Revision"] = None,
    ) -> "capo_datazone.types.get_asset_output.GetAssetOutput":
        """<p>Gets an Amazon DataZone asset.</p> <p>An asset is the fundamental building block in Amazon DataZone, representing any data resource that needs to be cataloged and managed. It can take many forms, from Amazon S3 buckets and database tables to dashboards and machine learning models. Each asset contains comprehensive metadata about the resource, including its location, schema, ownership, and lineage information. Assets are essential for organizing and managing data resources across an organization, making them discoverable and usable while maintaining proper governance.</p> <p>Before using the Amazon DataZone GetAsset command, ensure the following prerequisites are met:</p> <ul> <li> <p>Domain identifier must exist and be valid</p> </li> <li> <p>Asset identifier must exist</p> </li> <li> <p>User must have the required permissions to perform the action</p> </li> </ul>

        Args:
            domain_identifier: <p>The ID of the Amazon DataZone domain to which the asset belongs.</p>
            identifier: <p>The ID of the Amazon DataZone asset.</p> <p>This parameter supports either the value of <code>assetId</code> or <code>externalIdentifier</code> as input. If you are passing the value of <code>externalIdentifier</code>, you must prefix this value with <code>externalIdentifer%2F</code>.</p>
            revision: <p>The revision of the Amazon DataZone asset.</p>

        Raises:
            capo_datazone.errors.access_denied_exception.AccessDeniedException: <p>You do not have sufficient access to perform this action.</p>
            capo_datazone.errors.throttling_exception.ThrottlingException: <p>The request was denied due to request throttling.</p>
            capo_datazone.errors.unauthorized_exception.UnauthorizedException: <p>You do not have permission to perform this action.</p>
            capo_datazone.errors.internal_server_exception.InternalServerException: <p>The request has failed because of an unknown error, exception or failure.</p>
            capo_datazone.errors.resource_not_found_exception.ResourceNotFoundException: <p>The specified resource cannot be found.</p>
            capo_datazone.errors.validation_exception.ValidationException: <p>The input fails to satisfy the constraints specified by the Amazon Web Services service.</p>
            capo_datazone.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        async def _handler(
            req: "AsyncOperationRequest[capo_datazone.types.get_asset_input.GetAssetInput]",
        ) -> AsyncOperationResponse[
            "capo_datazone.types.get_asset_output.GetAssetOutput"
        ]:
            import capo_datazone._operations.data_zone.get_asset

            (
                output,
                http_response,
            ) = await capo_datazone._operations.data_zone.get_asset.async_get_asset(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_datazone.types.get_asset_input.GetAssetInput = {
            "domain_identifier": domain_identifier,
            "identifier": identifier,
        }
        if revision is not None:
            input_["revision"] = revision

        response = await aexecute_pipeline(
            AsyncOperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        await response.response.aclose()
        return response.output

    async def delete_asset(
        self,
        domain_identifier: "capo_datazone.types.domain_id.DomainId",
        identifier: "capo_datazone.types.asset_identifier.AssetIdentifier",
        *,
        config_overrides: Optional[AsyncDataZoneClientConfig] = None,
    ) -> "capo_datazone.types.delete_asset_output.DeleteAssetOutput":
        """<p>Deletes an asset in Amazon DataZone.</p> <ul> <li> <p>--domain-identifier must refer to a valid and existing domain. </p> </li> <li> <p>--identifier must refer to an existing asset in the specified domain.</p> </li> <li> <p>Asset must not be referenced in any existing asset filters.</p> </li> <li> <p>Asset must not be linked to any draft or published data product.</p> </li> <li> <p>User must have delete permissions for the domain and project.</p> </li> </ul>

        Args:
            domain_identifier: <p>The ID of the Amazon DataZone domain in which the asset is deleted.</p>
            identifier: <p>The identifier of the asset that is deleted.</p>

        Raises:
            capo_datazone.errors.access_denied_exception.AccessDeniedException: <p>You do not have sufficient access to perform this action.</p>
            capo_datazone.errors.throttling_exception.ThrottlingException: <p>The request was denied due to request throttling.</p>
            capo_datazone.errors.unauthorized_exception.UnauthorizedException: <p>You do not have permission to perform this action.</p>
            capo_datazone.errors.conflict_exception.ConflictException: <p>There is a conflict while performing this action.</p>
            capo_datazone.errors.internal_server_exception.InternalServerException: <p>The request has failed because of an unknown error, exception or failure.</p>
            capo_datazone.errors.resource_not_found_exception.ResourceNotFoundException: <p>The specified resource cannot be found.</p>
            capo_datazone.errors.validation_exception.ValidationException: <p>The input fails to satisfy the constraints specified by the Amazon Web Services service.</p>
            capo_datazone.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        async def _handler(
            req: "AsyncOperationRequest[capo_datazone.types.delete_asset_input.DeleteAssetInput]",
        ) -> AsyncOperationResponse[
            "capo_datazone.types.delete_asset_output.DeleteAssetOutput"
        ]:
            import capo_datazone._operations.data_zone.delete_asset

            (
                output,
                http_response,
            ) = await capo_datazone._operations.data_zone.delete_asset.async_delete_asset(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_datazone.types.delete_asset_input.DeleteAssetInput = {
            "domain_identifier": domain_identifier,
            "identifier": identifier,
        }

        response = await aexecute_pipeline(
            AsyncOperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        await response.response.aclose()
        return response.output

    async def create_asset_revision(
        self,
        name: "capo_datazone.types.asset_name.AssetName",
        domain_identifier: "capo_datazone.types.domain_id.DomainId",
        identifier: "capo_datazone.types.asset_identifier.AssetIdentifier",
        *,
        config_overrides: Optional[AsyncDataZoneClientConfig] = None,
        type_revision: Optional["capo_datazone.types.revision.Revision"] = None,
        description: Optional["capo_datazone.types.description.Description"] = None,
        glossary_terms: Optional[
            "capo_datazone.types.glossary_terms.GlossaryTerms"
        ] = None,
        forms_input: Optional[
            "capo_datazone.types.form_input_list.FormInputList"
        ] = None,
        prediction_configuration: Optional[
            "capo_datazone.types.prediction_configuration.PredictionConfiguration"
        ] = None,
        client_token: Optional["capo_datazone.types.client_token.ClientToken"] = None,
    ) -> "capo_datazone.types.create_asset_revision_output.CreateAssetRevisionOutput":
        """<p>Creates a revision of the asset.</p> <p>Asset revisions represent new versions of existing assets, capturing changes to either the underlying data or its metadata. They maintain a historical record of how assets evolve over time, who made changes, and when those changes occurred. This versioning capability is crucial for governance and compliance, allowing organizations to track changes, understand their impact, and roll back if necessary.</p> <p>Prerequisites:</p> <ul> <li> <p>Asset must already exist in the domain with identifier. </p> </li> <li> <p> <code>formsInput</code> is required when asset has the form type. <code>typeRevision</code> should be the latest version of form type. </p> </li> <li> <p>The form content must include all required fields (e.g., <code>bucketArn</code> for <code>S3ObjectCollectionForm</code>).</p> </li> <li> <p>The owning project of the original asset must still exist and be active.</p> </li> <li> <p>User must have write access to the project and domain.</p> </li> </ul>

        Args:
            name: <p>Te revised name of the asset.</p>
            domain_identifier: <p>The unique identifier of the domain where the asset is being revised.</p>
            identifier: <p>The identifier of the asset.</p>
            type_revision: <p>The revision type of the asset.</p>
            description: <p>The revised description of the asset.</p>
            glossary_terms: <p>The glossary terms to be attached to the asset as part of asset revision.</p>
            forms_input: <p>The metadata forms to be attached to the asset as part of asset revision.</p>
            prediction_configuration: <p>The configuration of the automatically generated business-friendly metadata for the asset.</p>
            client_token: <p>A unique, case-sensitive identifier that is provided to ensure the idempotency of the request.</p>

        Raises:
            capo_datazone.errors.access_denied_exception.AccessDeniedException: <p>You do not have sufficient access to perform this action.</p>
            capo_datazone.errors.throttling_exception.ThrottlingException: <p>The request was denied due to request throttling.</p>
            capo_datazone.errors.unauthorized_exception.UnauthorizedException: <p>You do not have permission to perform this action.</p>
            capo_datazone.errors.conflict_exception.ConflictException: <p>There is a conflict while performing this action.</p>
            capo_datazone.errors.internal_server_exception.InternalServerException: <p>The request has failed because of an unknown error, exception or failure.</p>
            capo_datazone.errors.resource_not_found_exception.ResourceNotFoundException: <p>The specified resource cannot be found.</p>
            capo_datazone.errors.validation_exception.ValidationException: <p>The input fails to satisfy the constraints specified by the Amazon Web Services service.</p>
            capo_datazone.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        async def _handler(
            req: "AsyncOperationRequest[capo_datazone.types.create_asset_revision_input.CreateAssetRevisionInput]",
        ) -> AsyncOperationResponse[
            "capo_datazone.types.create_asset_revision_output.CreateAssetRevisionOutput"
        ]:
            import capo_datazone._operations.data_zone.create_asset_revision

            (
                output,
                http_response,
            ) = await capo_datazone._operations.data_zone.create_asset_revision.async_create_asset_revision(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_datazone.types.create_asset_revision_input.CreateAssetRevisionInput = {
            "name": name,
            "domain_identifier": domain_identifier,
            "identifier": identifier,
        }
        if type_revision is not None:
            input_["type_revision"] = type_revision
        if description is not None:
            input_["description"] = description
        if glossary_terms is not None:
            input_["glossary_terms"] = glossary_terms
        if forms_input is not None:
            input_["forms_input"] = forms_input
        if prediction_configuration is not None:
            input_["prediction_configuration"] = prediction_configuration
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

    async def create_asset_type(
        self,
        domain_identifier: "capo_datazone.types.domain_id.DomainId",
        name: "capo_datazone.types.type_name.TypeName",
        forms_input: "capo_datazone.types.forms_input_map.FormsInputMap",
        owning_project_identifier: "capo_datazone.types.project_id.ProjectId",
        *,
        config_overrides: Optional[AsyncDataZoneClientConfig] = None,
        description: Optional["capo_datazone.types.description.Description"] = None,
    ) -> "capo_datazone.types.create_asset_type_output.CreateAssetTypeOutput":
        """<p>Creates a custom asset type.</p> <p>Prerequisites:</p> <ul> <li> <p>The <code>formsInput</code> field is required, however, can be passed as empty (e.g. <code>-forms-input {})</code>. </p> </li> <li> <p>You must have <code>CreateAssetType</code> permissions.</p> </li> <li> <p>The domain-identifier and owning-project-identifier must be valid and active.</p> </li> <li> <p>The name of the asset type must be unique within the domain — duplicate names will cause failure.</p> </li> <li> <p>JSON input must be valid — incorrect formatting causes Invalid JSON errors.</p> </li> </ul>

        Args:
            domain_identifier: <p>The unique identifier of the Amazon DataZone domain where the custom asset type is being created.</p>
            name: <p>The name of the custom asset type.</p>
            description: <p>The descripton of the custom asset type.</p>
            forms_input: <p>The metadata forms that are to be attached to the custom asset type.</p>
            owning_project_identifier: <p>The identifier of the Amazon DataZone project that is to own the custom asset type.</p>

        Raises:
            capo_datazone.errors.access_denied_exception.AccessDeniedException: <p>You do not have sufficient access to perform this action.</p>
            capo_datazone.errors.throttling_exception.ThrottlingException: <p>The request was denied due to request throttling.</p>
            capo_datazone.errors.unauthorized_exception.UnauthorizedException: <p>You do not have permission to perform this action.</p>
            capo_datazone.errors.conflict_exception.ConflictException: <p>There is a conflict while performing this action.</p>
            capo_datazone.errors.internal_server_exception.InternalServerException: <p>The request has failed because of an unknown error, exception or failure.</p>
            capo_datazone.errors.service_quota_exceeded_exception.ServiceQuotaExceededException: <p>The request has exceeded the specified service quota.</p>
            capo_datazone.errors.validation_exception.ValidationException: <p>The input fails to satisfy the constraints specified by the Amazon Web Services service.</p>
            capo_datazone.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        async def _handler(
            req: "AsyncOperationRequest[capo_datazone.types.create_asset_type_input.CreateAssetTypeInput]",
        ) -> AsyncOperationResponse[
            "capo_datazone.types.create_asset_type_output.CreateAssetTypeOutput"
        ]:
            import capo_datazone._operations.data_zone.create_asset_type

            (
                output,
                http_response,
            ) = await capo_datazone._operations.data_zone.create_asset_type.async_create_asset_type(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_datazone.types.create_asset_type_input.CreateAssetTypeInput = {
            "domain_identifier": domain_identifier,
            "name": name,
            "forms_input": forms_input,
            "owning_project_identifier": owning_project_identifier,
        }
        if description is not None:
            input_["description"] = description

        response = await aexecute_pipeline(
            AsyncOperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        await response.response.aclose()
        return response.output

    async def delete_asset_type(
        self,
        domain_identifier: "capo_datazone.types.domain_id.DomainId",
        identifier: "capo_datazone.types.asset_type_identifier.AssetTypeIdentifier",
        *,
        config_overrides: Optional[AsyncDataZoneClientConfig] = None,
    ) -> "capo_datazone.types.delete_asset_type_output.DeleteAssetTypeOutput":
        """<p>Deletes an asset type in Amazon DataZone.</p> <p>Prerequisites:</p> <ul> <li> <p>The asset type must exist in the domain. </p> </li> <li> <p>You must have DeleteAssetType permission.</p> </li> <li> <p>The asset type must not be in use (e.g., assigned to any asset). If used, deletion will fail.</p> </li> <li> <p>You should retrieve the asset type using get-asset-type to confirm its presence before deletion.</p> </li> </ul>

        Args:
            domain_identifier: <p>The ID of the Amazon DataZone domain in which the asset type is deleted.</p>
            identifier: <p>The identifier of the asset type that is deleted.</p>

        Raises:
            capo_datazone.errors.access_denied_exception.AccessDeniedException: <p>You do not have sufficient access to perform this action.</p>
            capo_datazone.errors.throttling_exception.ThrottlingException: <p>The request was denied due to request throttling.</p>
            capo_datazone.errors.unauthorized_exception.UnauthorizedException: <p>You do not have permission to perform this action.</p>
            capo_datazone.errors.conflict_exception.ConflictException: <p>There is a conflict while performing this action.</p>
            capo_datazone.errors.internal_server_exception.InternalServerException: <p>The request has failed because of an unknown error, exception or failure.</p>
            capo_datazone.errors.resource_not_found_exception.ResourceNotFoundException: <p>The specified resource cannot be found.</p>
            capo_datazone.errors.validation_exception.ValidationException: <p>The input fails to satisfy the constraints specified by the Amazon Web Services service.</p>
            capo_datazone.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        async def _handler(
            req: "AsyncOperationRequest[capo_datazone.types.delete_asset_type_input.DeleteAssetTypeInput]",
        ) -> AsyncOperationResponse[
            "capo_datazone.types.delete_asset_type_output.DeleteAssetTypeOutput"
        ]:
            import capo_datazone._operations.data_zone.delete_asset_type

            (
                output,
                http_response,
            ) = await capo_datazone._operations.data_zone.delete_asset_type.async_delete_asset_type(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_datazone.types.delete_asset_type_input.DeleteAssetTypeInput = {
            "domain_identifier": domain_identifier,
            "identifier": identifier,
        }

        response = await aexecute_pipeline(
            AsyncOperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        await response.response.aclose()
        return response.output

    async def get_asset_type(
        self,
        domain_identifier: "capo_datazone.types.domain_id.DomainId",
        identifier: "capo_datazone.types.asset_type_identifier.AssetTypeIdentifier",
        *,
        config_overrides: Optional[AsyncDataZoneClientConfig] = None,
        revision: Optional["capo_datazone.types.revision.Revision"] = None,
    ) -> "capo_datazone.types.get_asset_type_output.GetAssetTypeOutput":
        """<p>Gets an Amazon DataZone asset type.</p> <p>Asset types define the categories and characteristics of different kinds of data assets within Amazon DataZone.. They determine what metadata fields are required, what operations are possible, and how the asset integrates with other Amazon Web Services services. Asset types can range from built-in types like Amazon S3 buckets and Amazon Web Services Glue tables to custom types defined for specific organizational needs. Understanding asset types is crucial for properly organizing and managing different kinds of data resources.</p> <p>Prerequisites:</p> <ul> <li> <p>The asset type with identifier must exist in the domain. ResourceNotFoundException.</p> </li> <li> <p>You must have the GetAssetType permission.</p> </li> <li> <p>Ensure the domain-identifier value is correct and accessible.</p> </li> </ul>

        Args:
            domain_identifier: <p>The ID of the Amazon DataZone domain in which the asset type exists.</p>
            identifier: <p>The ID of the asset type.</p>
            revision: <p>The revision of the asset type.</p>

        Raises:
            capo_datazone.errors.access_denied_exception.AccessDeniedException: <p>You do not have sufficient access to perform this action.</p>
            capo_datazone.errors.throttling_exception.ThrottlingException: <p>The request was denied due to request throttling.</p>
            capo_datazone.errors.unauthorized_exception.UnauthorizedException: <p>You do not have permission to perform this action.</p>
            capo_datazone.errors.internal_server_exception.InternalServerException: <p>The request has failed because of an unknown error, exception or failure.</p>
            capo_datazone.errors.resource_not_found_exception.ResourceNotFoundException: <p>The specified resource cannot be found.</p>
            capo_datazone.errors.validation_exception.ValidationException: <p>The input fails to satisfy the constraints specified by the Amazon Web Services service.</p>
            capo_datazone.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        async def _handler(
            req: "AsyncOperationRequest[capo_datazone.types.get_asset_type_input.GetAssetTypeInput]",
        ) -> AsyncOperationResponse[
            "capo_datazone.types.get_asset_type_output.GetAssetTypeOutput"
        ]:
            import capo_datazone._operations.data_zone.get_asset_type

            (
                output,
                http_response,
            ) = await capo_datazone._operations.data_zone.get_asset_type.async_get_asset_type(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_datazone.types.get_asset_type_input.GetAssetTypeInput = {
            "domain_identifier": domain_identifier,
            "identifier": identifier,
        }
        if revision is not None:
            input_["revision"] = revision

        response = await aexecute_pipeline(
            AsyncOperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        await response.response.aclose()
        return response.output

    async def create_data_product(
        self,
        domain_identifier: "capo_datazone.types.domain_id.DomainId",
        name: "capo_datazone.types.data_product_name.DataProductName",
        owning_project_identifier: "capo_datazone.types.project_id.ProjectId",
        *,
        config_overrides: Optional[AsyncDataZoneClientConfig] = None,
        description: Optional[
            "capo_datazone.types.data_product_description.DataProductDescription"
        ] = None,
        glossary_terms: Optional[
            "capo_datazone.types.glossary_terms.GlossaryTerms"
        ] = None,
        forms_input: Optional[
            "capo_datazone.types.form_input_list.FormInputList"
        ] = None,
        items: Optional[
            "capo_datazone.types.data_product_items.DataProductItems"
        ] = None,
        client_token: Optional["capo_datazone.types.client_token.ClientToken"] = None,
    ) -> "capo_datazone.types.create_data_product_output.CreateDataProductOutput":
        """<p>Creates a data product.</p> <p>A data product is a comprehensive package that combines data assets with their associated metadata, documentation, and access controls. It's designed to serve specific business needs or use cases, making it easier for users to find and consume data appropriately. Data products include important information about data quality, freshness, and usage guidelines, effectively bridging the gap between data producers and consumers while ensuring proper governance.</p> <p>Prerequisites:</p> <ul> <li> <p>The domain must exist and be accessible. </p> </li> <li> <p>The owning project must be valid and active.</p> </li> <li> <p>The name must be unique within the domain (no existing data product with the same name).</p> </li> <li> <p>User must have create permissions for data products in the project.</p> </li> </ul>

        Args:
            domain_identifier: <p>The ID of the domain where the data product is created.</p>
            name: <p>The name of the data product.</p>
            owning_project_identifier: <p>The ID of the owning project of the data product.</p>
            description: <p>The description of the data product.</p>
            glossary_terms: <p>The glossary terms of the data product.</p>
            forms_input: <p>The metadata forms of the data product.</p>
            items: <p>The data assets of the data product.</p>
            client_token: <p>A unique, case-sensitive identifier that is provided to ensure the idempotency of the request.</p>

        Raises:
            capo_datazone.errors.access_denied_exception.AccessDeniedException: <p>You do not have sufficient access to perform this action.</p>
            capo_datazone.errors.throttling_exception.ThrottlingException: <p>The request was denied due to request throttling.</p>
            capo_datazone.errors.unauthorized_exception.UnauthorizedException: <p>You do not have permission to perform this action.</p>
            capo_datazone.errors.conflict_exception.ConflictException: <p>There is a conflict while performing this action.</p>
            capo_datazone.errors.internal_server_exception.InternalServerException: <p>The request has failed because of an unknown error, exception or failure.</p>
            capo_datazone.errors.resource_not_found_exception.ResourceNotFoundException: <p>The specified resource cannot be found.</p>
            capo_datazone.errors.service_quota_exceeded_exception.ServiceQuotaExceededException: <p>The request has exceeded the specified service quota.</p>
            capo_datazone.errors.validation_exception.ValidationException: <p>The input fails to satisfy the constraints specified by the Amazon Web Services service.</p>
            capo_datazone.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        async def _handler(
            req: "AsyncOperationRequest[capo_datazone.types.create_data_product_input.CreateDataProductInput]",
        ) -> AsyncOperationResponse[
            "capo_datazone.types.create_data_product_output.CreateDataProductOutput"
        ]:
            import capo_datazone._operations.data_zone.create_data_product

            (
                output,
                http_response,
            ) = await capo_datazone._operations.data_zone.create_data_product.async_create_data_product(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_datazone.types.create_data_product_input.CreateDataProductInput = {
            "domain_identifier": domain_identifier,
            "name": name,
            "owning_project_identifier": owning_project_identifier,
        }
        if description is not None:
            input_["description"] = description
        if glossary_terms is not None:
            input_["glossary_terms"] = glossary_terms
        if forms_input is not None:
            input_["forms_input"] = forms_input
        if items is not None:
            input_["items"] = items
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

    async def get_data_product(
        self,
        domain_identifier: "capo_datazone.types.domain_id.DomainId",
        identifier: "capo_datazone.types.data_product_id.DataProductId",
        *,
        config_overrides: Optional[AsyncDataZoneClientConfig] = None,
        revision: Optional["capo_datazone.types.revision.Revision"] = None,
    ) -> "capo_datazone.types.get_data_product_output.GetDataProductOutput":
        """<p>Gets the data product.</p> <p>Prerequisites:</p> <ul> <li> <p>The data product ID must exist. </p> </li> <li> <p>The domain must be valid and accessible.</p> </li> <li> <p>User must have read or discovery permissions for the data product.</p> </li> </ul>

        Args:
            domain_identifier: <p>The ID of the domain where the data product lives.</p>
            identifier: <p>The ID of the data product.</p>
            revision: <p>The revision of the data product.</p>

        Raises:
            capo_datazone.errors.access_denied_exception.AccessDeniedException: <p>You do not have sufficient access to perform this action.</p>
            capo_datazone.errors.throttling_exception.ThrottlingException: <p>The request was denied due to request throttling.</p>
            capo_datazone.errors.unauthorized_exception.UnauthorizedException: <p>You do not have permission to perform this action.</p>
            capo_datazone.errors.internal_server_exception.InternalServerException: <p>The request has failed because of an unknown error, exception or failure.</p>
            capo_datazone.errors.resource_not_found_exception.ResourceNotFoundException: <p>The specified resource cannot be found.</p>
            capo_datazone.errors.validation_exception.ValidationException: <p>The input fails to satisfy the constraints specified by the Amazon Web Services service.</p>
            capo_datazone.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        async def _handler(
            req: "AsyncOperationRequest[capo_datazone.types.get_data_product_input.GetDataProductInput]",
        ) -> AsyncOperationResponse[
            "capo_datazone.types.get_data_product_output.GetDataProductOutput"
        ]:
            import capo_datazone._operations.data_zone.get_data_product

            (
                output,
                http_response,
            ) = await capo_datazone._operations.data_zone.get_data_product.async_get_data_product(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_datazone.types.get_data_product_input.GetDataProductInput = {
            "domain_identifier": domain_identifier,
            "identifier": identifier,
        }
        if revision is not None:
            input_["revision"] = revision

        response = await aexecute_pipeline(
            AsyncOperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        await response.response.aclose()
        return response.output

    async def delete_data_product(
        self,
        domain_identifier: "capo_datazone.types.domain_id.DomainId",
        identifier: "capo_datazone.types.data_product_id.DataProductId",
        *,
        config_overrides: Optional[AsyncDataZoneClientConfig] = None,
    ) -> "capo_datazone.types.delete_data_product_output.DeleteDataProductOutput":
        """<p>Deletes a data product in Amazon DataZone.</p> <p>Prerequisites:</p> <ul> <li> <p>The data product must exist and not be deleted or archived. </p> </li> <li> <p>The user must have delete permissions for the data product.</p> </li> <li> <p>Domain and project must be active.</p> </li> </ul>

        Args:
            domain_identifier: <p>The ID of the Amazon DataZone domain in which the data product is deleted.</p>
            identifier: <p>The identifier of the data product that is deleted.</p>

        Raises:
            capo_datazone.errors.access_denied_exception.AccessDeniedException: <p>You do not have sufficient access to perform this action.</p>
            capo_datazone.errors.throttling_exception.ThrottlingException: <p>The request was denied due to request throttling.</p>
            capo_datazone.errors.unauthorized_exception.UnauthorizedException: <p>You do not have permission to perform this action.</p>
            capo_datazone.errors.conflict_exception.ConflictException: <p>There is a conflict while performing this action.</p>
            capo_datazone.errors.internal_server_exception.InternalServerException: <p>The request has failed because of an unknown error, exception or failure.</p>
            capo_datazone.errors.resource_not_found_exception.ResourceNotFoundException: <p>The specified resource cannot be found.</p>
            capo_datazone.errors.validation_exception.ValidationException: <p>The input fails to satisfy the constraints specified by the Amazon Web Services service.</p>
            capo_datazone.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        async def _handler(
            req: "AsyncOperationRequest[capo_datazone.types.delete_data_product_input.DeleteDataProductInput]",
        ) -> AsyncOperationResponse[
            "capo_datazone.types.delete_data_product_output.DeleteDataProductOutput"
        ]:
            import capo_datazone._operations.data_zone.delete_data_product

            (
                output,
                http_response,
            ) = await capo_datazone._operations.data_zone.delete_data_product.async_delete_data_product(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_datazone.types.delete_data_product_input.DeleteDataProductInput = {
            "domain_identifier": domain_identifier,
            "identifier": identifier,
        }

        response = await aexecute_pipeline(
            AsyncOperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        await response.response.aclose()
        return response.output

    async def create_data_product_revision(
        self,
        domain_identifier: "capo_datazone.types.domain_id.DomainId",
        identifier: "capo_datazone.types.data_product_id.DataProductId",
        name: "capo_datazone.types.data_product_name.DataProductName",
        *,
        config_overrides: Optional[AsyncDataZoneClientConfig] = None,
        description: Optional[
            "capo_datazone.types.data_product_description.DataProductDescription"
        ] = None,
        glossary_terms: Optional[
            "capo_datazone.types.glossary_terms.GlossaryTerms"
        ] = None,
        items: Optional[
            "capo_datazone.types.data_product_items.DataProductItems"
        ] = None,
        forms_input: Optional[
            "capo_datazone.types.form_input_list.FormInputList"
        ] = None,
        client_token: Optional["capo_datazone.types.client_token.ClientToken"] = None,
    ) -> "capo_datazone.types.create_data_product_revision_output.CreateDataProductRevisionOutput":
        """<p>Creates a data product revision.</p> <p>Prerequisites:</p> <ul> <li> <p>The original data product must exist in the given domain. </p> </li> <li> <p>User must have permissions on the data product.</p> </li> <li> <p>The domain must be valid and accessible.</p> </li> <li> <p>The new revision name must comply with naming constraints (if required).</p> </li> </ul>

        Args:
            domain_identifier: <p>The ID of the domain where the data product revision is created.</p>
            identifier: <p>The ID of the data product revision.</p>
            name: <p>The name of the data product revision.</p>
            description: <p>The description of the data product revision.</p>
            glossary_terms: <p>The glossary terms of the data product revision.</p>
            items: <p>The data assets of the data product revision.</p>
            forms_input: <p>The metadata forms of the data product revision.</p>
            client_token: <p>A unique, case-sensitive identifier that is provided to ensure the idempotency of the request.</p>

        Raises:
            capo_datazone.errors.access_denied_exception.AccessDeniedException: <p>You do not have sufficient access to perform this action.</p>
            capo_datazone.errors.throttling_exception.ThrottlingException: <p>The request was denied due to request throttling.</p>
            capo_datazone.errors.unauthorized_exception.UnauthorizedException: <p>You do not have permission to perform this action.</p>
            capo_datazone.errors.conflict_exception.ConflictException: <p>There is a conflict while performing this action.</p>
            capo_datazone.errors.internal_server_exception.InternalServerException: <p>The request has failed because of an unknown error, exception or failure.</p>
            capo_datazone.errors.resource_not_found_exception.ResourceNotFoundException: <p>The specified resource cannot be found.</p>
            capo_datazone.errors.validation_exception.ValidationException: <p>The input fails to satisfy the constraints specified by the Amazon Web Services service.</p>
            capo_datazone.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        async def _handler(
            req: "AsyncOperationRequest[capo_datazone.types.create_data_product_revision_input.CreateDataProductRevisionInput]",
        ) -> AsyncOperationResponse[
            "capo_datazone.types.create_data_product_revision_output.CreateDataProductRevisionOutput"
        ]:
            import capo_datazone._operations.data_zone.create_data_product_revision

            (
                output,
                http_response,
            ) = await capo_datazone._operations.data_zone.create_data_product_revision.async_create_data_product_revision(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_datazone.types.create_data_product_revision_input.CreateDataProductRevisionInput = {
            "domain_identifier": domain_identifier,
            "identifier": identifier,
            "name": name,
        }
        if description is not None:
            input_["description"] = description
        if glossary_terms is not None:
            input_["glossary_terms"] = glossary_terms
        if items is not None:
            input_["items"] = items
        if forms_input is not None:
            input_["forms_input"] = forms_input
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

    async def create_data_source(
        self,
        name: "capo_datazone.types.name.Name",
        domain_identifier: "capo_datazone.types.domain_id.DomainId",
        project_identifier: str,
        type: "capo_datazone.types.data_source_type.DataSourceType",
        *,
        config_overrides: Optional[AsyncDataZoneClientConfig] = None,
        description: Optional["capo_datazone.types.description.Description"] = None,
        environment_identifier: Optional[str] = None,
        connection_identifier: Optional[str] = None,
        configuration: Optional[
            "capo_datazone.types.data_source_configuration_input.DataSourceConfigurationInput"
        ] = None,
        recommendation: Optional[
            "capo_datazone.types.recommendation_configuration.RecommendationConfiguration"
        ] = None,
        enable_setting: Optional[
            "capo_datazone.types.enable_setting.EnableSetting"
        ] = None,
        schedule: Optional[
            "capo_datazone.types.schedule_configuration.ScheduleConfiguration"
        ] = None,
        publish_on_import: Optional[bool] = None,
        asset_forms_input: Optional[
            "capo_datazone.types.form_input_list.FormInputList"
        ] = None,
        client_token: Optional[str] = None,
    ) -> "capo_datazone.types.create_data_source_output.CreateDataSourceOutput":
        """<p>Creates an Amazon DataZone data source.</p>

        Args:
            name: <p>The name of the data source.</p>
            description: <p>The description of the data source.</p>
            domain_identifier: <p>The ID of the Amazon DataZone domain where the data source is created.</p>
            project_identifier: <p>The identifier of the Amazon DataZone project in which you want to add this data source.</p>
            environment_identifier: <p>The unique identifier of the Amazon DataZone environment to which the data source publishes assets. </p>
            connection_identifier: <p>The ID of the connection.</p>
            type: <p>The type of the data source. In Amazon DataZone, you can use data sources to import technical metadata of assets (data) from the source databases or data warehouses into Amazon DataZone. In the current release of Amazon DataZone, you can create and run data sources for Amazon Web Services Glue and Amazon Redshift.</p>
            configuration: <p>Specifies the configuration of the data source. It can be set to either <code>glueRunConfiguration</code> or <code>redshiftRunConfiguration</code>.</p>
            recommendation: <p>Specifies whether the business name generation is to be enabled for this data source.</p>
            enable_setting: <p>Specifies whether the data source is enabled.</p>
            schedule: <p>The schedule of the data source runs.</p>
            publish_on_import: <p>Specifies whether the assets that this data source creates in the inventory are to be also automatically published to the catalog.</p>
            asset_forms_input: <p>The metadata forms that are to be attached to the assets that this data source works with.</p>
            client_token: <p>A unique, case-sensitive identifier that is provided to ensure the idempotency of the request.</p>

        Raises:
            capo_datazone.errors.access_denied_exception.AccessDeniedException: <p>You do not have sufficient access to perform this action.</p>
            capo_datazone.errors.throttling_exception.ThrottlingException: <p>The request was denied due to request throttling.</p>
            capo_datazone.errors.unauthorized_exception.UnauthorizedException: <p>You do not have permission to perform this action.</p>
            capo_datazone.errors.conflict_exception.ConflictException: <p>There is a conflict while performing this action.</p>
            capo_datazone.errors.internal_server_exception.InternalServerException: <p>The request has failed because of an unknown error, exception or failure.</p>
            capo_datazone.errors.resource_not_found_exception.ResourceNotFoundException: <p>The specified resource cannot be found.</p>
            capo_datazone.errors.service_quota_exceeded_exception.ServiceQuotaExceededException: <p>The request has exceeded the specified service quota.</p>
            capo_datazone.errors.validation_exception.ValidationException: <p>The input fails to satisfy the constraints specified by the Amazon Web Services service.</p>
            capo_datazone.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        async def _handler(
            req: "AsyncOperationRequest[capo_datazone.types.create_data_source_input.CreateDataSourceInput]",
        ) -> AsyncOperationResponse[
            "capo_datazone.types.create_data_source_output.CreateDataSourceOutput"
        ]:
            import capo_datazone._operations.data_zone.create_data_source

            (
                output,
                http_response,
            ) = await capo_datazone._operations.data_zone.create_data_source.async_create_data_source(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_datazone.types.create_data_source_input.CreateDataSourceInput = {
            "name": name,
            "domain_identifier": domain_identifier,
            "project_identifier": project_identifier,
            "type": type,
        }
        if description is not None:
            input_["description"] = description
        if environment_identifier is not None:
            input_["environment_identifier"] = environment_identifier
        if connection_identifier is not None:
            input_["connection_identifier"] = connection_identifier
        if configuration is not None:
            input_["configuration"] = configuration
        if recommendation is not None:
            input_["recommendation"] = recommendation
        if enable_setting is not None:
            input_["enable_setting"] = enable_setting
        if schedule is not None:
            input_["schedule"] = schedule
        if publish_on_import is not None:
            input_["publish_on_import"] = publish_on_import
        if asset_forms_input is not None:
            input_["asset_forms_input"] = asset_forms_input
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

    async def get_data_source(
        self,
        domain_identifier: "capo_datazone.types.domain_id.DomainId",
        identifier: "capo_datazone.types.data_source_id.DataSourceId",
        *,
        config_overrides: Optional[AsyncDataZoneClientConfig] = None,
    ) -> "capo_datazone.types.get_data_source_output.GetDataSourceOutput":
        """<p>Gets an Amazon DataZone data source.</p>

        Args:
            domain_identifier: <p>The ID of the Amazon DataZone domain in which the data source exists.</p>
            identifier: <p>The ID of the Amazon DataZone data source.</p>

        Raises:
            capo_datazone.errors.access_denied_exception.AccessDeniedException: <p>You do not have sufficient access to perform this action.</p>
            capo_datazone.errors.throttling_exception.ThrottlingException: <p>The request was denied due to request throttling.</p>
            capo_datazone.errors.unauthorized_exception.UnauthorizedException: <p>You do not have permission to perform this action.</p>
            capo_datazone.errors.conflict_exception.ConflictException: <p>There is a conflict while performing this action.</p>
            capo_datazone.errors.internal_server_exception.InternalServerException: <p>The request has failed because of an unknown error, exception or failure.</p>
            capo_datazone.errors.resource_not_found_exception.ResourceNotFoundException: <p>The specified resource cannot be found.</p>
            capo_datazone.errors.service_quota_exceeded_exception.ServiceQuotaExceededException: <p>The request has exceeded the specified service quota.</p>
            capo_datazone.errors.validation_exception.ValidationException: <p>The input fails to satisfy the constraints specified by the Amazon Web Services service.</p>
            capo_datazone.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        async def _handler(
            req: "AsyncOperationRequest[capo_datazone.types.get_data_source_input.GetDataSourceInput]",
        ) -> AsyncOperationResponse[
            "capo_datazone.types.get_data_source_output.GetDataSourceOutput"
        ]:
            import capo_datazone._operations.data_zone.get_data_source

            (
                output,
                http_response,
            ) = await capo_datazone._operations.data_zone.get_data_source.async_get_data_source(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_datazone.types.get_data_source_input.GetDataSourceInput = {
            "domain_identifier": domain_identifier,
            "identifier": identifier,
        }

        response = await aexecute_pipeline(
            AsyncOperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        await response.response.aclose()
        return response.output

    async def update_data_source(
        self,
        domain_identifier: "capo_datazone.types.domain_id.DomainId",
        identifier: "capo_datazone.types.data_source_id.DataSourceId",
        *,
        config_overrides: Optional[AsyncDataZoneClientConfig] = None,
        name: Optional["capo_datazone.types.name.Name"] = None,
        description: Optional["capo_datazone.types.description.Description"] = None,
        enable_setting: Optional[
            "capo_datazone.types.enable_setting.EnableSetting"
        ] = None,
        publish_on_import: Optional[bool] = None,
        asset_forms_input: Optional[
            "capo_datazone.types.form_input_list.FormInputList"
        ] = None,
        schedule: Optional[
            "capo_datazone.types.schedule_configuration.ScheduleConfiguration"
        ] = None,
        configuration: Optional[
            "capo_datazone.types.data_source_configuration_input.DataSourceConfigurationInput"
        ] = None,
        recommendation: Optional[
            "capo_datazone.types.recommendation_configuration.RecommendationConfiguration"
        ] = None,
        retain_permissions_on_revoke_failure: Optional[bool] = None,
    ) -> "capo_datazone.types.update_data_source_output.UpdateDataSourceOutput":
        """<p>Updates the specified data source in Amazon DataZone.</p>

        Args:
            domain_identifier: <p>The identifier of the domain in which to update a data source.</p>
            identifier: <p>The identifier of the data source to be updated.</p>
            name: <p>The name to be updated as part of the <code>UpdateDataSource</code> action.</p>
            description: <p>The description to be updated as part of the <code>UpdateDataSource</code> action.</p>
            enable_setting: <p>The enable setting to be updated as part of the <code>UpdateDataSource</code> action.</p>
            publish_on_import: <p>The publish on import setting to be updated as part of the <code>UpdateDataSource</code> action.</p>
            asset_forms_input: <p>The asset forms to be updated as part of the <code>UpdateDataSource</code> action.</p>
            schedule: <p>The schedule to be updated as part of the <code>UpdateDataSource</code> action.</p>
            configuration: <p>The configuration to be updated as part of the <code>UpdateDataSource</code> action.</p>
            recommendation: <p>The recommendation to be updated as part of the <code>UpdateDataSource</code> action.</p>
            retain_permissions_on_revoke_failure: <p>Specifies that the granted permissions are retained in case of a self-subscribe functionality failure for a data source.</p>

        Raises:
            capo_datazone.errors.access_denied_exception.AccessDeniedException: <p>You do not have sufficient access to perform this action.</p>
            capo_datazone.errors.throttling_exception.ThrottlingException: <p>The request was denied due to request throttling.</p>
            capo_datazone.errors.unauthorized_exception.UnauthorizedException: <p>You do not have permission to perform this action.</p>
            capo_datazone.errors.conflict_exception.ConflictException: <p>There is a conflict while performing this action.</p>
            capo_datazone.errors.internal_server_exception.InternalServerException: <p>The request has failed because of an unknown error, exception or failure.</p>
            capo_datazone.errors.resource_not_found_exception.ResourceNotFoundException: <p>The specified resource cannot be found.</p>
            capo_datazone.errors.service_quota_exceeded_exception.ServiceQuotaExceededException: <p>The request has exceeded the specified service quota.</p>
            capo_datazone.errors.validation_exception.ValidationException: <p>The input fails to satisfy the constraints specified by the Amazon Web Services service.</p>
            capo_datazone.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        async def _handler(
            req: "AsyncOperationRequest[capo_datazone.types.update_data_source_input.UpdateDataSourceInput]",
        ) -> AsyncOperationResponse[
            "capo_datazone.types.update_data_source_output.UpdateDataSourceOutput"
        ]:
            import capo_datazone._operations.data_zone.update_data_source

            (
                output,
                http_response,
            ) = await capo_datazone._operations.data_zone.update_data_source.async_update_data_source(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_datazone.types.update_data_source_input.UpdateDataSourceInput = {
            "domain_identifier": domain_identifier,
            "identifier": identifier,
        }
        if name is not None:
            input_["name"] = name
        if description is not None:
            input_["description"] = description
        if enable_setting is not None:
            input_["enable_setting"] = enable_setting
        if publish_on_import is not None:
            input_["publish_on_import"] = publish_on_import
        if asset_forms_input is not None:
            input_["asset_forms_input"] = asset_forms_input
        if schedule is not None:
            input_["schedule"] = schedule
        if configuration is not None:
            input_["configuration"] = configuration
        if recommendation is not None:
            input_["recommendation"] = recommendation
        if retain_permissions_on_revoke_failure is not None:
            input_["retain_permissions_on_revoke_failure"] = (
                retain_permissions_on_revoke_failure
            )

        response = await aexecute_pipeline(
            AsyncOperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        await response.response.aclose()
        return response.output

    async def delete_data_source(
        self,
        domain_identifier: "capo_datazone.types.domain_id.DomainId",
        identifier: "capo_datazone.types.data_source_id.DataSourceId",
        *,
        config_overrides: Optional[AsyncDataZoneClientConfig] = None,
        client_token: Optional[str] = None,
        retain_permissions_on_revoke_failure: Optional[bool] = None,
    ) -> "capo_datazone.types.delete_data_source_output.DeleteDataSourceOutput":
        """<p>Deletes a data source in Amazon DataZone.</p>

        Args:
            domain_identifier: <p>The ID of the Amazon DataZone domain in which the data source is deleted.</p>
            identifier: <p>The identifier of the data source that is deleted.</p>
            client_token: <p>A unique, case-sensitive identifier that is provided to ensure the idempotency of the request.</p>
            retain_permissions_on_revoke_failure: <p>Specifies that the granted permissions are retained in case of a self-subscribe functionality failure for a data source.</p>

        Raises:
            capo_datazone.errors.access_denied_exception.AccessDeniedException: <p>You do not have sufficient access to perform this action.</p>
            capo_datazone.errors.throttling_exception.ThrottlingException: <p>The request was denied due to request throttling.</p>
            capo_datazone.errors.unauthorized_exception.UnauthorizedException: <p>You do not have permission to perform this action.</p>
            capo_datazone.errors.conflict_exception.ConflictException: <p>There is a conflict while performing this action.</p>
            capo_datazone.errors.internal_server_exception.InternalServerException: <p>The request has failed because of an unknown error, exception or failure.</p>
            capo_datazone.errors.resource_not_found_exception.ResourceNotFoundException: <p>The specified resource cannot be found.</p>
            capo_datazone.errors.service_quota_exceeded_exception.ServiceQuotaExceededException: <p>The request has exceeded the specified service quota.</p>
            capo_datazone.errors.validation_exception.ValidationException: <p>The input fails to satisfy the constraints specified by the Amazon Web Services service.</p>
            capo_datazone.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        async def _handler(
            req: "AsyncOperationRequest[capo_datazone.types.delete_data_source_input.DeleteDataSourceInput]",
        ) -> AsyncOperationResponse[
            "capo_datazone.types.delete_data_source_output.DeleteDataSourceOutput"
        ]:
            import capo_datazone._operations.data_zone.delete_data_source

            (
                output,
                http_response,
            ) = await capo_datazone._operations.data_zone.delete_data_source.async_delete_data_source(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_datazone.types.delete_data_source_input.DeleteDataSourceInput = {
            "domain_identifier": domain_identifier,
            "identifier": identifier,
        }
        if client_token is None:
            client_token = str(uuid.uuid4())
        input_["client_token"] = client_token
        if retain_permissions_on_revoke_failure is not None:
            input_["retain_permissions_on_revoke_failure"] = (
                retain_permissions_on_revoke_failure
            )

        response = await aexecute_pipeline(
            AsyncOperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        await response.response.aclose()
        return response.output

    async def list_data_sources(
        self,
        domain_identifier: "capo_datazone.types.domain_id.DomainId",
        project_identifier: str,
        *,
        config_overrides: Optional[AsyncDataZoneClientConfig] = None,
        environment_identifier: Optional[str] = None,
        connection_identifier: Optional[str] = None,
        type: Optional["capo_datazone.types.data_source_type.DataSourceType"] = None,
        status: Optional[
            "capo_datazone.types.data_source_status.DataSourceStatus"
        ] = None,
        name: Optional["capo_datazone.types.name.Name"] = None,
        next_token: Optional[
            "capo_datazone.types.pagination_token.PaginationToken"
        ] = None,
        max_results: Optional["capo_datazone.types.max_results.MaxResults"] = None,
    ) -> "capo_datazone.types.list_data_sources_output.ListDataSourcesOutput":
        """<p>Lists data sources in Amazon DataZone.</p>

        Args:
            domain_identifier: <p>The identifier of the Amazon DataZone domain in which to list the data sources.</p>
            project_identifier: <p>The identifier of the project in which to list data sources.</p>
            environment_identifier: <p>The identifier of the environment in which to list the data sources.</p>
            connection_identifier: <p>The ID of the connection.</p>
            type: <p>The type of the data source.</p>
            status: <p>The status of the data source.</p>
            name: <p>The name of the data source.</p>
            next_token: <p>When the number of data sources is greater than the default value for the <code>MaxResults</code> parameter, or if you explicitly specify a value for <code>MaxResults</code> that is less than the number of data sources, the response includes a pagination token named <code>NextToken</code>. You can specify this <code>NextToken</code> value in a subsequent call to <code>ListDataSources</code> to list the next set of data sources.</p>
            max_results: <p>The maximum number of data sources to return in a single call to <code>ListDataSources</code>. When the number of data sources to be listed is greater than the value of <code>MaxResults</code>, the response contains a <code>NextToken</code> value that you can use in a subsequent call to <code>ListDataSources</code> to list the next set of data sources.</p>

        Raises:
            capo_datazone.errors.access_denied_exception.AccessDeniedException: <p>You do not have sufficient access to perform this action.</p>
            capo_datazone.errors.throttling_exception.ThrottlingException: <p>The request was denied due to request throttling.</p>
            capo_datazone.errors.unauthorized_exception.UnauthorizedException: <p>You do not have permission to perform this action.</p>
            capo_datazone.errors.conflict_exception.ConflictException: <p>There is a conflict while performing this action.</p>
            capo_datazone.errors.internal_server_exception.InternalServerException: <p>The request has failed because of an unknown error, exception or failure.</p>
            capo_datazone.errors.resource_not_found_exception.ResourceNotFoundException: <p>The specified resource cannot be found.</p>
            capo_datazone.errors.service_quota_exceeded_exception.ServiceQuotaExceededException: <p>The request has exceeded the specified service quota.</p>
            capo_datazone.errors.validation_exception.ValidationException: <p>The input fails to satisfy the constraints specified by the Amazon Web Services service.</p>
            capo_datazone.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        async def _handler(
            req: "AsyncOperationRequest[capo_datazone.types.list_data_sources_input.ListDataSourcesInput]",
        ) -> AsyncOperationResponse[
            "capo_datazone.types.list_data_sources_output.ListDataSourcesOutput"
        ]:
            import capo_datazone._operations.data_zone.list_data_sources

            (
                output,
                http_response,
            ) = await capo_datazone._operations.data_zone.list_data_sources.async_list_data_sources(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_datazone.types.list_data_sources_input.ListDataSourcesInput = {
            "domain_identifier": domain_identifier,
            "project_identifier": project_identifier,
        }
        if environment_identifier is not None:
            input_["environment_identifier"] = environment_identifier
        if connection_identifier is not None:
            input_["connection_identifier"] = connection_identifier
        if type is not None:
            input_["type"] = type
        if status is not None:
            input_["status"] = status
        if name is not None:
            input_["name"] = name
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

    async def iter_list_data_sources(
        self,
        domain_identifier: "capo_datazone.types.domain_id.DomainId",
        project_identifier: str,
        *,
        config_overrides: Optional[AsyncDataZoneClientConfig] = None,
        environment_identifier: Optional[str] = None,
        connection_identifier: Optional[str] = None,
        type: Optional["capo_datazone.types.data_source_type.DataSourceType"] = None,
        status: Optional[
            "capo_datazone.types.data_source_status.DataSourceStatus"
        ] = None,
        name: Optional["capo_datazone.types.name.Name"] = None,
        next_token: Optional[
            "capo_datazone.types.pagination_token.PaginationToken"
        ] = None,
        max_results: Optional["capo_datazone.types.max_results.MaxResults"] = None,
    ) -> "AsyncIterator[capo_datazone.types.data_source_summary.DataSourceSummary]":
        _token = next_token
        while True:
            _response = await self.list_data_sources(
                domain_identifier,
                project_identifier,
                config_overrides=config_overrides,
                environment_identifier=environment_identifier,
                connection_identifier=connection_identifier,
                type=type,
                status=status,
                name=name,
                next_token=_token,
                max_results=max_results,
            )
            _page = _resolve_path(_response, ("items",))
            for _item in _page or []:
                yield _item
            _token = _resolve_path(_response, ("next_token",))
            if not _token:
                break

    async def start_data_source_run(
        self,
        domain_identifier: "capo_datazone.types.domain_id.DomainId",
        data_source_identifier: "capo_datazone.types.data_source_id.DataSourceId",
        *,
        config_overrides: Optional[AsyncDataZoneClientConfig] = None,
        client_token: Optional[str] = None,
    ) -> "capo_datazone.types.start_data_source_run_output.StartDataSourceRunOutput":
        """<p>Start the run of the specified data source in Amazon DataZone.</p>

        Args:
            domain_identifier: <p>The identifier of the Amazon DataZone domain in which to start a data source run.</p>
            data_source_identifier: <p>The identifier of the data source.</p>
            client_token: <p>A unique, case-sensitive identifier that is provided to ensure the idempotency of the request.</p>

        Raises:
            capo_datazone.errors.access_denied_exception.AccessDeniedException: <p>You do not have sufficient access to perform this action.</p>
            capo_datazone.errors.throttling_exception.ThrottlingException: <p>The request was denied due to request throttling.</p>
            capo_datazone.errors.unauthorized_exception.UnauthorizedException: <p>You do not have permission to perform this action.</p>
            capo_datazone.errors.conflict_exception.ConflictException: <p>There is a conflict while performing this action.</p>
            capo_datazone.errors.internal_server_exception.InternalServerException: <p>The request has failed because of an unknown error, exception or failure.</p>
            capo_datazone.errors.resource_not_found_exception.ResourceNotFoundException: <p>The specified resource cannot be found.</p>
            capo_datazone.errors.service_quota_exceeded_exception.ServiceQuotaExceededException: <p>The request has exceeded the specified service quota.</p>
            capo_datazone.errors.validation_exception.ValidationException: <p>The input fails to satisfy the constraints specified by the Amazon Web Services service.</p>
            capo_datazone.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        async def _handler(
            req: "AsyncOperationRequest[capo_datazone.types.start_data_source_run_input.StartDataSourceRunInput]",
        ) -> AsyncOperationResponse[
            "capo_datazone.types.start_data_source_run_output.StartDataSourceRunOutput"
        ]:
            import capo_datazone._operations.data_zone.start_data_source_run

            (
                output,
                http_response,
            ) = await capo_datazone._operations.data_zone.start_data_source_run.async_start_data_source_run(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_datazone.types.start_data_source_run_input.StartDataSourceRunInput = {
            "domain_identifier": domain_identifier,
            "data_source_identifier": data_source_identifier,
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

    async def get_data_source_run(
        self,
        domain_identifier: "capo_datazone.types.domain_id.DomainId",
        identifier: "capo_datazone.types.data_source_run_id.DataSourceRunId",
        *,
        config_overrides: Optional[AsyncDataZoneClientConfig] = None,
    ) -> "capo_datazone.types.get_data_source_run_output.GetDataSourceRunOutput":
        """<p>Gets an Amazon DataZone data source run.</p>

        Args:
            domain_identifier: <p>The ID of the domain in which this data source run was performed.</p>
            identifier: <p>The ID of the data source run.</p>

        Raises:
            capo_datazone.errors.access_denied_exception.AccessDeniedException: <p>You do not have sufficient access to perform this action.</p>
            capo_datazone.errors.throttling_exception.ThrottlingException: <p>The request was denied due to request throttling.</p>
            capo_datazone.errors.unauthorized_exception.UnauthorizedException: <p>You do not have permission to perform this action.</p>
            capo_datazone.errors.conflict_exception.ConflictException: <p>There is a conflict while performing this action.</p>
            capo_datazone.errors.internal_server_exception.InternalServerException: <p>The request has failed because of an unknown error, exception or failure.</p>
            capo_datazone.errors.resource_not_found_exception.ResourceNotFoundException: <p>The specified resource cannot be found.</p>
            capo_datazone.errors.service_quota_exceeded_exception.ServiceQuotaExceededException: <p>The request has exceeded the specified service quota.</p>
            capo_datazone.errors.validation_exception.ValidationException: <p>The input fails to satisfy the constraints specified by the Amazon Web Services service.</p>
            capo_datazone.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        async def _handler(
            req: "AsyncOperationRequest[capo_datazone.types.get_data_source_run_input.GetDataSourceRunInput]",
        ) -> AsyncOperationResponse[
            "capo_datazone.types.get_data_source_run_output.GetDataSourceRunOutput"
        ]:
            import capo_datazone._operations.data_zone.get_data_source_run

            (
                output,
                http_response,
            ) = await capo_datazone._operations.data_zone.get_data_source_run.async_get_data_source_run(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_datazone.types.get_data_source_run_input.GetDataSourceRunInput = {
            "domain_identifier": domain_identifier,
            "identifier": identifier,
        }

        response = await aexecute_pipeline(
            AsyncOperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        await response.response.aclose()
        return response.output

    async def list_data_source_runs(
        self,
        domain_identifier: "capo_datazone.types.domain_id.DomainId",
        data_source_identifier: "capo_datazone.types.data_source_id.DataSourceId",
        *,
        config_overrides: Optional[AsyncDataZoneClientConfig] = None,
        status: Optional[
            "capo_datazone.types.data_source_run_status.DataSourceRunStatus"
        ] = None,
        next_token: Optional[
            "capo_datazone.types.pagination_token.PaginationToken"
        ] = None,
        max_results: Optional["capo_datazone.types.max_results.MaxResults"] = None,
    ) -> "capo_datazone.types.list_data_source_runs_output.ListDataSourceRunsOutput":
        """<p>Lists data source runs in Amazon DataZone.</p>

        Args:
            domain_identifier: <p>The identifier of the Amazon DataZone domain in which to invoke the <code>ListDataSourceRuns</code> action.</p>
            data_source_identifier: <p>The identifier of the data source.</p>
            status: <p>The status of the data source.</p>
            next_token: <p>When the number of runs is greater than the default value for the <code>MaxResults</code> parameter, or if you explicitly specify a value for <code>MaxResults</code> that is less than the number of runs, the response includes a pagination token named <code>NextToken</code>. You can specify this <code>NextToken</code> value in a subsequent call to <code>ListDataSourceRuns</code> to list the next set of runs.</p>
            max_results: <p>The maximum number of runs to return in a single call to <code>ListDataSourceRuns</code>. When the number of runs to be listed is greater than the value of <code>MaxResults</code>, the response contains a <code>NextToken</code> value that you can use in a subsequent call to <code>ListDataSourceRuns</code> to list the next set of runs.</p>

        Raises:
            capo_datazone.errors.access_denied_exception.AccessDeniedException: <p>You do not have sufficient access to perform this action.</p>
            capo_datazone.errors.throttling_exception.ThrottlingException: <p>The request was denied due to request throttling.</p>
            capo_datazone.errors.unauthorized_exception.UnauthorizedException: <p>You do not have permission to perform this action.</p>
            capo_datazone.errors.conflict_exception.ConflictException: <p>There is a conflict while performing this action.</p>
            capo_datazone.errors.internal_server_exception.InternalServerException: <p>The request has failed because of an unknown error, exception or failure.</p>
            capo_datazone.errors.resource_not_found_exception.ResourceNotFoundException: <p>The specified resource cannot be found.</p>
            capo_datazone.errors.service_quota_exceeded_exception.ServiceQuotaExceededException: <p>The request has exceeded the specified service quota.</p>
            capo_datazone.errors.validation_exception.ValidationException: <p>The input fails to satisfy the constraints specified by the Amazon Web Services service.</p>
            capo_datazone.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        async def _handler(
            req: "AsyncOperationRequest[capo_datazone.types.list_data_source_runs_input.ListDataSourceRunsInput]",
        ) -> AsyncOperationResponse[
            "capo_datazone.types.list_data_source_runs_output.ListDataSourceRunsOutput"
        ]:
            import capo_datazone._operations.data_zone.list_data_source_runs

            (
                output,
                http_response,
            ) = await capo_datazone._operations.data_zone.list_data_source_runs.async_list_data_source_runs(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_datazone.types.list_data_source_runs_input.ListDataSourceRunsInput = {
            "domain_identifier": domain_identifier,
            "data_source_identifier": data_source_identifier,
        }
        if status is not None:
            input_["status"] = status
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

    async def iter_list_data_source_runs(
        self,
        domain_identifier: "capo_datazone.types.domain_id.DomainId",
        data_source_identifier: "capo_datazone.types.data_source_id.DataSourceId",
        *,
        config_overrides: Optional[AsyncDataZoneClientConfig] = None,
        status: Optional[
            "capo_datazone.types.data_source_run_status.DataSourceRunStatus"
        ] = None,
        next_token: Optional[
            "capo_datazone.types.pagination_token.PaginationToken"
        ] = None,
        max_results: Optional["capo_datazone.types.max_results.MaxResults"] = None,
    ) -> "AsyncIterator[capo_datazone.types.data_source_run_summary.DataSourceRunSummary]":
        _token = next_token
        while True:
            _response = await self.list_data_source_runs(
                domain_identifier,
                data_source_identifier,
                config_overrides=config_overrides,
                status=status,
                next_token=_token,
                max_results=max_results,
            )
            _page = _resolve_path(_response, ("items",))
            for _item in _page or []:
                yield _item
            _token = _resolve_path(_response, ("next_token",))
            if not _token:
                break

    async def create_domain(
        self,
        name: str,
        *,
        config_overrides: Optional[AsyncDataZoneClientConfig] = None,
        description: Optional[str] = None,
        single_sign_on: Optional[
            "capo_datazone.types.single_sign_on.SingleSignOn"
        ] = None,
        domain_execution_role: Optional["capo_datazone.types.role_arn.RoleArn"] = None,
        kms_key_identifier: Optional[
            "capo_datazone.types.kms_key_arn.KmsKeyArn"
        ] = None,
        tags: Optional["capo_datazone.types.tags.Tags"] = None,
        domain_version: Optional[
            "capo_datazone.types.domain_version.DomainVersion"
        ] = None,
        service_role: Optional["capo_datazone.types.role_arn.RoleArn"] = None,
        client_token: Optional[str] = None,
    ) -> "capo_datazone.types.create_domain_output.CreateDomainOutput":
        """<p>Creates an Amazon DataZone domain.</p>

        Args:
            name: <p>The name of the Amazon DataZone domain.</p>
            description: <p>The description of the Amazon DataZone domain.</p>
            single_sign_on: <p>The single-sign on configuration of the Amazon DataZone domain.</p>
            domain_execution_role: <p>The domain execution role that is created when an Amazon DataZone domain is created. The domain execution role is created in the Amazon Web Services account that houses the Amazon DataZone domain.</p>
            kms_key_identifier: <p>The identifier of the Amazon Web Services Key Management Service (KMS) key that is used to encrypt the Amazon DataZone domain, metadata, and reporting data. </p>
            tags: <p>The tags specified for the Amazon DataZone domain.</p>
            domain_version: <p>The version of the domain that is created.</p>
            service_role: <p>The service role of the domain that is created.</p>
            client_token: <p>A unique, case-sensitive identifier that is provided to ensure the idempotency of the request.</p>

        Raises:
            capo_datazone.errors.access_denied_exception.AccessDeniedException: <p>You do not have sufficient access to perform this action.</p>
            capo_datazone.errors.throttling_exception.ThrottlingException: <p>The request was denied due to request throttling.</p>
            capo_datazone.errors.unauthorized_exception.UnauthorizedException: <p>You do not have permission to perform this action.</p>
            capo_datazone.errors.conflict_exception.ConflictException: <p>There is a conflict while performing this action.</p>
            capo_datazone.errors.internal_server_exception.InternalServerException: <p>The request has failed because of an unknown error, exception or failure.</p>
            capo_datazone.errors.resource_not_found_exception.ResourceNotFoundException: <p>The specified resource cannot be found.</p>
            capo_datazone.errors.service_quota_exceeded_exception.ServiceQuotaExceededException: <p>The request has exceeded the specified service quota.</p>
            capo_datazone.errors.validation_exception.ValidationException: <p>The input fails to satisfy the constraints specified by the Amazon Web Services service.</p>
            capo_datazone.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        async def _handler(
            req: "AsyncOperationRequest[capo_datazone.types.create_domain_input.CreateDomainInput]",
        ) -> AsyncOperationResponse[
            "capo_datazone.types.create_domain_output.CreateDomainOutput"
        ]:
            import capo_datazone._operations.data_zone.create_domain

            (
                output,
                http_response,
            ) = await capo_datazone._operations.data_zone.create_domain.async_create_domain(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_datazone.types.create_domain_input.CreateDomainInput = {
            "name": name
        }
        if description is not None:
            input_["description"] = description
        if single_sign_on is not None:
            input_["single_sign_on"] = single_sign_on
        if domain_execution_role is not None:
            input_["domain_execution_role"] = domain_execution_role
        if kms_key_identifier is not None:
            input_["kms_key_identifier"] = kms_key_identifier
        if tags is not None:
            input_["tags"] = tags
        if domain_version is not None:
            input_["domain_version"] = domain_version
        if service_role is not None:
            input_["service_role"] = service_role
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

    async def get_domain(
        self,
        identifier: "capo_datazone.types.domain_id.DomainId",
        *,
        config_overrides: Optional[AsyncDataZoneClientConfig] = None,
    ) -> "capo_datazone.types.get_domain_output.GetDomainOutput":
        """<p>Gets an Amazon DataZone domain.</p>

        Args:
            identifier: <p>The identifier of the specified Amazon DataZone domain.</p>

        Raises:
            capo_datazone.errors.access_denied_exception.AccessDeniedException: <p>You do not have sufficient access to perform this action.</p>
            capo_datazone.errors.throttling_exception.ThrottlingException: <p>The request was denied due to request throttling.</p>
            capo_datazone.errors.unauthorized_exception.UnauthorizedException: <p>You do not have permission to perform this action.</p>
            capo_datazone.errors.internal_server_exception.InternalServerException: <p>The request has failed because of an unknown error, exception or failure.</p>
            capo_datazone.errors.resource_not_found_exception.ResourceNotFoundException: <p>The specified resource cannot be found.</p>
            capo_datazone.errors.service_quota_exceeded_exception.ServiceQuotaExceededException: <p>The request has exceeded the specified service quota.</p>
            capo_datazone.errors.validation_exception.ValidationException: <p>The input fails to satisfy the constraints specified by the Amazon Web Services service.</p>
            capo_datazone.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        async def _handler(
            req: "AsyncOperationRequest[capo_datazone.types.get_domain_input.GetDomainInput]",
        ) -> AsyncOperationResponse[
            "capo_datazone.types.get_domain_output.GetDomainOutput"
        ]:
            import capo_datazone._operations.data_zone.get_domain

            (
                output,
                http_response,
            ) = await capo_datazone._operations.data_zone.get_domain.async_get_domain(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_datazone.types.get_domain_input.GetDomainInput = {
            "identifier": identifier
        }

        response = await aexecute_pipeline(
            AsyncOperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        await response.response.aclose()
        return response.output

    async def update_domain(
        self,
        identifier: "capo_datazone.types.domain_id.DomainId",
        *,
        config_overrides: Optional[AsyncDataZoneClientConfig] = None,
        description: Optional[str] = None,
        single_sign_on: Optional[
            "capo_datazone.types.single_sign_on.SingleSignOn"
        ] = None,
        domain_execution_role: Optional["capo_datazone.types.role_arn.RoleArn"] = None,
        service_role: Optional["capo_datazone.types.role_arn.RoleArn"] = None,
        name: Optional[str] = None,
        client_token: Optional[str] = None,
    ) -> "capo_datazone.types.update_domain_output.UpdateDomainOutput":
        """<p>Updates a Amazon DataZone domain.</p>

        Args:
            identifier: <p>The ID of the Amazon Web Services domain that is to be updated.</p>
            description: <p>The description to be updated as part of the <code>UpdateDomain</code> action.</p>
            single_sign_on: <p>The single sign-on option to be updated as part of the <code>UpdateDomain</code> action.</p>
            domain_execution_role: <p>The domain execution role to be updated as part of the <code>UpdateDomain</code> action.</p>
            service_role: <p>The service role of the domain.</p>
            name: <p>The name to be updated as part of the <code>UpdateDomain</code> action.</p>
            client_token: <p>A unique, case-sensitive identifier that is provided to ensure the idempotency of the request.</p>

        Raises:
            capo_datazone.errors.access_denied_exception.AccessDeniedException: <p>You do not have sufficient access to perform this action.</p>
            capo_datazone.errors.throttling_exception.ThrottlingException: <p>The request was denied due to request throttling.</p>
            capo_datazone.errors.unauthorized_exception.UnauthorizedException: <p>You do not have permission to perform this action.</p>
            capo_datazone.errors.conflict_exception.ConflictException: <p>There is a conflict while performing this action.</p>
            capo_datazone.errors.internal_server_exception.InternalServerException: <p>The request has failed because of an unknown error, exception or failure.</p>
            capo_datazone.errors.resource_not_found_exception.ResourceNotFoundException: <p>The specified resource cannot be found.</p>
            capo_datazone.errors.service_quota_exceeded_exception.ServiceQuotaExceededException: <p>The request has exceeded the specified service quota.</p>
            capo_datazone.errors.validation_exception.ValidationException: <p>The input fails to satisfy the constraints specified by the Amazon Web Services service.</p>
            capo_datazone.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        async def _handler(
            req: "AsyncOperationRequest[capo_datazone.types.update_domain_input.UpdateDomainInput]",
        ) -> AsyncOperationResponse[
            "capo_datazone.types.update_domain_output.UpdateDomainOutput"
        ]:
            import capo_datazone._operations.data_zone.update_domain

            (
                output,
                http_response,
            ) = await capo_datazone._operations.data_zone.update_domain.async_update_domain(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_datazone.types.update_domain_input.UpdateDomainInput = {
            "identifier": identifier
        }
        if description is not None:
            input_["description"] = description
        if single_sign_on is not None:
            input_["single_sign_on"] = single_sign_on
        if domain_execution_role is not None:
            input_["domain_execution_role"] = domain_execution_role
        if service_role is not None:
            input_["service_role"] = service_role
        if name is not None:
            input_["name"] = name
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

    async def delete_domain(
        self,
        identifier: "capo_datazone.types.domain_id.DomainId",
        *,
        config_overrides: Optional[AsyncDataZoneClientConfig] = None,
        client_token: Optional[str] = None,
        skip_deletion_check: Optional[bool] = None,
        cascade_delete: Optional[bool] = None,
    ) -> "capo_datazone.types.delete_domain_output.DeleteDomainOutput":
        """<p>Deletes a Amazon DataZone domain.</p>

        Args:
            identifier: <p>The identifier of the Amazon Web Services domain that is to be deleted.</p>
            client_token: <p>A unique, case-sensitive identifier that is provided to ensure the idempotency of the request.</p>
            skip_deletion_check: <p>Specifies whether to skip the check that prevents deletion of a domain that still contains resources. When you use this parameter, Amazon DataZone deletes the domain but might not remove its associated resources, which can leave orphaned resources behind. To delete a domain and fully clean up its associated resources, use <code>cascadeDelete</code> instead. You can't use this parameter together with <code>cascadeDelete</code>.</p>
            cascade_delete: <p>Specifies whether to delete the domain along with all of its associated resources. When you use this parameter, Amazon DataZone deletes the domain and cleanly removes its associated resources without leaving orphaned resources behind. Amazon DataZone reports deletion progress in the <code>deleteProgress</code> field. Amazon DataZone reports any resources that it can't delete in the <code>failureReasons</code> field of the <code>GetDomain</code> response. You can't use this parameter together with <code>skipDeletionCheck</code>. If you don't specify a value, the default is <code>false</code>.</p>

        Raises:
            capo_datazone.errors.access_denied_exception.AccessDeniedException: <p>You do not have sufficient access to perform this action.</p>
            capo_datazone.errors.throttling_exception.ThrottlingException: <p>The request was denied due to request throttling.</p>
            capo_datazone.errors.unauthorized_exception.UnauthorizedException: <p>You do not have permission to perform this action.</p>
            capo_datazone.errors.conflict_exception.ConflictException: <p>There is a conflict while performing this action.</p>
            capo_datazone.errors.internal_server_exception.InternalServerException: <p>The request has failed because of an unknown error, exception or failure.</p>
            capo_datazone.errors.resource_not_found_exception.ResourceNotFoundException: <p>The specified resource cannot be found.</p>
            capo_datazone.errors.validation_exception.ValidationException: <p>The input fails to satisfy the constraints specified by the Amazon Web Services service.</p>
            capo_datazone.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        async def _handler(
            req: "AsyncOperationRequest[capo_datazone.types.delete_domain_input.DeleteDomainInput]",
        ) -> AsyncOperationResponse[
            "capo_datazone.types.delete_domain_output.DeleteDomainOutput"
        ]:
            import capo_datazone._operations.data_zone.delete_domain

            (
                output,
                http_response,
            ) = await capo_datazone._operations.data_zone.delete_domain.async_delete_domain(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_datazone.types.delete_domain_input.DeleteDomainInput = {
            "identifier": identifier
        }
        if client_token is None:
            client_token = str(uuid.uuid4())
        input_["client_token"] = client_token
        if skip_deletion_check is not None:
            input_["skip_deletion_check"] = skip_deletion_check
        if cascade_delete is not None:
            input_["cascade_delete"] = cascade_delete

        response = await aexecute_pipeline(
            AsyncOperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        await response.response.aclose()
        return response.output

    async def list_domains(
        self,
        *,
        config_overrides: Optional[AsyncDataZoneClientConfig] = None,
        status: Optional["capo_datazone.types.domain_status.DomainStatus"] = None,
        max_results: Optional[
            "capo_datazone.types.max_results_for_list_domains.MaxResultsForListDomains"
        ] = None,
        next_token: Optional[
            "capo_datazone.types.pagination_token.PaginationToken"
        ] = None,
    ) -> "capo_datazone.types.list_domains_output.ListDomainsOutput":
        """<p>Lists Amazon DataZone domains.</p>

        Args:
            status: <p>The status of the data source.</p>
            max_results: <p>The maximum number of domains to return in a single call to <code>ListDomains</code>. When the number of domains to be listed is greater than the value of <code>MaxResults</code>, the response contains a <code>NextToken</code> value that you can use in a subsequent call to <code>ListDomains</code> to list the next set of domains.</p>
            next_token: <p>When the number of domains is greater than the default value for the <code>MaxResults</code> parameter, or if you explicitly specify a value for <code>MaxResults</code> that is less than the number of domains, the response includes a pagination token named <code>NextToken</code>. You can specify this <code>NextToken</code> value in a subsequent call to <code>ListDomains</code> to list the next set of domains.</p>

        Raises:
            capo_datazone.errors.access_denied_exception.AccessDeniedException: <p>You do not have sufficient access to perform this action.</p>
            capo_datazone.errors.throttling_exception.ThrottlingException: <p>The request was denied due to request throttling.</p>
            capo_datazone.errors.unauthorized_exception.UnauthorizedException: <p>You do not have permission to perform this action.</p>
            capo_datazone.errors.conflict_exception.ConflictException: <p>There is a conflict while performing this action.</p>
            capo_datazone.errors.internal_server_exception.InternalServerException: <p>The request has failed because of an unknown error, exception or failure.</p>
            capo_datazone.errors.resource_not_found_exception.ResourceNotFoundException: <p>The specified resource cannot be found.</p>
            capo_datazone.errors.service_quota_exceeded_exception.ServiceQuotaExceededException: <p>The request has exceeded the specified service quota.</p>
            capo_datazone.errors.validation_exception.ValidationException: <p>The input fails to satisfy the constraints specified by the Amazon Web Services service.</p>
            capo_datazone.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        async def _handler(
            req: "AsyncOperationRequest[capo_datazone.types.list_domains_input.ListDomainsInput]",
        ) -> AsyncOperationResponse[
            "capo_datazone.types.list_domains_output.ListDomainsOutput"
        ]:
            import capo_datazone._operations.data_zone.list_domains

            (
                output,
                http_response,
            ) = await capo_datazone._operations.data_zone.list_domains.async_list_domains(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_datazone.types.list_domains_input.ListDomainsInput = {}
        if status is not None:
            input_["status"] = status
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

    async def iter_list_domains(
        self,
        *,
        config_overrides: Optional[AsyncDataZoneClientConfig] = None,
        status: Optional["capo_datazone.types.domain_status.DomainStatus"] = None,
        max_results: Optional[
            "capo_datazone.types.max_results_for_list_domains.MaxResultsForListDomains"
        ] = None,
        next_token: Optional[
            "capo_datazone.types.pagination_token.PaginationToken"
        ] = None,
    ) -> "AsyncIterator[capo_datazone.types.domain_summary.DomainSummary]":
        _token = next_token
        while True:
            _response = await self.list_domains(
                config_overrides=config_overrides,
                status=status,
                max_results=max_results,
                next_token=_token,
            )
            _page = _resolve_path(_response, ("items",))
            for _item in _page or []:
                yield _item
            _token = _resolve_path(_response, ("next_token",))
            if not _token:
                break

    async def create_domain_unit(
        self,
        domain_identifier: "capo_datazone.types.domain_id.DomainId",
        name: "capo_datazone.types.domain_unit_name.DomainUnitName",
        parent_domain_unit_identifier: "capo_datazone.types.domain_unit_id.DomainUnitId",
        *,
        config_overrides: Optional[AsyncDataZoneClientConfig] = None,
        description: Optional[
            "capo_datazone.types.domain_unit_description.DomainUnitDescription"
        ] = None,
        client_token: Optional["capo_datazone.types.client_token.ClientToken"] = None,
    ) -> "capo_datazone.types.create_domain_unit_output.CreateDomainUnitOutput":
        """<p>Creates a domain unit in Amazon DataZone.</p>

        Args:
            domain_identifier: <p>The ID of the domain where you want to crate a domain unit.</p>
            name: <p>The name of the domain unit.</p>
            parent_domain_unit_identifier: <p>The ID of the parent domain unit.</p>
            description: <p>The description of the domain unit.</p>
            client_token: <p>A unique, case-sensitive identifier that is provided to ensure the idempotency of the request.</p>

        Raises:
            capo_datazone.errors.access_denied_exception.AccessDeniedException: <p>You do not have sufficient access to perform this action.</p>
            capo_datazone.errors.throttling_exception.ThrottlingException: <p>The request was denied due to request throttling.</p>
            capo_datazone.errors.unauthorized_exception.UnauthorizedException: <p>You do not have permission to perform this action.</p>
            capo_datazone.errors.conflict_exception.ConflictException: <p>There is a conflict while performing this action.</p>
            capo_datazone.errors.internal_server_exception.InternalServerException: <p>The request has failed because of an unknown error, exception or failure.</p>
            capo_datazone.errors.service_quota_exceeded_exception.ServiceQuotaExceededException: <p>The request has exceeded the specified service quota.</p>
            capo_datazone.errors.validation_exception.ValidationException: <p>The input fails to satisfy the constraints specified by the Amazon Web Services service.</p>
            capo_datazone.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        async def _handler(
            req: "AsyncOperationRequest[capo_datazone.types.create_domain_unit_input.CreateDomainUnitInput]",
        ) -> AsyncOperationResponse[
            "capo_datazone.types.create_domain_unit_output.CreateDomainUnitOutput"
        ]:
            import capo_datazone._operations.data_zone.create_domain_unit

            (
                output,
                http_response,
            ) = await capo_datazone._operations.data_zone.create_domain_unit.async_create_domain_unit(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_datazone.types.create_domain_unit_input.CreateDomainUnitInput = {
            "domain_identifier": domain_identifier,
            "name": name,
            "parent_domain_unit_identifier": parent_domain_unit_identifier,
        }
        if description is not None:
            input_["description"] = description
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

    async def get_domain_unit(
        self,
        domain_identifier: "capo_datazone.types.domain_id.DomainId",
        identifier: "capo_datazone.types.domain_unit_id.DomainUnitId",
        *,
        config_overrides: Optional[AsyncDataZoneClientConfig] = None,
    ) -> "capo_datazone.types.get_domain_unit_output.GetDomainUnitOutput":
        """<p>Gets the details of the specified domain unit.</p>

        Args:
            domain_identifier: <p>The ID of the domain where you want to get a domain unit.</p>
            identifier: <p>The identifier of the domain unit that you want to get.</p>

        Raises:
            capo_datazone.errors.access_denied_exception.AccessDeniedException: <p>You do not have sufficient access to perform this action.</p>
            capo_datazone.errors.throttling_exception.ThrottlingException: <p>The request was denied due to request throttling.</p>
            capo_datazone.errors.unauthorized_exception.UnauthorizedException: <p>You do not have permission to perform this action.</p>
            capo_datazone.errors.internal_server_exception.InternalServerException: <p>The request has failed because of an unknown error, exception or failure.</p>
            capo_datazone.errors.resource_not_found_exception.ResourceNotFoundException: <p>The specified resource cannot be found.</p>
            capo_datazone.errors.validation_exception.ValidationException: <p>The input fails to satisfy the constraints specified by the Amazon Web Services service.</p>
            capo_datazone.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        async def _handler(
            req: "AsyncOperationRequest[capo_datazone.types.get_domain_unit_input.GetDomainUnitInput]",
        ) -> AsyncOperationResponse[
            "capo_datazone.types.get_domain_unit_output.GetDomainUnitOutput"
        ]:
            import capo_datazone._operations.data_zone.get_domain_unit

            (
                output,
                http_response,
            ) = await capo_datazone._operations.data_zone.get_domain_unit.async_get_domain_unit(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_datazone.types.get_domain_unit_input.GetDomainUnitInput = {
            "domain_identifier": domain_identifier,
            "identifier": identifier,
        }

        response = await aexecute_pipeline(
            AsyncOperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        await response.response.aclose()
        return response.output

    async def update_domain_unit(
        self,
        domain_identifier: "capo_datazone.types.domain_id.DomainId",
        identifier: "capo_datazone.types.domain_unit_id.DomainUnitId",
        *,
        config_overrides: Optional[AsyncDataZoneClientConfig] = None,
        description: Optional[
            "capo_datazone.types.domain_unit_description.DomainUnitDescription"
        ] = None,
        name: Optional["capo_datazone.types.domain_unit_name.DomainUnitName"] = None,
    ) -> "capo_datazone.types.update_domain_unit_output.UpdateDomainUnitOutput":
        """<p>Updates the domain unit.</p>

        Args:
            domain_identifier: <p>The ID of the domain where you want to update a domain unit.</p>
            identifier: <p>The ID of the domain unit that you want to update.</p>
            description: <p>The description of the domain unit that you want to update.</p>
            name: <p>The name of the domain unit that you want to update.</p>

        Raises:
            capo_datazone.errors.access_denied_exception.AccessDeniedException: <p>You do not have sufficient access to perform this action.</p>
            capo_datazone.errors.throttling_exception.ThrottlingException: <p>The request was denied due to request throttling.</p>
            capo_datazone.errors.unauthorized_exception.UnauthorizedException: <p>You do not have permission to perform this action.</p>
            capo_datazone.errors.conflict_exception.ConflictException: <p>There is a conflict while performing this action.</p>
            capo_datazone.errors.internal_server_exception.InternalServerException: <p>The request has failed because of an unknown error, exception or failure.</p>
            capo_datazone.errors.resource_not_found_exception.ResourceNotFoundException: <p>The specified resource cannot be found.</p>
            capo_datazone.errors.validation_exception.ValidationException: <p>The input fails to satisfy the constraints specified by the Amazon Web Services service.</p>
            capo_datazone.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        async def _handler(
            req: "AsyncOperationRequest[capo_datazone.types.update_domain_unit_input.UpdateDomainUnitInput]",
        ) -> AsyncOperationResponse[
            "capo_datazone.types.update_domain_unit_output.UpdateDomainUnitOutput"
        ]:
            import capo_datazone._operations.data_zone.update_domain_unit

            (
                output,
                http_response,
            ) = await capo_datazone._operations.data_zone.update_domain_unit.async_update_domain_unit(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_datazone.types.update_domain_unit_input.UpdateDomainUnitInput = {
            "domain_identifier": domain_identifier,
            "identifier": identifier,
        }
        if description is not None:
            input_["description"] = description
        if name is not None:
            input_["name"] = name

        response = await aexecute_pipeline(
            AsyncOperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        await response.response.aclose()
        return response.output

    async def delete_domain_unit(
        self,
        domain_identifier: "capo_datazone.types.domain_id.DomainId",
        identifier: "capo_datazone.types.domain_unit_id.DomainUnitId",
        *,
        config_overrides: Optional[AsyncDataZoneClientConfig] = None,
    ) -> "capo_datazone.types.delete_domain_unit_output.DeleteDomainUnitOutput":
        """<p>Deletes a domain unit.</p>

        Args:
            domain_identifier: <p>The ID of the domain where you want to delete a domain unit.</p>
            identifier: <p>The ID of the domain unit that you want to delete.</p>

        Raises:
            capo_datazone.errors.access_denied_exception.AccessDeniedException: <p>You do not have sufficient access to perform this action.</p>
            capo_datazone.errors.throttling_exception.ThrottlingException: <p>The request was denied due to request throttling.</p>
            capo_datazone.errors.unauthorized_exception.UnauthorizedException: <p>You do not have permission to perform this action.</p>
            capo_datazone.errors.conflict_exception.ConflictException: <p>There is a conflict while performing this action.</p>
            capo_datazone.errors.internal_server_exception.InternalServerException: <p>The request has failed because of an unknown error, exception or failure.</p>
            capo_datazone.errors.resource_not_found_exception.ResourceNotFoundException: <p>The specified resource cannot be found.</p>
            capo_datazone.errors.validation_exception.ValidationException: <p>The input fails to satisfy the constraints specified by the Amazon Web Services service.</p>
            capo_datazone.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        async def _handler(
            req: "AsyncOperationRequest[capo_datazone.types.delete_domain_unit_input.DeleteDomainUnitInput]",
        ) -> AsyncOperationResponse[
            "capo_datazone.types.delete_domain_unit_output.DeleteDomainUnitOutput"
        ]:
            import capo_datazone._operations.data_zone.delete_domain_unit

            (
                output,
                http_response,
            ) = await capo_datazone._operations.data_zone.delete_domain_unit.async_delete_domain_unit(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_datazone.types.delete_domain_unit_input.DeleteDomainUnitInput = {
            "domain_identifier": domain_identifier,
            "identifier": identifier,
        }

        response = await aexecute_pipeline(
            AsyncOperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        await response.response.aclose()
        return response.output

    async def list_domain_units_for_parent(
        self,
        domain_identifier: "capo_datazone.types.domain_id.DomainId",
        parent_domain_unit_identifier: "capo_datazone.types.domain_unit_id.DomainUnitId",
        *,
        config_overrides: Optional[AsyncDataZoneClientConfig] = None,
        max_results: Optional[
            "capo_datazone.types.max_results_for_list_domains.MaxResultsForListDomains"
        ] = None,
        next_token: Optional[
            "capo_datazone.types.pagination_token.PaginationToken"
        ] = None,
    ) -> "capo_datazone.types.list_domain_units_for_parent_output.ListDomainUnitsForParentOutput":
        """<p>Lists child domain units for the specified parent domain unit.</p>

        Args:
            domain_identifier: <p>The ID of the domain in which you want to list domain units for a parent domain unit.</p>
            parent_domain_unit_identifier: <p>The ID of the parent domain unit.</p>
            max_results: <p>The maximum number of domain units to return in a single call to ListDomainUnitsForParent. When the number of domain units to be listed is greater than the value of MaxResults, the response contains a NextToken value that you can use in a subsequent call to ListDomainUnitsForParent to list the next set of domain units.</p>
            next_token: <p>When the number of domain units is greater than the default value for the MaxResults parameter, or if you explicitly specify a value for MaxResults that is less than the number of domain units, the response includes a pagination token named NextToken. You can specify this NextToken value in a subsequent call to ListDomainUnitsForParent to list the next set of domain units.</p>

        Raises:
            capo_datazone.errors.access_denied_exception.AccessDeniedException: <p>You do not have sufficient access to perform this action.</p>
            capo_datazone.errors.throttling_exception.ThrottlingException: <p>The request was denied due to request throttling.</p>
            capo_datazone.errors.unauthorized_exception.UnauthorizedException: <p>You do not have permission to perform this action.</p>
            capo_datazone.errors.internal_server_exception.InternalServerException: <p>The request has failed because of an unknown error, exception or failure.</p>
            capo_datazone.errors.validation_exception.ValidationException: <p>The input fails to satisfy the constraints specified by the Amazon Web Services service.</p>
            capo_datazone.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        async def _handler(
            req: "AsyncOperationRequest[capo_datazone.types.list_domain_units_for_parent_input.ListDomainUnitsForParentInput]",
        ) -> AsyncOperationResponse[
            "capo_datazone.types.list_domain_units_for_parent_output.ListDomainUnitsForParentOutput"
        ]:
            import capo_datazone._operations.data_zone.list_domain_units_for_parent

            (
                output,
                http_response,
            ) = await capo_datazone._operations.data_zone.list_domain_units_for_parent.async_list_domain_units_for_parent(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_datazone.types.list_domain_units_for_parent_input.ListDomainUnitsForParentInput = {
            "domain_identifier": domain_identifier,
            "parent_domain_unit_identifier": parent_domain_unit_identifier,
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

    async def iter_list_domain_units_for_parent(
        self,
        domain_identifier: "capo_datazone.types.domain_id.DomainId",
        parent_domain_unit_identifier: "capo_datazone.types.domain_unit_id.DomainUnitId",
        *,
        config_overrides: Optional[AsyncDataZoneClientConfig] = None,
        max_results: Optional[
            "capo_datazone.types.max_results_for_list_domains.MaxResultsForListDomains"
        ] = None,
        next_token: Optional[
            "capo_datazone.types.pagination_token.PaginationToken"
        ] = None,
    ) -> "AsyncIterator[capo_datazone.types.domain_unit_summary.DomainUnitSummary]":
        _token = next_token
        while True:
            _response = await self.list_domain_units_for_parent(
                domain_identifier,
                parent_domain_unit_identifier,
                config_overrides=config_overrides,
                max_results=max_results,
                next_token=_token,
            )
            _page = _resolve_path(_response, ("items",))
            for _item in _page or []:
                yield _item
            _token = _resolve_path(_response, ("next_token",))
            if not _token:
                break

    async def put_environment_blueprint_configuration(
        self,
        domain_identifier: "capo_datazone.types.domain_id.DomainId",
        environment_blueprint_identifier: "capo_datazone.types.environment_blueprint_id.EnvironmentBlueprintId",
        enabled_regions: "capo_datazone.types.enabled_region_list.EnabledRegionList",
        *,
        config_overrides: Optional[AsyncDataZoneClientConfig] = None,
        provisioning_role_arn: Optional["capo_datazone.types.role_arn.RoleArn"] = None,
        manage_access_role_arn: Optional["capo_datazone.types.role_arn.RoleArn"] = None,
        environment_role_permission_boundary: Optional[
            "capo_datazone.types.policy_arn.PolicyArn"
        ] = None,
        regional_parameters: Optional[
            "capo_datazone.types.regional_parameter_map.RegionalParameterMap"
        ] = None,
        resource_configurations: Optional[
            "capo_datazone.types.put_resource_configurations.PutResourceConfigurations"
        ] = None,
        allow_user_provided_configurations: Optional[bool] = None,
        global_parameters: Optional[
            "capo_datazone.types.global_parameter_map.GlobalParameterMap"
        ] = None,
        provisioning_configurations: Optional[
            "capo_datazone.types.provisioning_configuration_list.ProvisioningConfigurationList"
        ] = None,
    ) -> "capo_datazone.types.put_environment_blueprint_configuration_output.PutEnvironmentBlueprintConfigurationOutput":
        """<p>Writes the configuration for the specified environment blueprint in Amazon DataZone.</p>

        Args:
            domain_identifier: <p>The identifier of the Amazon DataZone domain.</p>
            environment_blueprint_identifier: <p>The identifier of the environment blueprint.</p>
            provisioning_role_arn: <p>The ARN of the provisioning role.</p>
            manage_access_role_arn: <p>The ARN of the manage access role.</p>
            environment_role_permission_boundary: <p>The environment role permissions boundary.</p>
            enabled_regions: <p>Specifies the enabled Amazon Web Services Regions.</p>
            regional_parameters: <p>The regional parameters in the environment blueprint.</p>
            resource_configurations: <p>The resource configurations of the environment blueprint.</p>
            allow_user_provided_configurations: <p>Specifies whether user-provided resource configurations are allowed for the environment blueprint.</p>
            global_parameters: <p>Region-agnostic environment blueprint parameters. </p>
            provisioning_configurations: <p>The provisioning configuration of a blueprint.</p>

        Raises:
            capo_datazone.errors.access_denied_exception.AccessDeniedException: <p>You do not have sufficient access to perform this action.</p>
            capo_datazone.errors.throttling_exception.ThrottlingException: <p>The request was denied due to request throttling.</p>
            capo_datazone.errors.unauthorized_exception.UnauthorizedException: <p>You do not have permission to perform this action.</p>
            capo_datazone.errors.conflict_exception.ConflictException: <p>There is a conflict while performing this action.</p>
            capo_datazone.errors.internal_server_exception.InternalServerException: <p>The request has failed because of an unknown error, exception or failure.</p>
            capo_datazone.errors.resource_not_found_exception.ResourceNotFoundException: <p>The specified resource cannot be found.</p>
            capo_datazone.errors.validation_exception.ValidationException: <p>The input fails to satisfy the constraints specified by the Amazon Web Services service.</p>
            capo_datazone.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        async def _handler(
            req: "AsyncOperationRequest[capo_datazone.types.put_environment_blueprint_configuration_input.PutEnvironmentBlueprintConfigurationInput]",
        ) -> AsyncOperationResponse[
            "capo_datazone.types.put_environment_blueprint_configuration_output.PutEnvironmentBlueprintConfigurationOutput"
        ]:
            import capo_datazone._operations.data_zone.put_environment_blueprint_configuration

            (
                output,
                http_response,
            ) = await capo_datazone._operations.data_zone.put_environment_blueprint_configuration.async_put_environment_blueprint_configuration(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_datazone.types.put_environment_blueprint_configuration_input.PutEnvironmentBlueprintConfigurationInput = {
            "domain_identifier": domain_identifier,
            "environment_blueprint_identifier": environment_blueprint_identifier,
            "enabled_regions": enabled_regions,
        }
        if provisioning_role_arn is not None:
            input_["provisioning_role_arn"] = provisioning_role_arn
        if manage_access_role_arn is not None:
            input_["manage_access_role_arn"] = manage_access_role_arn
        if environment_role_permission_boundary is not None:
            input_["environment_role_permission_boundary"] = (
                environment_role_permission_boundary
            )
        if regional_parameters is not None:
            input_["regional_parameters"] = regional_parameters
        if resource_configurations is not None:
            input_["resource_configurations"] = resource_configurations
        if allow_user_provided_configurations is not None:
            input_["allow_user_provided_configurations"] = (
                allow_user_provided_configurations
            )
        if global_parameters is not None:
            input_["global_parameters"] = global_parameters
        if provisioning_configurations is not None:
            input_["provisioning_configurations"] = provisioning_configurations

        response = await aexecute_pipeline(
            AsyncOperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        await response.response.aclose()
        return response.output

    async def get_environment_blueprint_configuration(
        self,
        domain_identifier: "capo_datazone.types.domain_id.DomainId",
        environment_blueprint_identifier: "capo_datazone.types.environment_blueprint_id.EnvironmentBlueprintId",
        *,
        config_overrides: Optional[AsyncDataZoneClientConfig] = None,
    ) -> "capo_datazone.types.get_environment_blueprint_configuration_output.GetEnvironmentBlueprintConfigurationOutput":
        """<p>Gets the blueprint configuration in Amazon DataZone.</p>

        Args:
            domain_identifier: <p>The ID of the Amazon DataZone domain where this blueprint exists.</p>
            environment_blueprint_identifier: <p>He ID of the blueprint.</p>

        Raises:
            capo_datazone.errors.access_denied_exception.AccessDeniedException: <p>You do not have sufficient access to perform this action.</p>
            capo_datazone.errors.throttling_exception.ThrottlingException: <p>The request was denied due to request throttling.</p>
            capo_datazone.errors.unauthorized_exception.UnauthorizedException: <p>You do not have permission to perform this action.</p>
            capo_datazone.errors.internal_server_exception.InternalServerException: <p>The request has failed because of an unknown error, exception or failure.</p>
            capo_datazone.errors.resource_not_found_exception.ResourceNotFoundException: <p>The specified resource cannot be found.</p>
            capo_datazone.errors.validation_exception.ValidationException: <p>The input fails to satisfy the constraints specified by the Amazon Web Services service.</p>
            capo_datazone.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        async def _handler(
            req: "AsyncOperationRequest[capo_datazone.types.get_environment_blueprint_configuration_input.GetEnvironmentBlueprintConfigurationInput]",
        ) -> AsyncOperationResponse[
            "capo_datazone.types.get_environment_blueprint_configuration_output.GetEnvironmentBlueprintConfigurationOutput"
        ]:
            import capo_datazone._operations.data_zone.get_environment_blueprint_configuration

            (
                output,
                http_response,
            ) = await capo_datazone._operations.data_zone.get_environment_blueprint_configuration.async_get_environment_blueprint_configuration(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_datazone.types.get_environment_blueprint_configuration_input.GetEnvironmentBlueprintConfigurationInput = {
            "domain_identifier": domain_identifier,
            "environment_blueprint_identifier": environment_blueprint_identifier,
        }

        response = await aexecute_pipeline(
            AsyncOperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        await response.response.aclose()
        return response.output

    async def delete_environment_blueprint_configuration(
        self,
        domain_identifier: "capo_datazone.types.domain_id.DomainId",
        environment_blueprint_identifier: "capo_datazone.types.environment_blueprint_id.EnvironmentBlueprintId",
        *,
        config_overrides: Optional[AsyncDataZoneClientConfig] = None,
    ) -> "capo_datazone.types.delete_environment_blueprint_configuration_output.DeleteEnvironmentBlueprintConfigurationOutput":
        """<p>Deletes the blueprint configuration in Amazon DataZone.</p>

        Args:
            domain_identifier: <p>The ID of the Amazon DataZone domain in which the blueprint configuration is deleted.</p>
            environment_blueprint_identifier: <p>The ID of the blueprint the configuration of which is deleted.</p>

        Raises:
            capo_datazone.errors.access_denied_exception.AccessDeniedException: <p>You do not have sufficient access to perform this action.</p>
            capo_datazone.errors.throttling_exception.ThrottlingException: <p>The request was denied due to request throttling.</p>
            capo_datazone.errors.unauthorized_exception.UnauthorizedException: <p>You do not have permission to perform this action.</p>
            capo_datazone.errors.internal_server_exception.InternalServerException: <p>The request has failed because of an unknown error, exception or failure.</p>
            capo_datazone.errors.validation_exception.ValidationException: <p>The input fails to satisfy the constraints specified by the Amazon Web Services service.</p>
            capo_datazone.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        async def _handler(
            req: "AsyncOperationRequest[capo_datazone.types.delete_environment_blueprint_configuration_input.DeleteEnvironmentBlueprintConfigurationInput]",
        ) -> AsyncOperationResponse[
            "capo_datazone.types.delete_environment_blueprint_configuration_output.DeleteEnvironmentBlueprintConfigurationOutput"
        ]:
            import capo_datazone._operations.data_zone.delete_environment_blueprint_configuration

            (
                output,
                http_response,
            ) = await capo_datazone._operations.data_zone.delete_environment_blueprint_configuration.async_delete_environment_blueprint_configuration(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_datazone.types.delete_environment_blueprint_configuration_input.DeleteEnvironmentBlueprintConfigurationInput = {
            "domain_identifier": domain_identifier,
            "environment_blueprint_identifier": environment_blueprint_identifier,
        }

        response = await aexecute_pipeline(
            AsyncOperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        await response.response.aclose()
        return response.output

    async def list_environment_blueprint_configurations(
        self,
        domain_identifier: "capo_datazone.types.domain_id.DomainId",
        *,
        config_overrides: Optional[AsyncDataZoneClientConfig] = None,
        max_results: Optional["capo_datazone.types.max_results.MaxResults"] = None,
        next_token: Optional[
            "capo_datazone.types.pagination_token.PaginationToken"
        ] = None,
    ) -> "capo_datazone.types.list_environment_blueprint_configurations_output.ListEnvironmentBlueprintConfigurationsOutput":
        """<p>Lists blueprint configurations for a Amazon DataZone environment.</p>

        Args:
            domain_identifier: <p>The identifier of the Amazon DataZone domain.</p>
            max_results: <p>The maximum number of blueprint configurations to return in a single call to <code>ListEnvironmentBlueprintConfigurations</code>. When the number of configurations to be listed is greater than the value of <code>MaxResults</code>, the response contains a <code>NextToken</code> value that you can use in a subsequent call to <code>ListEnvironmentBlueprintConfigurations</code> to list the next set of configurations.</p>
            next_token: <p>When the number of blueprint configurations is greater than the default value for the <code>MaxResults</code> parameter, or if you explicitly specify a value for <code>MaxResults</code> that is less than the number of configurations, the response includes a pagination token named <code>NextToken</code>. You can specify this <code>NextToken</code> value in a subsequent call to <code>ListEnvironmentBlueprintConfigurations</code> to list the next set of configurations.</p>

        Raises:
            capo_datazone.errors.access_denied_exception.AccessDeniedException: <p>You do not have sufficient access to perform this action.</p>
            capo_datazone.errors.throttling_exception.ThrottlingException: <p>The request was denied due to request throttling.</p>
            capo_datazone.errors.unauthorized_exception.UnauthorizedException: <p>You do not have permission to perform this action.</p>
            capo_datazone.errors.internal_server_exception.InternalServerException: <p>The request has failed because of an unknown error, exception or failure.</p>
            capo_datazone.errors.resource_not_found_exception.ResourceNotFoundException: <p>The specified resource cannot be found.</p>
            capo_datazone.errors.validation_exception.ValidationException: <p>The input fails to satisfy the constraints specified by the Amazon Web Services service.</p>
            capo_datazone.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        async def _handler(
            req: "AsyncOperationRequest[capo_datazone.types.list_environment_blueprint_configurations_input.ListEnvironmentBlueprintConfigurationsInput]",
        ) -> AsyncOperationResponse[
            "capo_datazone.types.list_environment_blueprint_configurations_output.ListEnvironmentBlueprintConfigurationsOutput"
        ]:
            import capo_datazone._operations.data_zone.list_environment_blueprint_configurations

            (
                output,
                http_response,
            ) = await capo_datazone._operations.data_zone.list_environment_blueprint_configurations.async_list_environment_blueprint_configurations(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_datazone.types.list_environment_blueprint_configurations_input.ListEnvironmentBlueprintConfigurationsInput = {
            "domain_identifier": domain_identifier
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

    async def iter_list_environment_blueprint_configurations(
        self,
        domain_identifier: "capo_datazone.types.domain_id.DomainId",
        *,
        config_overrides: Optional[AsyncDataZoneClientConfig] = None,
        max_results: Optional["capo_datazone.types.max_results.MaxResults"] = None,
        next_token: Optional[
            "capo_datazone.types.pagination_token.PaginationToken"
        ] = None,
    ) -> "AsyncIterator[capo_datazone.types.environment_blueprint_configuration_item.EnvironmentBlueprintConfigurationItem]":
        _token = next_token
        while True:
            _response = await self.list_environment_blueprint_configurations(
                domain_identifier,
                config_overrides=config_overrides,
                max_results=max_results,
                next_token=_token,
            )
            _page = _resolve_path(_response, ("items",))
            for _item in _page or []:
                yield _item
            _token = _resolve_path(_response, ("next_token",))
            if not _token:
                break

    async def create_form_type(
        self,
        domain_identifier: "capo_datazone.types.domain_id.DomainId",
        name: "capo_datazone.types.form_type_name.FormTypeName",
        model: "capo_datazone.types.model.Model",
        owning_project_identifier: "capo_datazone.types.project_id.ProjectId",
        *,
        config_overrides: Optional[AsyncDataZoneClientConfig] = None,
        status: Optional["capo_datazone.types.form_type_status.FormTypeStatus"] = None,
        description: Optional["capo_datazone.types.description.Description"] = None,
    ) -> "capo_datazone.types.create_form_type_output.CreateFormTypeOutput":
        """<p>Creates a metadata form type.</p> <p>Prerequisites:</p> <ul> <li> <p>The domain must exist and be in an <code>ENABLED</code> state. </p> </li> <li> <p>The owning project must exist and be accessible.</p> </li> <li> <p>The name must be unique within the domain.</p> </li> </ul> <p>For custom form types, to indicate that a field should be searchable, annotate it with <code>@amazon.datazone#searchable</code>. By default, searchable fields are indexed for semantic search, where related query terms will match the attribute value even if they are not stemmed or keyword matches. To indicate that a field should be indexed for lexical search (which disables semantic search but supports stemmed and partial matches), annotate it with <code>@amazon.datazone#searchable(modes:["LEXICAL"])</code>. To indicate that a field should be indexed for technical identifier search (for more information on technical identifier search, see: <a href="https://aws.amazon.com/blogs/big-data/streamline-data-discovery-with-precise-technical-identifier-search-in-amazon-sagemaker-unified-studio/">https://aws.amazon.com/blogs/big-data/streamline-data-discovery-with-precise-technical-identifier-search-in-amazon-sagemaker-unified-studio/</a>), annotate it with <code>@amazon.datazone#searchable(modes:["TECHNICAL"])</code>.</p> <p>To denote that a field will store glossary term ids (which are filterable via the Search/SearchListings APIs), annotate it with <code>@amazon.datazone#glossaryterm("${GLOSSARY_ID}")</code>, where <code>${GLOSSARY_ID}</code> is the id of the glossary that the glossary terms stored in the field belong to. </p>

        Args:
            domain_identifier: <p>The ID of the Amazon DataZone domain in which this metadata form type is created.</p>
            name: <p>The name of this Amazon DataZone metadata form type.</p>
            model: <p>The model of this Amazon DataZone metadata form type.</p>
            owning_project_identifier: <p>The ID of the Amazon DataZone project that owns this metadata form type.</p>
            status: <p>The status of this Amazon DataZone metadata form type.</p>
            description: <p>The description of this Amazon DataZone metadata form type.</p>

        Raises:
            capo_datazone.errors.access_denied_exception.AccessDeniedException: <p>You do not have sufficient access to perform this action.</p>
            capo_datazone.errors.throttling_exception.ThrottlingException: <p>The request was denied due to request throttling.</p>
            capo_datazone.errors.unauthorized_exception.UnauthorizedException: <p>You do not have permission to perform this action.</p>
            capo_datazone.errors.conflict_exception.ConflictException: <p>There is a conflict while performing this action.</p>
            capo_datazone.errors.internal_server_exception.InternalServerException: <p>The request has failed because of an unknown error, exception or failure.</p>
            capo_datazone.errors.service_quota_exceeded_exception.ServiceQuotaExceededException: <p>The request has exceeded the specified service quota.</p>
            capo_datazone.errors.validation_exception.ValidationException: <p>The input fails to satisfy the constraints specified by the Amazon Web Services service.</p>
            capo_datazone.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        async def _handler(
            req: "AsyncOperationRequest[capo_datazone.types.create_form_type_input.CreateFormTypeInput]",
        ) -> AsyncOperationResponse[
            "capo_datazone.types.create_form_type_output.CreateFormTypeOutput"
        ]:
            import capo_datazone._operations.data_zone.create_form_type

            (
                output,
                http_response,
            ) = await capo_datazone._operations.data_zone.create_form_type.async_create_form_type(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_datazone.types.create_form_type_input.CreateFormTypeInput = {
            "domain_identifier": domain_identifier,
            "name": name,
            "model": model,
            "owning_project_identifier": owning_project_identifier,
        }
        if status is not None:
            input_["status"] = status
        if description is not None:
            input_["description"] = description

        response = await aexecute_pipeline(
            AsyncOperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        await response.response.aclose()
        return response.output

    async def delete_form_type(
        self,
        domain_identifier: "capo_datazone.types.domain_id.DomainId",
        form_type_identifier: "capo_datazone.types.form_type_identifier.FormTypeIdentifier",
        *,
        config_overrides: Optional[AsyncDataZoneClientConfig] = None,
    ) -> "capo_datazone.types.delete_form_type_output.DeleteFormTypeOutput":
        """<p>Deletes and metadata form type in Amazon DataZone.</p> <p>Prerequisites:</p> <ul> <li> <p>The form type must exist in the domain. </p> </li> <li> <p>The form type must not be in use by any asset types or assets.</p> </li> <li> <p>The domain must be valid and accessible.</p> </li> <li> <p>User must have delete permissions on the form type.</p> </li> <li> <p>Any dependencies (such as linked asset types) must be removed first.</p> </li> </ul>

        Args:
            domain_identifier: <p>The ID of the Amazon DataZone domain in which the metadata form type is deleted.</p>
            form_type_identifier: <p>The ID of the metadata form type that is deleted.</p>

        Raises:
            capo_datazone.errors.access_denied_exception.AccessDeniedException: <p>You do not have sufficient access to perform this action.</p>
            capo_datazone.errors.throttling_exception.ThrottlingException: <p>The request was denied due to request throttling.</p>
            capo_datazone.errors.unauthorized_exception.UnauthorizedException: <p>You do not have permission to perform this action.</p>
            capo_datazone.errors.conflict_exception.ConflictException: <p>There is a conflict while performing this action.</p>
            capo_datazone.errors.internal_server_exception.InternalServerException: <p>The request has failed because of an unknown error, exception or failure.</p>
            capo_datazone.errors.resource_not_found_exception.ResourceNotFoundException: <p>The specified resource cannot be found.</p>
            capo_datazone.errors.validation_exception.ValidationException: <p>The input fails to satisfy the constraints specified by the Amazon Web Services service.</p>
            capo_datazone.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        async def _handler(
            req: "AsyncOperationRequest[capo_datazone.types.delete_form_type_input.DeleteFormTypeInput]",
        ) -> AsyncOperationResponse[
            "capo_datazone.types.delete_form_type_output.DeleteFormTypeOutput"
        ]:
            import capo_datazone._operations.data_zone.delete_form_type

            (
                output,
                http_response,
            ) = await capo_datazone._operations.data_zone.delete_form_type.async_delete_form_type(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_datazone.types.delete_form_type_input.DeleteFormTypeInput = {
            "domain_identifier": domain_identifier,
            "form_type_identifier": form_type_identifier,
        }

        response = await aexecute_pipeline(
            AsyncOperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        await response.response.aclose()
        return response.output

    async def get_form_type(
        self,
        domain_identifier: "capo_datazone.types.domain_id.DomainId",
        form_type_identifier: "capo_datazone.types.form_type_identifier.FormTypeIdentifier",
        *,
        config_overrides: Optional[AsyncDataZoneClientConfig] = None,
        revision: Optional["capo_datazone.types.revision.Revision"] = None,
    ) -> "capo_datazone.types.get_form_type_output.GetFormTypeOutput":
        """<p>Gets a metadata form type in Amazon DataZone.</p> <p>Form types define the structure and validation rules for collecting metadata about assets in Amazon DataZone. They act as templates that ensure consistent metadata capture across similar types of assets, while allowing for customization to meet specific organizational needs. Form types can include required fields, validation rules, and dependencies, helping maintain high-quality metadata that makes data assets more discoverable and usable.</p> <ul> <li> <p>The form type with the specified identifier must exist in the given domain. </p> </li> <li> <p>The domain must be valid and active.</p> </li> <li> <p>User must have permission on the form type.</p> </li> <li> <p>The form type should not be deleted or in an invalid state.</p> </li> </ul> <p>One use case for this API is to determine whether a form field is indexed for search. </p> <p>A searchable field will be annotated with <code>@amazon.datazone#searchable</code>. By default, searchable fields are indexed for semantic search, where related query terms will match the attribute value even if they are not stemmed or keyword matches. If a field is indexed technical identifier search, it will be annotated with <code>@amazon.datazone#searchable(modes:["TECHNICAL"])</code>. If a field is indexed for lexical search (supports stemmed and prefix matches but not semantic matches), it will be annotated with <code>@amazon.datazone#searchable(modes:["LEXICAL"])</code>.</p> <p>A field storing glossary term IDs (which is filterable) will be annotated with <code>@amazon.datazone#glossaryterm("${glossaryId}")</code>. </p>

        Args:
            domain_identifier: <p>The ID of the Amazon DataZone domain in which this metadata form type exists.</p>
            form_type_identifier: <p>The ID of the metadata form type.</p>
            revision: <p>The revision of this metadata form type.</p>

        Raises:
            capo_datazone.errors.access_denied_exception.AccessDeniedException: <p>You do not have sufficient access to perform this action.</p>
            capo_datazone.errors.throttling_exception.ThrottlingException: <p>The request was denied due to request throttling.</p>
            capo_datazone.errors.unauthorized_exception.UnauthorizedException: <p>You do not have permission to perform this action.</p>
            capo_datazone.errors.internal_server_exception.InternalServerException: <p>The request has failed because of an unknown error, exception or failure.</p>
            capo_datazone.errors.resource_not_found_exception.ResourceNotFoundException: <p>The specified resource cannot be found.</p>
            capo_datazone.errors.validation_exception.ValidationException: <p>The input fails to satisfy the constraints specified by the Amazon Web Services service.</p>
            capo_datazone.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        async def _handler(
            req: "AsyncOperationRequest[capo_datazone.types.get_form_type_input.GetFormTypeInput]",
        ) -> AsyncOperationResponse[
            "capo_datazone.types.get_form_type_output.GetFormTypeOutput"
        ]:
            import capo_datazone._operations.data_zone.get_form_type

            (
                output,
                http_response,
            ) = await capo_datazone._operations.data_zone.get_form_type.async_get_form_type(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_datazone.types.get_form_type_input.GetFormTypeInput = {
            "domain_identifier": domain_identifier,
            "form_type_identifier": form_type_identifier,
        }
        if revision is not None:
            input_["revision"] = revision

        response = await aexecute_pipeline(
            AsyncOperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        await response.response.aclose()
        return response.output

    async def create_glossary(
        self,
        domain_identifier: "capo_datazone.types.domain_id.DomainId",
        name: "capo_datazone.types.glossary_name.GlossaryName",
        owning_project_identifier: "capo_datazone.types.project_id.ProjectId",
        *,
        config_overrides: Optional[AsyncDataZoneClientConfig] = None,
        description: Optional[
            "capo_datazone.types.glossary_description.GlossaryDescription"
        ] = None,
        status: Optional["capo_datazone.types.glossary_status.GlossaryStatus"] = None,
        usage_restrictions: Optional[
            "capo_datazone.types.glossary_usage_restrictions.GlossaryUsageRestrictions"
        ] = None,
        client_token: Optional["capo_datazone.types.client_token.ClientToken"] = None,
    ) -> "capo_datazone.types.create_glossary_output.CreateGlossaryOutput":
        """<p>Creates an Amazon DataZone business glossary.</p> <p>Specifies that this is a create glossary policy.</p> <p>A glossary serves as the central repository for business terminology and definitions within an organization. It helps establish and maintain a common language across different departments and teams, reducing miscommunication and ensuring consistent interpretation of business concepts. Glossaries can include hierarchical relationships between terms, cross-references, and links to actual data assets, making them invaluable for both business users and technical teams trying to understand and use data correctly.</p> <p>Prerequisites:</p> <ul> <li> <p>Domain must exist and be in an active state. </p> </li> <li> <p>Owning project must exist and be accessible by the caller.</p> </li> <li> <p>The glossary name must be unique within the domain.</p> </li> </ul>

        Args:
            domain_identifier: <p>The ID of the Amazon DataZone domain in which this business glossary is created.</p>
            name: <p>The name of this business glossary.</p>
            owning_project_identifier: <p>The ID of the project that currently owns business glossary.</p>
            description: <p>The description of this business glossary.</p>
            status: <p>The status of this business glossary.</p>
            usage_restrictions: <p>The usage restriction of the restricted glossary.</p>
            client_token: <p>A unique, case-sensitive identifier that is provided to ensure the idempotency of the request.</p>

        Raises:
            capo_datazone.errors.access_denied_exception.AccessDeniedException: <p>You do not have sufficient access to perform this action.</p>
            capo_datazone.errors.throttling_exception.ThrottlingException: <p>The request was denied due to request throttling.</p>
            capo_datazone.errors.unauthorized_exception.UnauthorizedException: <p>You do not have permission to perform this action.</p>
            capo_datazone.errors.conflict_exception.ConflictException: <p>There is a conflict while performing this action.</p>
            capo_datazone.errors.internal_server_exception.InternalServerException: <p>The request has failed because of an unknown error, exception or failure.</p>
            capo_datazone.errors.service_quota_exceeded_exception.ServiceQuotaExceededException: <p>The request has exceeded the specified service quota.</p>
            capo_datazone.errors.validation_exception.ValidationException: <p>The input fails to satisfy the constraints specified by the Amazon Web Services service.</p>
            capo_datazone.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        async def _handler(
            req: "AsyncOperationRequest[capo_datazone.types.create_glossary_input.CreateGlossaryInput]",
        ) -> AsyncOperationResponse[
            "capo_datazone.types.create_glossary_output.CreateGlossaryOutput"
        ]:
            import capo_datazone._operations.data_zone.create_glossary

            (
                output,
                http_response,
            ) = await capo_datazone._operations.data_zone.create_glossary.async_create_glossary(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_datazone.types.create_glossary_input.CreateGlossaryInput = {
            "domain_identifier": domain_identifier,
            "name": name,
            "owning_project_identifier": owning_project_identifier,
        }
        if description is not None:
            input_["description"] = description
        if status is not None:
            input_["status"] = status
        if usage_restrictions is not None:
            input_["usage_restrictions"] = usage_restrictions
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

    async def get_glossary(
        self,
        domain_identifier: "capo_datazone.types.domain_id.DomainId",
        identifier: "capo_datazone.types.glossary_id.GlossaryId",
        *,
        config_overrides: Optional[AsyncDataZoneClientConfig] = None,
    ) -> "capo_datazone.types.get_glossary_output.GetGlossaryOutput":
        """<p>Gets a business glossary in Amazon DataZone.</p> <p>Prerequisites:</p> <ul> <li> <p>The specified glossary ID must exist and be associated with the given domain. </p> </li> <li> <p>The caller must have the <code>datazone:GetGlossary</code> permission on the domain.</p> </li> </ul>

        Args:
            domain_identifier: <p>The ID of the Amazon DataZone domain in which this business glossary exists.</p>
            identifier: <p>The ID of the business glossary.</p>

        Raises:
            capo_datazone.errors.access_denied_exception.AccessDeniedException: <p>You do not have sufficient access to perform this action.</p>
            capo_datazone.errors.throttling_exception.ThrottlingException: <p>The request was denied due to request throttling.</p>
            capo_datazone.errors.unauthorized_exception.UnauthorizedException: <p>You do not have permission to perform this action.</p>
            capo_datazone.errors.internal_server_exception.InternalServerException: <p>The request has failed because of an unknown error, exception or failure.</p>
            capo_datazone.errors.resource_not_found_exception.ResourceNotFoundException: <p>The specified resource cannot be found.</p>
            capo_datazone.errors.validation_exception.ValidationException: <p>The input fails to satisfy the constraints specified by the Amazon Web Services service.</p>
            capo_datazone.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        async def _handler(
            req: "AsyncOperationRequest[capo_datazone.types.get_glossary_input.GetGlossaryInput]",
        ) -> AsyncOperationResponse[
            "capo_datazone.types.get_glossary_output.GetGlossaryOutput"
        ]:
            import capo_datazone._operations.data_zone.get_glossary

            (
                output,
                http_response,
            ) = await capo_datazone._operations.data_zone.get_glossary.async_get_glossary(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_datazone.types.get_glossary_input.GetGlossaryInput = {
            "domain_identifier": domain_identifier,
            "identifier": identifier,
        }

        response = await aexecute_pipeline(
            AsyncOperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        await response.response.aclose()
        return response.output

    async def update_glossary(
        self,
        domain_identifier: "capo_datazone.types.domain_id.DomainId",
        identifier: "capo_datazone.types.glossary_id.GlossaryId",
        *,
        config_overrides: Optional[AsyncDataZoneClientConfig] = None,
        name: Optional["capo_datazone.types.glossary_name.GlossaryName"] = None,
        description: Optional[
            "capo_datazone.types.glossary_description.GlossaryDescription"
        ] = None,
        status: Optional["capo_datazone.types.glossary_status.GlossaryStatus"] = None,
        client_token: Optional["capo_datazone.types.client_token.ClientToken"] = None,
    ) -> "capo_datazone.types.update_glossary_output.UpdateGlossaryOutput":
        """<p>Updates the business glossary in Amazon DataZone.</p> <p>Prerequisites:</p> <ul> <li> <p>The glossary must exist in the given domain. </p> </li> <li> <p>The caller must have the <code>datazone:UpdateGlossary</code> permission to update it.</p> </li> <li> <p>When updating the name, the new name must be unique within the domain.</p> </li> <li> <p>The glossary must not be deleted or in a terminal state.</p> </li> </ul>

        Args:
            domain_identifier: <p>The identifier of the Amazon DataZone domain in which a business glossary is to be updated.</p>
            identifier: <p>The identifier of the business glossary to be updated.</p>
            name: <p>The name to be updated as part of the <code>UpdateGlossary</code> action.</p>
            description: <p>The description to be updated as part of the <code>UpdateGlossary</code> action.</p>
            status: <p>The status to be updated as part of the <code>UpdateGlossary</code> action.</p>
            client_token: <p>A unique, case-sensitive identifier that is provided to ensure the idempotency of the request.</p>

        Raises:
            capo_datazone.errors.access_denied_exception.AccessDeniedException: <p>You do not have sufficient access to perform this action.</p>
            capo_datazone.errors.throttling_exception.ThrottlingException: <p>The request was denied due to request throttling.</p>
            capo_datazone.errors.unauthorized_exception.UnauthorizedException: <p>You do not have permission to perform this action.</p>
            capo_datazone.errors.conflict_exception.ConflictException: <p>There is a conflict while performing this action.</p>
            capo_datazone.errors.internal_server_exception.InternalServerException: <p>The request has failed because of an unknown error, exception or failure.</p>
            capo_datazone.errors.resource_not_found_exception.ResourceNotFoundException: <p>The specified resource cannot be found.</p>
            capo_datazone.errors.validation_exception.ValidationException: <p>The input fails to satisfy the constraints specified by the Amazon Web Services service.</p>
            capo_datazone.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        async def _handler(
            req: "AsyncOperationRequest[capo_datazone.types.update_glossary_input.UpdateGlossaryInput]",
        ) -> AsyncOperationResponse[
            "capo_datazone.types.update_glossary_output.UpdateGlossaryOutput"
        ]:
            import capo_datazone._operations.data_zone.update_glossary

            (
                output,
                http_response,
            ) = await capo_datazone._operations.data_zone.update_glossary.async_update_glossary(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_datazone.types.update_glossary_input.UpdateGlossaryInput = {
            "domain_identifier": domain_identifier,
            "identifier": identifier,
        }
        if name is not None:
            input_["name"] = name
        if description is not None:
            input_["description"] = description
        if status is not None:
            input_["status"] = status
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

    async def delete_glossary(
        self,
        domain_identifier: "capo_datazone.types.domain_id.DomainId",
        identifier: "capo_datazone.types.glossary_id.GlossaryId",
        *,
        config_overrides: Optional[AsyncDataZoneClientConfig] = None,
    ) -> "capo_datazone.types.delete_glossary_output.DeleteGlossaryOutput":
        """<p>Deletes a business glossary in Amazon DataZone.</p> <p>Prerequisites:</p> <ul> <li> <p>The glossary must be in DISABLED state. </p> </li> <li> <p>The glossary must not have any glossary terms associated with it.</p> </li> <li> <p>The glossary must exist in the specified domain.</p> </li> <li> <p>The caller must have the <code>datazone:DeleteGlossary</code> permission in the domain and glossary.</p> </li> <li> <p>Glossary should not be linked to any active metadata forms.</p> </li> </ul>

        Args:
            domain_identifier: <p>The ID of the Amazon DataZone domain in which the business glossary is deleted.</p>
            identifier: <p>The ID of the business glossary that is deleted.</p>

        Raises:
            capo_datazone.errors.access_denied_exception.AccessDeniedException: <p>You do not have sufficient access to perform this action.</p>
            capo_datazone.errors.throttling_exception.ThrottlingException: <p>The request was denied due to request throttling.</p>
            capo_datazone.errors.unauthorized_exception.UnauthorizedException: <p>You do not have permission to perform this action.</p>
            capo_datazone.errors.conflict_exception.ConflictException: <p>There is a conflict while performing this action.</p>
            capo_datazone.errors.internal_server_exception.InternalServerException: <p>The request has failed because of an unknown error, exception or failure.</p>
            capo_datazone.errors.resource_not_found_exception.ResourceNotFoundException: <p>The specified resource cannot be found.</p>
            capo_datazone.errors.validation_exception.ValidationException: <p>The input fails to satisfy the constraints specified by the Amazon Web Services service.</p>
            capo_datazone.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        async def _handler(
            req: "AsyncOperationRequest[capo_datazone.types.delete_glossary_input.DeleteGlossaryInput]",
        ) -> AsyncOperationResponse[
            "capo_datazone.types.delete_glossary_output.DeleteGlossaryOutput"
        ]:
            import capo_datazone._operations.data_zone.delete_glossary

            (
                output,
                http_response,
            ) = await capo_datazone._operations.data_zone.delete_glossary.async_delete_glossary(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_datazone.types.delete_glossary_input.DeleteGlossaryInput = {
            "domain_identifier": domain_identifier,
            "identifier": identifier,
        }

        response = await aexecute_pipeline(
            AsyncOperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        await response.response.aclose()
        return response.output

    async def create_glossary_term(
        self,
        domain_identifier: "capo_datazone.types.domain_id.DomainId",
        glossary_identifier: "capo_datazone.types.glossary_term_id.GlossaryTermId",
        name: "capo_datazone.types.glossary_term_name.GlossaryTermName",
        *,
        config_overrides: Optional[AsyncDataZoneClientConfig] = None,
        status: Optional[
            "capo_datazone.types.glossary_term_status.GlossaryTermStatus"
        ] = None,
        short_description: Optional[
            "capo_datazone.types.short_description.ShortDescription"
        ] = None,
        long_description: Optional[
            "capo_datazone.types.long_description.LongDescription"
        ] = None,
        term_relations: Optional[
            "capo_datazone.types.term_relations.TermRelations"
        ] = None,
        client_token: Optional["capo_datazone.types.client_token.ClientToken"] = None,
    ) -> "capo_datazone.types.create_glossary_term_output.CreateGlossaryTermOutput":
        """<p>Creates a business glossary term.</p> <p>A glossary term represents an individual entry within the Amazon DataZone glossary, serving as a standardized definition for a specific business concept or data element. Each term can include rich metadata such as detailed definitions, synonyms, related terms, and usage examples. Glossary terms can be linked directly to data assets, providing business context to technical data elements. This linking capability helps users understand the business meaning of data fields and ensures consistent interpretation across different systems and teams. Terms can also have relationships with other terms, creating a semantic network that reflects the complexity of business concepts.</p> <p>Prerequisites:</p> <ul> <li> <p>Domain must exist. </p> </li> <li> <p>Glossary must exist.</p> </li> <li> <p>The term name must be unique within the glossary.</p> </li> <li> <p>Ensure term does not conflict with existing terms in hierarchy.</p> </li> </ul>

        Args:
            domain_identifier: <p>The ID of the Amazon DataZone domain in which this business glossary term is created.</p>
            glossary_identifier: <p>The ID of the business glossary in which this term is created.</p>
            name: <p>The name of this business glossary term.</p>
            status: <p>The status of this business glossary term.</p>
            short_description: <p>The short description of this business glossary term.</p>
            long_description: <p>The long description of this business glossary term.</p>
            term_relations: <p>The term relations of this business glossary term.</p>
            client_token: <p>A unique, case-sensitive identifier that is provided to ensure the idempotency of the request.</p>

        Raises:
            capo_datazone.errors.access_denied_exception.AccessDeniedException: <p>You do not have sufficient access to perform this action.</p>
            capo_datazone.errors.throttling_exception.ThrottlingException: <p>The request was denied due to request throttling.</p>
            capo_datazone.errors.unauthorized_exception.UnauthorizedException: <p>You do not have permission to perform this action.</p>
            capo_datazone.errors.conflict_exception.ConflictException: <p>There is a conflict while performing this action.</p>
            capo_datazone.errors.internal_server_exception.InternalServerException: <p>The request has failed because of an unknown error, exception or failure.</p>
            capo_datazone.errors.resource_not_found_exception.ResourceNotFoundException: <p>The specified resource cannot be found.</p>
            capo_datazone.errors.service_quota_exceeded_exception.ServiceQuotaExceededException: <p>The request has exceeded the specified service quota.</p>
            capo_datazone.errors.validation_exception.ValidationException: <p>The input fails to satisfy the constraints specified by the Amazon Web Services service.</p>
            capo_datazone.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        async def _handler(
            req: "AsyncOperationRequest[capo_datazone.types.create_glossary_term_input.CreateGlossaryTermInput]",
        ) -> AsyncOperationResponse[
            "capo_datazone.types.create_glossary_term_output.CreateGlossaryTermOutput"
        ]:
            import capo_datazone._operations.data_zone.create_glossary_term

            (
                output,
                http_response,
            ) = await capo_datazone._operations.data_zone.create_glossary_term.async_create_glossary_term(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_datazone.types.create_glossary_term_input.CreateGlossaryTermInput = {
            "domain_identifier": domain_identifier,
            "glossary_identifier": glossary_identifier,
            "name": name,
        }
        if status is not None:
            input_["status"] = status
        if short_description is not None:
            input_["short_description"] = short_description
        if long_description is not None:
            input_["long_description"] = long_description
        if term_relations is not None:
            input_["term_relations"] = term_relations
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

    async def get_glossary_term(
        self,
        domain_identifier: "capo_datazone.types.domain_id.DomainId",
        identifier: "capo_datazone.types.glossary_term_id.GlossaryTermId",
        *,
        config_overrides: Optional[AsyncDataZoneClientConfig] = None,
    ) -> "capo_datazone.types.get_glossary_term_output.GetGlossaryTermOutput":
        """<p>Gets a business glossary term in Amazon DataZone.</p> <p>Prerequisites:</p> <ul> <li> <p>Glossary term with identifier must exist in the domain. </p> </li> <li> <p>User must have permission on the glossary term.</p> </li> <li> <p>Domain must be accessible and active.</p> </li> </ul>

        Args:
            domain_identifier: <p>The ID of the Amazon DataZone domain in which this business glossary term exists.</p>
            identifier: <p>The ID of the business glossary term.</p>

        Raises:
            capo_datazone.errors.access_denied_exception.AccessDeniedException: <p>You do not have sufficient access to perform this action.</p>
            capo_datazone.errors.throttling_exception.ThrottlingException: <p>The request was denied due to request throttling.</p>
            capo_datazone.errors.unauthorized_exception.UnauthorizedException: <p>You do not have permission to perform this action.</p>
            capo_datazone.errors.internal_server_exception.InternalServerException: <p>The request has failed because of an unknown error, exception or failure.</p>
            capo_datazone.errors.resource_not_found_exception.ResourceNotFoundException: <p>The specified resource cannot be found.</p>
            capo_datazone.errors.validation_exception.ValidationException: <p>The input fails to satisfy the constraints specified by the Amazon Web Services service.</p>
            capo_datazone.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        async def _handler(
            req: "AsyncOperationRequest[capo_datazone.types.get_glossary_term_input.GetGlossaryTermInput]",
        ) -> AsyncOperationResponse[
            "capo_datazone.types.get_glossary_term_output.GetGlossaryTermOutput"
        ]:
            import capo_datazone._operations.data_zone.get_glossary_term

            (
                output,
                http_response,
            ) = await capo_datazone._operations.data_zone.get_glossary_term.async_get_glossary_term(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_datazone.types.get_glossary_term_input.GetGlossaryTermInput = {
            "domain_identifier": domain_identifier,
            "identifier": identifier,
        }

        response = await aexecute_pipeline(
            AsyncOperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        await response.response.aclose()
        return response.output

    async def update_glossary_term(
        self,
        domain_identifier: "capo_datazone.types.domain_id.DomainId",
        identifier: "capo_datazone.types.glossary_term_id.GlossaryTermId",
        *,
        config_overrides: Optional[AsyncDataZoneClientConfig] = None,
        glossary_identifier: Optional[
            "capo_datazone.types.glossary_term_id.GlossaryTermId"
        ] = None,
        name: Optional[
            "capo_datazone.types.glossary_term_name.GlossaryTermName"
        ] = None,
        short_description: Optional[
            "capo_datazone.types.short_description.ShortDescription"
        ] = None,
        long_description: Optional[
            "capo_datazone.types.long_description.LongDescription"
        ] = None,
        term_relations: Optional[
            "capo_datazone.types.term_relations.TermRelations"
        ] = None,
        status: Optional[
            "capo_datazone.types.glossary_term_status.GlossaryTermStatus"
        ] = None,
    ) -> "capo_datazone.types.update_glossary_term_output.UpdateGlossaryTermOutput":
        """<p>Updates a business glossary term in Amazon DataZone.</p> <p>Prerequisites:</p> <ul> <li> <p>Glossary term must exist in the specified domain. </p> </li> <li> <p>New name must not conflict with existing terms in the same glossary.</p> </li> <li> <p>User must have permissions on the term.</p> </li> <li> <p>The term must not be in DELETED status.</p> </li> </ul>

        Args:
            domain_identifier: <p>The identifier of the Amazon DataZone domain in which a business glossary term is to be updated.</p>
            glossary_identifier: <p>The identifier of the business glossary in which a term is to be updated.</p>
            identifier: <p>The identifier of the business glossary term that is to be updated.</p>
            name: <p>The name to be updated as part of the <code>UpdateGlossaryTerm</code> action.</p>
            short_description: <p>The short description to be updated as part of the <code>UpdateGlossaryTerm</code> action.</p>
            long_description: <p>The long description to be updated as part of the <code>UpdateGlossaryTerm</code> action.</p>
            term_relations: <p>The term relations to be updated as part of the <code>UpdateGlossaryTerm</code> action.</p>
            status: <p>The status to be updated as part of the <code>UpdateGlossaryTerm</code> action.</p>

        Raises:
            capo_datazone.errors.access_denied_exception.AccessDeniedException: <p>You do not have sufficient access to perform this action.</p>
            capo_datazone.errors.throttling_exception.ThrottlingException: <p>The request was denied due to request throttling.</p>
            capo_datazone.errors.unauthorized_exception.UnauthorizedException: <p>You do not have permission to perform this action.</p>
            capo_datazone.errors.conflict_exception.ConflictException: <p>There is a conflict while performing this action.</p>
            capo_datazone.errors.internal_server_exception.InternalServerException: <p>The request has failed because of an unknown error, exception or failure.</p>
            capo_datazone.errors.resource_not_found_exception.ResourceNotFoundException: <p>The specified resource cannot be found.</p>
            capo_datazone.errors.validation_exception.ValidationException: <p>The input fails to satisfy the constraints specified by the Amazon Web Services service.</p>
            capo_datazone.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        async def _handler(
            req: "AsyncOperationRequest[capo_datazone.types.update_glossary_term_input.UpdateGlossaryTermInput]",
        ) -> AsyncOperationResponse[
            "capo_datazone.types.update_glossary_term_output.UpdateGlossaryTermOutput"
        ]:
            import capo_datazone._operations.data_zone.update_glossary_term

            (
                output,
                http_response,
            ) = await capo_datazone._operations.data_zone.update_glossary_term.async_update_glossary_term(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_datazone.types.update_glossary_term_input.UpdateGlossaryTermInput = {
            "domain_identifier": domain_identifier,
            "identifier": identifier,
        }
        if glossary_identifier is not None:
            input_["glossary_identifier"] = glossary_identifier
        if name is not None:
            input_["name"] = name
        if short_description is not None:
            input_["short_description"] = short_description
        if long_description is not None:
            input_["long_description"] = long_description
        if term_relations is not None:
            input_["term_relations"] = term_relations
        if status is not None:
            input_["status"] = status

        response = await aexecute_pipeline(
            AsyncOperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        await response.response.aclose()
        return response.output

    async def delete_glossary_term(
        self,
        domain_identifier: "capo_datazone.types.domain_id.DomainId",
        identifier: "capo_datazone.types.glossary_term_id.GlossaryTermId",
        *,
        config_overrides: Optional[AsyncDataZoneClientConfig] = None,
    ) -> "capo_datazone.types.delete_glossary_term_output.DeleteGlossaryTermOutput":
        """<p>Deletes a business glossary term in Amazon DataZone.</p> <p>Prerequisites:</p> <ul> <li> <p>Glossary term must exist and be active. </p> </li> <li> <p>The term must not be linked to other assets or child terms.</p> </li> <li> <p>Caller must have delete permissions in the domain/glossary.</p> </li> <li> <p>Ensure all associations (such as to assets or parent terms) are removed before deletion.</p> </li> </ul>

        Args:
            domain_identifier: <p>The ID of the Amazon DataZone domain in which the business glossary term is deleted.</p>
            identifier: <p>The ID of the business glossary term that is deleted.</p>

        Raises:
            capo_datazone.errors.access_denied_exception.AccessDeniedException: <p>You do not have sufficient access to perform this action.</p>
            capo_datazone.errors.throttling_exception.ThrottlingException: <p>The request was denied due to request throttling.</p>
            capo_datazone.errors.unauthorized_exception.UnauthorizedException: <p>You do not have permission to perform this action.</p>
            capo_datazone.errors.conflict_exception.ConflictException: <p>There is a conflict while performing this action.</p>
            capo_datazone.errors.internal_server_exception.InternalServerException: <p>The request has failed because of an unknown error, exception or failure.</p>
            capo_datazone.errors.resource_not_found_exception.ResourceNotFoundException: <p>The specified resource cannot be found.</p>
            capo_datazone.errors.validation_exception.ValidationException: <p>The input fails to satisfy the constraints specified by the Amazon Web Services service.</p>
            capo_datazone.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        async def _handler(
            req: "AsyncOperationRequest[capo_datazone.types.delete_glossary_term_input.DeleteGlossaryTermInput]",
        ) -> AsyncOperationResponse[
            "capo_datazone.types.delete_glossary_term_output.DeleteGlossaryTermOutput"
        ]:
            import capo_datazone._operations.data_zone.delete_glossary_term

            (
                output,
                http_response,
            ) = await capo_datazone._operations.data_zone.delete_glossary_term.async_delete_glossary_term(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_datazone.types.delete_glossary_term_input.DeleteGlossaryTermInput = {
            "domain_identifier": domain_identifier,
            "identifier": identifier,
        }

        response = await aexecute_pipeline(
            AsyncOperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        await response.response.aclose()
        return response.output

    async def get_listing(
        self,
        domain_identifier: "capo_datazone.types.domain_id.DomainId",
        identifier: "capo_datazone.types.listing_id.ListingId",
        *,
        config_overrides: Optional[AsyncDataZoneClientConfig] = None,
        listing_revision: Optional["capo_datazone.types.revision.Revision"] = None,
    ) -> "capo_datazone.types.get_listing_output.GetListingOutput":
        """<p>Gets a listing (a record of an asset at a given time). If you specify a listing version, only details that are specific to that version are returned.</p>

        Args:
            domain_identifier: <p>The ID of the Amazon DataZone domain.</p>
            identifier: <p>The ID of the listing.</p>
            listing_revision: <p>The revision of the listing.</p>

        Raises:
            capo_datazone.errors.access_denied_exception.AccessDeniedException: <p>You do not have sufficient access to perform this action.</p>
            capo_datazone.errors.throttling_exception.ThrottlingException: <p>The request was denied due to request throttling.</p>
            capo_datazone.errors.unauthorized_exception.UnauthorizedException: <p>You do not have permission to perform this action.</p>
            capo_datazone.errors.internal_server_exception.InternalServerException: <p>The request has failed because of an unknown error, exception or failure.</p>
            capo_datazone.errors.resource_not_found_exception.ResourceNotFoundException: <p>The specified resource cannot be found.</p>
            capo_datazone.errors.validation_exception.ValidationException: <p>The input fails to satisfy the constraints specified by the Amazon Web Services service.</p>
            capo_datazone.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        async def _handler(
            req: "AsyncOperationRequest[capo_datazone.types.get_listing_input.GetListingInput]",
        ) -> AsyncOperationResponse[
            "capo_datazone.types.get_listing_output.GetListingOutput"
        ]:
            import capo_datazone._operations.data_zone.get_listing

            (
                output,
                http_response,
            ) = await capo_datazone._operations.data_zone.get_listing.async_get_listing(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_datazone.types.get_listing_input.GetListingInput = {
            "domain_identifier": domain_identifier,
            "identifier": identifier,
        }
        if listing_revision is not None:
            input_["listing_revision"] = listing_revision

        response = await aexecute_pipeline(
            AsyncOperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        await response.response.aclose()
        return response.output

    async def delete_listing(
        self,
        domain_identifier: "capo_datazone.types.domain_id.DomainId",
        identifier: "capo_datazone.types.listing_id.ListingId",
        *,
        config_overrides: Optional[AsyncDataZoneClientConfig] = None,
    ) -> "capo_datazone.types.delete_listing_output.DeleteListingOutput":
        """<p>Deletes a listing (a record of an asset at a given time).</p>

        Args:
            domain_identifier: <p>The ID of the Amazon DataZone domain.</p>
            identifier: <p>The ID of the listing to be deleted.</p>

        Raises:
            capo_datazone.errors.access_denied_exception.AccessDeniedException: <p>You do not have sufficient access to perform this action.</p>
            capo_datazone.errors.throttling_exception.ThrottlingException: <p>The request was denied due to request throttling.</p>
            capo_datazone.errors.unauthorized_exception.UnauthorizedException: <p>You do not have permission to perform this action.</p>
            capo_datazone.errors.conflict_exception.ConflictException: <p>There is a conflict while performing this action.</p>
            capo_datazone.errors.internal_server_exception.InternalServerException: <p>The request has failed because of an unknown error, exception or failure.</p>
            capo_datazone.errors.resource_not_found_exception.ResourceNotFoundException: <p>The specified resource cannot be found.</p>
            capo_datazone.errors.validation_exception.ValidationException: <p>The input fails to satisfy the constraints specified by the Amazon Web Services service.</p>
            capo_datazone.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        async def _handler(
            req: "AsyncOperationRequest[capo_datazone.types.delete_listing_input.DeleteListingInput]",
        ) -> AsyncOperationResponse[
            "capo_datazone.types.delete_listing_output.DeleteListingOutput"
        ]:
            import capo_datazone._operations.data_zone.delete_listing

            (
                output,
                http_response,
            ) = await capo_datazone._operations.data_zone.delete_listing.async_delete_listing(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_datazone.types.delete_listing_input.DeleteListingInput = {
            "domain_identifier": domain_identifier,
            "identifier": identifier,
        }

        response = await aexecute_pipeline(
            AsyncOperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        await response.response.aclose()
        return response.output

    async def start_metadata_generation_run(
        self,
        domain_identifier: "capo_datazone.types.domain_id.DomainId",
        target: "capo_datazone.types.metadata_generation_run_target.MetadataGenerationRunTarget",
        owning_project_identifier: "capo_datazone.types.project_id.ProjectId",
        *,
        config_overrides: Optional[AsyncDataZoneClientConfig] = None,
        type: Optional[
            "capo_datazone.types.metadata_generation_run_type.MetadataGenerationRunType"
        ] = None,
        types: Optional[
            "capo_datazone.types.metadata_generation_run_types.MetadataGenerationRunTypes"
        ] = None,
        client_token: Optional["capo_datazone.types.client_token.ClientToken"] = None,
    ) -> "capo_datazone.types.start_metadata_generation_run_output.StartMetadataGenerationRunOutput":
        """<p>Starts the metadata generation run.</p> <p>Prerequisites:</p> <ul> <li> <p>Asset must be created and belong to the specified domain and project. </p> </li> <li> <p>Asset type must be supported for metadata generation (e.g., Amazon Web Services Glue table).</p> </li> <li> <p>Asset must have a structured schema with valid rows and columns.</p> </li> <li> <p>Valid values for --type: BUSINESS_DESCRIPTIONS, BUSINESS_NAMES, BUSINESS_GLOSSARY_ASSOCIATIONS.</p> </li> <li> <p>The user must have permission to run metadata generation in the domain/project.</p> </li> </ul>

        Args:
            domain_identifier: <p>The ID of the Amazon DataZone domain where you want to start a metadata generation run.</p>
            type: <p>The type of the metadata generation run.</p>
            types: <p>The types of the metadata generation run.</p>
            target: <p>The asset for which you want to start a metadata generation run.</p>
            client_token: <p>A unique, case-sensitive identifier to ensure idempotency of the request. This field is automatically populated if not provided.</p>
            owning_project_identifier: <p>The ID of the project that owns the asset for which you want to start a metadata generation run.</p>

        Raises:
            capo_datazone.errors.access_denied_exception.AccessDeniedException: <p>You do not have sufficient access to perform this action.</p>
            capo_datazone.errors.throttling_exception.ThrottlingException: <p>The request was denied due to request throttling.</p>
            capo_datazone.errors.unauthorized_exception.UnauthorizedException: <p>You do not have permission to perform this action.</p>
            capo_datazone.errors.conflict_exception.ConflictException: <p>There is a conflict while performing this action.</p>
            capo_datazone.errors.internal_server_exception.InternalServerException: <p>The request has failed because of an unknown error, exception or failure.</p>
            capo_datazone.errors.resource_not_found_exception.ResourceNotFoundException: <p>The specified resource cannot be found.</p>
            capo_datazone.errors.service_quota_exceeded_exception.ServiceQuotaExceededException: <p>The request has exceeded the specified service quota.</p>
            capo_datazone.errors.validation_exception.ValidationException: <p>The input fails to satisfy the constraints specified by the Amazon Web Services service.</p>
            capo_datazone.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        async def _handler(
            req: "AsyncOperationRequest[capo_datazone.types.start_metadata_generation_run_input.StartMetadataGenerationRunInput]",
        ) -> AsyncOperationResponse[
            "capo_datazone.types.start_metadata_generation_run_output.StartMetadataGenerationRunOutput"
        ]:
            import capo_datazone._operations.data_zone.start_metadata_generation_run

            (
                output,
                http_response,
            ) = await capo_datazone._operations.data_zone.start_metadata_generation_run.async_start_metadata_generation_run(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_datazone.types.start_metadata_generation_run_input.StartMetadataGenerationRunInput = {
            "domain_identifier": domain_identifier,
            "target": target,
            "owning_project_identifier": owning_project_identifier,
        }
        if type is not None:
            input_["type"] = type
        if types is not None:
            input_["types"] = types
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

    async def get_metadata_generation_run(
        self,
        domain_identifier: "capo_datazone.types.domain_id.DomainId",
        identifier: "capo_datazone.types.metadata_generation_run_identifier.MetadataGenerationRunIdentifier",
        *,
        config_overrides: Optional[AsyncDataZoneClientConfig] = None,
        type: Optional[
            "capo_datazone.types.metadata_generation_run_type.MetadataGenerationRunType"
        ] = None,
    ) -> "capo_datazone.types.get_metadata_generation_run_output.GetMetadataGenerationRunOutput":
        """<p>Gets a metadata generation run in Amazon DataZone.</p> <p>Prerequisites:</p> <ul> <li> <p>Valid domain and run identifier. </p> </li> <li> <p>The metadata generation run must exist.</p> </li> <li> <p>User must have read access to the metadata run.</p> </li> </ul>

        Args:
            domain_identifier: <p>The ID of the Amazon DataZone domain the metadata generation run of which you want to get.</p>
            identifier: <p>The identifier of the metadata generation run.</p>
            type: <p>The type of the metadata generation run.</p>

        Raises:
            capo_datazone.errors.access_denied_exception.AccessDeniedException: <p>You do not have sufficient access to perform this action.</p>
            capo_datazone.errors.throttling_exception.ThrottlingException: <p>The request was denied due to request throttling.</p>
            capo_datazone.errors.unauthorized_exception.UnauthorizedException: <p>You do not have permission to perform this action.</p>
            capo_datazone.errors.internal_server_exception.InternalServerException: <p>The request has failed because of an unknown error, exception or failure.</p>
            capo_datazone.errors.resource_not_found_exception.ResourceNotFoundException: <p>The specified resource cannot be found.</p>
            capo_datazone.errors.validation_exception.ValidationException: <p>The input fails to satisfy the constraints specified by the Amazon Web Services service.</p>
            capo_datazone.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        async def _handler(
            req: "AsyncOperationRequest[capo_datazone.types.get_metadata_generation_run_input.GetMetadataGenerationRunInput]",
        ) -> AsyncOperationResponse[
            "capo_datazone.types.get_metadata_generation_run_output.GetMetadataGenerationRunOutput"
        ]:
            import capo_datazone._operations.data_zone.get_metadata_generation_run

            (
                output,
                http_response,
            ) = await capo_datazone._operations.data_zone.get_metadata_generation_run.async_get_metadata_generation_run(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_datazone.types.get_metadata_generation_run_input.GetMetadataGenerationRunInput = {
            "domain_identifier": domain_identifier,
            "identifier": identifier,
        }
        if type is not None:
            input_["type"] = type

        response = await aexecute_pipeline(
            AsyncOperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        await response.response.aclose()
        return response.output

    async def cancel_metadata_generation_run(
        self,
        domain_identifier: "capo_datazone.types.domain_id.DomainId",
        identifier: "capo_datazone.types.metadata_generation_run_identifier.MetadataGenerationRunIdentifier",
        *,
        config_overrides: Optional[AsyncDataZoneClientConfig] = None,
    ) -> "capo_datazone.types.cancel_metadata_generation_run_output.CancelMetadataGenerationRunOutput":
        """<p>Cancels the metadata generation run.</p> <p>Prerequisites:</p> <ul> <li> <p>The run must exist and be in a cancelable status (e.g., SUBMITTED, IN_PROGRESS). </p> </li> <li> <p>Runs in SUCCEEDED status cannot be cancelled.</p> </li> <li> <p>User must have access to the run and cancel permissions.</p> </li> </ul>

        Args:
            domain_identifier: <p>The ID of the Amazon DataZone domain in which the metadata generation run is to be cancelled.</p>
            identifier: <p>The ID of the metadata generation run.</p>

        Raises:
            capo_datazone.errors.access_denied_exception.AccessDeniedException: <p>You do not have sufficient access to perform this action.</p>
            capo_datazone.errors.throttling_exception.ThrottlingException: <p>The request was denied due to request throttling.</p>
            capo_datazone.errors.unauthorized_exception.UnauthorizedException: <p>You do not have permission to perform this action.</p>
            capo_datazone.errors.conflict_exception.ConflictException: <p>There is a conflict while performing this action.</p>
            capo_datazone.errors.internal_server_exception.InternalServerException: <p>The request has failed because of an unknown error, exception or failure.</p>
            capo_datazone.errors.resource_not_found_exception.ResourceNotFoundException: <p>The specified resource cannot be found.</p>
            capo_datazone.errors.validation_exception.ValidationException: <p>The input fails to satisfy the constraints specified by the Amazon Web Services service.</p>
            capo_datazone.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        async def _handler(
            req: "AsyncOperationRequest[capo_datazone.types.cancel_metadata_generation_run_input.CancelMetadataGenerationRunInput]",
        ) -> AsyncOperationResponse[
            "capo_datazone.types.cancel_metadata_generation_run_output.CancelMetadataGenerationRunOutput"
        ]:
            import capo_datazone._operations.data_zone.cancel_metadata_generation_run

            (
                output,
                http_response,
            ) = await capo_datazone._operations.data_zone.cancel_metadata_generation_run.async_cancel_metadata_generation_run(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_datazone.types.cancel_metadata_generation_run_input.CancelMetadataGenerationRunInput = {
            "domain_identifier": domain_identifier,
            "identifier": identifier,
        }

        response = await aexecute_pipeline(
            AsyncOperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        await response.response.aclose()
        return response.output

    async def list_metadata_generation_runs(
        self,
        domain_identifier: "capo_datazone.types.domain_id.DomainId",
        *,
        config_overrides: Optional[AsyncDataZoneClientConfig] = None,
        status: Optional[
            "capo_datazone.types.metadata_generation_run_status.MetadataGenerationRunStatus"
        ] = None,
        type: Optional[
            "capo_datazone.types.metadata_generation_run_type.MetadataGenerationRunType"
        ] = None,
        next_token: Optional[
            "capo_datazone.types.pagination_token.PaginationToken"
        ] = None,
        max_results: Optional["capo_datazone.types.max_results.MaxResults"] = None,
        target_identifier: Optional["capo_datazone.types.entity_id.EntityId"] = None,
    ) -> "capo_datazone.types.list_metadata_generation_runs_output.ListMetadataGenerationRunsOutput":
        """<p>Lists all metadata generation runs.</p> <p>Metadata generation runs represent automated processes that leverage AI/ML capabilities to create or enhance asset metadata at scale. This feature helps organizations maintain comprehensive and consistent metadata across large numbers of assets without manual intervention. It can automatically generate business descriptions, tags, and other metadata elements, significantly reducing the time and effort required for metadata management while improving consistency and completeness.</p> <p>Prerequisites:</p> <ul> <li> <p>Valid domain identifier. </p> </li> <li> <p>User must have access to metadata generation runs in the domain.</p> </li> </ul>

        Args:
            domain_identifier: <p>The ID of the Amazon DataZone domain where you want to list metadata generation runs.</p>
            status: <p>The status of the metadata generation runs.</p>
            type: <p>The type of the metadata generation runs.</p>
            next_token: <p>When the number of metadata generation runs is greater than the default value for the MaxResults parameter, or if you explicitly specify a value for MaxResults that is less than the number of metadata generation runs, the response includes a pagination token named NextToken. You can specify this NextToken value in a subsequent call to ListMetadataGenerationRuns to list the next set of revisions.</p>
            max_results: <p>The maximum number of metadata generation runs to return in a single call to ListMetadataGenerationRuns. When the number of metadata generation runs to be listed is greater than the value of MaxResults, the response contains a NextToken value that you can use in a subsequent call to ListMetadataGenerationRuns to list the next set of revisions.</p>
            target_identifier: <p>The target ID for which you want to list metadata generation runs.</p>

        Raises:
            capo_datazone.errors.access_denied_exception.AccessDeniedException: <p>You do not have sufficient access to perform this action.</p>
            capo_datazone.errors.throttling_exception.ThrottlingException: <p>The request was denied due to request throttling.</p>
            capo_datazone.errors.unauthorized_exception.UnauthorizedException: <p>You do not have permission to perform this action.</p>
            capo_datazone.errors.internal_server_exception.InternalServerException: <p>The request has failed because of an unknown error, exception or failure.</p>
            capo_datazone.errors.resource_not_found_exception.ResourceNotFoundException: <p>The specified resource cannot be found.</p>
            capo_datazone.errors.validation_exception.ValidationException: <p>The input fails to satisfy the constraints specified by the Amazon Web Services service.</p>
            capo_datazone.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        async def _handler(
            req: "AsyncOperationRequest[capo_datazone.types.list_metadata_generation_runs_input.ListMetadataGenerationRunsInput]",
        ) -> AsyncOperationResponse[
            "capo_datazone.types.list_metadata_generation_runs_output.ListMetadataGenerationRunsOutput"
        ]:
            import capo_datazone._operations.data_zone.list_metadata_generation_runs

            (
                output,
                http_response,
            ) = await capo_datazone._operations.data_zone.list_metadata_generation_runs.async_list_metadata_generation_runs(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_datazone.types.list_metadata_generation_runs_input.ListMetadataGenerationRunsInput = {
            "domain_identifier": domain_identifier
        }
        if status is not None:
            input_["status"] = status
        if type is not None:
            input_["type"] = type
        if next_token is not None:
            input_["next_token"] = next_token
        if max_results is not None:
            input_["max_results"] = max_results
        if target_identifier is not None:
            input_["target_identifier"] = target_identifier

        response = await aexecute_pipeline(
            AsyncOperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        await response.response.aclose()
        return response.output

    async def iter_list_metadata_generation_runs(
        self,
        domain_identifier: "capo_datazone.types.domain_id.DomainId",
        *,
        config_overrides: Optional[AsyncDataZoneClientConfig] = None,
        status: Optional[
            "capo_datazone.types.metadata_generation_run_status.MetadataGenerationRunStatus"
        ] = None,
        type: Optional[
            "capo_datazone.types.metadata_generation_run_type.MetadataGenerationRunType"
        ] = None,
        next_token: Optional[
            "capo_datazone.types.pagination_token.PaginationToken"
        ] = None,
        max_results: Optional["capo_datazone.types.max_results.MaxResults"] = None,
        target_identifier: Optional["capo_datazone.types.entity_id.EntityId"] = None,
    ) -> "AsyncIterator[capo_datazone.types.metadata_generation_run_item.MetadataGenerationRunItem]":
        _token = next_token
        while True:
            _response = await self.list_metadata_generation_runs(
                domain_identifier,
                config_overrides=config_overrides,
                status=status,
                type=type,
                next_token=_token,
                max_results=max_results,
                target_identifier=target_identifier,
            )
            _page = _resolve_path(_response, ("items",))
            for _item in _page or []:
                yield _item
            _token = _resolve_path(_response, ("next_token",))
            if not _token:
                break

    async def create_notebook(
        self,
        domain_identifier: "capo_datazone.types.domain_id.DomainId",
        owning_project_identifier: "capo_datazone.types.project_id.ProjectId",
        name: "capo_datazone.types.notebook_name.NotebookName",
        *,
        config_overrides: Optional[AsyncDataZoneClientConfig] = None,
        description: Optional["capo_datazone.types.description.Description"] = None,
        type: Optional["capo_datazone.types.notebook_type.NotebookType"] = None,
        metadata: Optional["capo_datazone.types.metadata.Metadata"] = None,
        parameters: Optional["capo_datazone.types.parameters.Parameters"] = None,
        client_token: Optional["capo_datazone.types.client_token.ClientToken"] = None,
    ) -> "capo_datazone.types.create_notebook_output.CreateNotebookOutput":
        """<p>Creates a <a href="https://docs.aws.amazon.com/sagemaker-unified-studio/latest/userguide/notebooks.html">notebook</a> in Amazon SageMaker Unified Studio. A notebook is a collaborative document within a project that contains code cells for interactive computing.</p>

        Args:
            domain_identifier: <p>The identifier of the Amazon SageMaker Unified Studio domain in which to create the notebook.</p>
            owning_project_identifier: <p>The identifier of the project that owns the notebook.</p>
            name: <p>The name of the notebook. The name must be between 1 and 256 characters.</p>
            description: <p>The description of the notebook.</p>
            type: <p>The type of the notebook.</p>
            metadata: <p>The metadata for the notebook, specified as key-value pairs. You can specify up to 50 entries, with keys up to 128 characters and values up to 1024 characters.</p>
            parameters: <p>The sensitive parameters for the notebook, specified as key-value pairs. You can specify up to 50 entries, with keys up to 128 characters and values up to 1024 characters.</p>
            client_token: <p>A unique, case-sensitive identifier to ensure idempotency of the request. This field is automatically populated if not provided.</p>

        Raises:
            capo_datazone.errors.access_denied_exception.AccessDeniedException: <p>You do not have sufficient access to perform this action.</p>
            capo_datazone.errors.throttling_exception.ThrottlingException: <p>The request was denied due to request throttling.</p>
            capo_datazone.errors.unauthorized_exception.UnauthorizedException: <p>You do not have permission to perform this action.</p>
            capo_datazone.errors.conflict_exception.ConflictException: <p>There is a conflict while performing this action.</p>
            capo_datazone.errors.internal_server_exception.InternalServerException: <p>The request has failed because of an unknown error, exception or failure.</p>
            capo_datazone.errors.resource_not_found_exception.ResourceNotFoundException: <p>The specified resource cannot be found.</p>
            capo_datazone.errors.service_quota_exceeded_exception.ServiceQuotaExceededException: <p>The request has exceeded the specified service quota.</p>
            capo_datazone.errors.validation_exception.ValidationException: <p>The input fails to satisfy the constraints specified by the Amazon Web Services service.</p>
            capo_datazone.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        async def _handler(
            req: "AsyncOperationRequest[capo_datazone.types.create_notebook_input.CreateNotebookInput]",
        ) -> AsyncOperationResponse[
            "capo_datazone.types.create_notebook_output.CreateNotebookOutput"
        ]:
            import capo_datazone._operations.data_zone.create_notebook

            (
                output,
                http_response,
            ) = await capo_datazone._operations.data_zone.create_notebook.async_create_notebook(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_datazone.types.create_notebook_input.CreateNotebookInput = {
            "domain_identifier": domain_identifier,
            "owning_project_identifier": owning_project_identifier,
            "name": name,
        }
        if description is not None:
            input_["description"] = description
        if type is not None:
            input_["type"] = type
        if metadata is not None:
            input_["metadata"] = metadata
        if parameters is not None:
            input_["parameters"] = parameters
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

    async def get_notebook(
        self,
        domain_identifier: "capo_datazone.types.domain_id.DomainId",
        identifier: "capo_datazone.types.notebook_id.NotebookId",
        *,
        config_overrides: Optional[AsyncDataZoneClientConfig] = None,
    ) -> "capo_datazone.types.get_notebook_output.GetNotebookOutput":
        """<p>Gets the details of a <a href="https://docs.aws.amazon.com/sagemaker-unified-studio/latest/userguide/notebooks.html">notebook</a> in Amazon SageMaker Unified Studio.</p>

        Args:
            domain_identifier: <p>The identifier of the Amazon SageMaker Unified Studio domain in which the notebook exists.</p>
            identifier: <p>The identifier of the notebook.</p>

        Raises:
            capo_datazone.errors.access_denied_exception.AccessDeniedException: <p>You do not have sufficient access to perform this action.</p>
            capo_datazone.errors.throttling_exception.ThrottlingException: <p>The request was denied due to request throttling.</p>
            capo_datazone.errors.unauthorized_exception.UnauthorizedException: <p>You do not have permission to perform this action.</p>
            capo_datazone.errors.internal_server_exception.InternalServerException: <p>The request has failed because of an unknown error, exception or failure.</p>
            capo_datazone.errors.resource_not_found_exception.ResourceNotFoundException: <p>The specified resource cannot be found.</p>
            capo_datazone.errors.validation_exception.ValidationException: <p>The input fails to satisfy the constraints specified by the Amazon Web Services service.</p>
            capo_datazone.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        async def _handler(
            req: "AsyncOperationRequest[capo_datazone.types.get_notebook_input.GetNotebookInput]",
        ) -> AsyncOperationResponse[
            "capo_datazone.types.get_notebook_output.GetNotebookOutput"
        ]:
            import capo_datazone._operations.data_zone.get_notebook

            (
                output,
                http_response,
            ) = await capo_datazone._operations.data_zone.get_notebook.async_get_notebook(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_datazone.types.get_notebook_input.GetNotebookInput = {
            "domain_identifier": domain_identifier,
            "identifier": identifier,
        }

        response = await aexecute_pipeline(
            AsyncOperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        await response.response.aclose()
        return response.output

    async def update_notebook(
        self,
        domain_identifier: "capo_datazone.types.domain_id.DomainId",
        identifier: "capo_datazone.types.notebook_id.NotebookId",
        *,
        config_overrides: Optional[AsyncDataZoneClientConfig] = None,
        description: Optional["capo_datazone.types.description.Description"] = None,
        status: Optional["capo_datazone.types.notebook_status.NotebookStatus"] = None,
        name: Optional["capo_datazone.types.notebook_name.NotebookName"] = None,
        cell_order: Optional["capo_datazone.types.cell_order.CellOrder"] = None,
        type: Optional["capo_datazone.types.notebook_type.NotebookType"] = None,
        metadata: Optional["capo_datazone.types.metadata.Metadata"] = None,
        parameters: Optional["capo_datazone.types.parameters.Parameters"] = None,
        environment_configuration: Optional[
            "capo_datazone.types.environment_config.EnvironmentConfig"
        ] = None,
        client_token: Optional["capo_datazone.types.client_token.ClientToken"] = None,
    ) -> "capo_datazone.types.update_notebook_output.UpdateNotebookOutput":
        """<p>Updates a <a href="https://docs.aws.amazon.com/sagemaker-unified-studio/latest/userguide/notebooks.html">notebook</a> in Amazon SageMaker Unified Studio.</p>

        Args:
            domain_identifier: <p>The identifier of the Amazon SageMaker Unified Studio domain in which the notebook exists.</p>
            identifier: <p>The identifier of the notebook to update.</p>
            description: <p>The updated description of the notebook.</p>
            status: <p>The updated status of the notebook.</p>
            name: <p>The updated name of the notebook.</p>
            cell_order: <p>The updated ordered list of cells in the notebook.</p>
            type: <p>The updated type of the notebook.</p>
            metadata: <p>The updated metadata for the notebook, specified as key-value pairs.</p>
            parameters: <p>The updated sensitive parameters for the notebook, specified as key-value pairs.</p>
            environment_configuration: <p>The updated environment configuration for the notebook.</p>
            client_token: <p>A unique, case-sensitive identifier to ensure idempotency of the request. This field is automatically populated if not provided.</p>

        Raises:
            capo_datazone.errors.access_denied_exception.AccessDeniedException: <p>You do not have sufficient access to perform this action.</p>
            capo_datazone.errors.throttling_exception.ThrottlingException: <p>The request was denied due to request throttling.</p>
            capo_datazone.errors.unauthorized_exception.UnauthorizedException: <p>You do not have permission to perform this action.</p>
            capo_datazone.errors.conflict_exception.ConflictException: <p>There is a conflict while performing this action.</p>
            capo_datazone.errors.internal_server_exception.InternalServerException: <p>The request has failed because of an unknown error, exception or failure.</p>
            capo_datazone.errors.resource_not_found_exception.ResourceNotFoundException: <p>The specified resource cannot be found.</p>
            capo_datazone.errors.validation_exception.ValidationException: <p>The input fails to satisfy the constraints specified by the Amazon Web Services service.</p>
            capo_datazone.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        async def _handler(
            req: "AsyncOperationRequest[capo_datazone.types.update_notebook_input.UpdateNotebookInput]",
        ) -> AsyncOperationResponse[
            "capo_datazone.types.update_notebook_output.UpdateNotebookOutput"
        ]:
            import capo_datazone._operations.data_zone.update_notebook

            (
                output,
                http_response,
            ) = await capo_datazone._operations.data_zone.update_notebook.async_update_notebook(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_datazone.types.update_notebook_input.UpdateNotebookInput = {
            "domain_identifier": domain_identifier,
            "identifier": identifier,
        }
        if description is not None:
            input_["description"] = description
        if status is not None:
            input_["status"] = status
        if name is not None:
            input_["name"] = name
        if cell_order is not None:
            input_["cell_order"] = cell_order
        if type is not None:
            input_["type"] = type
        if metadata is not None:
            input_["metadata"] = metadata
        if parameters is not None:
            input_["parameters"] = parameters
        if environment_configuration is not None:
            input_["environment_configuration"] = environment_configuration
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

    async def delete_notebook(
        self,
        domain_identifier: "capo_datazone.types.domain_id.DomainId",
        identifier: "capo_datazone.types.notebook_id.NotebookId",
        *,
        config_overrides: Optional[AsyncDataZoneClientConfig] = None,
    ) -> "capo_datazone.types.delete_notebook_output.DeleteNotebookOutput":
        """<p>Deletes a <a href="https://docs.aws.amazon.com/sagemaker-unified-studio/latest/userguide/notebooks.html">notebook</a> in Amazon SageMaker Unified Studio.</p>

        Args:
            domain_identifier: <p>The identifier of the Amazon SageMaker Unified Studio domain in which the notebook exists.</p>
            identifier: <p>The identifier of the notebook to delete.</p>

        Raises:
            capo_datazone.errors.access_denied_exception.AccessDeniedException: <p>You do not have sufficient access to perform this action.</p>
            capo_datazone.errors.throttling_exception.ThrottlingException: <p>The request was denied due to request throttling.</p>
            capo_datazone.errors.unauthorized_exception.UnauthorizedException: <p>You do not have permission to perform this action.</p>
            capo_datazone.errors.conflict_exception.ConflictException: <p>There is a conflict while performing this action.</p>
            capo_datazone.errors.internal_server_exception.InternalServerException: <p>The request has failed because of an unknown error, exception or failure.</p>
            capo_datazone.errors.validation_exception.ValidationException: <p>The input fails to satisfy the constraints specified by the Amazon Web Services service.</p>
            capo_datazone.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        async def _handler(
            req: "AsyncOperationRequest[capo_datazone.types.delete_notebook_input.DeleteNotebookInput]",
        ) -> AsyncOperationResponse[
            "capo_datazone.types.delete_notebook_output.DeleteNotebookOutput"
        ]:
            import capo_datazone._operations.data_zone.delete_notebook

            (
                output,
                http_response,
            ) = await capo_datazone._operations.data_zone.delete_notebook.async_delete_notebook(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_datazone.types.delete_notebook_input.DeleteNotebookInput = {
            "domain_identifier": domain_identifier,
            "identifier": identifier,
        }

        response = await aexecute_pipeline(
            AsyncOperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        await response.response.aclose()
        return response.output

    async def list_notebooks(
        self,
        domain_identifier: "capo_datazone.types.domain_id.DomainId",
        owning_project_identifier: "capo_datazone.types.project_id.ProjectId",
        *,
        config_overrides: Optional[AsyncDataZoneClientConfig] = None,
        max_results: Optional["capo_datazone.types.max_results.MaxResults"] = None,
        sort_order: Optional["capo_datazone.types.sort_order.SortOrder"] = None,
        sort_by: Optional["capo_datazone.types.sort_key.SortKey"] = None,
        status: Optional["capo_datazone.types.notebook_status.NotebookStatus"] = None,
        type: Optional["capo_datazone.types.notebook_type.NotebookType"] = None,
        next_token: Optional[
            "capo_datazone.types.pagination_token.PaginationToken"
        ] = None,
    ) -> "capo_datazone.types.list_notebooks_output.ListNotebooksOutput":
        """<p>Lists <a href="https://docs.aws.amazon.com/sagemaker-unified-studio/latest/userguide/notebooks.html">notebooks</a> in Amazon SageMaker Unified Studio.</p>

        Args:
            domain_identifier: <p>The identifier of the Amazon SageMaker Unified Studio domain in which to list notebooks.</p>
            owning_project_identifier: <p>The identifier of the project that owns the notebooks.</p>
            max_results: <p>The maximum number of notebooks to return in a single call. When the number of notebooks exceeds the value of <code>MaxResults</code>, the response contains a <code>NextToken</code> value.</p>
            sort_order: <p>The sort order for the results.</p>
            sort_by: <p>The field to sort the results by.</p>
            status: <p>The status to filter notebooks by.</p>
            type: <p>The type to filter notebooks by.</p>
            next_token: <p>When the number of notebooks is greater than the default value for the <code>MaxResults</code> parameter, or if you explicitly specify a value for <code>MaxResults</code> that is less than the number of notebooks, the response includes a pagination token named <code>NextToken</code>. You can specify this <code>NextToken</code> value in a subsequent call to <code>ListNotebooks</code> to list the next set of notebooks.</p>

        Raises:
            capo_datazone.errors.access_denied_exception.AccessDeniedException: <p>You do not have sufficient access to perform this action.</p>
            capo_datazone.errors.throttling_exception.ThrottlingException: <p>The request was denied due to request throttling.</p>
            capo_datazone.errors.unauthorized_exception.UnauthorizedException: <p>You do not have permission to perform this action.</p>
            capo_datazone.errors.internal_server_exception.InternalServerException: <p>The request has failed because of an unknown error, exception or failure.</p>
            capo_datazone.errors.validation_exception.ValidationException: <p>The input fails to satisfy the constraints specified by the Amazon Web Services service.</p>
            capo_datazone.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        async def _handler(
            req: "AsyncOperationRequest[capo_datazone.types.list_notebooks_input.ListNotebooksInput]",
        ) -> AsyncOperationResponse[
            "capo_datazone.types.list_notebooks_output.ListNotebooksOutput"
        ]:
            import capo_datazone._operations.data_zone.list_notebooks

            (
                output,
                http_response,
            ) = await capo_datazone._operations.data_zone.list_notebooks.async_list_notebooks(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_datazone.types.list_notebooks_input.ListNotebooksInput = {
            "domain_identifier": domain_identifier,
            "owning_project_identifier": owning_project_identifier,
        }
        if max_results is not None:
            input_["max_results"] = max_results
        if sort_order is not None:
            input_["sort_order"] = sort_order
        if sort_by is not None:
            input_["sort_by"] = sort_by
        if status is not None:
            input_["status"] = status
        if type is not None:
            input_["type"] = type
        if next_token is not None:
            input_["next_token"] = next_token

        response = await aexecute_pipeline(
            AsyncOperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        await response.response.aclose()
        return response.output

    async def iter_list_notebooks(
        self,
        domain_identifier: "capo_datazone.types.domain_id.DomainId",
        owning_project_identifier: "capo_datazone.types.project_id.ProjectId",
        *,
        config_overrides: Optional[AsyncDataZoneClientConfig] = None,
        max_results: Optional["capo_datazone.types.max_results.MaxResults"] = None,
        sort_order: Optional["capo_datazone.types.sort_order.SortOrder"] = None,
        sort_by: Optional["capo_datazone.types.sort_key.SortKey"] = None,
        status: Optional["capo_datazone.types.notebook_status.NotebookStatus"] = None,
        type: Optional["capo_datazone.types.notebook_type.NotebookType"] = None,
        next_token: Optional[
            "capo_datazone.types.pagination_token.PaginationToken"
        ] = None,
    ) -> "AsyncIterator[capo_datazone.types.notebook_summary.NotebookSummary]":
        _token = next_token
        while True:
            _response = await self.list_notebooks(
                domain_identifier,
                owning_project_identifier,
                config_overrides=config_overrides,
                max_results=max_results,
                sort_order=sort_order,
                sort_by=sort_by,
                status=status,
                type=type,
                next_token=_token,
            )
            _page = _resolve_path(_response, ("items",))
            for _item in _page or []:
                yield _item
            _token = _resolve_path(_response, ("next_token",))
            if not _token:
                break

    async def start_notebook_export(
        self,
        domain_identifier: "capo_datazone.types.domain_id.DomainId",
        notebook_identifier: "capo_datazone.types.notebook_id.NotebookId",
        owning_project_identifier: "capo_datazone.types.project_id.ProjectId",
        file_format: "capo_datazone.types.file_format.FileFormat",
        *,
        config_overrides: Optional[AsyncDataZoneClientConfig] = None,
        client_token: Optional["capo_datazone.types.client_token.ClientToken"] = None,
    ) -> "capo_datazone.types.start_notebook_export_output.StartNotebookExportOutput":
        """<p>Starts a notebook export in Amazon SageMaker Unified Studio. This operation exports a notebook to a specified file format and stores the output in Amazon Simple Storage Service.</p>

        Args:
            domain_identifier: <p>The identifier of the Amazon SageMaker Unified Studio domain in which to export the notebook.</p>
            notebook_identifier: <p>The identifier of the notebook to export.</p>
            owning_project_identifier: <p>The identifier of the project that owns the notebook.</p>
            file_format: <p>The file format for the notebook export. Valid values are <code>PDF</code> and <code>IPYNB</code>.</p>
            client_token: <p>A unique, case-sensitive identifier to ensure idempotency of the request. This field is automatically populated if not provided.</p>

        Raises:
            capo_datazone.errors.access_denied_exception.AccessDeniedException: <p>You do not have sufficient access to perform this action.</p>
            capo_datazone.errors.throttling_exception.ThrottlingException: <p>The request was denied due to request throttling.</p>
            capo_datazone.errors.unauthorized_exception.UnauthorizedException: <p>You do not have permission to perform this action.</p>
            capo_datazone.errors.conflict_exception.ConflictException: <p>There is a conflict while performing this action.</p>
            capo_datazone.errors.internal_server_exception.InternalServerException: <p>The request has failed because of an unknown error, exception or failure.</p>
            capo_datazone.errors.resource_not_found_exception.ResourceNotFoundException: <p>The specified resource cannot be found.</p>
            capo_datazone.errors.service_quota_exceeded_exception.ServiceQuotaExceededException: <p>The request has exceeded the specified service quota.</p>
            capo_datazone.errors.validation_exception.ValidationException: <p>The input fails to satisfy the constraints specified by the Amazon Web Services service.</p>
            capo_datazone.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        async def _handler(
            req: "AsyncOperationRequest[capo_datazone.types.start_notebook_export_input.StartNotebookExportInput]",
        ) -> AsyncOperationResponse[
            "capo_datazone.types.start_notebook_export_output.StartNotebookExportOutput"
        ]:
            import capo_datazone._operations.data_zone.start_notebook_export

            (
                output,
                http_response,
            ) = await capo_datazone._operations.data_zone.start_notebook_export.async_start_notebook_export(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_datazone.types.start_notebook_export_input.StartNotebookExportInput = {
            "domain_identifier": domain_identifier,
            "notebook_identifier": notebook_identifier,
            "owning_project_identifier": owning_project_identifier,
            "file_format": file_format,
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

    async def get_notebook_export(
        self,
        domain_identifier: "capo_datazone.types.domain_id.DomainId",
        identifier: "capo_datazone.types.export_id.ExportId",
        *,
        config_overrides: Optional[AsyncDataZoneClientConfig] = None,
    ) -> "capo_datazone.types.get_notebook_export_output.GetNotebookExportOutput":
        """<p>Gets the details of a notebook export in Amazon SageMaker Unified Studio.</p>

        Args:
            domain_identifier: <p>The identifier of the Amazon SageMaker Unified Studio domain in which the notebook export exists.</p>
            identifier: <p>The identifier of the notebook export.</p>

        Raises:
            capo_datazone.errors.access_denied_exception.AccessDeniedException: <p>You do not have sufficient access to perform this action.</p>
            capo_datazone.errors.throttling_exception.ThrottlingException: <p>The request was denied due to request throttling.</p>
            capo_datazone.errors.unauthorized_exception.UnauthorizedException: <p>You do not have permission to perform this action.</p>
            capo_datazone.errors.internal_server_exception.InternalServerException: <p>The request has failed because of an unknown error, exception or failure.</p>
            capo_datazone.errors.resource_not_found_exception.ResourceNotFoundException: <p>The specified resource cannot be found.</p>
            capo_datazone.errors.validation_exception.ValidationException: <p>The input fails to satisfy the constraints specified by the Amazon Web Services service.</p>
            capo_datazone.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        async def _handler(
            req: "AsyncOperationRequest[capo_datazone.types.get_notebook_export_input.GetNotebookExportInput]",
        ) -> AsyncOperationResponse[
            "capo_datazone.types.get_notebook_export_output.GetNotebookExportOutput"
        ]:
            import capo_datazone._operations.data_zone.get_notebook_export

            (
                output,
                http_response,
            ) = await capo_datazone._operations.data_zone.get_notebook_export.async_get_notebook_export(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_datazone.types.get_notebook_export_input.GetNotebookExportInput = {
            "domain_identifier": domain_identifier,
            "identifier": identifier,
        }

        response = await aexecute_pipeline(
            AsyncOperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        await response.response.aclose()
        return response.output

    async def start_notebook_run(
        self,
        domain_identifier: "capo_datazone.types.domain_id.DomainId",
        owning_project_identifier: "capo_datazone.types.project_id.ProjectId",
        notebook_identifier: "capo_datazone.types.notebook_id.NotebookId",
        *,
        config_overrides: Optional[AsyncDataZoneClientConfig] = None,
        schedule_identifier: Optional[
            "capo_datazone.types.schedule_id.ScheduleId"
        ] = None,
        compute_configuration: Optional[
            "capo_datazone.types.compute_config.ComputeConfig"
        ] = None,
        network_configuration: Optional[
            "capo_datazone.types.network_config.NetworkConfig"
        ] = None,
        timeout_configuration: Optional[
            "capo_datazone.types.timeout_config.TimeoutConfig"
        ] = None,
        trigger_source: Optional[
            "capo_datazone.types.trigger_source.TriggerSource"
        ] = None,
        metadata: Optional["capo_datazone.types.metadata.Metadata"] = None,
        parameters: Optional["capo_datazone.types.parameters.Parameters"] = None,
        client_token: Optional["capo_datazone.types.client_token.ClientToken"] = None,
    ) -> "capo_datazone.types.start_notebook_run_output.StartNotebookRunOutput":
        """<p>Starts a notebook run in Amazon SageMaker Unified Studio. A notebook run represents the execution of an <a href="https://docs.aws.amazon.com/sagemaker-unified-studio/latest/userguide/notebooks.html">Amazon SageMaker notebook</a> within a project. You can configure compute, network, timeout, and environment settings for the run.</p>

        Args:
            domain_identifier: <p>The identifier of the Amazon SageMaker Unified Studio domain in which the notebook run is started.</p>
            owning_project_identifier: <p>The identifier of the project that owns the notebook run.</p>
            notebook_identifier: <p>The identifier of the notebook to run.</p>
            schedule_identifier: <p>The identifier of the schedule associated with the notebook run.</p>
            compute_configuration: <p>The compute configuration for the notebook run, including instance type and environment version.</p>
            network_configuration: <p>The network configuration for the notebook run, including network access type and optional VPC settings.</p>
            timeout_configuration: <p>The timeout configuration for the notebook run. The default timeout is 720 minutes (12 hours) and the maximum is 1440 minutes (24 hours).</p>
            trigger_source: <p>The source that triggered the notebook run.</p>
            metadata: <p>The metadata for the notebook run, specified as key-value pairs. You can specify up to 50 entries, with keys up to 128 characters and values up to 1024 characters.</p>
            parameters: <p>The sensitive parameters for the notebook run, specified as key-value pairs. You can specify up to 50 entries, with keys up to 128 characters and values up to 1024 characters.</p>
            client_token: <p>A unique, case-sensitive identifier to ensure idempotency of the request. This field is automatically populated if not provided.</p>

        Raises:
            capo_datazone.errors.access_denied_exception.AccessDeniedException: <p>You do not have sufficient access to perform this action.</p>
            capo_datazone.errors.throttling_exception.ThrottlingException: <p>The request was denied due to request throttling.</p>
            capo_datazone.errors.unauthorized_exception.UnauthorizedException: <p>You do not have permission to perform this action.</p>
            capo_datazone.errors.conflict_exception.ConflictException: <p>There is a conflict while performing this action.</p>
            capo_datazone.errors.internal_server_exception.InternalServerException: <p>The request has failed because of an unknown error, exception or failure.</p>
            capo_datazone.errors.resource_not_found_exception.ResourceNotFoundException: <p>The specified resource cannot be found.</p>
            capo_datazone.errors.service_quota_exceeded_exception.ServiceQuotaExceededException: <p>The request has exceeded the specified service quota.</p>
            capo_datazone.errors.validation_exception.ValidationException: <p>The input fails to satisfy the constraints specified by the Amazon Web Services service.</p>
            capo_datazone.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        async def _handler(
            req: "AsyncOperationRequest[capo_datazone.types.start_notebook_run_input.StartNotebookRunInput]",
        ) -> AsyncOperationResponse[
            "capo_datazone.types.start_notebook_run_output.StartNotebookRunOutput"
        ]:
            import capo_datazone._operations.data_zone.start_notebook_run

            (
                output,
                http_response,
            ) = await capo_datazone._operations.data_zone.start_notebook_run.async_start_notebook_run(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_datazone.types.start_notebook_run_input.StartNotebookRunInput = {
            "domain_identifier": domain_identifier,
            "owning_project_identifier": owning_project_identifier,
            "notebook_identifier": notebook_identifier,
        }
        if schedule_identifier is not None:
            input_["schedule_identifier"] = schedule_identifier
        if compute_configuration is not None:
            input_["compute_configuration"] = compute_configuration
        if network_configuration is not None:
            input_["network_configuration"] = network_configuration
        if timeout_configuration is not None:
            input_["timeout_configuration"] = timeout_configuration
        if trigger_source is not None:
            input_["trigger_source"] = trigger_source
        if metadata is not None:
            input_["metadata"] = metadata
        if parameters is not None:
            input_["parameters"] = parameters
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

    async def get_notebook_run(
        self,
        domain_identifier: "capo_datazone.types.domain_id.DomainId",
        identifier: "capo_datazone.types.notebook_run_id.NotebookRunId",
        *,
        config_overrides: Optional[AsyncDataZoneClientConfig] = None,
    ) -> "capo_datazone.types.get_notebook_run_output.GetNotebookRunOutput":
        """<p>Gets the details of a <a href="https://docs.aws.amazon.com/sagemaker-unified-studio/latest/userguide/notebooks.html">notebook run</a> in Amazon SageMaker Unified Studio.</p>

        Args:
            domain_identifier: <p>The identifier of the Amazon SageMaker Unified Studio domain in which the notebook run exists.</p>
            identifier: <p>The identifier of the notebook run.</p>

        Raises:
            capo_datazone.errors.access_denied_exception.AccessDeniedException: <p>You do not have sufficient access to perform this action.</p>
            capo_datazone.errors.throttling_exception.ThrottlingException: <p>The request was denied due to request throttling.</p>
            capo_datazone.errors.unauthorized_exception.UnauthorizedException: <p>You do not have permission to perform this action.</p>
            capo_datazone.errors.internal_server_exception.InternalServerException: <p>The request has failed because of an unknown error, exception or failure.</p>
            capo_datazone.errors.resource_not_found_exception.ResourceNotFoundException: <p>The specified resource cannot be found.</p>
            capo_datazone.errors.validation_exception.ValidationException: <p>The input fails to satisfy the constraints specified by the Amazon Web Services service.</p>
            capo_datazone.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        async def _handler(
            req: "AsyncOperationRequest[capo_datazone.types.get_notebook_run_input.GetNotebookRunInput]",
        ) -> AsyncOperationResponse[
            "capo_datazone.types.get_notebook_run_output.GetNotebookRunOutput"
        ]:
            import capo_datazone._operations.data_zone.get_notebook_run

            (
                output,
                http_response,
            ) = await capo_datazone._operations.data_zone.get_notebook_run.async_get_notebook_run(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_datazone.types.get_notebook_run_input.GetNotebookRunInput = {
            "domain_identifier": domain_identifier,
            "identifier": identifier,
        }

        response = await aexecute_pipeline(
            AsyncOperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        await response.response.aclose()
        return response.output

    async def list_notebook_runs(
        self,
        domain_identifier: "capo_datazone.types.domain_id.DomainId",
        owning_project_identifier: "capo_datazone.types.project_id.ProjectId",
        *,
        config_overrides: Optional[AsyncDataZoneClientConfig] = None,
        notebook_identifier: Optional[
            "capo_datazone.types.notebook_id.NotebookId"
        ] = None,
        status: Optional[
            "capo_datazone.types.notebook_run_status.NotebookRunStatus"
        ] = None,
        schedule_identifier: Optional[
            "capo_datazone.types.schedule_id.ScheduleId"
        ] = None,
        max_results: Optional["capo_datazone.types.max_results.MaxResults"] = None,
        sort_order: Optional["capo_datazone.types.sort_order.SortOrder"] = None,
        next_token: Optional[
            "capo_datazone.types.pagination_token.PaginationToken"
        ] = None,
    ) -> "capo_datazone.types.list_notebook_runs_output.ListNotebookRunsOutput":
        """<p>Lists <a href="https://docs.aws.amazon.com/sagemaker-unified-studio/latest/userguide/notebooks.html">notebook runs</a> in Amazon SageMaker Unified Studio.</p>

        Args:
            domain_identifier: <p>The identifier of the Amazon SageMaker Unified Studio domain in which to list notebook runs.</p>
            owning_project_identifier: <p>The identifier of the project that owns the notebook runs.</p>
            notebook_identifier: <p>The identifier of the notebook to filter runs by.</p>
            status: <p>The status to filter notebook runs by.</p>
            schedule_identifier: <p>The identifier of the schedule to filter notebook runs by.</p>
            max_results: <p>The maximum number of notebook runs to return in a single call. When the number of notebook runs exceeds the value of <code>MaxResults</code>, the response contains a <code>NextToken</code> value.</p>
            sort_order: <p>The sort order for the results.</p>
            next_token: <p>When the number of notebook runs is greater than the default value for the <code>MaxResults</code> parameter, or if you explicitly specify a value for <code>MaxResults</code> that is less than the number of notebook runs, the response includes a pagination token named <code>NextToken</code>. You can specify this <code>NextToken</code> value in a subsequent call to <code>ListNotebookRuns</code> to list the next set of notebook runs.</p>

        Raises:
            capo_datazone.errors.access_denied_exception.AccessDeniedException: <p>You do not have sufficient access to perform this action.</p>
            capo_datazone.errors.throttling_exception.ThrottlingException: <p>The request was denied due to request throttling.</p>
            capo_datazone.errors.unauthorized_exception.UnauthorizedException: <p>You do not have permission to perform this action.</p>
            capo_datazone.errors.internal_server_exception.InternalServerException: <p>The request has failed because of an unknown error, exception or failure.</p>
            capo_datazone.errors.validation_exception.ValidationException: <p>The input fails to satisfy the constraints specified by the Amazon Web Services service.</p>
            capo_datazone.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        async def _handler(
            req: "AsyncOperationRequest[capo_datazone.types.list_notebook_runs_input.ListNotebookRunsInput]",
        ) -> AsyncOperationResponse[
            "capo_datazone.types.list_notebook_runs_output.ListNotebookRunsOutput"
        ]:
            import capo_datazone._operations.data_zone.list_notebook_runs

            (
                output,
                http_response,
            ) = await capo_datazone._operations.data_zone.list_notebook_runs.async_list_notebook_runs(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_datazone.types.list_notebook_runs_input.ListNotebookRunsInput = {
            "domain_identifier": domain_identifier,
            "owning_project_identifier": owning_project_identifier,
        }
        if notebook_identifier is not None:
            input_["notebook_identifier"] = notebook_identifier
        if status is not None:
            input_["status"] = status
        if schedule_identifier is not None:
            input_["schedule_identifier"] = schedule_identifier
        if max_results is not None:
            input_["max_results"] = max_results
        if sort_order is not None:
            input_["sort_order"] = sort_order
        if next_token is not None:
            input_["next_token"] = next_token

        response = await aexecute_pipeline(
            AsyncOperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        await response.response.aclose()
        return response.output

    async def iter_list_notebook_runs(
        self,
        domain_identifier: "capo_datazone.types.domain_id.DomainId",
        owning_project_identifier: "capo_datazone.types.project_id.ProjectId",
        *,
        config_overrides: Optional[AsyncDataZoneClientConfig] = None,
        notebook_identifier: Optional[
            "capo_datazone.types.notebook_id.NotebookId"
        ] = None,
        status: Optional[
            "capo_datazone.types.notebook_run_status.NotebookRunStatus"
        ] = None,
        schedule_identifier: Optional[
            "capo_datazone.types.schedule_id.ScheduleId"
        ] = None,
        max_results: Optional["capo_datazone.types.max_results.MaxResults"] = None,
        sort_order: Optional["capo_datazone.types.sort_order.SortOrder"] = None,
        next_token: Optional[
            "capo_datazone.types.pagination_token.PaginationToken"
        ] = None,
    ) -> "AsyncIterator[capo_datazone.types.notebook_run_summary.NotebookRunSummary]":
        _token = next_token
        while True:
            _response = await self.list_notebook_runs(
                domain_identifier,
                owning_project_identifier,
                config_overrides=config_overrides,
                notebook_identifier=notebook_identifier,
                status=status,
                schedule_identifier=schedule_identifier,
                max_results=max_results,
                sort_order=sort_order,
                next_token=_token,
            )
            _page = _resolve_path(_response, ("items",))
            for _item in _page or []:
                yield _item
            _token = _resolve_path(_response, ("next_token",))
            if not _token:
                break

    async def stop_notebook_run(
        self,
        domain_identifier: "capo_datazone.types.domain_id.DomainId",
        identifier: "capo_datazone.types.notebook_run_id.NotebookRunId",
        *,
        config_overrides: Optional[AsyncDataZoneClientConfig] = None,
        client_token: Optional["capo_datazone.types.client_token.ClientToken"] = None,
    ) -> "capo_datazone.types.stop_notebook_run_output.StopNotebookRunOutput":
        """<p>Stops a running <a href="https://docs.aws.amazon.com/sagemaker-unified-studio/latest/userguide/notebooks.html">notebook run</a> in Amazon SageMaker Unified Studio.</p>

        Args:
            domain_identifier: <p>The identifier of the Amazon SageMaker Unified Studio domain in which the notebook run is stopped.</p>
            identifier: <p>The identifier of the notebook run to stop.</p>
            client_token: <p>A unique, case-sensitive identifier to ensure idempotency of the request. This field is automatically populated if not provided.</p>

        Raises:
            capo_datazone.errors.access_denied_exception.AccessDeniedException: <p>You do not have sufficient access to perform this action.</p>
            capo_datazone.errors.throttling_exception.ThrottlingException: <p>The request was denied due to request throttling.</p>
            capo_datazone.errors.unauthorized_exception.UnauthorizedException: <p>You do not have permission to perform this action.</p>
            capo_datazone.errors.conflict_exception.ConflictException: <p>There is a conflict while performing this action.</p>
            capo_datazone.errors.internal_server_exception.InternalServerException: <p>The request has failed because of an unknown error, exception or failure.</p>
            capo_datazone.errors.resource_not_found_exception.ResourceNotFoundException: <p>The specified resource cannot be found.</p>
            capo_datazone.errors.validation_exception.ValidationException: <p>The input fails to satisfy the constraints specified by the Amazon Web Services service.</p>
            capo_datazone.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        async def _handler(
            req: "AsyncOperationRequest[capo_datazone.types.stop_notebook_run_input.StopNotebookRunInput]",
        ) -> AsyncOperationResponse[
            "capo_datazone.types.stop_notebook_run_output.StopNotebookRunOutput"
        ]:
            import capo_datazone._operations.data_zone.stop_notebook_run

            (
                output,
                http_response,
            ) = await capo_datazone._operations.data_zone.stop_notebook_run.async_stop_notebook_run(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_datazone.types.stop_notebook_run_input.StopNotebookRunInput = {
            "domain_identifier": domain_identifier,
            "identifier": identifier,
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

    async def create_rule(
        self,
        domain_identifier: "capo_datazone.types.domain_id.DomainId",
        name: "capo_datazone.types.rule_name.RuleName",
        target: "capo_datazone.types.rule_target.RuleTarget",
        action: "capo_datazone.types.rule_action.RuleAction",
        scope: "capo_datazone.types.rule_scope.RuleScope",
        detail: "capo_datazone.types.rule_detail.RuleDetail",
        *,
        config_overrides: Optional[AsyncDataZoneClientConfig] = None,
        description: Optional["capo_datazone.types.description.Description"] = None,
        client_token: Optional["capo_datazone.types.client_token.ClientToken"] = None,
    ) -> "capo_datazone.types.create_rule_output.CreateRuleOutput":
        """<p>Creates a rule in Amazon DataZone. A rule is a formal agreement that enforces specific requirements across user workflows (e.g., publishing assets to the catalog, requesting subscriptions, creating projects) within the Amazon DataZone data portal. These rules help maintain consistency, ensure compliance, and uphold governance standards in data management processes. For instance, a metadata enforcement rule can specify the required information for creating a subscription request or publishing a data asset to the catalog, ensuring alignment with organizational standards.</p>

        Args:
            domain_identifier: <p>The ID of the domain where the rule is created.</p>
            name: <p>The name of the rule.</p>
            target: <p>The target of the rule.</p>
            action: <p>The action of the rule.</p>
            scope: <p>The scope of the rule.</p>
            detail: <p>The detail of the rule.</p>
            description: <p>The description of the rule.</p>
            client_token: <p>A unique, case-sensitive identifier that is provided to ensure the idempotency of the request.</p>

        Raises:
            capo_datazone.errors.access_denied_exception.AccessDeniedException: <p>You do not have sufficient access to perform this action.</p>
            capo_datazone.errors.throttling_exception.ThrottlingException: <p>The request was denied due to request throttling.</p>
            capo_datazone.errors.unauthorized_exception.UnauthorizedException: <p>You do not have permission to perform this action.</p>
            capo_datazone.errors.conflict_exception.ConflictException: <p>There is a conflict while performing this action.</p>
            capo_datazone.errors.internal_server_exception.InternalServerException: <p>The request has failed because of an unknown error, exception or failure.</p>
            capo_datazone.errors.resource_not_found_exception.ResourceNotFoundException: <p>The specified resource cannot be found.</p>
            capo_datazone.errors.service_quota_exceeded_exception.ServiceQuotaExceededException: <p>The request has exceeded the specified service quota.</p>
            capo_datazone.errors.validation_exception.ValidationException: <p>The input fails to satisfy the constraints specified by the Amazon Web Services service.</p>
            capo_datazone.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        async def _handler(
            req: "AsyncOperationRequest[capo_datazone.types.create_rule_input.CreateRuleInput]",
        ) -> AsyncOperationResponse[
            "capo_datazone.types.create_rule_output.CreateRuleOutput"
        ]:
            import capo_datazone._operations.data_zone.create_rule

            (
                output,
                http_response,
            ) = await capo_datazone._operations.data_zone.create_rule.async_create_rule(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_datazone.types.create_rule_input.CreateRuleInput = {
            "domain_identifier": domain_identifier,
            "name": name,
            "target": target,
            "action": action,
            "scope": scope,
            "detail": detail,
        }
        if description is not None:
            input_["description"] = description
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

    async def get_rule(
        self,
        domain_identifier: "capo_datazone.types.domain_id.DomainId",
        identifier: "capo_datazone.types.rule_id.RuleId",
        *,
        config_overrides: Optional[AsyncDataZoneClientConfig] = None,
        revision: Optional["capo_datazone.types.revision.Revision"] = None,
    ) -> "capo_datazone.types.get_rule_output.GetRuleOutput":
        """<p>Gets the details of a rule in Amazon DataZone. A rule is a formal agreement that enforces specific requirements across user workflows (e.g., publishing assets to the catalog, requesting subscriptions, creating projects) within the Amazon DataZone data portal. These rules help maintain consistency, ensure compliance, and uphold governance standards in data management processes. For instance, a metadata enforcement rule can specify the required information for creating a subscription request or publishing a data asset to the catalog, ensuring alignment with organizational standards.</p>

        Args:
            domain_identifier: <p>The ID of the domain where the <code>GetRule</code> action is to be invoked.</p>
            identifier: <p>The ID of the rule.</p>
            revision: <p>The revision of the rule.</p>

        Raises:
            capo_datazone.errors.access_denied_exception.AccessDeniedException: <p>You do not have sufficient access to perform this action.</p>
            capo_datazone.errors.throttling_exception.ThrottlingException: <p>The request was denied due to request throttling.</p>
            capo_datazone.errors.unauthorized_exception.UnauthorizedException: <p>You do not have permission to perform this action.</p>
            capo_datazone.errors.internal_server_exception.InternalServerException: <p>The request has failed because of an unknown error, exception or failure.</p>
            capo_datazone.errors.resource_not_found_exception.ResourceNotFoundException: <p>The specified resource cannot be found.</p>
            capo_datazone.errors.validation_exception.ValidationException: <p>The input fails to satisfy the constraints specified by the Amazon Web Services service.</p>
            capo_datazone.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        async def _handler(
            req: "AsyncOperationRequest[capo_datazone.types.get_rule_input.GetRuleInput]",
        ) -> AsyncOperationResponse[
            "capo_datazone.types.get_rule_output.GetRuleOutput"
        ]:
            import capo_datazone._operations.data_zone.get_rule

            (
                output,
                http_response,
            ) = await capo_datazone._operations.data_zone.get_rule.async_get_rule(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_datazone.types.get_rule_input.GetRuleInput = {
            "domain_identifier": domain_identifier,
            "identifier": identifier,
        }
        if revision is not None:
            input_["revision"] = revision

        response = await aexecute_pipeline(
            AsyncOperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        await response.response.aclose()
        return response.output

    async def update_rule(
        self,
        domain_identifier: "capo_datazone.types.domain_id.DomainId",
        identifier: "capo_datazone.types.rule_id.RuleId",
        *,
        config_overrides: Optional[AsyncDataZoneClientConfig] = None,
        name: Optional["capo_datazone.types.rule_name.RuleName"] = None,
        description: Optional["capo_datazone.types.description.Description"] = None,
        scope: Optional["capo_datazone.types.rule_scope.RuleScope"] = None,
        detail: Optional["capo_datazone.types.rule_detail.RuleDetail"] = None,
        include_child_domain_units: Optional[bool] = None,
    ) -> "capo_datazone.types.update_rule_output.UpdateRuleOutput":
        """<p>Updates a rule. In Amazon DataZone, a rule is a formal agreement that enforces specific requirements across user workflows (e.g., publishing assets to the catalog, requesting subscriptions, creating projects) within the Amazon DataZone data portal. These rules help maintain consistency, ensure compliance, and uphold governance standards in data management processes. For instance, a metadata enforcement rule can specify the required information for creating a subscription request or publishing a data asset to the catalog, ensuring alignment with organizational standards.</p>

        Args:
            domain_identifier: <p>The ID of the domain in which a rule is to be updated.</p>
            identifier: <p>The ID of the rule that is to be updated</p>
            name: <p>The name of the rule.</p>
            description: <p>The description of the rule.</p>
            scope: <p>The scrope of the rule.</p>
            detail: <p>The detail of the rule.</p>
            include_child_domain_units: <p>Specifies whether to update this rule in the child domain units.</p>

        Raises:
            capo_datazone.errors.access_denied_exception.AccessDeniedException: <p>You do not have sufficient access to perform this action.</p>
            capo_datazone.errors.throttling_exception.ThrottlingException: <p>The request was denied due to request throttling.</p>
            capo_datazone.errors.unauthorized_exception.UnauthorizedException: <p>You do not have permission to perform this action.</p>
            capo_datazone.errors.conflict_exception.ConflictException: <p>There is a conflict while performing this action.</p>
            capo_datazone.errors.internal_server_exception.InternalServerException: <p>The request has failed because of an unknown error, exception or failure.</p>
            capo_datazone.errors.resource_not_found_exception.ResourceNotFoundException: <p>The specified resource cannot be found.</p>
            capo_datazone.errors.service_quota_exceeded_exception.ServiceQuotaExceededException: <p>The request has exceeded the specified service quota.</p>
            capo_datazone.errors.validation_exception.ValidationException: <p>The input fails to satisfy the constraints specified by the Amazon Web Services service.</p>
            capo_datazone.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        async def _handler(
            req: "AsyncOperationRequest[capo_datazone.types.update_rule_input.UpdateRuleInput]",
        ) -> AsyncOperationResponse[
            "capo_datazone.types.update_rule_output.UpdateRuleOutput"
        ]:
            import capo_datazone._operations.data_zone.update_rule

            (
                output,
                http_response,
            ) = await capo_datazone._operations.data_zone.update_rule.async_update_rule(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_datazone.types.update_rule_input.UpdateRuleInput = {
            "domain_identifier": domain_identifier,
            "identifier": identifier,
        }
        if name is not None:
            input_["name"] = name
        if description is not None:
            input_["description"] = description
        if scope is not None:
            input_["scope"] = scope
        if detail is not None:
            input_["detail"] = detail
        if include_child_domain_units is not None:
            input_["include_child_domain_units"] = include_child_domain_units

        response = await aexecute_pipeline(
            AsyncOperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        await response.response.aclose()
        return response.output

    async def delete_rule(
        self,
        domain_identifier: "capo_datazone.types.domain_id.DomainId",
        identifier: "capo_datazone.types.rule_id.RuleId",
        *,
        config_overrides: Optional[AsyncDataZoneClientConfig] = None,
    ) -> "capo_datazone.types.delete_rule_output.DeleteRuleOutput":
        """<p>Deletes a rule in Amazon DataZone. A rule is a formal agreement that enforces specific requirements across user workflows (e.g., publishing assets to the catalog, requesting subscriptions, creating projects) within the Amazon DataZone data portal. These rules help maintain consistency, ensure compliance, and uphold governance standards in data management processes. For instance, a metadata enforcement rule can specify the required information for creating a subscription request or publishing a data asset to the catalog, ensuring alignment with organizational standards.</p>

        Args:
            domain_identifier: <p>The ID of the domain that where the rule is to be deleted.</p>
            identifier: <p>The ID of the rule that is to be deleted.</p>

        Raises:
            capo_datazone.errors.access_denied_exception.AccessDeniedException: <p>You do not have sufficient access to perform this action.</p>
            capo_datazone.errors.throttling_exception.ThrottlingException: <p>The request was denied due to request throttling.</p>
            capo_datazone.errors.unauthorized_exception.UnauthorizedException: <p>You do not have permission to perform this action.</p>
            capo_datazone.errors.conflict_exception.ConflictException: <p>There is a conflict while performing this action.</p>
            capo_datazone.errors.internal_server_exception.InternalServerException: <p>The request has failed because of an unknown error, exception or failure.</p>
            capo_datazone.errors.resource_not_found_exception.ResourceNotFoundException: <p>The specified resource cannot be found.</p>
            capo_datazone.errors.validation_exception.ValidationException: <p>The input fails to satisfy the constraints specified by the Amazon Web Services service.</p>
            capo_datazone.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        async def _handler(
            req: "AsyncOperationRequest[capo_datazone.types.delete_rule_input.DeleteRuleInput]",
        ) -> AsyncOperationResponse[
            "capo_datazone.types.delete_rule_output.DeleteRuleOutput"
        ]:
            import capo_datazone._operations.data_zone.delete_rule

            (
                output,
                http_response,
            ) = await capo_datazone._operations.data_zone.delete_rule.async_delete_rule(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_datazone.types.delete_rule_input.DeleteRuleInput = {
            "domain_identifier": domain_identifier,
            "identifier": identifier,
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
        domain_identifier: "capo_datazone.types.domain_id.DomainId",
        target_type: "capo_datazone.types.rule_target_type.RuleTargetType",
        target_identifier: str,
        *,
        config_overrides: Optional[AsyncDataZoneClientConfig] = None,
        rule_type: Optional["capo_datazone.types.rule_type.RuleType"] = None,
        action: Optional["capo_datazone.types.rule_action.RuleAction"] = None,
        project_ids: Optional["capo_datazone.types.project_ids.ProjectIds"] = None,
        asset_types: Optional[
            "capo_datazone.types.asset_type_identifiers.AssetTypeIdentifiers"
        ] = None,
        data_product: Optional[bool] = None,
        include_cascaded: Optional[bool] = None,
        max_results: Optional[int] = None,
        next_token: Optional[
            "capo_datazone.types.pagination_token.PaginationToken"
        ] = None,
    ) -> "capo_datazone.types.list_rules_output.ListRulesOutput":
        """<p>Lists existing rules. In Amazon DataZone, a rule is a formal agreement that enforces specific requirements across user workflows (e.g., publishing assets to the catalog, requesting subscriptions, creating projects) within the Amazon DataZone data portal. These rules help maintain consistency, ensure compliance, and uphold governance standards in data management processes. For instance, a metadata enforcement rule can specify the required information for creating a subscription request or publishing a data asset to the catalog, ensuring alignment with organizational standards.</p>

        Args:
            domain_identifier: <p>The ID of the domain in which the rules are to be listed.</p>
            target_type: <p>The target type of the rule.</p>
            target_identifier: <p>The target ID of the rule.</p>
            rule_type: <p>The type of the rule.</p>
            action: <p>The action of the rule.</p>
            project_ids: <p>The IDs of projects in which rules are to be listed.</p>
            asset_types: <p>The asset types of the rule.</p>
            data_product: <p>The data product of the rule.</p>
            include_cascaded: <p>Specifies whether to include cascading rules in the results.</p>
            max_results: <p>The maximum number of rules to return in a single call to <code>ListRules</code>. When the number of rules to be listed is greater than the value of <code>MaxResults</code>, the response contains a <code>NextToken</code> value that you can use in a subsequent call to <code>ListRules</code> to list the next set of rules.</p>
            next_token: <p>When the number of rules is greater than the default value for the <code>MaxResults</code> parameter, or if you explicitly specify a value for <code>MaxResults</code> that is less than the number of rules, the response includes a pagination token named <code>NextToken</code>. You can specify this <code>NextToken</code> value in a subsequent call to <code>ListRules</code> to list the next set of rules.</p>

        Raises:
            capo_datazone.errors.access_denied_exception.AccessDeniedException: <p>You do not have sufficient access to perform this action.</p>
            capo_datazone.errors.throttling_exception.ThrottlingException: <p>The request was denied due to request throttling.</p>
            capo_datazone.errors.unauthorized_exception.UnauthorizedException: <p>You do not have permission to perform this action.</p>
            capo_datazone.errors.internal_server_exception.InternalServerException: <p>The request has failed because of an unknown error, exception or failure.</p>
            capo_datazone.errors.resource_not_found_exception.ResourceNotFoundException: <p>The specified resource cannot be found.</p>
            capo_datazone.errors.validation_exception.ValidationException: <p>The input fails to satisfy the constraints specified by the Amazon Web Services service.</p>
            capo_datazone.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        async def _handler(
            req: "AsyncOperationRequest[capo_datazone.types.list_rules_input.ListRulesInput]",
        ) -> AsyncOperationResponse[
            "capo_datazone.types.list_rules_output.ListRulesOutput"
        ]:
            import capo_datazone._operations.data_zone.list_rules

            (
                output,
                http_response,
            ) = await capo_datazone._operations.data_zone.list_rules.async_list_rules(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_datazone.types.list_rules_input.ListRulesInput = {
            "domain_identifier": domain_identifier,
            "target_type": target_type,
            "target_identifier": target_identifier,
        }
        if rule_type is not None:
            input_["rule_type"] = rule_type
        if action is not None:
            input_["action"] = action
        if project_ids is not None:
            input_["project_ids"] = project_ids
        if asset_types is not None:
            input_["asset_types"] = asset_types
        if data_product is not None:
            input_["data_product"] = data_product
        if include_cascaded is not None:
            input_["include_cascaded"] = include_cascaded
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

    async def iter_list_rules(
        self,
        domain_identifier: "capo_datazone.types.domain_id.DomainId",
        target_type: "capo_datazone.types.rule_target_type.RuleTargetType",
        target_identifier: str,
        *,
        config_overrides: Optional[AsyncDataZoneClientConfig] = None,
        rule_type: Optional["capo_datazone.types.rule_type.RuleType"] = None,
        action: Optional["capo_datazone.types.rule_action.RuleAction"] = None,
        project_ids: Optional["capo_datazone.types.project_ids.ProjectIds"] = None,
        asset_types: Optional[
            "capo_datazone.types.asset_type_identifiers.AssetTypeIdentifiers"
        ] = None,
        data_product: Optional[bool] = None,
        include_cascaded: Optional[bool] = None,
        max_results: Optional[int] = None,
        next_token: Optional[
            "capo_datazone.types.pagination_token.PaginationToken"
        ] = None,
    ) -> "AsyncIterator[capo_datazone.types.rule_summary.RuleSummary]":
        _token = next_token
        while True:
            _response = await self.list_rules(
                domain_identifier,
                target_type,
                target_identifier,
                config_overrides=config_overrides,
                rule_type=rule_type,
                action=action,
                project_ids=project_ids,
                asset_types=asset_types,
                data_product=data_product,
                include_cascaded=include_cascaded,
                max_results=max_results,
                next_token=_token,
            )
            _page = _resolve_path(_response, ("items",))
            for _item in _page or []:
                yield _item
            _token = _resolve_path(_response, ("next_token",))
            if not _token:
                break

    async def __aenter__(self) -> Self:
        return self

    async def __aexit__(self, exc_type: Any, exc: Any, tb: Any):
        await self._client.aclose()
