from __future__ import annotations

from ._base import (
    DeserializationError as DeserializationError,
)
from ._base import (
    LambdaWebError as LambdaWebError,
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
from .internal_server_exception import (
    InternalServerException as InternalServerException,
)
from .throttling_exception import ThrottlingException as ThrottlingException
