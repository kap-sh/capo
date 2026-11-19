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
        StreamArn: str | None = None,
        ShardIterator: str | None = None,
    ):
        self.UseDualStack = UseDualStack if UseDualStack is not None else False
        self.UseFIPS = UseFIPS if UseFIPS is not None else False
        self.Region = Region if Region is not None else None
        self.Endpoint = Endpoint if Endpoint is not None else None
        self.AccountId = AccountId if AccountId is not None else None
        self.AccountIdEndpointMode = (
            AccountIdEndpointMode if AccountIdEndpointMode is not None else None
        )
        self.StreamArn = StreamArn if StreamArn is not None else None
        self.ShardIterator = ShardIterator if ShardIterator is not None else None


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
        return Endpoint(
            url=interpolate("{Endpoint}", p, _locals), properties={}, headers={}
        )
    _locals: dict[str, Any] = {}
    if p.Region is not None:
        _locals["PartitionResult"] = aws_partition(p.Region)
        if _locals["PartitionResult"] is not None:
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
                            if not (
                                string_equals(
                                    get_attr(
                                        _locals["PartitionResult"],
                                        interpolate("name", p, _locals),
                                    ),
                                    interpolate("aws", p, _locals),
                                )
                            ):
                                if not (
                                    string_equals(
                                        get_attr(
                                            _locals["PartitionResult"],
                                            interpolate("name", p, _locals),
                                        ),
                                        interpolate("aws-cn", p, _locals),
                                    )
                                ):
                                    if not (
                                        string_equals(
                                            get_attr(
                                                _locals["PartitionResult"],
                                                interpolate("name", p, _locals),
                                            ),
                                            interpolate("aws-us-gov", p, _locals),
                                        )
                                    ):
                                        if p.AccountIdEndpointMode is not None:
                                            if string_equals(
                                                p.AccountIdEndpointMode,
                                                interpolate("required", p, _locals),
                                            ):
                                                raise EndpointError(
                                                    interpolate(
                                                        "Invalid Configuration: AccountIdEndpointMode is required but account endpoints are not supported in this region",
                                                        p,
                                                        _locals,
                                                    )
                                                )
                                        return Endpoint(
                                            url=interpolate(
                                                "https://streams-dynamodb-fips.{Region}.{PartitionResult#dualStackDnsSuffix}",
                                                p,
                                                _locals,
                                            ),
                                            properties={},
                                            headers={},
                                        )
                            if string_equals(
                                p.Region, interpolate("me-central-1", p, _locals)
                            ):
                                if p.AccountIdEndpointMode is not None:
                                    if string_equals(
                                        p.AccountIdEndpointMode,
                                        interpolate("required", p, _locals),
                                    ):
                                        raise EndpointError(
                                            interpolate(
                                                "Invalid Configuration: AccountIdEndpointMode is required but account endpoints are not supported in this region",
                                                p,
                                                _locals,
                                            )
                                        )
                                return Endpoint(
                                    url=interpolate(
                                        "https://streams-dynamodb-fips.{Region}.{PartitionResult#dualStackDnsSuffix}",
                                        p,
                                        _locals,
                                    ),
                                    properties={},
                                    headers={},
                                )
                            if string_equals(
                                p.Region, interpolate("me-south-1", p, _locals)
                            ):
                                if p.AccountIdEndpointMode is not None:
                                    if string_equals(
                                        p.AccountIdEndpointMode,
                                        interpolate("required", p, _locals),
                                    ):
                                        raise EndpointError(
                                            interpolate(
                                                "Invalid Configuration: AccountIdEndpointMode is required but account endpoints are not supported in this region",
                                                p,
                                                _locals,
                                            )
                                        )
                                return Endpoint(
                                    url=interpolate(
                                        "https://streams-dynamodb-fips.{Region}.{PartitionResult#dualStackDnsSuffix}",
                                        p,
                                        _locals,
                                    ),
                                    properties={},
                                    headers={},
                                )
                            if p.AccountIdEndpointMode is not None:
                                if not (
                                    string_equals(
                                        p.AccountIdEndpointMode,
                                        interpolate("disabled", p, _locals),
                                    )
                                ):
                                    if p.StreamArn is not None:
                                        _locals["ParsedArn"] = aws_parse_arn(
                                            p.StreamArn
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
                                                            return Endpoint(
                                                                url=interpolate(
                                                                    "https://{ParsedArn#accountId}.streams-ddb-fips.{Region}.{PartitionResult#dualStackDnsSuffix}",
                                                                    p,
                                                                    _locals,
                                                                ),
                                                                properties={},
                                                                headers={},
                                                            )
                            if p.AccountIdEndpointMode is not None:
                                if not (
                                    string_equals(
                                        p.AccountIdEndpointMode,
                                        interpolate("disabled", p, _locals),
                                    )
                                ):
                                    if p.ShardIterator is not None:
                                        _locals["ParsedArn"] = aws_parse_arn(
                                            p.ShardIterator
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
                                                            return Endpoint(
                                                                url=interpolate(
                                                                    "https://{ParsedArn#accountId}.streams-ddb-fips.{Region}.{PartitionResult#dualStackDnsSuffix}",
                                                                    p,
                                                                    _locals,
                                                                ),
                                                                properties={},
                                                                headers={},
                                                            )
                            if p.AccountIdEndpointMode is not None:
                                if not (
                                    string_equals(
                                        p.AccountIdEndpointMode,
                                        interpolate("disabled", p, _locals),
                                    )
                                ):
                                    if p.AccountId is not None:
                                        if is_valid_host_label(p.AccountId, False):
                                            return Endpoint(
                                                url=interpolate(
                                                    "https://{AccountId}.streams-ddb-fips.{Region}.{PartitionResult#dualStackDnsSuffix}",
                                                    p,
                                                    _locals,
                                                ),
                                                properties={},
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
                                    p.AccountIdEndpointMode,
                                    interpolate("required", p, _locals),
                                ):
                                    raise EndpointError(
                                        interpolate(
                                            "AccountIdEndpointMode is required but no AccountID was provided or able to be loaded",
                                            p,
                                            _locals,
                                        )
                                    )
                            return Endpoint(
                                url=interpolate(
                                    "https://streams-dynamodb-fips.{Region}.{PartitionResult#dualStackDnsSuffix}",
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
                        if not (
                            string_equals(
                                get_attr(
                                    _locals["PartitionResult"],
                                    interpolate("name", p, _locals),
                                ),
                                interpolate("aws", p, _locals),
                            )
                        ):
                            if not (
                                string_equals(
                                    get_attr(
                                        _locals["PartitionResult"],
                                        interpolate("name", p, _locals),
                                    ),
                                    interpolate("aws-cn", p, _locals),
                                )
                            ):
                                if not (
                                    string_equals(
                                        get_attr(
                                            _locals["PartitionResult"],
                                            interpolate("name", p, _locals),
                                        ),
                                        interpolate("aws-us-gov", p, _locals),
                                    )
                                ):
                                    if p.AccountIdEndpointMode is not None:
                                        if string_equals(
                                            p.AccountIdEndpointMode,
                                            interpolate("required", p, _locals),
                                        ):
                                            raise EndpointError(
                                                interpolate(
                                                    "Invalid Configuration: AccountIdEndpointMode is required but account endpoints are not supported in this region",
                                                    p,
                                                    _locals,
                                                )
                                            )
                                    return Endpoint(
                                        url=interpolate(
                                            "https://streams.dynamodb.{Region}.{PartitionResult#dnsSuffix}",
                                            p,
                                            _locals,
                                        ),
                                        properties={},
                                        headers={},
                                    )
                        if string_equals(
                            p.Region, interpolate("me-central-1", p, _locals)
                        ):
                            if p.AccountIdEndpointMode is not None:
                                if string_equals(
                                    p.AccountIdEndpointMode,
                                    interpolate("required", p, _locals),
                                ):
                                    raise EndpointError(
                                        interpolate(
                                            "Invalid Configuration: AccountIdEndpointMode is required but account endpoints are not supported in this region",
                                            p,
                                            _locals,
                                        )
                                    )
                            return Endpoint(
                                url=interpolate(
                                    "https://streams.dynamodb.{Region}.{PartitionResult#dnsSuffix}",
                                    p,
                                    _locals,
                                ),
                                properties={},
                                headers={},
                            )
                        if string_equals(
                            p.Region, interpolate("me-south-1", p, _locals)
                        ):
                            if p.AccountIdEndpointMode is not None:
                                if string_equals(
                                    p.AccountIdEndpointMode,
                                    interpolate("required", p, _locals),
                                ):
                                    raise EndpointError(
                                        interpolate(
                                            "Invalid Configuration: AccountIdEndpointMode is required but account endpoints are not supported in this region",
                                            p,
                                            _locals,
                                        )
                                    )
                            return Endpoint(
                                url=interpolate(
                                    "https://streams.dynamodb.{Region}.{PartitionResult#dnsSuffix}",
                                    p,
                                    _locals,
                                ),
                                properties={},
                                headers={},
                            )
                        if p.AccountIdEndpointMode is not None:
                            if not (
                                string_equals(
                                    p.AccountIdEndpointMode,
                                    interpolate("disabled", p, _locals),
                                )
                            ):
                                if p.StreamArn is not None:
                                    _locals["ParsedArn"] = aws_parse_arn(p.StreamArn)
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
                                                        return Endpoint(
                                                            url=interpolate(
                                                                "https://{ParsedArn#accountId}.streams-ddb-fips.{Region}.{PartitionResult#dnsSuffix}",
                                                                p,
                                                                _locals,
                                                            ),
                                                            properties={},
                                                            headers={},
                                                        )
                        if p.AccountIdEndpointMode is not None:
                            if not (
                                string_equals(
                                    p.AccountIdEndpointMode,
                                    interpolate("disabled", p, _locals),
                                )
                            ):
                                if p.ShardIterator is not None:
                                    _locals["ParsedArn"] = aws_parse_arn(
                                        p.ShardIterator
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
                                                        return Endpoint(
                                                            url=interpolate(
                                                                "https://{ParsedArn#accountId}.streams-ddb-fips.{Region}.{PartitionResult#dnsSuffix}",
                                                                p,
                                                                _locals,
                                                            ),
                                                            properties={},
                                                            headers={},
                                                        )
                        if p.AccountIdEndpointMode is not None:
                            if not (
                                string_equals(
                                    p.AccountIdEndpointMode,
                                    interpolate("disabled", p, _locals),
                                )
                            ):
                                if p.AccountId is not None:
                                    if is_valid_host_label(p.AccountId, False):
                                        return Endpoint(
                                            url=interpolate(
                                                "https://{AccountId}.streams-ddb-fips.{Region}.{PartitionResult#dnsSuffix}",
                                                p,
                                                _locals,
                                            ),
                                            properties={},
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
                                p.AccountIdEndpointMode,
                                interpolate("required", p, _locals),
                            ):
                                raise EndpointError(
                                    interpolate(
                                        "AccountIdEndpointMode is required but no AccountID was provided or able to be loaded",
                                        p,
                                        _locals,
                                    )
                                )
                        return Endpoint(
                            url=interpolate(
                                "https://streams.dynamodb.{Region}.{PartitionResult#dnsSuffix}",
                                p,
                                _locals,
                            ),
                            properties={},
                            headers={},
                        )
                    if not (
                        string_equals(
                            get_attr(
                                _locals["PartitionResult"],
                                interpolate("name", p, _locals),
                            ),
                            interpolate("aws", p, _locals),
                        )
                    ):
                        if not (
                            string_equals(
                                get_attr(
                                    _locals["PartitionResult"],
                                    interpolate("name", p, _locals),
                                ),
                                interpolate("aws-cn", p, _locals),
                            )
                        ):
                            if not (
                                string_equals(
                                    get_attr(
                                        _locals["PartitionResult"],
                                        interpolate("name", p, _locals),
                                    ),
                                    interpolate("aws-us-gov", p, _locals),
                                )
                            ):
                                if p.AccountIdEndpointMode is not None:
                                    if string_equals(
                                        p.AccountIdEndpointMode,
                                        interpolate("required", p, _locals),
                                    ):
                                        raise EndpointError(
                                            interpolate(
                                                "Invalid Configuration: AccountIdEndpointMode is required but account endpoints are not supported in this region",
                                                p,
                                                _locals,
                                            )
                                        )
                                return Endpoint(
                                    url=interpolate(
                                        "https://streams.dynamodb-fips.{Region}.{PartitionResult#dnsSuffix}",
                                        p,
                                        _locals,
                                    ),
                                    properties={},
                                    headers={},
                                )
                    if string_equals(p.Region, interpolate("me-central-1", p, _locals)):
                        if p.AccountIdEndpointMode is not None:
                            if string_equals(
                                p.AccountIdEndpointMode,
                                interpolate("required", p, _locals),
                            ):
                                raise EndpointError(
                                    interpolate(
                                        "Invalid Configuration: AccountIdEndpointMode is required but account endpoints are not supported in this region",
                                        p,
                                        _locals,
                                    )
                                )
                        return Endpoint(
                            url=interpolate(
                                "https://streams.dynamodb-fips.{Region}.{PartitionResult#dnsSuffix}",
                                p,
                                _locals,
                            ),
                            properties={},
                            headers={},
                        )
                    if string_equals(p.Region, interpolate("me-south-1", p, _locals)):
                        if p.AccountIdEndpointMode is not None:
                            if string_equals(
                                p.AccountIdEndpointMode,
                                interpolate("required", p, _locals),
                            ):
                                raise EndpointError(
                                    interpolate(
                                        "Invalid Configuration: AccountIdEndpointMode is required but account endpoints are not supported in this region",
                                        p,
                                        _locals,
                                    )
                                )
                        return Endpoint(
                            url=interpolate(
                                "https://streams.dynamodb-fips.{Region}.{PartitionResult#dnsSuffix}",
                                p,
                                _locals,
                            ),
                            properties={},
                            headers={},
                        )
                    if p.AccountIdEndpointMode is not None:
                        if not (
                            string_equals(
                                p.AccountIdEndpointMode,
                                interpolate("disabled", p, _locals),
                            )
                        ):
                            if p.StreamArn is not None:
                                _locals["ParsedArn"] = aws_parse_arn(p.StreamArn)
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
                                                    return Endpoint(
                                                        url=interpolate(
                                                            "https://{ParsedArn#accountId}.streams-ddb-fips.{Region}.{PartitionResult#dnsSuffix}",
                                                            p,
                                                            _locals,
                                                        ),
                                                        properties={},
                                                        headers={},
                                                    )
                    if p.AccountIdEndpointMode is not None:
                        if not (
                            string_equals(
                                p.AccountIdEndpointMode,
                                interpolate("disabled", p, _locals),
                            )
                        ):
                            if p.ShardIterator is not None:
                                _locals["ParsedArn"] = aws_parse_arn(p.ShardIterator)
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
                                                    return Endpoint(
                                                        url=interpolate(
                                                            "https://{ParsedArn#accountId}.streams-ddb-fips.{Region}.{PartitionResult#dnsSuffix}",
                                                            p,
                                                            _locals,
                                                        ),
                                                        properties={},
                                                        headers={},
                                                    )
                    if p.AccountIdEndpointMode is not None:
                        if not (
                            string_equals(
                                p.AccountIdEndpointMode,
                                interpolate("disabled", p, _locals),
                            )
                        ):
                            if p.AccountId is not None:
                                if is_valid_host_label(p.AccountId, False):
                                    return Endpoint(
                                        url=interpolate(
                                            "https://{AccountId}.streams-ddb-fips.{Region}.{PartitionResult#dnsSuffix}",
                                            p,
                                            _locals,
                                        ),
                                        properties={},
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
                            raise EndpointError(
                                interpolate(
                                    "AccountIdEndpointMode is required but no AccountID was provided or able to be loaded",
                                    p,
                                    _locals,
                                )
                            )
                    return Endpoint(
                        url=interpolate(
                            "https://streams.dynamodb-fips.{Region}.{PartitionResult#dnsSuffix}",
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
                    if not (
                        string_equals(
                            get_attr(
                                _locals["PartitionResult"],
                                interpolate("name", p, _locals),
                            ),
                            interpolate("aws", p, _locals),
                        )
                    ):
                        if not (
                            string_equals(
                                get_attr(
                                    _locals["PartitionResult"],
                                    interpolate("name", p, _locals),
                                ),
                                interpolate("aws-cn", p, _locals),
                            )
                        ):
                            if not (
                                string_equals(
                                    get_attr(
                                        _locals["PartitionResult"],
                                        interpolate("name", p, _locals),
                                    ),
                                    interpolate("aws-us-gov", p, _locals),
                                )
                            ):
                                if p.AccountIdEndpointMode is not None:
                                    if string_equals(
                                        p.AccountIdEndpointMode,
                                        interpolate("required", p, _locals),
                                    ):
                                        raise EndpointError(
                                            interpolate(
                                                "Invalid Configuration: AccountIdEndpointMode is required but account endpoints are not supported in this region",
                                                p,
                                                _locals,
                                            )
                                        )
                                return Endpoint(
                                    url=interpolate(
                                        "https://streams-dynamodb.{Region}.{PartitionResult#dualStackDnsSuffix}",
                                        p,
                                        _locals,
                                    ),
                                    properties={},
                                    headers={},
                                )
                    if string_equals(p.Region, interpolate("me-central-1", p, _locals)):
                        if p.AccountIdEndpointMode is not None:
                            if string_equals(
                                p.AccountIdEndpointMode,
                                interpolate("required", p, _locals),
                            ):
                                raise EndpointError(
                                    interpolate(
                                        "Invalid Configuration: AccountIdEndpointMode is required but account endpoints are not supported in this region",
                                        p,
                                        _locals,
                                    )
                                )
                        return Endpoint(
                            url=interpolate(
                                "https://streams-dynamodb.{Region}.{PartitionResult#dualStackDnsSuffix}",
                                p,
                                _locals,
                            ),
                            properties={},
                            headers={},
                        )
                    if string_equals(p.Region, interpolate("me-south-1", p, _locals)):
                        if p.AccountIdEndpointMode is not None:
                            if string_equals(
                                p.AccountIdEndpointMode,
                                interpolate("required", p, _locals),
                            ):
                                raise EndpointError(
                                    interpolate(
                                        "Invalid Configuration: AccountIdEndpointMode is required but account endpoints are not supported in this region",
                                        p,
                                        _locals,
                                    )
                                )
                        return Endpoint(
                            url=interpolate(
                                "https://streams-dynamodb.{Region}.{PartitionResult#dualStackDnsSuffix}",
                                p,
                                _locals,
                            ),
                            properties={},
                            headers={},
                        )
                    if p.AccountIdEndpointMode is not None:
                        if not (
                            string_equals(
                                p.AccountIdEndpointMode,
                                interpolate("disabled", p, _locals),
                            )
                        ):
                            if p.StreamArn is not None:
                                _locals["ParsedArn"] = aws_parse_arn(p.StreamArn)
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
                                                    return Endpoint(
                                                        url=interpolate(
                                                            "https://{ParsedArn#accountId}.streams-ddb.{Region}.{PartitionResult#dualStackDnsSuffix}",
                                                            p,
                                                            _locals,
                                                        ),
                                                        properties={},
                                                        headers={},
                                                    )
                    if p.AccountIdEndpointMode is not None:
                        if not (
                            string_equals(
                                p.AccountIdEndpointMode,
                                interpolate("disabled", p, _locals),
                            )
                        ):
                            if p.ShardIterator is not None:
                                _locals["ParsedArn"] = aws_parse_arn(p.ShardIterator)
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
                                                    return Endpoint(
                                                        url=interpolate(
                                                            "https://{ParsedArn#accountId}.streams-ddb.{Region}.{PartitionResult#dualStackDnsSuffix}",
                                                            p,
                                                            _locals,
                                                        ),
                                                        properties={},
                                                        headers={},
                                                    )
                    if p.AccountIdEndpointMode is not None:
                        if not (
                            string_equals(
                                p.AccountIdEndpointMode,
                                interpolate("disabled", p, _locals),
                            )
                        ):
                            if p.AccountId is not None:
                                if is_valid_host_label(p.AccountId, False):
                                    return Endpoint(
                                        url=interpolate(
                                            "https://{AccountId}.streams-ddb.{Region}.{PartitionResult#dualStackDnsSuffix}",
                                            p,
                                            _locals,
                                        ),
                                        properties={},
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
                            raise EndpointError(
                                interpolate(
                                    "AccountIdEndpointMode is required but no AccountID was provided or able to be loaded",
                                    p,
                                    _locals,
                                )
                            )
                    return Endpoint(
                        url=interpolate(
                            "https://streams-dynamodb.{Region}.{PartitionResult#dualStackDnsSuffix}",
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
            if not (
                string_equals(
                    get_attr(
                        _locals["PartitionResult"], interpolate("name", p, _locals)
                    ),
                    interpolate("aws", p, _locals),
                )
            ):
                if not (
                    string_equals(
                        get_attr(
                            _locals["PartitionResult"], interpolate("name", p, _locals)
                        ),
                        interpolate("aws-cn", p, _locals),
                    )
                ):
                    if not (
                        string_equals(
                            get_attr(
                                _locals["PartitionResult"],
                                interpolate("name", p, _locals),
                            ),
                            interpolate("aws-us-gov", p, _locals),
                        )
                    ):
                        if p.AccountIdEndpointMode is not None:
                            if string_equals(
                                p.AccountIdEndpointMode,
                                interpolate("required", p, _locals),
                            ):
                                raise EndpointError(
                                    interpolate(
                                        "Invalid Configuration: AccountIdEndpointMode is required but account endpoints are not supported in this region",
                                        p,
                                        _locals,
                                    )
                                )
                        return Endpoint(
                            url=interpolate(
                                "https://streams.dynamodb.{Region}.{PartitionResult#dnsSuffix}",
                                p,
                                _locals,
                            ),
                            properties={},
                            headers={},
                        )
            if string_equals(p.Region, interpolate("me-central-1", p, _locals)):
                if p.AccountIdEndpointMode is not None:
                    if string_equals(
                        p.AccountIdEndpointMode, interpolate("required", p, _locals)
                    ):
                        raise EndpointError(
                            interpolate(
                                "Invalid Configuration: AccountIdEndpointMode is required but account endpoints are not supported in this region",
                                p,
                                _locals,
                            )
                        )
                return Endpoint(
                    url=interpolate(
                        "https://streams.dynamodb.{Region}.{PartitionResult#dnsSuffix}",
                        p,
                        _locals,
                    ),
                    properties={},
                    headers={},
                )
            if string_equals(p.Region, interpolate("me-south-1", p, _locals)):
                if p.AccountIdEndpointMode is not None:
                    if string_equals(
                        p.AccountIdEndpointMode, interpolate("required", p, _locals)
                    ):
                        raise EndpointError(
                            interpolate(
                                "Invalid Configuration: AccountIdEndpointMode is required but account endpoints are not supported in this region",
                                p,
                                _locals,
                            )
                        )
                return Endpoint(
                    url=interpolate(
                        "https://streams.dynamodb.{Region}.{PartitionResult#dnsSuffix}",
                        p,
                        _locals,
                    ),
                    properties={},
                    headers={},
                )
            if p.AccountIdEndpointMode is not None:
                if not (
                    string_equals(
                        p.AccountIdEndpointMode, interpolate("disabled", p, _locals)
                    )
                ):
                    if p.StreamArn is not None:
                        _locals["ParsedArn"] = aws_parse_arn(p.StreamArn)
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
                                                interpolate("accountId", p, _locals),
                                            ),
                                            False,
                                        ):
                                            return Endpoint(
                                                url=interpolate(
                                                    "https://{ParsedArn#accountId}.streams-ddb.{Region}.{PartitionResult#dnsSuffix}",
                                                    p,
                                                    _locals,
                                                ),
                                                properties={},
                                                headers={},
                                            )
            if p.AccountIdEndpointMode is not None:
                if not (
                    string_equals(
                        p.AccountIdEndpointMode, interpolate("disabled", p, _locals)
                    )
                ):
                    if p.ShardIterator is not None:
                        _locals["ParsedArn"] = aws_parse_arn(p.ShardIterator)
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
                                                interpolate("accountId", p, _locals),
                                            ),
                                            False,
                                        ):
                                            return Endpoint(
                                                url=interpolate(
                                                    "https://{ParsedArn#accountId}.streams-ddb.{Region}.{PartitionResult#dnsSuffix}",
                                                    p,
                                                    _locals,
                                                ),
                                                properties={},
                                                headers={},
                                            )
            if p.AccountIdEndpointMode is not None:
                if not (
                    string_equals(
                        p.AccountIdEndpointMode, interpolate("disabled", p, _locals)
                    )
                ):
                    if p.AccountId is not None:
                        if is_valid_host_label(p.AccountId, False):
                            return Endpoint(
                                url=interpolate(
                                    "https://{AccountId}.streams-ddb.{Region}.{PartitionResult#dnsSuffix}",
                                    p,
                                    _locals,
                                ),
                                properties={},
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
                    raise EndpointError(
                        interpolate(
                            "AccountIdEndpointMode is required but no AccountID was provided or able to be loaded",
                            p,
                            _locals,
                        )
                    )
            return Endpoint(
                url=interpolate(
                    "https://streams.dynamodb.{Region}.{PartitionResult#dnsSuffix}",
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
