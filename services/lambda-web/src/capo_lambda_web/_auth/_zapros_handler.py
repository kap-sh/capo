from typing import Optional, cast

from zapros import (
    AsyncBaseHandler,
    AsyncBaseMiddleware,
    AsyncSyncMismatchError,
    BaseHandler,
    BaseMiddleware,
    Request,
)
from zapros._models import Response

from ._signers import Signer


def ensure_async_handler(
    handler: AsyncBaseHandler | BaseHandler,
) -> AsyncBaseHandler:
    if isinstance(handler, AsyncBaseHandler):
        return handler
    raise AsyncSyncMismatchError(
        "Handler was expected to be an AsyncBaseHandler, but it is not."
    )


def ensure_sync_handler(
    handler: AsyncBaseHandler | BaseHandler,
) -> BaseHandler:
    if isinstance(handler, BaseHandler):
        return handler
    raise AsyncSyncMismatchError(
        "Handler was expected to be a BaseHandler, but it is not."
    )


def strip_accept_encoding(request: Request) -> Request:
    """Drop the ``Accept-Encoding`` zapros adds to every request.

    Like the AWS SDKs, the client never asks for transport compression: a
    response body must be the service's actual bytes so ``Content-Length``,
    checksums and ``Range`` stay coherent and a ``Content-Encoding`` on it is
    always stored metadata (an S3 object's), never something to undo. Removing
    the header before signing also keeps it out of the canonical request, where
    a proxy rewriting it in flight would break the signature.
    """
    if "accept-encoding" in request.headers:
        del request.headers["Accept-Encoding"]
    return request


class AuthMiddleware(BaseMiddleware, AsyncBaseMiddleware):
    """Sign the outgoing request using the Signer placed in ``context["signer"]``.

    The generated ``get_signer`` in each operation module resolves the
    effective auth scheme to a concrete :class:`Signer` and threads it
    through ``request.context`` before dispatch. This middleware does the
    actual signing; ``None`` means the operation opted out via
    ``@optionalAuth`` and the request passes through unsigned. Either way
    ``Accept-Encoding`` is stripped first (see :func:`strip_accept_encoding`).
    """

    def __init__(self, next_handler: BaseHandler | AsyncBaseHandler) -> None:
        self.next = cast(BaseHandler, next_handler)
        self.async_next = cast(AsyncBaseHandler, next_handler)

    def handle(self, request: Request) -> Response:
        next_handler = ensure_sync_handler(self.next)
        request = strip_accept_encoding(request)
        signer = cast(Optional[Signer], request.context.get("signer"))
        if signer is not None:
            request = signer.sign(request)
        return next_handler.handle(request)

    async def ahandle(self, request: Request) -> Response:
        next_handler = ensure_async_handler(self.async_next)
        request = strip_accept_encoding(request)
        signer = cast(Optional[Signer], request.context.get("signer"))
        if signer is not None:
            request = await signer.asign(request)
        return await next_handler.ahandle(request)
