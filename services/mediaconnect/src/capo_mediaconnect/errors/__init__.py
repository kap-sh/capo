from __future__ import annotations

from ._base import (
    DeserializationError as DeserializationError,
)
from ._base import (
    MediaConnectError as MediaConnectError,
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
from .add_flow_outputs420_exception import (
    AddFlowOutputs420Exception as AddFlowOutputs420Exception,
)
from .bad_request_exception import BadRequestException as BadRequestException
from .conflict_exception import ConflictException as ConflictException
from .create_bridge420_exception import (
    CreateBridge420Exception as CreateBridge420Exception,
)
from .create_flow420_exception import CreateFlow420Exception as CreateFlow420Exception
from .create_gateway420_exception import (
    CreateGateway420Exception as CreateGateway420Exception,
)
from .destination_endpoint_service_quota_exceeded_exception import (
    DestinationEndpointServiceQuotaExceededException as DestinationEndpointServiceQuotaExceededException,
)
from .forbidden_exception import ForbiddenException as ForbiddenException
from .grant_flow_entitlements420_exception import (
    GrantFlowEntitlements420Exception as GrantFlowEntitlements420Exception,
)
from .internal_server_error_exception import (
    InternalServerErrorException as InternalServerErrorException,
)
from .not_found_exception import NotFoundException as NotFoundException
from .router_input_service_quota_exceeded_exception import (
    RouterInputServiceQuotaExceededException as RouterInputServiceQuotaExceededException,
)
from .router_network_interface_service_quota_exceeded_exception import (
    RouterNetworkInterfaceServiceQuotaExceededException as RouterNetworkInterfaceServiceQuotaExceededException,
)
from .router_output_service_quota_exceeded_exception import (
    RouterOutputServiceQuotaExceededException as RouterOutputServiceQuotaExceededException,
)
from .service_unavailable_exception import (
    ServiceUnavailableException as ServiceUnavailableException,
)
from .source_endpoint_service_quota_exceeded_exception import (
    SourceEndpointServiceQuotaExceededException as SourceEndpointServiceQuotaExceededException,
)
from .too_many_requests_exception import (
    TooManyRequestsException as TooManyRequestsException,
)
