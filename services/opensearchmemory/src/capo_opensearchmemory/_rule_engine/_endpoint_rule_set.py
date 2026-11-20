from __future__ import annotations

from typing import Any

from ._endpoint_runtime import (
    Endpoint,
    EndpointError,
    interpolate,
    is_valid_host_label,
)


class EndpointParams:
    def __init__(
        self,
        *,
        Region: str | None = None,
        UseFIPS: bool | None = None,
        Endpoint: str | None = None,
        SpaceId: str | None = None,
    ):
        self.Region = Region
        self.UseFIPS = UseFIPS if UseFIPS is not None else False
        self.Endpoint = Endpoint if Endpoint is not None else None
        self.SpaceId = SpaceId if SpaceId is not None else None


def resolve(p: EndpointParams) -> Endpoint:  # type: ignore
    """Resolve endpoint from parameters using generated ruleset."""
    _locals: dict[str, Any] = {}
    if p.Endpoint is not None:
        if p.UseFIPS is True:
            raise EndpointError(
                interpolate(
                    "Invalid Configuration: FIPS and custom endpoint are not supported",
                    p,
                    _locals,
                )
            )
    _locals: dict[str, Any] = {}
    if p.Endpoint is not None:
        return Endpoint(
            url=interpolate("{Endpoint}", p, _locals), properties={}, headers={}
        )
    _locals: dict[str, Any] = {}
    if p.UseFIPS is True:
        raise EndpointError(
            interpolate(
                "Invalid Configuration: FIPS is not supported with OpenSearch Memory.",
                p,
                _locals,
            )
        )
    _locals: dict[str, Any] = {}
    if not (is_valid_host_label(p.Region, True)):
        raise EndpointError(
            interpolate(
                "Invalid Configuration: Region must be a valid host label", p, _locals
            )
        )
    _locals: dict[str, Any] = {}
    if p.SpaceId is not None:
        if is_valid_host_label(p.SpaceId, False):
            return Endpoint(
                url=interpolate("https://{SpaceId}.osm.{Region}.on.aws", p, _locals),
                properties={},
                headers={},
            )
    _locals: dict[str, Any] = {}
    if p.SpaceId is not None:
        raise EndpointError(
            interpolate("Invalid SpaceId: must be a valid host label", p, _locals)
        )
    _locals: dict[str, Any] = {}
    return Endpoint(
        url=interpolate("https://osm.{Region}.api.aws", p, _locals),
        properties={},
        headers={},
    )
    raise EndpointError("No endpoint rules matched")
