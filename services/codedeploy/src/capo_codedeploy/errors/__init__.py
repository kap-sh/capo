from __future__ import annotations

from ._base import (
    CodeDeployError as CodeDeployError,
)
from ._base import (
    DeserializationError as DeserializationError,
)
from ._base import (
    SerializationError as SerializationError,
)
from ._base import (
    ServiceError as ServiceError,
)
from ._base import (
    UnknownServiceError as UnknownServiceError,
)
from ._base import (
    WaiterFailedError as WaiterFailedError,
)
from ._base import (
    WaiterTimeoutError as WaiterTimeoutError,
)
from .alarms_limit_exceeded_exception import (
    AlarmsLimitExceededException as AlarmsLimitExceededException,
)
from .application_already_exists_exception import (
    ApplicationAlreadyExistsException as ApplicationAlreadyExistsException,
)
from .application_does_not_exist_exception import (
    ApplicationDoesNotExistException as ApplicationDoesNotExistException,
)
from .application_limit_exceeded_exception import (
    ApplicationLimitExceededException as ApplicationLimitExceededException,
)
from .application_name_required_exception import (
    ApplicationNameRequiredException as ApplicationNameRequiredException,
)
from .arn_not_supported_exception import (
    ArnNotSupportedException as ArnNotSupportedException,
)
from .batch_limit_exceeded_exception import (
    BatchLimitExceededException as BatchLimitExceededException,
)
from .bucket_name_filter_required_exception import (
    BucketNameFilterRequiredException as BucketNameFilterRequiredException,
)
from .deployment_already_completed_exception import (
    DeploymentAlreadyCompletedException as DeploymentAlreadyCompletedException,
)
from .deployment_config_already_exists_exception import (
    DeploymentConfigAlreadyExistsException as DeploymentConfigAlreadyExistsException,
)
from .deployment_config_does_not_exist_exception import (
    DeploymentConfigDoesNotExistException as DeploymentConfigDoesNotExistException,
)
from .deployment_config_in_use_exception import (
    DeploymentConfigInUseException as DeploymentConfigInUseException,
)
from .deployment_config_limit_exceeded_exception import (
    DeploymentConfigLimitExceededException as DeploymentConfigLimitExceededException,
)
from .deployment_config_name_required_exception import (
    DeploymentConfigNameRequiredException as DeploymentConfigNameRequiredException,
)
from .deployment_does_not_exist_exception import (
    DeploymentDoesNotExistException as DeploymentDoesNotExistException,
)
from .deployment_group_already_exists_exception import (
    DeploymentGroupAlreadyExistsException as DeploymentGroupAlreadyExistsException,
)
from .deployment_group_does_not_exist_exception import (
    DeploymentGroupDoesNotExistException as DeploymentGroupDoesNotExistException,
)
from .deployment_group_limit_exceeded_exception import (
    DeploymentGroupLimitExceededException as DeploymentGroupLimitExceededException,
)
from .deployment_group_name_required_exception import (
    DeploymentGroupNameRequiredException as DeploymentGroupNameRequiredException,
)
from .deployment_id_required_exception import (
    DeploymentIdRequiredException as DeploymentIdRequiredException,
)
from .deployment_is_not_in_ready_state_exception import (
    DeploymentIsNotInReadyStateException as DeploymentIsNotInReadyStateException,
)
from .deployment_limit_exceeded_exception import (
    DeploymentLimitExceededException as DeploymentLimitExceededException,
)
from .deployment_not_started_exception import (
    DeploymentNotStartedException as DeploymentNotStartedException,
)
from .deployment_target_does_not_exist_exception import (
    DeploymentTargetDoesNotExistException as DeploymentTargetDoesNotExistException,
)
from .deployment_target_id_required_exception import (
    DeploymentTargetIdRequiredException as DeploymentTargetIdRequiredException,
)
from .deployment_target_list_size_exceeded_exception import (
    DeploymentTargetListSizeExceededException as DeploymentTargetListSizeExceededException,
)
from .description_too_long_exception import (
    DescriptionTooLongException as DescriptionTooLongException,
)
from .ecs_service_mapping_limit_exceeded_exception import (
    ECSServiceMappingLimitExceededException as ECSServiceMappingLimitExceededException,
)
from .git_hub_account_token_does_not_exist_exception import (
    GitHubAccountTokenDoesNotExistException as GitHubAccountTokenDoesNotExistException,
)
from .git_hub_account_token_name_required_exception import (
    GitHubAccountTokenNameRequiredException as GitHubAccountTokenNameRequiredException,
)
from .iam_arn_required_exception import (
    IamArnRequiredException as IamArnRequiredException,
)
from .iam_session_arn_already_registered_exception import (
    IamSessionArnAlreadyRegisteredException as IamSessionArnAlreadyRegisteredException,
)
from .iam_user_arn_already_registered_exception import (
    IamUserArnAlreadyRegisteredException as IamUserArnAlreadyRegisteredException,
)
from .iam_user_arn_required_exception import (
    IamUserArnRequiredException as IamUserArnRequiredException,
)
from .instance_does_not_exist_exception import (
    InstanceDoesNotExistException as InstanceDoesNotExistException,
)
from .instance_id_required_exception import (
    InstanceIdRequiredException as InstanceIdRequiredException,
)
from .instance_limit_exceeded_exception import (
    InstanceLimitExceededException as InstanceLimitExceededException,
)
from .instance_name_already_registered_exception import (
    InstanceNameAlreadyRegisteredException as InstanceNameAlreadyRegisteredException,
)
from .instance_name_required_exception import (
    InstanceNameRequiredException as InstanceNameRequiredException,
)
from .instance_not_registered_exception import (
    InstanceNotRegisteredException as InstanceNotRegisteredException,
)
from .invalid_alarm_config_exception import (
    InvalidAlarmConfigException as InvalidAlarmConfigException,
)
from .invalid_application_name_exception import (
    InvalidApplicationNameException as InvalidApplicationNameException,
)
from .invalid_arn_exception import InvalidArnException as InvalidArnException
from .invalid_auto_rollback_config_exception import (
    InvalidAutoRollbackConfigException as InvalidAutoRollbackConfigException,
)
from .invalid_auto_scaling_group_exception import (
    InvalidAutoScalingGroupException as InvalidAutoScalingGroupException,
)
from .invalid_auto_scaling_group_process_to_suspend_exception import (
    InvalidAutoScalingGroupProcessToSuspendException as InvalidAutoScalingGroupProcessToSuspendException,
)
from .invalid_blue_green_deployment_configuration_exception import (
    InvalidBlueGreenDeploymentConfigurationException as InvalidBlueGreenDeploymentConfigurationException,
)
from .invalid_bucket_name_filter_exception import (
    InvalidBucketNameFilterException as InvalidBucketNameFilterException,
)
from .invalid_compute_platform_exception import (
    InvalidComputePlatformException as InvalidComputePlatformException,
)
from .invalid_deployed_state_filter_exception import (
    InvalidDeployedStateFilterException as InvalidDeployedStateFilterException,
)
from .invalid_deployment_config_name_exception import (
    InvalidDeploymentConfigNameException as InvalidDeploymentConfigNameException,
)
from .invalid_deployment_group_name_exception import (
    InvalidDeploymentGroupNameException as InvalidDeploymentGroupNameException,
)
from .invalid_deployment_id_exception import (
    InvalidDeploymentIdException as InvalidDeploymentIdException,
)
from .invalid_deployment_instance_type_exception import (
    InvalidDeploymentInstanceTypeException as InvalidDeploymentInstanceTypeException,
)
from .invalid_deployment_status_exception import (
    InvalidDeploymentStatusException as InvalidDeploymentStatusException,
)
from .invalid_deployment_style_exception import (
    InvalidDeploymentStyleException as InvalidDeploymentStyleException,
)
from .invalid_deployment_target_id_exception import (
    InvalidDeploymentTargetIdException as InvalidDeploymentTargetIdException,
)
from .invalid_deployment_wait_type_exception import (
    InvalidDeploymentWaitTypeException as InvalidDeploymentWaitTypeException,
)
from .invalid_ec2_tag_combination_exception import (
    InvalidEC2TagCombinationException as InvalidEC2TagCombinationException,
)
from .invalid_ec2_tag_exception import InvalidEC2TagException as InvalidEC2TagException
from .invalid_ecs_service_exception import (
    InvalidECSServiceException as InvalidECSServiceException,
)
from .invalid_external_id_exception import (
    InvalidExternalIdException as InvalidExternalIdException,
)
from .invalid_file_exists_behavior_exception import (
    InvalidFileExistsBehaviorException as InvalidFileExistsBehaviorException,
)
from .invalid_git_hub_account_token_exception import (
    InvalidGitHubAccountTokenException as InvalidGitHubAccountTokenException,
)
from .invalid_git_hub_account_token_name_exception import (
    InvalidGitHubAccountTokenNameException as InvalidGitHubAccountTokenNameException,
)
from .invalid_iam_session_arn_exception import (
    InvalidIamSessionArnException as InvalidIamSessionArnException,
)
from .invalid_iam_user_arn_exception import (
    InvalidIamUserArnException as InvalidIamUserArnException,
)
from .invalid_ignore_application_stop_failures_value_exception import (
    InvalidIgnoreApplicationStopFailuresValueException as InvalidIgnoreApplicationStopFailuresValueException,
)
from .invalid_input_exception import InvalidInputException as InvalidInputException
from .invalid_instance_name_exception import (
    InvalidInstanceNameException as InvalidInstanceNameException,
)
from .invalid_instance_status_exception import (
    InvalidInstanceStatusException as InvalidInstanceStatusException,
)
from .invalid_instance_type_exception import (
    InvalidInstanceTypeException as InvalidInstanceTypeException,
)
from .invalid_key_prefix_filter_exception import (
    InvalidKeyPrefixFilterException as InvalidKeyPrefixFilterException,
)
from .invalid_lifecycle_event_hook_execution_id_exception import (
    InvalidLifecycleEventHookExecutionIdException as InvalidLifecycleEventHookExecutionIdException,
)
from .invalid_lifecycle_event_hook_execution_status_exception import (
    InvalidLifecycleEventHookExecutionStatusException as InvalidLifecycleEventHookExecutionStatusException,
)
from .invalid_load_balancer_info_exception import (
    InvalidLoadBalancerInfoException as InvalidLoadBalancerInfoException,
)
from .invalid_minimum_healthy_host_value_exception import (
    InvalidMinimumHealthyHostValueException as InvalidMinimumHealthyHostValueException,
)
from .invalid_next_token_exception import (
    InvalidNextTokenException as InvalidNextTokenException,
)
from .invalid_on_premises_tag_combination_exception import (
    InvalidOnPremisesTagCombinationException as InvalidOnPremisesTagCombinationException,
)
from .invalid_operation_exception import (
    InvalidOperationException as InvalidOperationException,
)
from .invalid_registration_status_exception import (
    InvalidRegistrationStatusException as InvalidRegistrationStatusException,
)
from .invalid_revision_exception import (
    InvalidRevisionException as InvalidRevisionException,
)
from .invalid_role_exception import InvalidRoleException as InvalidRoleException
from .invalid_sort_by_exception import InvalidSortByException as InvalidSortByException
from .invalid_sort_order_exception import (
    InvalidSortOrderException as InvalidSortOrderException,
)
from .invalid_tag_exception import InvalidTagException as InvalidTagException
from .invalid_tag_filter_exception import (
    InvalidTagFilterException as InvalidTagFilterException,
)
from .invalid_tags_to_add_exception import (
    InvalidTagsToAddException as InvalidTagsToAddException,
)
from .invalid_target_filter_name_exception import (
    InvalidTargetFilterNameException as InvalidTargetFilterNameException,
)
from .invalid_target_group_pair_exception import (
    InvalidTargetGroupPairException as InvalidTargetGroupPairException,
)
from .invalid_target_instances_exception import (
    InvalidTargetInstancesException as InvalidTargetInstancesException,
)
from .invalid_time_range_exception import (
    InvalidTimeRangeException as InvalidTimeRangeException,
)
from .invalid_traffic_routing_configuration_exception import (
    InvalidTrafficRoutingConfigurationException as InvalidTrafficRoutingConfigurationException,
)
from .invalid_trigger_config_exception import (
    InvalidTriggerConfigException as InvalidTriggerConfigException,
)
from .invalid_update_outdated_instances_only_value_exception import (
    InvalidUpdateOutdatedInstancesOnlyValueException as InvalidUpdateOutdatedInstancesOnlyValueException,
)
from .invalid_zonal_deployment_configuration_exception import (
    InvalidZonalDeploymentConfigurationException as InvalidZonalDeploymentConfigurationException,
)
from .lifecycle_event_already_completed_exception import (
    LifecycleEventAlreadyCompletedException as LifecycleEventAlreadyCompletedException,
)
from .lifecycle_hook_limit_exceeded_exception import (
    LifecycleHookLimitExceededException as LifecycleHookLimitExceededException,
)
from .multiple_iam_arns_provided_exception import (
    MultipleIamArnsProvidedException as MultipleIamArnsProvidedException,
)
from .operation_not_supported_exception import (
    OperationNotSupportedException as OperationNotSupportedException,
)
from .resource_arn_required_exception import (
    ResourceArnRequiredException as ResourceArnRequiredException,
)
from .resource_validation_exception import (
    ResourceValidationException as ResourceValidationException,
)
from .revision_does_not_exist_exception import (
    RevisionDoesNotExistException as RevisionDoesNotExistException,
)
from .revision_required_exception import (
    RevisionRequiredException as RevisionRequiredException,
)
from .role_required_exception import RoleRequiredException as RoleRequiredException
from .tag_limit_exceeded_exception import (
    TagLimitExceededException as TagLimitExceededException,
)
from .tag_required_exception import TagRequiredException as TagRequiredException
from .tag_set_list_limit_exceeded_exception import (
    TagSetListLimitExceededException as TagSetListLimitExceededException,
)
from .throttling_exception import ThrottlingException as ThrottlingException
from .trigger_targets_limit_exceeded_exception import (
    TriggerTargetsLimitExceededException as TriggerTargetsLimitExceededException,
)
from .unsupported_action_for_deployment_type_exception import (
    UnsupportedActionForDeploymentTypeException as UnsupportedActionForDeploymentTypeException,
)
