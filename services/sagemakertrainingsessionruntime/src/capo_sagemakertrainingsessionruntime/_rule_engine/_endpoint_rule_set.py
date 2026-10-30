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
        UseFIPS: bool | None = None,
        Endpoint: str | None = None,
        Region: str | None = None,
    ):
        self.UseFIPS = UseFIPS if UseFIPS is not None else False
        self.Endpoint = Endpoint if Endpoint is not None else None
        self.Region = Region if Region is not None else None


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
        return Endpoint(url=p.Endpoint, properties={}, headers={})
    _locals: dict[str, Any] = {}
    if p.Region is not None:
        _locals["PartitionResult"] = aws_partition(p.Region)
        if _locals["PartitionResult"] is not None:
            if string_equals(
                get_attr(_locals["PartitionResult"], interpolate("name", p, _locals)),
                interpolate("aws", p, _locals),
            ):
                if p.UseFIPS is False:
                    return Endpoint(
                        url=interpolate(
                            "https://training-session-runtime.sagemaker.{Region}.{PartitionResult#dualStackDnsSuffix}",
                            p,
                            _locals,
                        ),
                        properties={},
                        headers={},
                    )
            if string_equals(
                get_attr(_locals["PartitionResult"], interpolate("name", p, _locals)),
                interpolate("aws-cn", p, _locals),
            ):
                if p.UseFIPS is False:
                    return Endpoint(
                        url=interpolate(
                            "https://training-session-runtime.sagemaker.{Region}.{PartitionResult#dualStackDnsSuffix}",
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
                if p.UseFIPS is False:
                    return Endpoint(
                        url=interpolate(
                            "https://training-session-runtime.sagemaker.{Region}.{PartitionResult#dualStackDnsSuffix}",
                            p,
                            _locals,
                        ),
                        properties={},
                        headers={},
                    )
            if p.UseFIPS is True:
                return Endpoint(
                    url=interpolate(
                        "https://training-session-runtime.sagemaker-fips.{Region}.{PartitionResult#dualStackDnsSuffix}",
                        p,
                        _locals,
                    ),
                    properties={},
                    headers={},
                )
            return Endpoint(
                url=interpolate(
                    "https://training-session-runtime.sagemaker.{Region}.{PartitionResult#dualStackDnsSuffix}",
                    p,
                    _locals,
                ),
                properties={},
                headers={},
            )
    raise EndpointError(
        interpolate("Invalid Configuration: Missing Region", p, _locals)
    )
    raise EndpointError("No endpoint rules matched")
