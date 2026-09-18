from __future__ import annotations

from . import _iter as _iter
from . import _protocol as _protocol
from ._auth._identity import Credentials as Credentials
from ._auth._identity import Identity as Identity
from ._auth._providers import (
    CachedProvider as CachedProvider,
)
from ._auth._providers import (
    ChainedProvider as ChainedProvider,
)
from ._auth._providers import (
    CredentialsProvider as CredentialsProvider,
)
from ._auth._providers import (
    EnvCredentialsProvider as EnvCredentialsProvider,
)
from ._auth._providers import (
    IdentityNotFound as IdentityNotFound,
)
from ._auth._providers import (
    IdentityProvider as IdentityProvider,
)
from ._auth._providers import (
    ProfileCredentialsProvider as ProfileCredentialsProvider,
)
from ._auth._providers import (
    StaticAwsCredentialsProvider as StaticAwsCredentialsProvider,
)
from ._auth._signers import (
    Signer as Signer,
)
from ._auth._signers import (
    SigV4ASigner as SigV4ASigner,
)
from ._auth._signers import (
    SigV4Signer as SigV4Signer,
)
from ._body import Body as Body
from ._services._pipeline import (
    AsyncOperationOptions as AsyncOperationOptions,
)
from ._services._pipeline import (
    AsyncOperationRequest as AsyncOperationRequest,
)
from ._services._pipeline import (
    AsyncOperationResponse as AsyncOperationResponse,
)
from ._services._pipeline import (
    OperationOptions as OperationOptions,
)
from ._services._pipeline import (
    OperationRequest as OperationRequest,
)
from ._services._pipeline import (
    OperationResponse as OperationResponse,
)
from ._services.async_sts import AsyncSTSClient as AsyncSTSClient
from ._services.sts import STSClient as STSClient
