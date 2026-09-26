from __future__ import annotations

from typing import Any

from ._endpoint_runtime import (
    Endpoint,
    EndpointError,
    interpolate,
)


class EndpointParams:
    def __init__(self, *, Region: str | None = None, Endpoint: str | None = None):
        self.Region = Region
        self.Endpoint = Endpoint if Endpoint is not None else None


def resolve(p: EndpointParams) -> Endpoint:  # type: ignore
    """Resolve endpoint from parameters using generated ruleset."""
    _locals: dict[str, Any] = {}
    if p.Endpoint is not None:
        return Endpoint(
            url=interpolate("{Endpoint}", p, _locals),
            properties={
                "authSchemes": [
                    {
                        "name": interpolate("sigv4", p, _locals),
                        "signingName": interpolate("pricingplanmanager", p, _locals),
                        "signingRegion": interpolate("us-east-1", p, _locals),
                    }
                ]
            },
            headers={},
        )
    _locals: dict[str, Any] = {}
    return Endpoint(
        url=interpolate("https://pricingplanmanager.us-east-1.api.aws", p, _locals),
        properties={
            "authSchemes": [
                {
                    "name": interpolate("sigv4", p, _locals),
                    "signingName": interpolate("pricingplanmanager", p, _locals),
                    "signingRegion": interpolate("us-east-1", p, _locals),
                }
            ]
        },
        headers={},
    )
    raise EndpointError("No endpoint rules matched")
