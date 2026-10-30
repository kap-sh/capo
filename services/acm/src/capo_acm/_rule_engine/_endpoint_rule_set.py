from __future__ import annotations

from typing import Any

from ._aws_partition import aws_partition
from ._endpoint_runtime import (
    Endpoint,
    EndpointError,
    get_attr,
    interpolate,
    string_equals,
)


class EndpointParams:
    def __init__(
        self,
        *,
        Region: str | None = None,
        ServiceType: str | None = None,
        UseFIPS: bool | None = None,
        UseDualStack: bool | None = None,
        Endpoint: str | None = None,
    ):
        self.Region = Region
        self.ServiceType = ServiceType
        self.UseFIPS = UseFIPS if UseFIPS is not None else False
        self.UseDualStack = UseDualStack if UseDualStack is not None else False
        self.Endpoint = Endpoint if Endpoint is not None else None


def resolve(p: EndpointParams) -> Endpoint:  # type: ignore
    """Resolve endpoint from parameters using generated ruleset."""
    _locals: dict[str, Any] = {}
    if p.Endpoint is not None:
        return Endpoint(
            url=interpolate("{Endpoint}", p, _locals), properties={}, headers={}
        )
    _locals: dict[str, Any] = {}
    _locals["PartitionResult"] = aws_partition(p.Region)
    if _locals["PartitionResult"] is not None:
        if string_equals(p.ServiceType, interpolate("ACM-ACME", p, _locals)):
            if p.Endpoint is not None:
                return Endpoint(
                    url=interpolate("{Endpoint}", p, _locals), properties={}, headers={}
                )
            if string_equals(
                get_attr(_locals["PartitionResult"], interpolate("name", p, _locals)),
                interpolate("aws", p, _locals),
            ):
                if p.UseFIPS is True:
                    raise EndpointError(
                        interpolate(
                            "FIPS endpoints are not available for ACME operations",
                            p,
                            _locals,
                        )
                    )
                return Endpoint(
                    url=interpolate(
                        "https://acm-acme.{Region}.{PartitionResult#dualStackDnsSuffix}",
                        p,
                        _locals,
                    ),
                    properties={},
                    headers={},
                )
            if string_equals(
                get_attr(_locals["PartitionResult"], interpolate("name", p, _locals)),
                interpolate("aws-us-gov", p, _locals),
            ):
                if p.UseFIPS is True:
                    raise EndpointError(
                        interpolate(
                            "FIPS endpoints are not available for ACME operations",
                            p,
                            _locals,
                        )
                    )
                return Endpoint(
                    url=interpolate(
                        "https://acm-acme.{Region}.{PartitionResult#dualStackDnsSuffix}",
                        p,
                        _locals,
                    ),
                    properties={},
                    headers={},
                )
            raise EndpointError(
                interpolate(
                    "ACME operations are only available in the aws and aws-us-gov partitions",
                    p,
                    _locals,
                )
            )
        if p.UseFIPS is True:
            if p.UseDualStack is True:
                return Endpoint(
                    url=interpolate(
                        "https://acm-fips.{Region}.{PartitionResult#dualStackDnsSuffix}",
                        p,
                        _locals,
                    ),
                    properties={},
                    headers={},
                )
        if p.UseFIPS is True:
            if string_equals(
                get_attr(_locals["PartitionResult"], interpolate("name", p, _locals)),
                interpolate("aws-us-gov", p, _locals),
            ):
                return Endpoint(
                    url=interpolate("https://acm.{Region}.amazonaws.com", p, _locals),
                    properties={},
                    headers={},
                )
            return Endpoint(
                url=interpolate(
                    "https://acm-fips.{Region}.{PartitionResult#dnsSuffix}", p, _locals
                ),
                properties={},
                headers={},
            )
        if p.UseDualStack is True:
            return Endpoint(
                url=interpolate(
                    "https://acm.{Region}.{PartitionResult#dualStackDnsSuffix}",
                    p,
                    _locals,
                ),
                properties={},
                headers={},
            )
        return Endpoint(
            url=interpolate(
                "https://acm.{Region}.{PartitionResult#dnsSuffix}", p, _locals
            ),
            properties={},
            headers={},
        )
    _locals: dict[str, Any] = {}
    raise EndpointError(
        interpolate("Region must be set to resolve an endpoint.", p, _locals)
    )
    raise EndpointError("No endpoint rules matched")
