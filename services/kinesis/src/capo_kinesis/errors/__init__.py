from __future__ import annotations

from ._base import (
    DeserializationError as DeserializationError,
)
from ._base import (
    KinesisError as KinesisError,
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
from .dry_run_operation_exception import (
    DryRunOperationException as DryRunOperationException,
)
from .expired_iterator_exception import (
    ExpiredIteratorException as ExpiredIteratorException,
)
from .expired_next_token_exception import (
    ExpiredNextTokenException as ExpiredNextTokenException,
)
from .internal_failure_exception import (
    InternalFailureException as InternalFailureException,
)
from .invalid_argument_exception import (
    InvalidArgumentException as InvalidArgumentException,
)
from .kms_access_denied_exception import (
    KMSAccessDeniedException as KMSAccessDeniedException,
)
from .kms_disabled_exception import KMSDisabledException as KMSDisabledException
from .kms_invalid_state_exception import (
    KMSInvalidStateException as KMSInvalidStateException,
)
from .kms_not_found_exception import KMSNotFoundException as KMSNotFoundException
from .kms_opt_in_required import KMSOptInRequired as KMSOptInRequired
from .kms_throttling_exception import KMSThrottlingException as KMSThrottlingException
from .limit_exceeded_exception import LimitExceededException as LimitExceededException
from .provisioned_throughput_exceeded_exception import (
    ProvisionedThroughputExceededException as ProvisionedThroughputExceededException,
)
from .resource_in_use_exception import ResourceInUseException as ResourceInUseException
from .resource_not_found_exception import (
    ResourceNotFoundException as ResourceNotFoundException,
)
from .throttling_exception import ThrottlingException as ThrottlingException
from .validation_exception import ValidationException as ValidationException
