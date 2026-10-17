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
        UseDualStack: bool | None = None,
        UseFIPS: bool | None = None,
        Region: str | None = None,
        Endpoint: str | None = None,
    ):
        self.UseDualStack = UseDualStack if UseDualStack is not None else False
        self.UseFIPS = UseFIPS if UseFIPS is not None else False
        self.Region = Region if Region is not None else None
        self.Endpoint = Endpoint if Endpoint is not None else None


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
        if p.UseDualStack is True:
            raise EndpointError(
                interpolate(
                    "Invalid Configuration: Dualstack and custom endpoint are not supported",
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
                    if p.UseDualStack is False:
                        return Endpoint(
                            url=interpolate(
                                "https://organizations.us-east-1.amazonaws.com",
                                p,
                                _locals,
                            ),
                            properties={
                                "authSchemes": [
                                    {
                                        "name": interpolate("sigv4", p, _locals),
                                        "signingName": interpolate(
                                            "organizations", p, _locals
                                        ),
                                        "signingRegion": interpolate(
                                            "us-east-1", p, _locals
                                        ),
                                    }
                                ]
                            },
                            headers={},
                        )
            if string_equals(
                get_attr(_locals["PartitionResult"], interpolate("name", p, _locals)),
                interpolate("aws", p, _locals),
            ):
                if p.UseFIPS is True:
                    if p.UseDualStack is False:
                        return Endpoint(
                            url=interpolate(
                                "https://organizations-fips.us-east-1.amazonaws.com",
                                p,
                                _locals,
                            ),
                            properties={
                                "authSchemes": [
                                    {
                                        "name": interpolate("sigv4", p, _locals),
                                        "signingName": interpolate(
                                            "organizations", p, _locals
                                        ),
                                        "signingRegion": interpolate(
                                            "us-east-1", p, _locals
                                        ),
                                    }
                                ]
                            },
                            headers={},
                        )
            if string_equals(
                get_attr(_locals["PartitionResult"], interpolate("name", p, _locals)),
                interpolate("aws-cn", p, _locals),
            ):
                if p.UseFIPS is False:
                    if p.UseDualStack is False:
                        return Endpoint(
                            url=interpolate(
                                "https://organizations.cn-northwest-1.amazonaws.com.cn",
                                p,
                                _locals,
                            ),
                            properties={
                                "authSchemes": [
                                    {
                                        "name": interpolate("sigv4", p, _locals),
                                        "signingName": interpolate(
                                            "organizations", p, _locals
                                        ),
                                        "signingRegion": interpolate(
                                            "cn-northwest-1", p, _locals
                                        ),
                                    }
                                ]
                            },
                            headers={},
                        )
            if string_equals(
                get_attr(_locals["PartitionResult"], interpolate("name", p, _locals)),
                interpolate("aws-us-gov", p, _locals),
            ):
                if p.UseFIPS is False:
                    if p.UseDualStack is False:
                        return Endpoint(
                            url=interpolate(
                                "https://organizations.us-gov-west-1.amazonaws.com",
                                p,
                                _locals,
                            ),
                            properties={
                                "authSchemes": [
                                    {
                                        "name": interpolate("sigv4", p, _locals),
                                        "signingName": interpolate(
                                            "organizations", p, _locals
                                        ),
                                        "signingRegion": interpolate(
                                            "us-gov-west-1", p, _locals
                                        ),
                                    }
                                ]
                            },
                            headers={},
                        )
            if string_equals(
                get_attr(_locals["PartitionResult"], interpolate("name", p, _locals)),
                interpolate("aws-us-gov", p, _locals),
            ):
                if p.UseFIPS is True:
                    if p.UseDualStack is False:
                        return Endpoint(
                            url=interpolate(
                                "https://organizations.us-gov-west-1.amazonaws.com",
                                p,
                                _locals,
                            ),
                            properties={
                                "authSchemes": [
                                    {
                                        "name": interpolate("sigv4", p, _locals),
                                        "signingName": interpolate(
                                            "organizations", p, _locals
                                        ),
                                        "signingRegion": interpolate(
                                            "us-gov-west-1", p, _locals
                                        ),
                                    }
                                ]
                            },
                            headers={},
                        )
            if string_equals(
                get_attr(_locals["PartitionResult"], interpolate("name", p, _locals)),
                interpolate("aws-iso", p, _locals),
            ):
                if p.UseFIPS is False:
                    if p.UseDualStack is False:
                        return Endpoint(
                            url=interpolate(
                                "https://organizations.us-iso-east-1.c2s.ic.gov",
                                p,
                                _locals,
                            ),
                            properties={
                                "authSchemes": [
                                    {
                                        "name": interpolate("sigv4", p, _locals),
                                        "signingName": interpolate(
                                            "organizations", p, _locals
                                        ),
                                        "signingRegion": interpolate(
                                            "us-iso-east-1", p, _locals
                                        ),
                                    }
                                ]
                            },
                            headers={},
                        )
            if string_equals(
                get_attr(_locals["PartitionResult"], interpolate("name", p, _locals)),
                interpolate("aws-iso-b", p, _locals),
            ):
                if p.UseFIPS is False:
                    if p.UseDualStack is False:
                        return Endpoint(
                            url=interpolate(
                                "https://organizations.us-isob-east-1.sc2s.sgov.gov",
                                p,
                                _locals,
                            ),
                            properties={
                                "authSchemes": [
                                    {
                                        "name": interpolate("sigv4", p, _locals),
                                        "signingName": interpolate(
                                            "organizations", p, _locals
                                        ),
                                        "signingRegion": interpolate(
                                            "us-isob-east-1", p, _locals
                                        ),
                                    }
                                ]
                            },
                            headers={},
                        )
            if string_equals(
                get_attr(_locals["PartitionResult"], interpolate("name", p, _locals)),
                interpolate("aws-iso-f", p, _locals),
            ):
                if p.UseFIPS is False:
                    if p.UseDualStack is False:
                        return Endpoint(
                            url=interpolate(
                                "https://organizations.us-isof-south-1.csp.hci.ic.gov",
                                p,
                                _locals,
                            ),
                            properties={
                                "authSchemes": [
                                    {
                                        "name": interpolate("sigv4", p, _locals),
                                        "signingName": interpolate(
                                            "organizations", p, _locals
                                        ),
                                        "signingRegion": interpolate(
                                            "us-isof-south-1", p, _locals
                                        ),
                                    }
                                ]
                            },
                            headers={},
                        )
            if p.UseFIPS is True:
                if p.UseDualStack is True:
                    if True is get_attr(
                        _locals["PartitionResult"],
                        interpolate("supportsFIPS", p, _locals),
                    ):
                        if True is get_attr(
                            _locals["PartitionResult"],
                            interpolate("supportsDualStack", p, _locals),
                        ):
                            return Endpoint(
                                url=interpolate(
                                    "https://organizations-fips.{Region}.{PartitionResult#dualStackDnsSuffix}",
                                    p,
                                    _locals,
                                ),
                                properties={},
                                headers={},
                            )
                    raise EndpointError(
                        interpolate(
                            "FIPS and DualStack are enabled, but this partition does not support one or both",
                            p,
                            _locals,
                        )
                    )
            if p.UseFIPS is True:
                if (
                    get_attr(
                        _locals["PartitionResult"],
                        interpolate("supportsFIPS", p, _locals),
                    )
                    is True
                ):
                    return Endpoint(
                        url=interpolate(
                            "https://organizations-fips.{Region}.{PartitionResult#dnsSuffix}",
                            p,
                            _locals,
                        ),
                        properties={},
                        headers={},
                    )
                raise EndpointError(
                    interpolate(
                        "FIPS is enabled but this partition does not support FIPS",
                        p,
                        _locals,
                    )
                )
            if p.UseDualStack is True:
                if True is get_attr(
                    _locals["PartitionResult"],
                    interpolate("supportsDualStack", p, _locals),
                ):
                    return Endpoint(
                        url=interpolate(
                            "https://organizations.{Region}.{PartitionResult#dualStackDnsSuffix}",
                            p,
                            _locals,
                        ),
                        properties={},
                        headers={},
                    )
                raise EndpointError(
                    interpolate(
                        "DualStack is enabled but this partition does not support DualStack",
                        p,
                        _locals,
                    )
                )
            return Endpoint(
                url=interpolate(
                    "https://organizations.{Region}.{PartitionResult#dnsSuffix}",
                    p,
                    _locals,
                ),
                properties={},
                headers={},
            )
    _locals: dict[str, Any] = {}
    raise EndpointError(
        interpolate("Invalid Configuration: Missing Region", p, _locals)
    )
    raise EndpointError("No endpoint rules matched")
