from __future__ import annotations

from ._base import (
    DeserializationError as DeserializationError,
)
from ._base import (
    RolesAnywhereError as RolesAnywhereError,
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
from .resource_not_found_exception import (
    ResourceNotFoundException as ResourceNotFoundException,
)
from .service_unavailable_exception import (
    ServiceUnavailableException as ServiceUnavailableException,
)
from .too_many_tags_exception import TooManyTagsException as TooManyTagsException
from .validation_exception import ValidationException as ValidationException
