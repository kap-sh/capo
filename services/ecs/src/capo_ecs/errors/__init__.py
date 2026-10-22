from __future__ import annotations

from ._base import (
    DeserializationError as DeserializationError,
)
from ._base import (
    ECSError as ECSError,
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
from .access_denied_exception import AccessDeniedException as AccessDeniedException
from .attribute_limit_exceeded_exception import (
    AttributeLimitExceededException as AttributeLimitExceededException,
)
from .blocked_exception import BlockedException as BlockedException
from .client_exception import ClientException as ClientException
from .cluster_contains_capacity_provider_exception import (
    ClusterContainsCapacityProviderException as ClusterContainsCapacityProviderException,
)
from .cluster_contains_container_instances_exception import (
    ClusterContainsContainerInstancesException as ClusterContainsContainerInstancesException,
)
from .cluster_contains_services_exception import (
    ClusterContainsServicesException as ClusterContainsServicesException,
)
from .cluster_contains_tasks_exception import (
    ClusterContainsTasksException as ClusterContainsTasksException,
)
from .cluster_not_found_exception import (
    ClusterNotFoundException as ClusterNotFoundException,
)
from .conflict_exception import ConflictException as ConflictException
from .daemon_not_active_exception import (
    DaemonNotActiveException as DaemonNotActiveException,
)
from .daemon_not_found_exception import (
    DaemonNotFoundException as DaemonNotFoundException,
)
from .gateway_not_found_exception import (
    GatewayNotFoundException as GatewayNotFoundException,
)
from .invalid_parameter_exception import (
    InvalidParameterException as InvalidParameterException,
)
from .limit_exceeded_exception import LimitExceededException as LimitExceededException
from .missing_version_exception import (
    MissingVersionException as MissingVersionException,
)
from .namespace_not_found_exception import (
    NamespaceNotFoundException as NamespaceNotFoundException,
)
from .no_update_available_exception import (
    NoUpdateAvailableException as NoUpdateAvailableException,
)
from .platform_task_definition_incompatibility_exception import (
    PlatformTaskDefinitionIncompatibilityException as PlatformTaskDefinitionIncompatibilityException,
)
from .platform_unknown_exception import (
    PlatformUnknownException as PlatformUnknownException,
)
from .resource_in_use_exception import ResourceInUseException as ResourceInUseException
from .resource_not_found_exception import (
    ResourceNotFoundException as ResourceNotFoundException,
)
from .server_exception import ServerException as ServerException
from .service_deployment_not_found_exception import (
    ServiceDeploymentNotFoundException as ServiceDeploymentNotFoundException,
)
from .service_not_active_exception import (
    ServiceNotActiveException as ServiceNotActiveException,
)
from .service_not_found_exception import (
    ServiceNotFoundException as ServiceNotFoundException,
)
from .target_not_connected_exception import (
    TargetNotConnectedException as TargetNotConnectedException,
)
from .target_not_found_exception import (
    TargetNotFoundException as TargetNotFoundException,
)
from .task_set_not_found_exception import (
    TaskSetNotFoundException as TaskSetNotFoundException,
)
from .unsupported_feature_exception import (
    UnsupportedFeatureException as UnsupportedFeatureException,
)
from .update_in_progress_exception import (
    UpdateInProgressException as UpdateInProgressException,
)
