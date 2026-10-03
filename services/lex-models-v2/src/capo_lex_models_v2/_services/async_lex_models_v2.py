"""Generated from Smithy shape ``com.amazonaws.lexmodelsv2#LexModelBuildingServiceV2``."""

import warnings
from collections.abc import AsyncIterator
from typing import TYPE_CHECKING, Any, Iterable, Optional

from typing_extensions import Self, TypedDict
from zapros import AsyncBaseHandler, AsyncClient

import capo_lex_models_v2._auth._signers
import capo_lex_models_v2._auth._sigv4
from capo_lex_models_v2._auth._identity import Credentials
from capo_lex_models_v2._auth._providers import (
    CredentialsProvider,
    IdentityProvider,
    StaticAwsCredentialsProvider,
    default_aws_credentials_chain,
)
from capo_lex_models_v2._auth._zapros_handler import AuthMiddleware
from capo_lex_models_v2._pagination import resolve_path as _resolve_path
from capo_lex_models_v2._services._aws_config import aaws_config
from capo_lex_models_v2._services._pipeline import (
    AsyncInterceptor,
    AsyncOperationOptions,
    AsyncOperationRequest,
    AsyncOperationResponse,
    aexecute_pipeline,
    aretry,
)

if TYPE_CHECKING:
    import capo_lex_models_v2.types.aggregated_utterances_filters
    import capo_lex_models_v2.types.aggregated_utterances_sort_by
    import capo_lex_models_v2.types.amazon_resource_name
    import capo_lex_models_v2.types.analysis_scope
    import capo_lex_models_v2.types.analytics_bin_by_list
    import capo_lex_models_v2.types.analytics_intent_filters
    import capo_lex_models_v2.types.analytics_intent_group_by_list
    import capo_lex_models_v2.types.analytics_intent_metrics
    import capo_lex_models_v2.types.analytics_intent_stage_filters
    import capo_lex_models_v2.types.analytics_intent_stage_group_by_list
    import capo_lex_models_v2.types.analytics_intent_stage_metrics
    import capo_lex_models_v2.types.analytics_path
    import capo_lex_models_v2.types.analytics_path_filters
    import capo_lex_models_v2.types.analytics_session_filters
    import capo_lex_models_v2.types.analytics_session_group_by_list
    import capo_lex_models_v2.types.analytics_session_metrics
    import capo_lex_models_v2.types.analytics_utterance_attributes
    import capo_lex_models_v2.types.analytics_utterance_filters
    import capo_lex_models_v2.types.analytics_utterance_group_by_list
    import capo_lex_models_v2.types.analytics_utterance_metrics
    import capo_lex_models_v2.types.associated_transcript_filters
    import capo_lex_models_v2.types.audio_filler_settings
    import capo_lex_models_v2.types.batch_create_custom_vocabulary_item_request
    import capo_lex_models_v2.types.batch_create_custom_vocabulary_item_response
    import capo_lex_models_v2.types.batch_delete_custom_vocabulary_item_request
    import capo_lex_models_v2.types.batch_delete_custom_vocabulary_item_response
    import capo_lex_models_v2.types.batch_update_custom_vocabulary_item_request
    import capo_lex_models_v2.types.batch_update_custom_vocabulary_item_response
    import capo_lex_models_v2.types.bot_alias_id
    import capo_lex_models_v2.types.bot_alias_locale_settings_map
    import capo_lex_models_v2.types.bot_analyzer_history_summary
    import capo_lex_models_v2.types.bot_analyzer_recommendation
    import capo_lex_models_v2.types.bot_filters
    import capo_lex_models_v2.types.bot_locale_filters
    import capo_lex_models_v2.types.bot_locale_sort_by
    import capo_lex_models_v2.types.bot_members
    import capo_lex_models_v2.types.bot_sort_by
    import capo_lex_models_v2.types.bot_type
    import capo_lex_models_v2.types.bot_version
    import capo_lex_models_v2.types.bot_version_locale_specification
    import capo_lex_models_v2.types.bot_version_replica_sort_by
    import capo_lex_models_v2.types.bot_version_sort_by
    import capo_lex_models_v2.types.build_bot_locale_request
    import capo_lex_models_v2.types.build_bot_locale_response
    import capo_lex_models_v2.types.built_in_intent_sort_by
    import capo_lex_models_v2.types.built_in_or_custom_slot_type_id
    import capo_lex_models_v2.types.built_in_slot_type_sort_by
    import capo_lex_models_v2.types.built_ins_max_results
    import capo_lex_models_v2.types.composite_slot_type_setting
    import capo_lex_models_v2.types.condition_map
    import capo_lex_models_v2.types.confidence_threshold
    import capo_lex_models_v2.types.conversation_log_settings
    import capo_lex_models_v2.types.create_bot_alias_request
    import capo_lex_models_v2.types.create_bot_alias_response
    import capo_lex_models_v2.types.create_bot_locale_request
    import capo_lex_models_v2.types.create_bot_locale_response
    import capo_lex_models_v2.types.create_bot_replica_request
    import capo_lex_models_v2.types.create_bot_replica_response
    import capo_lex_models_v2.types.create_bot_request
    import capo_lex_models_v2.types.create_bot_response
    import capo_lex_models_v2.types.create_bot_version_request
    import capo_lex_models_v2.types.create_bot_version_response
    import capo_lex_models_v2.types.create_custom_vocabulary_items_list
    import capo_lex_models_v2.types.create_export_request
    import capo_lex_models_v2.types.create_export_response
    import capo_lex_models_v2.types.create_intent_request
    import capo_lex_models_v2.types.create_intent_response
    import capo_lex_models_v2.types.create_resource_policy_request
    import capo_lex_models_v2.types.create_resource_policy_response
    import capo_lex_models_v2.types.create_resource_policy_statement_request
    import capo_lex_models_v2.types.create_resource_policy_statement_response
    import capo_lex_models_v2.types.create_slot_request
    import capo_lex_models_v2.types.create_slot_response
    import capo_lex_models_v2.types.create_slot_type_request
    import capo_lex_models_v2.types.create_slot_type_response
    import capo_lex_models_v2.types.create_test_set_discrepancy_report_request
    import capo_lex_models_v2.types.create_test_set_discrepancy_report_response
    import capo_lex_models_v2.types.create_upload_url_request
    import capo_lex_models_v2.types.create_upload_url_response
    import capo_lex_models_v2.types.data_privacy
    import capo_lex_models_v2.types.delete_bot_alias_request
    import capo_lex_models_v2.types.delete_bot_alias_response
    import capo_lex_models_v2.types.delete_bot_analyzer_recommendation_request
    import capo_lex_models_v2.types.delete_bot_analyzer_recommendation_response
    import capo_lex_models_v2.types.delete_bot_locale_request
    import capo_lex_models_v2.types.delete_bot_locale_response
    import capo_lex_models_v2.types.delete_bot_replica_request
    import capo_lex_models_v2.types.delete_bot_replica_response
    import capo_lex_models_v2.types.delete_bot_request
    import capo_lex_models_v2.types.delete_bot_response
    import capo_lex_models_v2.types.delete_bot_version_request
    import capo_lex_models_v2.types.delete_bot_version_response
    import capo_lex_models_v2.types.delete_custom_vocabulary_items_list
    import capo_lex_models_v2.types.delete_custom_vocabulary_request
    import capo_lex_models_v2.types.delete_custom_vocabulary_response
    import capo_lex_models_v2.types.delete_export_request
    import capo_lex_models_v2.types.delete_export_response
    import capo_lex_models_v2.types.delete_import_request
    import capo_lex_models_v2.types.delete_import_response
    import capo_lex_models_v2.types.delete_intent_request
    import capo_lex_models_v2.types.delete_resource_policy_request
    import capo_lex_models_v2.types.delete_resource_policy_response
    import capo_lex_models_v2.types.delete_resource_policy_statement_request
    import capo_lex_models_v2.types.delete_resource_policy_statement_response
    import capo_lex_models_v2.types.delete_slot_request
    import capo_lex_models_v2.types.delete_slot_type_request
    import capo_lex_models_v2.types.delete_test_set_request
    import capo_lex_models_v2.types.delete_utterances_request
    import capo_lex_models_v2.types.delete_utterances_response
    import capo_lex_models_v2.types.describe_bot_alias_request
    import capo_lex_models_v2.types.describe_bot_alias_response
    import capo_lex_models_v2.types.describe_bot_analyzer_recommendation_request
    import capo_lex_models_v2.types.describe_bot_analyzer_recommendation_response
    import capo_lex_models_v2.types.describe_bot_locale_request
    import capo_lex_models_v2.types.describe_bot_locale_response
    import capo_lex_models_v2.types.describe_bot_recommendation_request
    import capo_lex_models_v2.types.describe_bot_recommendation_response
    import capo_lex_models_v2.types.describe_bot_replica_request
    import capo_lex_models_v2.types.describe_bot_replica_response
    import capo_lex_models_v2.types.describe_bot_request
    import capo_lex_models_v2.types.describe_bot_resource_generation_request
    import capo_lex_models_v2.types.describe_bot_resource_generation_response
    import capo_lex_models_v2.types.describe_bot_response
    import capo_lex_models_v2.types.describe_bot_version_request
    import capo_lex_models_v2.types.describe_bot_version_response
    import capo_lex_models_v2.types.describe_custom_vocabulary_metadata_request
    import capo_lex_models_v2.types.describe_custom_vocabulary_metadata_response
    import capo_lex_models_v2.types.describe_export_request
    import capo_lex_models_v2.types.describe_export_response
    import capo_lex_models_v2.types.describe_import_request
    import capo_lex_models_v2.types.describe_import_response
    import capo_lex_models_v2.types.describe_intent_request
    import capo_lex_models_v2.types.describe_intent_response
    import capo_lex_models_v2.types.describe_resource_policy_request
    import capo_lex_models_v2.types.describe_resource_policy_response
    import capo_lex_models_v2.types.describe_slot_request
    import capo_lex_models_v2.types.describe_slot_response
    import capo_lex_models_v2.types.describe_slot_type_request
    import capo_lex_models_v2.types.describe_slot_type_response
    import capo_lex_models_v2.types.describe_test_execution_request
    import capo_lex_models_v2.types.describe_test_execution_response
    import capo_lex_models_v2.types.describe_test_set_discrepancy_report_request
    import capo_lex_models_v2.types.describe_test_set_discrepancy_report_response
    import capo_lex_models_v2.types.describe_test_set_generation_request
    import capo_lex_models_v2.types.describe_test_set_generation_response
    import capo_lex_models_v2.types.describe_test_set_request
    import capo_lex_models_v2.types.describe_test_set_response
    import capo_lex_models_v2.types.description
    import capo_lex_models_v2.types.dialog_code_hook_settings
    import capo_lex_models_v2.types.display_name
    import capo_lex_models_v2.types.draft_bot_version
    import capo_lex_models_v2.types.effect
    import capo_lex_models_v2.types.encryption_setting
    import capo_lex_models_v2.types.error_log_settings
    import capo_lex_models_v2.types.export_filters
    import capo_lex_models_v2.types.export_resource_specification
    import capo_lex_models_v2.types.export_sort_by
    import capo_lex_models_v2.types.external_source_setting
    import capo_lex_models_v2.types.fulfillment_code_hook_settings
    import capo_lex_models_v2.types.generate_bot_element_request
    import capo_lex_models_v2.types.generate_bot_element_response
    import capo_lex_models_v2.types.generation_input
    import capo_lex_models_v2.types.generation_sort_by
    import capo_lex_models_v2.types.generative_ai_settings
    import capo_lex_models_v2.types.get_test_execution_artifacts_url_request
    import capo_lex_models_v2.types.get_test_execution_artifacts_url_response
    import capo_lex_models_v2.types.id
    import capo_lex_models_v2.types.import_export_file_format
    import capo_lex_models_v2.types.import_export_file_password
    import capo_lex_models_v2.types.import_filters
    import capo_lex_models_v2.types.import_resource_specification
    import capo_lex_models_v2.types.import_sort_by
    import capo_lex_models_v2.types.initial_response_setting
    import capo_lex_models_v2.types.input_contexts_list
    import capo_lex_models_v2.types.intent_closing_setting
    import capo_lex_models_v2.types.intent_confirmation_setting
    import capo_lex_models_v2.types.intent_filters
    import capo_lex_models_v2.types.intent_signature
    import capo_lex_models_v2.types.intent_sort_by
    import capo_lex_models_v2.types.kendra_configuration
    import capo_lex_models_v2.types.list_aggregated_utterances_request
    import capo_lex_models_v2.types.list_aggregated_utterances_response
    import capo_lex_models_v2.types.list_bot_alias_replicas_request
    import capo_lex_models_v2.types.list_bot_alias_replicas_response
    import capo_lex_models_v2.types.list_bot_aliases_request
    import capo_lex_models_v2.types.list_bot_aliases_response
    import capo_lex_models_v2.types.list_bot_analyzer_history_request
    import capo_lex_models_v2.types.list_bot_analyzer_history_response
    import capo_lex_models_v2.types.list_bot_locales_request
    import capo_lex_models_v2.types.list_bot_locales_response
    import capo_lex_models_v2.types.list_bot_recommendations_request
    import capo_lex_models_v2.types.list_bot_recommendations_response
    import capo_lex_models_v2.types.list_bot_replicas_request
    import capo_lex_models_v2.types.list_bot_replicas_response
    import capo_lex_models_v2.types.list_bot_resource_generations_request
    import capo_lex_models_v2.types.list_bot_resource_generations_response
    import capo_lex_models_v2.types.list_bot_version_replicas_request
    import capo_lex_models_v2.types.list_bot_version_replicas_response
    import capo_lex_models_v2.types.list_bot_versions_request
    import capo_lex_models_v2.types.list_bot_versions_response
    import capo_lex_models_v2.types.list_bots_request
    import capo_lex_models_v2.types.list_bots_response
    import capo_lex_models_v2.types.list_built_in_intents_request
    import capo_lex_models_v2.types.list_built_in_intents_response
    import capo_lex_models_v2.types.list_built_in_slot_types_request
    import capo_lex_models_v2.types.list_built_in_slot_types_response
    import capo_lex_models_v2.types.list_custom_vocabulary_items_request
    import capo_lex_models_v2.types.list_custom_vocabulary_items_response
    import capo_lex_models_v2.types.list_exports_request
    import capo_lex_models_v2.types.list_exports_response
    import capo_lex_models_v2.types.list_imports_request
    import capo_lex_models_v2.types.list_imports_response
    import capo_lex_models_v2.types.list_intent_metrics_request
    import capo_lex_models_v2.types.list_intent_metrics_response
    import capo_lex_models_v2.types.list_intent_paths_request
    import capo_lex_models_v2.types.list_intent_paths_response
    import capo_lex_models_v2.types.list_intent_stage_metrics_request
    import capo_lex_models_v2.types.list_intent_stage_metrics_response
    import capo_lex_models_v2.types.list_intents_request
    import capo_lex_models_v2.types.list_intents_response
    import capo_lex_models_v2.types.list_recommended_intents_request
    import capo_lex_models_v2.types.list_recommended_intents_response
    import capo_lex_models_v2.types.list_session_analytics_data_request
    import capo_lex_models_v2.types.list_session_analytics_data_response
    import capo_lex_models_v2.types.list_session_metrics_request
    import capo_lex_models_v2.types.list_session_metrics_response
    import capo_lex_models_v2.types.list_slot_types_request
    import capo_lex_models_v2.types.list_slot_types_response
    import capo_lex_models_v2.types.list_slots_request
    import capo_lex_models_v2.types.list_slots_response
    import capo_lex_models_v2.types.list_tags_for_resource_request
    import capo_lex_models_v2.types.list_tags_for_resource_response
    import capo_lex_models_v2.types.list_test_execution_result_items_request
    import capo_lex_models_v2.types.list_test_execution_result_items_response
    import capo_lex_models_v2.types.list_test_executions_request
    import capo_lex_models_v2.types.list_test_executions_response
    import capo_lex_models_v2.types.list_test_set_records_request
    import capo_lex_models_v2.types.list_test_set_records_response
    import capo_lex_models_v2.types.list_test_sets_request
    import capo_lex_models_v2.types.list_test_sets_response
    import capo_lex_models_v2.types.list_utterance_analytics_data_request
    import capo_lex_models_v2.types.list_utterance_analytics_data_response
    import capo_lex_models_v2.types.list_utterance_metrics_request
    import capo_lex_models_v2.types.list_utterance_metrics_response
    import capo_lex_models_v2.types.locale_id
    import capo_lex_models_v2.types.max_results
    import capo_lex_models_v2.types.merge_strategy
    import capo_lex_models_v2.types.multiple_values_setting
    import capo_lex_models_v2.types.name
    import capo_lex_models_v2.types.next_index
    import capo_lex_models_v2.types.next_token
    import capo_lex_models_v2.types.numerical_bot_version
    import capo_lex_models_v2.types.obfuscation_setting
    import capo_lex_models_v2.types.operation_list
    import capo_lex_models_v2.types.output_contexts_list
    import capo_lex_models_v2.types.policy
    import capo_lex_models_v2.types.principal_list
    import capo_lex_models_v2.types.q_in_connect_intent_configuration
    import capo_lex_models_v2.types.qn_a_intent_configuration
    import capo_lex_models_v2.types.replica_region
    import capo_lex_models_v2.types.revision_id
    import capo_lex_models_v2.types.role_arn
    import capo_lex_models_v2.types.sample_utterances_list
    import capo_lex_models_v2.types.search_associated_transcripts_request
    import capo_lex_models_v2.types.search_associated_transcripts_response
    import capo_lex_models_v2.types.search_order
    import capo_lex_models_v2.types.sentiment_analysis_settings
    import capo_lex_models_v2.types.session_data_sort_by
    import capo_lex_models_v2.types.session_id
    import capo_lex_models_v2.types.session_ttl
    import capo_lex_models_v2.types.skip_resource_in_use_check
    import capo_lex_models_v2.types.slot_filters
    import capo_lex_models_v2.types.slot_priorities_list
    import capo_lex_models_v2.types.slot_sort_by
    import capo_lex_models_v2.types.slot_type_filters
    import capo_lex_models_v2.types.slot_type_signature
    import capo_lex_models_v2.types.slot_type_sort_by
    import capo_lex_models_v2.types.slot_type_values
    import capo_lex_models_v2.types.slot_value_elicitation_setting
    import capo_lex_models_v2.types.slot_value_selection_setting
    import capo_lex_models_v2.types.speaker_diarization_settings
    import capo_lex_models_v2.types.speech_detection_sensitivity
    import capo_lex_models_v2.types.speech_recognition_settings
    import capo_lex_models_v2.types.start_bot_analyzer_request
    import capo_lex_models_v2.types.start_bot_analyzer_response
    import capo_lex_models_v2.types.start_bot_recommendation_request
    import capo_lex_models_v2.types.start_bot_recommendation_response
    import capo_lex_models_v2.types.start_bot_resource_generation_request
    import capo_lex_models_v2.types.start_bot_resource_generation_response
    import capo_lex_models_v2.types.start_import_request
    import capo_lex_models_v2.types.start_import_response
    import capo_lex_models_v2.types.start_test_execution_request
    import capo_lex_models_v2.types.start_test_execution_response
    import capo_lex_models_v2.types.start_test_set_generation_request
    import capo_lex_models_v2.types.start_test_set_generation_response
    import capo_lex_models_v2.types.stop_bot_analyzer_request
    import capo_lex_models_v2.types.stop_bot_analyzer_response
    import capo_lex_models_v2.types.stop_bot_recommendation_request
    import capo_lex_models_v2.types.stop_bot_recommendation_response
    import capo_lex_models_v2.types.sub_slot_setting
    import capo_lex_models_v2.types.tag_key_list
    import capo_lex_models_v2.types.tag_map
    import capo_lex_models_v2.types.tag_resource_request
    import capo_lex_models_v2.types.tag_resource_response
    import capo_lex_models_v2.types.test_execution_api_mode
    import capo_lex_models_v2.types.test_execution_modality
    import capo_lex_models_v2.types.test_execution_result_filter_by
    import capo_lex_models_v2.types.test_execution_sort_by
    import capo_lex_models_v2.types.test_execution_target
    import capo_lex_models_v2.types.test_set_discrepancy_report_resource_target
    import capo_lex_models_v2.types.test_set_generation_data_source
    import capo_lex_models_v2.types.test_set_sort_by
    import capo_lex_models_v2.types.test_set_storage_location
    import capo_lex_models_v2.types.timestamp
    import capo_lex_models_v2.types.transcript_source_setting
    import capo_lex_models_v2.types.unified_speech_settings
    import capo_lex_models_v2.types.untag_resource_request
    import capo_lex_models_v2.types.untag_resource_response
    import capo_lex_models_v2.types.update_bot_alias_request
    import capo_lex_models_v2.types.update_bot_alias_response
    import capo_lex_models_v2.types.update_bot_locale_request
    import capo_lex_models_v2.types.update_bot_locale_response
    import capo_lex_models_v2.types.update_bot_recommendation_request
    import capo_lex_models_v2.types.update_bot_recommendation_response
    import capo_lex_models_v2.types.update_bot_request
    import capo_lex_models_v2.types.update_bot_response
    import capo_lex_models_v2.types.update_custom_vocabulary_items_list
    import capo_lex_models_v2.types.update_export_request
    import capo_lex_models_v2.types.update_export_response
    import capo_lex_models_v2.types.update_intent_request
    import capo_lex_models_v2.types.update_intent_response
    import capo_lex_models_v2.types.update_resource_policy_request
    import capo_lex_models_v2.types.update_resource_policy_response
    import capo_lex_models_v2.types.update_slot_request
    import capo_lex_models_v2.types.update_slot_response
    import capo_lex_models_v2.types.update_slot_type_request
    import capo_lex_models_v2.types.update_slot_type_response
    import capo_lex_models_v2.types.update_test_set_request
    import capo_lex_models_v2.types.update_test_set_response
    import capo_lex_models_v2.types.utterance_aggregation_duration
    import capo_lex_models_v2.types.utterance_data_sort_by
    import capo_lex_models_v2.types.uuid
    import capo_lex_models_v2.types.voice_settings


class AsyncLexModelsV2ClientConfig(TypedDict, total=False, closed=True):
    operation_interceptors: Iterable[AsyncInterceptor[Any, Any]]
    retry_max_attempts: int | None
    region: str | None
    use_dual_stack: bool | None
    use_fips: bool | None
    endpoint: str | None
    credentials_provider: IdentityProvider[Credentials] | None


class AsyncLexModelsV2Client:
    """A client for the ``LexModelsV2`` service.

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
        self._config = AsyncLexModelsV2ClientConfig(
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
        self, config_overrides: Optional[AsyncLexModelsV2ClientConfig] = None
    ) -> tuple[Iterable[AsyncInterceptor[Any, Any]], AsyncOperationOptions]:
        overrides: AsyncLexModelsV2ClientConfig = config_overrides or {}
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

    async def batch_create_custom_vocabulary_item(
        self,
        bot_id: "capo_lex_models_v2.types.id.Id",
        bot_version: "capo_lex_models_v2.types.bot_version.BotVersion",
        locale_id: "capo_lex_models_v2.types.locale_id.LocaleId",
        custom_vocabulary_item_list: "capo_lex_models_v2.types.create_custom_vocabulary_items_list.CreateCustomVocabularyItemsList",
        *,
        config_overrides: Optional[AsyncLexModelsV2ClientConfig] = None,
    ) -> "capo_lex_models_v2.types.batch_create_custom_vocabulary_item_response.BatchCreateCustomVocabularyItemResponse":
        """<p>Create a batch of custom vocabulary items for a given bot locale's custom vocabulary.</p>

        Args:
            bot_id: <p>The identifier of the bot associated with this custom vocabulary.</p>
            bot_version: <p>The identifier of the version of the bot associated with this custom vocabulary.</p>
            locale_id: <p>The identifier of the language and locale where this custom vocabulary is used. The string must match one of the supported locales. For more information, see <a href="https://docs.aws.amazon.com/lexv2/latest/dg/how-languages.html"> Supported Languages </a>.</p>
            custom_vocabulary_item_list: <p>A list of new custom vocabulary items. Each entry must contain a phrase and can optionally contain a displayAs and/or a weight.</p>

        Raises:
            capo_lex_models_v2.errors.internal_server_exception.InternalServerException: <p>The service encountered an unexpected condition. Try your request again.</p>
            capo_lex_models_v2.errors.resource_not_found_exception.ResourceNotFoundException: <p>You asked to describe a resource that doesn't exist. Check the resource that you are requesting and try again.</p>
            capo_lex_models_v2.errors.service_quota_exceeded_exception.ServiceQuotaExceededException: <p>You have reached a quota for your bot. </p>
            capo_lex_models_v2.errors.throttling_exception.ThrottlingException: <p>Your request rate is too high. Reduce the frequency of requests.</p>
            capo_lex_models_v2.errors.validation_exception.ValidationException: <p>One of the input parameters in your request isn't valid. Check the parameters and try your request again.</p>
            capo_lex_models_v2.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        async def _handler(
            req: "AsyncOperationRequest[capo_lex_models_v2.types.batch_create_custom_vocabulary_item_request.BatchCreateCustomVocabularyItemRequest]",
        ) -> AsyncOperationResponse[
            "capo_lex_models_v2.types.batch_create_custom_vocabulary_item_response.BatchCreateCustomVocabularyItemResponse"
        ]:
            import capo_lex_models_v2._operations.lex_model_building_service_v2.batch_create_custom_vocabulary_item

            (
                output,
                http_response,
            ) = await capo_lex_models_v2._operations.lex_model_building_service_v2.batch_create_custom_vocabulary_item.async_batch_create_custom_vocabulary_item(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_lex_models_v2.types.batch_create_custom_vocabulary_item_request.BatchCreateCustomVocabularyItemRequest = {
            "bot_id": bot_id,
            "bot_version": bot_version,
            "locale_id": locale_id,
            "custom_vocabulary_item_list": custom_vocabulary_item_list,
        }

        response = await aexecute_pipeline(
            AsyncOperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        await response.response.aclose()
        return response.output

    async def batch_delete_custom_vocabulary_item(
        self,
        bot_id: "capo_lex_models_v2.types.id.Id",
        bot_version: "capo_lex_models_v2.types.bot_version.BotVersion",
        locale_id: "capo_lex_models_v2.types.locale_id.LocaleId",
        custom_vocabulary_item_list: "capo_lex_models_v2.types.delete_custom_vocabulary_items_list.DeleteCustomVocabularyItemsList",
        *,
        config_overrides: Optional[AsyncLexModelsV2ClientConfig] = None,
    ) -> "capo_lex_models_v2.types.batch_delete_custom_vocabulary_item_response.BatchDeleteCustomVocabularyItemResponse":
        """<p>Delete a batch of custom vocabulary items for a given bot locale's custom vocabulary.</p>

        Args:
            bot_id: <p>The identifier of the bot associated with this custom vocabulary.</p>
            bot_version: <p>The identifier of the version of the bot associated with this custom vocabulary.</p>
            locale_id: <p>The identifier of the language and locale where this custom vocabulary is used. The string must match one of the supported locales. For more information, see <a href="https://docs.aws.amazon.com/lexv2/latest/dg/how-languages.html"> Supported Languages </a>.</p>
            custom_vocabulary_item_list: <p>A list of custom vocabulary items requested to be deleted. Each entry must contain the unique custom vocabulary entry identifier.</p>

        Raises:
            capo_lex_models_v2.errors.internal_server_exception.InternalServerException: <p>The service encountered an unexpected condition. Try your request again.</p>
            capo_lex_models_v2.errors.resource_not_found_exception.ResourceNotFoundException: <p>You asked to describe a resource that doesn't exist. Check the resource that you are requesting and try again.</p>
            capo_lex_models_v2.errors.service_quota_exceeded_exception.ServiceQuotaExceededException: <p>You have reached a quota for your bot. </p>
            capo_lex_models_v2.errors.throttling_exception.ThrottlingException: <p>Your request rate is too high. Reduce the frequency of requests.</p>
            capo_lex_models_v2.errors.validation_exception.ValidationException: <p>One of the input parameters in your request isn't valid. Check the parameters and try your request again.</p>
            capo_lex_models_v2.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        async def _handler(
            req: "AsyncOperationRequest[capo_lex_models_v2.types.batch_delete_custom_vocabulary_item_request.BatchDeleteCustomVocabularyItemRequest]",
        ) -> AsyncOperationResponse[
            "capo_lex_models_v2.types.batch_delete_custom_vocabulary_item_response.BatchDeleteCustomVocabularyItemResponse"
        ]:
            import capo_lex_models_v2._operations.lex_model_building_service_v2.batch_delete_custom_vocabulary_item

            (
                output,
                http_response,
            ) = await capo_lex_models_v2._operations.lex_model_building_service_v2.batch_delete_custom_vocabulary_item.async_batch_delete_custom_vocabulary_item(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_lex_models_v2.types.batch_delete_custom_vocabulary_item_request.BatchDeleteCustomVocabularyItemRequest = {
            "bot_id": bot_id,
            "bot_version": bot_version,
            "locale_id": locale_id,
            "custom_vocabulary_item_list": custom_vocabulary_item_list,
        }

        response = await aexecute_pipeline(
            AsyncOperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        await response.response.aclose()
        return response.output

    async def batch_update_custom_vocabulary_item(
        self,
        bot_id: "capo_lex_models_v2.types.id.Id",
        bot_version: "capo_lex_models_v2.types.bot_version.BotVersion",
        locale_id: "capo_lex_models_v2.types.locale_id.LocaleId",
        custom_vocabulary_item_list: "capo_lex_models_v2.types.update_custom_vocabulary_items_list.UpdateCustomVocabularyItemsList",
        *,
        config_overrides: Optional[AsyncLexModelsV2ClientConfig] = None,
    ) -> "capo_lex_models_v2.types.batch_update_custom_vocabulary_item_response.BatchUpdateCustomVocabularyItemResponse":
        """<p>Update a batch of custom vocabulary items for a given bot locale's custom vocabulary.</p>

        Args:
            bot_id: <p>The identifier of the bot associated with this custom vocabulary</p>
            bot_version: <p>The identifier of the version of the bot associated with this custom vocabulary.</p>
            locale_id: <p>The identifier of the language and locale where this custom vocabulary is used. The string must match one of the supported locales. For more information, see <a href="https://docs.aws.amazon.com/lexv2/latest/dg/how-languages.html"> Supported Languages </a>.</p>
            custom_vocabulary_item_list: <p>A list of custom vocabulary items with updated fields. Each entry must contain a phrase and can optionally contain a displayAs and/or a weight.</p>

        Raises:
            capo_lex_models_v2.errors.internal_server_exception.InternalServerException: <p>The service encountered an unexpected condition. Try your request again.</p>
            capo_lex_models_v2.errors.resource_not_found_exception.ResourceNotFoundException: <p>You asked to describe a resource that doesn't exist. Check the resource that you are requesting and try again.</p>
            capo_lex_models_v2.errors.service_quota_exceeded_exception.ServiceQuotaExceededException: <p>You have reached a quota for your bot. </p>
            capo_lex_models_v2.errors.throttling_exception.ThrottlingException: <p>Your request rate is too high. Reduce the frequency of requests.</p>
            capo_lex_models_v2.errors.validation_exception.ValidationException: <p>One of the input parameters in your request isn't valid. Check the parameters and try your request again.</p>
            capo_lex_models_v2.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        async def _handler(
            req: "AsyncOperationRequest[capo_lex_models_v2.types.batch_update_custom_vocabulary_item_request.BatchUpdateCustomVocabularyItemRequest]",
        ) -> AsyncOperationResponse[
            "capo_lex_models_v2.types.batch_update_custom_vocabulary_item_response.BatchUpdateCustomVocabularyItemResponse"
        ]:
            import capo_lex_models_v2._operations.lex_model_building_service_v2.batch_update_custom_vocabulary_item

            (
                output,
                http_response,
            ) = await capo_lex_models_v2._operations.lex_model_building_service_v2.batch_update_custom_vocabulary_item.async_batch_update_custom_vocabulary_item(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_lex_models_v2.types.batch_update_custom_vocabulary_item_request.BatchUpdateCustomVocabularyItemRequest = {
            "bot_id": bot_id,
            "bot_version": bot_version,
            "locale_id": locale_id,
            "custom_vocabulary_item_list": custom_vocabulary_item_list,
        }

        response = await aexecute_pipeline(
            AsyncOperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        await response.response.aclose()
        return response.output

    async def build_bot_locale(
        self,
        bot_id: "capo_lex_models_v2.types.id.Id",
        bot_version: "capo_lex_models_v2.types.draft_bot_version.DraftBotVersion",
        locale_id: "capo_lex_models_v2.types.locale_id.LocaleId",
        *,
        config_overrides: Optional[AsyncLexModelsV2ClientConfig] = None,
    ) -> "capo_lex_models_v2.types.build_bot_locale_response.BuildBotLocaleResponse":
        """<p>Builds a bot, its intents, and its slot types into a specific locale. A bot can be built into multiple locales. At runtime the locale is used to choose a specific build of the bot.</p>

        Args:
            bot_id: <p>The identifier of the bot to build. The identifier is returned in the response from the <a href="https://docs.aws.amazon.com/lexv2/latest/APIReference/API_CreateBot.html">CreateBot</a> operation.</p>
            bot_version: <p>The version of the bot to build. This can only be the draft version of the bot.</p>
            locale_id: <p>The identifier of the language and locale that the bot will be used in. The string must match one of the supported locales. All of the intents, slot types, and slots used in the bot must have the same locale. For more information, see <a href="https://docs.aws.amazon.com/lexv2/latest/dg/how-languages.html">Supported languages</a>.</p>

        Raises:
            capo_lex_models_v2.errors.conflict_exception.ConflictException: <p>The action that you tried to perform couldn't be completed because the resource is in a conflicting state. For example, deleting a bot that is in the CREATING state. Try your request again. </p>
            capo_lex_models_v2.errors.internal_server_exception.InternalServerException: <p>The service encountered an unexpected condition. Try your request again.</p>
            capo_lex_models_v2.errors.precondition_failed_exception.PreconditionFailedException: <p>Your request couldn't be completed because one or more request fields aren't valid. Check the fields in your request and try again.</p>
            capo_lex_models_v2.errors.service_quota_exceeded_exception.ServiceQuotaExceededException: <p>You have reached a quota for your bot. </p>
            capo_lex_models_v2.errors.throttling_exception.ThrottlingException: <p>Your request rate is too high. Reduce the frequency of requests.</p>
            capo_lex_models_v2.errors.validation_exception.ValidationException: <p>One of the input parameters in your request isn't valid. Check the parameters and try your request again.</p>
            capo_lex_models_v2.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        async def _handler(
            req: "AsyncOperationRequest[capo_lex_models_v2.types.build_bot_locale_request.BuildBotLocaleRequest]",
        ) -> AsyncOperationResponse[
            "capo_lex_models_v2.types.build_bot_locale_response.BuildBotLocaleResponse"
        ]:
            import capo_lex_models_v2._operations.lex_model_building_service_v2.build_bot_locale

            (
                output,
                http_response,
            ) = await capo_lex_models_v2._operations.lex_model_building_service_v2.build_bot_locale.async_build_bot_locale(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_lex_models_v2.types.build_bot_locale_request.BuildBotLocaleRequest = {
            "bot_id": bot_id,
            "bot_version": bot_version,
            "locale_id": locale_id,
        }

        response = await aexecute_pipeline(
            AsyncOperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        await response.response.aclose()
        return response.output

    async def create_bot(
        self,
        bot_name: "capo_lex_models_v2.types.name.Name",
        role_arn: "capo_lex_models_v2.types.role_arn.RoleArn",
        data_privacy: "capo_lex_models_v2.types.data_privacy.DataPrivacy",
        idle_session_ttl_in_seconds: "capo_lex_models_v2.types.session_ttl.SessionTTL",
        *,
        config_overrides: Optional[AsyncLexModelsV2ClientConfig] = None,
        description: Optional[
            "capo_lex_models_v2.types.description.Description"
        ] = None,
        bot_tags: Optional["capo_lex_models_v2.types.tag_map.TagMap"] = None,
        test_bot_alias_tags: Optional["capo_lex_models_v2.types.tag_map.TagMap"] = None,
        bot_type: Optional["capo_lex_models_v2.types.bot_type.BotType"] = None,
        bot_members: Optional["capo_lex_models_v2.types.bot_members.BotMembers"] = None,
        error_log_settings: Optional[
            "capo_lex_models_v2.types.error_log_settings.ErrorLogSettings"
        ] = None,
    ) -> "capo_lex_models_v2.types.create_bot_response.CreateBotResponse":
        """<p>Creates an Amazon Lex conversational bot. </p>

        Args:
            bot_name: <p>The name of the bot. The bot name must be unique in the account that creates the bot.</p>
            description: <p>A description of the bot. It appears in lists to help you identify a particular bot.</p>
            role_arn: <p>The Amazon Resource Name (ARN) of an IAM role that has permission to access the bot.</p>
            data_privacy: <p>Provides information on additional privacy protections Amazon Lex should use with the bot's data.</p>
            idle_session_ttl_in_seconds: <p>The time, in seconds, that Amazon Lex should keep information about a user's conversation with the bot. </p> <p>A user interaction remains active for the amount of time specified. If no conversation occurs during this time, the session expires and Amazon Lex deletes any data provided before the timeout.</p> <p>You can specify between 60 (1 minute) and 86,400 (24 hours) seconds.</p>
            bot_tags: <p>A list of tags to add to the bot. You can only add tags when you create a bot. You can't use the <code>UpdateBot</code> operation to update tags. To update tags, use the <code>TagResource</code> operation.</p>
            test_bot_alias_tags: <p>A list of tags to add to the test alias for a bot. You can only add tags when you create a bot. You can't use the <code>UpdateAlias</code> operation to update tags. To update tags on the test alias, use the <code>TagResource</code> operation.</p>
            bot_type: <p>The type of a bot to create.</p>
            bot_members: <p>The list of bot members in a network to be created.</p>
            error_log_settings: <p>Specifies the configuration for error logging during bot creation.</p>

        Raises:
            capo_lex_models_v2.errors.conflict_exception.ConflictException: <p>The action that you tried to perform couldn't be completed because the resource is in a conflicting state. For example, deleting a bot that is in the CREATING state. Try your request again. </p>
            capo_lex_models_v2.errors.internal_server_exception.InternalServerException: <p>The service encountered an unexpected condition. Try your request again.</p>
            capo_lex_models_v2.errors.precondition_failed_exception.PreconditionFailedException: <p>Your request couldn't be completed because one or more request fields aren't valid. Check the fields in your request and try again.</p>
            capo_lex_models_v2.errors.service_quota_exceeded_exception.ServiceQuotaExceededException: <p>You have reached a quota for your bot. </p>
            capo_lex_models_v2.errors.throttling_exception.ThrottlingException: <p>Your request rate is too high. Reduce the frequency of requests.</p>
            capo_lex_models_v2.errors.validation_exception.ValidationException: <p>One of the input parameters in your request isn't valid. Check the parameters and try your request again.</p>
            capo_lex_models_v2.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        async def _handler(
            req: "AsyncOperationRequest[capo_lex_models_v2.types.create_bot_request.CreateBotRequest]",
        ) -> AsyncOperationResponse[
            "capo_lex_models_v2.types.create_bot_response.CreateBotResponse"
        ]:
            import capo_lex_models_v2._operations.lex_model_building_service_v2.create_bot

            (
                output,
                http_response,
            ) = await capo_lex_models_v2._operations.lex_model_building_service_v2.create_bot.async_create_bot(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_lex_models_v2.types.create_bot_request.CreateBotRequest = {
            "bot_name": bot_name,
            "role_arn": role_arn,
            "data_privacy": data_privacy,
            "idle_session_ttl_in_seconds": idle_session_ttl_in_seconds,
        }
        if description is not None:
            input_["description"] = description
        if bot_tags is not None:
            input_["bot_tags"] = bot_tags
        if test_bot_alias_tags is not None:
            input_["test_bot_alias_tags"] = test_bot_alias_tags
        if bot_type is not None:
            input_["bot_type"] = bot_type
        if bot_members is not None:
            input_["bot_members"] = bot_members
        if error_log_settings is not None:
            input_["error_log_settings"] = error_log_settings

        response = await aexecute_pipeline(
            AsyncOperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        await response.response.aclose()
        return response.output

    async def create_bot_alias(
        self,
        bot_alias_name: "capo_lex_models_v2.types.name.Name",
        bot_id: "capo_lex_models_v2.types.id.Id",
        *,
        config_overrides: Optional[AsyncLexModelsV2ClientConfig] = None,
        description: Optional[
            "capo_lex_models_v2.types.description.Description"
        ] = None,
        bot_version: Optional[
            "capo_lex_models_v2.types.numerical_bot_version.NumericalBotVersion"
        ] = None,
        bot_alias_locale_settings: Optional[
            "capo_lex_models_v2.types.bot_alias_locale_settings_map.BotAliasLocaleSettingsMap"
        ] = None,
        conversation_log_settings: Optional[
            "capo_lex_models_v2.types.conversation_log_settings.ConversationLogSettings"
        ] = None,
        sentiment_analysis_settings: Optional[
            "capo_lex_models_v2.types.sentiment_analysis_settings.SentimentAnalysisSettings"
        ] = None,
        tags: Optional["capo_lex_models_v2.types.tag_map.TagMap"] = None,
    ) -> "capo_lex_models_v2.types.create_bot_alias_response.CreateBotAliasResponse":
        """<p>Creates an alias for the specified version of a bot. Use an alias to enable you to change the version of a bot without updating applications that use the bot.</p> <p>For example, you can create an alias called "PROD" that your applications use to call the Amazon Lex bot. </p>

        Args:
            bot_alias_name: <p>The alias to create. The name must be unique for the bot.</p>
            description: <p>A description of the alias. Use this description to help identify the alias.</p>
            bot_version: <p>The version of the bot that this alias points to. You can use the <a href="https://docs.aws.amazon.com/lexv2/latest/APIReference/API_UpdateBotAlias.html">UpdateBotAlias</a> operation to change the bot version associated with the alias.</p>
            bot_alias_locale_settings: <p>Maps configuration information to a specific locale. You can use this parameter to specify a specific Lambda function to run different functions in different locales.</p>
            conversation_log_settings: <p>Specifies whether Amazon Lex logs text and audio for a conversation with the bot. When you enable conversation logs, text logs store text input, transcripts of audio input, and associated metadata in Amazon CloudWatch Logs. Audio logs store audio input in Amazon S3.</p>
            bot_id: <p>The unique identifier of the bot that the alias applies to.</p>
            tags: <p>A list of tags to add to the bot alias. You can only add tags when you create an alias, you can't use the <code>UpdateBotAlias</code> operation to update the tags on a bot alias. To update tags, use the <code>TagResource</code> operation.</p>

        Raises:
            capo_lex_models_v2.errors.conflict_exception.ConflictException: <p>The action that you tried to perform couldn't be completed because the resource is in a conflicting state. For example, deleting a bot that is in the CREATING state. Try your request again. </p>
            capo_lex_models_v2.errors.internal_server_exception.InternalServerException: <p>The service encountered an unexpected condition. Try your request again.</p>
            capo_lex_models_v2.errors.precondition_failed_exception.PreconditionFailedException: <p>Your request couldn't be completed because one or more request fields aren't valid. Check the fields in your request and try again.</p>
            capo_lex_models_v2.errors.service_quota_exceeded_exception.ServiceQuotaExceededException: <p>You have reached a quota for your bot. </p>
            capo_lex_models_v2.errors.throttling_exception.ThrottlingException: <p>Your request rate is too high. Reduce the frequency of requests.</p>
            capo_lex_models_v2.errors.validation_exception.ValidationException: <p>One of the input parameters in your request isn't valid. Check the parameters and try your request again.</p>
            capo_lex_models_v2.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        async def _handler(
            req: "AsyncOperationRequest[capo_lex_models_v2.types.create_bot_alias_request.CreateBotAliasRequest]",
        ) -> AsyncOperationResponse[
            "capo_lex_models_v2.types.create_bot_alias_response.CreateBotAliasResponse"
        ]:
            import capo_lex_models_v2._operations.lex_model_building_service_v2.create_bot_alias

            (
                output,
                http_response,
            ) = await capo_lex_models_v2._operations.lex_model_building_service_v2.create_bot_alias.async_create_bot_alias(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_lex_models_v2.types.create_bot_alias_request.CreateBotAliasRequest = {
            "bot_alias_name": bot_alias_name,
            "bot_id": bot_id,
        }
        if description is not None:
            input_["description"] = description
        if bot_version is not None:
            input_["bot_version"] = bot_version
        if bot_alias_locale_settings is not None:
            input_["bot_alias_locale_settings"] = bot_alias_locale_settings
        if conversation_log_settings is not None:
            input_["conversation_log_settings"] = conversation_log_settings
        if sentiment_analysis_settings is not None:
            input_["sentiment_analysis_settings"] = sentiment_analysis_settings
        if tags is not None:
            input_["tags"] = tags

        response = await aexecute_pipeline(
            AsyncOperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        await response.response.aclose()
        return response.output

    async def create_bot_locale(
        self,
        bot_id: "capo_lex_models_v2.types.id.Id",
        bot_version: "capo_lex_models_v2.types.draft_bot_version.DraftBotVersion",
        locale_id: "capo_lex_models_v2.types.locale_id.LocaleId",
        nlu_intent_confidence_threshold: "capo_lex_models_v2.types.confidence_threshold.ConfidenceThreshold",
        *,
        config_overrides: Optional[AsyncLexModelsV2ClientConfig] = None,
        description: Optional[
            "capo_lex_models_v2.types.description.Description"
        ] = None,
        voice_settings: Optional[
            "capo_lex_models_v2.types.voice_settings.VoiceSettings"
        ] = None,
        unified_speech_settings: Optional[
            "capo_lex_models_v2.types.unified_speech_settings.UnifiedSpeechSettings"
        ] = None,
        audio_filler_settings: Optional[
            "capo_lex_models_v2.types.audio_filler_settings.AudioFillerSettings"
        ] = None,
        speech_recognition_settings: Optional[
            "capo_lex_models_v2.types.speech_recognition_settings.SpeechRecognitionSettings"
        ] = None,
        generative_ai_settings: Optional[
            "capo_lex_models_v2.types.generative_ai_settings.GenerativeAISettings"
        ] = None,
        speech_detection_sensitivity: Optional[
            "capo_lex_models_v2.types.speech_detection_sensitivity.SpeechDetectionSensitivity"
        ] = None,
        speaker_diarization_settings: Optional[
            "capo_lex_models_v2.types.speaker_diarization_settings.SpeakerDiarizationSettings"
        ] = None,
    ) -> "capo_lex_models_v2.types.create_bot_locale_response.CreateBotLocaleResponse":
        """<p>Creates a locale in the bot. The locale contains the intents and slot types that the bot uses in conversations with users in the specified language and locale. You must add a locale to a bot before you can add intents and slot types to the bot.</p>

        Args:
            bot_id: <p>The identifier of the bot to create the locale for.</p>
            bot_version: <p>The version of the bot to create the locale for. This can only be the draft version of the bot.</p>
            locale_id: <p>The identifier of the language and locale that the bot will be used in. The string must match one of the supported locales. All of the intents, slot types, and slots used in the bot must have the same locale. For more information, see <a href="https://docs.aws.amazon.com/lexv2/latest/dg/how-languages.html">Supported languages</a>.</p>
            description: <p>A description of the bot locale. Use this to help identify the bot locale in lists.</p>
            nlu_intent_confidence_threshold: <p>Determines the threshold where Amazon Lex will insert the <code>AMAZON.FallbackIntent</code>, <code>AMAZON.KendraSearchIntent</code>, or both when returning alternative intents. <code>AMAZON.FallbackIntent</code> and <code>AMAZON.KendraSearchIntent</code> are only inserted if they are configured for the bot.</p> <p>For example, suppose a bot is configured with the confidence threshold of 0.80 and the <code>AMAZON.FallbackIntent</code>. Amazon Lex returns three alternative intents with the following confidence scores: IntentA (0.70), IntentB (0.60), IntentC (0.50). The response from the <code>RecognizeText</code> operation would be:</p> <ul> <li> <p>AMAZON.FallbackIntent</p> </li> <li> <p>IntentA</p> </li> <li> <p>IntentB</p> </li> <li> <p>IntentC</p> </li> </ul>
            voice_settings: <p>The Amazon Polly voice ID that Amazon Lex uses for voice interaction with the user.</p>
            unified_speech_settings: <p>Unified speech settings to configure for the new bot locale.</p>
            audio_filler_settings: <p>Audio filler settings to configure for the new bot locale. When enabled, Amazon Lex plays a brief background audio filler during speech-to-speech interactions to mask processing delays. Requires <code>unifiedSpeechSettings</code> (speech-to-speech) to be configured on the bot locale.</p>
            speech_recognition_settings: <p>Speech-to-text settings to configure for the new bot locale.</p>
            speech_detection_sensitivity: <p>The sensitivity level for voice activity detection (VAD) in the bot locale. This setting helps optimize speech recognition accuracy by adjusting how the system responds to background noise during voice interactions.</p>
            speaker_diarization_settings: <p>The speaker diarization settings to configure for the new bot locale. When enabled, Amazon Lex restricts speech detection to the primary (loudest) speaker during streaming audio conversations.</p>

        Raises:
            capo_lex_models_v2.errors.conflict_exception.ConflictException: <p>The action that you tried to perform couldn't be completed because the resource is in a conflicting state. For example, deleting a bot that is in the CREATING state. Try your request again. </p>
            capo_lex_models_v2.errors.internal_server_exception.InternalServerException: <p>The service encountered an unexpected condition. Try your request again.</p>
            capo_lex_models_v2.errors.precondition_failed_exception.PreconditionFailedException: <p>Your request couldn't be completed because one or more request fields aren't valid. Check the fields in your request and try again.</p>
            capo_lex_models_v2.errors.service_quota_exceeded_exception.ServiceQuotaExceededException: <p>You have reached a quota for your bot. </p>
            capo_lex_models_v2.errors.throttling_exception.ThrottlingException: <p>Your request rate is too high. Reduce the frequency of requests.</p>
            capo_lex_models_v2.errors.validation_exception.ValidationException: <p>One of the input parameters in your request isn't valid. Check the parameters and try your request again.</p>
            capo_lex_models_v2.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        async def _handler(
            req: "AsyncOperationRequest[capo_lex_models_v2.types.create_bot_locale_request.CreateBotLocaleRequest]",
        ) -> AsyncOperationResponse[
            "capo_lex_models_v2.types.create_bot_locale_response.CreateBotLocaleResponse"
        ]:
            import capo_lex_models_v2._operations.lex_model_building_service_v2.create_bot_locale

            (
                output,
                http_response,
            ) = await capo_lex_models_v2._operations.lex_model_building_service_v2.create_bot_locale.async_create_bot_locale(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_lex_models_v2.types.create_bot_locale_request.CreateBotLocaleRequest = {
            "bot_id": bot_id,
            "bot_version": bot_version,
            "locale_id": locale_id,
            "nlu_intent_confidence_threshold": nlu_intent_confidence_threshold,
        }
        if description is not None:
            input_["description"] = description
        if voice_settings is not None:
            input_["voice_settings"] = voice_settings
        if unified_speech_settings is not None:
            input_["unified_speech_settings"] = unified_speech_settings
        if audio_filler_settings is not None:
            input_["audio_filler_settings"] = audio_filler_settings
        if speech_recognition_settings is not None:
            input_["speech_recognition_settings"] = speech_recognition_settings
        if generative_ai_settings is not None:
            input_["generative_ai_settings"] = generative_ai_settings
        if speech_detection_sensitivity is not None:
            input_["speech_detection_sensitivity"] = speech_detection_sensitivity
        if speaker_diarization_settings is not None:
            input_["speaker_diarization_settings"] = speaker_diarization_settings

        response = await aexecute_pipeline(
            AsyncOperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        await response.response.aclose()
        return response.output

    async def create_bot_replica(
        self,
        bot_id: "capo_lex_models_v2.types.id.Id",
        replica_region: "capo_lex_models_v2.types.replica_region.ReplicaRegion",
        *,
        config_overrides: Optional[AsyncLexModelsV2ClientConfig] = None,
    ) -> (
        "capo_lex_models_v2.types.create_bot_replica_response.CreateBotReplicaResponse"
    ):
        """<p>Action to create a replication of the source bot in the secondary region.</p>

        Args:
            bot_id: <p>The request for the unique bot ID of the source bot to be replicated in the secondary region.</p>
            replica_region: <p>The request for the secondary region that will be used in the replication of the source bot.</p>

        Raises:
            capo_lex_models_v2.errors.conflict_exception.ConflictException: <p>The action that you tried to perform couldn't be completed because the resource is in a conflicting state. For example, deleting a bot that is in the CREATING state. Try your request again. </p>
            capo_lex_models_v2.errors.internal_server_exception.InternalServerException: <p>The service encountered an unexpected condition. Try your request again.</p>
            capo_lex_models_v2.errors.precondition_failed_exception.PreconditionFailedException: <p>Your request couldn't be completed because one or more request fields aren't valid. Check the fields in your request and try again.</p>
            capo_lex_models_v2.errors.service_quota_exceeded_exception.ServiceQuotaExceededException: <p>You have reached a quota for your bot. </p>
            capo_lex_models_v2.errors.throttling_exception.ThrottlingException: <p>Your request rate is too high. Reduce the frequency of requests.</p>
            capo_lex_models_v2.errors.validation_exception.ValidationException: <p>One of the input parameters in your request isn't valid. Check the parameters and try your request again.</p>
            capo_lex_models_v2.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        async def _handler(
            req: "AsyncOperationRequest[capo_lex_models_v2.types.create_bot_replica_request.CreateBotReplicaRequest]",
        ) -> AsyncOperationResponse[
            "capo_lex_models_v2.types.create_bot_replica_response.CreateBotReplicaResponse"
        ]:
            import capo_lex_models_v2._operations.lex_model_building_service_v2.create_bot_replica

            (
                output,
                http_response,
            ) = await capo_lex_models_v2._operations.lex_model_building_service_v2.create_bot_replica.async_create_bot_replica(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_lex_models_v2.types.create_bot_replica_request.CreateBotReplicaRequest = {
            "bot_id": bot_id,
            "replica_region": replica_region,
        }

        response = await aexecute_pipeline(
            AsyncOperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        await response.response.aclose()
        return response.output

    async def create_bot_version(
        self,
        bot_id: "capo_lex_models_v2.types.id.Id",
        bot_version_locale_specification: "capo_lex_models_v2.types.bot_version_locale_specification.BotVersionLocaleSpecification",
        *,
        config_overrides: Optional[AsyncLexModelsV2ClientConfig] = None,
        description: Optional[
            "capo_lex_models_v2.types.description.Description"
        ] = None,
    ) -> (
        "capo_lex_models_v2.types.create_bot_version_response.CreateBotVersionResponse"
    ):
        """<p>Creates an immutable version of the bot. When you create the first version of a bot, Amazon Lex sets the version number to 1. Subsequent bot versions increase in an increment of 1. The version number will always represent the total number of versions created of the bot, not the current number of versions. If a bot version is deleted, that bot version number will not be reused.</p>

        Args:
            bot_id: <p>The identifier of the bot to create the version for.</p>
            description: <p>A description of the version. Use the description to help identify the version in lists.</p>
            bot_version_locale_specification: <p>Specifies the locales that Amazon Lex adds to this version. You can choose the <code>Draft</code> version or any other previously published version for each locale. When you specify a source version, the locale data is copied from the source version to the new version.</p>

        Raises:
            capo_lex_models_v2.errors.conflict_exception.ConflictException: <p>The action that you tried to perform couldn't be completed because the resource is in a conflicting state. For example, deleting a bot that is in the CREATING state. Try your request again. </p>
            capo_lex_models_v2.errors.internal_server_exception.InternalServerException: <p>The service encountered an unexpected condition. Try your request again.</p>
            capo_lex_models_v2.errors.precondition_failed_exception.PreconditionFailedException: <p>Your request couldn't be completed because one or more request fields aren't valid. Check the fields in your request and try again.</p>
            capo_lex_models_v2.errors.service_quota_exceeded_exception.ServiceQuotaExceededException: <p>You have reached a quota for your bot. </p>
            capo_lex_models_v2.errors.throttling_exception.ThrottlingException: <p>Your request rate is too high. Reduce the frequency of requests.</p>
            capo_lex_models_v2.errors.validation_exception.ValidationException: <p>One of the input parameters in your request isn't valid. Check the parameters and try your request again.</p>
            capo_lex_models_v2.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        async def _handler(
            req: "AsyncOperationRequest[capo_lex_models_v2.types.create_bot_version_request.CreateBotVersionRequest]",
        ) -> AsyncOperationResponse[
            "capo_lex_models_v2.types.create_bot_version_response.CreateBotVersionResponse"
        ]:
            import capo_lex_models_v2._operations.lex_model_building_service_v2.create_bot_version

            (
                output,
                http_response,
            ) = await capo_lex_models_v2._operations.lex_model_building_service_v2.create_bot_version.async_create_bot_version(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_lex_models_v2.types.create_bot_version_request.CreateBotVersionRequest = {
            "bot_id": bot_id,
            "bot_version_locale_specification": bot_version_locale_specification,
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

    async def create_export(
        self,
        resource_specification: "capo_lex_models_v2.types.export_resource_specification.ExportResourceSpecification",
        file_format: "capo_lex_models_v2.types.import_export_file_format.ImportExportFileFormat",
        *,
        config_overrides: Optional[AsyncLexModelsV2ClientConfig] = None,
        file_password: Optional[
            "capo_lex_models_v2.types.import_export_file_password.ImportExportFilePassword"
        ] = None,
    ) -> "capo_lex_models_v2.types.create_export_response.CreateExportResponse":
        """<p>Creates a zip archive containing the contents of a bot or a bot locale. The archive contains a directory structure that contains JSON files that define the bot.</p> <p>You can create an archive that contains the complete definition of a bot, or you can specify that the archive contain only the definition of a single bot locale.</p> <p>For more information about exporting bots, and about the structure of the export archive, see <a href="https://docs.aws.amazon.com/lexv2/latest/dg/importing-exporting.html"> Importing and exporting bots </a> </p>

        Args:
            resource_specification: <p>Specifies the type of resource to export, either a bot or a bot locale. You can only specify one type of resource to export.</p>
            file_format: <p>The file format of the bot or bot locale definition files.</p>
            file_password: <p>An password to use to encrypt the exported archive. Using a password is optional, but you should encrypt the archive to protect the data in transit between Amazon Lex and your local computer.</p>

        Raises:
            capo_lex_models_v2.errors.conflict_exception.ConflictException: <p>The action that you tried to perform couldn't be completed because the resource is in a conflicting state. For example, deleting a bot that is in the CREATING state. Try your request again. </p>
            capo_lex_models_v2.errors.internal_server_exception.InternalServerException: <p>The service encountered an unexpected condition. Try your request again.</p>
            capo_lex_models_v2.errors.resource_not_found_exception.ResourceNotFoundException: <p>You asked to describe a resource that doesn't exist. Check the resource that you are requesting and try again.</p>
            capo_lex_models_v2.errors.service_quota_exceeded_exception.ServiceQuotaExceededException: <p>You have reached a quota for your bot. </p>
            capo_lex_models_v2.errors.throttling_exception.ThrottlingException: <p>Your request rate is too high. Reduce the frequency of requests.</p>
            capo_lex_models_v2.errors.validation_exception.ValidationException: <p>One of the input parameters in your request isn't valid. Check the parameters and try your request again.</p>
            capo_lex_models_v2.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        async def _handler(
            req: "AsyncOperationRequest[capo_lex_models_v2.types.create_export_request.CreateExportRequest]",
        ) -> AsyncOperationResponse[
            "capo_lex_models_v2.types.create_export_response.CreateExportResponse"
        ]:
            import capo_lex_models_v2._operations.lex_model_building_service_v2.create_export

            (
                output,
                http_response,
            ) = await capo_lex_models_v2._operations.lex_model_building_service_v2.create_export.async_create_export(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_lex_models_v2.types.create_export_request.CreateExportRequest = {
            "resource_specification": resource_specification,
            "file_format": file_format,
        }
        if file_password is not None:
            input_["file_password"] = file_password

        response = await aexecute_pipeline(
            AsyncOperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        await response.response.aclose()
        return response.output

    async def create_intent(
        self,
        intent_name: "capo_lex_models_v2.types.name.Name",
        bot_id: "capo_lex_models_v2.types.id.Id",
        bot_version: "capo_lex_models_v2.types.draft_bot_version.DraftBotVersion",
        locale_id: "capo_lex_models_v2.types.locale_id.LocaleId",
        *,
        config_overrides: Optional[AsyncLexModelsV2ClientConfig] = None,
        intent_display_name: Optional[
            "capo_lex_models_v2.types.display_name.DisplayName"
        ] = None,
        description: Optional[
            "capo_lex_models_v2.types.description.Description"
        ] = None,
        parent_intent_signature: Optional[
            "capo_lex_models_v2.types.intent_signature.IntentSignature"
        ] = None,
        sample_utterances: Optional[
            "capo_lex_models_v2.types.sample_utterances_list.SampleUtterancesList"
        ] = None,
        dialog_code_hook: Optional[
            "capo_lex_models_v2.types.dialog_code_hook_settings.DialogCodeHookSettings"
        ] = None,
        fulfillment_code_hook: Optional[
            "capo_lex_models_v2.types.fulfillment_code_hook_settings.FulfillmentCodeHookSettings"
        ] = None,
        intent_confirmation_setting: Optional[
            "capo_lex_models_v2.types.intent_confirmation_setting.IntentConfirmationSetting"
        ] = None,
        intent_closing_setting: Optional[
            "capo_lex_models_v2.types.intent_closing_setting.IntentClosingSetting"
        ] = None,
        input_contexts: Optional[
            "capo_lex_models_v2.types.input_contexts_list.InputContextsList"
        ] = None,
        output_contexts: Optional[
            "capo_lex_models_v2.types.output_contexts_list.OutputContextsList"
        ] = None,
        kendra_configuration: Optional[
            "capo_lex_models_v2.types.kendra_configuration.KendraConfiguration"
        ] = None,
        initial_response_setting: Optional[
            "capo_lex_models_v2.types.initial_response_setting.InitialResponseSetting"
        ] = None,
        qn_a_intent_configuration: Optional[
            "capo_lex_models_v2.types.qn_a_intent_configuration.QnAIntentConfiguration"
        ] = None,
        q_in_connect_intent_configuration: Optional[
            "capo_lex_models_v2.types.q_in_connect_intent_configuration.QInConnectIntentConfiguration"
        ] = None,
    ) -> "capo_lex_models_v2.types.create_intent_response.CreateIntentResponse":
        """<p>Creates an intent.</p> <p>To define the interaction between the user and your bot, you define one or more intents. For example, for a pizza ordering bot you would create an <code>OrderPizza</code> intent.</p> <p>When you create an intent, you must provide a name. You can optionally provide the following:</p> <ul> <li> <p>Sample utterances. For example, "I want to order a pizza" and "Can I order a pizza." You can't provide utterances for built-in intents.</p> </li> <li> <p>Information to be gathered. You specify slots for the information that you bot requests from the user. You can specify standard slot types, such as date and time, or custom slot types for your application.</p> </li> <li> <p>How the intent is fulfilled. You can provide a Lambda function or configure the intent to return the intent information to your client application. If you use a Lambda function, Amazon Lex invokes the function when all of the intent information is available.</p> </li> <li> <p>A confirmation prompt to send to the user to confirm an intent. For example, "Shall I order your pizza?"</p> </li> <li> <p>A conclusion statement to send to the user after the intent is fulfilled. For example, "I ordered your pizza."</p> </li> <li> <p>A follow-up prompt that asks the user for additional activity. For example, "Do you want a drink with your pizza?"</p> </li> </ul>

        Args:
            intent_name: <p>The name of the intent. Intent names must be unique in the locale that contains the intent and cannot match the name of any built-in intent.</p>
            intent_display_name: <p>A display name for the intent. If configured, This name will be shown to users during Intent Disambiguation instead of the intent name. Display names should be user-friendly, descriptive and match the intent's purpose to improve user experience during disambiguation.</p>
            description: <p>A description of the intent. Use the description to help identify the intent in lists.</p>
            parent_intent_signature: <p>A unique identifier for the built-in intent to base this intent on.</p>
            sample_utterances: <p>An array of strings that a user might say to signal the intent. For example, "I want a pizza", or "I want a {PizzaSize} pizza". </p> <p>In an utterance, slot names are enclosed in curly braces ("{", "}") to indicate where they should be displayed in the utterance shown to the user.. </p>
            dialog_code_hook: <p>Specifies that Amazon Lex invokes the alias Lambda function for each user input. You can invoke this Lambda function to personalize user interaction.</p> <p>For example, suppose that your bot determines that the user's name is John. You Lambda function might retrieve John's information from a backend database and prepopulate some of the values. For example, if you find that John is gluten intolerant, you might set the corresponding intent slot, <code>glutenIntolerant</code> to <code>true</code>. You might find John's phone number and set the corresponding session attribute.</p>
            fulfillment_code_hook: <p>Specifies that Amazon Lex invokes the alias Lambda function when the intent is ready for fulfillment. You can invoke this function to complete the bot's transaction with the user.</p> <p>For example, in a pizza ordering bot, the Lambda function can look up the closest pizza restaurant to the customer's location and then place an order on the customer's behalf.</p>
            intent_confirmation_setting: <p>Provides prompts that Amazon Lex sends to the user to confirm the completion of an intent. If the user answers "no," the settings contain a statement that is sent to the user to end the intent.</p>
            intent_closing_setting: <p>Sets the response that Amazon Lex sends to the user when the intent is closed.</p>
            input_contexts: <p>A list of contexts that must be active for this intent to be considered by Amazon Lex.</p> <p>When an intent has an input context list, Amazon Lex only considers using the intent in an interaction with the user when the specified contexts are included in the active context list for the session. If the contexts are not active, then Amazon Lex will not use the intent.</p> <p>A context can be automatically activated using the <code>outputContexts</code> property or it can be set at runtime.</p> <p> For example, if there are two intents with different input contexts that respond to the same utterances, only the intent with the active context will respond.</p> <p>An intent may have up to 5 input contexts. If an intent has multiple input contexts, all of the contexts must be active to consider the intent.</p>
            output_contexts: <p>A lists of contexts that the intent activates when it is fulfilled.</p> <p>You can use an output context to indicate the intents that Amazon Lex should consider for the next turn of the conversation with a customer. </p> <p>When you use the <code>outputContextsList</code> property, all of the contexts specified in the list are activated when the intent is fulfilled. You can set up to 10 output contexts. You can also set the number of conversation turns that the context should be active, or the length of time that the context should be active.</p>
            kendra_configuration: <p>Configuration information required to use the <code>AMAZON.KendraSearchIntent</code> intent to connect to an Amazon Kendra index. The <code>AMAZON.KendraSearchIntent</code> intent is called when Amazon Lex can't determine another intent to invoke.</p>
            bot_id: <p>The identifier of the bot associated with this intent.</p>
            bot_version: <p>The version of the bot associated with this intent.</p>
            locale_id: <p>The identifier of the language and locale where this intent is used. All of the bots, slot types, and slots used by the intent must have the same locale. For more information, see <a href="https://docs.aws.amazon.com/lexv2/latest/dg/how-languages.html">Supported languages</a>.</p>
            initial_response_setting: <p>Configuration settings for the response that is sent to the user at the beginning of a conversation, before eliciting slot values.</p>
            qn_a_intent_configuration: <p>Specifies the configuration of the built-in <code>Amazon.QnAIntent</code>. The <code>AMAZON.QnAIntent</code> intent is called when Amazon Lex can't determine another intent to invoke. If you specify this field, you can't specify the <code>kendraConfiguration</code> field.</p>
            q_in_connect_intent_configuration: <p>Qinconnect intent configuration details for the create intent request.</p>

        Raises:
            capo_lex_models_v2.errors.conflict_exception.ConflictException: <p>The action that you tried to perform couldn't be completed because the resource is in a conflicting state. For example, deleting a bot that is in the CREATING state. Try your request again. </p>
            capo_lex_models_v2.errors.internal_server_exception.InternalServerException: <p>The service encountered an unexpected condition. Try your request again.</p>
            capo_lex_models_v2.errors.precondition_failed_exception.PreconditionFailedException: <p>Your request couldn't be completed because one or more request fields aren't valid. Check the fields in your request and try again.</p>
            capo_lex_models_v2.errors.service_quota_exceeded_exception.ServiceQuotaExceededException: <p>You have reached a quota for your bot. </p>
            capo_lex_models_v2.errors.throttling_exception.ThrottlingException: <p>Your request rate is too high. Reduce the frequency of requests.</p>
            capo_lex_models_v2.errors.validation_exception.ValidationException: <p>One of the input parameters in your request isn't valid. Check the parameters and try your request again.</p>
            capo_lex_models_v2.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        async def _handler(
            req: "AsyncOperationRequest[capo_lex_models_v2.types.create_intent_request.CreateIntentRequest]",
        ) -> AsyncOperationResponse[
            "capo_lex_models_v2.types.create_intent_response.CreateIntentResponse"
        ]:
            import capo_lex_models_v2._operations.lex_model_building_service_v2.create_intent

            (
                output,
                http_response,
            ) = await capo_lex_models_v2._operations.lex_model_building_service_v2.create_intent.async_create_intent(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_lex_models_v2.types.create_intent_request.CreateIntentRequest = {
            "intent_name": intent_name,
            "bot_id": bot_id,
            "bot_version": bot_version,
            "locale_id": locale_id,
        }
        if intent_display_name is not None:
            input_["intent_display_name"] = intent_display_name
        if description is not None:
            input_["description"] = description
        if parent_intent_signature is not None:
            input_["parent_intent_signature"] = parent_intent_signature
        if sample_utterances is not None:
            input_["sample_utterances"] = sample_utterances
        if dialog_code_hook is not None:
            input_["dialog_code_hook"] = dialog_code_hook
        if fulfillment_code_hook is not None:
            input_["fulfillment_code_hook"] = fulfillment_code_hook
        if intent_confirmation_setting is not None:
            input_["intent_confirmation_setting"] = intent_confirmation_setting
        if intent_closing_setting is not None:
            input_["intent_closing_setting"] = intent_closing_setting
        if input_contexts is not None:
            input_["input_contexts"] = input_contexts
        if output_contexts is not None:
            input_["output_contexts"] = output_contexts
        if kendra_configuration is not None:
            input_["kendra_configuration"] = kendra_configuration
        if initial_response_setting is not None:
            input_["initial_response_setting"] = initial_response_setting
        if qn_a_intent_configuration is not None:
            input_["qn_a_intent_configuration"] = qn_a_intent_configuration
        if q_in_connect_intent_configuration is not None:
            input_["q_in_connect_intent_configuration"] = (
                q_in_connect_intent_configuration
            )

        response = await aexecute_pipeline(
            AsyncOperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        await response.response.aclose()
        return response.output

    async def create_resource_policy(
        self,
        resource_arn: "capo_lex_models_v2.types.amazon_resource_name.AmazonResourceName",
        policy: "capo_lex_models_v2.types.policy.Policy",
        *,
        config_overrides: Optional[AsyncLexModelsV2ClientConfig] = None,
    ) -> "capo_lex_models_v2.types.create_resource_policy_response.CreateResourcePolicyResponse":
        """<p>Creates a new resource policy with the specified policy statements.</p>

        Args:
            resource_arn: <p>The Amazon Resource Name (ARN) of the bot or bot alias that the resource policy is attached to.</p>
            policy: <p>A resource policy to add to the resource. The policy is a JSON structure that contains one or more statements that define the policy. The policy must follow the IAM syntax. For more information about the contents of a JSON policy document, see <a href="https://docs.aws.amazon.com/IAM/latest/UserGuide/reference_policies.html"> IAM JSON policy reference </a>. </p> <p>If the policy isn't valid, Amazon Lex returns a validation exception.</p>

        Raises:
            capo_lex_models_v2.errors.internal_server_exception.InternalServerException: <p>The service encountered an unexpected condition. Try your request again.</p>
            capo_lex_models_v2.errors.precondition_failed_exception.PreconditionFailedException: <p>Your request couldn't be completed because one or more request fields aren't valid. Check the fields in your request and try again.</p>
            capo_lex_models_v2.errors.resource_not_found_exception.ResourceNotFoundException: <p>You asked to describe a resource that doesn't exist. Check the resource that you are requesting and try again.</p>
            capo_lex_models_v2.errors.service_quota_exceeded_exception.ServiceQuotaExceededException: <p>You have reached a quota for your bot. </p>
            capo_lex_models_v2.errors.throttling_exception.ThrottlingException: <p>Your request rate is too high. Reduce the frequency of requests.</p>
            capo_lex_models_v2.errors.validation_exception.ValidationException: <p>One of the input parameters in your request isn't valid. Check the parameters and try your request again.</p>
            capo_lex_models_v2.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        async def _handler(
            req: "AsyncOperationRequest[capo_lex_models_v2.types.create_resource_policy_request.CreateResourcePolicyRequest]",
        ) -> AsyncOperationResponse[
            "capo_lex_models_v2.types.create_resource_policy_response.CreateResourcePolicyResponse"
        ]:
            import capo_lex_models_v2._operations.lex_model_building_service_v2.create_resource_policy

            (
                output,
                http_response,
            ) = await capo_lex_models_v2._operations.lex_model_building_service_v2.create_resource_policy.async_create_resource_policy(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_lex_models_v2.types.create_resource_policy_request.CreateResourcePolicyRequest = {
            "resource_arn": resource_arn,
            "policy": policy,
        }

        response = await aexecute_pipeline(
            AsyncOperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        await response.response.aclose()
        return response.output

    async def create_resource_policy_statement(
        self,
        resource_arn: "capo_lex_models_v2.types.amazon_resource_name.AmazonResourceName",
        statement_id: "capo_lex_models_v2.types.name.Name",
        effect: "capo_lex_models_v2.types.effect.Effect",
        principal: "capo_lex_models_v2.types.principal_list.PrincipalList",
        action: "capo_lex_models_v2.types.operation_list.OperationList",
        *,
        config_overrides: Optional[AsyncLexModelsV2ClientConfig] = None,
        condition: Optional[
            "capo_lex_models_v2.types.condition_map.ConditionMap"
        ] = None,
        expected_revision_id: Optional[
            "capo_lex_models_v2.types.revision_id.RevisionId"
        ] = None,
    ) -> "capo_lex_models_v2.types.create_resource_policy_statement_response.CreateResourcePolicyStatementResponse":
        """<p>Adds a new resource policy statement to a bot or bot alias. If a resource policy exists, the statement is added to the current resource policy. If a policy doesn't exist, a new policy is created.</p> <p>You can't create a resource policy statement that allows cross-account access.</p> <p>You need to add the <code>CreateResourcePolicy</code> or <code>UpdateResourcePolicy</code> action to the bot role in order to call the API.</p>

        Args:
            resource_arn: <p>The Amazon Resource Name (ARN) of the bot or bot alias that the resource policy is attached to.</p>
            statement_id: <p>The name of the statement. The ID is the same as the <code>Sid</code> IAM property. The statement name must be unique within the policy. For more information, see <a href="https://docs.aws.amazon.com/IAM/latest/UserGuide/reference_policies_elements_sid.html">IAM JSON policy elements: Sid</a>. </p>
            effect: <p>Determines whether the statement allows or denies access to the resource.</p>
            principal: <p>An IAM principal, such as an IAM user, IAM role, or Amazon Web Services services that is allowed or denied access to a resource. For more information, see <a href="https://docs.aws.amazon.com/IAM/latest/UserGuide/reference_policies_elements_principal.html">Amazon Web Services JSON policy elements: Principal</a>.</p>
            action: <p>The Amazon Lex action that this policy either allows or denies. The action must apply to the resource type of the specified ARN. For more information, see <a href="https://docs.aws.amazon.com/service-authorization/latest/reference/list_amazonlexv2.html"> Actions, resources, and condition keys for Amazon Lex V2</a>.</p>
            condition: <p>Specifies a condition when the policy is in effect. If the principal of the policy is a service principal, you must provide two condition blocks, one with a SourceAccount global condition key and one with a SourceArn global condition key.</p> <p>For more information, see <a href="https://docs.aws.amazon.com/IAM/latest/UserGuide/reference_policies_elements_condition.html">IAM JSON policy elements: Condition </a>.</p>
            expected_revision_id: <p>The identifier of the revision of the policy to edit. If this revision ID doesn't match the current revision ID, Amazon Lex throws an exception.</p> <p>If you don't specify a revision, Amazon Lex overwrites the contents of the policy with the new values.</p>

        Raises:
            capo_lex_models_v2.errors.conflict_exception.ConflictException: <p>The action that you tried to perform couldn't be completed because the resource is in a conflicting state. For example, deleting a bot that is in the CREATING state. Try your request again. </p>
            capo_lex_models_v2.errors.internal_server_exception.InternalServerException: <p>The service encountered an unexpected condition. Try your request again.</p>
            capo_lex_models_v2.errors.precondition_failed_exception.PreconditionFailedException: <p>Your request couldn't be completed because one or more request fields aren't valid. Check the fields in your request and try again.</p>
            capo_lex_models_v2.errors.resource_not_found_exception.ResourceNotFoundException: <p>You asked to describe a resource that doesn't exist. Check the resource that you are requesting and try again.</p>
            capo_lex_models_v2.errors.service_quota_exceeded_exception.ServiceQuotaExceededException: <p>You have reached a quota for your bot. </p>
            capo_lex_models_v2.errors.throttling_exception.ThrottlingException: <p>Your request rate is too high. Reduce the frequency of requests.</p>
            capo_lex_models_v2.errors.validation_exception.ValidationException: <p>One of the input parameters in your request isn't valid. Check the parameters and try your request again.</p>
            capo_lex_models_v2.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        async def _handler(
            req: "AsyncOperationRequest[capo_lex_models_v2.types.create_resource_policy_statement_request.CreateResourcePolicyStatementRequest]",
        ) -> AsyncOperationResponse[
            "capo_lex_models_v2.types.create_resource_policy_statement_response.CreateResourcePolicyStatementResponse"
        ]:
            import capo_lex_models_v2._operations.lex_model_building_service_v2.create_resource_policy_statement

            (
                output,
                http_response,
            ) = await capo_lex_models_v2._operations.lex_model_building_service_v2.create_resource_policy_statement.async_create_resource_policy_statement(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_lex_models_v2.types.create_resource_policy_statement_request.CreateResourcePolicyStatementRequest = {
            "resource_arn": resource_arn,
            "statement_id": statement_id,
            "effect": effect,
            "principal": principal,
            "action": action,
        }
        if condition is not None:
            input_["condition"] = condition
        if expected_revision_id is not None:
            input_["expected_revision_id"] = expected_revision_id

        response = await aexecute_pipeline(
            AsyncOperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        await response.response.aclose()
        return response.output

    async def create_slot(
        self,
        slot_name: "capo_lex_models_v2.types.name.Name",
        value_elicitation_setting: "capo_lex_models_v2.types.slot_value_elicitation_setting.SlotValueElicitationSetting",
        bot_id: "capo_lex_models_v2.types.id.Id",
        bot_version: "capo_lex_models_v2.types.draft_bot_version.DraftBotVersion",
        locale_id: "capo_lex_models_v2.types.locale_id.LocaleId",
        intent_id: "capo_lex_models_v2.types.id.Id",
        *,
        config_overrides: Optional[AsyncLexModelsV2ClientConfig] = None,
        description: Optional[
            "capo_lex_models_v2.types.description.Description"
        ] = None,
        slot_type_id: Optional[
            "capo_lex_models_v2.types.built_in_or_custom_slot_type_id.BuiltInOrCustomSlotTypeId"
        ] = None,
        obfuscation_setting: Optional[
            "capo_lex_models_v2.types.obfuscation_setting.ObfuscationSetting"
        ] = None,
        multiple_values_setting: Optional[
            "capo_lex_models_v2.types.multiple_values_setting.MultipleValuesSetting"
        ] = None,
        sub_slot_setting: Optional[
            "capo_lex_models_v2.types.sub_slot_setting.SubSlotSetting"
        ] = None,
    ) -> "capo_lex_models_v2.types.create_slot_response.CreateSlotResponse":
        """<p>Creates a slot in an intent. A slot is a variable needed to fulfill an intent. For example, an <code>OrderPizza</code> intent might need slots for size, crust, and number of pizzas. For each slot, you define one or more utterances that Amazon Lex uses to elicit a response from the user. </p>

        Args:
            slot_name: <p>The name of the slot. Slot names must be unique within the bot that contains the slot.</p>
            description: <p>A description of the slot. Use this to help identify the slot in lists.</p>
            slot_type_id: <p>The unique identifier for the slot type associated with this slot. The slot type determines the values that can be entered into the slot.</p>
            value_elicitation_setting: <p>Specifies prompts that Amazon Lex sends to the user to elicit a response that provides the value for the slot. </p>
            obfuscation_setting: <p>Determines how slot values are used in Amazon CloudWatch logs. If the value of the <code>obfuscationSetting</code> parameter is <code>DefaultObfuscation</code>, slot values are obfuscated in the log output. If the value is <code>None</code>, the actual value is present in the log output.</p> <p>The default is to obfuscate values in the CloudWatch logs.</p>
            bot_id: <p>The identifier of the bot associated with the slot.</p>
            bot_version: <p>The version of the bot associated with the slot.</p>
            locale_id: <p>The identifier of the language and locale that the slot will be used in. The string must match one of the supported locales. All of the bots, intents, slot types used by the slot must have the same locale. For more information, see <a href="https://docs.aws.amazon.com/lexv2/latest/dg/how-languages.html">Supported languages</a>.</p>
            intent_id: <p>The identifier of the intent that contains the slot.</p>
            multiple_values_setting: <p>Indicates whether the slot returns multiple values in one response. Multi-value slots are only available in the <code>en-US</code> locale. If you set this value to <code>true</code> in any other locale, Amazon Lex throws a <code>ValidationException</code>. </p> <p>If the <code>multipleValuesSetting</code> is not set, the default value is <code>false</code>.</p>
            sub_slot_setting: <p>Specifications for the constituent sub slots and the expression for the composite slot.</p>

        Raises:
            capo_lex_models_v2.errors.conflict_exception.ConflictException: <p>The action that you tried to perform couldn't be completed because the resource is in a conflicting state. For example, deleting a bot that is in the CREATING state. Try your request again. </p>
            capo_lex_models_v2.errors.internal_server_exception.InternalServerException: <p>The service encountered an unexpected condition. Try your request again.</p>
            capo_lex_models_v2.errors.precondition_failed_exception.PreconditionFailedException: <p>Your request couldn't be completed because one or more request fields aren't valid. Check the fields in your request and try again.</p>
            capo_lex_models_v2.errors.service_quota_exceeded_exception.ServiceQuotaExceededException: <p>You have reached a quota for your bot. </p>
            capo_lex_models_v2.errors.throttling_exception.ThrottlingException: <p>Your request rate is too high. Reduce the frequency of requests.</p>
            capo_lex_models_v2.errors.validation_exception.ValidationException: <p>One of the input parameters in your request isn't valid. Check the parameters and try your request again.</p>
            capo_lex_models_v2.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        async def _handler(
            req: "AsyncOperationRequest[capo_lex_models_v2.types.create_slot_request.CreateSlotRequest]",
        ) -> AsyncOperationResponse[
            "capo_lex_models_v2.types.create_slot_response.CreateSlotResponse"
        ]:
            import capo_lex_models_v2._operations.lex_model_building_service_v2.create_slot

            (
                output,
                http_response,
            ) = await capo_lex_models_v2._operations.lex_model_building_service_v2.create_slot.async_create_slot(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_lex_models_v2.types.create_slot_request.CreateSlotRequest = {
            "slot_name": slot_name,
            "value_elicitation_setting": value_elicitation_setting,
            "bot_id": bot_id,
            "bot_version": bot_version,
            "locale_id": locale_id,
            "intent_id": intent_id,
        }
        if description is not None:
            input_["description"] = description
        if slot_type_id is not None:
            input_["slot_type_id"] = slot_type_id
        if obfuscation_setting is not None:
            input_["obfuscation_setting"] = obfuscation_setting
        if multiple_values_setting is not None:
            input_["multiple_values_setting"] = multiple_values_setting
        if sub_slot_setting is not None:
            input_["sub_slot_setting"] = sub_slot_setting

        response = await aexecute_pipeline(
            AsyncOperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        await response.response.aclose()
        return response.output

    async def create_slot_type(
        self,
        slot_type_name: "capo_lex_models_v2.types.name.Name",
        bot_id: "capo_lex_models_v2.types.id.Id",
        bot_version: "capo_lex_models_v2.types.draft_bot_version.DraftBotVersion",
        locale_id: "capo_lex_models_v2.types.locale_id.LocaleId",
        *,
        config_overrides: Optional[AsyncLexModelsV2ClientConfig] = None,
        description: Optional[
            "capo_lex_models_v2.types.description.Description"
        ] = None,
        slot_type_values: Optional[
            "capo_lex_models_v2.types.slot_type_values.SlotTypeValues"
        ] = None,
        value_selection_setting: Optional[
            "capo_lex_models_v2.types.slot_value_selection_setting.SlotValueSelectionSetting"
        ] = None,
        parent_slot_type_signature: Optional[
            "capo_lex_models_v2.types.slot_type_signature.SlotTypeSignature"
        ] = None,
        external_source_setting: Optional[
            "capo_lex_models_v2.types.external_source_setting.ExternalSourceSetting"
        ] = None,
        composite_slot_type_setting: Optional[
            "capo_lex_models_v2.types.composite_slot_type_setting.CompositeSlotTypeSetting"
        ] = None,
    ) -> "capo_lex_models_v2.types.create_slot_type_response.CreateSlotTypeResponse":
        """<p>Creates a custom slot type</p> <p> To create a custom slot type, specify a name for the slot type and a set of enumeration values, the values that a slot of this type can assume. </p>

        Args:
            slot_type_name: <p>The name for the slot. A slot type name must be unique within the intent.</p>
            description: <p>A description of the slot type. Use the description to help identify the slot type in lists.</p>
            slot_type_values: <p>A list of <code>SlotTypeValue</code> objects that defines the values that the slot type can take. Each value can have a list of synonyms, additional values that help train the machine learning model about the values that it resolves for a slot.</p>
            value_selection_setting: <p>Determines the strategy that Amazon Lex uses to select a value from the list of possible values. The field can be set to one of the following values:</p> <ul> <li> <p> <code>ORIGINAL_VALUE</code> - Returns the value entered by the user, if the user value is similar to the slot value.</p> </li> <li> <p> <code>TOP_RESOLUTION</code> - If there is a resolution list for the slot, return the first value in the resolution list. If there is no resolution list, return null.</p> </li> </ul> <p>If you don't specify the <code>valueSelectionSetting</code> parameter, the default is <code>ORIGINAL_VALUE</code>.</p>
            parent_slot_type_signature: <p>The built-in slot type used as a parent of this slot type. When you define a parent slot type, the new slot type has the configuration of the parent slot type.</p> <p>Only <code>AMAZON.AlphaNumeric</code> is supported.</p>
            bot_id: <p>The identifier of the bot associated with this slot type.</p>
            bot_version: <p>The identifier of the bot version associated with this slot type.</p>
            locale_id: <p>The identifier of the language and locale that the slot type will be used in. The string must match one of the supported locales. All of the bots, intents, and slots used by the slot type must have the same locale. For more information, see <a href="https://docs.aws.amazon.com/lexv2/latest/dg/how-languages.html">Supported languages</a>.</p>
            external_source_setting: <p>Sets the type of external information used to create the slot type.</p>
            composite_slot_type_setting: <p>Specifications for a composite slot type.</p>

        Raises:
            capo_lex_models_v2.errors.conflict_exception.ConflictException: <p>The action that you tried to perform couldn't be completed because the resource is in a conflicting state. For example, deleting a bot that is in the CREATING state. Try your request again. </p>
            capo_lex_models_v2.errors.internal_server_exception.InternalServerException: <p>The service encountered an unexpected condition. Try your request again.</p>
            capo_lex_models_v2.errors.precondition_failed_exception.PreconditionFailedException: <p>Your request couldn't be completed because one or more request fields aren't valid. Check the fields in your request and try again.</p>
            capo_lex_models_v2.errors.service_quota_exceeded_exception.ServiceQuotaExceededException: <p>You have reached a quota for your bot. </p>
            capo_lex_models_v2.errors.throttling_exception.ThrottlingException: <p>Your request rate is too high. Reduce the frequency of requests.</p>
            capo_lex_models_v2.errors.validation_exception.ValidationException: <p>One of the input parameters in your request isn't valid. Check the parameters and try your request again.</p>
            capo_lex_models_v2.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        async def _handler(
            req: "AsyncOperationRequest[capo_lex_models_v2.types.create_slot_type_request.CreateSlotTypeRequest]",
        ) -> AsyncOperationResponse[
            "capo_lex_models_v2.types.create_slot_type_response.CreateSlotTypeResponse"
        ]:
            import capo_lex_models_v2._operations.lex_model_building_service_v2.create_slot_type

            (
                output,
                http_response,
            ) = await capo_lex_models_v2._operations.lex_model_building_service_v2.create_slot_type.async_create_slot_type(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_lex_models_v2.types.create_slot_type_request.CreateSlotTypeRequest = {
            "slot_type_name": slot_type_name,
            "bot_id": bot_id,
            "bot_version": bot_version,
            "locale_id": locale_id,
        }
        if description is not None:
            input_["description"] = description
        if slot_type_values is not None:
            input_["slot_type_values"] = slot_type_values
        if value_selection_setting is not None:
            input_["value_selection_setting"] = value_selection_setting
        if parent_slot_type_signature is not None:
            input_["parent_slot_type_signature"] = parent_slot_type_signature
        if external_source_setting is not None:
            input_["external_source_setting"] = external_source_setting
        if composite_slot_type_setting is not None:
            input_["composite_slot_type_setting"] = composite_slot_type_setting

        response = await aexecute_pipeline(
            AsyncOperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        await response.response.aclose()
        return response.output

    async def create_test_set_discrepancy_report(
        self,
        test_set_id: "capo_lex_models_v2.types.id.Id",
        target: "capo_lex_models_v2.types.test_set_discrepancy_report_resource_target.TestSetDiscrepancyReportResourceTarget",
        *,
        config_overrides: Optional[AsyncLexModelsV2ClientConfig] = None,
    ) -> "capo_lex_models_v2.types.create_test_set_discrepancy_report_response.CreateTestSetDiscrepancyReportResponse":
        """<p>Create a report that describes the differences between the bot and the test set.</p>

        Args:
            test_set_id: <p>The test set Id for the test set discrepancy report.</p>
            target: <p>The target bot for the test set discrepancy report.</p>

        Raises:
            capo_lex_models_v2.errors.conflict_exception.ConflictException: <p>The action that you tried to perform couldn't be completed because the resource is in a conflicting state. For example, deleting a bot that is in the CREATING state. Try your request again. </p>
            capo_lex_models_v2.errors.internal_server_exception.InternalServerException: <p>The service encountered an unexpected condition. Try your request again.</p>
            capo_lex_models_v2.errors.resource_not_found_exception.ResourceNotFoundException: <p>You asked to describe a resource that doesn't exist. Check the resource that you are requesting and try again.</p>
            capo_lex_models_v2.errors.service_quota_exceeded_exception.ServiceQuotaExceededException: <p>You have reached a quota for your bot. </p>
            capo_lex_models_v2.errors.throttling_exception.ThrottlingException: <p>Your request rate is too high. Reduce the frequency of requests.</p>
            capo_lex_models_v2.errors.validation_exception.ValidationException: <p>One of the input parameters in your request isn't valid. Check the parameters and try your request again.</p>
            capo_lex_models_v2.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        async def _handler(
            req: "AsyncOperationRequest[capo_lex_models_v2.types.create_test_set_discrepancy_report_request.CreateTestSetDiscrepancyReportRequest]",
        ) -> AsyncOperationResponse[
            "capo_lex_models_v2.types.create_test_set_discrepancy_report_response.CreateTestSetDiscrepancyReportResponse"
        ]:
            import capo_lex_models_v2._operations.lex_model_building_service_v2.create_test_set_discrepancy_report

            (
                output,
                http_response,
            ) = await capo_lex_models_v2._operations.lex_model_building_service_v2.create_test_set_discrepancy_report.async_create_test_set_discrepancy_report(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_lex_models_v2.types.create_test_set_discrepancy_report_request.CreateTestSetDiscrepancyReportRequest = {
            "test_set_id": test_set_id,
            "target": target,
        }

        response = await aexecute_pipeline(
            AsyncOperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        await response.response.aclose()
        return response.output

    async def create_upload_url(
        self, *, config_overrides: Optional[AsyncLexModelsV2ClientConfig] = None
    ) -> "capo_lex_models_v2.types.create_upload_url_response.CreateUploadUrlResponse":
        """<p>Gets a pre-signed S3 write URL that you use to upload the zip archive when importing a bot or a bot locale. </p>

        Raises:
            capo_lex_models_v2.errors.conflict_exception.ConflictException: <p>The action that you tried to perform couldn't be completed because the resource is in a conflicting state. For example, deleting a bot that is in the CREATING state. Try your request again. </p>
            capo_lex_models_v2.errors.internal_server_exception.InternalServerException: <p>The service encountered an unexpected condition. Try your request again.</p>
            capo_lex_models_v2.errors.resource_not_found_exception.ResourceNotFoundException: <p>You asked to describe a resource that doesn't exist. Check the resource that you are requesting and try again.</p>
            capo_lex_models_v2.errors.throttling_exception.ThrottlingException: <p>Your request rate is too high. Reduce the frequency of requests.</p>
            capo_lex_models_v2.errors.validation_exception.ValidationException: <p>One of the input parameters in your request isn't valid. Check the parameters and try your request again.</p>
            capo_lex_models_v2.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        async def _handler(
            req: "AsyncOperationRequest[capo_lex_models_v2.types.create_upload_url_request.CreateUploadUrlRequest]",
        ) -> AsyncOperationResponse[
            "capo_lex_models_v2.types.create_upload_url_response.CreateUploadUrlResponse"
        ]:
            import capo_lex_models_v2._operations.lex_model_building_service_v2.create_upload_url

            (
                output,
                http_response,
            ) = await capo_lex_models_v2._operations.lex_model_building_service_v2.create_upload_url.async_create_upload_url(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_lex_models_v2.types.create_upload_url_request.CreateUploadUrlRequest = {}

        response = await aexecute_pipeline(
            AsyncOperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        await response.response.aclose()
        return response.output

    async def delete_bot(
        self,
        bot_id: "capo_lex_models_v2.types.id.Id",
        *,
        config_overrides: Optional[AsyncLexModelsV2ClientConfig] = None,
        skip_resource_in_use_check: Optional[
            "capo_lex_models_v2.types.skip_resource_in_use_check.SkipResourceInUseCheck"
        ] = None,
    ) -> "capo_lex_models_v2.types.delete_bot_response.DeleteBotResponse":
        """<p>Deletes all versions of a bot, including the <code>Draft</code> version. To delete a specific version, use the <code>DeleteBotVersion</code> operation.</p> <p>When you delete a bot, all of the resources contained in the bot are also deleted. Deleting a bot removes all locales, intents, slot, and slot types defined for the bot.</p> <p>If a bot has an alias, the <code>DeleteBot</code> operation returns a <code>ResourceInUseException</code> exception. If you want to delete the bot and the alias, set the <code>skipResourceInUseCheck</code> parameter to <code>true</code>.</p>

        Args:
            bot_id: <p>The identifier of the bot to delete. </p>
            skip_resource_in_use_check: <p>By default, Amazon Lex checks if any other resource, such as an alias or bot network, is using the bot version before it is deleted and throws a <code>ResourceInUseException</code> exception if the bot is being used by another resource. Set this parameter to <code>true</code> to skip this check and remove the bot even if it is being used by another resource.</p>

        Raises:
            capo_lex_models_v2.errors.conflict_exception.ConflictException: <p>The action that you tried to perform couldn't be completed because the resource is in a conflicting state. For example, deleting a bot that is in the CREATING state. Try your request again. </p>
            capo_lex_models_v2.errors.internal_server_exception.InternalServerException: <p>The service encountered an unexpected condition. Try your request again.</p>
            capo_lex_models_v2.errors.precondition_failed_exception.PreconditionFailedException: <p>Your request couldn't be completed because one or more request fields aren't valid. Check the fields in your request and try again.</p>
            capo_lex_models_v2.errors.service_quota_exceeded_exception.ServiceQuotaExceededException: <p>You have reached a quota for your bot. </p>
            capo_lex_models_v2.errors.throttling_exception.ThrottlingException: <p>Your request rate is too high. Reduce the frequency of requests.</p>
            capo_lex_models_v2.errors.validation_exception.ValidationException: <p>One of the input parameters in your request isn't valid. Check the parameters and try your request again.</p>
            capo_lex_models_v2.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        async def _handler(
            req: "AsyncOperationRequest[capo_lex_models_v2.types.delete_bot_request.DeleteBotRequest]",
        ) -> AsyncOperationResponse[
            "capo_lex_models_v2.types.delete_bot_response.DeleteBotResponse"
        ]:
            import capo_lex_models_v2._operations.lex_model_building_service_v2.delete_bot

            (
                output,
                http_response,
            ) = await capo_lex_models_v2._operations.lex_model_building_service_v2.delete_bot.async_delete_bot(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_lex_models_v2.types.delete_bot_request.DeleteBotRequest = {
            "bot_id": bot_id
        }
        if skip_resource_in_use_check is not None:
            input_["skip_resource_in_use_check"] = skip_resource_in_use_check

        response = await aexecute_pipeline(
            AsyncOperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        await response.response.aclose()
        return response.output

    async def delete_bot_alias(
        self,
        bot_alias_id: "capo_lex_models_v2.types.bot_alias_id.BotAliasId",
        bot_id: "capo_lex_models_v2.types.id.Id",
        *,
        config_overrides: Optional[AsyncLexModelsV2ClientConfig] = None,
        skip_resource_in_use_check: Optional[
            "capo_lex_models_v2.types.skip_resource_in_use_check.SkipResourceInUseCheck"
        ] = None,
    ) -> "capo_lex_models_v2.types.delete_bot_alias_response.DeleteBotAliasResponse":
        """<p>Deletes the specified bot alias.</p>

        Args:
            bot_alias_id: <p>The unique identifier of the bot alias to delete.</p>
            bot_id: <p>The unique identifier of the bot associated with the alias to delete.</p>
            skip_resource_in_use_check: <p>By default, Amazon Lex checks if any other resource, such as a bot network, is using the bot alias before it is deleted and throws a <code>ResourceInUseException</code> exception if the alias is being used by another resource. Set this parameter to <code>true</code> to skip this check and remove the alias even if it is being used by another resource.</p>

        Raises:
            capo_lex_models_v2.errors.conflict_exception.ConflictException: <p>The action that you tried to perform couldn't be completed because the resource is in a conflicting state. For example, deleting a bot that is in the CREATING state. Try your request again. </p>
            capo_lex_models_v2.errors.internal_server_exception.InternalServerException: <p>The service encountered an unexpected condition. Try your request again.</p>
            capo_lex_models_v2.errors.precondition_failed_exception.PreconditionFailedException: <p>Your request couldn't be completed because one or more request fields aren't valid. Check the fields in your request and try again.</p>
            capo_lex_models_v2.errors.service_quota_exceeded_exception.ServiceQuotaExceededException: <p>You have reached a quota for your bot. </p>
            capo_lex_models_v2.errors.throttling_exception.ThrottlingException: <p>Your request rate is too high. Reduce the frequency of requests.</p>
            capo_lex_models_v2.errors.validation_exception.ValidationException: <p>One of the input parameters in your request isn't valid. Check the parameters and try your request again.</p>
            capo_lex_models_v2.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        async def _handler(
            req: "AsyncOperationRequest[capo_lex_models_v2.types.delete_bot_alias_request.DeleteBotAliasRequest]",
        ) -> AsyncOperationResponse[
            "capo_lex_models_v2.types.delete_bot_alias_response.DeleteBotAliasResponse"
        ]:
            import capo_lex_models_v2._operations.lex_model_building_service_v2.delete_bot_alias

            (
                output,
                http_response,
            ) = await capo_lex_models_v2._operations.lex_model_building_service_v2.delete_bot_alias.async_delete_bot_alias(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_lex_models_v2.types.delete_bot_alias_request.DeleteBotAliasRequest = {
            "bot_alias_id": bot_alias_id,
            "bot_id": bot_id,
        }
        if skip_resource_in_use_check is not None:
            input_["skip_resource_in_use_check"] = skip_resource_in_use_check

        response = await aexecute_pipeline(
            AsyncOperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        await response.response.aclose()
        return response.output

    async def delete_bot_analyzer_recommendation(
        self,
        bot_id: "capo_lex_models_v2.types.id.Id",
        bot_analyzer_request_id: "capo_lex_models_v2.types.uuid.UUID",
        *,
        config_overrides: Optional[AsyncLexModelsV2ClientConfig] = None,
    ) -> "capo_lex_models_v2.types.delete_bot_analyzer_recommendation_response.DeleteBotAnalyzerRecommendationResponse":
        """<p>Permanently deletes the recommendations and analysis results for a specific bot analysis request. This operation is provided for GDPR compliance and cannot be undone.</p> <p>After deletion, the analysis results cannot be retrieved. The analysis request ID will still appear in the history list, but attempting to describe the recommendations will return a <code>ResourceNotFoundException</code>.</p>

        Args:
            bot_id: <p>The unique identifier of the bot.</p>
            bot_analyzer_request_id: <p>The unique identifier of the analysis request whose recommendations should be deleted.</p>

        Raises:
            capo_lex_models_v2.errors.internal_server_exception.InternalServerException: <p>The service encountered an unexpected condition. Try your request again.</p>
            capo_lex_models_v2.errors.resource_not_found_exception.ResourceNotFoundException: <p>You asked to describe a resource that doesn't exist. Check the resource that you are requesting and try again.</p>
            capo_lex_models_v2.errors.throttling_exception.ThrottlingException: <p>Your request rate is too high. Reduce the frequency of requests.</p>
            capo_lex_models_v2.errors.validation_exception.ValidationException: <p>One of the input parameters in your request isn't valid. Check the parameters and try your request again.</p>
            capo_lex_models_v2.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        async def _handler(
            req: "AsyncOperationRequest[capo_lex_models_v2.types.delete_bot_analyzer_recommendation_request.DeleteBotAnalyzerRecommendationRequest]",
        ) -> AsyncOperationResponse[
            "capo_lex_models_v2.types.delete_bot_analyzer_recommendation_response.DeleteBotAnalyzerRecommendationResponse"
        ]:
            import capo_lex_models_v2._operations.lex_model_building_service_v2.delete_bot_analyzer_recommendation

            (
                output,
                http_response,
            ) = await capo_lex_models_v2._operations.lex_model_building_service_v2.delete_bot_analyzer_recommendation.async_delete_bot_analyzer_recommendation(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_lex_models_v2.types.delete_bot_analyzer_recommendation_request.DeleteBotAnalyzerRecommendationRequest = {
            "bot_id": bot_id,
            "bot_analyzer_request_id": bot_analyzer_request_id,
        }

        response = await aexecute_pipeline(
            AsyncOperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        await response.response.aclose()
        return response.output

    async def delete_bot_locale(
        self,
        bot_id: "capo_lex_models_v2.types.id.Id",
        bot_version: "capo_lex_models_v2.types.draft_bot_version.DraftBotVersion",
        locale_id: "capo_lex_models_v2.types.locale_id.LocaleId",
        *,
        config_overrides: Optional[AsyncLexModelsV2ClientConfig] = None,
    ) -> "capo_lex_models_v2.types.delete_bot_locale_response.DeleteBotLocaleResponse":
        """<p>Removes a locale from a bot.</p> <p>When you delete a locale, all intents, slots, and slot types defined for the locale are also deleted.</p>

        Args:
            bot_id: <p>The unique identifier of the bot that contains the locale.</p>
            bot_version: <p>The version of the bot that contains the locale. </p>
            locale_id: <p>The identifier of the language and locale that will be deleted. The string must match one of the supported locales. For more information, see <a href="https://docs.aws.amazon.com/lexv2/latest/dg/how-languages.html">Supported languages</a>.</p>

        Raises:
            capo_lex_models_v2.errors.conflict_exception.ConflictException: <p>The action that you tried to perform couldn't be completed because the resource is in a conflicting state. For example, deleting a bot that is in the CREATING state. Try your request again. </p>
            capo_lex_models_v2.errors.internal_server_exception.InternalServerException: <p>The service encountered an unexpected condition. Try your request again.</p>
            capo_lex_models_v2.errors.precondition_failed_exception.PreconditionFailedException: <p>Your request couldn't be completed because one or more request fields aren't valid. Check the fields in your request and try again.</p>
            capo_lex_models_v2.errors.service_quota_exceeded_exception.ServiceQuotaExceededException: <p>You have reached a quota for your bot. </p>
            capo_lex_models_v2.errors.throttling_exception.ThrottlingException: <p>Your request rate is too high. Reduce the frequency of requests.</p>
            capo_lex_models_v2.errors.validation_exception.ValidationException: <p>One of the input parameters in your request isn't valid. Check the parameters and try your request again.</p>
            capo_lex_models_v2.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        async def _handler(
            req: "AsyncOperationRequest[capo_lex_models_v2.types.delete_bot_locale_request.DeleteBotLocaleRequest]",
        ) -> AsyncOperationResponse[
            "capo_lex_models_v2.types.delete_bot_locale_response.DeleteBotLocaleResponse"
        ]:
            import capo_lex_models_v2._operations.lex_model_building_service_v2.delete_bot_locale

            (
                output,
                http_response,
            ) = await capo_lex_models_v2._operations.lex_model_building_service_v2.delete_bot_locale.async_delete_bot_locale(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_lex_models_v2.types.delete_bot_locale_request.DeleteBotLocaleRequest = {
            "bot_id": bot_id,
            "bot_version": bot_version,
            "locale_id": locale_id,
        }

        response = await aexecute_pipeline(
            AsyncOperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        await response.response.aclose()
        return response.output

    async def delete_bot_replica(
        self,
        bot_id: "capo_lex_models_v2.types.id.Id",
        replica_region: "capo_lex_models_v2.types.replica_region.ReplicaRegion",
        *,
        config_overrides: Optional[AsyncLexModelsV2ClientConfig] = None,
    ) -> (
        "capo_lex_models_v2.types.delete_bot_replica_response.DeleteBotReplicaResponse"
    ):
        """<p>The action to delete the replicated bot in the secondary region.</p>

        Args:
            bot_id: <p>The unique ID of the replicated bot to be deleted from the secondary region</p>
            replica_region: <p>The secondary region of the replicated bot that will be deleted.</p>

        Raises:
            capo_lex_models_v2.errors.conflict_exception.ConflictException: <p>The action that you tried to perform couldn't be completed because the resource is in a conflicting state. For example, deleting a bot that is in the CREATING state. Try your request again. </p>
            capo_lex_models_v2.errors.internal_server_exception.InternalServerException: <p>The service encountered an unexpected condition. Try your request again.</p>
            capo_lex_models_v2.errors.precondition_failed_exception.PreconditionFailedException: <p>Your request couldn't be completed because one or more request fields aren't valid. Check the fields in your request and try again.</p>
            capo_lex_models_v2.errors.service_quota_exceeded_exception.ServiceQuotaExceededException: <p>You have reached a quota for your bot. </p>
            capo_lex_models_v2.errors.throttling_exception.ThrottlingException: <p>Your request rate is too high. Reduce the frequency of requests.</p>
            capo_lex_models_v2.errors.validation_exception.ValidationException: <p>One of the input parameters in your request isn't valid. Check the parameters and try your request again.</p>
            capo_lex_models_v2.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        async def _handler(
            req: "AsyncOperationRequest[capo_lex_models_v2.types.delete_bot_replica_request.DeleteBotReplicaRequest]",
        ) -> AsyncOperationResponse[
            "capo_lex_models_v2.types.delete_bot_replica_response.DeleteBotReplicaResponse"
        ]:
            import capo_lex_models_v2._operations.lex_model_building_service_v2.delete_bot_replica

            (
                output,
                http_response,
            ) = await capo_lex_models_v2._operations.lex_model_building_service_v2.delete_bot_replica.async_delete_bot_replica(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_lex_models_v2.types.delete_bot_replica_request.DeleteBotReplicaRequest = {
            "bot_id": bot_id,
            "replica_region": replica_region,
        }

        response = await aexecute_pipeline(
            AsyncOperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        await response.response.aclose()
        return response.output

    async def delete_bot_version(
        self,
        bot_id: "capo_lex_models_v2.types.id.Id",
        bot_version: "capo_lex_models_v2.types.numerical_bot_version.NumericalBotVersion",
        *,
        config_overrides: Optional[AsyncLexModelsV2ClientConfig] = None,
        skip_resource_in_use_check: Optional[
            "capo_lex_models_v2.types.skip_resource_in_use_check.SkipResourceInUseCheck"
        ] = None,
    ) -> (
        "capo_lex_models_v2.types.delete_bot_version_response.DeleteBotVersionResponse"
    ):
        """<p>Deletes a specific version of a bot. To delete all versions of a bot, use the <a href="https://docs.aws.amazon.com/lexv2/latest/APIReference/API_DeleteBot.html">DeleteBot</a> operation.</p>

        Args:
            bot_id: <p>The identifier of the bot that contains the version.</p>
            bot_version: <p>The version of the bot to delete.</p>
            skip_resource_in_use_check: <p>By default, Amazon Lex checks if any other resource, such as an alias or bot network, is using the bot version before it is deleted and throws a <code>ResourceInUseException</code> exception if the version is being used by another resource. Set this parameter to <code>true</code> to skip this check and remove the version even if it is being used by another resource.</p>

        Raises:
            capo_lex_models_v2.errors.conflict_exception.ConflictException: <p>The action that you tried to perform couldn't be completed because the resource is in a conflicting state. For example, deleting a bot that is in the CREATING state. Try your request again. </p>
            capo_lex_models_v2.errors.internal_server_exception.InternalServerException: <p>The service encountered an unexpected condition. Try your request again.</p>
            capo_lex_models_v2.errors.precondition_failed_exception.PreconditionFailedException: <p>Your request couldn't be completed because one or more request fields aren't valid. Check the fields in your request and try again.</p>
            capo_lex_models_v2.errors.service_quota_exceeded_exception.ServiceQuotaExceededException: <p>You have reached a quota for your bot. </p>
            capo_lex_models_v2.errors.throttling_exception.ThrottlingException: <p>Your request rate is too high. Reduce the frequency of requests.</p>
            capo_lex_models_v2.errors.validation_exception.ValidationException: <p>One of the input parameters in your request isn't valid. Check the parameters and try your request again.</p>
            capo_lex_models_v2.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        async def _handler(
            req: "AsyncOperationRequest[capo_lex_models_v2.types.delete_bot_version_request.DeleteBotVersionRequest]",
        ) -> AsyncOperationResponse[
            "capo_lex_models_v2.types.delete_bot_version_response.DeleteBotVersionResponse"
        ]:
            import capo_lex_models_v2._operations.lex_model_building_service_v2.delete_bot_version

            (
                output,
                http_response,
            ) = await capo_lex_models_v2._operations.lex_model_building_service_v2.delete_bot_version.async_delete_bot_version(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_lex_models_v2.types.delete_bot_version_request.DeleteBotVersionRequest = {
            "bot_id": bot_id,
            "bot_version": bot_version,
        }
        if skip_resource_in_use_check is not None:
            input_["skip_resource_in_use_check"] = skip_resource_in_use_check

        response = await aexecute_pipeline(
            AsyncOperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        await response.response.aclose()
        return response.output

    async def delete_custom_vocabulary(
        self,
        bot_id: "capo_lex_models_v2.types.id.Id",
        bot_version: "capo_lex_models_v2.types.draft_bot_version.DraftBotVersion",
        locale_id: "capo_lex_models_v2.types.locale_id.LocaleId",
        *,
        config_overrides: Optional[AsyncLexModelsV2ClientConfig] = None,
    ) -> "capo_lex_models_v2.types.delete_custom_vocabulary_response.DeleteCustomVocabularyResponse":
        """<p>Removes a custom vocabulary from the specified locale in the specified bot.</p>

        Args:
            bot_id: <p>The unique identifier of the bot to remove the custom vocabulary from.</p>
            bot_version: <p>The version of the bot to remove the custom vocabulary from.</p>
            locale_id: <p>The locale identifier for the locale that contains the custom vocabulary to remove.</p>

        Raises:
            capo_lex_models_v2.errors.conflict_exception.ConflictException: <p>The action that you tried to perform couldn't be completed because the resource is in a conflicting state. For example, deleting a bot that is in the CREATING state. Try your request again. </p>
            capo_lex_models_v2.errors.internal_server_exception.InternalServerException: <p>The service encountered an unexpected condition. Try your request again.</p>
            capo_lex_models_v2.errors.precondition_failed_exception.PreconditionFailedException: <p>Your request couldn't be completed because one or more request fields aren't valid. Check the fields in your request and try again.</p>
            capo_lex_models_v2.errors.service_quota_exceeded_exception.ServiceQuotaExceededException: <p>You have reached a quota for your bot. </p>
            capo_lex_models_v2.errors.throttling_exception.ThrottlingException: <p>Your request rate is too high. Reduce the frequency of requests.</p>
            capo_lex_models_v2.errors.validation_exception.ValidationException: <p>One of the input parameters in your request isn't valid. Check the parameters and try your request again.</p>
            capo_lex_models_v2.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        async def _handler(
            req: "AsyncOperationRequest[capo_lex_models_v2.types.delete_custom_vocabulary_request.DeleteCustomVocabularyRequest]",
        ) -> AsyncOperationResponse[
            "capo_lex_models_v2.types.delete_custom_vocabulary_response.DeleteCustomVocabularyResponse"
        ]:
            import capo_lex_models_v2._operations.lex_model_building_service_v2.delete_custom_vocabulary

            (
                output,
                http_response,
            ) = await capo_lex_models_v2._operations.lex_model_building_service_v2.delete_custom_vocabulary.async_delete_custom_vocabulary(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_lex_models_v2.types.delete_custom_vocabulary_request.DeleteCustomVocabularyRequest = {
            "bot_id": bot_id,
            "bot_version": bot_version,
            "locale_id": locale_id,
        }

        response = await aexecute_pipeline(
            AsyncOperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        await response.response.aclose()
        return response.output

    async def delete_export(
        self,
        export_id: "capo_lex_models_v2.types.id.Id",
        *,
        config_overrides: Optional[AsyncLexModelsV2ClientConfig] = None,
    ) -> "capo_lex_models_v2.types.delete_export_response.DeleteExportResponse":
        """<p>Removes a previous export and the associated files stored in an S3 bucket.</p>

        Args:
            export_id: <p>The unique identifier of the export to delete.</p>

        Raises:
            capo_lex_models_v2.errors.internal_server_exception.InternalServerException: <p>The service encountered an unexpected condition. Try your request again.</p>
            capo_lex_models_v2.errors.precondition_failed_exception.PreconditionFailedException: <p>Your request couldn't be completed because one or more request fields aren't valid. Check the fields in your request and try again.</p>
            capo_lex_models_v2.errors.service_quota_exceeded_exception.ServiceQuotaExceededException: <p>You have reached a quota for your bot. </p>
            capo_lex_models_v2.errors.throttling_exception.ThrottlingException: <p>Your request rate is too high. Reduce the frequency of requests.</p>
            capo_lex_models_v2.errors.validation_exception.ValidationException: <p>One of the input parameters in your request isn't valid. Check the parameters and try your request again.</p>
            capo_lex_models_v2.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        async def _handler(
            req: "AsyncOperationRequest[capo_lex_models_v2.types.delete_export_request.DeleteExportRequest]",
        ) -> AsyncOperationResponse[
            "capo_lex_models_v2.types.delete_export_response.DeleteExportResponse"
        ]:
            import capo_lex_models_v2._operations.lex_model_building_service_v2.delete_export

            (
                output,
                http_response,
            ) = await capo_lex_models_v2._operations.lex_model_building_service_v2.delete_export.async_delete_export(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_lex_models_v2.types.delete_export_request.DeleteExportRequest = {
            "export_id": export_id
        }

        response = await aexecute_pipeline(
            AsyncOperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        await response.response.aclose()
        return response.output

    async def delete_import(
        self,
        import_id: "capo_lex_models_v2.types.id.Id",
        *,
        config_overrides: Optional[AsyncLexModelsV2ClientConfig] = None,
    ) -> "capo_lex_models_v2.types.delete_import_response.DeleteImportResponse":
        """<p>Removes a previous import and the associated file stored in an S3 bucket.</p>

        Args:
            import_id: <p>The unique identifier of the import to delete.</p>

        Raises:
            capo_lex_models_v2.errors.internal_server_exception.InternalServerException: <p>The service encountered an unexpected condition. Try your request again.</p>
            capo_lex_models_v2.errors.precondition_failed_exception.PreconditionFailedException: <p>Your request couldn't be completed because one or more request fields aren't valid. Check the fields in your request and try again.</p>
            capo_lex_models_v2.errors.service_quota_exceeded_exception.ServiceQuotaExceededException: <p>You have reached a quota for your bot. </p>
            capo_lex_models_v2.errors.throttling_exception.ThrottlingException: <p>Your request rate is too high. Reduce the frequency of requests.</p>
            capo_lex_models_v2.errors.validation_exception.ValidationException: <p>One of the input parameters in your request isn't valid. Check the parameters and try your request again.</p>
            capo_lex_models_v2.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        async def _handler(
            req: "AsyncOperationRequest[capo_lex_models_v2.types.delete_import_request.DeleteImportRequest]",
        ) -> AsyncOperationResponse[
            "capo_lex_models_v2.types.delete_import_response.DeleteImportResponse"
        ]:
            import capo_lex_models_v2._operations.lex_model_building_service_v2.delete_import

            (
                output,
                http_response,
            ) = await capo_lex_models_v2._operations.lex_model_building_service_v2.delete_import.async_delete_import(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_lex_models_v2.types.delete_import_request.DeleteImportRequest = {
            "import_id": import_id
        }

        response = await aexecute_pipeline(
            AsyncOperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        await response.response.aclose()
        return response.output

    async def delete_intent(
        self,
        intent_id: "capo_lex_models_v2.types.id.Id",
        bot_id: "capo_lex_models_v2.types.id.Id",
        bot_version: "capo_lex_models_v2.types.draft_bot_version.DraftBotVersion",
        locale_id: "capo_lex_models_v2.types.locale_id.LocaleId",
        *,
        config_overrides: Optional[AsyncLexModelsV2ClientConfig] = None,
    ) -> None:
        """<p>Removes the specified intent.</p> <p>Deleting an intent also deletes the slots associated with the intent.</p>

        Args:
            intent_id: <p>The unique identifier of the intent to delete.</p>
            bot_id: <p>The identifier of the bot associated with the intent.</p>
            bot_version: <p>The version of the bot associated with the intent.</p>
            locale_id: <p>The identifier of the language and locale where the bot will be deleted. The string must match one of the supported locales. For more information, see <a href="https://docs.aws.amazon.com/lexv2/latest/dg/how-languages.html">Supported languages</a>.</p>

        Raises:
            capo_lex_models_v2.errors.conflict_exception.ConflictException: <p>The action that you tried to perform couldn't be completed because the resource is in a conflicting state. For example, deleting a bot that is in the CREATING state. Try your request again. </p>
            capo_lex_models_v2.errors.internal_server_exception.InternalServerException: <p>The service encountered an unexpected condition. Try your request again.</p>
            capo_lex_models_v2.errors.precondition_failed_exception.PreconditionFailedException: <p>Your request couldn't be completed because one or more request fields aren't valid. Check the fields in your request and try again.</p>
            capo_lex_models_v2.errors.service_quota_exceeded_exception.ServiceQuotaExceededException: <p>You have reached a quota for your bot. </p>
            capo_lex_models_v2.errors.throttling_exception.ThrottlingException: <p>Your request rate is too high. Reduce the frequency of requests.</p>
            capo_lex_models_v2.errors.validation_exception.ValidationException: <p>One of the input parameters in your request isn't valid. Check the parameters and try your request again.</p>
            capo_lex_models_v2.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        async def _handler(
            req: "AsyncOperationRequest[capo_lex_models_v2.types.delete_intent_request.DeleteIntentRequest]",
        ) -> AsyncOperationResponse[None]:
            import capo_lex_models_v2._operations.lex_model_building_service_v2.delete_intent

            (
                output,
                http_response,
            ) = await capo_lex_models_v2._operations.lex_model_building_service_v2.delete_intent.async_delete_intent(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_lex_models_v2.types.delete_intent_request.DeleteIntentRequest = {
            "intent_id": intent_id,
            "bot_id": bot_id,
            "bot_version": bot_version,
            "locale_id": locale_id,
        }

        response = await aexecute_pipeline(
            AsyncOperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        await response.response.aclose()
        return response.output

    async def delete_resource_policy(
        self,
        resource_arn: "capo_lex_models_v2.types.amazon_resource_name.AmazonResourceName",
        *,
        config_overrides: Optional[AsyncLexModelsV2ClientConfig] = None,
        expected_revision_id: Optional[
            "capo_lex_models_v2.types.revision_id.RevisionId"
        ] = None,
    ) -> "capo_lex_models_v2.types.delete_resource_policy_response.DeleteResourcePolicyResponse":
        """<p>Removes an existing policy from a bot or bot alias. If the resource doesn't have a policy attached, Amazon Lex returns an exception.</p>

        Args:
            resource_arn: <p>The Amazon Resource Name (ARN) of the bot or bot alias that has the resource policy attached.</p>
            expected_revision_id: <p>The identifier of the revision to edit. If this ID doesn't match the current revision number, Amazon Lex returns an exception</p> <p>If you don't specify a revision ID, Amazon Lex will delete the current policy.</p>

        Raises:
            capo_lex_models_v2.errors.internal_server_exception.InternalServerException: <p>The service encountered an unexpected condition. Try your request again.</p>
            capo_lex_models_v2.errors.precondition_failed_exception.PreconditionFailedException: <p>Your request couldn't be completed because one or more request fields aren't valid. Check the fields in your request and try again.</p>
            capo_lex_models_v2.errors.resource_not_found_exception.ResourceNotFoundException: <p>You asked to describe a resource that doesn't exist. Check the resource that you are requesting and try again.</p>
            capo_lex_models_v2.errors.throttling_exception.ThrottlingException: <p>Your request rate is too high. Reduce the frequency of requests.</p>
            capo_lex_models_v2.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        async def _handler(
            req: "AsyncOperationRequest[capo_lex_models_v2.types.delete_resource_policy_request.DeleteResourcePolicyRequest]",
        ) -> AsyncOperationResponse[
            "capo_lex_models_v2.types.delete_resource_policy_response.DeleteResourcePolicyResponse"
        ]:
            import capo_lex_models_v2._operations.lex_model_building_service_v2.delete_resource_policy

            (
                output,
                http_response,
            ) = await capo_lex_models_v2._operations.lex_model_building_service_v2.delete_resource_policy.async_delete_resource_policy(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_lex_models_v2.types.delete_resource_policy_request.DeleteResourcePolicyRequest = {
            "resource_arn": resource_arn
        }
        if expected_revision_id is not None:
            input_["expected_revision_id"] = expected_revision_id

        response = await aexecute_pipeline(
            AsyncOperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        await response.response.aclose()
        return response.output

    async def delete_resource_policy_statement(
        self,
        resource_arn: "capo_lex_models_v2.types.amazon_resource_name.AmazonResourceName",
        statement_id: "capo_lex_models_v2.types.name.Name",
        *,
        config_overrides: Optional[AsyncLexModelsV2ClientConfig] = None,
        expected_revision_id: Optional[
            "capo_lex_models_v2.types.revision_id.RevisionId"
        ] = None,
    ) -> "capo_lex_models_v2.types.delete_resource_policy_statement_response.DeleteResourcePolicyStatementResponse":
        """<p>Deletes a policy statement from a resource policy. If you delete the last statement from a policy, the policy is deleted. If you specify a statement ID that doesn't exist in the policy, or if the bot or bot alias doesn't have a policy attached, Amazon Lex returns an exception.</p> <p>You need to add the <code>DeleteResourcePolicy</code> or <code>UpdateResourcePolicy</code> action to the bot role in order to call the API.</p>

        Args:
            resource_arn: <p>The Amazon Resource Name (ARN) of the bot or bot alias that the resource policy is attached to.</p>
            statement_id: <p>The name of the statement (SID) to delete from the policy.</p>
            expected_revision_id: <p>The identifier of the revision of the policy to delete the statement from. If this revision ID doesn't match the current revision ID, Amazon Lex throws an exception.</p> <p>If you don't specify a revision, Amazon Lex removes the current contents of the statement. </p>

        Raises:
            capo_lex_models_v2.errors.internal_server_exception.InternalServerException: <p>The service encountered an unexpected condition. Try your request again.</p>
            capo_lex_models_v2.errors.precondition_failed_exception.PreconditionFailedException: <p>Your request couldn't be completed because one or more request fields aren't valid. Check the fields in your request and try again.</p>
            capo_lex_models_v2.errors.resource_not_found_exception.ResourceNotFoundException: <p>You asked to describe a resource that doesn't exist. Check the resource that you are requesting and try again.</p>
            capo_lex_models_v2.errors.throttling_exception.ThrottlingException: <p>Your request rate is too high. Reduce the frequency of requests.</p>
            capo_lex_models_v2.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        async def _handler(
            req: "AsyncOperationRequest[capo_lex_models_v2.types.delete_resource_policy_statement_request.DeleteResourcePolicyStatementRequest]",
        ) -> AsyncOperationResponse[
            "capo_lex_models_v2.types.delete_resource_policy_statement_response.DeleteResourcePolicyStatementResponse"
        ]:
            import capo_lex_models_v2._operations.lex_model_building_service_v2.delete_resource_policy_statement

            (
                output,
                http_response,
            ) = await capo_lex_models_v2._operations.lex_model_building_service_v2.delete_resource_policy_statement.async_delete_resource_policy_statement(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_lex_models_v2.types.delete_resource_policy_statement_request.DeleteResourcePolicyStatementRequest = {
            "resource_arn": resource_arn,
            "statement_id": statement_id,
        }
        if expected_revision_id is not None:
            input_["expected_revision_id"] = expected_revision_id

        response = await aexecute_pipeline(
            AsyncOperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        await response.response.aclose()
        return response.output

    async def delete_slot(
        self,
        slot_id: "capo_lex_models_v2.types.id.Id",
        bot_id: "capo_lex_models_v2.types.id.Id",
        bot_version: "capo_lex_models_v2.types.draft_bot_version.DraftBotVersion",
        locale_id: "capo_lex_models_v2.types.locale_id.LocaleId",
        intent_id: "capo_lex_models_v2.types.id.Id",
        *,
        config_overrides: Optional[AsyncLexModelsV2ClientConfig] = None,
    ) -> None:
        """<p>Deletes the specified slot from an intent.</p>

        Args:
            slot_id: <p>The identifier of the slot to delete. </p>
            bot_id: <p>The identifier of the bot associated with the slot to delete.</p>
            bot_version: <p>The version of the bot associated with the slot to delete.</p>
            locale_id: <p>The identifier of the language and locale that the slot will be deleted from. The string must match one of the supported locales. For more information, see <a href="https://docs.aws.amazon.com/lexv2/latest/dg/how-languages.html">Supported languages</a>.</p>
            intent_id: <p>The identifier of the intent associated with the slot.</p>

        Raises:
            capo_lex_models_v2.errors.conflict_exception.ConflictException: <p>The action that you tried to perform couldn't be completed because the resource is in a conflicting state. For example, deleting a bot that is in the CREATING state. Try your request again. </p>
            capo_lex_models_v2.errors.internal_server_exception.InternalServerException: <p>The service encountered an unexpected condition. Try your request again.</p>
            capo_lex_models_v2.errors.precondition_failed_exception.PreconditionFailedException: <p>Your request couldn't be completed because one or more request fields aren't valid. Check the fields in your request and try again.</p>
            capo_lex_models_v2.errors.service_quota_exceeded_exception.ServiceQuotaExceededException: <p>You have reached a quota for your bot. </p>
            capo_lex_models_v2.errors.throttling_exception.ThrottlingException: <p>Your request rate is too high. Reduce the frequency of requests.</p>
            capo_lex_models_v2.errors.validation_exception.ValidationException: <p>One of the input parameters in your request isn't valid. Check the parameters and try your request again.</p>
            capo_lex_models_v2.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        async def _handler(
            req: "AsyncOperationRequest[capo_lex_models_v2.types.delete_slot_request.DeleteSlotRequest]",
        ) -> AsyncOperationResponse[None]:
            import capo_lex_models_v2._operations.lex_model_building_service_v2.delete_slot

            (
                output,
                http_response,
            ) = await capo_lex_models_v2._operations.lex_model_building_service_v2.delete_slot.async_delete_slot(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_lex_models_v2.types.delete_slot_request.DeleteSlotRequest = {
            "slot_id": slot_id,
            "bot_id": bot_id,
            "bot_version": bot_version,
            "locale_id": locale_id,
            "intent_id": intent_id,
        }

        response = await aexecute_pipeline(
            AsyncOperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        await response.response.aclose()
        return response.output

    async def delete_slot_type(
        self,
        slot_type_id: "capo_lex_models_v2.types.id.Id",
        bot_id: "capo_lex_models_v2.types.id.Id",
        bot_version: "capo_lex_models_v2.types.draft_bot_version.DraftBotVersion",
        locale_id: "capo_lex_models_v2.types.locale_id.LocaleId",
        *,
        config_overrides: Optional[AsyncLexModelsV2ClientConfig] = None,
        skip_resource_in_use_check: Optional[
            "capo_lex_models_v2.types.skip_resource_in_use_check.SkipResourceInUseCheck"
        ] = None,
    ) -> None:
        """<p>Deletes a slot type from a bot locale.</p> <p>If a slot is using the slot type, Amazon Lex throws a <code>ResourceInUseException</code> exception. To avoid the exception, set the <code>skipResourceInUseCheck</code> parameter to <code>true</code>.</p>

        Args:
            slot_type_id: <p>The identifier of the slot type to delete.</p>
            bot_id: <p>The identifier of the bot associated with the slot type.</p>
            bot_version: <p>The version of the bot associated with the slot type.</p>
            locale_id: <p>The identifier of the language and locale that the slot type will be deleted from. The string must match one of the supported locales. For more information, see <a href="https://docs.aws.amazon.com/lexv2/latest/dg/how-languages.html">Supported languages</a>.</p>
            skip_resource_in_use_check: <p>By default, the <code>DeleteSlotType</code> operations throws a <code>ResourceInUseException</code> exception if you try to delete a slot type used by a slot. Set the <code>skipResourceInUseCheck</code> parameter to <code>true</code> to skip this check and remove the slot type even if a slot uses it.</p>

        Raises:
            capo_lex_models_v2.errors.conflict_exception.ConflictException: <p>The action that you tried to perform couldn't be completed because the resource is in a conflicting state. For example, deleting a bot that is in the CREATING state. Try your request again. </p>
            capo_lex_models_v2.errors.internal_server_exception.InternalServerException: <p>The service encountered an unexpected condition. Try your request again.</p>
            capo_lex_models_v2.errors.precondition_failed_exception.PreconditionFailedException: <p>Your request couldn't be completed because one or more request fields aren't valid. Check the fields in your request and try again.</p>
            capo_lex_models_v2.errors.service_quota_exceeded_exception.ServiceQuotaExceededException: <p>You have reached a quota for your bot. </p>
            capo_lex_models_v2.errors.throttling_exception.ThrottlingException: <p>Your request rate is too high. Reduce the frequency of requests.</p>
            capo_lex_models_v2.errors.validation_exception.ValidationException: <p>One of the input parameters in your request isn't valid. Check the parameters and try your request again.</p>
            capo_lex_models_v2.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        async def _handler(
            req: "AsyncOperationRequest[capo_lex_models_v2.types.delete_slot_type_request.DeleteSlotTypeRequest]",
        ) -> AsyncOperationResponse[None]:
            import capo_lex_models_v2._operations.lex_model_building_service_v2.delete_slot_type

            (
                output,
                http_response,
            ) = await capo_lex_models_v2._operations.lex_model_building_service_v2.delete_slot_type.async_delete_slot_type(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_lex_models_v2.types.delete_slot_type_request.DeleteSlotTypeRequest = {
            "slot_type_id": slot_type_id,
            "bot_id": bot_id,
            "bot_version": bot_version,
            "locale_id": locale_id,
        }
        if skip_resource_in_use_check is not None:
            input_["skip_resource_in_use_check"] = skip_resource_in_use_check

        response = await aexecute_pipeline(
            AsyncOperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        await response.response.aclose()
        return response.output

    async def delete_test_set(
        self,
        test_set_id: "capo_lex_models_v2.types.id.Id",
        *,
        config_overrides: Optional[AsyncLexModelsV2ClientConfig] = None,
    ) -> None:
        """<p>The action to delete the selected test set.</p>

        Args:
            test_set_id: <p>The test set Id of the test set to be deleted.</p>

        Raises:
            capo_lex_models_v2.errors.conflict_exception.ConflictException: <p>The action that you tried to perform couldn't be completed because the resource is in a conflicting state. For example, deleting a bot that is in the CREATING state. Try your request again. </p>
            capo_lex_models_v2.errors.internal_server_exception.InternalServerException: <p>The service encountered an unexpected condition. Try your request again.</p>
            capo_lex_models_v2.errors.precondition_failed_exception.PreconditionFailedException: <p>Your request couldn't be completed because one or more request fields aren't valid. Check the fields in your request and try again.</p>
            capo_lex_models_v2.errors.service_quota_exceeded_exception.ServiceQuotaExceededException: <p>You have reached a quota for your bot. </p>
            capo_lex_models_v2.errors.throttling_exception.ThrottlingException: <p>Your request rate is too high. Reduce the frequency of requests.</p>
            capo_lex_models_v2.errors.validation_exception.ValidationException: <p>One of the input parameters in your request isn't valid. Check the parameters and try your request again.</p>
            capo_lex_models_v2.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        async def _handler(
            req: "AsyncOperationRequest[capo_lex_models_v2.types.delete_test_set_request.DeleteTestSetRequest]",
        ) -> AsyncOperationResponse[None]:
            import capo_lex_models_v2._operations.lex_model_building_service_v2.delete_test_set

            (
                output,
                http_response,
            ) = await capo_lex_models_v2._operations.lex_model_building_service_v2.delete_test_set.async_delete_test_set(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_lex_models_v2.types.delete_test_set_request.DeleteTestSetRequest = {
            "test_set_id": test_set_id
        }

        response = await aexecute_pipeline(
            AsyncOperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        await response.response.aclose()
        return response.output

    async def delete_utterances(
        self,
        bot_id: "capo_lex_models_v2.types.id.Id",
        *,
        config_overrides: Optional[AsyncLexModelsV2ClientConfig] = None,
        locale_id: Optional["capo_lex_models_v2.types.locale_id.LocaleId"] = None,
        session_id: Optional["capo_lex_models_v2.types.session_id.SessionId"] = None,
    ) -> "capo_lex_models_v2.types.delete_utterances_response.DeleteUtterancesResponse":
        """<p>Deletes stored utterances.</p> <p>Amazon Lex stores the utterances that users send to your bot. Utterances are stored for 15 days for use with the <a href="https://docs.aws.amazon.com/lexv2/latest/APIReference/API_ListAggregatedUtterances.html">ListAggregatedUtterances</a> operation, and then stored indefinitely for use in improving the ability of your bot to respond to user input..</p> <p>Use the <code>DeleteUtterances</code> operation to manually delete utterances for a specific session. When you use the <code>DeleteUtterances</code> operation, utterances stored for improving your bot's ability to respond to user input are deleted immediately. Utterances stored for use with the <code>ListAggregatedUtterances</code> operation are deleted after 15 days.</p>

        Args:
            bot_id: <p>The unique identifier of the bot that contains the utterances.</p>
            locale_id: <p>The identifier of the language and locale where the utterances were collected. The string must match one of the supported locales. For more information, see <a href="https://docs.aws.amazon.com/lexv2/latest/dg/how-languages.html">Supported languages</a>.</p>
            session_id: <p>The unique identifier of the session with the user. The ID is returned in the response from the <a href="https://docs.aws.amazon.com/lexv2/latest/APIReference/API_runtime_RecognizeText.html">RecognizeText</a> and <a href="https://docs.aws.amazon.com/lexv2/latest/APIReference/API_runtime_RecognizeUtterance.html">RecognizeUtterance</a> operations.</p>

        Raises:
            capo_lex_models_v2.errors.internal_server_exception.InternalServerException: <p>The service encountered an unexpected condition. Try your request again.</p>
            capo_lex_models_v2.errors.throttling_exception.ThrottlingException: <p>Your request rate is too high. Reduce the frequency of requests.</p>
            capo_lex_models_v2.errors.validation_exception.ValidationException: <p>One of the input parameters in your request isn't valid. Check the parameters and try your request again.</p>
            capo_lex_models_v2.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        async def _handler(
            req: "AsyncOperationRequest[capo_lex_models_v2.types.delete_utterances_request.DeleteUtterancesRequest]",
        ) -> AsyncOperationResponse[
            "capo_lex_models_v2.types.delete_utterances_response.DeleteUtterancesResponse"
        ]:
            import capo_lex_models_v2._operations.lex_model_building_service_v2.delete_utterances

            (
                output,
                http_response,
            ) = await capo_lex_models_v2._operations.lex_model_building_service_v2.delete_utterances.async_delete_utterances(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_lex_models_v2.types.delete_utterances_request.DeleteUtterancesRequest = {
            "bot_id": bot_id
        }
        if locale_id is not None:
            input_["locale_id"] = locale_id
        if session_id is not None:
            input_["session_id"] = session_id

        response = await aexecute_pipeline(
            AsyncOperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        await response.response.aclose()
        return response.output

    async def describe_bot(
        self,
        bot_id: "capo_lex_models_v2.types.id.Id",
        *,
        config_overrides: Optional[AsyncLexModelsV2ClientConfig] = None,
    ) -> "capo_lex_models_v2.types.describe_bot_response.DescribeBotResponse":
        """<p>Provides metadata information about a bot. </p>

        Args:
            bot_id: <p>The unique identifier of the bot to describe.</p>

        Raises:
            capo_lex_models_v2.errors.internal_server_exception.InternalServerException: <p>The service encountered an unexpected condition. Try your request again.</p>
            capo_lex_models_v2.errors.resource_not_found_exception.ResourceNotFoundException: <p>You asked to describe a resource that doesn't exist. Check the resource that you are requesting and try again.</p>
            capo_lex_models_v2.errors.service_quota_exceeded_exception.ServiceQuotaExceededException: <p>You have reached a quota for your bot. </p>
            capo_lex_models_v2.errors.throttling_exception.ThrottlingException: <p>Your request rate is too high. Reduce the frequency of requests.</p>
            capo_lex_models_v2.errors.validation_exception.ValidationException: <p>One of the input parameters in your request isn't valid. Check the parameters and try your request again.</p>
            capo_lex_models_v2.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        async def _handler(
            req: "AsyncOperationRequest[capo_lex_models_v2.types.describe_bot_request.DescribeBotRequest]",
        ) -> AsyncOperationResponse[
            "capo_lex_models_v2.types.describe_bot_response.DescribeBotResponse"
        ]:
            import capo_lex_models_v2._operations.lex_model_building_service_v2.describe_bot

            (
                output,
                http_response,
            ) = await capo_lex_models_v2._operations.lex_model_building_service_v2.describe_bot.async_describe_bot(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_lex_models_v2.types.describe_bot_request.DescribeBotRequest = {
            "bot_id": bot_id
        }

        response = await aexecute_pipeline(
            AsyncOperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        await response.response.aclose()
        return response.output

    async def describe_bot_alias(
        self,
        bot_alias_id: "capo_lex_models_v2.types.bot_alias_id.BotAliasId",
        bot_id: "capo_lex_models_v2.types.id.Id",
        *,
        config_overrides: Optional[AsyncLexModelsV2ClientConfig] = None,
    ) -> (
        "capo_lex_models_v2.types.describe_bot_alias_response.DescribeBotAliasResponse"
    ):
        """<p>Get information about a specific bot alias.</p>

        Args:
            bot_alias_id: <p>The identifier of the bot alias to describe.</p>
            bot_id: <p>The identifier of the bot associated with the bot alias to describe.</p>

        Raises:
            capo_lex_models_v2.errors.internal_server_exception.InternalServerException: <p>The service encountered an unexpected condition. Try your request again.</p>
            capo_lex_models_v2.errors.resource_not_found_exception.ResourceNotFoundException: <p>You asked to describe a resource that doesn't exist. Check the resource that you are requesting and try again.</p>
            capo_lex_models_v2.errors.service_quota_exceeded_exception.ServiceQuotaExceededException: <p>You have reached a quota for your bot. </p>
            capo_lex_models_v2.errors.throttling_exception.ThrottlingException: <p>Your request rate is too high. Reduce the frequency of requests.</p>
            capo_lex_models_v2.errors.validation_exception.ValidationException: <p>One of the input parameters in your request isn't valid. Check the parameters and try your request again.</p>
            capo_lex_models_v2.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        async def _handler(
            req: "AsyncOperationRequest[capo_lex_models_v2.types.describe_bot_alias_request.DescribeBotAliasRequest]",
        ) -> AsyncOperationResponse[
            "capo_lex_models_v2.types.describe_bot_alias_response.DescribeBotAliasResponse"
        ]:
            import capo_lex_models_v2._operations.lex_model_building_service_v2.describe_bot_alias

            (
                output,
                http_response,
            ) = await capo_lex_models_v2._operations.lex_model_building_service_v2.describe_bot_alias.async_describe_bot_alias(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_lex_models_v2.types.describe_bot_alias_request.DescribeBotAliasRequest = {
            "bot_alias_id": bot_alias_id,
            "bot_id": bot_id,
        }

        response = await aexecute_pipeline(
            AsyncOperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        await response.response.aclose()
        return response.output

    async def describe_bot_analyzer_recommendation(
        self,
        bot_id: "capo_lex_models_v2.types.id.Id",
        bot_analyzer_request_id: "capo_lex_models_v2.types.uuid.UUID",
        *,
        config_overrides: Optional[AsyncLexModelsV2ClientConfig] = None,
        next_token: Optional["capo_lex_models_v2.types.next_token.NextToken"] = None,
        max_results: Optional["capo_lex_models_v2.types.max_results.MaxResults"] = None,
    ) -> "capo_lex_models_v2.types.describe_bot_analyzer_recommendation_response.DescribeBotAnalyzerRecommendationResponse":
        """<p>Retrieves the analysis results and recommendations for bot optimization. The analysis must be in <code>Available</code> status before recommendations can be retrieved.</p> <p>Recommendations are returned with pagination support. Each recommendation includes the issue location, priority level, detailed description, and proposed fix.</p>

        Args:
            bot_id: <p>The unique identifier of the bot.</p>
            bot_analyzer_request_id: <p>The unique identifier of the analysis request.</p>
            next_token: <p>If the response from a previous request was truncated, the <code>nextToken</code> value is used to retrieve the next page of recommendations.</p>
            max_results: <p>The maximum number of recommendations to return in the response. The default is 5.</p>

        Raises:
            capo_lex_models_v2.errors.internal_server_exception.InternalServerException: <p>The service encountered an unexpected condition. Try your request again.</p>
            capo_lex_models_v2.errors.resource_not_found_exception.ResourceNotFoundException: <p>You asked to describe a resource that doesn't exist. Check the resource that you are requesting and try again.</p>
            capo_lex_models_v2.errors.throttling_exception.ThrottlingException: <p>Your request rate is too high. Reduce the frequency of requests.</p>
            capo_lex_models_v2.errors.validation_exception.ValidationException: <p>One of the input parameters in your request isn't valid. Check the parameters and try your request again.</p>
            capo_lex_models_v2.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        async def _handler(
            req: "AsyncOperationRequest[capo_lex_models_v2.types.describe_bot_analyzer_recommendation_request.DescribeBotAnalyzerRecommendationRequest]",
        ) -> AsyncOperationResponse[
            "capo_lex_models_v2.types.describe_bot_analyzer_recommendation_response.DescribeBotAnalyzerRecommendationResponse"
        ]:
            import capo_lex_models_v2._operations.lex_model_building_service_v2.describe_bot_analyzer_recommendation

            (
                output,
                http_response,
            ) = await capo_lex_models_v2._operations.lex_model_building_service_v2.describe_bot_analyzer_recommendation.async_describe_bot_analyzer_recommendation(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_lex_models_v2.types.describe_bot_analyzer_recommendation_request.DescribeBotAnalyzerRecommendationRequest = {
            "bot_id": bot_id,
            "bot_analyzer_request_id": bot_analyzer_request_id,
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

    async def iter_describe_bot_analyzer_recommendation(
        self,
        bot_id: "capo_lex_models_v2.types.id.Id",
        bot_analyzer_request_id: "capo_lex_models_v2.types.uuid.UUID",
        *,
        config_overrides: Optional[AsyncLexModelsV2ClientConfig] = None,
        next_token: Optional["capo_lex_models_v2.types.next_token.NextToken"] = None,
        max_results: Optional["capo_lex_models_v2.types.max_results.MaxResults"] = None,
    ) -> "AsyncIterator[capo_lex_models_v2.types.bot_analyzer_recommendation.BotAnalyzerRecommendation]":
        _token = next_token
        while True:
            _response = await self.describe_bot_analyzer_recommendation(
                bot_id,
                bot_analyzer_request_id,
                config_overrides=config_overrides,
                next_token=_token,
                max_results=max_results,
            )
            _page = _resolve_path(_response, ("bot_analyzer_recommendation_list",))
            for _item in _page or []:
                yield _item
            _token = _resolve_path(_response, ("next_token",))
            if not _token:
                break

    async def describe_bot_locale(
        self,
        bot_id: "capo_lex_models_v2.types.id.Id",
        bot_version: "capo_lex_models_v2.types.bot_version.BotVersion",
        locale_id: "capo_lex_models_v2.types.locale_id.LocaleId",
        *,
        config_overrides: Optional[AsyncLexModelsV2ClientConfig] = None,
    ) -> "capo_lex_models_v2.types.describe_bot_locale_response.DescribeBotLocaleResponse":
        """<p>Describes the settings that a bot has for a specific locale. </p>

        Args:
            bot_id: <p>The identifier of the bot associated with the locale.</p>
            bot_version: <p>The version of the bot associated with the locale.</p>
            locale_id: <p>The unique identifier of the locale to describe. The string must match one of the supported locales. For more information, see <a href="https://docs.aws.amazon.com/lexv2/latest/dg/how-languages.html">Supported languages</a>. </p>

        Raises:
            capo_lex_models_v2.errors.internal_server_exception.InternalServerException: <p>The service encountered an unexpected condition. Try your request again.</p>
            capo_lex_models_v2.errors.resource_not_found_exception.ResourceNotFoundException: <p>You asked to describe a resource that doesn't exist. Check the resource that you are requesting and try again.</p>
            capo_lex_models_v2.errors.service_quota_exceeded_exception.ServiceQuotaExceededException: <p>You have reached a quota for your bot. </p>
            capo_lex_models_v2.errors.throttling_exception.ThrottlingException: <p>Your request rate is too high. Reduce the frequency of requests.</p>
            capo_lex_models_v2.errors.validation_exception.ValidationException: <p>One of the input parameters in your request isn't valid. Check the parameters and try your request again.</p>
            capo_lex_models_v2.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        async def _handler(
            req: "AsyncOperationRequest[capo_lex_models_v2.types.describe_bot_locale_request.DescribeBotLocaleRequest]",
        ) -> AsyncOperationResponse[
            "capo_lex_models_v2.types.describe_bot_locale_response.DescribeBotLocaleResponse"
        ]:
            import capo_lex_models_v2._operations.lex_model_building_service_v2.describe_bot_locale

            (
                output,
                http_response,
            ) = await capo_lex_models_v2._operations.lex_model_building_service_v2.describe_bot_locale.async_describe_bot_locale(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_lex_models_v2.types.describe_bot_locale_request.DescribeBotLocaleRequest = {
            "bot_id": bot_id,
            "bot_version": bot_version,
            "locale_id": locale_id,
        }

        response = await aexecute_pipeline(
            AsyncOperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        await response.response.aclose()
        return response.output

    async def describe_bot_recommendation(
        self,
        bot_id: "capo_lex_models_v2.types.id.Id",
        bot_version: "capo_lex_models_v2.types.draft_bot_version.DraftBotVersion",
        locale_id: "capo_lex_models_v2.types.locale_id.LocaleId",
        bot_recommendation_id: "capo_lex_models_v2.types.id.Id",
        *,
        config_overrides: Optional[AsyncLexModelsV2ClientConfig] = None,
    ) -> "capo_lex_models_v2.types.describe_bot_recommendation_response.DescribeBotRecommendationResponse":
        """<p>Provides metadata information about a bot recommendation. This information will enable you to get a description on the request inputs, to download associated transcripts after processing is complete, and to download intents and slot-types generated by the bot recommendation.</p>

        Args:
            bot_id: <p>The unique identifier of the bot associated with the bot recommendation.</p>
            bot_version: <p>The version of the bot associated with the bot recommendation.</p>
            locale_id: <p>The identifier of the language and locale of the bot recommendation to describe. The string must match one of the supported locales. For more information, see <a href="https://docs.aws.amazon.com/lexv2/latest/dg/how-languages.html">Supported languages</a>.</p>
            bot_recommendation_id: <p>The identifier of the bot recommendation to describe.</p>

        Raises:
            capo_lex_models_v2.errors.internal_server_exception.InternalServerException: <p>The service encountered an unexpected condition. Try your request again.</p>
            capo_lex_models_v2.errors.resource_not_found_exception.ResourceNotFoundException: <p>You asked to describe a resource that doesn't exist. Check the resource that you are requesting and try again.</p>
            capo_lex_models_v2.errors.throttling_exception.ThrottlingException: <p>Your request rate is too high. Reduce the frequency of requests.</p>
            capo_lex_models_v2.errors.validation_exception.ValidationException: <p>One of the input parameters in your request isn't valid. Check the parameters and try your request again.</p>
            capo_lex_models_v2.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        async def _handler(
            req: "AsyncOperationRequest[capo_lex_models_v2.types.describe_bot_recommendation_request.DescribeBotRecommendationRequest]",
        ) -> AsyncOperationResponse[
            "capo_lex_models_v2.types.describe_bot_recommendation_response.DescribeBotRecommendationResponse"
        ]:
            import capo_lex_models_v2._operations.lex_model_building_service_v2.describe_bot_recommendation

            (
                output,
                http_response,
            ) = await capo_lex_models_v2._operations.lex_model_building_service_v2.describe_bot_recommendation.async_describe_bot_recommendation(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_lex_models_v2.types.describe_bot_recommendation_request.DescribeBotRecommendationRequest = {
            "bot_id": bot_id,
            "bot_version": bot_version,
            "locale_id": locale_id,
            "bot_recommendation_id": bot_recommendation_id,
        }

        response = await aexecute_pipeline(
            AsyncOperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        await response.response.aclose()
        return response.output

    async def describe_bot_replica(
        self,
        bot_id: "capo_lex_models_v2.types.id.Id",
        replica_region: "capo_lex_models_v2.types.replica_region.ReplicaRegion",
        *,
        config_overrides: Optional[AsyncLexModelsV2ClientConfig] = None,
    ) -> "capo_lex_models_v2.types.describe_bot_replica_response.DescribeBotReplicaResponse":
        """<p>Monitors the bot replication status through the UI console.</p>

        Args:
            bot_id: <p>The request for the unique bot ID of the replicated bot being monitored.</p>
            replica_region: <p>The request for the region of the replicated bot being monitored.</p>

        Raises:
            capo_lex_models_v2.errors.internal_server_exception.InternalServerException: <p>The service encountered an unexpected condition. Try your request again.</p>
            capo_lex_models_v2.errors.resource_not_found_exception.ResourceNotFoundException: <p>You asked to describe a resource that doesn't exist. Check the resource that you are requesting and try again.</p>
            capo_lex_models_v2.errors.service_quota_exceeded_exception.ServiceQuotaExceededException: <p>You have reached a quota for your bot. </p>
            capo_lex_models_v2.errors.throttling_exception.ThrottlingException: <p>Your request rate is too high. Reduce the frequency of requests.</p>
            capo_lex_models_v2.errors.validation_exception.ValidationException: <p>One of the input parameters in your request isn't valid. Check the parameters and try your request again.</p>
            capo_lex_models_v2.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        async def _handler(
            req: "AsyncOperationRequest[capo_lex_models_v2.types.describe_bot_replica_request.DescribeBotReplicaRequest]",
        ) -> AsyncOperationResponse[
            "capo_lex_models_v2.types.describe_bot_replica_response.DescribeBotReplicaResponse"
        ]:
            import capo_lex_models_v2._operations.lex_model_building_service_v2.describe_bot_replica

            (
                output,
                http_response,
            ) = await capo_lex_models_v2._operations.lex_model_building_service_v2.describe_bot_replica.async_describe_bot_replica(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_lex_models_v2.types.describe_bot_replica_request.DescribeBotReplicaRequest = {
            "bot_id": bot_id,
            "replica_region": replica_region,
        }

        response = await aexecute_pipeline(
            AsyncOperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        await response.response.aclose()
        return response.output

    async def describe_bot_resource_generation(
        self,
        bot_id: "capo_lex_models_v2.types.id.Id",
        bot_version: "capo_lex_models_v2.types.bot_version.BotVersion",
        locale_id: "capo_lex_models_v2.types.locale_id.LocaleId",
        generation_id: "capo_lex_models_v2.types.id.Id",
        *,
        config_overrides: Optional[AsyncLexModelsV2ClientConfig] = None,
    ) -> "capo_lex_models_v2.types.describe_bot_resource_generation_response.DescribeBotResourceGenerationResponse":
        """<p>Returns information about a request to generate a bot through natural language description, made through the <code>StartBotResource</code> API. Use the <code>generatedBotLocaleUrl</code> to retrieve the Amazon S3 object containing the bot locale configuration. You can then modify and import this configuration.</p>

        Args:
            bot_id: <p>The unique identifier of the bot for which to return the generation details.</p>
            bot_version: <p>The version of the bot for which to return the generation details.</p>
            locale_id: <p>The locale of the bot for which to return the generation details.</p>
            generation_id: <p>The unique identifier of the generation request for which to return the generation details.</p>

        Raises:
            capo_lex_models_v2.errors.internal_server_exception.InternalServerException: <p>The service encountered an unexpected condition. Try your request again.</p>
            capo_lex_models_v2.errors.resource_not_found_exception.ResourceNotFoundException: <p>You asked to describe a resource that doesn't exist. Check the resource that you are requesting and try again.</p>
            capo_lex_models_v2.errors.throttling_exception.ThrottlingException: <p>Your request rate is too high. Reduce the frequency of requests.</p>
            capo_lex_models_v2.errors.validation_exception.ValidationException: <p>One of the input parameters in your request isn't valid. Check the parameters and try your request again.</p>
            capo_lex_models_v2.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        async def _handler(
            req: "AsyncOperationRequest[capo_lex_models_v2.types.describe_bot_resource_generation_request.DescribeBotResourceGenerationRequest]",
        ) -> AsyncOperationResponse[
            "capo_lex_models_v2.types.describe_bot_resource_generation_response.DescribeBotResourceGenerationResponse"
        ]:
            import capo_lex_models_v2._operations.lex_model_building_service_v2.describe_bot_resource_generation

            (
                output,
                http_response,
            ) = await capo_lex_models_v2._operations.lex_model_building_service_v2.describe_bot_resource_generation.async_describe_bot_resource_generation(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_lex_models_v2.types.describe_bot_resource_generation_request.DescribeBotResourceGenerationRequest = {
            "bot_id": bot_id,
            "bot_version": bot_version,
            "locale_id": locale_id,
            "generation_id": generation_id,
        }

        response = await aexecute_pipeline(
            AsyncOperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        await response.response.aclose()
        return response.output

    async def describe_bot_version(
        self,
        bot_id: "capo_lex_models_v2.types.id.Id",
        bot_version: "capo_lex_models_v2.types.numerical_bot_version.NumericalBotVersion",
        *,
        config_overrides: Optional[AsyncLexModelsV2ClientConfig] = None,
    ) -> "capo_lex_models_v2.types.describe_bot_version_response.DescribeBotVersionResponse":
        """<p>Provides metadata about a version of a bot.</p>

        Args:
            bot_id: <p>The identifier of the bot containing the version to return metadata for.</p>
            bot_version: <p>The version of the bot to return metadata for.</p>

        Raises:
            capo_lex_models_v2.errors.internal_server_exception.InternalServerException: <p>The service encountered an unexpected condition. Try your request again.</p>
            capo_lex_models_v2.errors.resource_not_found_exception.ResourceNotFoundException: <p>You asked to describe a resource that doesn't exist. Check the resource that you are requesting and try again.</p>
            capo_lex_models_v2.errors.service_quota_exceeded_exception.ServiceQuotaExceededException: <p>You have reached a quota for your bot. </p>
            capo_lex_models_v2.errors.throttling_exception.ThrottlingException: <p>Your request rate is too high. Reduce the frequency of requests.</p>
            capo_lex_models_v2.errors.validation_exception.ValidationException: <p>One of the input parameters in your request isn't valid. Check the parameters and try your request again.</p>
            capo_lex_models_v2.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        async def _handler(
            req: "AsyncOperationRequest[capo_lex_models_v2.types.describe_bot_version_request.DescribeBotVersionRequest]",
        ) -> AsyncOperationResponse[
            "capo_lex_models_v2.types.describe_bot_version_response.DescribeBotVersionResponse"
        ]:
            import capo_lex_models_v2._operations.lex_model_building_service_v2.describe_bot_version

            (
                output,
                http_response,
            ) = await capo_lex_models_v2._operations.lex_model_building_service_v2.describe_bot_version.async_describe_bot_version(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_lex_models_v2.types.describe_bot_version_request.DescribeBotVersionRequest = {
            "bot_id": bot_id,
            "bot_version": bot_version,
        }

        response = await aexecute_pipeline(
            AsyncOperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        await response.response.aclose()
        return response.output

    async def describe_custom_vocabulary_metadata(
        self,
        bot_id: "capo_lex_models_v2.types.id.Id",
        bot_version: "capo_lex_models_v2.types.bot_version.BotVersion",
        locale_id: "capo_lex_models_v2.types.locale_id.LocaleId",
        *,
        config_overrides: Optional[AsyncLexModelsV2ClientConfig] = None,
    ) -> "capo_lex_models_v2.types.describe_custom_vocabulary_metadata_response.DescribeCustomVocabularyMetadataResponse":
        """<p>Provides metadata information about a custom vocabulary.</p>

        Args:
            bot_id: <p>The unique identifier of the bot that contains the custom vocabulary.</p>
            bot_version: <p>The bot version of the bot to return metadata for.</p>
            locale_id: <p>The locale to return the custom vocabulary information for. The locale must be <code>en_GB</code>.</p>

        Raises:
            capo_lex_models_v2.errors.internal_server_exception.InternalServerException: <p>The service encountered an unexpected condition. Try your request again.</p>
            capo_lex_models_v2.errors.resource_not_found_exception.ResourceNotFoundException: <p>You asked to describe a resource that doesn't exist. Check the resource that you are requesting and try again.</p>
            capo_lex_models_v2.errors.service_quota_exceeded_exception.ServiceQuotaExceededException: <p>You have reached a quota for your bot. </p>
            capo_lex_models_v2.errors.throttling_exception.ThrottlingException: <p>Your request rate is too high. Reduce the frequency of requests.</p>
            capo_lex_models_v2.errors.validation_exception.ValidationException: <p>One of the input parameters in your request isn't valid. Check the parameters and try your request again.</p>
            capo_lex_models_v2.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        async def _handler(
            req: "AsyncOperationRequest[capo_lex_models_v2.types.describe_custom_vocabulary_metadata_request.DescribeCustomVocabularyMetadataRequest]",
        ) -> AsyncOperationResponse[
            "capo_lex_models_v2.types.describe_custom_vocabulary_metadata_response.DescribeCustomVocabularyMetadataResponse"
        ]:
            import capo_lex_models_v2._operations.lex_model_building_service_v2.describe_custom_vocabulary_metadata

            (
                output,
                http_response,
            ) = await capo_lex_models_v2._operations.lex_model_building_service_v2.describe_custom_vocabulary_metadata.async_describe_custom_vocabulary_metadata(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_lex_models_v2.types.describe_custom_vocabulary_metadata_request.DescribeCustomVocabularyMetadataRequest = {
            "bot_id": bot_id,
            "bot_version": bot_version,
            "locale_id": locale_id,
        }

        response = await aexecute_pipeline(
            AsyncOperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        await response.response.aclose()
        return response.output

    async def describe_export(
        self,
        export_id: "capo_lex_models_v2.types.id.Id",
        *,
        config_overrides: Optional[AsyncLexModelsV2ClientConfig] = None,
    ) -> "capo_lex_models_v2.types.describe_export_response.DescribeExportResponse":
        """<p>Gets information about a specific export.</p>

        Args:
            export_id: <p>The unique identifier of the export to describe.</p>

        Raises:
            capo_lex_models_v2.errors.internal_server_exception.InternalServerException: <p>The service encountered an unexpected condition. Try your request again.</p>
            capo_lex_models_v2.errors.resource_not_found_exception.ResourceNotFoundException: <p>You asked to describe a resource that doesn't exist. Check the resource that you are requesting and try again.</p>
            capo_lex_models_v2.errors.throttling_exception.ThrottlingException: <p>Your request rate is too high. Reduce the frequency of requests.</p>
            capo_lex_models_v2.errors.validation_exception.ValidationException: <p>One of the input parameters in your request isn't valid. Check the parameters and try your request again.</p>
            capo_lex_models_v2.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        async def _handler(
            req: "AsyncOperationRequest[capo_lex_models_v2.types.describe_export_request.DescribeExportRequest]",
        ) -> AsyncOperationResponse[
            "capo_lex_models_v2.types.describe_export_response.DescribeExportResponse"
        ]:
            import capo_lex_models_v2._operations.lex_model_building_service_v2.describe_export

            (
                output,
                http_response,
            ) = await capo_lex_models_v2._operations.lex_model_building_service_v2.describe_export.async_describe_export(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_lex_models_v2.types.describe_export_request.DescribeExportRequest = {
            "export_id": export_id
        }

        response = await aexecute_pipeline(
            AsyncOperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        await response.response.aclose()
        return response.output

    async def describe_import(
        self,
        import_id: "capo_lex_models_v2.types.id.Id",
        *,
        config_overrides: Optional[AsyncLexModelsV2ClientConfig] = None,
    ) -> "capo_lex_models_v2.types.describe_import_response.DescribeImportResponse":
        """<p>Gets information about a specific import.</p>

        Args:
            import_id: <p>The unique identifier of the import to describe.</p>

        Raises:
            capo_lex_models_v2.errors.internal_server_exception.InternalServerException: <p>The service encountered an unexpected condition. Try your request again.</p>
            capo_lex_models_v2.errors.resource_not_found_exception.ResourceNotFoundException: <p>You asked to describe a resource that doesn't exist. Check the resource that you are requesting and try again.</p>
            capo_lex_models_v2.errors.throttling_exception.ThrottlingException: <p>Your request rate is too high. Reduce the frequency of requests.</p>
            capo_lex_models_v2.errors.validation_exception.ValidationException: <p>One of the input parameters in your request isn't valid. Check the parameters and try your request again.</p>
            capo_lex_models_v2.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        async def _handler(
            req: "AsyncOperationRequest[capo_lex_models_v2.types.describe_import_request.DescribeImportRequest]",
        ) -> AsyncOperationResponse[
            "capo_lex_models_v2.types.describe_import_response.DescribeImportResponse"
        ]:
            import capo_lex_models_v2._operations.lex_model_building_service_v2.describe_import

            (
                output,
                http_response,
            ) = await capo_lex_models_v2._operations.lex_model_building_service_v2.describe_import.async_describe_import(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_lex_models_v2.types.describe_import_request.DescribeImportRequest = {
            "import_id": import_id
        }

        response = await aexecute_pipeline(
            AsyncOperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        await response.response.aclose()
        return response.output

    async def describe_intent(
        self,
        intent_id: "capo_lex_models_v2.types.id.Id",
        bot_id: "capo_lex_models_v2.types.id.Id",
        bot_version: "capo_lex_models_v2.types.bot_version.BotVersion",
        locale_id: "capo_lex_models_v2.types.locale_id.LocaleId",
        *,
        config_overrides: Optional[AsyncLexModelsV2ClientConfig] = None,
    ) -> "capo_lex_models_v2.types.describe_intent_response.DescribeIntentResponse":
        """<p>Returns metadata about an intent.</p>

        Args:
            intent_id: <p>The identifier of the intent to describe.</p>
            bot_id: <p>The identifier of the bot associated with the intent.</p>
            bot_version: <p>The version of the bot associated with the intent.</p>
            locale_id: <p>The identifier of the language and locale of the intent to describe. The string must match one of the supported locales. For more information, see <a href="https://docs.aws.amazon.com/lexv2/latest/dg/how-languages.html">Supported languages</a>.</p>

        Raises:
            capo_lex_models_v2.errors.internal_server_exception.InternalServerException: <p>The service encountered an unexpected condition. Try your request again.</p>
            capo_lex_models_v2.errors.resource_not_found_exception.ResourceNotFoundException: <p>You asked to describe a resource that doesn't exist. Check the resource that you are requesting and try again.</p>
            capo_lex_models_v2.errors.service_quota_exceeded_exception.ServiceQuotaExceededException: <p>You have reached a quota for your bot. </p>
            capo_lex_models_v2.errors.throttling_exception.ThrottlingException: <p>Your request rate is too high. Reduce the frequency of requests.</p>
            capo_lex_models_v2.errors.validation_exception.ValidationException: <p>One of the input parameters in your request isn't valid. Check the parameters and try your request again.</p>
            capo_lex_models_v2.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        async def _handler(
            req: "AsyncOperationRequest[capo_lex_models_v2.types.describe_intent_request.DescribeIntentRequest]",
        ) -> AsyncOperationResponse[
            "capo_lex_models_v2.types.describe_intent_response.DescribeIntentResponse"
        ]:
            import capo_lex_models_v2._operations.lex_model_building_service_v2.describe_intent

            (
                output,
                http_response,
            ) = await capo_lex_models_v2._operations.lex_model_building_service_v2.describe_intent.async_describe_intent(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_lex_models_v2.types.describe_intent_request.DescribeIntentRequest = {
            "intent_id": intent_id,
            "bot_id": bot_id,
            "bot_version": bot_version,
            "locale_id": locale_id,
        }

        response = await aexecute_pipeline(
            AsyncOperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        await response.response.aclose()
        return response.output

    async def describe_resource_policy(
        self,
        resource_arn: "capo_lex_models_v2.types.amazon_resource_name.AmazonResourceName",
        *,
        config_overrides: Optional[AsyncLexModelsV2ClientConfig] = None,
    ) -> "capo_lex_models_v2.types.describe_resource_policy_response.DescribeResourcePolicyResponse":
        """<p>Gets the resource policy and policy revision for a bot or bot alias.</p>

        Args:
            resource_arn: <p>The Amazon Resource Name (ARN) of the bot or bot alias that the resource policy is attached to.</p>

        Raises:
            capo_lex_models_v2.errors.internal_server_exception.InternalServerException: <p>The service encountered an unexpected condition. Try your request again.</p>
            capo_lex_models_v2.errors.resource_not_found_exception.ResourceNotFoundException: <p>You asked to describe a resource that doesn't exist. Check the resource that you are requesting and try again.</p>
            capo_lex_models_v2.errors.throttling_exception.ThrottlingException: <p>Your request rate is too high. Reduce the frequency of requests.</p>
            capo_lex_models_v2.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        async def _handler(
            req: "AsyncOperationRequest[capo_lex_models_v2.types.describe_resource_policy_request.DescribeResourcePolicyRequest]",
        ) -> AsyncOperationResponse[
            "capo_lex_models_v2.types.describe_resource_policy_response.DescribeResourcePolicyResponse"
        ]:
            import capo_lex_models_v2._operations.lex_model_building_service_v2.describe_resource_policy

            (
                output,
                http_response,
            ) = await capo_lex_models_v2._operations.lex_model_building_service_v2.describe_resource_policy.async_describe_resource_policy(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_lex_models_v2.types.describe_resource_policy_request.DescribeResourcePolicyRequest = {
            "resource_arn": resource_arn
        }

        response = await aexecute_pipeline(
            AsyncOperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        await response.response.aclose()
        return response.output

    async def describe_slot(
        self,
        slot_id: "capo_lex_models_v2.types.id.Id",
        bot_id: "capo_lex_models_v2.types.id.Id",
        bot_version: "capo_lex_models_v2.types.bot_version.BotVersion",
        locale_id: "capo_lex_models_v2.types.locale_id.LocaleId",
        intent_id: "capo_lex_models_v2.types.id.Id",
        *,
        config_overrides: Optional[AsyncLexModelsV2ClientConfig] = None,
    ) -> "capo_lex_models_v2.types.describe_slot_response.DescribeSlotResponse":
        """<p>Gets metadata information about a slot.</p>

        Args:
            slot_id: <p>The unique identifier for the slot.</p>
            bot_id: <p>The identifier of the bot associated with the slot.</p>
            bot_version: <p>The version of the bot associated with the slot.</p>
            locale_id: <p>The identifier of the language and locale of the slot to describe. The string must match one of the supported locales. For more information, see <a href="https://docs.aws.amazon.com/lexv2/latest/dg/how-languages.html">Supported languages</a>.</p>
            intent_id: <p>The identifier of the intent that contains the slot.</p>

        Raises:
            capo_lex_models_v2.errors.internal_server_exception.InternalServerException: <p>The service encountered an unexpected condition. Try your request again.</p>
            capo_lex_models_v2.errors.resource_not_found_exception.ResourceNotFoundException: <p>You asked to describe a resource that doesn't exist. Check the resource that you are requesting and try again.</p>
            capo_lex_models_v2.errors.service_quota_exceeded_exception.ServiceQuotaExceededException: <p>You have reached a quota for your bot. </p>
            capo_lex_models_v2.errors.throttling_exception.ThrottlingException: <p>Your request rate is too high. Reduce the frequency of requests.</p>
            capo_lex_models_v2.errors.validation_exception.ValidationException: <p>One of the input parameters in your request isn't valid. Check the parameters and try your request again.</p>
            capo_lex_models_v2.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        async def _handler(
            req: "AsyncOperationRequest[capo_lex_models_v2.types.describe_slot_request.DescribeSlotRequest]",
        ) -> AsyncOperationResponse[
            "capo_lex_models_v2.types.describe_slot_response.DescribeSlotResponse"
        ]:
            import capo_lex_models_v2._operations.lex_model_building_service_v2.describe_slot

            (
                output,
                http_response,
            ) = await capo_lex_models_v2._operations.lex_model_building_service_v2.describe_slot.async_describe_slot(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_lex_models_v2.types.describe_slot_request.DescribeSlotRequest = {
            "slot_id": slot_id,
            "bot_id": bot_id,
            "bot_version": bot_version,
            "locale_id": locale_id,
            "intent_id": intent_id,
        }

        response = await aexecute_pipeline(
            AsyncOperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        await response.response.aclose()
        return response.output

    async def describe_slot_type(
        self,
        slot_type_id: "capo_lex_models_v2.types.id.Id",
        bot_id: "capo_lex_models_v2.types.id.Id",
        bot_version: "capo_lex_models_v2.types.bot_version.BotVersion",
        locale_id: "capo_lex_models_v2.types.locale_id.LocaleId",
        *,
        config_overrides: Optional[AsyncLexModelsV2ClientConfig] = None,
    ) -> (
        "capo_lex_models_v2.types.describe_slot_type_response.DescribeSlotTypeResponse"
    ):
        """<p>Gets metadata information about a slot type.</p>

        Args:
            slot_type_id: <p>The identifier of the slot type.</p>
            bot_id: <p>The identifier of the bot associated with the slot type.</p>
            bot_version: <p>The version of the bot associated with the slot type.</p>
            locale_id: <p>The identifier of the language and locale of the slot type to describe. The string must match one of the supported locales. For more information, see <a href="https://docs.aws.amazon.com/lexv2/latest/dg/how-languages.html">Supported languages</a>.</p>

        Raises:
            capo_lex_models_v2.errors.internal_server_exception.InternalServerException: <p>The service encountered an unexpected condition. Try your request again.</p>
            capo_lex_models_v2.errors.resource_not_found_exception.ResourceNotFoundException: <p>You asked to describe a resource that doesn't exist. Check the resource that you are requesting and try again.</p>
            capo_lex_models_v2.errors.service_quota_exceeded_exception.ServiceQuotaExceededException: <p>You have reached a quota for your bot. </p>
            capo_lex_models_v2.errors.throttling_exception.ThrottlingException: <p>Your request rate is too high. Reduce the frequency of requests.</p>
            capo_lex_models_v2.errors.validation_exception.ValidationException: <p>One of the input parameters in your request isn't valid. Check the parameters and try your request again.</p>
            capo_lex_models_v2.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        async def _handler(
            req: "AsyncOperationRequest[capo_lex_models_v2.types.describe_slot_type_request.DescribeSlotTypeRequest]",
        ) -> AsyncOperationResponse[
            "capo_lex_models_v2.types.describe_slot_type_response.DescribeSlotTypeResponse"
        ]:
            import capo_lex_models_v2._operations.lex_model_building_service_v2.describe_slot_type

            (
                output,
                http_response,
            ) = await capo_lex_models_v2._operations.lex_model_building_service_v2.describe_slot_type.async_describe_slot_type(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_lex_models_v2.types.describe_slot_type_request.DescribeSlotTypeRequest = {
            "slot_type_id": slot_type_id,
            "bot_id": bot_id,
            "bot_version": bot_version,
            "locale_id": locale_id,
        }

        response = await aexecute_pipeline(
            AsyncOperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        await response.response.aclose()
        return response.output

    async def describe_test_execution(
        self,
        test_execution_id: "capo_lex_models_v2.types.id.Id",
        *,
        config_overrides: Optional[AsyncLexModelsV2ClientConfig] = None,
    ) -> "capo_lex_models_v2.types.describe_test_execution_response.DescribeTestExecutionResponse":
        """<p>Gets metadata information about the test execution.</p>

        Args:
            test_execution_id: <p>The execution Id of the test set execution.</p>

        Raises:
            capo_lex_models_v2.errors.internal_server_exception.InternalServerException: <p>The service encountered an unexpected condition. Try your request again.</p>
            capo_lex_models_v2.errors.resource_not_found_exception.ResourceNotFoundException: <p>You asked to describe a resource that doesn't exist. Check the resource that you are requesting and try again.</p>
            capo_lex_models_v2.errors.service_quota_exceeded_exception.ServiceQuotaExceededException: <p>You have reached a quota for your bot. </p>
            capo_lex_models_v2.errors.throttling_exception.ThrottlingException: <p>Your request rate is too high. Reduce the frequency of requests.</p>
            capo_lex_models_v2.errors.validation_exception.ValidationException: <p>One of the input parameters in your request isn't valid. Check the parameters and try your request again.</p>
            capo_lex_models_v2.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        async def _handler(
            req: "AsyncOperationRequest[capo_lex_models_v2.types.describe_test_execution_request.DescribeTestExecutionRequest]",
        ) -> AsyncOperationResponse[
            "capo_lex_models_v2.types.describe_test_execution_response.DescribeTestExecutionResponse"
        ]:
            import capo_lex_models_v2._operations.lex_model_building_service_v2.describe_test_execution

            (
                output,
                http_response,
            ) = await capo_lex_models_v2._operations.lex_model_building_service_v2.describe_test_execution.async_describe_test_execution(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_lex_models_v2.types.describe_test_execution_request.DescribeTestExecutionRequest = {
            "test_execution_id": test_execution_id
        }

        response = await aexecute_pipeline(
            AsyncOperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        await response.response.aclose()
        return response.output

    async def describe_test_set(
        self,
        test_set_id: "capo_lex_models_v2.types.id.Id",
        *,
        config_overrides: Optional[AsyncLexModelsV2ClientConfig] = None,
    ) -> "capo_lex_models_v2.types.describe_test_set_response.DescribeTestSetResponse":
        """<p>Gets metadata information about the test set.</p>

        Args:
            test_set_id: <p>The test set Id for the test set request.</p>

        Raises:
            capo_lex_models_v2.errors.internal_server_exception.InternalServerException: <p>The service encountered an unexpected condition. Try your request again.</p>
            capo_lex_models_v2.errors.resource_not_found_exception.ResourceNotFoundException: <p>You asked to describe a resource that doesn't exist. Check the resource that you are requesting and try again.</p>
            capo_lex_models_v2.errors.service_quota_exceeded_exception.ServiceQuotaExceededException: <p>You have reached a quota for your bot. </p>
            capo_lex_models_v2.errors.throttling_exception.ThrottlingException: <p>Your request rate is too high. Reduce the frequency of requests.</p>
            capo_lex_models_v2.errors.validation_exception.ValidationException: <p>One of the input parameters in your request isn't valid. Check the parameters and try your request again.</p>
            capo_lex_models_v2.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        async def _handler(
            req: "AsyncOperationRequest[capo_lex_models_v2.types.describe_test_set_request.DescribeTestSetRequest]",
        ) -> AsyncOperationResponse[
            "capo_lex_models_v2.types.describe_test_set_response.DescribeTestSetResponse"
        ]:
            import capo_lex_models_v2._operations.lex_model_building_service_v2.describe_test_set

            (
                output,
                http_response,
            ) = await capo_lex_models_v2._operations.lex_model_building_service_v2.describe_test_set.async_describe_test_set(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_lex_models_v2.types.describe_test_set_request.DescribeTestSetRequest = {
            "test_set_id": test_set_id
        }

        response = await aexecute_pipeline(
            AsyncOperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        await response.response.aclose()
        return response.output

    async def describe_test_set_discrepancy_report(
        self,
        test_set_discrepancy_report_id: "capo_lex_models_v2.types.id.Id",
        *,
        config_overrides: Optional[AsyncLexModelsV2ClientConfig] = None,
    ) -> "capo_lex_models_v2.types.describe_test_set_discrepancy_report_response.DescribeTestSetDiscrepancyReportResponse":
        """<p>Gets metadata information about the test set discrepancy report.</p>

        Args:
            test_set_discrepancy_report_id: <p>The unique identifier of the test set discrepancy report.</p>

        Raises:
            capo_lex_models_v2.errors.internal_server_exception.InternalServerException: <p>The service encountered an unexpected condition. Try your request again.</p>
            capo_lex_models_v2.errors.resource_not_found_exception.ResourceNotFoundException: <p>You asked to describe a resource that doesn't exist. Check the resource that you are requesting and try again.</p>
            capo_lex_models_v2.errors.service_quota_exceeded_exception.ServiceQuotaExceededException: <p>You have reached a quota for your bot. </p>
            capo_lex_models_v2.errors.throttling_exception.ThrottlingException: <p>Your request rate is too high. Reduce the frequency of requests.</p>
            capo_lex_models_v2.errors.validation_exception.ValidationException: <p>One of the input parameters in your request isn't valid. Check the parameters and try your request again.</p>
            capo_lex_models_v2.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        async def _handler(
            req: "AsyncOperationRequest[capo_lex_models_v2.types.describe_test_set_discrepancy_report_request.DescribeTestSetDiscrepancyReportRequest]",
        ) -> AsyncOperationResponse[
            "capo_lex_models_v2.types.describe_test_set_discrepancy_report_response.DescribeTestSetDiscrepancyReportResponse"
        ]:
            import capo_lex_models_v2._operations.lex_model_building_service_v2.describe_test_set_discrepancy_report

            (
                output,
                http_response,
            ) = await capo_lex_models_v2._operations.lex_model_building_service_v2.describe_test_set_discrepancy_report.async_describe_test_set_discrepancy_report(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_lex_models_v2.types.describe_test_set_discrepancy_report_request.DescribeTestSetDiscrepancyReportRequest = {
            "test_set_discrepancy_report_id": test_set_discrepancy_report_id
        }

        response = await aexecute_pipeline(
            AsyncOperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        await response.response.aclose()
        return response.output

    async def describe_test_set_generation(
        self,
        test_set_generation_id: "capo_lex_models_v2.types.id.Id",
        *,
        config_overrides: Optional[AsyncLexModelsV2ClientConfig] = None,
    ) -> "capo_lex_models_v2.types.describe_test_set_generation_response.DescribeTestSetGenerationResponse":
        """<p>Gets metadata information about the test set generation.</p>

        Args:
            test_set_generation_id: <p>The unique identifier of the test set generation.</p>

        Raises:
            capo_lex_models_v2.errors.internal_server_exception.InternalServerException: <p>The service encountered an unexpected condition. Try your request again.</p>
            capo_lex_models_v2.errors.resource_not_found_exception.ResourceNotFoundException: <p>You asked to describe a resource that doesn't exist. Check the resource that you are requesting and try again.</p>
            capo_lex_models_v2.errors.service_quota_exceeded_exception.ServiceQuotaExceededException: <p>You have reached a quota for your bot. </p>
            capo_lex_models_v2.errors.throttling_exception.ThrottlingException: <p>Your request rate is too high. Reduce the frequency of requests.</p>
            capo_lex_models_v2.errors.validation_exception.ValidationException: <p>One of the input parameters in your request isn't valid. Check the parameters and try your request again.</p>
            capo_lex_models_v2.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        async def _handler(
            req: "AsyncOperationRequest[capo_lex_models_v2.types.describe_test_set_generation_request.DescribeTestSetGenerationRequest]",
        ) -> AsyncOperationResponse[
            "capo_lex_models_v2.types.describe_test_set_generation_response.DescribeTestSetGenerationResponse"
        ]:
            import capo_lex_models_v2._operations.lex_model_building_service_v2.describe_test_set_generation

            (
                output,
                http_response,
            ) = await capo_lex_models_v2._operations.lex_model_building_service_v2.describe_test_set_generation.async_describe_test_set_generation(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_lex_models_v2.types.describe_test_set_generation_request.DescribeTestSetGenerationRequest = {
            "test_set_generation_id": test_set_generation_id
        }

        response = await aexecute_pipeline(
            AsyncOperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        await response.response.aclose()
        return response.output

    async def generate_bot_element(
        self,
        intent_id: "capo_lex_models_v2.types.id.Id",
        bot_id: "capo_lex_models_v2.types.id.Id",
        bot_version: "capo_lex_models_v2.types.bot_version.BotVersion",
        locale_id: "capo_lex_models_v2.types.locale_id.LocaleId",
        *,
        config_overrides: Optional[AsyncLexModelsV2ClientConfig] = None,
    ) -> "capo_lex_models_v2.types.generate_bot_element_response.GenerateBotElementResponse":
        """<p>Generates sample utterances for an intent.</p>

        Args:
            intent_id: <p>The intent unique Id for the bot request to generate utterances.</p>
            bot_id: <p>The bot unique Id for the bot request to generate utterances.</p>
            bot_version: <p>The bot version for the bot request to generate utterances.</p>
            locale_id: <p>The unique locale Id for the bot request to generate utterances.</p>

        Raises:
            capo_lex_models_v2.errors.conflict_exception.ConflictException: <p>The action that you tried to perform couldn't be completed because the resource is in a conflicting state. For example, deleting a bot that is in the CREATING state. Try your request again. </p>
            capo_lex_models_v2.errors.internal_server_exception.InternalServerException: <p>The service encountered an unexpected condition. Try your request again.</p>
            capo_lex_models_v2.errors.precondition_failed_exception.PreconditionFailedException: <p>Your request couldn't be completed because one or more request fields aren't valid. Check the fields in your request and try again.</p>
            capo_lex_models_v2.errors.resource_not_found_exception.ResourceNotFoundException: <p>You asked to describe a resource that doesn't exist. Check the resource that you are requesting and try again.</p>
            capo_lex_models_v2.errors.service_quota_exceeded_exception.ServiceQuotaExceededException: <p>You have reached a quota for your bot. </p>
            capo_lex_models_v2.errors.throttling_exception.ThrottlingException: <p>Your request rate is too high. Reduce the frequency of requests.</p>
            capo_lex_models_v2.errors.validation_exception.ValidationException: <p>One of the input parameters in your request isn't valid. Check the parameters and try your request again.</p>
            capo_lex_models_v2.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        async def _handler(
            req: "AsyncOperationRequest[capo_lex_models_v2.types.generate_bot_element_request.GenerateBotElementRequest]",
        ) -> AsyncOperationResponse[
            "capo_lex_models_v2.types.generate_bot_element_response.GenerateBotElementResponse"
        ]:
            import capo_lex_models_v2._operations.lex_model_building_service_v2.generate_bot_element

            (
                output,
                http_response,
            ) = await capo_lex_models_v2._operations.lex_model_building_service_v2.generate_bot_element.async_generate_bot_element(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_lex_models_v2.types.generate_bot_element_request.GenerateBotElementRequest = {
            "intent_id": intent_id,
            "bot_id": bot_id,
            "bot_version": bot_version,
            "locale_id": locale_id,
        }

        response = await aexecute_pipeline(
            AsyncOperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        await response.response.aclose()
        return response.output

    async def get_test_execution_artifacts_url(
        self,
        test_execution_id: "capo_lex_models_v2.types.id.Id",
        *,
        config_overrides: Optional[AsyncLexModelsV2ClientConfig] = None,
    ) -> "capo_lex_models_v2.types.get_test_execution_artifacts_url_response.GetTestExecutionArtifactsUrlResponse":
        """<p>The pre-signed Amazon S3 URL to download the test execution result artifacts.</p>

        Args:
            test_execution_id: <p>The unique identifier of the completed test execution.</p>

        Raises:
            capo_lex_models_v2.errors.internal_server_exception.InternalServerException: <p>The service encountered an unexpected condition. Try your request again.</p>
            capo_lex_models_v2.errors.resource_not_found_exception.ResourceNotFoundException: <p>You asked to describe a resource that doesn't exist. Check the resource that you are requesting and try again.</p>
            capo_lex_models_v2.errors.service_quota_exceeded_exception.ServiceQuotaExceededException: <p>You have reached a quota for your bot. </p>
            capo_lex_models_v2.errors.throttling_exception.ThrottlingException: <p>Your request rate is too high. Reduce the frequency of requests.</p>
            capo_lex_models_v2.errors.validation_exception.ValidationException: <p>One of the input parameters in your request isn't valid. Check the parameters and try your request again.</p>
            capo_lex_models_v2.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        async def _handler(
            req: "AsyncOperationRequest[capo_lex_models_v2.types.get_test_execution_artifacts_url_request.GetTestExecutionArtifactsUrlRequest]",
        ) -> AsyncOperationResponse[
            "capo_lex_models_v2.types.get_test_execution_artifacts_url_response.GetTestExecutionArtifactsUrlResponse"
        ]:
            import capo_lex_models_v2._operations.lex_model_building_service_v2.get_test_execution_artifacts_url

            (
                output,
                http_response,
            ) = await capo_lex_models_v2._operations.lex_model_building_service_v2.get_test_execution_artifacts_url.async_get_test_execution_artifacts_url(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_lex_models_v2.types.get_test_execution_artifacts_url_request.GetTestExecutionArtifactsUrlRequest = {
            "test_execution_id": test_execution_id
        }

        response = await aexecute_pipeline(
            AsyncOperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        await response.response.aclose()
        return response.output

    async def list_aggregated_utterances(
        self,
        bot_id: "capo_lex_models_v2.types.id.Id",
        locale_id: "capo_lex_models_v2.types.locale_id.LocaleId",
        aggregation_duration: "capo_lex_models_v2.types.utterance_aggregation_duration.UtteranceAggregationDuration",
        *,
        config_overrides: Optional[AsyncLexModelsV2ClientConfig] = None,
        bot_alias_id: Optional[
            "capo_lex_models_v2.types.bot_alias_id.BotAliasId"
        ] = None,
        bot_version: Optional["capo_lex_models_v2.types.bot_version.BotVersion"] = None,
        sort_by: Optional[
            "capo_lex_models_v2.types.aggregated_utterances_sort_by.AggregatedUtterancesSortBy"
        ] = None,
        filters: Optional[
            "capo_lex_models_v2.types.aggregated_utterances_filters.AggregatedUtterancesFilters"
        ] = None,
        max_results: Optional["capo_lex_models_v2.types.max_results.MaxResults"] = None,
        next_token: Optional["capo_lex_models_v2.types.next_token.NextToken"] = None,
    ) -> "capo_lex_models_v2.types.list_aggregated_utterances_response.ListAggregatedUtterancesResponse":
        """<p>Provides a list of utterances that users have sent to the bot.</p> <p>Utterances are aggregated by the text of the utterance. For example, all instances where customers used the phrase "I want to order pizza" are aggregated into the same line in the response.</p> <p>You can see both detected utterances and missed utterances. A detected utterance is where the bot properly recognized the utterance and activated the associated intent. A missed utterance was not recognized by the bot and didn't activate an intent.</p> <p>Utterances can be aggregated for a bot alias or for a bot version, but not both at the same time.</p> <p>Utterances statistics are not generated under the following conditions:</p> <ul> <li> <p>The <code>childDirected</code> field was set to true when the bot was created.</p> </li> <li> <p>You are using slot obfuscation with one or more slots.</p> </li> <li> <p>You opted out of participating in improving Amazon Lex.</p> </li> </ul>

        Args:
            bot_id: <p>The unique identifier of the bot associated with this request.</p>
            bot_alias_id: <p>The identifier of the bot alias associated with this request. If you specify the bot alias, you can't specify the bot version.</p>
            bot_version: <p>The identifier of the bot version associated with this request. If you specify the bot version, you can't specify the bot alias.</p>
            locale_id: <p>The identifier of the language and locale where the utterances were collected. For more information, see <a href="https://docs.aws.amazon.com/lexv2/latest/dg/how-languages.html">Supported languages</a>.</p>
            aggregation_duration: <p>The time window for aggregating the utterance information. You can specify a time between one hour and two weeks.</p>
            sort_by: <p>Specifies sorting parameters for the list of utterances. You can sort by the hit count, the missed count, or the number of distinct sessions the utterance appeared in.</p>
            filters: <p>Provides the specification of a filter used to limit the utterances in the response to only those that match the filter specification. You can only specify one filter and one string to filter on.</p>
            max_results: <p>The maximum number of utterances to return in each page of results. If there are fewer results than the maximum page size, only the actual number of results are returned. If you don't specify the <code>maxResults</code> parameter, 1,000 results are returned.</p>
            next_token: <p>If the response from the <code>ListAggregatedUtterances</code> operation contains more results that specified in the <code>maxResults</code> parameter, a token is returned in the response. Use that token in the <code>nextToken</code> parameter to return the next page of results.</p>

        Raises:
            capo_lex_models_v2.errors.internal_server_exception.InternalServerException: <p>The service encountered an unexpected condition. Try your request again.</p>
            capo_lex_models_v2.errors.precondition_failed_exception.PreconditionFailedException: <p>Your request couldn't be completed because one or more request fields aren't valid. Check the fields in your request and try again.</p>
            capo_lex_models_v2.errors.throttling_exception.ThrottlingException: <p>Your request rate is too high. Reduce the frequency of requests.</p>
            capo_lex_models_v2.errors.validation_exception.ValidationException: <p>One of the input parameters in your request isn't valid. Check the parameters and try your request again.</p>
            capo_lex_models_v2.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        async def _handler(
            req: "AsyncOperationRequest[capo_lex_models_v2.types.list_aggregated_utterances_request.ListAggregatedUtterancesRequest]",
        ) -> AsyncOperationResponse[
            "capo_lex_models_v2.types.list_aggregated_utterances_response.ListAggregatedUtterancesResponse"
        ]:
            import capo_lex_models_v2._operations.lex_model_building_service_v2.list_aggregated_utterances

            (
                output,
                http_response,
            ) = await capo_lex_models_v2._operations.lex_model_building_service_v2.list_aggregated_utterances.async_list_aggregated_utterances(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_lex_models_v2.types.list_aggregated_utterances_request.ListAggregatedUtterancesRequest = {
            "bot_id": bot_id,
            "locale_id": locale_id,
            "aggregation_duration": aggregation_duration,
        }
        if bot_alias_id is not None:
            input_["bot_alias_id"] = bot_alias_id
        if bot_version is not None:
            input_["bot_version"] = bot_version
        if sort_by is not None:
            input_["sort_by"] = sort_by
        if filters is not None:
            input_["filters"] = filters
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

    async def iter_list_aggregated_utterances(
        self,
        bot_id: "capo_lex_models_v2.types.id.Id",
        locale_id: "capo_lex_models_v2.types.locale_id.LocaleId",
        aggregation_duration: "capo_lex_models_v2.types.utterance_aggregation_duration.UtteranceAggregationDuration",
        *,
        config_overrides: Optional[AsyncLexModelsV2ClientConfig] = None,
        bot_alias_id: Optional[
            "capo_lex_models_v2.types.bot_alias_id.BotAliasId"
        ] = None,
        bot_version: Optional["capo_lex_models_v2.types.bot_version.BotVersion"] = None,
        sort_by: Optional[
            "capo_lex_models_v2.types.aggregated_utterances_sort_by.AggregatedUtterancesSortBy"
        ] = None,
        filters: Optional[
            "capo_lex_models_v2.types.aggregated_utterances_filters.AggregatedUtterancesFilters"
        ] = None,
        max_results: Optional["capo_lex_models_v2.types.max_results.MaxResults"] = None,
        next_token: Optional["capo_lex_models_v2.types.next_token.NextToken"] = None,
    ) -> "AsyncIterator[capo_lex_models_v2.types.list_aggregated_utterances_response.ListAggregatedUtterancesResponse]":
        _token = next_token
        while True:
            _response = await self.list_aggregated_utterances(
                bot_id,
                locale_id,
                aggregation_duration,
                config_overrides=config_overrides,
                bot_alias_id=bot_alias_id,
                bot_version=bot_version,
                sort_by=sort_by,
                filters=filters,
                max_results=max_results,
                next_token=_token,
            )
            yield _response
            _token = _resolve_path(_response, ("next_token",))
            if not _token:
                break

    async def list_bot_aliases(
        self,
        bot_id: "capo_lex_models_v2.types.id.Id",
        *,
        config_overrides: Optional[AsyncLexModelsV2ClientConfig] = None,
        max_results: Optional["capo_lex_models_v2.types.max_results.MaxResults"] = None,
        next_token: Optional["capo_lex_models_v2.types.next_token.NextToken"] = None,
    ) -> "capo_lex_models_v2.types.list_bot_aliases_response.ListBotAliasesResponse":
        """<p>Gets a list of aliases for the specified bot.</p>

        Args:
            bot_id: <p>The identifier of the bot to list aliases for.</p>
            max_results: <p>The maximum number of aliases to return in each page of results. If there are fewer results than the max page size, only the actual number of results are returned.</p>
            next_token: <p>If the response from the <code>ListBotAliases</code> operation contains more results than specified in the <code>maxResults</code> parameter, a token is returned in the response. Use that token in the <code>nextToken</code> parameter to return the next page of results.</p>

        Raises:
            capo_lex_models_v2.errors.internal_server_exception.InternalServerException: <p>The service encountered an unexpected condition. Try your request again.</p>
            capo_lex_models_v2.errors.service_quota_exceeded_exception.ServiceQuotaExceededException: <p>You have reached a quota for your bot. </p>
            capo_lex_models_v2.errors.throttling_exception.ThrottlingException: <p>Your request rate is too high. Reduce the frequency of requests.</p>
            capo_lex_models_v2.errors.validation_exception.ValidationException: <p>One of the input parameters in your request isn't valid. Check the parameters and try your request again.</p>
            capo_lex_models_v2.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        async def _handler(
            req: "AsyncOperationRequest[capo_lex_models_v2.types.list_bot_aliases_request.ListBotAliasesRequest]",
        ) -> AsyncOperationResponse[
            "capo_lex_models_v2.types.list_bot_aliases_response.ListBotAliasesResponse"
        ]:
            import capo_lex_models_v2._operations.lex_model_building_service_v2.list_bot_aliases

            (
                output,
                http_response,
            ) = await capo_lex_models_v2._operations.lex_model_building_service_v2.list_bot_aliases.async_list_bot_aliases(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_lex_models_v2.types.list_bot_aliases_request.ListBotAliasesRequest = {
            "bot_id": bot_id
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

    async def iter_list_bot_aliases(
        self,
        bot_id: "capo_lex_models_v2.types.id.Id",
        *,
        config_overrides: Optional[AsyncLexModelsV2ClientConfig] = None,
        max_results: Optional["capo_lex_models_v2.types.max_results.MaxResults"] = None,
        next_token: Optional["capo_lex_models_v2.types.next_token.NextToken"] = None,
    ) -> "AsyncIterator[capo_lex_models_v2.types.list_bot_aliases_response.ListBotAliasesResponse]":
        _token = next_token
        while True:
            _response = await self.list_bot_aliases(
                bot_id,
                config_overrides=config_overrides,
                max_results=max_results,
                next_token=_token,
            )
            yield _response
            _token = _resolve_path(_response, ("next_token",))
            if not _token:
                break

    async def list_bot_alias_replicas(
        self,
        bot_id: "capo_lex_models_v2.types.id.Id",
        replica_region: "capo_lex_models_v2.types.replica_region.ReplicaRegion",
        *,
        config_overrides: Optional[AsyncLexModelsV2ClientConfig] = None,
        max_results: Optional["capo_lex_models_v2.types.max_results.MaxResults"] = None,
        next_token: Optional["capo_lex_models_v2.types.next_token.NextToken"] = None,
    ) -> "capo_lex_models_v2.types.list_bot_alias_replicas_response.ListBotAliasReplicasResponse":
        """<p>The action to list the replicated bots created from the source bot alias.</p>

        Args:
            bot_id: <p>The request for the unique bot ID of the replicated bot created from the source bot alias.</p>
            replica_region: <p>The request for the secondary region of the replicated bot created from the source bot alias.</p>
            max_results: <p>The request for maximum results to list the replicated bots created from the source bot alias.</p>
            next_token: <p>The request for the next token for the replicated bot created from the source bot alias.</p>

        Raises:
            capo_lex_models_v2.errors.internal_server_exception.InternalServerException: <p>The service encountered an unexpected condition. Try your request again.</p>
            capo_lex_models_v2.errors.service_quota_exceeded_exception.ServiceQuotaExceededException: <p>You have reached a quota for your bot. </p>
            capo_lex_models_v2.errors.throttling_exception.ThrottlingException: <p>Your request rate is too high. Reduce the frequency of requests.</p>
            capo_lex_models_v2.errors.validation_exception.ValidationException: <p>One of the input parameters in your request isn't valid. Check the parameters and try your request again.</p>
            capo_lex_models_v2.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        async def _handler(
            req: "AsyncOperationRequest[capo_lex_models_v2.types.list_bot_alias_replicas_request.ListBotAliasReplicasRequest]",
        ) -> AsyncOperationResponse[
            "capo_lex_models_v2.types.list_bot_alias_replicas_response.ListBotAliasReplicasResponse"
        ]:
            import capo_lex_models_v2._operations.lex_model_building_service_v2.list_bot_alias_replicas

            (
                output,
                http_response,
            ) = await capo_lex_models_v2._operations.lex_model_building_service_v2.list_bot_alias_replicas.async_list_bot_alias_replicas(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_lex_models_v2.types.list_bot_alias_replicas_request.ListBotAliasReplicasRequest = {
            "bot_id": bot_id,
            "replica_region": replica_region,
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

    async def iter_list_bot_alias_replicas(
        self,
        bot_id: "capo_lex_models_v2.types.id.Id",
        replica_region: "capo_lex_models_v2.types.replica_region.ReplicaRegion",
        *,
        config_overrides: Optional[AsyncLexModelsV2ClientConfig] = None,
        max_results: Optional["capo_lex_models_v2.types.max_results.MaxResults"] = None,
        next_token: Optional["capo_lex_models_v2.types.next_token.NextToken"] = None,
    ) -> "AsyncIterator[capo_lex_models_v2.types.list_bot_alias_replicas_response.ListBotAliasReplicasResponse]":
        _token = next_token
        while True:
            _response = await self.list_bot_alias_replicas(
                bot_id,
                replica_region,
                config_overrides=config_overrides,
                max_results=max_results,
                next_token=_token,
            )
            yield _response
            _token = _resolve_path(_response, ("next_token",))
            if not _token:
                break

    async def list_bot_analyzer_history(
        self,
        bot_id: "capo_lex_models_v2.types.id.Id",
        *,
        config_overrides: Optional[AsyncLexModelsV2ClientConfig] = None,
        locale_id: Optional["capo_lex_models_v2.types.locale_id.LocaleId"] = None,
        bot_version: Optional[
            "capo_lex_models_v2.types.draft_bot_version.DraftBotVersion"
        ] = None,
        next_token: Optional["capo_lex_models_v2.types.next_token.NextToken"] = None,
        max_results: Optional["capo_lex_models_v2.types.max_results.MaxResults"] = None,
    ) -> "capo_lex_models_v2.types.list_bot_analyzer_history_response.ListBotAnalyzerHistoryResponse":
        """<p>Retrieves a list of historical bot analysis executions for a specific bot. You can filter the results by locale and bot version.</p> <p>The history includes all analysis executions regardless of their status, allowing you to track past analyses and their outcomes.</p>

        Args:
            bot_id: <p>The unique identifier of the bot.</p>
            locale_id: <p>The locale identifier to filter the history. If not specified, returns history for all locales.</p>
            bot_version: <p>The bot version to filter the history. If not specified, defaults to <code>DRAFT</code>.</p>
            next_token: <p>If the response from a previous request was truncated, the <code>nextToken</code> value is used to retrieve the next page of history entries.</p>
            max_results: <p>The maximum number of history entries to return in the response. The default is 10.</p>

        Raises:
            capo_lex_models_v2.errors.internal_server_exception.InternalServerException: <p>The service encountered an unexpected condition. Try your request again.</p>
            capo_lex_models_v2.errors.resource_not_found_exception.ResourceNotFoundException: <p>You asked to describe a resource that doesn't exist. Check the resource that you are requesting and try again.</p>
            capo_lex_models_v2.errors.throttling_exception.ThrottlingException: <p>Your request rate is too high. Reduce the frequency of requests.</p>
            capo_lex_models_v2.errors.validation_exception.ValidationException: <p>One of the input parameters in your request isn't valid. Check the parameters and try your request again.</p>
            capo_lex_models_v2.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        async def _handler(
            req: "AsyncOperationRequest[capo_lex_models_v2.types.list_bot_analyzer_history_request.ListBotAnalyzerHistoryRequest]",
        ) -> AsyncOperationResponse[
            "capo_lex_models_v2.types.list_bot_analyzer_history_response.ListBotAnalyzerHistoryResponse"
        ]:
            import capo_lex_models_v2._operations.lex_model_building_service_v2.list_bot_analyzer_history

            (
                output,
                http_response,
            ) = await capo_lex_models_v2._operations.lex_model_building_service_v2.list_bot_analyzer_history.async_list_bot_analyzer_history(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_lex_models_v2.types.list_bot_analyzer_history_request.ListBotAnalyzerHistoryRequest = {
            "bot_id": bot_id
        }
        if locale_id is not None:
            input_["locale_id"] = locale_id
        if bot_version is not None:
            input_["bot_version"] = bot_version
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

    async def iter_list_bot_analyzer_history(
        self,
        bot_id: "capo_lex_models_v2.types.id.Id",
        *,
        config_overrides: Optional[AsyncLexModelsV2ClientConfig] = None,
        locale_id: Optional["capo_lex_models_v2.types.locale_id.LocaleId"] = None,
        bot_version: Optional[
            "capo_lex_models_v2.types.draft_bot_version.DraftBotVersion"
        ] = None,
        next_token: Optional["capo_lex_models_v2.types.next_token.NextToken"] = None,
        max_results: Optional["capo_lex_models_v2.types.max_results.MaxResults"] = None,
    ) -> "AsyncIterator[capo_lex_models_v2.types.bot_analyzer_history_summary.BotAnalyzerHistorySummary]":
        _token = next_token
        while True:
            _response = await self.list_bot_analyzer_history(
                bot_id,
                config_overrides=config_overrides,
                locale_id=locale_id,
                bot_version=bot_version,
                next_token=_token,
                max_results=max_results,
            )
            _page = _resolve_path(_response, ("bot_analyzer_history_list",))
            for _item in _page or []:
                yield _item
            _token = _resolve_path(_response, ("next_token",))
            if not _token:
                break

    async def list_bot_locales(
        self,
        bot_id: "capo_lex_models_v2.types.id.Id",
        bot_version: "capo_lex_models_v2.types.bot_version.BotVersion",
        *,
        config_overrides: Optional[AsyncLexModelsV2ClientConfig] = None,
        sort_by: Optional[
            "capo_lex_models_v2.types.bot_locale_sort_by.BotLocaleSortBy"
        ] = None,
        filters: Optional[
            "capo_lex_models_v2.types.bot_locale_filters.BotLocaleFilters"
        ] = None,
        max_results: Optional["capo_lex_models_v2.types.max_results.MaxResults"] = None,
        next_token: Optional["capo_lex_models_v2.types.next_token.NextToken"] = None,
    ) -> "capo_lex_models_v2.types.list_bot_locales_response.ListBotLocalesResponse":
        """<p>Gets a list of locales for the specified bot.</p>

        Args:
            bot_id: <p>The identifier of the bot to list locales for.</p>
            bot_version: <p>The version of the bot to list locales for.</p>
            sort_by: <p>Specifies sorting parameters for the list of locales. You can sort by locale name in ascending or descending order.</p>
            filters: <p>Provides the specification for a filter used to limit the response to only those locales that match the filter specification. You can only specify one filter and one value to filter on.</p>
            max_results: <p>The maximum number of aliases to return in each page of results. If there are fewer results than the max page size, only the actual number of results are returned.</p>
            next_token: <p>If the response from the <code>ListBotLocales</code> operation contains more results than specified in the <code>maxResults</code> parameter, a token is returned in the response. Use that token as the <code>nextToken</code> parameter to return the next page of results. </p>

        Raises:
            capo_lex_models_v2.errors.internal_server_exception.InternalServerException: <p>The service encountered an unexpected condition. Try your request again.</p>
            capo_lex_models_v2.errors.service_quota_exceeded_exception.ServiceQuotaExceededException: <p>You have reached a quota for your bot. </p>
            capo_lex_models_v2.errors.throttling_exception.ThrottlingException: <p>Your request rate is too high. Reduce the frequency of requests.</p>
            capo_lex_models_v2.errors.validation_exception.ValidationException: <p>One of the input parameters in your request isn't valid. Check the parameters and try your request again.</p>
            capo_lex_models_v2.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        async def _handler(
            req: "AsyncOperationRequest[capo_lex_models_v2.types.list_bot_locales_request.ListBotLocalesRequest]",
        ) -> AsyncOperationResponse[
            "capo_lex_models_v2.types.list_bot_locales_response.ListBotLocalesResponse"
        ]:
            import capo_lex_models_v2._operations.lex_model_building_service_v2.list_bot_locales

            (
                output,
                http_response,
            ) = await capo_lex_models_v2._operations.lex_model_building_service_v2.list_bot_locales.async_list_bot_locales(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_lex_models_v2.types.list_bot_locales_request.ListBotLocalesRequest = {
            "bot_id": bot_id,
            "bot_version": bot_version,
        }
        if sort_by is not None:
            input_["sort_by"] = sort_by
        if filters is not None:
            input_["filters"] = filters
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

    async def iter_list_bot_locales(
        self,
        bot_id: "capo_lex_models_v2.types.id.Id",
        bot_version: "capo_lex_models_v2.types.bot_version.BotVersion",
        *,
        config_overrides: Optional[AsyncLexModelsV2ClientConfig] = None,
        sort_by: Optional[
            "capo_lex_models_v2.types.bot_locale_sort_by.BotLocaleSortBy"
        ] = None,
        filters: Optional[
            "capo_lex_models_v2.types.bot_locale_filters.BotLocaleFilters"
        ] = None,
        max_results: Optional["capo_lex_models_v2.types.max_results.MaxResults"] = None,
        next_token: Optional["capo_lex_models_v2.types.next_token.NextToken"] = None,
    ) -> "AsyncIterator[capo_lex_models_v2.types.list_bot_locales_response.ListBotLocalesResponse]":
        _token = next_token
        while True:
            _response = await self.list_bot_locales(
                bot_id,
                bot_version,
                config_overrides=config_overrides,
                sort_by=sort_by,
                filters=filters,
                max_results=max_results,
                next_token=_token,
            )
            yield _response
            _token = _resolve_path(_response, ("next_token",))
            if not _token:
                break

    async def list_bot_recommendations(
        self,
        bot_id: "capo_lex_models_v2.types.id.Id",
        bot_version: "capo_lex_models_v2.types.draft_bot_version.DraftBotVersion",
        locale_id: "capo_lex_models_v2.types.locale_id.LocaleId",
        *,
        config_overrides: Optional[AsyncLexModelsV2ClientConfig] = None,
        max_results: Optional["capo_lex_models_v2.types.max_results.MaxResults"] = None,
        next_token: Optional["capo_lex_models_v2.types.next_token.NextToken"] = None,
    ) -> "capo_lex_models_v2.types.list_bot_recommendations_response.ListBotRecommendationsResponse":
        """<p>Get a list of bot recommendations that meet the specified criteria.</p>

        Args:
            bot_id: <p>The unique identifier of the bot that contains the bot recommendation list.</p>
            bot_version: <p>The version of the bot that contains the bot recommendation list.</p>
            locale_id: <p>The identifier of the language and locale of the bot recommendation list.</p>
            max_results: <p>The maximum number of bot recommendations to return in each page of results. If there are fewer results than the max page size, only the actual number of results are returned.</p>
            next_token: <p>If the response from the ListBotRecommendation operation contains more results than specified in the maxResults parameter, a token is returned in the response. Use that token in the nextToken parameter to return the next page of results.</p>

        Raises:
            capo_lex_models_v2.errors.internal_server_exception.InternalServerException: <p>The service encountered an unexpected condition. Try your request again.</p>
            capo_lex_models_v2.errors.resource_not_found_exception.ResourceNotFoundException: <p>You asked to describe a resource that doesn't exist. Check the resource that you are requesting and try again.</p>
            capo_lex_models_v2.errors.throttling_exception.ThrottlingException: <p>Your request rate is too high. Reduce the frequency of requests.</p>
            capo_lex_models_v2.errors.validation_exception.ValidationException: <p>One of the input parameters in your request isn't valid. Check the parameters and try your request again.</p>
            capo_lex_models_v2.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        async def _handler(
            req: "AsyncOperationRequest[capo_lex_models_v2.types.list_bot_recommendations_request.ListBotRecommendationsRequest]",
        ) -> AsyncOperationResponse[
            "capo_lex_models_v2.types.list_bot_recommendations_response.ListBotRecommendationsResponse"
        ]:
            import capo_lex_models_v2._operations.lex_model_building_service_v2.list_bot_recommendations

            (
                output,
                http_response,
            ) = await capo_lex_models_v2._operations.lex_model_building_service_v2.list_bot_recommendations.async_list_bot_recommendations(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_lex_models_v2.types.list_bot_recommendations_request.ListBotRecommendationsRequest = {
            "bot_id": bot_id,
            "bot_version": bot_version,
            "locale_id": locale_id,
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

    async def iter_list_bot_recommendations(
        self,
        bot_id: "capo_lex_models_v2.types.id.Id",
        bot_version: "capo_lex_models_v2.types.draft_bot_version.DraftBotVersion",
        locale_id: "capo_lex_models_v2.types.locale_id.LocaleId",
        *,
        config_overrides: Optional[AsyncLexModelsV2ClientConfig] = None,
        max_results: Optional["capo_lex_models_v2.types.max_results.MaxResults"] = None,
        next_token: Optional["capo_lex_models_v2.types.next_token.NextToken"] = None,
    ) -> "AsyncIterator[capo_lex_models_v2.types.list_bot_recommendations_response.ListBotRecommendationsResponse]":
        _token = next_token
        while True:
            _response = await self.list_bot_recommendations(
                bot_id,
                bot_version,
                locale_id,
                config_overrides=config_overrides,
                max_results=max_results,
                next_token=_token,
            )
            yield _response
            _token = _resolve_path(_response, ("next_token",))
            if not _token:
                break

    async def list_bot_replicas(
        self,
        bot_id: "capo_lex_models_v2.types.id.Id",
        *,
        config_overrides: Optional[AsyncLexModelsV2ClientConfig] = None,
    ) -> "capo_lex_models_v2.types.list_bot_replicas_response.ListBotReplicasResponse":
        """<p>The action to list the replicated bots.</p>

        Args:
            bot_id: <p>The request for the unique bot IDs in the list of replicated bots.</p>

        Raises:
            capo_lex_models_v2.errors.internal_server_exception.InternalServerException: <p>The service encountered an unexpected condition. Try your request again.</p>
            capo_lex_models_v2.errors.service_quota_exceeded_exception.ServiceQuotaExceededException: <p>You have reached a quota for your bot. </p>
            capo_lex_models_v2.errors.throttling_exception.ThrottlingException: <p>Your request rate is too high. Reduce the frequency of requests.</p>
            capo_lex_models_v2.errors.validation_exception.ValidationException: <p>One of the input parameters in your request isn't valid. Check the parameters and try your request again.</p>
            capo_lex_models_v2.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        async def _handler(
            req: "AsyncOperationRequest[capo_lex_models_v2.types.list_bot_replicas_request.ListBotReplicasRequest]",
        ) -> AsyncOperationResponse[
            "capo_lex_models_v2.types.list_bot_replicas_response.ListBotReplicasResponse"
        ]:
            import capo_lex_models_v2._operations.lex_model_building_service_v2.list_bot_replicas

            (
                output,
                http_response,
            ) = await capo_lex_models_v2._operations.lex_model_building_service_v2.list_bot_replicas.async_list_bot_replicas(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_lex_models_v2.types.list_bot_replicas_request.ListBotReplicasRequest = {
            "bot_id": bot_id
        }

        response = await aexecute_pipeline(
            AsyncOperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        await response.response.aclose()
        return response.output

    async def list_bot_resource_generations(
        self,
        bot_id: "capo_lex_models_v2.types.id.Id",
        bot_version: "capo_lex_models_v2.types.bot_version.BotVersion",
        locale_id: "capo_lex_models_v2.types.locale_id.LocaleId",
        *,
        config_overrides: Optional[AsyncLexModelsV2ClientConfig] = None,
        sort_by: Optional[
            "capo_lex_models_v2.types.generation_sort_by.GenerationSortBy"
        ] = None,
        max_results: Optional["capo_lex_models_v2.types.max_results.MaxResults"] = None,
        next_token: Optional["capo_lex_models_v2.types.next_token.NextToken"] = None,
    ) -> "capo_lex_models_v2.types.list_bot_resource_generations_response.ListBotResourceGenerationsResponse":
        """<p>Lists the generation requests made for a bot locale.</p>

        Args:
            bot_id: <p>The unique identifier of the bot whose generation requests you want to view.</p>
            bot_version: <p>The version of the bot whose generation requests you want to view.</p>
            locale_id: <p>The locale of the bot whose generation requests you want to view.</p>
            sort_by: <p>An object containing information about the attribute and the method by which to sort the results</p>
            max_results: <p>The maximum number of results to return in the response.</p>
            next_token: <p>If the total number of results is greater than the number specified in the <code>maxResults</code>, the response returns a token in the <code>nextToken</code> field. Use this token when making a request to return the next batch of results.</p>

        Raises:
            capo_lex_models_v2.errors.internal_server_exception.InternalServerException: <p>The service encountered an unexpected condition. Try your request again.</p>
            capo_lex_models_v2.errors.resource_not_found_exception.ResourceNotFoundException: <p>You asked to describe a resource that doesn't exist. Check the resource that you are requesting and try again.</p>
            capo_lex_models_v2.errors.throttling_exception.ThrottlingException: <p>Your request rate is too high. Reduce the frequency of requests.</p>
            capo_lex_models_v2.errors.validation_exception.ValidationException: <p>One of the input parameters in your request isn't valid. Check the parameters and try your request again.</p>
            capo_lex_models_v2.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        async def _handler(
            req: "AsyncOperationRequest[capo_lex_models_v2.types.list_bot_resource_generations_request.ListBotResourceGenerationsRequest]",
        ) -> AsyncOperationResponse[
            "capo_lex_models_v2.types.list_bot_resource_generations_response.ListBotResourceGenerationsResponse"
        ]:
            import capo_lex_models_v2._operations.lex_model_building_service_v2.list_bot_resource_generations

            (
                output,
                http_response,
            ) = await capo_lex_models_v2._operations.lex_model_building_service_v2.list_bot_resource_generations.async_list_bot_resource_generations(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_lex_models_v2.types.list_bot_resource_generations_request.ListBotResourceGenerationsRequest = {
            "bot_id": bot_id,
            "bot_version": bot_version,
            "locale_id": locale_id,
        }
        if sort_by is not None:
            input_["sort_by"] = sort_by
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

    async def iter_list_bot_resource_generations(
        self,
        bot_id: "capo_lex_models_v2.types.id.Id",
        bot_version: "capo_lex_models_v2.types.bot_version.BotVersion",
        locale_id: "capo_lex_models_v2.types.locale_id.LocaleId",
        *,
        config_overrides: Optional[AsyncLexModelsV2ClientConfig] = None,
        sort_by: Optional[
            "capo_lex_models_v2.types.generation_sort_by.GenerationSortBy"
        ] = None,
        max_results: Optional["capo_lex_models_v2.types.max_results.MaxResults"] = None,
        next_token: Optional["capo_lex_models_v2.types.next_token.NextToken"] = None,
    ) -> "AsyncIterator[capo_lex_models_v2.types.list_bot_resource_generations_response.ListBotResourceGenerationsResponse]":
        _token = next_token
        while True:
            _response = await self.list_bot_resource_generations(
                bot_id,
                bot_version,
                locale_id,
                config_overrides=config_overrides,
                sort_by=sort_by,
                max_results=max_results,
                next_token=_token,
            )
            yield _response
            _token = _resolve_path(_response, ("next_token",))
            if not _token:
                break

    async def list_bots(
        self,
        *,
        config_overrides: Optional[AsyncLexModelsV2ClientConfig] = None,
        sort_by: Optional["capo_lex_models_v2.types.bot_sort_by.BotSortBy"] = None,
        filters: Optional["capo_lex_models_v2.types.bot_filters.BotFilters"] = None,
        max_results: Optional["capo_lex_models_v2.types.max_results.MaxResults"] = None,
        next_token: Optional["capo_lex_models_v2.types.next_token.NextToken"] = None,
    ) -> "capo_lex_models_v2.types.list_bots_response.ListBotsResponse":
        """<p>Gets a list of available bots.</p>

        Args:
            sort_by: <p>Specifies sorting parameters for the list of bots. You can specify that the list be sorted by bot name in ascending or descending order.</p>
            filters: <p>Provides the specification of a filter used to limit the bots in the response to only those that match the filter specification. You can only specify one filter and one string to filter on.</p>
            max_results: <p>The maximum number of bots to return in each page of results. If there are fewer results than the maximum page size, only the actual number of results are returned.</p>
            next_token: <p>If the response from the <code>ListBots</code> operation contains more results than specified in the <code>maxResults</code> parameter, a token is returned in the response. </p> <p>Use the returned token in the <code>nextToken</code> parameter of a <code>ListBots</code> request to return the next page of results. For a complete set of results, call the <code>ListBots</code> operation until the <code>nextToken</code> returned in the response is null.</p>

        Raises:
            capo_lex_models_v2.errors.internal_server_exception.InternalServerException: <p>The service encountered an unexpected condition. Try your request again.</p>
            capo_lex_models_v2.errors.service_quota_exceeded_exception.ServiceQuotaExceededException: <p>You have reached a quota for your bot. </p>
            capo_lex_models_v2.errors.throttling_exception.ThrottlingException: <p>Your request rate is too high. Reduce the frequency of requests.</p>
            capo_lex_models_v2.errors.validation_exception.ValidationException: <p>One of the input parameters in your request isn't valid. Check the parameters and try your request again.</p>
            capo_lex_models_v2.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        async def _handler(
            req: "AsyncOperationRequest[capo_lex_models_v2.types.list_bots_request.ListBotsRequest]",
        ) -> AsyncOperationResponse[
            "capo_lex_models_v2.types.list_bots_response.ListBotsResponse"
        ]:
            import capo_lex_models_v2._operations.lex_model_building_service_v2.list_bots

            (
                output,
                http_response,
            ) = await capo_lex_models_v2._operations.lex_model_building_service_v2.list_bots.async_list_bots(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_lex_models_v2.types.list_bots_request.ListBotsRequest = {}
        if sort_by is not None:
            input_["sort_by"] = sort_by
        if filters is not None:
            input_["filters"] = filters
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

    async def iter_list_bots(
        self,
        *,
        config_overrides: Optional[AsyncLexModelsV2ClientConfig] = None,
        sort_by: Optional["capo_lex_models_v2.types.bot_sort_by.BotSortBy"] = None,
        filters: Optional["capo_lex_models_v2.types.bot_filters.BotFilters"] = None,
        max_results: Optional["capo_lex_models_v2.types.max_results.MaxResults"] = None,
        next_token: Optional["capo_lex_models_v2.types.next_token.NextToken"] = None,
    ) -> "AsyncIterator[capo_lex_models_v2.types.list_bots_response.ListBotsResponse]":
        _token = next_token
        while True:
            _response = await self.list_bots(
                config_overrides=config_overrides,
                sort_by=sort_by,
                filters=filters,
                max_results=max_results,
                next_token=_token,
            )
            yield _response
            _token = _resolve_path(_response, ("next_token",))
            if not _token:
                break

    async def list_bot_version_replicas(
        self,
        bot_id: "capo_lex_models_v2.types.id.Id",
        replica_region: "capo_lex_models_v2.types.replica_region.ReplicaRegion",
        *,
        config_overrides: Optional[AsyncLexModelsV2ClientConfig] = None,
        max_results: Optional["capo_lex_models_v2.types.max_results.MaxResults"] = None,
        next_token: Optional["capo_lex_models_v2.types.next_token.NextToken"] = None,
        sort_by: Optional[
            "capo_lex_models_v2.types.bot_version_replica_sort_by.BotVersionReplicaSortBy"
        ] = None,
    ) -> "capo_lex_models_v2.types.list_bot_version_replicas_response.ListBotVersionReplicasResponse":
        """<p>Contains information about all the versions replication statuses applicable for Global Resiliency.</p>

        Args:
            bot_id: <p>The request for the unique ID in the list of replicated bots.</p>
            replica_region: <p>The request for the region used in the list of replicated bots.</p>
            max_results: <p>The maximum results given in the list of replicated bots.</p>
            next_token: <p>The next token given in the list of replicated bots.</p>
            sort_by: <p>The requested sort category for the list of replicated bots.</p>

        Raises:
            capo_lex_models_v2.errors.internal_server_exception.InternalServerException: <p>The service encountered an unexpected condition. Try your request again.</p>
            capo_lex_models_v2.errors.service_quota_exceeded_exception.ServiceQuotaExceededException: <p>You have reached a quota for your bot. </p>
            capo_lex_models_v2.errors.throttling_exception.ThrottlingException: <p>Your request rate is too high. Reduce the frequency of requests.</p>
            capo_lex_models_v2.errors.validation_exception.ValidationException: <p>One of the input parameters in your request isn't valid. Check the parameters and try your request again.</p>
            capo_lex_models_v2.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        async def _handler(
            req: "AsyncOperationRequest[capo_lex_models_v2.types.list_bot_version_replicas_request.ListBotVersionReplicasRequest]",
        ) -> AsyncOperationResponse[
            "capo_lex_models_v2.types.list_bot_version_replicas_response.ListBotVersionReplicasResponse"
        ]:
            import capo_lex_models_v2._operations.lex_model_building_service_v2.list_bot_version_replicas

            (
                output,
                http_response,
            ) = await capo_lex_models_v2._operations.lex_model_building_service_v2.list_bot_version_replicas.async_list_bot_version_replicas(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_lex_models_v2.types.list_bot_version_replicas_request.ListBotVersionReplicasRequest = {
            "bot_id": bot_id,
            "replica_region": replica_region,
        }
        if max_results is not None:
            input_["max_results"] = max_results
        if next_token is not None:
            input_["next_token"] = next_token
        if sort_by is not None:
            input_["sort_by"] = sort_by

        response = await aexecute_pipeline(
            AsyncOperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        await response.response.aclose()
        return response.output

    async def iter_list_bot_version_replicas(
        self,
        bot_id: "capo_lex_models_v2.types.id.Id",
        replica_region: "capo_lex_models_v2.types.replica_region.ReplicaRegion",
        *,
        config_overrides: Optional[AsyncLexModelsV2ClientConfig] = None,
        max_results: Optional["capo_lex_models_v2.types.max_results.MaxResults"] = None,
        next_token: Optional["capo_lex_models_v2.types.next_token.NextToken"] = None,
        sort_by: Optional[
            "capo_lex_models_v2.types.bot_version_replica_sort_by.BotVersionReplicaSortBy"
        ] = None,
    ) -> "AsyncIterator[capo_lex_models_v2.types.list_bot_version_replicas_response.ListBotVersionReplicasResponse]":
        _token = next_token
        while True:
            _response = await self.list_bot_version_replicas(
                bot_id,
                replica_region,
                config_overrides=config_overrides,
                max_results=max_results,
                next_token=_token,
                sort_by=sort_by,
            )
            yield _response
            _token = _resolve_path(_response, ("next_token",))
            if not _token:
                break

    async def list_bot_versions(
        self,
        bot_id: "capo_lex_models_v2.types.id.Id",
        *,
        config_overrides: Optional[AsyncLexModelsV2ClientConfig] = None,
        sort_by: Optional[
            "capo_lex_models_v2.types.bot_version_sort_by.BotVersionSortBy"
        ] = None,
        max_results: Optional["capo_lex_models_v2.types.max_results.MaxResults"] = None,
        next_token: Optional["capo_lex_models_v2.types.next_token.NextToken"] = None,
    ) -> "capo_lex_models_v2.types.list_bot_versions_response.ListBotVersionsResponse":
        """<p>Gets information about all of the versions of a bot.</p> <p>The <code>ListBotVersions</code> operation returns a summary of each version of a bot. For example, if a bot has three numbered versions, the <code>ListBotVersions</code> operation returns for summaries, one for each numbered version and one for the <code>DRAFT</code> version.</p> <p>The <code>ListBotVersions</code> operation always returns at least one version, the <code>DRAFT</code> version.</p>

        Args:
            bot_id: <p>The identifier of the bot to list versions for.</p>
            sort_by: <p>Specifies sorting parameters for the list of versions. You can specify that the list be sorted by version name in either ascending or descending order.</p>
            max_results: <p>The maximum number of versions to return in each page of results. If there are fewer results than the max page size, only the actual number of results are returned.</p>
            next_token: <p>If the response to the <code>ListBotVersion</code> operation contains more results than specified in the <code>maxResults</code> parameter, a token is returned in the response. Use that token in the <code>nextToken</code> parameter to return the next page of results.</p>

        Raises:
            capo_lex_models_v2.errors.internal_server_exception.InternalServerException: <p>The service encountered an unexpected condition. Try your request again.</p>
            capo_lex_models_v2.errors.service_quota_exceeded_exception.ServiceQuotaExceededException: <p>You have reached a quota for your bot. </p>
            capo_lex_models_v2.errors.throttling_exception.ThrottlingException: <p>Your request rate is too high. Reduce the frequency of requests.</p>
            capo_lex_models_v2.errors.validation_exception.ValidationException: <p>One of the input parameters in your request isn't valid. Check the parameters and try your request again.</p>
            capo_lex_models_v2.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        async def _handler(
            req: "AsyncOperationRequest[capo_lex_models_v2.types.list_bot_versions_request.ListBotVersionsRequest]",
        ) -> AsyncOperationResponse[
            "capo_lex_models_v2.types.list_bot_versions_response.ListBotVersionsResponse"
        ]:
            import capo_lex_models_v2._operations.lex_model_building_service_v2.list_bot_versions

            (
                output,
                http_response,
            ) = await capo_lex_models_v2._operations.lex_model_building_service_v2.list_bot_versions.async_list_bot_versions(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_lex_models_v2.types.list_bot_versions_request.ListBotVersionsRequest = {
            "bot_id": bot_id
        }
        if sort_by is not None:
            input_["sort_by"] = sort_by
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

    async def iter_list_bot_versions(
        self,
        bot_id: "capo_lex_models_v2.types.id.Id",
        *,
        config_overrides: Optional[AsyncLexModelsV2ClientConfig] = None,
        sort_by: Optional[
            "capo_lex_models_v2.types.bot_version_sort_by.BotVersionSortBy"
        ] = None,
        max_results: Optional["capo_lex_models_v2.types.max_results.MaxResults"] = None,
        next_token: Optional["capo_lex_models_v2.types.next_token.NextToken"] = None,
    ) -> "AsyncIterator[capo_lex_models_v2.types.list_bot_versions_response.ListBotVersionsResponse]":
        _token = next_token
        while True:
            _response = await self.list_bot_versions(
                bot_id,
                config_overrides=config_overrides,
                sort_by=sort_by,
                max_results=max_results,
                next_token=_token,
            )
            yield _response
            _token = _resolve_path(_response, ("next_token",))
            if not _token:
                break

    async def list_built_in_intents(
        self,
        locale_id: "capo_lex_models_v2.types.locale_id.LocaleId",
        *,
        config_overrides: Optional[AsyncLexModelsV2ClientConfig] = None,
        sort_by: Optional[
            "capo_lex_models_v2.types.built_in_intent_sort_by.BuiltInIntentSortBy"
        ] = None,
        max_results: Optional[
            "capo_lex_models_v2.types.built_ins_max_results.BuiltInsMaxResults"
        ] = None,
        next_token: Optional["capo_lex_models_v2.types.next_token.NextToken"] = None,
    ) -> "capo_lex_models_v2.types.list_built_in_intents_response.ListBuiltInIntentsResponse":
        """<p>Gets a list of built-in intents provided by Amazon Lex that you can use in your bot. </p> <p>To use a built-in intent as a the base for your own intent, include the built-in intent signature in the <code>parentIntentSignature</code> parameter when you call the <code>CreateIntent</code> operation. For more information, see <a href="https://docs.aws.amazon.com/lexv2/latest/APIReference/API_CreateIntent.html">CreateIntent</a>.</p>

        Args:
            locale_id: <p>The identifier of the language and locale of the intents to list. The string must match one of the supported locales. For more information, see <a href="https://docs.aws.amazon.com/lexv2/latest/dg/how-languages.html">Supported languages</a>.</p>
            sort_by: <p>Specifies sorting parameters for the list of built-in intents. You can specify that the list be sorted by the built-in intent signature in either ascending or descending order.</p>
            max_results: <p>The maximum number of built-in intents to return in each page of results. If there are fewer results than the max page size, only the actual number of results are returned.</p>
            next_token: <p>If the response from the <code>ListBuiltInIntents</code> operation contains more results than specified in the <code>maxResults</code> parameter, a token is returned in the response. Use that token in the <code>nextToken</code> parameter to return the next page of results.</p>

        Raises:
            capo_lex_models_v2.errors.internal_server_exception.InternalServerException: <p>The service encountered an unexpected condition. Try your request again.</p>
            capo_lex_models_v2.errors.service_quota_exceeded_exception.ServiceQuotaExceededException: <p>You have reached a quota for your bot. </p>
            capo_lex_models_v2.errors.throttling_exception.ThrottlingException: <p>Your request rate is too high. Reduce the frequency of requests.</p>
            capo_lex_models_v2.errors.validation_exception.ValidationException: <p>One of the input parameters in your request isn't valid. Check the parameters and try your request again.</p>
            capo_lex_models_v2.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        async def _handler(
            req: "AsyncOperationRequest[capo_lex_models_v2.types.list_built_in_intents_request.ListBuiltInIntentsRequest]",
        ) -> AsyncOperationResponse[
            "capo_lex_models_v2.types.list_built_in_intents_response.ListBuiltInIntentsResponse"
        ]:
            import capo_lex_models_v2._operations.lex_model_building_service_v2.list_built_in_intents

            (
                output,
                http_response,
            ) = await capo_lex_models_v2._operations.lex_model_building_service_v2.list_built_in_intents.async_list_built_in_intents(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_lex_models_v2.types.list_built_in_intents_request.ListBuiltInIntentsRequest = {
            "locale_id": locale_id
        }
        if sort_by is not None:
            input_["sort_by"] = sort_by
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

    async def iter_list_built_in_intents(
        self,
        locale_id: "capo_lex_models_v2.types.locale_id.LocaleId",
        *,
        config_overrides: Optional[AsyncLexModelsV2ClientConfig] = None,
        sort_by: Optional[
            "capo_lex_models_v2.types.built_in_intent_sort_by.BuiltInIntentSortBy"
        ] = None,
        max_results: Optional[
            "capo_lex_models_v2.types.built_ins_max_results.BuiltInsMaxResults"
        ] = None,
        next_token: Optional["capo_lex_models_v2.types.next_token.NextToken"] = None,
    ) -> "AsyncIterator[capo_lex_models_v2.types.list_built_in_intents_response.ListBuiltInIntentsResponse]":
        _token = next_token
        while True:
            _response = await self.list_built_in_intents(
                locale_id,
                config_overrides=config_overrides,
                sort_by=sort_by,
                max_results=max_results,
                next_token=_token,
            )
            yield _response
            _token = _resolve_path(_response, ("next_token",))
            if not _token:
                break

    async def list_built_in_slot_types(
        self,
        locale_id: "capo_lex_models_v2.types.locale_id.LocaleId",
        *,
        config_overrides: Optional[AsyncLexModelsV2ClientConfig] = None,
        sort_by: Optional[
            "capo_lex_models_v2.types.built_in_slot_type_sort_by.BuiltInSlotTypeSortBy"
        ] = None,
        max_results: Optional[
            "capo_lex_models_v2.types.built_ins_max_results.BuiltInsMaxResults"
        ] = None,
        next_token: Optional["capo_lex_models_v2.types.next_token.NextToken"] = None,
    ) -> "capo_lex_models_v2.types.list_built_in_slot_types_response.ListBuiltInSlotTypesResponse":
        """<p>Gets a list of built-in slot types that meet the specified criteria.</p>

        Args:
            locale_id: <p>The identifier of the language and locale of the slot types to list. The string must match one of the supported locales. For more information, see <a href="https://docs.aws.amazon.com/lexv2/latest/dg/how-languages.html">Supported languages</a>.</p>
            sort_by: <p>Determines the sort order for the response from the <code>ListBuiltInSlotTypes</code> operation. You can choose to sort by the slot type signature in either ascending or descending order.</p>
            max_results: <p>The maximum number of built-in slot types to return in each page of results. If there are fewer results than the max page size, only the actual number of results are returned.</p>
            next_token: <p>If the response from the <code>ListBuiltInSlotTypes</code> operation contains more results than specified in the <code>maxResults</code> parameter, a token is returned in the response. Use that token in the <code>nextToken</code> parameter to return the next page of results.</p>

        Raises:
            capo_lex_models_v2.errors.internal_server_exception.InternalServerException: <p>The service encountered an unexpected condition. Try your request again.</p>
            capo_lex_models_v2.errors.service_quota_exceeded_exception.ServiceQuotaExceededException: <p>You have reached a quota for your bot. </p>
            capo_lex_models_v2.errors.throttling_exception.ThrottlingException: <p>Your request rate is too high. Reduce the frequency of requests.</p>
            capo_lex_models_v2.errors.validation_exception.ValidationException: <p>One of the input parameters in your request isn't valid. Check the parameters and try your request again.</p>
            capo_lex_models_v2.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        async def _handler(
            req: "AsyncOperationRequest[capo_lex_models_v2.types.list_built_in_slot_types_request.ListBuiltInSlotTypesRequest]",
        ) -> AsyncOperationResponse[
            "capo_lex_models_v2.types.list_built_in_slot_types_response.ListBuiltInSlotTypesResponse"
        ]:
            import capo_lex_models_v2._operations.lex_model_building_service_v2.list_built_in_slot_types

            (
                output,
                http_response,
            ) = await capo_lex_models_v2._operations.lex_model_building_service_v2.list_built_in_slot_types.async_list_built_in_slot_types(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_lex_models_v2.types.list_built_in_slot_types_request.ListBuiltInSlotTypesRequest = {
            "locale_id": locale_id
        }
        if sort_by is not None:
            input_["sort_by"] = sort_by
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

    async def iter_list_built_in_slot_types(
        self,
        locale_id: "capo_lex_models_v2.types.locale_id.LocaleId",
        *,
        config_overrides: Optional[AsyncLexModelsV2ClientConfig] = None,
        sort_by: Optional[
            "capo_lex_models_v2.types.built_in_slot_type_sort_by.BuiltInSlotTypeSortBy"
        ] = None,
        max_results: Optional[
            "capo_lex_models_v2.types.built_ins_max_results.BuiltInsMaxResults"
        ] = None,
        next_token: Optional["capo_lex_models_v2.types.next_token.NextToken"] = None,
    ) -> "AsyncIterator[capo_lex_models_v2.types.list_built_in_slot_types_response.ListBuiltInSlotTypesResponse]":
        _token = next_token
        while True:
            _response = await self.list_built_in_slot_types(
                locale_id,
                config_overrides=config_overrides,
                sort_by=sort_by,
                max_results=max_results,
                next_token=_token,
            )
            yield _response
            _token = _resolve_path(_response, ("next_token",))
            if not _token:
                break

    async def list_custom_vocabulary_items(
        self,
        bot_id: "capo_lex_models_v2.types.id.Id",
        bot_version: "capo_lex_models_v2.types.bot_version.BotVersion",
        locale_id: "capo_lex_models_v2.types.locale_id.LocaleId",
        *,
        config_overrides: Optional[AsyncLexModelsV2ClientConfig] = None,
        max_results: Optional["capo_lex_models_v2.types.max_results.MaxResults"] = None,
        next_token: Optional["capo_lex_models_v2.types.next_token.NextToken"] = None,
    ) -> "capo_lex_models_v2.types.list_custom_vocabulary_items_response.ListCustomVocabularyItemsResponse":
        """<p>Paginated list of custom vocabulary items for a given bot locale's custom vocabulary.</p>

        Args:
            bot_id: <p>The identifier of the version of the bot associated with this custom vocabulary.</p>
            bot_version: <p>The bot version of the bot to the list custom vocabulary request.</p>
            locale_id: <p>The identifier of the language and locale where this custom vocabulary is used. The string must match one of the supported locales. For more information, see Supported languages (https://docs.aws.amazon.com/lexv2/latest/dg/how-languages.html).</p>
            max_results: <p>The maximum number of items returned by the list operation.</p>
            next_token: <p>The nextToken identifier to the list custom vocabulary request.</p>

        Raises:
            capo_lex_models_v2.errors.internal_server_exception.InternalServerException: <p>The service encountered an unexpected condition. Try your request again.</p>
            capo_lex_models_v2.errors.resource_not_found_exception.ResourceNotFoundException: <p>You asked to describe a resource that doesn't exist. Check the resource that you are requesting and try again.</p>
            capo_lex_models_v2.errors.service_quota_exceeded_exception.ServiceQuotaExceededException: <p>You have reached a quota for your bot. </p>
            capo_lex_models_v2.errors.throttling_exception.ThrottlingException: <p>Your request rate is too high. Reduce the frequency of requests.</p>
            capo_lex_models_v2.errors.validation_exception.ValidationException: <p>One of the input parameters in your request isn't valid. Check the parameters and try your request again.</p>
            capo_lex_models_v2.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        async def _handler(
            req: "AsyncOperationRequest[capo_lex_models_v2.types.list_custom_vocabulary_items_request.ListCustomVocabularyItemsRequest]",
        ) -> AsyncOperationResponse[
            "capo_lex_models_v2.types.list_custom_vocabulary_items_response.ListCustomVocabularyItemsResponse"
        ]:
            import capo_lex_models_v2._operations.lex_model_building_service_v2.list_custom_vocabulary_items

            (
                output,
                http_response,
            ) = await capo_lex_models_v2._operations.lex_model_building_service_v2.list_custom_vocabulary_items.async_list_custom_vocabulary_items(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_lex_models_v2.types.list_custom_vocabulary_items_request.ListCustomVocabularyItemsRequest = {
            "bot_id": bot_id,
            "bot_version": bot_version,
            "locale_id": locale_id,
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

    async def iter_list_custom_vocabulary_items(
        self,
        bot_id: "capo_lex_models_v2.types.id.Id",
        bot_version: "capo_lex_models_v2.types.bot_version.BotVersion",
        locale_id: "capo_lex_models_v2.types.locale_id.LocaleId",
        *,
        config_overrides: Optional[AsyncLexModelsV2ClientConfig] = None,
        max_results: Optional["capo_lex_models_v2.types.max_results.MaxResults"] = None,
        next_token: Optional["capo_lex_models_v2.types.next_token.NextToken"] = None,
    ) -> "AsyncIterator[capo_lex_models_v2.types.list_custom_vocabulary_items_response.ListCustomVocabularyItemsResponse]":
        _token = next_token
        while True:
            _response = await self.list_custom_vocabulary_items(
                bot_id,
                bot_version,
                locale_id,
                config_overrides=config_overrides,
                max_results=max_results,
                next_token=_token,
            )
            yield _response
            _token = _resolve_path(_response, ("next_token",))
            if not _token:
                break

    async def list_exports(
        self,
        *,
        config_overrides: Optional[AsyncLexModelsV2ClientConfig] = None,
        bot_id: Optional["capo_lex_models_v2.types.id.Id"] = None,
        bot_version: Optional["capo_lex_models_v2.types.bot_version.BotVersion"] = None,
        sort_by: Optional[
            "capo_lex_models_v2.types.export_sort_by.ExportSortBy"
        ] = None,
        filters: Optional[
            "capo_lex_models_v2.types.export_filters.ExportFilters"
        ] = None,
        max_results: Optional["capo_lex_models_v2.types.max_results.MaxResults"] = None,
        next_token: Optional["capo_lex_models_v2.types.next_token.NextToken"] = None,
        locale_id: Optional["capo_lex_models_v2.types.locale_id.LocaleId"] = None,
    ) -> "capo_lex_models_v2.types.list_exports_response.ListExportsResponse":
        """<p>Lists the exports for a bot, bot locale, or custom vocabulary. Exports are kept in the list for 7 days.</p>

        Args:
            bot_id: <p>The unique identifier that Amazon Lex assigned to the bot.</p>
            bot_version: <p>The version of the bot to list exports for. </p>
            sort_by: <p>Determines the field that the list of exports is sorted by. You can sort by the <code>LastUpdatedDateTime</code> field in ascending or descending order.</p>
            filters: <p>Provides the specification of a filter used to limit the exports in the response to only those that match the filter specification. You can only specify one filter and one string to filter on.</p>
            max_results: <p>The maximum number of exports to return in each page of results. If there are fewer results than the max page size, only the actual number of results are returned.</p>
            next_token: <p>If the response from the <code>ListExports</code> operation contains more results that specified in the <code>maxResults</code> parameter, a token is returned in the response. </p> <p>Use the returned token in the <code>nextToken</code> parameter of a <code>ListExports</code> request to return the next page of results. For a complete set of results, call the <code>ListExports</code> operation until the <code>nextToken</code> returned in the response is null.</p>
            locale_id: <p>Specifies the resources that should be exported. If you don't specify a resource type in the <code>filters</code> parameter, both bot locales and custom vocabularies are exported.</p>

        Raises:
            capo_lex_models_v2.errors.internal_server_exception.InternalServerException: <p>The service encountered an unexpected condition. Try your request again.</p>
            capo_lex_models_v2.errors.throttling_exception.ThrottlingException: <p>Your request rate is too high. Reduce the frequency of requests.</p>
            capo_lex_models_v2.errors.validation_exception.ValidationException: <p>One of the input parameters in your request isn't valid. Check the parameters and try your request again.</p>
            capo_lex_models_v2.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        async def _handler(
            req: "AsyncOperationRequest[capo_lex_models_v2.types.list_exports_request.ListExportsRequest]",
        ) -> AsyncOperationResponse[
            "capo_lex_models_v2.types.list_exports_response.ListExportsResponse"
        ]:
            import capo_lex_models_v2._operations.lex_model_building_service_v2.list_exports

            (
                output,
                http_response,
            ) = await capo_lex_models_v2._operations.lex_model_building_service_v2.list_exports.async_list_exports(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_lex_models_v2.types.list_exports_request.ListExportsRequest = {}
        if bot_id is not None:
            input_["bot_id"] = bot_id
        if bot_version is not None:
            input_["bot_version"] = bot_version
        if sort_by is not None:
            input_["sort_by"] = sort_by
        if filters is not None:
            input_["filters"] = filters
        if max_results is not None:
            input_["max_results"] = max_results
        if next_token is not None:
            input_["next_token"] = next_token
        if locale_id is not None:
            input_["locale_id"] = locale_id

        response = await aexecute_pipeline(
            AsyncOperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        await response.response.aclose()
        return response.output

    async def iter_list_exports(
        self,
        *,
        config_overrides: Optional[AsyncLexModelsV2ClientConfig] = None,
        bot_id: Optional["capo_lex_models_v2.types.id.Id"] = None,
        bot_version: Optional["capo_lex_models_v2.types.bot_version.BotVersion"] = None,
        sort_by: Optional[
            "capo_lex_models_v2.types.export_sort_by.ExportSortBy"
        ] = None,
        filters: Optional[
            "capo_lex_models_v2.types.export_filters.ExportFilters"
        ] = None,
        max_results: Optional["capo_lex_models_v2.types.max_results.MaxResults"] = None,
        next_token: Optional["capo_lex_models_v2.types.next_token.NextToken"] = None,
        locale_id: Optional["capo_lex_models_v2.types.locale_id.LocaleId"] = None,
    ) -> "AsyncIterator[capo_lex_models_v2.types.list_exports_response.ListExportsResponse]":
        _token = next_token
        while True:
            _response = await self.list_exports(
                config_overrides=config_overrides,
                bot_id=bot_id,
                bot_version=bot_version,
                sort_by=sort_by,
                filters=filters,
                max_results=max_results,
                next_token=_token,
                locale_id=locale_id,
            )
            yield _response
            _token = _resolve_path(_response, ("next_token",))
            if not _token:
                break

    async def list_imports(
        self,
        *,
        config_overrides: Optional[AsyncLexModelsV2ClientConfig] = None,
        bot_id: Optional["capo_lex_models_v2.types.id.Id"] = None,
        bot_version: Optional[
            "capo_lex_models_v2.types.draft_bot_version.DraftBotVersion"
        ] = None,
        sort_by: Optional[
            "capo_lex_models_v2.types.import_sort_by.ImportSortBy"
        ] = None,
        filters: Optional[
            "capo_lex_models_v2.types.import_filters.ImportFilters"
        ] = None,
        max_results: Optional["capo_lex_models_v2.types.max_results.MaxResults"] = None,
        next_token: Optional["capo_lex_models_v2.types.next_token.NextToken"] = None,
        locale_id: Optional["capo_lex_models_v2.types.locale_id.LocaleId"] = None,
    ) -> "capo_lex_models_v2.types.list_imports_response.ListImportsResponse":
        """<p>Lists the imports for a bot, bot locale, or custom vocabulary. Imports are kept in the list for 7 days.</p>

        Args:
            bot_id: <p>The unique identifier that Amazon Lex assigned to the bot.</p>
            bot_version: <p>The version of the bot to list imports for.</p>
            sort_by: <p>Determines the field that the list of imports is sorted by. You can sort by the <code>LastUpdatedDateTime</code> field in ascending or descending order.</p>
            filters: <p>Provides the specification of a filter used to limit the bots in the response to only those that match the filter specification. You can only specify one filter and one string to filter on.</p>
            max_results: <p>The maximum number of imports to return in each page of results. If there are fewer results than the max page size, only the actual number of results are returned.</p>
            next_token: <p>If the response from the <code>ListImports</code> operation contains more results than specified in the <code>maxResults</code> parameter, a token is returned in the response.</p> <p>Use the returned token in the <code>nextToken</code> parameter of a <code>ListImports</code> request to return the next page of results. For a complete set of results, call the <code>ListImports</code> operation until the <code>nextToken</code> returned in the response is null.</p>
            locale_id: <p>Specifies the locale that should be present in the list. If you don't specify a resource type in the <code>filters</code> parameter, the list contains both bot locales and custom vocabularies.</p>

        Raises:
            capo_lex_models_v2.errors.internal_server_exception.InternalServerException: <p>The service encountered an unexpected condition. Try your request again.</p>
            capo_lex_models_v2.errors.throttling_exception.ThrottlingException: <p>Your request rate is too high. Reduce the frequency of requests.</p>
            capo_lex_models_v2.errors.validation_exception.ValidationException: <p>One of the input parameters in your request isn't valid. Check the parameters and try your request again.</p>
            capo_lex_models_v2.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        async def _handler(
            req: "AsyncOperationRequest[capo_lex_models_v2.types.list_imports_request.ListImportsRequest]",
        ) -> AsyncOperationResponse[
            "capo_lex_models_v2.types.list_imports_response.ListImportsResponse"
        ]:
            import capo_lex_models_v2._operations.lex_model_building_service_v2.list_imports

            (
                output,
                http_response,
            ) = await capo_lex_models_v2._operations.lex_model_building_service_v2.list_imports.async_list_imports(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_lex_models_v2.types.list_imports_request.ListImportsRequest = {}
        if bot_id is not None:
            input_["bot_id"] = bot_id
        if bot_version is not None:
            input_["bot_version"] = bot_version
        if sort_by is not None:
            input_["sort_by"] = sort_by
        if filters is not None:
            input_["filters"] = filters
        if max_results is not None:
            input_["max_results"] = max_results
        if next_token is not None:
            input_["next_token"] = next_token
        if locale_id is not None:
            input_["locale_id"] = locale_id

        response = await aexecute_pipeline(
            AsyncOperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        await response.response.aclose()
        return response.output

    async def iter_list_imports(
        self,
        *,
        config_overrides: Optional[AsyncLexModelsV2ClientConfig] = None,
        bot_id: Optional["capo_lex_models_v2.types.id.Id"] = None,
        bot_version: Optional[
            "capo_lex_models_v2.types.draft_bot_version.DraftBotVersion"
        ] = None,
        sort_by: Optional[
            "capo_lex_models_v2.types.import_sort_by.ImportSortBy"
        ] = None,
        filters: Optional[
            "capo_lex_models_v2.types.import_filters.ImportFilters"
        ] = None,
        max_results: Optional["capo_lex_models_v2.types.max_results.MaxResults"] = None,
        next_token: Optional["capo_lex_models_v2.types.next_token.NextToken"] = None,
        locale_id: Optional["capo_lex_models_v2.types.locale_id.LocaleId"] = None,
    ) -> "AsyncIterator[capo_lex_models_v2.types.list_imports_response.ListImportsResponse]":
        _token = next_token
        while True:
            _response = await self.list_imports(
                config_overrides=config_overrides,
                bot_id=bot_id,
                bot_version=bot_version,
                sort_by=sort_by,
                filters=filters,
                max_results=max_results,
                next_token=_token,
                locale_id=locale_id,
            )
            yield _response
            _token = _resolve_path(_response, ("next_token",))
            if not _token:
                break

    async def list_intent_metrics(
        self,
        bot_id: "capo_lex_models_v2.types.id.Id",
        start_date_time: "capo_lex_models_v2.types.timestamp.Timestamp",
        end_date_time: "capo_lex_models_v2.types.timestamp.Timestamp",
        metrics: "capo_lex_models_v2.types.analytics_intent_metrics.AnalyticsIntentMetrics",
        *,
        config_overrides: Optional[AsyncLexModelsV2ClientConfig] = None,
        bin_by: Optional[
            "capo_lex_models_v2.types.analytics_bin_by_list.AnalyticsBinByList"
        ] = None,
        group_by: Optional[
            "capo_lex_models_v2.types.analytics_intent_group_by_list.AnalyticsIntentGroupByList"
        ] = None,
        filters: Optional[
            "capo_lex_models_v2.types.analytics_intent_filters.AnalyticsIntentFilters"
        ] = None,
        max_results: Optional["capo_lex_models_v2.types.max_results.MaxResults"] = None,
        next_token: Optional["capo_lex_models_v2.types.next_token.NextToken"] = None,
    ) -> "capo_lex_models_v2.types.list_intent_metrics_response.ListIntentMetricsResponse":
        """<p>Retrieves summary metrics for the intents in your bot. The following fields are required:</p> <ul> <li> <p> <code>metrics</code> – A list of <a href="https://docs.aws.amazon.com/lexv2/latest/APIReference/API_AnalyticsIntentMetric.html">AnalyticsIntentMetric</a> objects. In each object, use the <code>name</code> field to specify the metric to calculate, the <code>statistic</code> field to specify whether to calculate the <code>Sum</code>, <code>Average</code>, or <code>Max</code> number, and the <code>order</code> field to specify whether to sort the results in <code>Ascending</code> or <code>Descending</code> order.</p> </li> <li> <p> <code>startDateTime</code> and <code>endDateTime</code> – Define a time range for which you want to retrieve results.</p> </li> </ul> <p>Of the optional fields, you can organize the results in the following ways:</p> <ul> <li> <p>Use the <code>filters</code> field to filter the results, the <code>groupBy</code> field to specify categories by which to group the results, and the <code>binBy</code> field to specify time intervals by which to group the results.</p> </li> <li> <p>Use the <code>maxResults</code> field to limit the number of results to return in a single response and the <code>nextToken</code> field to return the next batch of results if the response does not return the full set of results.</p> </li> </ul> <p>Note that an <code>order</code> field exists in both <code>binBy</code> and <code>metrics</code>. You can specify only one <code>order</code> in a given request.</p>

        Args:
            bot_id: <p>The identifier for the bot for which you want to retrieve intent metrics.</p>
            start_date_time: <p>The timestamp that marks the beginning of the range of time for which you want to see intent metrics.</p>
            end_date_time: <p>The date and time that marks the end of the range of time for which you want to see intent metrics.</p>
            metrics: <p>A list of objects, each of which contains a metric you want to list, the statistic for the metric you want to return, and the order by which to organize the results.</p>
            bin_by: <p>A list of objects, each of which contains specifications for organizing the results by time.</p>
            group_by: <p>A list of objects, each of which specifies how to group the results. You can group by the following criteria:</p> <ul> <li> <p> <code>IntentName</code> – The name of the intent.</p> </li> <li> <p> <code>IntentEndState</code> – The final state of the intent. The possible end states are detailed in <a href="https://docs.aws.amazon.com/analytics-key-definitions-intents">Key definitions</a> in the user guide.</p> </li> </ul>
            filters: <p>A list of objects, each of which describes a condition by which you want to filter the results.</p>
            max_results: <p>The maximum number of results to return in each page of results. If there are fewer results than the maximum page size, only the actual number of results are returned.</p>
            next_token: <p>If the response from the ListIntentMetrics operation contains more results than specified in the maxResults parameter, a token is returned in the response.</p> <p>Use the returned token in the nextToken parameter of a ListIntentMetrics request to return the next page of results. For a complete set of results, call the ListIntentMetrics operation until the nextToken returned in the response is null.</p>

        Raises:
            capo_lex_models_v2.errors.internal_server_exception.InternalServerException: <p>The service encountered an unexpected condition. Try your request again.</p>
            capo_lex_models_v2.errors.precondition_failed_exception.PreconditionFailedException: <p>Your request couldn't be completed because one or more request fields aren't valid. Check the fields in your request and try again.</p>
            capo_lex_models_v2.errors.service_quota_exceeded_exception.ServiceQuotaExceededException: <p>You have reached a quota for your bot. </p>
            capo_lex_models_v2.errors.throttling_exception.ThrottlingException: <p>Your request rate is too high. Reduce the frequency of requests.</p>
            capo_lex_models_v2.errors.validation_exception.ValidationException: <p>One of the input parameters in your request isn't valid. Check the parameters and try your request again.</p>
            capo_lex_models_v2.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        async def _handler(
            req: "AsyncOperationRequest[capo_lex_models_v2.types.list_intent_metrics_request.ListIntentMetricsRequest]",
        ) -> AsyncOperationResponse[
            "capo_lex_models_v2.types.list_intent_metrics_response.ListIntentMetricsResponse"
        ]:
            import capo_lex_models_v2._operations.lex_model_building_service_v2.list_intent_metrics

            (
                output,
                http_response,
            ) = await capo_lex_models_v2._operations.lex_model_building_service_v2.list_intent_metrics.async_list_intent_metrics(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_lex_models_v2.types.list_intent_metrics_request.ListIntentMetricsRequest = {
            "bot_id": bot_id,
            "start_date_time": start_date_time,
            "end_date_time": end_date_time,
            "metrics": metrics,
        }
        if bin_by is not None:
            input_["bin_by"] = bin_by
        if group_by is not None:
            input_["group_by"] = group_by
        if filters is not None:
            input_["filters"] = filters
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

    async def iter_list_intent_metrics(
        self,
        bot_id: "capo_lex_models_v2.types.id.Id",
        start_date_time: "capo_lex_models_v2.types.timestamp.Timestamp",
        end_date_time: "capo_lex_models_v2.types.timestamp.Timestamp",
        metrics: "capo_lex_models_v2.types.analytics_intent_metrics.AnalyticsIntentMetrics",
        *,
        config_overrides: Optional[AsyncLexModelsV2ClientConfig] = None,
        bin_by: Optional[
            "capo_lex_models_v2.types.analytics_bin_by_list.AnalyticsBinByList"
        ] = None,
        group_by: Optional[
            "capo_lex_models_v2.types.analytics_intent_group_by_list.AnalyticsIntentGroupByList"
        ] = None,
        filters: Optional[
            "capo_lex_models_v2.types.analytics_intent_filters.AnalyticsIntentFilters"
        ] = None,
        max_results: Optional["capo_lex_models_v2.types.max_results.MaxResults"] = None,
        next_token: Optional["capo_lex_models_v2.types.next_token.NextToken"] = None,
    ) -> "AsyncIterator[capo_lex_models_v2.types.list_intent_metrics_response.ListIntentMetricsResponse]":
        _token = next_token
        while True:
            _response = await self.list_intent_metrics(
                bot_id,
                start_date_time,
                end_date_time,
                metrics,
                config_overrides=config_overrides,
                bin_by=bin_by,
                group_by=group_by,
                filters=filters,
                max_results=max_results,
                next_token=_token,
            )
            yield _response
            _token = _resolve_path(_response, ("next_token",))
            if not _token:
                break

    async def list_intent_paths(
        self,
        bot_id: "capo_lex_models_v2.types.id.Id",
        start_date_time: "capo_lex_models_v2.types.timestamp.Timestamp",
        end_date_time: "capo_lex_models_v2.types.timestamp.Timestamp",
        intent_path: "capo_lex_models_v2.types.analytics_path.AnalyticsPath",
        *,
        config_overrides: Optional[AsyncLexModelsV2ClientConfig] = None,
        filters: Optional[
            "capo_lex_models_v2.types.analytics_path_filters.AnalyticsPathFilters"
        ] = None,
    ) -> "capo_lex_models_v2.types.list_intent_paths_response.ListIntentPathsResponse":
        """<p>Retrieves summary statistics for a path of intents that users take over sessions with your bot. The following fields are required:</p> <ul> <li> <p> <code>startDateTime</code> and <code>endDateTime</code> – Define a time range for which you want to retrieve results.</p> </li> <li> <p> <code>intentPath</code> – Define an order of intents for which you want to retrieve metrics. Separate intents in the path with a forward slash. For example, populate the <code>intentPath</code> field with <code>/BookCar/BookHotel</code> to see details about how many times users invoked the <code>BookCar</code> and <code>BookHotel</code> intents in that order.</p> </li> </ul> <p>Use the optional <code>filters</code> field to filter the results.</p>

        Args:
            bot_id: <p>The identifier for the bot for which you want to retrieve intent path metrics.</p>
            start_date_time: <p>The date and time that marks the beginning of the range of time for which you want to see intent path metrics.</p>
            end_date_time: <p>The date and time that marks the end of the range of time for which you want to see intent path metrics.</p>
            intent_path: <p>The intent path for which you want to retrieve metrics. Use a forward slash to separate intents in the path. For example:</p> <ul> <li> <p>/BookCar</p> </li> <li> <p>/BookCar/BookHotel</p> </li> <li> <p>/BookHotel/BookCar</p> </li> </ul>
            filters: <p>A list of objects, each describes a condition by which you want to filter the results.</p>

        Raises:
            capo_lex_models_v2.errors.internal_server_exception.InternalServerException: <p>The service encountered an unexpected condition. Try your request again.</p>
            capo_lex_models_v2.errors.precondition_failed_exception.PreconditionFailedException: <p>Your request couldn't be completed because one or more request fields aren't valid. Check the fields in your request and try again.</p>
            capo_lex_models_v2.errors.service_quota_exceeded_exception.ServiceQuotaExceededException: <p>You have reached a quota for your bot. </p>
            capo_lex_models_v2.errors.throttling_exception.ThrottlingException: <p>Your request rate is too high. Reduce the frequency of requests.</p>
            capo_lex_models_v2.errors.validation_exception.ValidationException: <p>One of the input parameters in your request isn't valid. Check the parameters and try your request again.</p>
            capo_lex_models_v2.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        async def _handler(
            req: "AsyncOperationRequest[capo_lex_models_v2.types.list_intent_paths_request.ListIntentPathsRequest]",
        ) -> AsyncOperationResponse[
            "capo_lex_models_v2.types.list_intent_paths_response.ListIntentPathsResponse"
        ]:
            import capo_lex_models_v2._operations.lex_model_building_service_v2.list_intent_paths

            (
                output,
                http_response,
            ) = await capo_lex_models_v2._operations.lex_model_building_service_v2.list_intent_paths.async_list_intent_paths(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_lex_models_v2.types.list_intent_paths_request.ListIntentPathsRequest = {
            "bot_id": bot_id,
            "start_date_time": start_date_time,
            "end_date_time": end_date_time,
            "intent_path": intent_path,
        }
        if filters is not None:
            input_["filters"] = filters

        response = await aexecute_pipeline(
            AsyncOperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        await response.response.aclose()
        return response.output

    async def list_intents(
        self,
        bot_id: "capo_lex_models_v2.types.id.Id",
        bot_version: "capo_lex_models_v2.types.bot_version.BotVersion",
        locale_id: "capo_lex_models_v2.types.locale_id.LocaleId",
        *,
        config_overrides: Optional[AsyncLexModelsV2ClientConfig] = None,
        sort_by: Optional[
            "capo_lex_models_v2.types.intent_sort_by.IntentSortBy"
        ] = None,
        filters: Optional[
            "capo_lex_models_v2.types.intent_filters.IntentFilters"
        ] = None,
        max_results: Optional["capo_lex_models_v2.types.max_results.MaxResults"] = None,
        next_token: Optional["capo_lex_models_v2.types.next_token.NextToken"] = None,
    ) -> "capo_lex_models_v2.types.list_intents_response.ListIntentsResponse":
        """<p>Get a list of intents that meet the specified criteria.</p>

        Args:
            bot_id: <p>The unique identifier of the bot that contains the intent.</p>
            bot_version: <p>The version of the bot that contains the intent.</p>
            locale_id: <p>The identifier of the language and locale of the intents to list. The string must match one of the supported locales. For more information, see <a href="https://docs.aws.amazon.com/lexv2/latest/dg/how-languages.html">Supported languages</a>.</p>
            sort_by: <p>Determines the sort order for the response from the <code>ListIntents</code> operation. You can choose to sort by the intent name or last updated date in either ascending or descending order.</p>
            filters: <p>Provides the specification of a filter used to limit the intents in the response to only those that match the filter specification. You can only specify one filter and only one string to filter on.</p>
            max_results: <p>The maximum number of intents to return in each page of results. If there are fewer results than the max page size, only the actual number of results are returned.</p>
            next_token: <p>If the response from the <code>ListIntents</code> operation contains more results than specified in the <code>maxResults</code> parameter, a token is returned in the response.</p> <p>Use the returned token in the <code>nextToken</code> parameter of a <code>ListIntents</code> request to return the next page of results. For a complete set of results, call the <code>ListIntents</code> operation until the <code>nextToken</code> returned in the response is null.</p>

        Raises:
            capo_lex_models_v2.errors.internal_server_exception.InternalServerException: <p>The service encountered an unexpected condition. Try your request again.</p>
            capo_lex_models_v2.errors.service_quota_exceeded_exception.ServiceQuotaExceededException: <p>You have reached a quota for your bot. </p>
            capo_lex_models_v2.errors.throttling_exception.ThrottlingException: <p>Your request rate is too high. Reduce the frequency of requests.</p>
            capo_lex_models_v2.errors.validation_exception.ValidationException: <p>One of the input parameters in your request isn't valid. Check the parameters and try your request again.</p>
            capo_lex_models_v2.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        async def _handler(
            req: "AsyncOperationRequest[capo_lex_models_v2.types.list_intents_request.ListIntentsRequest]",
        ) -> AsyncOperationResponse[
            "capo_lex_models_v2.types.list_intents_response.ListIntentsResponse"
        ]:
            import capo_lex_models_v2._operations.lex_model_building_service_v2.list_intents

            (
                output,
                http_response,
            ) = await capo_lex_models_v2._operations.lex_model_building_service_v2.list_intents.async_list_intents(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_lex_models_v2.types.list_intents_request.ListIntentsRequest = {
            "bot_id": bot_id,
            "bot_version": bot_version,
            "locale_id": locale_id,
        }
        if sort_by is not None:
            input_["sort_by"] = sort_by
        if filters is not None:
            input_["filters"] = filters
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

    async def iter_list_intents(
        self,
        bot_id: "capo_lex_models_v2.types.id.Id",
        bot_version: "capo_lex_models_v2.types.bot_version.BotVersion",
        locale_id: "capo_lex_models_v2.types.locale_id.LocaleId",
        *,
        config_overrides: Optional[AsyncLexModelsV2ClientConfig] = None,
        sort_by: Optional[
            "capo_lex_models_v2.types.intent_sort_by.IntentSortBy"
        ] = None,
        filters: Optional[
            "capo_lex_models_v2.types.intent_filters.IntentFilters"
        ] = None,
        max_results: Optional["capo_lex_models_v2.types.max_results.MaxResults"] = None,
        next_token: Optional["capo_lex_models_v2.types.next_token.NextToken"] = None,
    ) -> "AsyncIterator[capo_lex_models_v2.types.list_intents_response.ListIntentsResponse]":
        _token = next_token
        while True:
            _response = await self.list_intents(
                bot_id,
                bot_version,
                locale_id,
                config_overrides=config_overrides,
                sort_by=sort_by,
                filters=filters,
                max_results=max_results,
                next_token=_token,
            )
            yield _response
            _token = _resolve_path(_response, ("next_token",))
            if not _token:
                break

    async def list_intent_stage_metrics(
        self,
        bot_id: "capo_lex_models_v2.types.id.Id",
        start_date_time: "capo_lex_models_v2.types.timestamp.Timestamp",
        end_date_time: "capo_lex_models_v2.types.timestamp.Timestamp",
        metrics: "capo_lex_models_v2.types.analytics_intent_stage_metrics.AnalyticsIntentStageMetrics",
        *,
        config_overrides: Optional[AsyncLexModelsV2ClientConfig] = None,
        bin_by: Optional[
            "capo_lex_models_v2.types.analytics_bin_by_list.AnalyticsBinByList"
        ] = None,
        group_by: Optional[
            "capo_lex_models_v2.types.analytics_intent_stage_group_by_list.AnalyticsIntentStageGroupByList"
        ] = None,
        filters: Optional[
            "capo_lex_models_v2.types.analytics_intent_stage_filters.AnalyticsIntentStageFilters"
        ] = None,
        max_results: Optional["capo_lex_models_v2.types.max_results.MaxResults"] = None,
        next_token: Optional["capo_lex_models_v2.types.next_token.NextToken"] = None,
    ) -> "capo_lex_models_v2.types.list_intent_stage_metrics_response.ListIntentStageMetricsResponse":
        """<p>Retrieves summary metrics for the stages within intents in your bot. The following fields are required:</p> <ul> <li> <p> <code>metrics</code> – A list of <a href="https://docs.aws.amazon.com/lexv2/latest/APIReference/API_AnalyticsIntentStageMetric.html">AnalyticsIntentStageMetric</a> objects. In each object, use the <code>name</code> field to specify the metric to calculate, the <code>statistic</code> field to specify whether to calculate the <code>Sum</code>, <code>Average</code>, or <code>Max</code> number, and the <code>order</code> field to specify whether to sort the results in <code>Ascending</code> or <code>Descending</code> order.</p> </li> <li> <p> <code>startDateTime</code> and <code>endDateTime</code> – Define a time range for which you want to retrieve results.</p> </li> </ul> <p>Of the optional fields, you can organize the results in the following ways:</p> <ul> <li> <p>Use the <code>filters</code> field to filter the results, the <code>groupBy</code> field to specify categories by which to group the results, and the <code>binBy</code> field to specify time intervals by which to group the results.</p> </li> <li> <p>Use the <code>maxResults</code> field to limit the number of results to return in a single response and the <code>nextToken</code> field to return the next batch of results if the response does not return the full set of results.</p> </li> </ul> <p>Note that an <code>order</code> field exists in both <code>binBy</code> and <code>metrics</code>. You can only specify one <code>order</code> in a given request.</p>

        Args:
            bot_id: <p>The identifier for the bot for which you want to retrieve intent stage metrics.</p>
            start_date_time: <p>The date and time that marks the beginning of the range of time for which you want to see intent stage metrics.</p>
            end_date_time: <p>The date and time that marks the end of the range of time for which you want to see intent stage metrics.</p>
            metrics: <p>A list of objects, each of which contains a metric you want to list, the statistic for the metric you want to return, and the method by which to organize the results.</p>
            bin_by: <p>A list of objects, each of which contains specifications for organizing the results by time.</p>
            group_by: <p>A list of objects, each of which specifies how to group the results. You can group by the following criteria:</p> <ul> <li> <p> <code>IntentStageName</code> – The name of the intent stage.</p> </li> <li> <p> <code>SwitchedToIntent</code> – The intent to which the conversation was switched (if any).</p> </li> </ul>
            filters: <p>A list of objects, each of which describes a condition by which you want to filter the results.</p>
            max_results: <p>The maximum number of results to return in each page of results. If there are fewer results than the maximum page size, only the actual number of results are returned.</p>
            next_token: <p>If the response from the ListIntentStageMetrics operation contains more results than specified in the maxResults parameter, a token is returned in the response.</p> <p>Use the returned token in the nextToken parameter of a ListIntentStageMetrics request to return the next page of results. For a complete set of results, call the ListIntentStageMetrics operation until the nextToken returned in the response is null.</p>

        Raises:
            capo_lex_models_v2.errors.internal_server_exception.InternalServerException: <p>The service encountered an unexpected condition. Try your request again.</p>
            capo_lex_models_v2.errors.precondition_failed_exception.PreconditionFailedException: <p>Your request couldn't be completed because one or more request fields aren't valid. Check the fields in your request and try again.</p>
            capo_lex_models_v2.errors.service_quota_exceeded_exception.ServiceQuotaExceededException: <p>You have reached a quota for your bot. </p>
            capo_lex_models_v2.errors.throttling_exception.ThrottlingException: <p>Your request rate is too high. Reduce the frequency of requests.</p>
            capo_lex_models_v2.errors.validation_exception.ValidationException: <p>One of the input parameters in your request isn't valid. Check the parameters and try your request again.</p>
            capo_lex_models_v2.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        async def _handler(
            req: "AsyncOperationRequest[capo_lex_models_v2.types.list_intent_stage_metrics_request.ListIntentStageMetricsRequest]",
        ) -> AsyncOperationResponse[
            "capo_lex_models_v2.types.list_intent_stage_metrics_response.ListIntentStageMetricsResponse"
        ]:
            import capo_lex_models_v2._operations.lex_model_building_service_v2.list_intent_stage_metrics

            (
                output,
                http_response,
            ) = await capo_lex_models_v2._operations.lex_model_building_service_v2.list_intent_stage_metrics.async_list_intent_stage_metrics(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_lex_models_v2.types.list_intent_stage_metrics_request.ListIntentStageMetricsRequest = {
            "bot_id": bot_id,
            "start_date_time": start_date_time,
            "end_date_time": end_date_time,
            "metrics": metrics,
        }
        if bin_by is not None:
            input_["bin_by"] = bin_by
        if group_by is not None:
            input_["group_by"] = group_by
        if filters is not None:
            input_["filters"] = filters
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

    async def iter_list_intent_stage_metrics(
        self,
        bot_id: "capo_lex_models_v2.types.id.Id",
        start_date_time: "capo_lex_models_v2.types.timestamp.Timestamp",
        end_date_time: "capo_lex_models_v2.types.timestamp.Timestamp",
        metrics: "capo_lex_models_v2.types.analytics_intent_stage_metrics.AnalyticsIntentStageMetrics",
        *,
        config_overrides: Optional[AsyncLexModelsV2ClientConfig] = None,
        bin_by: Optional[
            "capo_lex_models_v2.types.analytics_bin_by_list.AnalyticsBinByList"
        ] = None,
        group_by: Optional[
            "capo_lex_models_v2.types.analytics_intent_stage_group_by_list.AnalyticsIntentStageGroupByList"
        ] = None,
        filters: Optional[
            "capo_lex_models_v2.types.analytics_intent_stage_filters.AnalyticsIntentStageFilters"
        ] = None,
        max_results: Optional["capo_lex_models_v2.types.max_results.MaxResults"] = None,
        next_token: Optional["capo_lex_models_v2.types.next_token.NextToken"] = None,
    ) -> "AsyncIterator[capo_lex_models_v2.types.list_intent_stage_metrics_response.ListIntentStageMetricsResponse]":
        _token = next_token
        while True:
            _response = await self.list_intent_stage_metrics(
                bot_id,
                start_date_time,
                end_date_time,
                metrics,
                config_overrides=config_overrides,
                bin_by=bin_by,
                group_by=group_by,
                filters=filters,
                max_results=max_results,
                next_token=_token,
            )
            yield _response
            _token = _resolve_path(_response, ("next_token",))
            if not _token:
                break

    async def list_recommended_intents(
        self,
        bot_id: "capo_lex_models_v2.types.id.Id",
        bot_version: "capo_lex_models_v2.types.draft_bot_version.DraftBotVersion",
        locale_id: "capo_lex_models_v2.types.locale_id.LocaleId",
        bot_recommendation_id: "capo_lex_models_v2.types.id.Id",
        *,
        config_overrides: Optional[AsyncLexModelsV2ClientConfig] = None,
        next_token: Optional["capo_lex_models_v2.types.next_token.NextToken"] = None,
        max_results: Optional["capo_lex_models_v2.types.max_results.MaxResults"] = None,
    ) -> "capo_lex_models_v2.types.list_recommended_intents_response.ListRecommendedIntentsResponse":
        """<p>Gets a list of recommended intents provided by the bot recommendation that you can use in your bot. Intents in the response are ordered by relevance.</p>

        Args:
            bot_id: <p>The unique identifier of the bot associated with the recommended intents.</p>
            bot_version: <p>The version of the bot that contains the recommended intents.</p>
            locale_id: <p>The identifier of the language and locale of the recommended intents.</p>
            bot_recommendation_id: <p>The identifier of the bot recommendation that contains the recommended intents.</p>
            next_token: <p>If the response from the ListRecommendedIntents operation contains more results than specified in the maxResults parameter, a token is returned in the response. Use that token in the nextToken parameter to return the next page of results.</p>
            max_results: <p>The maximum number of bot recommendations to return in each page of results. If there are fewer results than the max page size, only the actual number of results are returned.</p>

        Raises:
            capo_lex_models_v2.errors.internal_server_exception.InternalServerException: <p>The service encountered an unexpected condition. Try your request again.</p>
            capo_lex_models_v2.errors.resource_not_found_exception.ResourceNotFoundException: <p>You asked to describe a resource that doesn't exist. Check the resource that you are requesting and try again.</p>
            capo_lex_models_v2.errors.service_quota_exceeded_exception.ServiceQuotaExceededException: <p>You have reached a quota for your bot. </p>
            capo_lex_models_v2.errors.throttling_exception.ThrottlingException: <p>Your request rate is too high. Reduce the frequency of requests.</p>
            capo_lex_models_v2.errors.validation_exception.ValidationException: <p>One of the input parameters in your request isn't valid. Check the parameters and try your request again.</p>
            capo_lex_models_v2.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        async def _handler(
            req: "AsyncOperationRequest[capo_lex_models_v2.types.list_recommended_intents_request.ListRecommendedIntentsRequest]",
        ) -> AsyncOperationResponse[
            "capo_lex_models_v2.types.list_recommended_intents_response.ListRecommendedIntentsResponse"
        ]:
            import capo_lex_models_v2._operations.lex_model_building_service_v2.list_recommended_intents

            (
                output,
                http_response,
            ) = await capo_lex_models_v2._operations.lex_model_building_service_v2.list_recommended_intents.async_list_recommended_intents(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_lex_models_v2.types.list_recommended_intents_request.ListRecommendedIntentsRequest = {
            "bot_id": bot_id,
            "bot_version": bot_version,
            "locale_id": locale_id,
            "bot_recommendation_id": bot_recommendation_id,
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

    async def iter_list_recommended_intents(
        self,
        bot_id: "capo_lex_models_v2.types.id.Id",
        bot_version: "capo_lex_models_v2.types.draft_bot_version.DraftBotVersion",
        locale_id: "capo_lex_models_v2.types.locale_id.LocaleId",
        bot_recommendation_id: "capo_lex_models_v2.types.id.Id",
        *,
        config_overrides: Optional[AsyncLexModelsV2ClientConfig] = None,
        next_token: Optional["capo_lex_models_v2.types.next_token.NextToken"] = None,
        max_results: Optional["capo_lex_models_v2.types.max_results.MaxResults"] = None,
    ) -> "AsyncIterator[capo_lex_models_v2.types.list_recommended_intents_response.ListRecommendedIntentsResponse]":
        _token = next_token
        while True:
            _response = await self.list_recommended_intents(
                bot_id,
                bot_version,
                locale_id,
                bot_recommendation_id,
                config_overrides=config_overrides,
                next_token=_token,
                max_results=max_results,
            )
            yield _response
            _token = _resolve_path(_response, ("next_token",))
            if not _token:
                break

    async def list_session_analytics_data(
        self,
        bot_id: "capo_lex_models_v2.types.id.Id",
        start_date_time: "capo_lex_models_v2.types.timestamp.Timestamp",
        end_date_time: "capo_lex_models_v2.types.timestamp.Timestamp",
        *,
        config_overrides: Optional[AsyncLexModelsV2ClientConfig] = None,
        sort_by: Optional[
            "capo_lex_models_v2.types.session_data_sort_by.SessionDataSortBy"
        ] = None,
        filters: Optional[
            "capo_lex_models_v2.types.analytics_session_filters.AnalyticsSessionFilters"
        ] = None,
        max_results: Optional["capo_lex_models_v2.types.max_results.MaxResults"] = None,
        next_token: Optional["capo_lex_models_v2.types.next_token.NextToken"] = None,
    ) -> "capo_lex_models_v2.types.list_session_analytics_data_response.ListSessionAnalyticsDataResponse":
        """<p>Retrieves a list of metadata for individual user sessions with your bot. The <code>startDateTime</code> and <code>endDateTime</code> fields are required. These fields define a time range for which you want to retrieve results. Of the optional fields, you can organize the results in the following ways:</p> <ul> <li> <p>Use the <code>filters</code> field to filter the results and the <code>sortBy</code> field to specify the values by which to sort the results.</p> </li> <li> <p>Use the <code>maxResults</code> field to limit the number of results to return in a single response and the <code>nextToken</code> field to return the next batch of results if the response does not return the full set of results.</p> </li> </ul>

        Args:
            bot_id: <p>The identifier for the bot for which you want to retrieve session analytics.</p>
            start_date_time: <p>The date and time that marks the beginning of the range of time for which you want to see session analytics.</p>
            end_date_time: <p>The date and time that marks the end of the range of time for which you want to see session analytics.</p>
            sort_by: <p>An object specifying the measure and method by which to sort the session analytics data.</p>
            filters: <p>A list of objects, each of which describes a condition by which you want to filter the results.</p>
            max_results: <p>The maximum number of results to return in each page of results. If there are fewer results than the maximum page size, only the actual number of results are returned.</p>
            next_token: <p>If the response from the ListSessionAnalyticsData operation contains more results than specified in the maxResults parameter, a token is returned in the response.</p> <p>Use the returned token in the nextToken parameter of a ListSessionAnalyticsData request to return the next page of results. For a complete set of results, call the ListSessionAnalyticsData operation until the nextToken returned in the response is null.</p>

        Raises:
            capo_lex_models_v2.errors.internal_server_exception.InternalServerException: <p>The service encountered an unexpected condition. Try your request again.</p>
            capo_lex_models_v2.errors.precondition_failed_exception.PreconditionFailedException: <p>Your request couldn't be completed because one or more request fields aren't valid. Check the fields in your request and try again.</p>
            capo_lex_models_v2.errors.service_quota_exceeded_exception.ServiceQuotaExceededException: <p>You have reached a quota for your bot. </p>
            capo_lex_models_v2.errors.throttling_exception.ThrottlingException: <p>Your request rate is too high. Reduce the frequency of requests.</p>
            capo_lex_models_v2.errors.validation_exception.ValidationException: <p>One of the input parameters in your request isn't valid. Check the parameters and try your request again.</p>
            capo_lex_models_v2.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        async def _handler(
            req: "AsyncOperationRequest[capo_lex_models_v2.types.list_session_analytics_data_request.ListSessionAnalyticsDataRequest]",
        ) -> AsyncOperationResponse[
            "capo_lex_models_v2.types.list_session_analytics_data_response.ListSessionAnalyticsDataResponse"
        ]:
            import capo_lex_models_v2._operations.lex_model_building_service_v2.list_session_analytics_data

            (
                output,
                http_response,
            ) = await capo_lex_models_v2._operations.lex_model_building_service_v2.list_session_analytics_data.async_list_session_analytics_data(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_lex_models_v2.types.list_session_analytics_data_request.ListSessionAnalyticsDataRequest = {
            "bot_id": bot_id,
            "start_date_time": start_date_time,
            "end_date_time": end_date_time,
        }
        if sort_by is not None:
            input_["sort_by"] = sort_by
        if filters is not None:
            input_["filters"] = filters
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

    async def iter_list_session_analytics_data(
        self,
        bot_id: "capo_lex_models_v2.types.id.Id",
        start_date_time: "capo_lex_models_v2.types.timestamp.Timestamp",
        end_date_time: "capo_lex_models_v2.types.timestamp.Timestamp",
        *,
        config_overrides: Optional[AsyncLexModelsV2ClientConfig] = None,
        sort_by: Optional[
            "capo_lex_models_v2.types.session_data_sort_by.SessionDataSortBy"
        ] = None,
        filters: Optional[
            "capo_lex_models_v2.types.analytics_session_filters.AnalyticsSessionFilters"
        ] = None,
        max_results: Optional["capo_lex_models_v2.types.max_results.MaxResults"] = None,
        next_token: Optional["capo_lex_models_v2.types.next_token.NextToken"] = None,
    ) -> "AsyncIterator[capo_lex_models_v2.types.list_session_analytics_data_response.ListSessionAnalyticsDataResponse]":
        _token = next_token
        while True:
            _response = await self.list_session_analytics_data(
                bot_id,
                start_date_time,
                end_date_time,
                config_overrides=config_overrides,
                sort_by=sort_by,
                filters=filters,
                max_results=max_results,
                next_token=_token,
            )
            yield _response
            _token = _resolve_path(_response, ("next_token",))
            if not _token:
                break

    async def list_session_metrics(
        self,
        bot_id: "capo_lex_models_v2.types.id.Id",
        start_date_time: "capo_lex_models_v2.types.timestamp.Timestamp",
        end_date_time: "capo_lex_models_v2.types.timestamp.Timestamp",
        metrics: "capo_lex_models_v2.types.analytics_session_metrics.AnalyticsSessionMetrics",
        *,
        config_overrides: Optional[AsyncLexModelsV2ClientConfig] = None,
        bin_by: Optional[
            "capo_lex_models_v2.types.analytics_bin_by_list.AnalyticsBinByList"
        ] = None,
        group_by: Optional[
            "capo_lex_models_v2.types.analytics_session_group_by_list.AnalyticsSessionGroupByList"
        ] = None,
        filters: Optional[
            "capo_lex_models_v2.types.analytics_session_filters.AnalyticsSessionFilters"
        ] = None,
        max_results: Optional["capo_lex_models_v2.types.max_results.MaxResults"] = None,
        next_token: Optional["capo_lex_models_v2.types.next_token.NextToken"] = None,
    ) -> "capo_lex_models_v2.types.list_session_metrics_response.ListSessionMetricsResponse":
        """<p>Retrieves summary metrics for the user sessions with your bot. The following fields are required:</p> <ul> <li> <p> <code>metrics</code> – A list of <a href="https://docs.aws.amazon.com/lexv2/latest/APIReference/API_AnalyticsSessionMetric.html">AnalyticsSessionMetric</a> objects. In each object, use the <code>name</code> field to specify the metric to calculate, the <code>statistic</code> field to specify whether to calculate the <code>Sum</code>, <code>Average</code>, or <code>Max</code> number, and the <code>order</code> field to specify whether to sort the results in <code>Ascending</code> or <code>Descending</code> order.</p> </li> <li> <p> <code>startDateTime</code> and <code>endDateTime</code> – Define a time range for which you want to retrieve results.</p> </li> </ul> <p>Of the optional fields, you can organize the results in the following ways:</p> <ul> <li> <p>Use the <code>filters</code> field to filter the results, the <code>groupBy</code> field to specify categories by which to group the results, and the <code>binBy</code> field to specify time intervals by which to group the results.</p> </li> <li> <p>Use the <code>maxResults</code> field to limit the number of results to return in a single response and the <code>nextToken</code> field to return the next batch of results if the response does not return the full set of results.</p> </li> </ul> <p>Note that an <code>order</code> field exists in both <code>binBy</code> and <code>metrics</code>. Currently, you can specify it in either field, but not in both.</p>

        Args:
            bot_id: <p>The identifier for the bot for which you want to retrieve session metrics.</p>
            start_date_time: <p>The date and time that marks the beginning of the range of time for which you want to see session metrics.</p>
            end_date_time: <p>The date and time that marks the end of the range of time for which you want to see session metrics.</p>
            metrics: <p>A list of objects, each of which contains a metric you want to list, the statistic for the metric you want to return, and the method by which to organize the results.</p>
            bin_by: <p>A list of objects, each of which contains specifications for organizing the results by time.</p>
            group_by: <p>A list of objects, each of which specifies how to group the results. You can group by the following criteria:</p> <ul> <li> <p> <code>ConversationEndState</code> – The final state of the conversation. The possible end states are detailed in <a href="https://docs.aws.amazon.com/analytics-key-definitions-conversations">Key definitions</a> in the user guide.</p> </li> <li> <p> <code>LocaleId</code> – The unique identifier of the bot locale.</p> </li> </ul>
            filters: <p>A list of objects, each of which describes a condition by which you want to filter the results.</p>
            max_results: <p>The maximum number of results to return in each page of results. If there are fewer results than the maximum page size, only the actual number of results are returned.</p>
            next_token: <p>If the response from the ListSessionMetrics operation contains more results than specified in the maxResults parameter, a token is returned in the response.</p> <p>Use the returned token in the nextToken parameter of a ListSessionMetrics request to return the next page of results. For a complete set of results, call the ListSessionMetrics operation until the nextToken returned in the response is null.</p>

        Raises:
            capo_lex_models_v2.errors.internal_server_exception.InternalServerException: <p>The service encountered an unexpected condition. Try your request again.</p>
            capo_lex_models_v2.errors.precondition_failed_exception.PreconditionFailedException: <p>Your request couldn't be completed because one or more request fields aren't valid. Check the fields in your request and try again.</p>
            capo_lex_models_v2.errors.service_quota_exceeded_exception.ServiceQuotaExceededException: <p>You have reached a quota for your bot. </p>
            capo_lex_models_v2.errors.throttling_exception.ThrottlingException: <p>Your request rate is too high. Reduce the frequency of requests.</p>
            capo_lex_models_v2.errors.validation_exception.ValidationException: <p>One of the input parameters in your request isn't valid. Check the parameters and try your request again.</p>
            capo_lex_models_v2.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        async def _handler(
            req: "AsyncOperationRequest[capo_lex_models_v2.types.list_session_metrics_request.ListSessionMetricsRequest]",
        ) -> AsyncOperationResponse[
            "capo_lex_models_v2.types.list_session_metrics_response.ListSessionMetricsResponse"
        ]:
            import capo_lex_models_v2._operations.lex_model_building_service_v2.list_session_metrics

            (
                output,
                http_response,
            ) = await capo_lex_models_v2._operations.lex_model_building_service_v2.list_session_metrics.async_list_session_metrics(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_lex_models_v2.types.list_session_metrics_request.ListSessionMetricsRequest = {
            "bot_id": bot_id,
            "start_date_time": start_date_time,
            "end_date_time": end_date_time,
            "metrics": metrics,
        }
        if bin_by is not None:
            input_["bin_by"] = bin_by
        if group_by is not None:
            input_["group_by"] = group_by
        if filters is not None:
            input_["filters"] = filters
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

    async def iter_list_session_metrics(
        self,
        bot_id: "capo_lex_models_v2.types.id.Id",
        start_date_time: "capo_lex_models_v2.types.timestamp.Timestamp",
        end_date_time: "capo_lex_models_v2.types.timestamp.Timestamp",
        metrics: "capo_lex_models_v2.types.analytics_session_metrics.AnalyticsSessionMetrics",
        *,
        config_overrides: Optional[AsyncLexModelsV2ClientConfig] = None,
        bin_by: Optional[
            "capo_lex_models_v2.types.analytics_bin_by_list.AnalyticsBinByList"
        ] = None,
        group_by: Optional[
            "capo_lex_models_v2.types.analytics_session_group_by_list.AnalyticsSessionGroupByList"
        ] = None,
        filters: Optional[
            "capo_lex_models_v2.types.analytics_session_filters.AnalyticsSessionFilters"
        ] = None,
        max_results: Optional["capo_lex_models_v2.types.max_results.MaxResults"] = None,
        next_token: Optional["capo_lex_models_v2.types.next_token.NextToken"] = None,
    ) -> "AsyncIterator[capo_lex_models_v2.types.list_session_metrics_response.ListSessionMetricsResponse]":
        _token = next_token
        while True:
            _response = await self.list_session_metrics(
                bot_id,
                start_date_time,
                end_date_time,
                metrics,
                config_overrides=config_overrides,
                bin_by=bin_by,
                group_by=group_by,
                filters=filters,
                max_results=max_results,
                next_token=_token,
            )
            yield _response
            _token = _resolve_path(_response, ("next_token",))
            if not _token:
                break

    async def list_slots(
        self,
        bot_id: "capo_lex_models_v2.types.id.Id",
        bot_version: "capo_lex_models_v2.types.bot_version.BotVersion",
        locale_id: "capo_lex_models_v2.types.locale_id.LocaleId",
        intent_id: "capo_lex_models_v2.types.id.Id",
        *,
        config_overrides: Optional[AsyncLexModelsV2ClientConfig] = None,
        sort_by: Optional["capo_lex_models_v2.types.slot_sort_by.SlotSortBy"] = None,
        filters: Optional["capo_lex_models_v2.types.slot_filters.SlotFilters"] = None,
        max_results: Optional["capo_lex_models_v2.types.max_results.MaxResults"] = None,
        next_token: Optional["capo_lex_models_v2.types.next_token.NextToken"] = None,
    ) -> "capo_lex_models_v2.types.list_slots_response.ListSlotsResponse":
        """<p>Gets a list of slots that match the specified criteria.</p>

        Args:
            bot_id: <p>The identifier of the bot that contains the slot.</p>
            bot_version: <p>The version of the bot that contains the slot.</p>
            locale_id: <p>The identifier of the language and locale of the slots to list. The string must match one of the supported locales. For more information, see <a href="https://docs.aws.amazon.com/lexv2/latest/dg/how-languages.html">Supported languages</a>.</p>
            intent_id: <p>The unique identifier of the intent that contains the slot.</p>
            sort_by: <p>Determines the sort order for the response from the <code>ListSlots</code> operation. You can choose to sort by the slot name or last updated date in either ascending or descending order.</p>
            filters: <p>Provides the specification of a filter used to limit the slots in the response to only those that match the filter specification. You can only specify one filter and only one string to filter on.</p>
            max_results: <p>The maximum number of slots to return in each page of results. If there are fewer results than the max page size, only the actual number of results are returned.</p>
            next_token: <p>If the response from the <code>ListSlots</code> operation contains more results than specified in the <code>maxResults</code> parameter, a token is returned in the response. Use that token in the <code>nextToken</code> parameter to return the next page of results.</p>

        Raises:
            capo_lex_models_v2.errors.internal_server_exception.InternalServerException: <p>The service encountered an unexpected condition. Try your request again.</p>
            capo_lex_models_v2.errors.service_quota_exceeded_exception.ServiceQuotaExceededException: <p>You have reached a quota for your bot. </p>
            capo_lex_models_v2.errors.throttling_exception.ThrottlingException: <p>Your request rate is too high. Reduce the frequency of requests.</p>
            capo_lex_models_v2.errors.validation_exception.ValidationException: <p>One of the input parameters in your request isn't valid. Check the parameters and try your request again.</p>
            capo_lex_models_v2.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        async def _handler(
            req: "AsyncOperationRequest[capo_lex_models_v2.types.list_slots_request.ListSlotsRequest]",
        ) -> AsyncOperationResponse[
            "capo_lex_models_v2.types.list_slots_response.ListSlotsResponse"
        ]:
            import capo_lex_models_v2._operations.lex_model_building_service_v2.list_slots

            (
                output,
                http_response,
            ) = await capo_lex_models_v2._operations.lex_model_building_service_v2.list_slots.async_list_slots(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_lex_models_v2.types.list_slots_request.ListSlotsRequest = {
            "bot_id": bot_id,
            "bot_version": bot_version,
            "locale_id": locale_id,
            "intent_id": intent_id,
        }
        if sort_by is not None:
            input_["sort_by"] = sort_by
        if filters is not None:
            input_["filters"] = filters
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

    async def iter_list_slots(
        self,
        bot_id: "capo_lex_models_v2.types.id.Id",
        bot_version: "capo_lex_models_v2.types.bot_version.BotVersion",
        locale_id: "capo_lex_models_v2.types.locale_id.LocaleId",
        intent_id: "capo_lex_models_v2.types.id.Id",
        *,
        config_overrides: Optional[AsyncLexModelsV2ClientConfig] = None,
        sort_by: Optional["capo_lex_models_v2.types.slot_sort_by.SlotSortBy"] = None,
        filters: Optional["capo_lex_models_v2.types.slot_filters.SlotFilters"] = None,
        max_results: Optional["capo_lex_models_v2.types.max_results.MaxResults"] = None,
        next_token: Optional["capo_lex_models_v2.types.next_token.NextToken"] = None,
    ) -> (
        "AsyncIterator[capo_lex_models_v2.types.list_slots_response.ListSlotsResponse]"
    ):
        _token = next_token
        while True:
            _response = await self.list_slots(
                bot_id,
                bot_version,
                locale_id,
                intent_id,
                config_overrides=config_overrides,
                sort_by=sort_by,
                filters=filters,
                max_results=max_results,
                next_token=_token,
            )
            yield _response
            _token = _resolve_path(_response, ("next_token",))
            if not _token:
                break

    async def list_slot_types(
        self,
        bot_id: "capo_lex_models_v2.types.id.Id",
        bot_version: "capo_lex_models_v2.types.bot_version.BotVersion",
        locale_id: "capo_lex_models_v2.types.locale_id.LocaleId",
        *,
        config_overrides: Optional[AsyncLexModelsV2ClientConfig] = None,
        sort_by: Optional[
            "capo_lex_models_v2.types.slot_type_sort_by.SlotTypeSortBy"
        ] = None,
        filters: Optional[
            "capo_lex_models_v2.types.slot_type_filters.SlotTypeFilters"
        ] = None,
        max_results: Optional["capo_lex_models_v2.types.max_results.MaxResults"] = None,
        next_token: Optional["capo_lex_models_v2.types.next_token.NextToken"] = None,
    ) -> "capo_lex_models_v2.types.list_slot_types_response.ListSlotTypesResponse":
        """<p>Gets a list of slot types that match the specified criteria.</p>

        Args:
            bot_id: <p>The unique identifier of the bot that contains the slot types.</p>
            bot_version: <p>The version of the bot that contains the slot type.</p>
            locale_id: <p>The identifier of the language and locale of the slot types to list. The string must match one of the supported locales. For more information, see <a href="https://docs.aws.amazon.com/lexv2/latest/dg/how-languages.html">Supported languages</a>.</p>
            sort_by: <p>Determines the sort order for the response from the <code>ListSlotTypes</code> operation. You can choose to sort by the slot type name or last updated date in either ascending or descending order.</p>
            filters: <p>Provides the specification of a filter used to limit the slot types in the response to only those that match the filter specification. You can only specify one filter and only one string to filter on.</p>
            max_results: <p>The maximum number of slot types to return in each page of results. If there are fewer results than the max page size, only the actual number of results are returned.</p>
            next_token: <p>If the response from the <code>ListSlotTypes</code> operation contains more results than specified in the <code>maxResults</code> parameter, a token is returned in the response. Use that token in the <code>nextToken</code> parameter to return the next page of results.</p>

        Raises:
            capo_lex_models_v2.errors.internal_server_exception.InternalServerException: <p>The service encountered an unexpected condition. Try your request again.</p>
            capo_lex_models_v2.errors.service_quota_exceeded_exception.ServiceQuotaExceededException: <p>You have reached a quota for your bot. </p>
            capo_lex_models_v2.errors.throttling_exception.ThrottlingException: <p>Your request rate is too high. Reduce the frequency of requests.</p>
            capo_lex_models_v2.errors.validation_exception.ValidationException: <p>One of the input parameters in your request isn't valid. Check the parameters and try your request again.</p>
            capo_lex_models_v2.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        async def _handler(
            req: "AsyncOperationRequest[capo_lex_models_v2.types.list_slot_types_request.ListSlotTypesRequest]",
        ) -> AsyncOperationResponse[
            "capo_lex_models_v2.types.list_slot_types_response.ListSlotTypesResponse"
        ]:
            import capo_lex_models_v2._operations.lex_model_building_service_v2.list_slot_types

            (
                output,
                http_response,
            ) = await capo_lex_models_v2._operations.lex_model_building_service_v2.list_slot_types.async_list_slot_types(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_lex_models_v2.types.list_slot_types_request.ListSlotTypesRequest = {
            "bot_id": bot_id,
            "bot_version": bot_version,
            "locale_id": locale_id,
        }
        if sort_by is not None:
            input_["sort_by"] = sort_by
        if filters is not None:
            input_["filters"] = filters
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

    async def iter_list_slot_types(
        self,
        bot_id: "capo_lex_models_v2.types.id.Id",
        bot_version: "capo_lex_models_v2.types.bot_version.BotVersion",
        locale_id: "capo_lex_models_v2.types.locale_id.LocaleId",
        *,
        config_overrides: Optional[AsyncLexModelsV2ClientConfig] = None,
        sort_by: Optional[
            "capo_lex_models_v2.types.slot_type_sort_by.SlotTypeSortBy"
        ] = None,
        filters: Optional[
            "capo_lex_models_v2.types.slot_type_filters.SlotTypeFilters"
        ] = None,
        max_results: Optional["capo_lex_models_v2.types.max_results.MaxResults"] = None,
        next_token: Optional["capo_lex_models_v2.types.next_token.NextToken"] = None,
    ) -> "AsyncIterator[capo_lex_models_v2.types.list_slot_types_response.ListSlotTypesResponse]":
        _token = next_token
        while True:
            _response = await self.list_slot_types(
                bot_id,
                bot_version,
                locale_id,
                config_overrides=config_overrides,
                sort_by=sort_by,
                filters=filters,
                max_results=max_results,
                next_token=_token,
            )
            yield _response
            _token = _resolve_path(_response, ("next_token",))
            if not _token:
                break

    async def list_tags_for_resource(
        self,
        resource_arn: "capo_lex_models_v2.types.amazon_resource_name.AmazonResourceName",
        *,
        config_overrides: Optional[AsyncLexModelsV2ClientConfig] = None,
    ) -> "capo_lex_models_v2.types.list_tags_for_resource_response.ListTagsForResourceResponse":
        """<p>Gets a list of tags associated with a resource. Only bots, bot aliases, and bot channels can have tags associated with them.</p>

        Args:
            resource_arn: <p>The Amazon Resource Name (ARN) of the resource to get a list of tags for.</p>

        Raises:
            capo_lex_models_v2.errors.internal_server_exception.InternalServerException: <p>The service encountered an unexpected condition. Try your request again.</p>
            capo_lex_models_v2.errors.resource_not_found_exception.ResourceNotFoundException: <p>You asked to describe a resource that doesn't exist. Check the resource that you are requesting and try again.</p>
            capo_lex_models_v2.errors.throttling_exception.ThrottlingException: <p>Your request rate is too high. Reduce the frequency of requests.</p>
            capo_lex_models_v2.errors.validation_exception.ValidationException: <p>One of the input parameters in your request isn't valid. Check the parameters and try your request again.</p>
            capo_lex_models_v2.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        async def _handler(
            req: "AsyncOperationRequest[capo_lex_models_v2.types.list_tags_for_resource_request.ListTagsForResourceRequest]",
        ) -> AsyncOperationResponse[
            "capo_lex_models_v2.types.list_tags_for_resource_response.ListTagsForResourceResponse"
        ]:
            import capo_lex_models_v2._operations.lex_model_building_service_v2.list_tags_for_resource

            (
                output,
                http_response,
            ) = await capo_lex_models_v2._operations.lex_model_building_service_v2.list_tags_for_resource.async_list_tags_for_resource(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_lex_models_v2.types.list_tags_for_resource_request.ListTagsForResourceRequest = {
            "resource_arn": resource_arn
        }

        response = await aexecute_pipeline(
            AsyncOperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        await response.response.aclose()
        return response.output

    async def list_test_execution_result_items(
        self,
        test_execution_id: "capo_lex_models_v2.types.id.Id",
        result_filter_by: "capo_lex_models_v2.types.test_execution_result_filter_by.TestExecutionResultFilterBy",
        *,
        config_overrides: Optional[AsyncLexModelsV2ClientConfig] = None,
        max_results: Optional["capo_lex_models_v2.types.max_results.MaxResults"] = None,
        next_token: Optional["capo_lex_models_v2.types.next_token.NextToken"] = None,
    ) -> "capo_lex_models_v2.types.list_test_execution_result_items_response.ListTestExecutionResultItemsResponse":
        """<p>Gets a list of test execution result items.</p>

        Args:
            test_execution_id: <p>The unique identifier of the test execution to list the result items.</p>
            result_filter_by: <p>The filter for the list of results from the test set execution.</p>
            max_results: <p>The maximum number of test execution result items to return in each page. If there are fewer results than the max page size, only the actual number of results are returned.</p>
            next_token: <p>If the response from the <code>ListTestExecutionResultItems</code> operation contains more results than specified in the <code>maxResults</code> parameter, a token is returned in the response. Use that token in the <code>nextToken</code> parameter to return the next page of results.</p>

        Raises:
            capo_lex_models_v2.errors.internal_server_exception.InternalServerException: <p>The service encountered an unexpected condition. Try your request again.</p>
            capo_lex_models_v2.errors.resource_not_found_exception.ResourceNotFoundException: <p>You asked to describe a resource that doesn't exist. Check the resource that you are requesting and try again.</p>
            capo_lex_models_v2.errors.service_quota_exceeded_exception.ServiceQuotaExceededException: <p>You have reached a quota for your bot. </p>
            capo_lex_models_v2.errors.throttling_exception.ThrottlingException: <p>Your request rate is too high. Reduce the frequency of requests.</p>
            capo_lex_models_v2.errors.validation_exception.ValidationException: <p>One of the input parameters in your request isn't valid. Check the parameters and try your request again.</p>
            capo_lex_models_v2.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        async def _handler(
            req: "AsyncOperationRequest[capo_lex_models_v2.types.list_test_execution_result_items_request.ListTestExecutionResultItemsRequest]",
        ) -> AsyncOperationResponse[
            "capo_lex_models_v2.types.list_test_execution_result_items_response.ListTestExecutionResultItemsResponse"
        ]:
            import capo_lex_models_v2._operations.lex_model_building_service_v2.list_test_execution_result_items

            (
                output,
                http_response,
            ) = await capo_lex_models_v2._operations.lex_model_building_service_v2.list_test_execution_result_items.async_list_test_execution_result_items(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_lex_models_v2.types.list_test_execution_result_items_request.ListTestExecutionResultItemsRequest = {
            "test_execution_id": test_execution_id,
            "result_filter_by": result_filter_by,
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

    async def iter_list_test_execution_result_items(
        self,
        test_execution_id: "capo_lex_models_v2.types.id.Id",
        result_filter_by: "capo_lex_models_v2.types.test_execution_result_filter_by.TestExecutionResultFilterBy",
        *,
        config_overrides: Optional[AsyncLexModelsV2ClientConfig] = None,
        max_results: Optional["capo_lex_models_v2.types.max_results.MaxResults"] = None,
        next_token: Optional["capo_lex_models_v2.types.next_token.NextToken"] = None,
    ) -> "AsyncIterator[capo_lex_models_v2.types.list_test_execution_result_items_response.ListTestExecutionResultItemsResponse]":
        _token = next_token
        while True:
            _response = await self.list_test_execution_result_items(
                test_execution_id,
                result_filter_by,
                config_overrides=config_overrides,
                max_results=max_results,
                next_token=_token,
            )
            yield _response
            _token = _resolve_path(_response, ("next_token",))
            if not _token:
                break

    async def list_test_executions(
        self,
        *,
        config_overrides: Optional[AsyncLexModelsV2ClientConfig] = None,
        sort_by: Optional[
            "capo_lex_models_v2.types.test_execution_sort_by.TestExecutionSortBy"
        ] = None,
        max_results: Optional["capo_lex_models_v2.types.max_results.MaxResults"] = None,
        next_token: Optional["capo_lex_models_v2.types.next_token.NextToken"] = None,
    ) -> "capo_lex_models_v2.types.list_test_executions_response.ListTestExecutionsResponse":
        """<p>The list of test set executions.</p>

        Args:
            sort_by: <p>The sort order of the test set executions.</p>
            max_results: <p>The maximum number of test executions to return in each page. If there are fewer results than the max page size, only the actual number of results are returned.</p>
            next_token: <p>If the response from the ListTestExecutions operation contains more results than specified in the maxResults parameter, a token is returned in the response. Use that token in the nextToken parameter to return the next page of results.</p>

        Raises:
            capo_lex_models_v2.errors.internal_server_exception.InternalServerException: <p>The service encountered an unexpected condition. Try your request again.</p>
            capo_lex_models_v2.errors.service_quota_exceeded_exception.ServiceQuotaExceededException: <p>You have reached a quota for your bot. </p>
            capo_lex_models_v2.errors.throttling_exception.ThrottlingException: <p>Your request rate is too high. Reduce the frequency of requests.</p>
            capo_lex_models_v2.errors.validation_exception.ValidationException: <p>One of the input parameters in your request isn't valid. Check the parameters and try your request again.</p>
            capo_lex_models_v2.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        async def _handler(
            req: "AsyncOperationRequest[capo_lex_models_v2.types.list_test_executions_request.ListTestExecutionsRequest]",
        ) -> AsyncOperationResponse[
            "capo_lex_models_v2.types.list_test_executions_response.ListTestExecutionsResponse"
        ]:
            import capo_lex_models_v2._operations.lex_model_building_service_v2.list_test_executions

            (
                output,
                http_response,
            ) = await capo_lex_models_v2._operations.lex_model_building_service_v2.list_test_executions.async_list_test_executions(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_lex_models_v2.types.list_test_executions_request.ListTestExecutionsRequest = {}
        if sort_by is not None:
            input_["sort_by"] = sort_by
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

    async def iter_list_test_executions(
        self,
        *,
        config_overrides: Optional[AsyncLexModelsV2ClientConfig] = None,
        sort_by: Optional[
            "capo_lex_models_v2.types.test_execution_sort_by.TestExecutionSortBy"
        ] = None,
        max_results: Optional["capo_lex_models_v2.types.max_results.MaxResults"] = None,
        next_token: Optional["capo_lex_models_v2.types.next_token.NextToken"] = None,
    ) -> "AsyncIterator[capo_lex_models_v2.types.list_test_executions_response.ListTestExecutionsResponse]":
        _token = next_token
        while True:
            _response = await self.list_test_executions(
                config_overrides=config_overrides,
                sort_by=sort_by,
                max_results=max_results,
                next_token=_token,
            )
            yield _response
            _token = _resolve_path(_response, ("next_token",))
            if not _token:
                break

    async def list_test_set_records(
        self,
        test_set_id: "capo_lex_models_v2.types.id.Id",
        *,
        config_overrides: Optional[AsyncLexModelsV2ClientConfig] = None,
        max_results: Optional["capo_lex_models_v2.types.max_results.MaxResults"] = None,
        next_token: Optional["capo_lex_models_v2.types.next_token.NextToken"] = None,
    ) -> "capo_lex_models_v2.types.list_test_set_records_response.ListTestSetRecordsResponse":
        """<p>The list of test set records.</p>

        Args:
            test_set_id: <p>The identifier of the test set to list its test set records.</p>
            max_results: <p>The maximum number of test set records to return in each page. If there are fewer records than the max page size, only the actual number of records are returned.</p>
            next_token: <p>If the response from the ListTestSetRecords operation contains more results than specified in the maxResults parameter, a token is returned in the response. Use that token in the nextToken parameter to return the next page of results.</p>

        Raises:
            capo_lex_models_v2.errors.internal_server_exception.InternalServerException: <p>The service encountered an unexpected condition. Try your request again.</p>
            capo_lex_models_v2.errors.resource_not_found_exception.ResourceNotFoundException: <p>You asked to describe a resource that doesn't exist. Check the resource that you are requesting and try again.</p>
            capo_lex_models_v2.errors.service_quota_exceeded_exception.ServiceQuotaExceededException: <p>You have reached a quota for your bot. </p>
            capo_lex_models_v2.errors.throttling_exception.ThrottlingException: <p>Your request rate is too high. Reduce the frequency of requests.</p>
            capo_lex_models_v2.errors.validation_exception.ValidationException: <p>One of the input parameters in your request isn't valid. Check the parameters and try your request again.</p>
            capo_lex_models_v2.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        async def _handler(
            req: "AsyncOperationRequest[capo_lex_models_v2.types.list_test_set_records_request.ListTestSetRecordsRequest]",
        ) -> AsyncOperationResponse[
            "capo_lex_models_v2.types.list_test_set_records_response.ListTestSetRecordsResponse"
        ]:
            import capo_lex_models_v2._operations.lex_model_building_service_v2.list_test_set_records

            (
                output,
                http_response,
            ) = await capo_lex_models_v2._operations.lex_model_building_service_v2.list_test_set_records.async_list_test_set_records(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_lex_models_v2.types.list_test_set_records_request.ListTestSetRecordsRequest = {
            "test_set_id": test_set_id
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

    async def iter_list_test_set_records(
        self,
        test_set_id: "capo_lex_models_v2.types.id.Id",
        *,
        config_overrides: Optional[AsyncLexModelsV2ClientConfig] = None,
        max_results: Optional["capo_lex_models_v2.types.max_results.MaxResults"] = None,
        next_token: Optional["capo_lex_models_v2.types.next_token.NextToken"] = None,
    ) -> "AsyncIterator[capo_lex_models_v2.types.list_test_set_records_response.ListTestSetRecordsResponse]":
        _token = next_token
        while True:
            _response = await self.list_test_set_records(
                test_set_id,
                config_overrides=config_overrides,
                max_results=max_results,
                next_token=_token,
            )
            yield _response
            _token = _resolve_path(_response, ("next_token",))
            if not _token:
                break

    async def list_test_sets(
        self,
        *,
        config_overrides: Optional[AsyncLexModelsV2ClientConfig] = None,
        sort_by: Optional[
            "capo_lex_models_v2.types.test_set_sort_by.TestSetSortBy"
        ] = None,
        max_results: Optional["capo_lex_models_v2.types.max_results.MaxResults"] = None,
        next_token: Optional["capo_lex_models_v2.types.next_token.NextToken"] = None,
    ) -> "capo_lex_models_v2.types.list_test_sets_response.ListTestSetsResponse":
        """<p>The list of the test sets</p>

        Args:
            sort_by: <p>The sort order for the list of test sets.</p>
            max_results: <p>The maximum number of test sets to return in each page. If there are fewer results than the max page size, only the actual number of results are returned.</p>
            next_token: <p>If the response from the ListTestSets operation contains more results than specified in the maxResults parameter, a token is returned in the response. Use that token in the nextToken parameter to return the next page of results.</p>

        Raises:
            capo_lex_models_v2.errors.internal_server_exception.InternalServerException: <p>The service encountered an unexpected condition. Try your request again.</p>
            capo_lex_models_v2.errors.service_quota_exceeded_exception.ServiceQuotaExceededException: <p>You have reached a quota for your bot. </p>
            capo_lex_models_v2.errors.throttling_exception.ThrottlingException: <p>Your request rate is too high. Reduce the frequency of requests.</p>
            capo_lex_models_v2.errors.validation_exception.ValidationException: <p>One of the input parameters in your request isn't valid. Check the parameters and try your request again.</p>
            capo_lex_models_v2.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        async def _handler(
            req: "AsyncOperationRequest[capo_lex_models_v2.types.list_test_sets_request.ListTestSetsRequest]",
        ) -> AsyncOperationResponse[
            "capo_lex_models_v2.types.list_test_sets_response.ListTestSetsResponse"
        ]:
            import capo_lex_models_v2._operations.lex_model_building_service_v2.list_test_sets

            (
                output,
                http_response,
            ) = await capo_lex_models_v2._operations.lex_model_building_service_v2.list_test_sets.async_list_test_sets(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_lex_models_v2.types.list_test_sets_request.ListTestSetsRequest = {}
        if sort_by is not None:
            input_["sort_by"] = sort_by
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

    async def iter_list_test_sets(
        self,
        *,
        config_overrides: Optional[AsyncLexModelsV2ClientConfig] = None,
        sort_by: Optional[
            "capo_lex_models_v2.types.test_set_sort_by.TestSetSortBy"
        ] = None,
        max_results: Optional["capo_lex_models_v2.types.max_results.MaxResults"] = None,
        next_token: Optional["capo_lex_models_v2.types.next_token.NextToken"] = None,
    ) -> "AsyncIterator[capo_lex_models_v2.types.list_test_sets_response.ListTestSetsResponse]":
        _token = next_token
        while True:
            _response = await self.list_test_sets(
                config_overrides=config_overrides,
                sort_by=sort_by,
                max_results=max_results,
                next_token=_token,
            )
            yield _response
            _token = _resolve_path(_response, ("next_token",))
            if not _token:
                break

    async def list_utterance_analytics_data(
        self,
        bot_id: "capo_lex_models_v2.types.id.Id",
        start_date_time: "capo_lex_models_v2.types.timestamp.Timestamp",
        end_date_time: "capo_lex_models_v2.types.timestamp.Timestamp",
        *,
        config_overrides: Optional[AsyncLexModelsV2ClientConfig] = None,
        sort_by: Optional[
            "capo_lex_models_v2.types.utterance_data_sort_by.UtteranceDataSortBy"
        ] = None,
        filters: Optional[
            "capo_lex_models_v2.types.analytics_utterance_filters.AnalyticsUtteranceFilters"
        ] = None,
        max_results: Optional["capo_lex_models_v2.types.max_results.MaxResults"] = None,
        next_token: Optional["capo_lex_models_v2.types.next_token.NextToken"] = None,
    ) -> "capo_lex_models_v2.types.list_utterance_analytics_data_response.ListUtteranceAnalyticsDataResponse":
        """<note> <p>To use this API operation, your IAM role must have permissions to perform the <a href="https://docs.aws.amazon.com/lexv2/latest/APIReference/API_ListAggregatedUtterances.html">ListAggregatedUtterances</a> operation, which provides access to utterance-related analytics. See <a href="https://docs.aws.amazon.com/lexv2/latest/dg/monitoring-utterances.html">Viewing utterance statistics</a> for the IAM policy to apply to the IAM role.</p> </note> <p>Retrieves a list of metadata for individual user utterances to your bot. The following fields are required:</p> <ul> <li> <p> <code>startDateTime</code> and <code>endDateTime</code> – Define a time range for which you want to retrieve results.</p> </li> </ul> <p>Of the optional fields, you can organize the results in the following ways:</p> <ul> <li> <p>Use the <code>filters</code> field to filter the results and the <code>sortBy</code> field to specify the values by which to sort the results.</p> </li> <li> <p>Use the <code>maxResults</code> field to limit the number of results to return in a single response and the <code>nextToken</code> field to return the next batch of results if the response does not return the full set of results.</p> </li> </ul>

        Args:
            bot_id: <p>The identifier for the bot for which you want to retrieve utterance analytics.</p>
            start_date_time: <p>The date and time that marks the beginning of the range of time for which you want to see utterance analytics.</p>
            end_date_time: <p>The date and time that marks the end of the range of time for which you want to see utterance analytics.</p>
            sort_by: <p>An object specifying the measure and method by which to sort the utterance analytics data.</p>
            filters: <p>A list of objects, each of which describes a condition by which you want to filter the results.</p>
            max_results: <p>The maximum number of results to return in each page of results. If there are fewer results than the maximum page size, only the actual number of results are returned.</p>
            next_token: <p>If the response from the ListUtteranceAnalyticsData operation contains more results than specified in the maxResults parameter, a token is returned in the response.</p> <p>Use the returned token in the nextToken parameter of a ListUtteranceAnalyticsData request to return the next page of results. For a complete set of results, call the ListUtteranceAnalyticsData operation until the nextToken returned in the response is null.</p>

        Raises:
            capo_lex_models_v2.errors.internal_server_exception.InternalServerException: <p>The service encountered an unexpected condition. Try your request again.</p>
            capo_lex_models_v2.errors.precondition_failed_exception.PreconditionFailedException: <p>Your request couldn't be completed because one or more request fields aren't valid. Check the fields in your request and try again.</p>
            capo_lex_models_v2.errors.service_quota_exceeded_exception.ServiceQuotaExceededException: <p>You have reached a quota for your bot. </p>
            capo_lex_models_v2.errors.throttling_exception.ThrottlingException: <p>Your request rate is too high. Reduce the frequency of requests.</p>
            capo_lex_models_v2.errors.validation_exception.ValidationException: <p>One of the input parameters in your request isn't valid. Check the parameters and try your request again.</p>
            capo_lex_models_v2.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        async def _handler(
            req: "AsyncOperationRequest[capo_lex_models_v2.types.list_utterance_analytics_data_request.ListUtteranceAnalyticsDataRequest]",
        ) -> AsyncOperationResponse[
            "capo_lex_models_v2.types.list_utterance_analytics_data_response.ListUtteranceAnalyticsDataResponse"
        ]:
            import capo_lex_models_v2._operations.lex_model_building_service_v2.list_utterance_analytics_data

            (
                output,
                http_response,
            ) = await capo_lex_models_v2._operations.lex_model_building_service_v2.list_utterance_analytics_data.async_list_utterance_analytics_data(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_lex_models_v2.types.list_utterance_analytics_data_request.ListUtteranceAnalyticsDataRequest = {
            "bot_id": bot_id,
            "start_date_time": start_date_time,
            "end_date_time": end_date_time,
        }
        if sort_by is not None:
            input_["sort_by"] = sort_by
        if filters is not None:
            input_["filters"] = filters
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

    async def iter_list_utterance_analytics_data(
        self,
        bot_id: "capo_lex_models_v2.types.id.Id",
        start_date_time: "capo_lex_models_v2.types.timestamp.Timestamp",
        end_date_time: "capo_lex_models_v2.types.timestamp.Timestamp",
        *,
        config_overrides: Optional[AsyncLexModelsV2ClientConfig] = None,
        sort_by: Optional[
            "capo_lex_models_v2.types.utterance_data_sort_by.UtteranceDataSortBy"
        ] = None,
        filters: Optional[
            "capo_lex_models_v2.types.analytics_utterance_filters.AnalyticsUtteranceFilters"
        ] = None,
        max_results: Optional["capo_lex_models_v2.types.max_results.MaxResults"] = None,
        next_token: Optional["capo_lex_models_v2.types.next_token.NextToken"] = None,
    ) -> "AsyncIterator[capo_lex_models_v2.types.list_utterance_analytics_data_response.ListUtteranceAnalyticsDataResponse]":
        _token = next_token
        while True:
            _response = await self.list_utterance_analytics_data(
                bot_id,
                start_date_time,
                end_date_time,
                config_overrides=config_overrides,
                sort_by=sort_by,
                filters=filters,
                max_results=max_results,
                next_token=_token,
            )
            yield _response
            _token = _resolve_path(_response, ("next_token",))
            if not _token:
                break

    async def list_utterance_metrics(
        self,
        bot_id: "capo_lex_models_v2.types.id.Id",
        start_date_time: "capo_lex_models_v2.types.timestamp.Timestamp",
        end_date_time: "capo_lex_models_v2.types.timestamp.Timestamp",
        metrics: "capo_lex_models_v2.types.analytics_utterance_metrics.AnalyticsUtteranceMetrics",
        *,
        config_overrides: Optional[AsyncLexModelsV2ClientConfig] = None,
        bin_by: Optional[
            "capo_lex_models_v2.types.analytics_bin_by_list.AnalyticsBinByList"
        ] = None,
        group_by: Optional[
            "capo_lex_models_v2.types.analytics_utterance_group_by_list.AnalyticsUtteranceGroupByList"
        ] = None,
        attributes: Optional[
            "capo_lex_models_v2.types.analytics_utterance_attributes.AnalyticsUtteranceAttributes"
        ] = None,
        filters: Optional[
            "capo_lex_models_v2.types.analytics_utterance_filters.AnalyticsUtteranceFilters"
        ] = None,
        max_results: Optional["capo_lex_models_v2.types.max_results.MaxResults"] = None,
        next_token: Optional["capo_lex_models_v2.types.next_token.NextToken"] = None,
    ) -> "capo_lex_models_v2.types.list_utterance_metrics_response.ListUtteranceMetricsResponse":
        """<note> <p>To use this API operation, your IAM role must have permissions to perform the <a href="https://docs.aws.amazon.com/lexv2/latest/APIReference/API_ListAggregatedUtterances.html">ListAggregatedUtterances</a> operation, which provides access to utterance-related analytics. See <a href="https://docs.aws.amazon.com/lexv2/latest/dg/monitoring-utterances.html">Viewing utterance statistics</a> for the IAM policy to apply to the IAM role.</p> </note> <p>Retrieves summary metrics for the utterances in your bot. The following fields are required:</p> <ul> <li> <p> <code>metrics</code> – A list of <a href="https://docs.aws.amazon.com/lexv2/latest/APIReference/API_AnalyticsUtteranceMetric.html">AnalyticsUtteranceMetric</a> objects. In each object, use the <code>name</code> field to specify the metric to calculate, the <code>statistic</code> field to specify whether to calculate the <code>Sum</code>, <code>Average</code>, or <code>Max</code> number, and the <code>order</code> field to specify whether to sort the results in <code>Ascending</code> or <code>Descending</code> order.</p> </li> <li> <p> <code>startDateTime</code> and <code>endDateTime</code> – Define a time range for which you want to retrieve results.</p> </li> </ul> <p>Of the optional fields, you can organize the results in the following ways:</p> <ul> <li> <p>Use the <code>filters</code> field to filter the results, the <code>groupBy</code> field to specify categories by which to group the results, and the <code>binBy</code> field to specify time intervals by which to group the results.</p> </li> <li> <p>Use the <code>maxResults</code> field to limit the number of results to return in a single response and the <code>nextToken</code> field to return the next batch of results if the response does not return the full set of results.</p> </li> </ul> <p>Note that an <code>order</code> field exists in both <code>binBy</code> and <code>metrics</code>. Currently, you can specify it in either field, but not in both.</p>

        Args:
            bot_id: <p>The identifier for the bot for which you want to retrieve utterance metrics.</p>
            start_date_time: <p>The date and time that marks the beginning of the range of time for which you want to see utterance metrics.</p>
            end_date_time: <p>The date and time that marks the end of the range of time for which you want to see utterance metrics.</p>
            metrics: <p>A list of objects, each of which contains a metric you want to list, the statistic for the metric you want to return, and the method by which to organize the results.</p>
            bin_by: <p>A list of objects, each of which contains specifications for organizing the results by time.</p>
            group_by: <p>A list of objects, each of which specifies how to group the results. You can group by the following criteria:</p> <ul> <li> <p> <code>UtteranceText</code> – The transcription of the utterance.</p> </li> <li> <p> <code>UtteranceState</code> – The state of the utterance. The possible states are detailed in <a href="https://docs.aws.amazon.com/analytics-key-definitions-utterances">Key definitions</a> in the user guide.</p> </li> </ul>
            attributes: <p>A list containing attributes related to the utterance that you want the response to return. The following attributes are possible:</p> <ul> <li> <p> <code>LastUsedIntent</code> – The last used intent at the time of the utterance.</p> </li> </ul>
            filters: <p>A list of objects, each of which describes a condition by which you want to filter the results.</p>
            max_results: <p>The maximum number of results to return in each page of results. If there are fewer results than the maximum page size, only the actual number of results are returned.</p>
            next_token: <p>If the response from the ListUtteranceMetrics operation contains more results than specified in the maxResults parameter, a token is returned in the response.</p> <p>Use the returned token in the nextToken parameter of a ListUtteranceMetrics request to return the next page of results. For a complete set of results, call the ListUtteranceMetrics operation until the nextToken returned in the response is null.</p>

        Raises:
            capo_lex_models_v2.errors.internal_server_exception.InternalServerException: <p>The service encountered an unexpected condition. Try your request again.</p>
            capo_lex_models_v2.errors.precondition_failed_exception.PreconditionFailedException: <p>Your request couldn't be completed because one or more request fields aren't valid. Check the fields in your request and try again.</p>
            capo_lex_models_v2.errors.service_quota_exceeded_exception.ServiceQuotaExceededException: <p>You have reached a quota for your bot. </p>
            capo_lex_models_v2.errors.throttling_exception.ThrottlingException: <p>Your request rate is too high. Reduce the frequency of requests.</p>
            capo_lex_models_v2.errors.validation_exception.ValidationException: <p>One of the input parameters in your request isn't valid. Check the parameters and try your request again.</p>
            capo_lex_models_v2.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        async def _handler(
            req: "AsyncOperationRequest[capo_lex_models_v2.types.list_utterance_metrics_request.ListUtteranceMetricsRequest]",
        ) -> AsyncOperationResponse[
            "capo_lex_models_v2.types.list_utterance_metrics_response.ListUtteranceMetricsResponse"
        ]:
            import capo_lex_models_v2._operations.lex_model_building_service_v2.list_utterance_metrics

            (
                output,
                http_response,
            ) = await capo_lex_models_v2._operations.lex_model_building_service_v2.list_utterance_metrics.async_list_utterance_metrics(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_lex_models_v2.types.list_utterance_metrics_request.ListUtteranceMetricsRequest = {
            "bot_id": bot_id,
            "start_date_time": start_date_time,
            "end_date_time": end_date_time,
            "metrics": metrics,
        }
        if bin_by is not None:
            input_["bin_by"] = bin_by
        if group_by is not None:
            input_["group_by"] = group_by
        if attributes is not None:
            input_["attributes"] = attributes
        if filters is not None:
            input_["filters"] = filters
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

    async def iter_list_utterance_metrics(
        self,
        bot_id: "capo_lex_models_v2.types.id.Id",
        start_date_time: "capo_lex_models_v2.types.timestamp.Timestamp",
        end_date_time: "capo_lex_models_v2.types.timestamp.Timestamp",
        metrics: "capo_lex_models_v2.types.analytics_utterance_metrics.AnalyticsUtteranceMetrics",
        *,
        config_overrides: Optional[AsyncLexModelsV2ClientConfig] = None,
        bin_by: Optional[
            "capo_lex_models_v2.types.analytics_bin_by_list.AnalyticsBinByList"
        ] = None,
        group_by: Optional[
            "capo_lex_models_v2.types.analytics_utterance_group_by_list.AnalyticsUtteranceGroupByList"
        ] = None,
        attributes: Optional[
            "capo_lex_models_v2.types.analytics_utterance_attributes.AnalyticsUtteranceAttributes"
        ] = None,
        filters: Optional[
            "capo_lex_models_v2.types.analytics_utterance_filters.AnalyticsUtteranceFilters"
        ] = None,
        max_results: Optional["capo_lex_models_v2.types.max_results.MaxResults"] = None,
        next_token: Optional["capo_lex_models_v2.types.next_token.NextToken"] = None,
    ) -> "AsyncIterator[capo_lex_models_v2.types.list_utterance_metrics_response.ListUtteranceMetricsResponse]":
        _token = next_token
        while True:
            _response = await self.list_utterance_metrics(
                bot_id,
                start_date_time,
                end_date_time,
                metrics,
                config_overrides=config_overrides,
                bin_by=bin_by,
                group_by=group_by,
                attributes=attributes,
                filters=filters,
                max_results=max_results,
                next_token=_token,
            )
            yield _response
            _token = _resolve_path(_response, ("next_token",))
            if not _token:
                break

    async def search_associated_transcripts(
        self,
        bot_id: "capo_lex_models_v2.types.id.Id",
        bot_version: "capo_lex_models_v2.types.bot_version.BotVersion",
        locale_id: "capo_lex_models_v2.types.locale_id.LocaleId",
        bot_recommendation_id: "capo_lex_models_v2.types.id.Id",
        filters: "capo_lex_models_v2.types.associated_transcript_filters.AssociatedTranscriptFilters",
        *,
        config_overrides: Optional[AsyncLexModelsV2ClientConfig] = None,
        search_order: Optional[
            "capo_lex_models_v2.types.search_order.SearchOrder"
        ] = None,
        max_results: Optional["capo_lex_models_v2.types.max_results.MaxResults"] = None,
        next_index: Optional["capo_lex_models_v2.types.next_index.NextIndex"] = None,
    ) -> "capo_lex_models_v2.types.search_associated_transcripts_response.SearchAssociatedTranscriptsResponse":
        """<p>Search for associated transcripts that meet the specified criteria.</p>

        Args:
            bot_id: <p>The unique identifier of the bot associated with the transcripts that you are searching.</p>
            bot_version: <p>The version of the bot containing the transcripts that you are searching.</p>
            locale_id: <p>The identifier of the language and locale of the transcripts to search. The string must match one of the supported locales. For more information, see <a href="https://docs.aws.amazon.com/lexv2/latest/dg/how-languages.html">Supported languages</a> </p>
            bot_recommendation_id: <p>The unique identifier of the bot recommendation associated with the transcripts to search.</p>
            search_order: <p>How SearchResults are ordered. Valid values are Ascending or Descending. The default is Descending.</p>
            filters: <p>A list of filter objects.</p>
            max_results: <p>The maximum number of bot recommendations to return in each page of results. If there are fewer results than the max page size, only the actual number of results are returned.</p>
            next_index: <p>If the response from the SearchAssociatedTranscriptsRequest operation contains more results than specified in the maxResults parameter, an index is returned in the response. Use that index in the nextIndex parameter to return the next page of results.</p>

        Raises:
            capo_lex_models_v2.errors.internal_server_exception.InternalServerException: <p>The service encountered an unexpected condition. Try your request again.</p>
            capo_lex_models_v2.errors.resource_not_found_exception.ResourceNotFoundException: <p>You asked to describe a resource that doesn't exist. Check the resource that you are requesting and try again.</p>
            capo_lex_models_v2.errors.service_quota_exceeded_exception.ServiceQuotaExceededException: <p>You have reached a quota for your bot. </p>
            capo_lex_models_v2.errors.throttling_exception.ThrottlingException: <p>Your request rate is too high. Reduce the frequency of requests.</p>
            capo_lex_models_v2.errors.validation_exception.ValidationException: <p>One of the input parameters in your request isn't valid. Check the parameters and try your request again.</p>
            capo_lex_models_v2.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        async def _handler(
            req: "AsyncOperationRequest[capo_lex_models_v2.types.search_associated_transcripts_request.SearchAssociatedTranscriptsRequest]",
        ) -> AsyncOperationResponse[
            "capo_lex_models_v2.types.search_associated_transcripts_response.SearchAssociatedTranscriptsResponse"
        ]:
            import capo_lex_models_v2._operations.lex_model_building_service_v2.search_associated_transcripts

            (
                output,
                http_response,
            ) = await capo_lex_models_v2._operations.lex_model_building_service_v2.search_associated_transcripts.async_search_associated_transcripts(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_lex_models_v2.types.search_associated_transcripts_request.SearchAssociatedTranscriptsRequest = {
            "bot_id": bot_id,
            "bot_version": bot_version,
            "locale_id": locale_id,
            "bot_recommendation_id": bot_recommendation_id,
            "filters": filters,
        }
        if search_order is not None:
            input_["search_order"] = search_order
        if max_results is not None:
            input_["max_results"] = max_results
        if next_index is not None:
            input_["next_index"] = next_index

        response = await aexecute_pipeline(
            AsyncOperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        await response.response.aclose()
        return response.output

    async def start_bot_analyzer(
        self,
        bot_id: "capo_lex_models_v2.types.id.Id",
        analysis_scope: "capo_lex_models_v2.types.analysis_scope.AnalysisScope",
        *,
        config_overrides: Optional[AsyncLexModelsV2ClientConfig] = None,
        locale_id: Optional["capo_lex_models_v2.types.locale_id.LocaleId"] = None,
        bot_version: Optional[
            "capo_lex_models_v2.types.draft_bot_version.DraftBotVersion"
        ] = None,
    ) -> (
        "capo_lex_models_v2.types.start_bot_analyzer_response.StartBotAnalyzerResponse"
    ):
        """<p>Initiates an asynchronous analysis of your bot configuration using AI-powered analysis to identify potential issues and recommend improvements based on AWS best practices.</p> <p>The analysis examines your bot's configuration, including intents, utterances, slots, and conversation flows, to provide actionable recommendations for optimization.</p>

        Args:
            bot_id: <p>The unique identifier of the bot to analyze.</p>
            analysis_scope: <p>The scope of analysis to perform. Currently only <code>BotLocale</code> scope is supported.</p> <p>Valid Values: <code>BotLocale</code> </p>
            locale_id: <p>The locale identifier for the bot locale to analyze. Required when <code>analysisScope</code> is <code>BotLocale</code>.</p>
            bot_version: <p>The version of the bot to analyze. Defaults to <code>DRAFT</code> if not specified.</p>

        Raises:
            capo_lex_models_v2.errors.conflict_exception.ConflictException: <p>The action that you tried to perform couldn't be completed because the resource is in a conflicting state. For example, deleting a bot that is in the CREATING state. Try your request again. </p>
            capo_lex_models_v2.errors.internal_server_exception.InternalServerException: <p>The service encountered an unexpected condition. Try your request again.</p>
            capo_lex_models_v2.errors.resource_not_found_exception.ResourceNotFoundException: <p>You asked to describe a resource that doesn't exist. Check the resource that you are requesting and try again.</p>
            capo_lex_models_v2.errors.throttling_exception.ThrottlingException: <p>Your request rate is too high. Reduce the frequency of requests.</p>
            capo_lex_models_v2.errors.validation_exception.ValidationException: <p>One of the input parameters in your request isn't valid. Check the parameters and try your request again.</p>
            capo_lex_models_v2.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        async def _handler(
            req: "AsyncOperationRequest[capo_lex_models_v2.types.start_bot_analyzer_request.StartBotAnalyzerRequest]",
        ) -> AsyncOperationResponse[
            "capo_lex_models_v2.types.start_bot_analyzer_response.StartBotAnalyzerResponse"
        ]:
            import capo_lex_models_v2._operations.lex_model_building_service_v2.start_bot_analyzer

            (
                output,
                http_response,
            ) = await capo_lex_models_v2._operations.lex_model_building_service_v2.start_bot_analyzer.async_start_bot_analyzer(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_lex_models_v2.types.start_bot_analyzer_request.StartBotAnalyzerRequest = {
            "bot_id": bot_id,
            "analysis_scope": analysis_scope,
        }
        if locale_id is not None:
            input_["locale_id"] = locale_id
        if bot_version is not None:
            input_["bot_version"] = bot_version

        response = await aexecute_pipeline(
            AsyncOperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        await response.response.aclose()
        return response.output

    async def start_bot_recommendation(
        self,
        bot_id: "capo_lex_models_v2.types.id.Id",
        bot_version: "capo_lex_models_v2.types.draft_bot_version.DraftBotVersion",
        locale_id: "capo_lex_models_v2.types.locale_id.LocaleId",
        transcript_source_setting: "capo_lex_models_v2.types.transcript_source_setting.TranscriptSourceSetting",
        *,
        config_overrides: Optional[AsyncLexModelsV2ClientConfig] = None,
        encryption_setting: Optional[
            "capo_lex_models_v2.types.encryption_setting.EncryptionSetting"
        ] = None,
    ) -> "capo_lex_models_v2.types.start_bot_recommendation_response.StartBotRecommendationResponse":
        """<p>Use this to provide your transcript data, and to start the bot recommendation process.</p>

        Args:
            bot_id: <p>The unique identifier of the bot containing the bot recommendation.</p>
            bot_version: <p>The version of the bot containing the bot recommendation.</p>
            locale_id: <p>The identifier of the language and locale of the bot recommendation to start. The string must match one of the supported locales. For more information, see <a href="https://docs.aws.amazon.com/lexv2/latest/dg/how-languages.html">Supported languages</a> </p>
            transcript_source_setting: <p>The object representing the Amazon S3 bucket containing the transcript, as well as the associated metadata.</p>
            encryption_setting: <p>The object representing the passwords that will be used to encrypt the data related to the bot recommendation results, as well as the KMS key ARN used to encrypt the associated metadata.</p>

        Raises:
            capo_lex_models_v2.errors.conflict_exception.ConflictException: <p>The action that you tried to perform couldn't be completed because the resource is in a conflicting state. For example, deleting a bot that is in the CREATING state. Try your request again. </p>
            capo_lex_models_v2.errors.internal_server_exception.InternalServerException: <p>The service encountered an unexpected condition. Try your request again.</p>
            capo_lex_models_v2.errors.precondition_failed_exception.PreconditionFailedException: <p>Your request couldn't be completed because one or more request fields aren't valid. Check the fields in your request and try again.</p>
            capo_lex_models_v2.errors.resource_not_found_exception.ResourceNotFoundException: <p>You asked to describe a resource that doesn't exist. Check the resource that you are requesting and try again.</p>
            capo_lex_models_v2.errors.service_quota_exceeded_exception.ServiceQuotaExceededException: <p>You have reached a quota for your bot. </p>
            capo_lex_models_v2.errors.throttling_exception.ThrottlingException: <p>Your request rate is too high. Reduce the frequency of requests.</p>
            capo_lex_models_v2.errors.validation_exception.ValidationException: <p>One of the input parameters in your request isn't valid. Check the parameters and try your request again.</p>
            capo_lex_models_v2.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        async def _handler(
            req: "AsyncOperationRequest[capo_lex_models_v2.types.start_bot_recommendation_request.StartBotRecommendationRequest]",
        ) -> AsyncOperationResponse[
            "capo_lex_models_v2.types.start_bot_recommendation_response.StartBotRecommendationResponse"
        ]:
            import capo_lex_models_v2._operations.lex_model_building_service_v2.start_bot_recommendation

            (
                output,
                http_response,
            ) = await capo_lex_models_v2._operations.lex_model_building_service_v2.start_bot_recommendation.async_start_bot_recommendation(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_lex_models_v2.types.start_bot_recommendation_request.StartBotRecommendationRequest = {
            "bot_id": bot_id,
            "bot_version": bot_version,
            "locale_id": locale_id,
            "transcript_source_setting": transcript_source_setting,
        }
        if encryption_setting is not None:
            input_["encryption_setting"] = encryption_setting

        response = await aexecute_pipeline(
            AsyncOperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        await response.response.aclose()
        return response.output

    async def start_bot_resource_generation(
        self,
        generation_input_prompt: "capo_lex_models_v2.types.generation_input.GenerationInput",
        bot_id: "capo_lex_models_v2.types.id.Id",
        bot_version: "capo_lex_models_v2.types.bot_version.BotVersion",
        locale_id: "capo_lex_models_v2.types.locale_id.LocaleId",
        *,
        config_overrides: Optional[AsyncLexModelsV2ClientConfig] = None,
    ) -> "capo_lex_models_v2.types.start_bot_resource_generation_response.StartBotResourceGenerationResponse":
        """<p>Starts a request for the descriptive bot builder to generate a bot locale configuration based on the prompt you provide it. After you make this call, use the <code>DescribeBotResourceGeneration</code> operation to check on the status of the generation and for the <code>generatedBotLocaleUrl</code> when the generation is complete. Use that value to retrieve the Amazon S3 object containing the bot locale configuration. You can then modify and import this configuration.</p>

        Args:
            generation_input_prompt: <p>The prompt to generate intents and slot types for the bot locale. Your description should be both <i>detailed</i> and <i>precise</i> to help generate appropriate and sufficient intents for your bot. Include a list of actions to improve the intent creation process.</p>
            bot_id: <p>The unique identifier of the bot for which to generate intents and slot types.</p>
            bot_version: <p>The version of the bot for which to generate intents and slot types.</p>
            locale_id: <p>The locale of the bot for which to generate intents and slot types.</p>

        Raises:
            capo_lex_models_v2.errors.conflict_exception.ConflictException: <p>The action that you tried to perform couldn't be completed because the resource is in a conflicting state. For example, deleting a bot that is in the CREATING state. Try your request again. </p>
            capo_lex_models_v2.errors.internal_server_exception.InternalServerException: <p>The service encountered an unexpected condition. Try your request again.</p>
            capo_lex_models_v2.errors.precondition_failed_exception.PreconditionFailedException: <p>Your request couldn't be completed because one or more request fields aren't valid. Check the fields in your request and try again.</p>
            capo_lex_models_v2.errors.service_quota_exceeded_exception.ServiceQuotaExceededException: <p>You have reached a quota for your bot. </p>
            capo_lex_models_v2.errors.throttling_exception.ThrottlingException: <p>Your request rate is too high. Reduce the frequency of requests.</p>
            capo_lex_models_v2.errors.validation_exception.ValidationException: <p>One of the input parameters in your request isn't valid. Check the parameters and try your request again.</p>
            capo_lex_models_v2.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        async def _handler(
            req: "AsyncOperationRequest[capo_lex_models_v2.types.start_bot_resource_generation_request.StartBotResourceGenerationRequest]",
        ) -> AsyncOperationResponse[
            "capo_lex_models_v2.types.start_bot_resource_generation_response.StartBotResourceGenerationResponse"
        ]:
            import capo_lex_models_v2._operations.lex_model_building_service_v2.start_bot_resource_generation

            (
                output,
                http_response,
            ) = await capo_lex_models_v2._operations.lex_model_building_service_v2.start_bot_resource_generation.async_start_bot_resource_generation(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_lex_models_v2.types.start_bot_resource_generation_request.StartBotResourceGenerationRequest = {
            "generation_input_prompt": generation_input_prompt,
            "bot_id": bot_id,
            "bot_version": bot_version,
            "locale_id": locale_id,
        }

        response = await aexecute_pipeline(
            AsyncOperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        await response.response.aclose()
        return response.output

    async def start_import(
        self,
        import_id: "capo_lex_models_v2.types.id.Id",
        resource_specification: "capo_lex_models_v2.types.import_resource_specification.ImportResourceSpecification",
        merge_strategy: "capo_lex_models_v2.types.merge_strategy.MergeStrategy",
        *,
        config_overrides: Optional[AsyncLexModelsV2ClientConfig] = None,
        file_password: Optional[
            "capo_lex_models_v2.types.import_export_file_password.ImportExportFilePassword"
        ] = None,
    ) -> "capo_lex_models_v2.types.start_import_response.StartImportResponse":
        """<p>Starts importing a bot, bot locale, or custom vocabulary from a zip archive that you uploaded to an S3 bucket.</p>

        Args:
            import_id: <p>The unique identifier for the import. It is included in the response from the <a href="https://docs.aws.amazon.com/lexv2/latest/APIReference/API_CreateUploadUrl.html">CreateUploadUrl</a> operation.</p>
            resource_specification: <p>Parameters for creating the bot, bot locale or custom vocabulary.</p>
            merge_strategy: <p>The strategy to use when there is a name conflict between the imported resource and an existing resource. When the merge strategy is <code>FailOnConflict</code> existing resources are not overwritten and the import fails.</p>
            file_password: <p>The password used to encrypt the zip archive that contains the resource definition. You should always encrypt the zip archive to protect it during transit between your site and Amazon Lex.</p>

        Raises:
            capo_lex_models_v2.errors.conflict_exception.ConflictException: <p>The action that you tried to perform couldn't be completed because the resource is in a conflicting state. For example, deleting a bot that is in the CREATING state. Try your request again. </p>
            capo_lex_models_v2.errors.internal_server_exception.InternalServerException: <p>The service encountered an unexpected condition. Try your request again.</p>
            capo_lex_models_v2.errors.resource_not_found_exception.ResourceNotFoundException: <p>You asked to describe a resource that doesn't exist. Check the resource that you are requesting and try again.</p>
            capo_lex_models_v2.errors.service_quota_exceeded_exception.ServiceQuotaExceededException: <p>You have reached a quota for your bot. </p>
            capo_lex_models_v2.errors.throttling_exception.ThrottlingException: <p>Your request rate is too high. Reduce the frequency of requests.</p>
            capo_lex_models_v2.errors.validation_exception.ValidationException: <p>One of the input parameters in your request isn't valid. Check the parameters and try your request again.</p>
            capo_lex_models_v2.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        async def _handler(
            req: "AsyncOperationRequest[capo_lex_models_v2.types.start_import_request.StartImportRequest]",
        ) -> AsyncOperationResponse[
            "capo_lex_models_v2.types.start_import_response.StartImportResponse"
        ]:
            import capo_lex_models_v2._operations.lex_model_building_service_v2.start_import

            (
                output,
                http_response,
            ) = await capo_lex_models_v2._operations.lex_model_building_service_v2.start_import.async_start_import(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_lex_models_v2.types.start_import_request.StartImportRequest = {
            "import_id": import_id,
            "resource_specification": resource_specification,
            "merge_strategy": merge_strategy,
        }
        if file_password is not None:
            input_["file_password"] = file_password

        response = await aexecute_pipeline(
            AsyncOperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        await response.response.aclose()
        return response.output

    async def start_test_execution(
        self,
        test_set_id: "capo_lex_models_v2.types.id.Id",
        target: "capo_lex_models_v2.types.test_execution_target.TestExecutionTarget",
        api_mode: "capo_lex_models_v2.types.test_execution_api_mode.TestExecutionApiMode",
        *,
        config_overrides: Optional[AsyncLexModelsV2ClientConfig] = None,
        test_execution_modality: Optional[
            "capo_lex_models_v2.types.test_execution_modality.TestExecutionModality"
        ] = None,
    ) -> "capo_lex_models_v2.types.start_test_execution_response.StartTestExecutionResponse":
        """<p>The action to start test set execution.</p>

        Args:
            test_set_id: <p>The test set Id for the test set execution.</p>
            target: <p>The target bot for the test set execution.</p>
            api_mode: <p>Indicates whether we use streaming or non-streaming APIs for the test set execution. For streaming, StartConversation Runtime API is used. Whereas, for non-streaming, RecognizeUtterance and RecognizeText Amazon Lex Runtime API are used.</p>
            test_execution_modality: <p>Indicates whether audio or text is used.</p>

        Raises:
            capo_lex_models_v2.errors.conflict_exception.ConflictException: <p>The action that you tried to perform couldn't be completed because the resource is in a conflicting state. For example, deleting a bot that is in the CREATING state. Try your request again. </p>
            capo_lex_models_v2.errors.internal_server_exception.InternalServerException: <p>The service encountered an unexpected condition. Try your request again.</p>
            capo_lex_models_v2.errors.resource_not_found_exception.ResourceNotFoundException: <p>You asked to describe a resource that doesn't exist. Check the resource that you are requesting and try again.</p>
            capo_lex_models_v2.errors.service_quota_exceeded_exception.ServiceQuotaExceededException: <p>You have reached a quota for your bot. </p>
            capo_lex_models_v2.errors.throttling_exception.ThrottlingException: <p>Your request rate is too high. Reduce the frequency of requests.</p>
            capo_lex_models_v2.errors.validation_exception.ValidationException: <p>One of the input parameters in your request isn't valid. Check the parameters and try your request again.</p>
            capo_lex_models_v2.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        async def _handler(
            req: "AsyncOperationRequest[capo_lex_models_v2.types.start_test_execution_request.StartTestExecutionRequest]",
        ) -> AsyncOperationResponse[
            "capo_lex_models_v2.types.start_test_execution_response.StartTestExecutionResponse"
        ]:
            import capo_lex_models_v2._operations.lex_model_building_service_v2.start_test_execution

            (
                output,
                http_response,
            ) = await capo_lex_models_v2._operations.lex_model_building_service_v2.start_test_execution.async_start_test_execution(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_lex_models_v2.types.start_test_execution_request.StartTestExecutionRequest = {
            "test_set_id": test_set_id,
            "target": target,
            "api_mode": api_mode,
        }
        if test_execution_modality is not None:
            input_["test_execution_modality"] = test_execution_modality

        response = await aexecute_pipeline(
            AsyncOperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        await response.response.aclose()
        return response.output

    async def start_test_set_generation(
        self,
        test_set_name: "capo_lex_models_v2.types.name.Name",
        storage_location: "capo_lex_models_v2.types.test_set_storage_location.TestSetStorageLocation",
        generation_data_source: "capo_lex_models_v2.types.test_set_generation_data_source.TestSetGenerationDataSource",
        role_arn: "capo_lex_models_v2.types.role_arn.RoleArn",
        *,
        config_overrides: Optional[AsyncLexModelsV2ClientConfig] = None,
        description: Optional[
            "capo_lex_models_v2.types.description.Description"
        ] = None,
        test_set_tags: Optional["capo_lex_models_v2.types.tag_map.TagMap"] = None,
    ) -> "capo_lex_models_v2.types.start_test_set_generation_response.StartTestSetGenerationResponse":
        """<p>The action to start the generation of test set.</p>

        Args:
            test_set_name: <p>The test set name for the test set generation request.</p>
            description: <p>The test set description for the test set generation request.</p>
            storage_location: <p>The Amazon S3 storage location for the test set generation.</p>
            generation_data_source: <p>The data source for the test set generation.</p>
            role_arn: <p>The roleARN used for any operation in the test set to access resources in the Amazon Web Services account.</p>
            test_set_tags: <p>A list of tags to add to the test set. You can only add tags when you import/generate a new test set. You can't use the <code>UpdateTestSet</code> operation to update tags. To update tags, use the <code>TagResource</code> operation.</p>

        Raises:
            capo_lex_models_v2.errors.conflict_exception.ConflictException: <p>The action that you tried to perform couldn't be completed because the resource is in a conflicting state. For example, deleting a bot that is in the CREATING state. Try your request again. </p>
            capo_lex_models_v2.errors.internal_server_exception.InternalServerException: <p>The service encountered an unexpected condition. Try your request again.</p>
            capo_lex_models_v2.errors.resource_not_found_exception.ResourceNotFoundException: <p>You asked to describe a resource that doesn't exist. Check the resource that you are requesting and try again.</p>
            capo_lex_models_v2.errors.service_quota_exceeded_exception.ServiceQuotaExceededException: <p>You have reached a quota for your bot. </p>
            capo_lex_models_v2.errors.throttling_exception.ThrottlingException: <p>Your request rate is too high. Reduce the frequency of requests.</p>
            capo_lex_models_v2.errors.validation_exception.ValidationException: <p>One of the input parameters in your request isn't valid. Check the parameters and try your request again.</p>
            capo_lex_models_v2.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        async def _handler(
            req: "AsyncOperationRequest[capo_lex_models_v2.types.start_test_set_generation_request.StartTestSetGenerationRequest]",
        ) -> AsyncOperationResponse[
            "capo_lex_models_v2.types.start_test_set_generation_response.StartTestSetGenerationResponse"
        ]:
            import capo_lex_models_v2._operations.lex_model_building_service_v2.start_test_set_generation

            (
                output,
                http_response,
            ) = await capo_lex_models_v2._operations.lex_model_building_service_v2.start_test_set_generation.async_start_test_set_generation(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_lex_models_v2.types.start_test_set_generation_request.StartTestSetGenerationRequest = {
            "test_set_name": test_set_name,
            "storage_location": storage_location,
            "generation_data_source": generation_data_source,
            "role_arn": role_arn,
        }
        if description is not None:
            input_["description"] = description
        if test_set_tags is not None:
            input_["test_set_tags"] = test_set_tags

        response = await aexecute_pipeline(
            AsyncOperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        await response.response.aclose()
        return response.output

    async def stop_bot_analyzer(
        self,
        bot_id: "capo_lex_models_v2.types.id.Id",
        bot_analyzer_request_id: "capo_lex_models_v2.types.uuid.UUID",
        *,
        config_overrides: Optional[AsyncLexModelsV2ClientConfig] = None,
    ) -> "capo_lex_models_v2.types.stop_bot_analyzer_response.StopBotAnalyzerResponse":
        """<p>Cancels an ongoing bot analysis execution. Once stopped, the analysis cannot be resumed and no recommendations will be generated.</p>

        Args:
            bot_id: <p>The unique identifier of the bot.</p>
            bot_analyzer_request_id: <p>The unique identifier of the analysis request to stop.</p>

        Raises:
            capo_lex_models_v2.errors.internal_server_exception.InternalServerException: <p>The service encountered an unexpected condition. Try your request again.</p>
            capo_lex_models_v2.errors.resource_not_found_exception.ResourceNotFoundException: <p>You asked to describe a resource that doesn't exist. Check the resource that you are requesting and try again.</p>
            capo_lex_models_v2.errors.throttling_exception.ThrottlingException: <p>Your request rate is too high. Reduce the frequency of requests.</p>
            capo_lex_models_v2.errors.validation_exception.ValidationException: <p>One of the input parameters in your request isn't valid. Check the parameters and try your request again.</p>
            capo_lex_models_v2.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        async def _handler(
            req: "AsyncOperationRequest[capo_lex_models_v2.types.stop_bot_analyzer_request.StopBotAnalyzerRequest]",
        ) -> AsyncOperationResponse[
            "capo_lex_models_v2.types.stop_bot_analyzer_response.StopBotAnalyzerResponse"
        ]:
            import capo_lex_models_v2._operations.lex_model_building_service_v2.stop_bot_analyzer

            (
                output,
                http_response,
            ) = await capo_lex_models_v2._operations.lex_model_building_service_v2.stop_bot_analyzer.async_stop_bot_analyzer(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_lex_models_v2.types.stop_bot_analyzer_request.StopBotAnalyzerRequest = {
            "bot_id": bot_id,
            "bot_analyzer_request_id": bot_analyzer_request_id,
        }

        response = await aexecute_pipeline(
            AsyncOperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        await response.response.aclose()
        return response.output

    async def stop_bot_recommendation(
        self,
        bot_id: "capo_lex_models_v2.types.id.Id",
        bot_version: "capo_lex_models_v2.types.draft_bot_version.DraftBotVersion",
        locale_id: "capo_lex_models_v2.types.locale_id.LocaleId",
        bot_recommendation_id: "capo_lex_models_v2.types.id.Id",
        *,
        config_overrides: Optional[AsyncLexModelsV2ClientConfig] = None,
    ) -> "capo_lex_models_v2.types.stop_bot_recommendation_response.StopBotRecommendationResponse":
        """<p>Stop an already running Bot Recommendation request.</p>

        Args:
            bot_id: <p>The unique identifier of the bot containing the bot recommendation to be stopped.</p>
            bot_version: <p>The version of the bot containing the bot recommendation.</p>
            locale_id: <p>The identifier of the language and locale of the bot recommendation to stop. The string must match one of the supported locales. For more information, see <a href="https://docs.aws.amazon.com/lexv2/latest/dg/how-languages.html">Supported languages</a> </p>
            bot_recommendation_id: <p>The unique identifier of the bot recommendation to be stopped.</p>

        Raises:
            capo_lex_models_v2.errors.conflict_exception.ConflictException: <p>The action that you tried to perform couldn't be completed because the resource is in a conflicting state. For example, deleting a bot that is in the CREATING state. Try your request again. </p>
            capo_lex_models_v2.errors.internal_server_exception.InternalServerException: <p>The service encountered an unexpected condition. Try your request again.</p>
            capo_lex_models_v2.errors.precondition_failed_exception.PreconditionFailedException: <p>Your request couldn't be completed because one or more request fields aren't valid. Check the fields in your request and try again.</p>
            capo_lex_models_v2.errors.resource_not_found_exception.ResourceNotFoundException: <p>You asked to describe a resource that doesn't exist. Check the resource that you are requesting and try again.</p>
            capo_lex_models_v2.errors.service_quota_exceeded_exception.ServiceQuotaExceededException: <p>You have reached a quota for your bot. </p>
            capo_lex_models_v2.errors.throttling_exception.ThrottlingException: <p>Your request rate is too high. Reduce the frequency of requests.</p>
            capo_lex_models_v2.errors.validation_exception.ValidationException: <p>One of the input parameters in your request isn't valid. Check the parameters and try your request again.</p>
            capo_lex_models_v2.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        async def _handler(
            req: "AsyncOperationRequest[capo_lex_models_v2.types.stop_bot_recommendation_request.StopBotRecommendationRequest]",
        ) -> AsyncOperationResponse[
            "capo_lex_models_v2.types.stop_bot_recommendation_response.StopBotRecommendationResponse"
        ]:
            import capo_lex_models_v2._operations.lex_model_building_service_v2.stop_bot_recommendation

            (
                output,
                http_response,
            ) = await capo_lex_models_v2._operations.lex_model_building_service_v2.stop_bot_recommendation.async_stop_bot_recommendation(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_lex_models_v2.types.stop_bot_recommendation_request.StopBotRecommendationRequest = {
            "bot_id": bot_id,
            "bot_version": bot_version,
            "locale_id": locale_id,
            "bot_recommendation_id": bot_recommendation_id,
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
        resource_arn: "capo_lex_models_v2.types.amazon_resource_name.AmazonResourceName",
        tags: "capo_lex_models_v2.types.tag_map.TagMap",
        *,
        config_overrides: Optional[AsyncLexModelsV2ClientConfig] = None,
    ) -> "capo_lex_models_v2.types.tag_resource_response.TagResourceResponse":
        """<p>Adds the specified tags to the specified resource. If a tag key already exists, the existing value is replaced with the new value.</p>

        Args:
            resource_arn: <p>The Amazon Resource Name (ARN) of the bot, bot alias, or bot channel to tag.</p>
            tags: <p>A list of tag keys to add to the resource. If a tag key already exists, the existing value is replaced with the new value.</p>

        Raises:
            capo_lex_models_v2.errors.internal_server_exception.InternalServerException: <p>The service encountered an unexpected condition. Try your request again.</p>
            capo_lex_models_v2.errors.resource_not_found_exception.ResourceNotFoundException: <p>You asked to describe a resource that doesn't exist. Check the resource that you are requesting and try again.</p>
            capo_lex_models_v2.errors.throttling_exception.ThrottlingException: <p>Your request rate is too high. Reduce the frequency of requests.</p>
            capo_lex_models_v2.errors.validation_exception.ValidationException: <p>One of the input parameters in your request isn't valid. Check the parameters and try your request again.</p>
            capo_lex_models_v2.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        async def _handler(
            req: "AsyncOperationRequest[capo_lex_models_v2.types.tag_resource_request.TagResourceRequest]",
        ) -> AsyncOperationResponse[
            "capo_lex_models_v2.types.tag_resource_response.TagResourceResponse"
        ]:
            import capo_lex_models_v2._operations.lex_model_building_service_v2.tag_resource

            (
                output,
                http_response,
            ) = await capo_lex_models_v2._operations.lex_model_building_service_v2.tag_resource.async_tag_resource(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_lex_models_v2.types.tag_resource_request.TagResourceRequest = {
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
        resource_arn: "capo_lex_models_v2.types.amazon_resource_name.AmazonResourceName",
        tag_keys: "capo_lex_models_v2.types.tag_key_list.TagKeyList",
        *,
        config_overrides: Optional[AsyncLexModelsV2ClientConfig] = None,
    ) -> "capo_lex_models_v2.types.untag_resource_response.UntagResourceResponse":
        """<p>Removes tags from a bot, bot alias, or bot channel.</p>

        Args:
            resource_arn: <p>The Amazon Resource Name (ARN) of the resource to remove the tags from.</p>
            tag_keys: <p>A list of tag keys to remove from the resource. If a tag key does not exist on the resource, it is ignored.</p>

        Raises:
            capo_lex_models_v2.errors.internal_server_exception.InternalServerException: <p>The service encountered an unexpected condition. Try your request again.</p>
            capo_lex_models_v2.errors.resource_not_found_exception.ResourceNotFoundException: <p>You asked to describe a resource that doesn't exist. Check the resource that you are requesting and try again.</p>
            capo_lex_models_v2.errors.throttling_exception.ThrottlingException: <p>Your request rate is too high. Reduce the frequency of requests.</p>
            capo_lex_models_v2.errors.validation_exception.ValidationException: <p>One of the input parameters in your request isn't valid. Check the parameters and try your request again.</p>
            capo_lex_models_v2.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        async def _handler(
            req: "AsyncOperationRequest[capo_lex_models_v2.types.untag_resource_request.UntagResourceRequest]",
        ) -> AsyncOperationResponse[
            "capo_lex_models_v2.types.untag_resource_response.UntagResourceResponse"
        ]:
            import capo_lex_models_v2._operations.lex_model_building_service_v2.untag_resource

            (
                output,
                http_response,
            ) = await capo_lex_models_v2._operations.lex_model_building_service_v2.untag_resource.async_untag_resource(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_lex_models_v2.types.untag_resource_request.UntagResourceRequest = {
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

    async def update_bot(
        self,
        bot_id: "capo_lex_models_v2.types.id.Id",
        bot_name: "capo_lex_models_v2.types.name.Name",
        role_arn: "capo_lex_models_v2.types.role_arn.RoleArn",
        data_privacy: "capo_lex_models_v2.types.data_privacy.DataPrivacy",
        idle_session_ttl_in_seconds: "capo_lex_models_v2.types.session_ttl.SessionTTL",
        *,
        config_overrides: Optional[AsyncLexModelsV2ClientConfig] = None,
        description: Optional[
            "capo_lex_models_v2.types.description.Description"
        ] = None,
        bot_type: Optional["capo_lex_models_v2.types.bot_type.BotType"] = None,
        bot_members: Optional["capo_lex_models_v2.types.bot_members.BotMembers"] = None,
        error_log_settings: Optional[
            "capo_lex_models_v2.types.error_log_settings.ErrorLogSettings"
        ] = None,
    ) -> "capo_lex_models_v2.types.update_bot_response.UpdateBotResponse":
        """<p>Updates the configuration of an existing bot. </p>

        Args:
            bot_id: <p>The unique identifier of the bot to update. This identifier is returned by the <a href="https://docs.aws.amazon.com/lexv2/latest/APIReference/API_CreateBot.html">CreateBot</a> operation.</p>
            bot_name: <p>The new name of the bot. The name must be unique in the account that creates the bot.</p>
            description: <p>A description of the bot.</p>
            role_arn: <p>The Amazon Resource Name (ARN) of an IAM role that has permissions to access the bot.</p>
            data_privacy: <p>Provides information on additional privacy protections Amazon Lex should use with the bot's data.</p>
            idle_session_ttl_in_seconds: <p>The time, in seconds, that Amazon Lex should keep information about a user's conversation with the bot.</p> <p>A user interaction remains active for the amount of time specified. If no conversation occurs during this time, the session expires and Amazon Lex deletes any data provided before the timeout.</p> <p>You can specify between 60 (1 minute) and 86,400 (24 hours) seconds.</p>
            bot_type: <p>The type of the bot to be updated.</p>
            bot_members: <p>The list of bot members in the network associated with the update action.</p>
            error_log_settings: <p>Allows you to modify how Amazon Lex logs errors during bot interactions, including destinations for error logs and the types of errors to be captured.</p>

        Raises:
            capo_lex_models_v2.errors.conflict_exception.ConflictException: <p>The action that you tried to perform couldn't be completed because the resource is in a conflicting state. For example, deleting a bot that is in the CREATING state. Try your request again. </p>
            capo_lex_models_v2.errors.internal_server_exception.InternalServerException: <p>The service encountered an unexpected condition. Try your request again.</p>
            capo_lex_models_v2.errors.precondition_failed_exception.PreconditionFailedException: <p>Your request couldn't be completed because one or more request fields aren't valid. Check the fields in your request and try again.</p>
            capo_lex_models_v2.errors.service_quota_exceeded_exception.ServiceQuotaExceededException: <p>You have reached a quota for your bot. </p>
            capo_lex_models_v2.errors.throttling_exception.ThrottlingException: <p>Your request rate is too high. Reduce the frequency of requests.</p>
            capo_lex_models_v2.errors.validation_exception.ValidationException: <p>One of the input parameters in your request isn't valid. Check the parameters and try your request again.</p>
            capo_lex_models_v2.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        async def _handler(
            req: "AsyncOperationRequest[capo_lex_models_v2.types.update_bot_request.UpdateBotRequest]",
        ) -> AsyncOperationResponse[
            "capo_lex_models_v2.types.update_bot_response.UpdateBotResponse"
        ]:
            import capo_lex_models_v2._operations.lex_model_building_service_v2.update_bot

            (
                output,
                http_response,
            ) = await capo_lex_models_v2._operations.lex_model_building_service_v2.update_bot.async_update_bot(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_lex_models_v2.types.update_bot_request.UpdateBotRequest = {
            "bot_id": bot_id,
            "bot_name": bot_name,
            "role_arn": role_arn,
            "data_privacy": data_privacy,
            "idle_session_ttl_in_seconds": idle_session_ttl_in_seconds,
        }
        if description is not None:
            input_["description"] = description
        if bot_type is not None:
            input_["bot_type"] = bot_type
        if bot_members is not None:
            input_["bot_members"] = bot_members
        if error_log_settings is not None:
            input_["error_log_settings"] = error_log_settings

        response = await aexecute_pipeline(
            AsyncOperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        await response.response.aclose()
        return response.output

    async def update_bot_alias(
        self,
        bot_alias_id: "capo_lex_models_v2.types.bot_alias_id.BotAliasId",
        bot_alias_name: "capo_lex_models_v2.types.name.Name",
        bot_id: "capo_lex_models_v2.types.id.Id",
        *,
        config_overrides: Optional[AsyncLexModelsV2ClientConfig] = None,
        description: Optional[
            "capo_lex_models_v2.types.description.Description"
        ] = None,
        bot_version: Optional["capo_lex_models_v2.types.bot_version.BotVersion"] = None,
        bot_alias_locale_settings: Optional[
            "capo_lex_models_v2.types.bot_alias_locale_settings_map.BotAliasLocaleSettingsMap"
        ] = None,
        conversation_log_settings: Optional[
            "capo_lex_models_v2.types.conversation_log_settings.ConversationLogSettings"
        ] = None,
        sentiment_analysis_settings: Optional[
            "capo_lex_models_v2.types.sentiment_analysis_settings.SentimentAnalysisSettings"
        ] = None,
    ) -> "capo_lex_models_v2.types.update_bot_alias_response.UpdateBotAliasResponse":
        """<p>Updates the configuration of an existing bot alias.</p>

        Args:
            bot_alias_id: <p>The unique identifier of the bot alias.</p>
            bot_alias_name: <p>The new name to assign to the bot alias.</p>
            description: <p>The new description to assign to the bot alias.</p>
            bot_version: <p>The new bot version to assign to the bot alias.</p>
            bot_alias_locale_settings: <p>The new Lambda functions to use in each locale for the bot alias.</p>
            conversation_log_settings: <p>The new settings for storing conversation logs in Amazon CloudWatch Logs and Amazon S3 buckets.</p>
            bot_id: <p>The identifier of the bot with the updated alias.</p>

        Raises:
            capo_lex_models_v2.errors.conflict_exception.ConflictException: <p>The action that you tried to perform couldn't be completed because the resource is in a conflicting state. For example, deleting a bot that is in the CREATING state. Try your request again. </p>
            capo_lex_models_v2.errors.internal_server_exception.InternalServerException: <p>The service encountered an unexpected condition. Try your request again.</p>
            capo_lex_models_v2.errors.precondition_failed_exception.PreconditionFailedException: <p>Your request couldn't be completed because one or more request fields aren't valid. Check the fields in your request and try again.</p>
            capo_lex_models_v2.errors.service_quota_exceeded_exception.ServiceQuotaExceededException: <p>You have reached a quota for your bot. </p>
            capo_lex_models_v2.errors.throttling_exception.ThrottlingException: <p>Your request rate is too high. Reduce the frequency of requests.</p>
            capo_lex_models_v2.errors.validation_exception.ValidationException: <p>One of the input parameters in your request isn't valid. Check the parameters and try your request again.</p>
            capo_lex_models_v2.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        async def _handler(
            req: "AsyncOperationRequest[capo_lex_models_v2.types.update_bot_alias_request.UpdateBotAliasRequest]",
        ) -> AsyncOperationResponse[
            "capo_lex_models_v2.types.update_bot_alias_response.UpdateBotAliasResponse"
        ]:
            import capo_lex_models_v2._operations.lex_model_building_service_v2.update_bot_alias

            (
                output,
                http_response,
            ) = await capo_lex_models_v2._operations.lex_model_building_service_v2.update_bot_alias.async_update_bot_alias(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_lex_models_v2.types.update_bot_alias_request.UpdateBotAliasRequest = {
            "bot_alias_id": bot_alias_id,
            "bot_alias_name": bot_alias_name,
            "bot_id": bot_id,
        }
        if description is not None:
            input_["description"] = description
        if bot_version is not None:
            input_["bot_version"] = bot_version
        if bot_alias_locale_settings is not None:
            input_["bot_alias_locale_settings"] = bot_alias_locale_settings
        if conversation_log_settings is not None:
            input_["conversation_log_settings"] = conversation_log_settings
        if sentiment_analysis_settings is not None:
            input_["sentiment_analysis_settings"] = sentiment_analysis_settings

        response = await aexecute_pipeline(
            AsyncOperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        await response.response.aclose()
        return response.output

    async def update_bot_locale(
        self,
        bot_id: "capo_lex_models_v2.types.id.Id",
        bot_version: "capo_lex_models_v2.types.draft_bot_version.DraftBotVersion",
        locale_id: "capo_lex_models_v2.types.locale_id.LocaleId",
        nlu_intent_confidence_threshold: "capo_lex_models_v2.types.confidence_threshold.ConfidenceThreshold",
        *,
        config_overrides: Optional[AsyncLexModelsV2ClientConfig] = None,
        description: Optional[
            "capo_lex_models_v2.types.description.Description"
        ] = None,
        voice_settings: Optional[
            "capo_lex_models_v2.types.voice_settings.VoiceSettings"
        ] = None,
        unified_speech_settings: Optional[
            "capo_lex_models_v2.types.unified_speech_settings.UnifiedSpeechSettings"
        ] = None,
        audio_filler_settings: Optional[
            "capo_lex_models_v2.types.audio_filler_settings.AudioFillerSettings"
        ] = None,
        speech_recognition_settings: Optional[
            "capo_lex_models_v2.types.speech_recognition_settings.SpeechRecognitionSettings"
        ] = None,
        generative_ai_settings: Optional[
            "capo_lex_models_v2.types.generative_ai_settings.GenerativeAISettings"
        ] = None,
        speech_detection_sensitivity: Optional[
            "capo_lex_models_v2.types.speech_detection_sensitivity.SpeechDetectionSensitivity"
        ] = None,
        speaker_diarization_settings: Optional[
            "capo_lex_models_v2.types.speaker_diarization_settings.SpeakerDiarizationSettings"
        ] = None,
    ) -> "capo_lex_models_v2.types.update_bot_locale_response.UpdateBotLocaleResponse":
        """<p>Updates the settings that a bot has for a specific locale.</p>

        Args:
            bot_id: <p>The unique identifier of the bot that contains the locale.</p>
            bot_version: <p>The version of the bot that contains the locale to be updated. The version can only be the <code>DRAFT</code> version.</p>
            locale_id: <p>The identifier of the language and locale to update. The string must match one of the supported locales. For more information, see <a href="https://docs.aws.amazon.com/lexv2/latest/dg/how-languages.html">Supported languages</a>.</p>
            description: <p>The new description of the locale.</p>
            nlu_intent_confidence_threshold: <p>The new confidence threshold where Amazon Lex inserts the <code>AMAZON.FallbackIntent</code> and <code>AMAZON.KendraSearchIntent</code> intents in the list of possible intents for an utterance.</p>
            voice_settings: <p>The new Amazon Polly voice Amazon Lex should use for voice interaction with the user.</p>
            unified_speech_settings: <p>Updated unified speech settings to apply to the bot locale.</p>
            audio_filler_settings: <p>Updated audio filler settings to apply to the bot locale. When enabled, requires <code>unifiedSpeechSettings</code> (speech-to-speech) to be configured on the bot locale.</p>
            speech_recognition_settings: <p>Updated speech-to-text settings to apply to the bot locale.</p>
            generative_ai_settings: <p>Contains settings for generative AI features powered by Amazon Bedrock for your bot locale. Use this object to turn generative AI features on and off. Pricing may differ if you turn a feature on. For more information, see LINK.</p>
            speech_detection_sensitivity: <p>The new sensitivity level for voice activity detection (VAD) in the bot locale. This setting helps optimize speech recognition accuracy by adjusting how the system responds to background noise during voice interactions.</p>
            speaker_diarization_settings: <p>The updated speaker diarization settings to apply to the bot locale. If you omit this field, Amazon Lex keeps the setting currently stored on the bot locale. To turn speaker diarization off, set <code>enabled</code> to <code>false</code> explicitly.</p>

        Raises:
            capo_lex_models_v2.errors.conflict_exception.ConflictException: <p>The action that you tried to perform couldn't be completed because the resource is in a conflicting state. For example, deleting a bot that is in the CREATING state. Try your request again. </p>
            capo_lex_models_v2.errors.internal_server_exception.InternalServerException: <p>The service encountered an unexpected condition. Try your request again.</p>
            capo_lex_models_v2.errors.precondition_failed_exception.PreconditionFailedException: <p>Your request couldn't be completed because one or more request fields aren't valid. Check the fields in your request and try again.</p>
            capo_lex_models_v2.errors.service_quota_exceeded_exception.ServiceQuotaExceededException: <p>You have reached a quota for your bot. </p>
            capo_lex_models_v2.errors.throttling_exception.ThrottlingException: <p>Your request rate is too high. Reduce the frequency of requests.</p>
            capo_lex_models_v2.errors.validation_exception.ValidationException: <p>One of the input parameters in your request isn't valid. Check the parameters and try your request again.</p>
            capo_lex_models_v2.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        async def _handler(
            req: "AsyncOperationRequest[capo_lex_models_v2.types.update_bot_locale_request.UpdateBotLocaleRequest]",
        ) -> AsyncOperationResponse[
            "capo_lex_models_v2.types.update_bot_locale_response.UpdateBotLocaleResponse"
        ]:
            import capo_lex_models_v2._operations.lex_model_building_service_v2.update_bot_locale

            (
                output,
                http_response,
            ) = await capo_lex_models_v2._operations.lex_model_building_service_v2.update_bot_locale.async_update_bot_locale(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_lex_models_v2.types.update_bot_locale_request.UpdateBotLocaleRequest = {
            "bot_id": bot_id,
            "bot_version": bot_version,
            "locale_id": locale_id,
            "nlu_intent_confidence_threshold": nlu_intent_confidence_threshold,
        }
        if description is not None:
            input_["description"] = description
        if voice_settings is not None:
            input_["voice_settings"] = voice_settings
        if unified_speech_settings is not None:
            input_["unified_speech_settings"] = unified_speech_settings
        if audio_filler_settings is not None:
            input_["audio_filler_settings"] = audio_filler_settings
        if speech_recognition_settings is not None:
            input_["speech_recognition_settings"] = speech_recognition_settings
        if generative_ai_settings is not None:
            input_["generative_ai_settings"] = generative_ai_settings
        if speech_detection_sensitivity is not None:
            input_["speech_detection_sensitivity"] = speech_detection_sensitivity
        if speaker_diarization_settings is not None:
            input_["speaker_diarization_settings"] = speaker_diarization_settings

        response = await aexecute_pipeline(
            AsyncOperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        await response.response.aclose()
        return response.output

    async def update_bot_recommendation(
        self,
        bot_id: "capo_lex_models_v2.types.id.Id",
        bot_version: "capo_lex_models_v2.types.draft_bot_version.DraftBotVersion",
        locale_id: "capo_lex_models_v2.types.locale_id.LocaleId",
        bot_recommendation_id: "capo_lex_models_v2.types.id.Id",
        encryption_setting: "capo_lex_models_v2.types.encryption_setting.EncryptionSetting",
        *,
        config_overrides: Optional[AsyncLexModelsV2ClientConfig] = None,
    ) -> "capo_lex_models_v2.types.update_bot_recommendation_response.UpdateBotRecommendationResponse":
        """<p>Updates an existing bot recommendation request.</p>

        Args:
            bot_id: <p>The unique identifier of the bot containing the bot recommendation to be updated.</p>
            bot_version: <p>The version of the bot containing the bot recommendation to be updated.</p>
            locale_id: <p>The identifier of the language and locale of the bot recommendation to update. The string must match one of the supported locales. For more information, see <a href="https://docs.aws.amazon.com/lexv2/latest/dg/how-languages.html">Supported languages</a> </p>
            bot_recommendation_id: <p>The unique identifier of the bot recommendation to be updated.</p>
            encryption_setting: <p>The object representing the passwords that will be used to encrypt the data related to the bot recommendation results, as well as the KMS key ARN used to encrypt the associated metadata.</p>

        Raises:
            capo_lex_models_v2.errors.conflict_exception.ConflictException: <p>The action that you tried to perform couldn't be completed because the resource is in a conflicting state. For example, deleting a bot that is in the CREATING state. Try your request again. </p>
            capo_lex_models_v2.errors.internal_server_exception.InternalServerException: <p>The service encountered an unexpected condition. Try your request again.</p>
            capo_lex_models_v2.errors.precondition_failed_exception.PreconditionFailedException: <p>Your request couldn't be completed because one or more request fields aren't valid. Check the fields in your request and try again.</p>
            capo_lex_models_v2.errors.resource_not_found_exception.ResourceNotFoundException: <p>You asked to describe a resource that doesn't exist. Check the resource that you are requesting and try again.</p>
            capo_lex_models_v2.errors.service_quota_exceeded_exception.ServiceQuotaExceededException: <p>You have reached a quota for your bot. </p>
            capo_lex_models_v2.errors.throttling_exception.ThrottlingException: <p>Your request rate is too high. Reduce the frequency of requests.</p>
            capo_lex_models_v2.errors.validation_exception.ValidationException: <p>One of the input parameters in your request isn't valid. Check the parameters and try your request again.</p>
            capo_lex_models_v2.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        async def _handler(
            req: "AsyncOperationRequest[capo_lex_models_v2.types.update_bot_recommendation_request.UpdateBotRecommendationRequest]",
        ) -> AsyncOperationResponse[
            "capo_lex_models_v2.types.update_bot_recommendation_response.UpdateBotRecommendationResponse"
        ]:
            import capo_lex_models_v2._operations.lex_model_building_service_v2.update_bot_recommendation

            (
                output,
                http_response,
            ) = await capo_lex_models_v2._operations.lex_model_building_service_v2.update_bot_recommendation.async_update_bot_recommendation(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_lex_models_v2.types.update_bot_recommendation_request.UpdateBotRecommendationRequest = {
            "bot_id": bot_id,
            "bot_version": bot_version,
            "locale_id": locale_id,
            "bot_recommendation_id": bot_recommendation_id,
            "encryption_setting": encryption_setting,
        }

        response = await aexecute_pipeline(
            AsyncOperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        await response.response.aclose()
        return response.output

    async def update_export(
        self,
        export_id: "capo_lex_models_v2.types.id.Id",
        *,
        config_overrides: Optional[AsyncLexModelsV2ClientConfig] = None,
        file_password: Optional[
            "capo_lex_models_v2.types.import_export_file_password.ImportExportFilePassword"
        ] = None,
    ) -> "capo_lex_models_v2.types.update_export_response.UpdateExportResponse":
        """<p>Updates the password used to protect an export zip archive.</p> <p>The password is not required. If you don't supply a password, Amazon Lex generates a zip file that is not protected by a password. This is the archive that is available at the pre-signed S3 URL provided by the <a href="https://docs.aws.amazon.com/lexv2/latest/APIReference/API_DescribeExport.html">DescribeExport</a> operation.</p>

        Args:
            export_id: <p>The unique identifier Amazon Lex assigned to the export.</p>
            file_password: <p>The new password to use to encrypt the export zip archive.</p>

        Raises:
            capo_lex_models_v2.errors.conflict_exception.ConflictException: <p>The action that you tried to perform couldn't be completed because the resource is in a conflicting state. For example, deleting a bot that is in the CREATING state. Try your request again. </p>
            capo_lex_models_v2.errors.internal_server_exception.InternalServerException: <p>The service encountered an unexpected condition. Try your request again.</p>
            capo_lex_models_v2.errors.resource_not_found_exception.ResourceNotFoundException: <p>You asked to describe a resource that doesn't exist. Check the resource that you are requesting and try again.</p>
            capo_lex_models_v2.errors.service_quota_exceeded_exception.ServiceQuotaExceededException: <p>You have reached a quota for your bot. </p>
            capo_lex_models_v2.errors.throttling_exception.ThrottlingException: <p>Your request rate is too high. Reduce the frequency of requests.</p>
            capo_lex_models_v2.errors.validation_exception.ValidationException: <p>One of the input parameters in your request isn't valid. Check the parameters and try your request again.</p>
            capo_lex_models_v2.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        async def _handler(
            req: "AsyncOperationRequest[capo_lex_models_v2.types.update_export_request.UpdateExportRequest]",
        ) -> AsyncOperationResponse[
            "capo_lex_models_v2.types.update_export_response.UpdateExportResponse"
        ]:
            import capo_lex_models_v2._operations.lex_model_building_service_v2.update_export

            (
                output,
                http_response,
            ) = await capo_lex_models_v2._operations.lex_model_building_service_v2.update_export.async_update_export(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_lex_models_v2.types.update_export_request.UpdateExportRequest = {
            "export_id": export_id
        }
        if file_password is not None:
            input_["file_password"] = file_password

        response = await aexecute_pipeline(
            AsyncOperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        await response.response.aclose()
        return response.output

    async def update_intent(
        self,
        intent_id: "capo_lex_models_v2.types.id.Id",
        intent_name: "capo_lex_models_v2.types.name.Name",
        bot_id: "capo_lex_models_v2.types.id.Id",
        bot_version: "capo_lex_models_v2.types.draft_bot_version.DraftBotVersion",
        locale_id: "capo_lex_models_v2.types.locale_id.LocaleId",
        *,
        config_overrides: Optional[AsyncLexModelsV2ClientConfig] = None,
        intent_display_name: Optional[
            "capo_lex_models_v2.types.display_name.DisplayName"
        ] = None,
        description: Optional[
            "capo_lex_models_v2.types.description.Description"
        ] = None,
        parent_intent_signature: Optional[
            "capo_lex_models_v2.types.intent_signature.IntentSignature"
        ] = None,
        sample_utterances: Optional[
            "capo_lex_models_v2.types.sample_utterances_list.SampleUtterancesList"
        ] = None,
        dialog_code_hook: Optional[
            "capo_lex_models_v2.types.dialog_code_hook_settings.DialogCodeHookSettings"
        ] = None,
        fulfillment_code_hook: Optional[
            "capo_lex_models_v2.types.fulfillment_code_hook_settings.FulfillmentCodeHookSettings"
        ] = None,
        slot_priorities: Optional[
            "capo_lex_models_v2.types.slot_priorities_list.SlotPrioritiesList"
        ] = None,
        intent_confirmation_setting: Optional[
            "capo_lex_models_v2.types.intent_confirmation_setting.IntentConfirmationSetting"
        ] = None,
        intent_closing_setting: Optional[
            "capo_lex_models_v2.types.intent_closing_setting.IntentClosingSetting"
        ] = None,
        input_contexts: Optional[
            "capo_lex_models_v2.types.input_contexts_list.InputContextsList"
        ] = None,
        output_contexts: Optional[
            "capo_lex_models_v2.types.output_contexts_list.OutputContextsList"
        ] = None,
        kendra_configuration: Optional[
            "capo_lex_models_v2.types.kendra_configuration.KendraConfiguration"
        ] = None,
        initial_response_setting: Optional[
            "capo_lex_models_v2.types.initial_response_setting.InitialResponseSetting"
        ] = None,
        qn_a_intent_configuration: Optional[
            "capo_lex_models_v2.types.qn_a_intent_configuration.QnAIntentConfiguration"
        ] = None,
        q_in_connect_intent_configuration: Optional[
            "capo_lex_models_v2.types.q_in_connect_intent_configuration.QInConnectIntentConfiguration"
        ] = None,
    ) -> "capo_lex_models_v2.types.update_intent_response.UpdateIntentResponse":
        """<p>Updates the settings for an intent.</p>

        Args:
            intent_id: <p>The unique identifier of the intent to update.</p>
            intent_name: <p>The new name for the intent.</p>
            intent_display_name: <p>The new display name for the intent.</p>
            description: <p>The new description of the intent.</p>
            parent_intent_signature: <p>The signature of the new built-in intent to use as the parent of this intent.</p>
            sample_utterances: <p>New utterances used to invoke the intent.</p>
            dialog_code_hook: <p>The new Lambda function to use between each turn of the conversation with the bot.</p>
            fulfillment_code_hook: <p>The new Lambda function to call when all of the intents required slots are provided and the intent is ready for fulfillment.</p>
            slot_priorities: <p>A new list of slots and their priorities that are contained by the intent.</p>
            intent_confirmation_setting: <p>New prompts that Amazon Lex sends to the user to confirm the completion of an intent.</p>
            intent_closing_setting: <p>The new response that Amazon Lex sends the user when the intent is closed.</p>
            input_contexts: <p>A new list of contexts that must be active in order for Amazon Lex to consider the intent.</p>
            output_contexts: <p>A new list of contexts that Amazon Lex activates when the intent is fulfilled.</p>
            kendra_configuration: <p>New configuration settings for connecting to an Amazon Kendra index.</p>
            bot_id: <p>The identifier of the bot that contains the intent.</p>
            bot_version: <p>The version of the bot that contains the intent. Must be <code>DRAFT</code>.</p>
            locale_id: <p>The identifier of the language and locale where this intent is used. The string must match one of the supported locales. For more information, see <a href="https://docs.aws.amazon.com/lexv2/latest/dg/how-languages.html">Supported languages</a>.</p>
            initial_response_setting: <p>Configuration settings for a response sent to the user before Amazon Lex starts eliciting slots.</p>
            qn_a_intent_configuration: <p>Specifies the configuration of the built-in <code>Amazon.QnAIntent</code>. The <code>AMAZON.QnAIntent</code> intent is called when Amazon Lex can't determine another intent to invoke. If you specify this field, you can't specify the <code>kendraConfiguration</code> field.</p>
            q_in_connect_intent_configuration: <p>Qinconnect intent configuration details for the update intent request.</p>

        Raises:
            capo_lex_models_v2.errors.conflict_exception.ConflictException: <p>The action that you tried to perform couldn't be completed because the resource is in a conflicting state. For example, deleting a bot that is in the CREATING state. Try your request again. </p>
            capo_lex_models_v2.errors.internal_server_exception.InternalServerException: <p>The service encountered an unexpected condition. Try your request again.</p>
            capo_lex_models_v2.errors.precondition_failed_exception.PreconditionFailedException: <p>Your request couldn't be completed because one or more request fields aren't valid. Check the fields in your request and try again.</p>
            capo_lex_models_v2.errors.service_quota_exceeded_exception.ServiceQuotaExceededException: <p>You have reached a quota for your bot. </p>
            capo_lex_models_v2.errors.throttling_exception.ThrottlingException: <p>Your request rate is too high. Reduce the frequency of requests.</p>
            capo_lex_models_v2.errors.validation_exception.ValidationException: <p>One of the input parameters in your request isn't valid. Check the parameters and try your request again.</p>
            capo_lex_models_v2.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        async def _handler(
            req: "AsyncOperationRequest[capo_lex_models_v2.types.update_intent_request.UpdateIntentRequest]",
        ) -> AsyncOperationResponse[
            "capo_lex_models_v2.types.update_intent_response.UpdateIntentResponse"
        ]:
            import capo_lex_models_v2._operations.lex_model_building_service_v2.update_intent

            (
                output,
                http_response,
            ) = await capo_lex_models_v2._operations.lex_model_building_service_v2.update_intent.async_update_intent(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_lex_models_v2.types.update_intent_request.UpdateIntentRequest = {
            "intent_id": intent_id,
            "intent_name": intent_name,
            "bot_id": bot_id,
            "bot_version": bot_version,
            "locale_id": locale_id,
        }
        if intent_display_name is not None:
            input_["intent_display_name"] = intent_display_name
        if description is not None:
            input_["description"] = description
        if parent_intent_signature is not None:
            input_["parent_intent_signature"] = parent_intent_signature
        if sample_utterances is not None:
            input_["sample_utterances"] = sample_utterances
        if dialog_code_hook is not None:
            input_["dialog_code_hook"] = dialog_code_hook
        if fulfillment_code_hook is not None:
            input_["fulfillment_code_hook"] = fulfillment_code_hook
        if slot_priorities is not None:
            input_["slot_priorities"] = slot_priorities
        if intent_confirmation_setting is not None:
            input_["intent_confirmation_setting"] = intent_confirmation_setting
        if intent_closing_setting is not None:
            input_["intent_closing_setting"] = intent_closing_setting
        if input_contexts is not None:
            input_["input_contexts"] = input_contexts
        if output_contexts is not None:
            input_["output_contexts"] = output_contexts
        if kendra_configuration is not None:
            input_["kendra_configuration"] = kendra_configuration
        if initial_response_setting is not None:
            input_["initial_response_setting"] = initial_response_setting
        if qn_a_intent_configuration is not None:
            input_["qn_a_intent_configuration"] = qn_a_intent_configuration
        if q_in_connect_intent_configuration is not None:
            input_["q_in_connect_intent_configuration"] = (
                q_in_connect_intent_configuration
            )

        response = await aexecute_pipeline(
            AsyncOperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        await response.response.aclose()
        return response.output

    async def update_resource_policy(
        self,
        resource_arn: "capo_lex_models_v2.types.amazon_resource_name.AmazonResourceName",
        policy: "capo_lex_models_v2.types.policy.Policy",
        *,
        config_overrides: Optional[AsyncLexModelsV2ClientConfig] = None,
        expected_revision_id: Optional[
            "capo_lex_models_v2.types.revision_id.RevisionId"
        ] = None,
    ) -> "capo_lex_models_v2.types.update_resource_policy_response.UpdateResourcePolicyResponse":
        """<p>Replaces the existing resource policy for a bot or bot alias with a new one. If the policy doesn't exist, Amazon Lex returns an exception.</p>

        Args:
            resource_arn: <p>The Amazon Resource Name (ARN) of the bot or bot alias that the resource policy is attached to.</p>
            policy: <p>A resource policy to add to the resource. The policy is a JSON structure that contains one or more statements that define the policy. The policy must follow the IAM syntax. For more information about the contents of a JSON policy document, see <a href="https://docs.aws.amazon.com/IAM/latest/UserGuide/reference_policies.html"> IAM JSON policy reference </a>. </p> <p>If the policy isn't valid, Amazon Lex returns a validation exception.</p>
            expected_revision_id: <p>The identifier of the revision of the policy to update. If this revision ID doesn't match the current revision ID, Amazon Lex throws an exception.</p> <p>If you don't specify a revision, Amazon Lex overwrites the contents of the policy with the new values.</p>

        Raises:
            capo_lex_models_v2.errors.internal_server_exception.InternalServerException: <p>The service encountered an unexpected condition. Try your request again.</p>
            capo_lex_models_v2.errors.precondition_failed_exception.PreconditionFailedException: <p>Your request couldn't be completed because one or more request fields aren't valid. Check the fields in your request and try again.</p>
            capo_lex_models_v2.errors.resource_not_found_exception.ResourceNotFoundException: <p>You asked to describe a resource that doesn't exist. Check the resource that you are requesting and try again.</p>
            capo_lex_models_v2.errors.service_quota_exceeded_exception.ServiceQuotaExceededException: <p>You have reached a quota for your bot. </p>
            capo_lex_models_v2.errors.throttling_exception.ThrottlingException: <p>Your request rate is too high. Reduce the frequency of requests.</p>
            capo_lex_models_v2.errors.validation_exception.ValidationException: <p>One of the input parameters in your request isn't valid. Check the parameters and try your request again.</p>
            capo_lex_models_v2.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        async def _handler(
            req: "AsyncOperationRequest[capo_lex_models_v2.types.update_resource_policy_request.UpdateResourcePolicyRequest]",
        ) -> AsyncOperationResponse[
            "capo_lex_models_v2.types.update_resource_policy_response.UpdateResourcePolicyResponse"
        ]:
            import capo_lex_models_v2._operations.lex_model_building_service_v2.update_resource_policy

            (
                output,
                http_response,
            ) = await capo_lex_models_v2._operations.lex_model_building_service_v2.update_resource_policy.async_update_resource_policy(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_lex_models_v2.types.update_resource_policy_request.UpdateResourcePolicyRequest = {
            "resource_arn": resource_arn,
            "policy": policy,
        }
        if expected_revision_id is not None:
            input_["expected_revision_id"] = expected_revision_id

        response = await aexecute_pipeline(
            AsyncOperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        await response.response.aclose()
        return response.output

    async def update_slot(
        self,
        slot_id: "capo_lex_models_v2.types.id.Id",
        slot_name: "capo_lex_models_v2.types.name.Name",
        value_elicitation_setting: "capo_lex_models_v2.types.slot_value_elicitation_setting.SlotValueElicitationSetting",
        bot_id: "capo_lex_models_v2.types.id.Id",
        bot_version: "capo_lex_models_v2.types.draft_bot_version.DraftBotVersion",
        locale_id: "capo_lex_models_v2.types.locale_id.LocaleId",
        intent_id: "capo_lex_models_v2.types.id.Id",
        *,
        config_overrides: Optional[AsyncLexModelsV2ClientConfig] = None,
        description: Optional[
            "capo_lex_models_v2.types.description.Description"
        ] = None,
        slot_type_id: Optional[
            "capo_lex_models_v2.types.built_in_or_custom_slot_type_id.BuiltInOrCustomSlotTypeId"
        ] = None,
        obfuscation_setting: Optional[
            "capo_lex_models_v2.types.obfuscation_setting.ObfuscationSetting"
        ] = None,
        multiple_values_setting: Optional[
            "capo_lex_models_v2.types.multiple_values_setting.MultipleValuesSetting"
        ] = None,
        sub_slot_setting: Optional[
            "capo_lex_models_v2.types.sub_slot_setting.SubSlotSetting"
        ] = None,
    ) -> "capo_lex_models_v2.types.update_slot_response.UpdateSlotResponse":
        """<p>Updates the settings for a slot.</p>

        Args:
            slot_id: <p>The unique identifier for the slot to update.</p>
            slot_name: <p>The new name for the slot.</p>
            description: <p>The new description for the slot.</p>
            slot_type_id: <p>The unique identifier of the new slot type to associate with this slot. </p>
            value_elicitation_setting: <p>A new set of prompts that Amazon Lex sends to the user to elicit a response the provides a value for the slot.</p>
            obfuscation_setting: <p>New settings that determine how slot values are formatted in Amazon CloudWatch logs. </p>
            bot_id: <p>The unique identifier of the bot that contains the slot.</p>
            bot_version: <p>The version of the bot that contains the slot. Must always be <code>DRAFT</code>.</p>
            locale_id: <p>The identifier of the language and locale that contains the slot. The string must match one of the supported locales. For more information, see <a href="https://docs.aws.amazon.com/lexv2/latest/dg/how-languages.html">Supported languages</a>.</p>
            intent_id: <p>The identifier of the intent that contains the slot.</p>
            multiple_values_setting: <p>Determines whether the slot accepts multiple values in one response. Multiple value slots are only available in the en-US locale. If you set this value to <code>true</code> in any other locale, Amazon Lex throws a <code>ValidationException</code>.</p> <p>If the <code>multipleValuesSetting</code> is not set, the default value is <code>false</code>.</p>
            sub_slot_setting: <p>Specifications for the constituent sub slots and the expression for the composite slot.</p>

        Raises:
            capo_lex_models_v2.errors.conflict_exception.ConflictException: <p>The action that you tried to perform couldn't be completed because the resource is in a conflicting state. For example, deleting a bot that is in the CREATING state. Try your request again. </p>
            capo_lex_models_v2.errors.internal_server_exception.InternalServerException: <p>The service encountered an unexpected condition. Try your request again.</p>
            capo_lex_models_v2.errors.precondition_failed_exception.PreconditionFailedException: <p>Your request couldn't be completed because one or more request fields aren't valid. Check the fields in your request and try again.</p>
            capo_lex_models_v2.errors.service_quota_exceeded_exception.ServiceQuotaExceededException: <p>You have reached a quota for your bot. </p>
            capo_lex_models_v2.errors.throttling_exception.ThrottlingException: <p>Your request rate is too high. Reduce the frequency of requests.</p>
            capo_lex_models_v2.errors.validation_exception.ValidationException: <p>One of the input parameters in your request isn't valid. Check the parameters and try your request again.</p>
            capo_lex_models_v2.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        async def _handler(
            req: "AsyncOperationRequest[capo_lex_models_v2.types.update_slot_request.UpdateSlotRequest]",
        ) -> AsyncOperationResponse[
            "capo_lex_models_v2.types.update_slot_response.UpdateSlotResponse"
        ]:
            import capo_lex_models_v2._operations.lex_model_building_service_v2.update_slot

            (
                output,
                http_response,
            ) = await capo_lex_models_v2._operations.lex_model_building_service_v2.update_slot.async_update_slot(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_lex_models_v2.types.update_slot_request.UpdateSlotRequest = {
            "slot_id": slot_id,
            "slot_name": slot_name,
            "value_elicitation_setting": value_elicitation_setting,
            "bot_id": bot_id,
            "bot_version": bot_version,
            "locale_id": locale_id,
            "intent_id": intent_id,
        }
        if description is not None:
            input_["description"] = description
        if slot_type_id is not None:
            input_["slot_type_id"] = slot_type_id
        if obfuscation_setting is not None:
            input_["obfuscation_setting"] = obfuscation_setting
        if multiple_values_setting is not None:
            input_["multiple_values_setting"] = multiple_values_setting
        if sub_slot_setting is not None:
            input_["sub_slot_setting"] = sub_slot_setting

        response = await aexecute_pipeline(
            AsyncOperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        await response.response.aclose()
        return response.output

    async def update_slot_type(
        self,
        slot_type_id: "capo_lex_models_v2.types.id.Id",
        slot_type_name: "capo_lex_models_v2.types.name.Name",
        bot_id: "capo_lex_models_v2.types.id.Id",
        bot_version: "capo_lex_models_v2.types.draft_bot_version.DraftBotVersion",
        locale_id: "capo_lex_models_v2.types.locale_id.LocaleId",
        *,
        config_overrides: Optional[AsyncLexModelsV2ClientConfig] = None,
        description: Optional[
            "capo_lex_models_v2.types.description.Description"
        ] = None,
        slot_type_values: Optional[
            "capo_lex_models_v2.types.slot_type_values.SlotTypeValues"
        ] = None,
        value_selection_setting: Optional[
            "capo_lex_models_v2.types.slot_value_selection_setting.SlotValueSelectionSetting"
        ] = None,
        parent_slot_type_signature: Optional[
            "capo_lex_models_v2.types.slot_type_signature.SlotTypeSignature"
        ] = None,
        external_source_setting: Optional[
            "capo_lex_models_v2.types.external_source_setting.ExternalSourceSetting"
        ] = None,
        composite_slot_type_setting: Optional[
            "capo_lex_models_v2.types.composite_slot_type_setting.CompositeSlotTypeSetting"
        ] = None,
    ) -> "capo_lex_models_v2.types.update_slot_type_response.UpdateSlotTypeResponse":
        """<p>Updates the configuration of an existing slot type.</p>

        Args:
            slot_type_id: <p>The unique identifier of the slot type to update.</p>
            slot_type_name: <p>The new name of the slot type.</p>
            description: <p>The new description of the slot type.</p>
            slot_type_values: <p>A new list of values and their optional synonyms that define the values that the slot type can take.</p>
            value_selection_setting: <p>The strategy that Amazon Lex should use when deciding on a value from the list of slot type values.</p>
            parent_slot_type_signature: <p>The new built-in slot type that should be used as the parent of this slot type.</p>
            bot_id: <p>The identifier of the bot that contains the slot type.</p>
            bot_version: <p>The version of the bot that contains the slot type. Must be <code>DRAFT</code>.</p>
            locale_id: <p>The identifier of the language and locale that contains the slot type. The string must match one of the supported locales. For more information, see <a href="https://docs.aws.amazon.com/lexv2/latest/dg/how-languages.html">Supported languages</a>.</p>
            composite_slot_type_setting: <p>Specifications for a composite slot type.</p>

        Raises:
            capo_lex_models_v2.errors.conflict_exception.ConflictException: <p>The action that you tried to perform couldn't be completed because the resource is in a conflicting state. For example, deleting a bot that is in the CREATING state. Try your request again. </p>
            capo_lex_models_v2.errors.internal_server_exception.InternalServerException: <p>The service encountered an unexpected condition. Try your request again.</p>
            capo_lex_models_v2.errors.precondition_failed_exception.PreconditionFailedException: <p>Your request couldn't be completed because one or more request fields aren't valid. Check the fields in your request and try again.</p>
            capo_lex_models_v2.errors.service_quota_exceeded_exception.ServiceQuotaExceededException: <p>You have reached a quota for your bot. </p>
            capo_lex_models_v2.errors.throttling_exception.ThrottlingException: <p>Your request rate is too high. Reduce the frequency of requests.</p>
            capo_lex_models_v2.errors.validation_exception.ValidationException: <p>One of the input parameters in your request isn't valid. Check the parameters and try your request again.</p>
            capo_lex_models_v2.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        async def _handler(
            req: "AsyncOperationRequest[capo_lex_models_v2.types.update_slot_type_request.UpdateSlotTypeRequest]",
        ) -> AsyncOperationResponse[
            "capo_lex_models_v2.types.update_slot_type_response.UpdateSlotTypeResponse"
        ]:
            import capo_lex_models_v2._operations.lex_model_building_service_v2.update_slot_type

            (
                output,
                http_response,
            ) = await capo_lex_models_v2._operations.lex_model_building_service_v2.update_slot_type.async_update_slot_type(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_lex_models_v2.types.update_slot_type_request.UpdateSlotTypeRequest = {
            "slot_type_id": slot_type_id,
            "slot_type_name": slot_type_name,
            "bot_id": bot_id,
            "bot_version": bot_version,
            "locale_id": locale_id,
        }
        if description is not None:
            input_["description"] = description
        if slot_type_values is not None:
            input_["slot_type_values"] = slot_type_values
        if value_selection_setting is not None:
            input_["value_selection_setting"] = value_selection_setting
        if parent_slot_type_signature is not None:
            input_["parent_slot_type_signature"] = parent_slot_type_signature
        if external_source_setting is not None:
            input_["external_source_setting"] = external_source_setting
        if composite_slot_type_setting is not None:
            input_["composite_slot_type_setting"] = composite_slot_type_setting

        response = await aexecute_pipeline(
            AsyncOperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        await response.response.aclose()
        return response.output

    async def update_test_set(
        self,
        test_set_id: "capo_lex_models_v2.types.id.Id",
        test_set_name: "capo_lex_models_v2.types.name.Name",
        *,
        config_overrides: Optional[AsyncLexModelsV2ClientConfig] = None,
        description: Optional[
            "capo_lex_models_v2.types.description.Description"
        ] = None,
    ) -> "capo_lex_models_v2.types.update_test_set_response.UpdateTestSetResponse":
        """<p>The action to update the test set.</p>

        Args:
            test_set_id: <p>The test set Id for which update test operation to be performed.</p>
            test_set_name: <p>The new test set name.</p>
            description: <p>The new test set description.</p>

        Raises:
            capo_lex_models_v2.errors.conflict_exception.ConflictException: <p>The action that you tried to perform couldn't be completed because the resource is in a conflicting state. For example, deleting a bot that is in the CREATING state. Try your request again. </p>
            capo_lex_models_v2.errors.internal_server_exception.InternalServerException: <p>The service encountered an unexpected condition. Try your request again.</p>
            capo_lex_models_v2.errors.precondition_failed_exception.PreconditionFailedException: <p>Your request couldn't be completed because one or more request fields aren't valid. Check the fields in your request and try again.</p>
            capo_lex_models_v2.errors.service_quota_exceeded_exception.ServiceQuotaExceededException: <p>You have reached a quota for your bot. </p>
            capo_lex_models_v2.errors.throttling_exception.ThrottlingException: <p>Your request rate is too high. Reduce the frequency of requests.</p>
            capo_lex_models_v2.errors.validation_exception.ValidationException: <p>One of the input parameters in your request isn't valid. Check the parameters and try your request again.</p>
            capo_lex_models_v2.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        async def _handler(
            req: "AsyncOperationRequest[capo_lex_models_v2.types.update_test_set_request.UpdateTestSetRequest]",
        ) -> AsyncOperationResponse[
            "capo_lex_models_v2.types.update_test_set_response.UpdateTestSetResponse"
        ]:
            import capo_lex_models_v2._operations.lex_model_building_service_v2.update_test_set

            (
                output,
                http_response,
            ) = await capo_lex_models_v2._operations.lex_model_building_service_v2.update_test_set.async_update_test_set(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_lex_models_v2.types.update_test_set_request.UpdateTestSetRequest = {
            "test_set_id": test_set_id,
            "test_set_name": test_set_name,
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

    async def __aenter__(self) -> Self:
        return self

    async def __aexit__(self, exc_type: Any, exc: Any, tb: Any):
        await self._client.aclose()
