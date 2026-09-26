from __future__ import annotations

from typing import Any

from ._endpoint_runtime import (
    Endpoint,
    EndpointError,
    interpolate,
)


class EndpointParams:
    def __init__(self, *, Region: str | None = None, Endpoint: str | None = None):
        self.Region = Region if Region is not None else None
        self.Endpoint = Endpoint if Endpoint is not None else None


def resolve(p: EndpointParams) -> Endpoint:  # type: ignore
    """Resolve endpoint from parameters using generated ruleset."""
    _locals: dict[str, Any] = {}
    if p.Endpoint is not None:
        return Endpoint(url=p.Endpoint, properties={}, headers={})
    _locals: dict[str, Any] = {}
    if p.Region is not None:
        return Endpoint(
            url=interpolate(
                "https://agent-registry-control.{Region}.api.aws", p, _locals
            ),
            properties={},
            headers={},
        )
    _locals: dict[str, Any] = {}
    raise EndpointError(
        interpolate(
            "Unable to resolve an Agent Registry Control endpoint: Region was not set and no explicit Endpoint override was provided.",
            p,
            _locals,
        )
    )
    raise EndpointError("No endpoint rules matched")
