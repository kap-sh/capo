from __future__ import annotations

from typing import Any

from ._aws_partition import aws_partition
from ._endpoint_runtime import (
    Endpoint,
    EndpointError,
    aws_parse_arn,
    get_attr,
    interpolate,
    is_valid_host_label,
    parse_url,
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
        AccountId: str | None = None,
        AccountIdEndpointMode: str | None = None,
        ResourceArn: str | None = None,
        ResourceArnList: list[str] | None = None,
        IsSearchOperation: bool | None = None,
    ):
        self.UseDualStack = UseDualStack if UseDualStack is not None else False
        self.UseFIPS = UseFIPS if UseFIPS is not None else False
        self.Region = Region if Region is not None else None
        self.Endpoint = Endpoint if Endpoint is not None else None
        self.AccountId = AccountId if AccountId is not None else None
        self.AccountIdEndpointMode = (
            AccountIdEndpointMode if AccountIdEndpointMode is not None else None
        )
        self.ResourceArn = ResourceArn if ResourceArn is not None else None
        self.ResourceArnList = ResourceArnList if ResourceArnList is not None else None
        self.IsSearchOperation = (
            IsSearchOperation if IsSearchOperation is not None else None
        )


def resolve(p: EndpointParams) -> Endpoint:  # type: ignore
    """Resolve endpoint from parameters using generated ruleset."""
    _locals: dict[str, Any] = {}
    if p.Endpoint is not None:
        if p.Region is not None:
            _locals["PartitionResult"] = aws_partition(p.Region)
            if _locals["PartitionResult"] is not None:
                _locals["parsedEndpoint"] = parse_url(p.Endpoint)
                if _locals["parsedEndpoint"] is not None:
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
                    if string_equals(
                        get_attr(
                            _locals["parsedEndpoint"],
                            interpolate("authority", p, _locals),
                        ),
                        interpolate(
                            "dynamodb.{Region}.{PartitionResult#dualStackDnsSuffix}",
                            p,
                            _locals,
                        ),
                    ):
                        raise EndpointError(
                            interpolate(
                                "Endpoint override is not supported for dual-stack endpoints. Please enable dual-stack functionality by enabling the configuration. For more details, see: https://docs.aws.amazon.com/sdkref/latest/guide/feature-endpoints.html",
                                p,
                                _locals,
                            )
                        )
                    if string_equals(
                        get_attr(
                            _locals["parsedEndpoint"],
                            interpolate("authority", p, _locals),
                        ),
                        interpolate(
                            "search-dynamodb.{Region}.{PartitionResult#dualStackDnsSuffix}",
                            p,
                            _locals,
                        ),
                    ):
                        raise EndpointError(
                            interpolate(
                                "Endpoint override is not supported for dual-stack endpoints. Please enable dual-stack functionality by enabling the configuration. For more details, see: https://docs.aws.amazon.com/sdkref/latest/guide/feature-endpoints.html",
                                p,
                                _locals,
                            )
                        )
                    return Endpoint(
                        url=interpolate("{Endpoint}", p, _locals),
                        properties={},
                        headers={},
                    )
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
        return Endpoint(
            url=interpolate("{Endpoint}", p, _locals), properties={}, headers={}
        )
    _locals: dict[str, Any] = {}
    if p.Region is not None:
        _locals["PartitionResult"] = aws_partition(p.Region)
        if _locals["PartitionResult"] is not None:
            if string_equals(p.Region, interpolate("local", p, _locals)):
                if p.UseFIPS is True:
                    raise EndpointError(
                        interpolate(
                            "Invalid Configuration: FIPS and local endpoint are not supported",
                            p,
                            _locals,
                        )
                    )
                if p.UseDualStack is True:
                    raise EndpointError(
                        interpolate(
                            "Invalid Configuration: Dualstack and local endpoint are not supported",
                            p,
                            _locals,
                        )
                    )
                return Endpoint(
                    url=interpolate("http://localhost:8000", p, _locals),
                    properties={
                        "authSchemes": [
                            {
                                "signingRegion": interpolate("us-east-1", p, _locals),
                                "signingName": interpolate("dynamodb", p, _locals),
                                "name": interpolate("sigv4", p, _locals),
                            }
                        ]
                    },
                    headers={},
                )
            if p.UseFIPS is True:
                if p.UseDualStack is True:
                    if (
                        get_attr(
                            _locals["PartitionResult"],
                            interpolate("supportsFIPS", p, _locals),
                        )
                        is True
                    ):
                        if (
                            get_attr(
                                _locals["PartitionResult"],
                                interpolate("supportsDualStack", p, _locals),
                            )
                            is True
                        ):
                            if p.AccountIdEndpointMode is not None:
                                if string_equals(
                                    p.AccountIdEndpointMode,
                                    interpolate("required", p, _locals),
                                ):
                                    raise EndpointError(
                                        interpolate(
                                            "Invalid Configuration: AccountIdEndpointMode is required and FIPS is enabled, but FIPS account endpoints are not supported",
                                            p,
                                            _locals,
                                        )
                                    )
                            if p.IsSearchOperation is not None:
                                if p.IsSearchOperation is True:
                                    return Endpoint(
                                        url=interpolate(
                                            "https://search-dynamodb-fips.{Region}.{PartitionResult#dualStackDnsSuffix}",
                                            p,
                                            _locals,
                                        ),
                                        properties={},
                                        headers={},
                                    )
                            return Endpoint(
                                url=interpolate(
                                    "https://dynamodb-fips.{Region}.{PartitionResult#dualStackDnsSuffix}",
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
                    if string_equals(
                        get_attr(
                            _locals["PartitionResult"], interpolate("name", p, _locals)
                        ),
                        interpolate("aws-us-gov", p, _locals),
                    ):
                        if p.AccountIdEndpointMode is not None:
                            if string_equals(
                                p.AccountIdEndpointMode,
                                interpolate("required", p, _locals),
                            ):
                                raise EndpointError(
                                    interpolate(
                                        "Invalid Configuration: AccountIdEndpointMode is required and FIPS is enabled, but FIPS account endpoints are not supported",
                                        p,
                                        _locals,
                                    )
                                )
                        if p.IsSearchOperation is not None:
                            if p.IsSearchOperation is True:
                                return Endpoint(
                                    url=interpolate(
                                        "https://search-dynamodb.{Region}.{PartitionResult#dnsSuffix}",
                                        p,
                                        _locals,
                                    ),
                                    properties={},
                                    headers={},
                                )
                        return Endpoint(
                            url=interpolate(
                                "https://dynamodb.{Region}.{PartitionResult#dnsSuffix}",
                                p,
                                _locals,
                            ),
                            properties={},
                            headers={},
                        )
                    if p.AccountIdEndpointMode is not None:
                        if string_equals(
                            p.AccountIdEndpointMode, interpolate("required", p, _locals)
                        ):
                            raise EndpointError(
                                interpolate(
                                    "Invalid Configuration: AccountIdEndpointMode is required and FIPS is enabled, but FIPS account endpoints are not supported",
                                    p,
                                    _locals,
                                )
                            )
                    if p.IsSearchOperation is not None:
                        if p.IsSearchOperation is True:
                            return Endpoint(
                                url=interpolate(
                                    "https://search-dynamodb-fips.{Region}.{PartitionResult#dnsSuffix}",
                                    p,
                                    _locals,
                                ),
                                properties={},
                                headers={},
                            )
                    return Endpoint(
                        url=interpolate(
                            "https://dynamodb-fips.{Region}.{PartitionResult#dnsSuffix}",
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
                if (
                    get_attr(
                        _locals["PartitionResult"],
                        interpolate("supportsDualStack", p, _locals),
                    )
                    is True
                ):
                    if p.AccountIdEndpointMode is not None:
                        if not (
                            string_equals(
                                p.AccountIdEndpointMode,
                                interpolate("disabled", p, _locals),
                            )
                        ):
                            if string_equals(
                                get_attr(
                                    _locals["PartitionResult"],
                                    interpolate("name", p, _locals),
                                ),
                                interpolate("aws", p, _locals),
                            ):
                                if p.UseFIPS is not True:
                                    if p.ResourceArn is not None:
                                        _locals["ParsedArn"] = aws_parse_arn(
                                            p.ResourceArn
                                        )
                                        if _locals["ParsedArn"] is not None:
                                            if string_equals(
                                                get_attr(
                                                    _locals["ParsedArn"],
                                                    interpolate("service", p, _locals),
                                                ),
                                                interpolate("dynamodb", p, _locals),
                                            ):
                                                if is_valid_host_label(
                                                    get_attr(
                                                        _locals["ParsedArn"],
                                                        interpolate(
                                                            "region", p, _locals
                                                        ),
                                                    ),
                                                    False,
                                                ):
                                                    if string_equals(
                                                        get_attr(
                                                            _locals["ParsedArn"],
                                                            interpolate(
                                                                "region", p, _locals
                                                            ),
                                                        ),
                                                        interpolate(
                                                            "{Region}", p, _locals
                                                        ),
                                                    ):
                                                        if is_valid_host_label(
                                                            get_attr(
                                                                _locals["ParsedArn"],
                                                                interpolate(
                                                                    "accountId",
                                                                    p,
                                                                    _locals,
                                                                ),
                                                            ),
                                                            False,
                                                        ):
                                                            if (
                                                                p.IsSearchOperation
                                                                is not None
                                                            ):
                                                                if (
                                                                    p.IsSearchOperation
                                                                    is True
                                                                ):
                                                                    return Endpoint(
                                                                        url=interpolate(
                                                                            "https://{ParsedArn#accountId}.search-ddb.{Region}.{PartitionResult#dualStackDnsSuffix}",
                                                                            p,
                                                                            _locals,
                                                                        ),
                                                                        properties={
                                                                            "metricValues": [
                                                                                interpolate(
                                                                                    "O",
                                                                                    p,
                                                                                    _locals,
                                                                                )
                                                                            ]
                                                                        },
                                                                        headers={},
                                                                    )
                                                            return Endpoint(
                                                                url=interpolate(
                                                                    "https://{ParsedArn#accountId}.ddb.{Region}.{PartitionResult#dualStackDnsSuffix}",
                                                                    p,
                                                                    _locals,
                                                                ),
                                                                properties={
                                                                    "metricValues": [
                                                                        interpolate(
                                                                            "O",
                                                                            p,
                                                                            _locals,
                                                                        )
                                                                    ]
                                                                },
                                                                headers={},
                                                            )
                    if p.AccountIdEndpointMode is not None:
                        if not (
                            string_equals(
                                p.AccountIdEndpointMode,
                                interpolate("disabled", p, _locals),
                            )
                        ):
                            if string_equals(
                                get_attr(
                                    _locals["PartitionResult"],
                                    interpolate("name", p, _locals),
                                ),
                                interpolate("aws", p, _locals),
                            ):
                                if p.UseFIPS is not True:
                                    if p.ResourceArnList is not None:
                                        _locals["FirstArn"] = get_attr(
                                            p.ResourceArnList,
                                            interpolate("[0]", p, _locals),
                                        )
                                        if _locals["FirstArn"] is not None:
                                            _locals["ParsedArn"] = aws_parse_arn(
                                                _locals["FirstArn"]
                                            )
                                            if _locals["ParsedArn"] is not None:
                                                if string_equals(
                                                    get_attr(
                                                        _locals["ParsedArn"],
                                                        interpolate(
                                                            "service", p, _locals
                                                        ),
                                                    ),
                                                    interpolate("dynamodb", p, _locals),
                                                ):
                                                    if is_valid_host_label(
                                                        get_attr(
                                                            _locals["ParsedArn"],
                                                            interpolate(
                                                                "region", p, _locals
                                                            ),
                                                        ),
                                                        False,
                                                    ):
                                                        if string_equals(
                                                            get_attr(
                                                                _locals["ParsedArn"],
                                                                interpolate(
                                                                    "region", p, _locals
                                                                ),
                                                            ),
                                                            interpolate(
                                                                "{Region}", p, _locals
                                                            ),
                                                        ):
                                                            if is_valid_host_label(
                                                                get_attr(
                                                                    _locals[
                                                                        "ParsedArn"
                                                                    ],
                                                                    interpolate(
                                                                        "accountId",
                                                                        p,
                                                                        _locals,
                                                                    ),
                                                                ),
                                                                False,
                                                            ):
                                                                if (
                                                                    p.IsSearchOperation
                                                                    is not None
                                                                ):
                                                                    if (
                                                                        p.IsSearchOperation
                                                                        is True
                                                                    ):
                                                                        return Endpoint(
                                                                            url=interpolate(
                                                                                "https://{ParsedArn#accountId}.search-ddb.{Region}.{PartitionResult#dualStackDnsSuffix}",
                                                                                p,
                                                                                _locals,
                                                                            ),
                                                                            properties={
                                                                                "metricValues": [
                                                                                    interpolate(
                                                                                        "O",
                                                                                        p,
                                                                                        _locals,
                                                                                    )
                                                                                ]
                                                                            },
                                                                            headers={},
                                                                        )
                                                                return Endpoint(
                                                                    url=interpolate(
                                                                        "https://{ParsedArn#accountId}.ddb.{Region}.{PartitionResult#dualStackDnsSuffix}",
                                                                        p,
                                                                        _locals,
                                                                    ),
                                                                    properties={
                                                                        "metricValues": [
                                                                            interpolate(
                                                                                "O",
                                                                                p,
                                                                                _locals,
                                                                            )
                                                                        ]
                                                                    },
                                                                    headers={},
                                                                )
                    if p.AccountIdEndpointMode is not None:
                        if not (
                            string_equals(
                                p.AccountIdEndpointMode,
                                interpolate("disabled", p, _locals),
                            )
                        ):
                            if string_equals(
                                get_attr(
                                    _locals["PartitionResult"],
                                    interpolate("name", p, _locals),
                                ),
                                interpolate("aws", p, _locals),
                            ):
                                if p.UseFIPS is not True:
                                    if p.AccountId is not None:
                                        if is_valid_host_label(p.AccountId, False):
                                            if p.IsSearchOperation is not None:
                                                if p.IsSearchOperation is True:
                                                    return Endpoint(
                                                        url=interpolate(
                                                            "https://{AccountId}.search-ddb.{Region}.{PartitionResult#dualStackDnsSuffix}",
                                                            p,
                                                            _locals,
                                                        ),
                                                        properties={
                                                            "metricValues": [
                                                                interpolate(
                                                                    "O", p, _locals
                                                                )
                                                            ]
                                                        },
                                                        headers={},
                                                    )
                                            return Endpoint(
                                                url=interpolate(
                                                    "https://{AccountId}.ddb.{Region}.{PartitionResult#dualStackDnsSuffix}",
                                                    p,
                                                    _locals,
                                                ),
                                                properties={
                                                    "metricValues": [
                                                        interpolate("O", p, _locals)
                                                    ]
                                                },
                                                headers={},
                                            )
                                        raise EndpointError(
                                            interpolate(
                                                "Credentials-sourced account ID parameter is invalid",
                                                p,
                                                _locals,
                                            )
                                        )
                    if p.AccountIdEndpointMode is not None:
                        if string_equals(
                            p.AccountIdEndpointMode, interpolate("required", p, _locals)
                        ):
                            if p.UseFIPS is not True:
                                if string_equals(
                                    get_attr(
                                        _locals["PartitionResult"],
                                        interpolate("name", p, _locals),
                                    ),
                                    interpolate("aws", p, _locals),
                                ):
                                    raise EndpointError(
                                        interpolate(
                                            "AccountIdEndpointMode is required but no AccountID was provided or able to be loaded",
                                            p,
                                            _locals,
                                        )
                                    )
                                raise EndpointError(
                                    interpolate(
                                        "Invalid Configuration: AccountIdEndpointMode is required but account endpoints are not supported in this partition",
                                        p,
                                        _locals,
                                    )
                                )
                            raise EndpointError(
                                interpolate(
                                    "Invalid Configuration: AccountIdEndpointMode is required and FIPS is enabled, but FIPS account endpoints are not supported",
                                    p,
                                    _locals,
                                )
                            )
                    if p.IsSearchOperation is not None:
                        if p.IsSearchOperation is True:
                            return Endpoint(
                                url=interpolate(
                                    "https://search-dynamodb.{Region}.{PartitionResult#dualStackDnsSuffix}",
                                    p,
                                    _locals,
                                ),
                                properties={},
                                headers={},
                            )
                    return Endpoint(
                        url=interpolate(
                            "https://dynamodb.{Region}.{PartitionResult#dualStackDnsSuffix}",
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
            if p.AccountIdEndpointMode is not None:
                if not (
                    string_equals(
                        p.AccountIdEndpointMode, interpolate("disabled", p, _locals)
                    )
                ):
                    if string_equals(
                        get_attr(
                            _locals["PartitionResult"], interpolate("name", p, _locals)
                        ),
                        interpolate("aws", p, _locals),
                    ):
                        if p.UseFIPS is not True:
                            if p.ResourceArn is not None:
                                _locals["ParsedArn"] = aws_parse_arn(p.ResourceArn)
                                if _locals["ParsedArn"] is not None:
                                    if string_equals(
                                        get_attr(
                                            _locals["ParsedArn"],
                                            interpolate("service", p, _locals),
                                        ),
                                        interpolate("dynamodb", p, _locals),
                                    ):
                                        if is_valid_host_label(
                                            get_attr(
                                                _locals["ParsedArn"],
                                                interpolate("region", p, _locals),
                                            ),
                                            False,
                                        ):
                                            if string_equals(
                                                get_attr(
                                                    _locals["ParsedArn"],
                                                    interpolate("region", p, _locals),
                                                ),
                                                interpolate("{Region}", p, _locals),
                                            ):
                                                if is_valid_host_label(
                                                    get_attr(
                                                        _locals["ParsedArn"],
                                                        interpolate(
                                                            "accountId", p, _locals
                                                        ),
                                                    ),
                                                    False,
                                                ):
                                                    if p.IsSearchOperation is not None:
                                                        if p.IsSearchOperation is True:
                                                            return Endpoint(
                                                                url=interpolate(
                                                                    "https://{ParsedArn#accountId}.search-ddb.{Region}.{PartitionResult#dnsSuffix}",
                                                                    p,
                                                                    _locals,
                                                                ),
                                                                properties={
                                                                    "metricValues": [
                                                                        interpolate(
                                                                            "O",
                                                                            p,
                                                                            _locals,
                                                                        )
                                                                    ]
                                                                },
                                                                headers={},
                                                            )
                                                    return Endpoint(
                                                        url=interpolate(
                                                            "https://{ParsedArn#accountId}.ddb.{Region}.{PartitionResult#dnsSuffix}",
                                                            p,
                                                            _locals,
                                                        ),
                                                        properties={
                                                            "metricValues": [
                                                                interpolate(
                                                                    "O", p, _locals
                                                                )
                                                            ]
                                                        },
                                                        headers={},
                                                    )
            if p.AccountIdEndpointMode is not None:
                if not (
                    string_equals(
                        p.AccountIdEndpointMode, interpolate("disabled", p, _locals)
                    )
                ):
                    if string_equals(
                        get_attr(
                            _locals["PartitionResult"], interpolate("name", p, _locals)
                        ),
                        interpolate("aws", p, _locals),
                    ):
                        if p.UseFIPS is not True:
                            if p.ResourceArnList is not None:
                                _locals["FirstArn"] = get_attr(
                                    p.ResourceArnList, interpolate("[0]", p, _locals)
                                )
                                if _locals["FirstArn"] is not None:
                                    _locals["ParsedArn"] = aws_parse_arn(
                                        _locals["FirstArn"]
                                    )
                                    if _locals["ParsedArn"] is not None:
                                        if string_equals(
                                            get_attr(
                                                _locals["ParsedArn"],
                                                interpolate("service", p, _locals),
                                            ),
                                            interpolate("dynamodb", p, _locals),
                                        ):
                                            if is_valid_host_label(
                                                get_attr(
                                                    _locals["ParsedArn"],
                                                    interpolate("region", p, _locals),
                                                ),
                                                False,
                                            ):
                                                if string_equals(
                                                    get_attr(
                                                        _locals["ParsedArn"],
                                                        interpolate(
                                                            "region", p, _locals
                                                        ),
                                                    ),
                                                    interpolate("{Region}", p, _locals),
                                                ):
                                                    if is_valid_host_label(
                                                        get_attr(
                                                            _locals["ParsedArn"],
                                                            interpolate(
                                                                "accountId", p, _locals
                                                            ),
                                                        ),
                                                        False,
                                                    ):
                                                        if (
                                                            p.IsSearchOperation
                                                            is not None
                                                        ):
                                                            if (
                                                                p.IsSearchOperation
                                                                is True
                                                            ):
                                                                return Endpoint(
                                                                    url=interpolate(
                                                                        "https://{ParsedArn#accountId}.search-ddb.{Region}.{PartitionResult#dnsSuffix}",
                                                                        p,
                                                                        _locals,
                                                                    ),
                                                                    properties={
                                                                        "metricValues": [
                                                                            interpolate(
                                                                                "O",
                                                                                p,
                                                                                _locals,
                                                                            )
                                                                        ]
                                                                    },
                                                                    headers={},
                                                                )
                                                        return Endpoint(
                                                            url=interpolate(
                                                                "https://{ParsedArn#accountId}.ddb.{Region}.{PartitionResult#dnsSuffix}",
                                                                p,
                                                                _locals,
                                                            ),
                                                            properties={
                                                                "metricValues": [
                                                                    interpolate(
                                                                        "O", p, _locals
                                                                    )
                                                                ]
                                                            },
                                                            headers={},
                                                        )
            if p.AccountIdEndpointMode is not None:
                if not (
                    string_equals(
                        p.AccountIdEndpointMode, interpolate("disabled", p, _locals)
                    )
                ):
                    if string_equals(
                        get_attr(
                            _locals["PartitionResult"], interpolate("name", p, _locals)
                        ),
                        interpolate("aws", p, _locals),
                    ):
                        if p.UseFIPS is not True:
                            if p.AccountId is not None:
                                if is_valid_host_label(p.AccountId, False):
                                    if p.IsSearchOperation is not None:
                                        if p.IsSearchOperation is True:
                                            return Endpoint(
                                                url=interpolate(
                                                    "https://{AccountId}.search-ddb.{Region}.{PartitionResult#dnsSuffix}",
                                                    p,
                                                    _locals,
                                                ),
                                                properties={
                                                    "metricValues": [
                                                        interpolate("O", p, _locals)
                                                    ]
                                                },
                                                headers={},
                                            )
                                    return Endpoint(
                                        url=interpolate(
                                            "https://{AccountId}.ddb.{Region}.{PartitionResult#dnsSuffix}",
                                            p,
                                            _locals,
                                        ),
                                        properties={
                                            "metricValues": [
                                                interpolate("O", p, _locals)
                                            ]
                                        },
                                        headers={},
                                    )
                                raise EndpointError(
                                    interpolate(
                                        "Credentials-sourced account ID parameter is invalid",
                                        p,
                                        _locals,
                                    )
                                )
            if p.AccountIdEndpointMode is not None:
                if string_equals(
                    p.AccountIdEndpointMode, interpolate("required", p, _locals)
                ):
                    if p.UseFIPS is not True:
                        if string_equals(
                            get_attr(
                                _locals["PartitionResult"],
                                interpolate("name", p, _locals),
                            ),
                            interpolate("aws", p, _locals),
                        ):
                            raise EndpointError(
                                interpolate(
                                    "AccountIdEndpointMode is required but no AccountID was provided or able to be loaded",
                                    p,
                                    _locals,
                                )
                            )
                        raise EndpointError(
                            interpolate(
                                "Invalid Configuration: AccountIdEndpointMode is required but account endpoints are not supported in this partition",
                                p,
                                _locals,
                            )
                        )
                    raise EndpointError(
                        interpolate(
                            "Invalid Configuration: AccountIdEndpointMode is required and FIPS is enabled, but FIPS account endpoints are not supported",
                            p,
                            _locals,
                        )
                    )
            if p.IsSearchOperation is not None:
                if p.IsSearchOperation is True:
                    return Endpoint(
                        url=interpolate(
                            "https://search-dynamodb.{Region}.{PartitionResult#dnsSuffix}",
                            p,
                            _locals,
                        ),
                        properties={},
                        headers={},
                    )
            return Endpoint(
                url=interpolate(
                    "https://dynamodb.{Region}.{PartitionResult#dnsSuffix}", p, _locals
                ),
                properties={},
                headers={},
            )
    _locals: dict[str, Any] = {}
    raise EndpointError(
        interpolate("Invalid Configuration: Missing Region", p, _locals)
    )
    raise EndpointError("No endpoint rules matched")
