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
    substring,
)


class EndpointParams:
    def __init__(
        self,
        *,
        UseDualStack: bool | None = None,
        UseFIPS: bool | None = None,
        ResourceType: str | None = None,
        Region: str | None = None,
        Endpoint: str | None = None,
        OperationType: str | None = None,
        StreamId: str | None = None,
        StreamARN: str | None = None,
        ConsumerARN: str | None = None,
        ResourceARN: str | None = None,
        ChannelARN: str | None = None,
        QueueARN: str | None = None,
        AccountId: str | None = None,
        AccountIdEndpointMode: str | None = None,
    ):
        self.UseDualStack = UseDualStack if UseDualStack is not None else False
        self.UseFIPS = UseFIPS if UseFIPS is not None else False
        self.ResourceType = ResourceType if ResourceType is not None else ""
        self.Region = Region if Region is not None else None
        self.Endpoint = Endpoint if Endpoint is not None else None
        self.OperationType = OperationType if OperationType is not None else None
        self.StreamId = StreamId if StreamId is not None else None
        self.StreamARN = StreamARN if StreamARN is not None else None
        self.ConsumerARN = ConsumerARN if ConsumerARN is not None else None
        self.ResourceARN = ResourceARN if ResourceARN is not None else None
        self.ChannelARN = ChannelARN if ChannelARN is not None else None
        self.QueueARN = QueueARN if QueueARN is not None else None
        self.AccountId = AccountId if AccountId is not None else None
        self.AccountIdEndpointMode = (
            AccountIdEndpointMode if AccountIdEndpointMode is not None else None
        )


def resolve(p: EndpointParams) -> Endpoint:  # type: ignore
    """Resolve endpoint from parameters using generated ruleset."""
    _locals: dict[str, Any] = {}
    if p.StreamId is not None:
        _locals["StreamIdDelimiterValue"] = substring(p.StreamId, 20, 21, False)
        if _locals["StreamIdDelimiterValue"] is not None:
            if string_equals(
                _locals["StreamIdDelimiterValue"], interpolate("-", p, _locals)
            ):
                _locals["StreamIdDelimiterReversedValue"] = substring(
                    p.StreamId, 3, 4, True
                )
                if _locals["StreamIdDelimiterReversedValue"] is not None:
                    if string_equals(
                        _locals["StreamIdDelimiterReversedValue"],
                        interpolate("-", p, _locals),
                    ):
                        _locals["StreamIdPrefixValue"] = substring(
                            p.StreamId, 0, 20, False
                        )
                        if _locals["StreamIdPrefixValue"] is not None:
                            _locals["StreamIdSuffixValue"] = substring(
                                p.StreamId, 21, 24, False
                            )
                            if _locals["StreamIdSuffixValue"] is not None:
                                if p.Region is not None:
                                    _locals["PartitionResult"] = aws_partition(p.Region)
                                    if _locals["PartitionResult"] is not None:
                                        if not (
                                            string_equals(
                                                get_attr(
                                                    _locals["PartitionResult"],
                                                    interpolate("name", p, _locals),
                                                ),
                                                interpolate("aws-iso", p, _locals),
                                            )
                                        ):
                                            if not (
                                                string_equals(
                                                    get_attr(
                                                        _locals["PartitionResult"],
                                                        interpolate("name", p, _locals),
                                                    ),
                                                    interpolate(
                                                        "aws-iso-b", p, _locals
                                                    ),
                                                )
                                            ):
                                                if p.OperationType is not None:
                                                    if p.Endpoint is not None:
                                                        _locals[
                                                            "HttpsCustomEndpointDelimiterValue"
                                                        ] = substring(
                                                            p.Endpoint, 15, 16, False
                                                        )
                                                        if (
                                                            _locals[
                                                                "HttpsCustomEndpointDelimiterValue"
                                                            ]
                                                            is not None
                                                        ):
                                                            if string_equals(
                                                                _locals[
                                                                    "HttpsCustomEndpointDelimiterValue"
                                                                ],
                                                                interpolate(
                                                                    "-", p, _locals
                                                                ),
                                                            ):
                                                                _locals[
                                                                    "HttpsEndpointDelimiterValue"
                                                                ] = substring(
                                                                    p.Endpoint,
                                                                    20,
                                                                    21,
                                                                    False,
                                                                )
                                                                if (
                                                                    _locals[
                                                                        "HttpsEndpointDelimiterValue"
                                                                    ]
                                                                    is not None
                                                                ):
                                                                    if string_equals(
                                                                        _locals[
                                                                            "HttpsEndpointDelimiterValue"
                                                                        ],
                                                                        interpolate(
                                                                            ".",
                                                                            p,
                                                                            _locals,
                                                                        ),
                                                                    ):
                                                                        _locals[
                                                                            "HttpsCustomEndpointSuffixValue"
                                                                        ] = substring(
                                                                            p.Endpoint,
                                                                            15,
                                                                            20,
                                                                            False,
                                                                        )
                                                                        if (
                                                                            _locals[
                                                                                "HttpsCustomEndpointSuffixValue"
                                                                            ]
                                                                            is not None
                                                                        ):
                                                                            if (
                                                                                p.UseFIPS
                                                                                is True
                                                                            ):
                                                                                if (
                                                                                    p.UseDualStack
                                                                                    is True
                                                                                ):
                                                                                    if (
                                                                                        get_attr(
                                                                                            _locals[
                                                                                                "PartitionResult"
                                                                                            ],
                                                                                            interpolate(
                                                                                                "supportsFIPS",
                                                                                                p,
                                                                                                _locals,
                                                                                            ),
                                                                                        )
                                                                                        is True
                                                                                    ):
                                                                                        if (
                                                                                            get_attr(
                                                                                                _locals[
                                                                                                    "PartitionResult"
                                                                                                ],
                                                                                                interpolate(
                                                                                                    "supportsDualStack",
                                                                                                    p,
                                                                                                    _locals,
                                                                                                ),
                                                                                            )
                                                                                            is True
                                                                                        ):
                                                                                            return Endpoint(
                                                                                                url=interpolate(
                                                                                                    "https://{StreamIdPrefixValue}.{StreamIdSuffixValue}.{OperationType}-kinesis{HttpsCustomEndpointSuffixValue}-fips.{Region}.{PartitionResult#dualStackDnsSuffix}",
                                                                                                    p,
                                                                                                    _locals,
                                                                                                ),
                                                                                                properties={},
                                                                                                headers={},
                                                                                            )
                                                                                        raise EndpointError(
                                                                                            interpolate(
                                                                                                "DualStack is enabled, but this partition does not support DualStack.",
                                                                                                p,
                                                                                                _locals,
                                                                                            )
                                                                                        )
                                                                                    raise EndpointError(
                                                                                        interpolate(
                                                                                            "FIPS is enabled, but this partition does not support FIPS.",
                                                                                            p,
                                                                                            _locals,
                                                                                        )
                                                                                    )
                                                                            if (
                                                                                p.UseFIPS
                                                                                is True
                                                                            ):
                                                                                if (
                                                                                    get_attr(
                                                                                        _locals[
                                                                                            "PartitionResult"
                                                                                        ],
                                                                                        interpolate(
                                                                                            "supportsFIPS",
                                                                                            p,
                                                                                            _locals,
                                                                                        ),
                                                                                    )
                                                                                    is True
                                                                                ):
                                                                                    return Endpoint(
                                                                                        url=interpolate(
                                                                                            "https://{StreamIdPrefixValue}.{StreamIdSuffixValue}.{OperationType}-kinesis{HttpsCustomEndpointSuffixValue}-fips.{Region}.{PartitionResult#dnsSuffix}",
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
                                                                            if (
                                                                                p.UseDualStack
                                                                                is True
                                                                            ):
                                                                                if (
                                                                                    get_attr(
                                                                                        _locals[
                                                                                            "PartitionResult"
                                                                                        ],
                                                                                        interpolate(
                                                                                            "supportsDualStack",
                                                                                            p,
                                                                                            _locals,
                                                                                        ),
                                                                                    )
                                                                                    is True
                                                                                ):
                                                                                    return Endpoint(
                                                                                        url=interpolate(
                                                                                            "https://{StreamIdPrefixValue}.{StreamIdSuffixValue}.{OperationType}-kinesis{HttpsCustomEndpointSuffixValue}.{Region}.{PartitionResult#dualStackDnsSuffix}",
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
                                                                                    "https://{StreamIdPrefixValue}.{StreamIdSuffixValue}.{OperationType}-kinesis{HttpsCustomEndpointSuffixValue}.{Region}.{PartitionResult#dnsSuffix}",
                                                                                    p,
                                                                                    _locals,
                                                                                ),
                                                                                properties={},
                                                                                headers={},
                                                                            )
                                                    if p.Endpoint is not None:
                                                        _locals[
                                                            "PlainCustomEndpointDelimiterValue"
                                                        ] = substring(
                                                            p.Endpoint, 7, 8, False
                                                        )
                                                        if (
                                                            _locals[
                                                                "PlainCustomEndpointDelimiterValue"
                                                            ]
                                                            is not None
                                                        ):
                                                            if string_equals(
                                                                _locals[
                                                                    "PlainCustomEndpointDelimiterValue"
                                                                ],
                                                                interpolate(
                                                                    "-", p, _locals
                                                                ),
                                                            ):
                                                                _locals[
                                                                    "PlainEndpointDelimiterValue"
                                                                ] = substring(
                                                                    p.Endpoint,
                                                                    12,
                                                                    13,
                                                                    False,
                                                                )
                                                                if (
                                                                    _locals[
                                                                        "PlainEndpointDelimiterValue"
                                                                    ]
                                                                    is not None
                                                                ):
                                                                    if string_equals(
                                                                        _locals[
                                                                            "PlainEndpointDelimiterValue"
                                                                        ],
                                                                        interpolate(
                                                                            ".",
                                                                            p,
                                                                            _locals,
                                                                        ),
                                                                    ):
                                                                        _locals[
                                                                            "PlainCustomEndpointSuffixValue"
                                                                        ] = substring(
                                                                            p.Endpoint,
                                                                            7,
                                                                            12,
                                                                            False,
                                                                        )
                                                                        if (
                                                                            _locals[
                                                                                "PlainCustomEndpointSuffixValue"
                                                                            ]
                                                                            is not None
                                                                        ):
                                                                            if (
                                                                                p.UseFIPS
                                                                                is True
                                                                            ):
                                                                                if (
                                                                                    p.UseDualStack
                                                                                    is True
                                                                                ):
                                                                                    if (
                                                                                        get_attr(
                                                                                            _locals[
                                                                                                "PartitionResult"
                                                                                            ],
                                                                                            interpolate(
                                                                                                "supportsFIPS",
                                                                                                p,
                                                                                                _locals,
                                                                                            ),
                                                                                        )
                                                                                        is True
                                                                                    ):
                                                                                        if (
                                                                                            get_attr(
                                                                                                _locals[
                                                                                                    "PartitionResult"
                                                                                                ],
                                                                                                interpolate(
                                                                                                    "supportsDualStack",
                                                                                                    p,
                                                                                                    _locals,
                                                                                                ),
                                                                                            )
                                                                                            is True
                                                                                        ):
                                                                                            return Endpoint(
                                                                                                url=interpolate(
                                                                                                    "https://{StreamIdPrefixValue}.{StreamIdSuffixValue}.{OperationType}-kinesis{PlainCustomEndpointSuffixValue}-fips.{Region}.{PartitionResult#dualStackDnsSuffix}",
                                                                                                    p,
                                                                                                    _locals,
                                                                                                ),
                                                                                                properties={},
                                                                                                headers={},
                                                                                            )
                                                                                        raise EndpointError(
                                                                                            interpolate(
                                                                                                "DualStack is enabled, but this partition does not support DualStack.",
                                                                                                p,
                                                                                                _locals,
                                                                                            )
                                                                                        )
                                                                                    raise EndpointError(
                                                                                        interpolate(
                                                                                            "FIPS is enabled, but this partition does not support FIPS.",
                                                                                            p,
                                                                                            _locals,
                                                                                        )
                                                                                    )
                                                                            if (
                                                                                p.UseFIPS
                                                                                is True
                                                                            ):
                                                                                if (
                                                                                    get_attr(
                                                                                        _locals[
                                                                                            "PartitionResult"
                                                                                        ],
                                                                                        interpolate(
                                                                                            "supportsFIPS",
                                                                                            p,
                                                                                            _locals,
                                                                                        ),
                                                                                    )
                                                                                    is True
                                                                                ):
                                                                                    return Endpoint(
                                                                                        url=interpolate(
                                                                                            "https://{StreamIdPrefixValue}.{StreamIdSuffixValue}.{OperationType}-kinesis{PlainCustomEndpointSuffixValue}-fips.{Region}.{PartitionResult#dnsSuffix}",
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
                                                                            if (
                                                                                p.UseDualStack
                                                                                is True
                                                                            ):
                                                                                if (
                                                                                    get_attr(
                                                                                        _locals[
                                                                                            "PartitionResult"
                                                                                        ],
                                                                                        interpolate(
                                                                                            "supportsDualStack",
                                                                                            p,
                                                                                            _locals,
                                                                                        ),
                                                                                    )
                                                                                    is True
                                                                                ):
                                                                                    return Endpoint(
                                                                                        url=interpolate(
                                                                                            "https://{StreamIdPrefixValue}.{StreamIdSuffixValue}.{OperationType}-kinesis{PlainCustomEndpointSuffixValue}.{Region}.{PartitionResult#dualStackDnsSuffix}",
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
                                                                                    "https://{StreamIdPrefixValue}.{StreamIdSuffixValue}.{OperationType}-kinesis{PlainCustomEndpointSuffixValue}.{Region}.{PartitionResult#dnsSuffix}",
                                                                                    p,
                                                                                    _locals,
                                                                                ),
                                                                                properties={},
                                                                                headers={},
                                                                            )
                                                    if p.UseFIPS is True:
                                                        if p.UseDualStack is True:
                                                            if (
                                                                get_attr(
                                                                    _locals[
                                                                        "PartitionResult"
                                                                    ],
                                                                    interpolate(
                                                                        "supportsFIPS",
                                                                        p,
                                                                        _locals,
                                                                    ),
                                                                )
                                                                is True
                                                            ):
                                                                if (
                                                                    get_attr(
                                                                        _locals[
                                                                            "PartitionResult"
                                                                        ],
                                                                        interpolate(
                                                                            "supportsDualStack",
                                                                            p,
                                                                            _locals,
                                                                        ),
                                                                    )
                                                                    is True
                                                                ):
                                                                    return Endpoint(
                                                                        url=interpolate(
                                                                            "https://{StreamIdPrefixValue}.{StreamIdSuffixValue}.{OperationType}-kinesis-fips.{Region}.{PartitionResult#dualStackDnsSuffix}",
                                                                            p,
                                                                            _locals,
                                                                        ),
                                                                        properties={},
                                                                        headers={},
                                                                    )
                                                                raise EndpointError(
                                                                    interpolate(
                                                                        "DualStack is enabled, but this partition does not support DualStack.",
                                                                        p,
                                                                        _locals,
                                                                    )
                                                                )
                                                            raise EndpointError(
                                                                interpolate(
                                                                    "FIPS is enabled, but this partition does not support FIPS.",
                                                                    p,
                                                                    _locals,
                                                                )
                                                            )
                                                    if p.UseFIPS is True:
                                                        if (
                                                            get_attr(
                                                                _locals[
                                                                    "PartitionResult"
                                                                ],
                                                                interpolate(
                                                                    "supportsFIPS",
                                                                    p,
                                                                    _locals,
                                                                ),
                                                            )
                                                            is True
                                                        ):
                                                            return Endpoint(
                                                                url=interpolate(
                                                                    "https://{StreamIdPrefixValue}.{StreamIdSuffixValue}.{OperationType}-kinesis-fips.{Region}.{PartitionResult#dnsSuffix}",
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
                                                                _locals[
                                                                    "PartitionResult"
                                                                ],
                                                                interpolate(
                                                                    "supportsDualStack",
                                                                    p,
                                                                    _locals,
                                                                ),
                                                            )
                                                            is True
                                                        ):
                                                            return Endpoint(
                                                                url=interpolate(
                                                                    "https://{StreamIdPrefixValue}.{StreamIdSuffixValue}.{OperationType}-kinesis.{Region}.{PartitionResult#dualStackDnsSuffix}",
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
                                                            "https://{StreamIdPrefixValue}.{StreamIdSuffixValue}.{OperationType}-kinesis.{Region}.{PartitionResult#dnsSuffix}",
                                                            p,
                                                            _locals,
                                                        ),
                                                        properties={},
                                                        headers={},
                                                    )
                                                raise EndpointError(
                                                    interpolate(
                                                        "Operation Type is not set. Please contact service team for resolution.",
                                                        p,
                                                        _locals,
                                                    )
                                                )
    _locals: dict[str, Any] = {}
    if p.StreamARN is not None:
        if not (p.Endpoint is not None):
            if p.Region is not None:
                _locals["PartitionResult"] = aws_partition(p.Region)
                if _locals["PartitionResult"] is not None:
                    if not (
                        string_equals(
                            get_attr(
                                _locals["PartitionResult"],
                                interpolate("name", p, _locals),
                            ),
                            interpolate("aws-iso", p, _locals),
                        )
                    ):
                        if not (
                            string_equals(
                                get_attr(
                                    _locals["PartitionResult"],
                                    interpolate("name", p, _locals),
                                ),
                                interpolate("aws-iso-b", p, _locals),
                            )
                        ):
                            _locals["arn"] = aws_parse_arn(p.StreamARN)
                            if _locals["arn"] is not None:
                                if is_valid_host_label(
                                    get_attr(
                                        _locals["arn"],
                                        interpolate("accountId", p, _locals),
                                    ),
                                    False,
                                ):
                                    if is_valid_host_label(
                                        get_attr(
                                            _locals["arn"],
                                            interpolate("region", p, _locals),
                                        ),
                                        False,
                                    ):
                                        if string_equals(
                                            get_attr(
                                                _locals["arn"],
                                                interpolate("service", p, _locals),
                                            ),
                                            interpolate("kinesis", p, _locals),
                                        ):
                                            _locals["arnType"] = get_attr(
                                                _locals["arn"],
                                                interpolate(
                                                    "resourceId[0]", p, _locals
                                                ),
                                            )
                                            if _locals["arnType"] is not None:
                                                if not (
                                                    string_equals(
                                                        _locals["arnType"],
                                                        interpolate("", p, _locals),
                                                    )
                                                ):
                                                    if string_equals(
                                                        _locals["arnType"],
                                                        interpolate(
                                                            "stream", p, _locals
                                                        ),
                                                    ):
                                                        if string_equals(
                                                            get_attr(
                                                                _locals[
                                                                    "PartitionResult"
                                                                ],
                                                                interpolate(
                                                                    "name", p, _locals
                                                                ),
                                                            ),
                                                            interpolate(
                                                                "{arn#partition}",
                                                                p,
                                                                _locals,
                                                            ),
                                                        ):
                                                            if (
                                                                p.OperationType
                                                                is not None
                                                            ):
                                                                if p.UseFIPS is True:
                                                                    if (
                                                                        p.UseDualStack
                                                                        is True
                                                                    ):
                                                                        if (
                                                                            get_attr(
                                                                                _locals[
                                                                                    "PartitionResult"
                                                                                ],
                                                                                interpolate(
                                                                                    "supportsFIPS",
                                                                                    p,
                                                                                    _locals,
                                                                                ),
                                                                            )
                                                                            is True
                                                                        ):
                                                                            if (
                                                                                get_attr(
                                                                                    _locals[
                                                                                        "PartitionResult"
                                                                                    ],
                                                                                    interpolate(
                                                                                        "supportsDualStack",
                                                                                        p,
                                                                                        _locals,
                                                                                    ),
                                                                                )
                                                                                is True
                                                                            ):
                                                                                return Endpoint(
                                                                                    url=interpolate(
                                                                                        "https://{arn#accountId}.{OperationType}-kinesis-fips.{Region}.{PartitionResult#dualStackDnsSuffix}",
                                                                                        p,
                                                                                        _locals,
                                                                                    ),
                                                                                    properties={},
                                                                                    headers={},
                                                                                )
                                                                            raise EndpointError(
                                                                                interpolate(
                                                                                    "DualStack is enabled, but this partition does not support DualStack.",
                                                                                    p,
                                                                                    _locals,
                                                                                )
                                                                            )
                                                                        raise EndpointError(
                                                                            interpolate(
                                                                                "FIPS is enabled, but this partition does not support FIPS.",
                                                                                p,
                                                                                _locals,
                                                                            )
                                                                        )
                                                                if p.UseFIPS is True:
                                                                    if (
                                                                        get_attr(
                                                                            _locals[
                                                                                "PartitionResult"
                                                                            ],
                                                                            interpolate(
                                                                                "supportsFIPS",
                                                                                p,
                                                                                _locals,
                                                                            ),
                                                                        )
                                                                        is True
                                                                    ):
                                                                        return Endpoint(
                                                                            url=interpolate(
                                                                                "https://{arn#accountId}.{OperationType}-kinesis-fips.{Region}.{PartitionResult#dnsSuffix}",
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
                                                                if (
                                                                    p.UseDualStack
                                                                    is True
                                                                ):
                                                                    if (
                                                                        get_attr(
                                                                            _locals[
                                                                                "PartitionResult"
                                                                            ],
                                                                            interpolate(
                                                                                "supportsDualStack",
                                                                                p,
                                                                                _locals,
                                                                            ),
                                                                        )
                                                                        is True
                                                                    ):
                                                                        return Endpoint(
                                                                            url=interpolate(
                                                                                "https://{arn#accountId}.{OperationType}-kinesis.{Region}.{PartitionResult#dualStackDnsSuffix}",
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
                                                                        "https://{arn#accountId}.{OperationType}-kinesis.{Region}.{PartitionResult#dnsSuffix}",
                                                                        p,
                                                                        _locals,
                                                                    ),
                                                                    properties={},
                                                                    headers={},
                                                                )
                                                            raise EndpointError(
                                                                interpolate(
                                                                    "Operation Type is not set. Please contact service team for resolution.",
                                                                    p,
                                                                    _locals,
                                                                )
                                                            )
                                                        raise EndpointError(
                                                            interpolate(
                                                                "Partition: {arn#partition} from ARN doesn't match with partition name: {PartitionResult#name}.",
                                                                p,
                                                                _locals,
                                                            )
                                                        )
                                                    raise EndpointError(
                                                        interpolate(
                                                            "Invalid ARN: Kinesis ARNs don't support `{arnType}` arn types.",
                                                            p,
                                                            _locals,
                                                        )
                                                    )
                                            raise EndpointError(
                                                interpolate(
                                                    "Invalid ARN: No ARN type specified",
                                                    p,
                                                    _locals,
                                                )
                                            )
                                        raise EndpointError(
                                            interpolate(
                                                "Invalid ARN: The ARN was not for the Kinesis service, found: {arn#service}.",
                                                p,
                                                _locals,
                                            )
                                        )
                                    raise EndpointError(
                                        interpolate(
                                            "Invalid ARN: Invalid region.", p, _locals
                                        )
                                    )
                                raise EndpointError(
                                    interpolate(
                                        "Invalid ARN: Invalid account id.", p, _locals
                                    )
                                )
                            raise EndpointError(
                                interpolate(
                                    "Invalid ARN: Failed to parse ARN.", p, _locals
                                )
                            )
    _locals: dict[str, Any] = {}
    if p.ConsumerARN is not None:
        if not (p.Endpoint is not None):
            if p.Region is not None:
                _locals["PartitionResult"] = aws_partition(p.Region)
                if _locals["PartitionResult"] is not None:
                    if not (
                        string_equals(
                            get_attr(
                                _locals["PartitionResult"],
                                interpolate("name", p, _locals),
                            ),
                            interpolate("aws-iso", p, _locals),
                        )
                    ):
                        if not (
                            string_equals(
                                get_attr(
                                    _locals["PartitionResult"],
                                    interpolate("name", p, _locals),
                                ),
                                interpolate("aws-iso-b", p, _locals),
                            )
                        ):
                            _locals["arn"] = aws_parse_arn(p.ConsumerARN)
                            if _locals["arn"] is not None:
                                if is_valid_host_label(
                                    get_attr(
                                        _locals["arn"],
                                        interpolate("accountId", p, _locals),
                                    ),
                                    False,
                                ):
                                    if is_valid_host_label(
                                        get_attr(
                                            _locals["arn"],
                                            interpolate("region", p, _locals),
                                        ),
                                        False,
                                    ):
                                        if string_equals(
                                            get_attr(
                                                _locals["arn"],
                                                interpolate("service", p, _locals),
                                            ),
                                            interpolate("kinesis", p, _locals),
                                        ):
                                            _locals["arnType"] = get_attr(
                                                _locals["arn"],
                                                interpolate(
                                                    "resourceId[0]", p, _locals
                                                ),
                                            )
                                            if _locals["arnType"] is not None:
                                                if not (
                                                    string_equals(
                                                        _locals["arnType"],
                                                        interpolate("", p, _locals),
                                                    )
                                                ):
                                                    if string_equals(
                                                        _locals["arnType"],
                                                        interpolate(
                                                            "stream", p, _locals
                                                        ),
                                                    ):
                                                        if string_equals(
                                                            get_attr(
                                                                _locals[
                                                                    "PartitionResult"
                                                                ],
                                                                interpolate(
                                                                    "name", p, _locals
                                                                ),
                                                            ),
                                                            interpolate(
                                                                "{arn#partition}",
                                                                p,
                                                                _locals,
                                                            ),
                                                        ):
                                                            if (
                                                                p.OperationType
                                                                is not None
                                                            ):
                                                                if p.UseFIPS is True:
                                                                    if (
                                                                        p.UseDualStack
                                                                        is True
                                                                    ):
                                                                        if (
                                                                            get_attr(
                                                                                _locals[
                                                                                    "PartitionResult"
                                                                                ],
                                                                                interpolate(
                                                                                    "supportsFIPS",
                                                                                    p,
                                                                                    _locals,
                                                                                ),
                                                                            )
                                                                            is True
                                                                        ):
                                                                            if (
                                                                                get_attr(
                                                                                    _locals[
                                                                                        "PartitionResult"
                                                                                    ],
                                                                                    interpolate(
                                                                                        "supportsDualStack",
                                                                                        p,
                                                                                        _locals,
                                                                                    ),
                                                                                )
                                                                                is True
                                                                            ):
                                                                                return Endpoint(
                                                                                    url=interpolate(
                                                                                        "https://{arn#accountId}.{OperationType}-kinesis-fips.{Region}.{PartitionResult#dualStackDnsSuffix}",
                                                                                        p,
                                                                                        _locals,
                                                                                    ),
                                                                                    properties={},
                                                                                    headers={},
                                                                                )
                                                                            raise EndpointError(
                                                                                interpolate(
                                                                                    "DualStack is enabled, but this partition does not support DualStack.",
                                                                                    p,
                                                                                    _locals,
                                                                                )
                                                                            )
                                                                        raise EndpointError(
                                                                            interpolate(
                                                                                "FIPS is enabled, but this partition does not support FIPS.",
                                                                                p,
                                                                                _locals,
                                                                            )
                                                                        )
                                                                if p.UseFIPS is True:
                                                                    if (
                                                                        get_attr(
                                                                            _locals[
                                                                                "PartitionResult"
                                                                            ],
                                                                            interpolate(
                                                                                "supportsFIPS",
                                                                                p,
                                                                                _locals,
                                                                            ),
                                                                        )
                                                                        is True
                                                                    ):
                                                                        return Endpoint(
                                                                            url=interpolate(
                                                                                "https://{arn#accountId}.{OperationType}-kinesis-fips.{Region}.{PartitionResult#dnsSuffix}",
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
                                                                if (
                                                                    p.UseDualStack
                                                                    is True
                                                                ):
                                                                    if (
                                                                        get_attr(
                                                                            _locals[
                                                                                "PartitionResult"
                                                                            ],
                                                                            interpolate(
                                                                                "supportsDualStack",
                                                                                p,
                                                                                _locals,
                                                                            ),
                                                                        )
                                                                        is True
                                                                    ):
                                                                        return Endpoint(
                                                                            url=interpolate(
                                                                                "https://{arn#accountId}.{OperationType}-kinesis.{Region}.{PartitionResult#dualStackDnsSuffix}",
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
                                                                        "https://{arn#accountId}.{OperationType}-kinesis.{Region}.{PartitionResult#dnsSuffix}",
                                                                        p,
                                                                        _locals,
                                                                    ),
                                                                    properties={},
                                                                    headers={},
                                                                )
                                                            raise EndpointError(
                                                                interpolate(
                                                                    "Operation Type is not set. Please contact service team for resolution.",
                                                                    p,
                                                                    _locals,
                                                                )
                                                            )
                                                        raise EndpointError(
                                                            interpolate(
                                                                "Partition: {arn#partition} from ARN doesn't match with partition name: {PartitionResult#name}.",
                                                                p,
                                                                _locals,
                                                            )
                                                        )
                                                    raise EndpointError(
                                                        interpolate(
                                                            "Invalid ARN: Kinesis ARNs don't support `{arnType}` arn types.",
                                                            p,
                                                            _locals,
                                                        )
                                                    )
                                            raise EndpointError(
                                                interpolate(
                                                    "Invalid ARN: No ARN type specified",
                                                    p,
                                                    _locals,
                                                )
                                            )
                                        raise EndpointError(
                                            interpolate(
                                                "Invalid ARN: The ARN was not for the Kinesis service, found: {arn#service}.",
                                                p,
                                                _locals,
                                            )
                                        )
                                    raise EndpointError(
                                        interpolate(
                                            "Invalid ARN: Invalid region.", p, _locals
                                        )
                                    )
                                raise EndpointError(
                                    interpolate(
                                        "Invalid ARN: Invalid account id.", p, _locals
                                    )
                                )
                            raise EndpointError(
                                interpolate(
                                    "Invalid ARN: Failed to parse ARN.", p, _locals
                                )
                            )
    _locals: dict[str, Any] = {}
    if p.ResourceARN is not None:
        if not (p.Endpoint is not None):
            if p.Region is not None:
                _locals["PartitionResult"] = aws_partition(p.Region)
                if _locals["PartitionResult"] is not None:
                    if not (
                        string_equals(
                            get_attr(
                                _locals["PartitionResult"],
                                interpolate("name", p, _locals),
                            ),
                            interpolate("aws-iso", p, _locals),
                        )
                    ):
                        if not (
                            string_equals(
                                get_attr(
                                    _locals["PartitionResult"],
                                    interpolate("name", p, _locals),
                                ),
                                interpolate("aws-iso-b", p, _locals),
                            )
                        ):
                            _locals["arn"] = aws_parse_arn(p.ResourceARN)
                            if _locals["arn"] is not None:
                                if is_valid_host_label(
                                    get_attr(
                                        _locals["arn"],
                                        interpolate("accountId", p, _locals),
                                    ),
                                    False,
                                ):
                                    if is_valid_host_label(
                                        get_attr(
                                            _locals["arn"],
                                            interpolate("region", p, _locals),
                                        ),
                                        False,
                                    ):
                                        if string_equals(
                                            get_attr(
                                                _locals["arn"],
                                                interpolate("service", p, _locals),
                                            ),
                                            interpolate("kinesis", p, _locals),
                                        ):
                                            _locals["arnType"] = get_attr(
                                                _locals["arn"],
                                                interpolate(
                                                    "resourceId[0]", p, _locals
                                                ),
                                            )
                                            if _locals["arnType"] is not None:
                                                if not (
                                                    string_equals(
                                                        _locals["arnType"],
                                                        interpolate("", p, _locals),
                                                    )
                                                ):
                                                    if not (
                                                        string_equals(
                                                            _locals["arnType"],
                                                            interpolate(
                                                                "stream", p, _locals
                                                            ),
                                                        )
                                                    ):
                                                        if not (
                                                            string_equals(
                                                                _locals["arnType"],
                                                                interpolate(
                                                                    "channel",
                                                                    p,
                                                                    _locals,
                                                                ),
                                                            )
                                                        ):
                                                            if not (
                                                                string_equals(
                                                                    _locals["arnType"],
                                                                    interpolate(
                                                                        "queue",
                                                                        p,
                                                                        _locals,
                                                                    ),
                                                                )
                                                            ):
                                                                raise EndpointError(
                                                                    interpolate(
                                                                        "Invalid ARN: Unsupported resource type `{arnType}`. Expected: stream, channel, or queue.",
                                                                        p,
                                                                        _locals,
                                                                    )
                                                                )
                                                    if string_equals(
                                                        get_attr(
                                                            _locals["PartitionResult"],
                                                            interpolate(
                                                                "name", p, _locals
                                                            ),
                                                        ),
                                                        interpolate(
                                                            "{arn#partition}",
                                                            p,
                                                            _locals,
                                                        ),
                                                    ):
                                                        if p.OperationType is not None:
                                                            if string_equals(
                                                                _locals["arnType"],
                                                                interpolate(
                                                                    "stream", p, _locals
                                                                ),
                                                            ):
                                                                if p.UseFIPS is True:
                                                                    if (
                                                                        p.UseDualStack
                                                                        is True
                                                                    ):
                                                                        if (
                                                                            get_attr(
                                                                                _locals[
                                                                                    "PartitionResult"
                                                                                ],
                                                                                interpolate(
                                                                                    "supportsFIPS",
                                                                                    p,
                                                                                    _locals,
                                                                                ),
                                                                            )
                                                                            is True
                                                                        ):
                                                                            if (
                                                                                get_attr(
                                                                                    _locals[
                                                                                        "PartitionResult"
                                                                                    ],
                                                                                    interpolate(
                                                                                        "supportsDualStack",
                                                                                        p,
                                                                                        _locals,
                                                                                    ),
                                                                                )
                                                                                is True
                                                                            ):
                                                                                return Endpoint(
                                                                                    url=interpolate(
                                                                                        "https://{arn#accountId}.{OperationType}-kinesis-fips.{Region}.{PartitionResult#dualStackDnsSuffix}",
                                                                                        p,
                                                                                        _locals,
                                                                                    ),
                                                                                    properties={},
                                                                                    headers={},
                                                                                )
                                                                            raise EndpointError(
                                                                                interpolate(
                                                                                    "DualStack is enabled, but this partition does not support DualStack.",
                                                                                    p,
                                                                                    _locals,
                                                                                )
                                                                            )
                                                                        raise EndpointError(
                                                                            interpolate(
                                                                                "FIPS is enabled, but this partition does not support FIPS.",
                                                                                p,
                                                                                _locals,
                                                                            )
                                                                        )
                                                                if p.UseFIPS is True:
                                                                    if (
                                                                        get_attr(
                                                                            _locals[
                                                                                "PartitionResult"
                                                                            ],
                                                                            interpolate(
                                                                                "supportsFIPS",
                                                                                p,
                                                                                _locals,
                                                                            ),
                                                                        )
                                                                        is True
                                                                    ):
                                                                        return Endpoint(
                                                                            url=interpolate(
                                                                                "https://{arn#accountId}.{OperationType}-kinesis-fips.{Region}.{PartitionResult#dnsSuffix}",
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
                                                                if (
                                                                    p.UseDualStack
                                                                    is True
                                                                ):
                                                                    if (
                                                                        get_attr(
                                                                            _locals[
                                                                                "PartitionResult"
                                                                            ],
                                                                            interpolate(
                                                                                "supportsDualStack",
                                                                                p,
                                                                                _locals,
                                                                            ),
                                                                        )
                                                                        is True
                                                                    ):
                                                                        return Endpoint(
                                                                            url=interpolate(
                                                                                "https://{arn#accountId}.{OperationType}-kinesis.{Region}.{PartitionResult#dualStackDnsSuffix}",
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
                                                                        "https://{arn#accountId}.{OperationType}-kinesis.{Region}.{PartitionResult#dnsSuffix}",
                                                                        p,
                                                                        _locals,
                                                                    ),
                                                                    properties={},
                                                                    headers={},
                                                                )
                                                            if string_equals(
                                                                _locals["arnType"],
                                                                interpolate(
                                                                    "channel",
                                                                    p,
                                                                    _locals,
                                                                ),
                                                            ):
                                                                _locals[
                                                                    "resourceId"
                                                                ] = get_attr(
                                                                    _locals["arn"],
                                                                    interpolate(
                                                                        "resourceId[1]",
                                                                        p,
                                                                        _locals,
                                                                    ),
                                                                )
                                                                if (
                                                                    _locals[
                                                                        "resourceId"
                                                                    ]
                                                                    is not None
                                                                ):
                                                                    if is_valid_host_label(
                                                                        _locals[
                                                                            "resourceId"
                                                                        ],
                                                                        False,
                                                                    ):
                                                                        if (
                                                                            p.UseFIPS
                                                                            is True
                                                                        ):
                                                                            if (
                                                                                p.UseDualStack
                                                                                is True
                                                                            ):
                                                                                if (
                                                                                    get_attr(
                                                                                        _locals[
                                                                                            "PartitionResult"
                                                                                        ],
                                                                                        interpolate(
                                                                                            "supportsFIPS",
                                                                                            p,
                                                                                            _locals,
                                                                                        ),
                                                                                    )
                                                                                    is True
                                                                                ):
                                                                                    if (
                                                                                        get_attr(
                                                                                            _locals[
                                                                                                "PartitionResult"
                                                                                            ],
                                                                                            interpolate(
                                                                                                "supportsDualStack",
                                                                                                p,
                                                                                                _locals,
                                                                                            ),
                                                                                        )
                                                                                        is True
                                                                                    ):
                                                                                        return Endpoint(
                                                                                            url=interpolate(
                                                                                                "https://{resourceId}.{OperationType}-kinesis-fips.{Region}.{PartitionResult#dualStackDnsSuffix}",
                                                                                                p,
                                                                                                _locals,
                                                                                            ),
                                                                                            properties={},
                                                                                            headers={},
                                                                                        )
                                                                                    raise EndpointError(
                                                                                        interpolate(
                                                                                            "DualStack is enabled, but this partition does not support DualStack.",
                                                                                            p,
                                                                                            _locals,
                                                                                        )
                                                                                    )
                                                                                raise EndpointError(
                                                                                    interpolate(
                                                                                        "FIPS is enabled, but this partition does not support FIPS.",
                                                                                        p,
                                                                                        _locals,
                                                                                    )
                                                                                )
                                                                        if (
                                                                            p.UseFIPS
                                                                            is True
                                                                        ):
                                                                            if (
                                                                                get_attr(
                                                                                    _locals[
                                                                                        "PartitionResult"
                                                                                    ],
                                                                                    interpolate(
                                                                                        "supportsFIPS",
                                                                                        p,
                                                                                        _locals,
                                                                                    ),
                                                                                )
                                                                                is True
                                                                            ):
                                                                                return Endpoint(
                                                                                    url=interpolate(
                                                                                        "https://{resourceId}.{OperationType}-kinesis-fips.{Region}.{PartitionResult#dnsSuffix}",
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
                                                                        if (
                                                                            p.UseDualStack
                                                                            is True
                                                                        ):
                                                                            if (
                                                                                get_attr(
                                                                                    _locals[
                                                                                        "PartitionResult"
                                                                                    ],
                                                                                    interpolate(
                                                                                        "supportsDualStack",
                                                                                        p,
                                                                                        _locals,
                                                                                    ),
                                                                                )
                                                                                is True
                                                                            ):
                                                                                return Endpoint(
                                                                                    url=interpolate(
                                                                                        "https://{resourceId}.{OperationType}-kinesis.{Region}.{PartitionResult#dualStackDnsSuffix}",
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
                                                                                "https://{resourceId}.{OperationType}-kinesis.{Region}.{PartitionResult#dnsSuffix}",
                                                                                p,
                                                                                _locals,
                                                                            ),
                                                                            properties={},
                                                                            headers={},
                                                                        )
                                                                    raise EndpointError(
                                                                        interpolate(
                                                                            "Invalid ARN: Invalid channel id.",
                                                                            p,
                                                                            _locals,
                                                                        )
                                                                    )
                                                                raise EndpointError(
                                                                    interpolate(
                                                                        "Invalid ARN: Missing channel id.",
                                                                        p,
                                                                        _locals,
                                                                    )
                                                                )
                                                            if string_equals(
                                                                _locals["arnType"],
                                                                interpolate(
                                                                    "queue", p, _locals
                                                                ),
                                                            ):
                                                                _locals[
                                                                    "resourceId"
                                                                ] = get_attr(
                                                                    _locals["arn"],
                                                                    interpolate(
                                                                        "resourceId[1]",
                                                                        p,
                                                                        _locals,
                                                                    ),
                                                                )
                                                                if (
                                                                    _locals[
                                                                        "resourceId"
                                                                    ]
                                                                    is not None
                                                                ):
                                                                    if is_valid_host_label(
                                                                        _locals[
                                                                            "resourceId"
                                                                        ],
                                                                        False,
                                                                    ):
                                                                        if (
                                                                            p.UseFIPS
                                                                            is True
                                                                        ):
                                                                            if (
                                                                                p.UseDualStack
                                                                                is True
                                                                            ):
                                                                                if (
                                                                                    get_attr(
                                                                                        _locals[
                                                                                            "PartitionResult"
                                                                                        ],
                                                                                        interpolate(
                                                                                            "supportsFIPS",
                                                                                            p,
                                                                                            _locals,
                                                                                        ),
                                                                                    )
                                                                                    is True
                                                                                ):
                                                                                    if (
                                                                                        get_attr(
                                                                                            _locals[
                                                                                                "PartitionResult"
                                                                                            ],
                                                                                            interpolate(
                                                                                                "supportsDualStack",
                                                                                                p,
                                                                                                _locals,
                                                                                            ),
                                                                                        )
                                                                                        is True
                                                                                    ):
                                                                                        return Endpoint(
                                                                                            url=interpolate(
                                                                                                "https://{resourceId}.{OperationType}-kinesis-queues-fips.{Region}.{PartitionResult#dualStackDnsSuffix}",
                                                                                                p,
                                                                                                _locals,
                                                                                            ),
                                                                                            properties={},
                                                                                            headers={},
                                                                                        )
                                                                                    raise EndpointError(
                                                                                        interpolate(
                                                                                            "DualStack is enabled, but this partition does not support DualStack.",
                                                                                            p,
                                                                                            _locals,
                                                                                        )
                                                                                    )
                                                                                raise EndpointError(
                                                                                    interpolate(
                                                                                        "FIPS is enabled, but this partition does not support FIPS.",
                                                                                        p,
                                                                                        _locals,
                                                                                    )
                                                                                )
                                                                        if (
                                                                            p.UseFIPS
                                                                            is True
                                                                        ):
                                                                            if (
                                                                                get_attr(
                                                                                    _locals[
                                                                                        "PartitionResult"
                                                                                    ],
                                                                                    interpolate(
                                                                                        "supportsFIPS",
                                                                                        p,
                                                                                        _locals,
                                                                                    ),
                                                                                )
                                                                                is True
                                                                            ):
                                                                                return Endpoint(
                                                                                    url=interpolate(
                                                                                        "https://{resourceId}.{OperationType}-kinesis-queues-fips.{Region}.{PartitionResult#dnsSuffix}",
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
                                                                        if (
                                                                            p.UseDualStack
                                                                            is True
                                                                        ):
                                                                            if (
                                                                                get_attr(
                                                                                    _locals[
                                                                                        "PartitionResult"
                                                                                    ],
                                                                                    interpolate(
                                                                                        "supportsDualStack",
                                                                                        p,
                                                                                        _locals,
                                                                                    ),
                                                                                )
                                                                                is True
                                                                            ):
                                                                                return Endpoint(
                                                                                    url=interpolate(
                                                                                        "https://{resourceId}.{OperationType}-kinesis-queues.{Region}.{PartitionResult#dualStackDnsSuffix}",
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
                                                                                "https://{resourceId}.{OperationType}-kinesis-queues.{Region}.{PartitionResult#dnsSuffix}",
                                                                                p,
                                                                                _locals,
                                                                            ),
                                                                            properties={},
                                                                            headers={},
                                                                        )
                                                                    raise EndpointError(
                                                                        interpolate(
                                                                            "Invalid ARN: Invalid queue id.",
                                                                            p,
                                                                            _locals,
                                                                        )
                                                                    )
                                                                raise EndpointError(
                                                                    interpolate(
                                                                        "Invalid ARN: Missing queue id.",
                                                                        p,
                                                                        _locals,
                                                                    )
                                                                )
                                                        raise EndpointError(
                                                            interpolate(
                                                                "Operation Type is not set. Please contact service team for resolution.",
                                                                p,
                                                                _locals,
                                                            )
                                                        )
                                                    raise EndpointError(
                                                        interpolate(
                                                            "Partition: {arn#partition} from ARN doesn't match with partition name: {PartitionResult#name}.",
                                                            p,
                                                            _locals,
                                                        )
                                                    )
                                            raise EndpointError(
                                                interpolate(
                                                    "Invalid ARN: No ARN type specified",
                                                    p,
                                                    _locals,
                                                )
                                            )
                                        raise EndpointError(
                                            interpolate(
                                                "Invalid ARN: The ARN was not for the Kinesis service, found: {arn#service}.",
                                                p,
                                                _locals,
                                            )
                                        )
                                    raise EndpointError(
                                        interpolate(
                                            "Invalid ARN: Invalid region.", p, _locals
                                        )
                                    )
                                raise EndpointError(
                                    interpolate(
                                        "Invalid ARN: Invalid account id.", p, _locals
                                    )
                                )
                            raise EndpointError(
                                interpolate(
                                    "Invalid ARN: Failed to parse ARN.", p, _locals
                                )
                            )
    _locals: dict[str, Any] = {}
    if p.ResourceARN is not None:
        if not (p.Endpoint is not None):
            if p.Region is not None:
                _locals["PartitionResult"] = aws_partition(p.Region)
                if _locals["PartitionResult"] is not None:
                    _locals["isoArn"] = aws_parse_arn(p.ResourceARN)
                    if _locals["isoArn"] is not None:
                        _locals["isoArnType"] = get_attr(
                            _locals["isoArn"], interpolate("resourceId[0]", p, _locals)
                        )
                        if _locals["isoArnType"] is not None:
                            if string_equals(
                                _locals["isoArnType"], interpolate("queue", p, _locals)
                            ):
                                if is_valid_host_label(
                                    get_attr(
                                        _locals["isoArn"],
                                        interpolate("accountId", p, _locals),
                                    ),
                                    False,
                                ):
                                    if is_valid_host_label(
                                        get_attr(
                                            _locals["isoArn"],
                                            interpolate("region", p, _locals),
                                        ),
                                        False,
                                    ):
                                        if string_equals(
                                            get_attr(
                                                _locals["isoArn"],
                                                interpolate("service", p, _locals),
                                            ),
                                            interpolate("kinesis", p, _locals),
                                        ):
                                            if string_equals(
                                                get_attr(
                                                    _locals["PartitionResult"],
                                                    interpolate("name", p, _locals),
                                                ),
                                                interpolate(
                                                    "{isoArn#partition}", p, _locals
                                                ),
                                            ):
                                                if p.OperationType is not None:
                                                    _locals["isoResourceId"] = get_attr(
                                                        _locals["isoArn"],
                                                        interpolate(
                                                            "resourceId[1]", p, _locals
                                                        ),
                                                    )
                                                    if (
                                                        _locals["isoResourceId"]
                                                        is not None
                                                    ):
                                                        if is_valid_host_label(
                                                            _locals["isoResourceId"],
                                                            False,
                                                        ):
                                                            if string_equals(
                                                                get_attr(
                                                                    _locals[
                                                                        "PartitionResult"
                                                                    ],
                                                                    interpolate(
                                                                        "name",
                                                                        p,
                                                                        _locals,
                                                                    ),
                                                                ),
                                                                interpolate(
                                                                    "aws-iso",
                                                                    p,
                                                                    _locals,
                                                                ),
                                                            ):
                                                                if p.UseFIPS is True:
                                                                    if (
                                                                        p.UseDualStack
                                                                        is True
                                                                    ):
                                                                        if (
                                                                            get_attr(
                                                                                _locals[
                                                                                    "PartitionResult"
                                                                                ],
                                                                                interpolate(
                                                                                    "supportsFIPS",
                                                                                    p,
                                                                                    _locals,
                                                                                ),
                                                                            )
                                                                            is True
                                                                        ):
                                                                            if (
                                                                                get_attr(
                                                                                    _locals[
                                                                                        "PartitionResult"
                                                                                    ],
                                                                                    interpolate(
                                                                                        "supportsDualStack",
                                                                                        p,
                                                                                        _locals,
                                                                                    ),
                                                                                )
                                                                                is True
                                                                            ):
                                                                                return Endpoint(
                                                                                    url=interpolate(
                                                                                        "https://kinesis-queues-fips.{Region}.{PartitionResult#dualStackDnsSuffix}",
                                                                                        p,
                                                                                        _locals,
                                                                                    ),
                                                                                    properties={},
                                                                                    headers={},
                                                                                )
                                                                            raise EndpointError(
                                                                                interpolate(
                                                                                    "DualStack is enabled, but this partition does not support DualStack.",
                                                                                    p,
                                                                                    _locals,
                                                                                )
                                                                            )
                                                                        raise EndpointError(
                                                                            interpolate(
                                                                                "FIPS is enabled, but this partition does not support FIPS.",
                                                                                p,
                                                                                _locals,
                                                                            )
                                                                        )
                                                                if p.UseFIPS is True:
                                                                    if (
                                                                        get_attr(
                                                                            _locals[
                                                                                "PartitionResult"
                                                                            ],
                                                                            interpolate(
                                                                                "supportsFIPS",
                                                                                p,
                                                                                _locals,
                                                                            ),
                                                                        )
                                                                        is True
                                                                    ):
                                                                        return Endpoint(
                                                                            url=interpolate(
                                                                                "https://kinesis-queues-fips.{Region}.{PartitionResult#dnsSuffix}",
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
                                                                if (
                                                                    p.UseDualStack
                                                                    is True
                                                                ):
                                                                    if (
                                                                        get_attr(
                                                                            _locals[
                                                                                "PartitionResult"
                                                                            ],
                                                                            interpolate(
                                                                                "supportsDualStack",
                                                                                p,
                                                                                _locals,
                                                                            ),
                                                                        )
                                                                        is True
                                                                    ):
                                                                        return Endpoint(
                                                                            url=interpolate(
                                                                                "https://kinesis-queues.{Region}.{PartitionResult#dualStackDnsSuffix}",
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
                                                                        "https://kinesis-queues.{Region}.{PartitionResult#dnsSuffix}",
                                                                        p,
                                                                        _locals,
                                                                    ),
                                                                    properties={},
                                                                    headers={},
                                                                )
                                                            if string_equals(
                                                                get_attr(
                                                                    _locals[
                                                                        "PartitionResult"
                                                                    ],
                                                                    interpolate(
                                                                        "name",
                                                                        p,
                                                                        _locals,
                                                                    ),
                                                                ),
                                                                interpolate(
                                                                    "aws-iso-b",
                                                                    p,
                                                                    _locals,
                                                                ),
                                                            ):
                                                                if p.UseFIPS is True:
                                                                    if (
                                                                        p.UseDualStack
                                                                        is True
                                                                    ):
                                                                        if (
                                                                            get_attr(
                                                                                _locals[
                                                                                    "PartitionResult"
                                                                                ],
                                                                                interpolate(
                                                                                    "supportsFIPS",
                                                                                    p,
                                                                                    _locals,
                                                                                ),
                                                                            )
                                                                            is True
                                                                        ):
                                                                            if (
                                                                                get_attr(
                                                                                    _locals[
                                                                                        "PartitionResult"
                                                                                    ],
                                                                                    interpolate(
                                                                                        "supportsDualStack",
                                                                                        p,
                                                                                        _locals,
                                                                                    ),
                                                                                )
                                                                                is True
                                                                            ):
                                                                                return Endpoint(
                                                                                    url=interpolate(
                                                                                        "https://kinesis-queues-fips.{Region}.{PartitionResult#dualStackDnsSuffix}",
                                                                                        p,
                                                                                        _locals,
                                                                                    ),
                                                                                    properties={},
                                                                                    headers={},
                                                                                )
                                                                            raise EndpointError(
                                                                                interpolate(
                                                                                    "DualStack is enabled, but this partition does not support DualStack.",
                                                                                    p,
                                                                                    _locals,
                                                                                )
                                                                            )
                                                                        raise EndpointError(
                                                                            interpolate(
                                                                                "FIPS is enabled, but this partition does not support FIPS.",
                                                                                p,
                                                                                _locals,
                                                                            )
                                                                        )
                                                                if p.UseFIPS is True:
                                                                    if (
                                                                        get_attr(
                                                                            _locals[
                                                                                "PartitionResult"
                                                                            ],
                                                                            interpolate(
                                                                                "supportsFIPS",
                                                                                p,
                                                                                _locals,
                                                                            ),
                                                                        )
                                                                        is True
                                                                    ):
                                                                        return Endpoint(
                                                                            url=interpolate(
                                                                                "https://kinesis-queues-fips.{Region}.{PartitionResult#dnsSuffix}",
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
                                                                if (
                                                                    p.UseDualStack
                                                                    is True
                                                                ):
                                                                    if (
                                                                        get_attr(
                                                                            _locals[
                                                                                "PartitionResult"
                                                                            ],
                                                                            interpolate(
                                                                                "supportsDualStack",
                                                                                p,
                                                                                _locals,
                                                                            ),
                                                                        )
                                                                        is True
                                                                    ):
                                                                        return Endpoint(
                                                                            url=interpolate(
                                                                                "https://kinesis-queues.{Region}.{PartitionResult#dualStackDnsSuffix}",
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
                                                                        "https://kinesis-queues.{Region}.{PartitionResult#dnsSuffix}",
                                                                        p,
                                                                        _locals,
                                                                    ),
                                                                    properties={},
                                                                    headers={},
                                                                )
                                                        raise EndpointError(
                                                            interpolate(
                                                                "Invalid ARN: Invalid queue id.",
                                                                p,
                                                                _locals,
                                                            )
                                                        )
                                                    raise EndpointError(
                                                        interpolate(
                                                            "Invalid ARN: Missing queue id.",
                                                            p,
                                                            _locals,
                                                        )
                                                    )
                                                raise EndpointError(
                                                    interpolate(
                                                        "Operation Type is not set. Please contact service team for resolution.",
                                                        p,
                                                        _locals,
                                                    )
                                                )
                                            raise EndpointError(
                                                interpolate(
                                                    "Partition: {isoArn#partition} from ARN doesn't match with partition name: {PartitionResult#name}.",
                                                    p,
                                                    _locals,
                                                )
                                            )
                                        raise EndpointError(
                                            interpolate(
                                                "Invalid ARN: The ARN was not for the Kinesis service, found: {isoArn#service}.",
                                                p,
                                                _locals,
                                            )
                                        )
                                    raise EndpointError(
                                        interpolate(
                                            "Invalid ARN: Invalid region.", p, _locals
                                        )
                                    )
                                raise EndpointError(
                                    interpolate(
                                        "Invalid ARN: Invalid account id.", p, _locals
                                    )
                                )
    _locals: dict[str, Any] = {}
    if p.ChannelARN is not None:
        if not (p.Endpoint is not None):
            if p.Region is not None:
                _locals["PartitionResult"] = aws_partition(p.Region)
                if _locals["PartitionResult"] is not None:
                    if not (
                        string_equals(
                            get_attr(
                                _locals["PartitionResult"],
                                interpolate("name", p, _locals),
                            ),
                            interpolate("aws-iso", p, _locals),
                        )
                    ):
                        if not (
                            string_equals(
                                get_attr(
                                    _locals["PartitionResult"],
                                    interpolate("name", p, _locals),
                                ),
                                interpolate("aws-iso-b", p, _locals),
                            )
                        ):
                            _locals["arn"] = aws_parse_arn(p.ChannelARN)
                            if _locals["arn"] is not None:
                                if is_valid_host_label(
                                    get_attr(
                                        _locals["arn"],
                                        interpolate("accountId", p, _locals),
                                    ),
                                    False,
                                ):
                                    if is_valid_host_label(
                                        get_attr(
                                            _locals["arn"],
                                            interpolate("region", p, _locals),
                                        ),
                                        False,
                                    ):
                                        if string_equals(
                                            get_attr(
                                                _locals["arn"],
                                                interpolate("service", p, _locals),
                                            ),
                                            interpolate("kinesis", p, _locals),
                                        ):
                                            _locals["arnType"] = get_attr(
                                                _locals["arn"],
                                                interpolate(
                                                    "resourceId[0]", p, _locals
                                                ),
                                            )
                                            if _locals["arnType"] is not None:
                                                if not (
                                                    string_equals(
                                                        _locals["arnType"],
                                                        interpolate("", p, _locals),
                                                    )
                                                ):
                                                    if string_equals(
                                                        _locals["arnType"],
                                                        interpolate(
                                                            "channel", p, _locals
                                                        ),
                                                    ):
                                                        if string_equals(
                                                            get_attr(
                                                                _locals[
                                                                    "PartitionResult"
                                                                ],
                                                                interpolate(
                                                                    "name", p, _locals
                                                                ),
                                                            ),
                                                            interpolate(
                                                                "{arn#partition}",
                                                                p,
                                                                _locals,
                                                            ),
                                                        ):
                                                            if (
                                                                p.OperationType
                                                                is not None
                                                            ):
                                                                _locals["channelId"] = (
                                                                    get_attr(
                                                                        _locals["arn"],
                                                                        interpolate(
                                                                            "resourceId[1]",
                                                                            p,
                                                                            _locals,
                                                                        ),
                                                                    )
                                                                )
                                                                if (
                                                                    _locals["channelId"]
                                                                    is not None
                                                                ):
                                                                    if is_valid_host_label(
                                                                        _locals[
                                                                            "channelId"
                                                                        ],
                                                                        False,
                                                                    ):
                                                                        if not (
                                                                            string_equals(
                                                                                p.OperationType,
                                                                                interpolate(
                                                                                    "data",
                                                                                    p,
                                                                                    _locals,
                                                                                ),
                                                                            )
                                                                        ):
                                                                            if (
                                                                                p.UseFIPS
                                                                                is True
                                                                            ):
                                                                                if (
                                                                                    p.UseDualStack
                                                                                    is True
                                                                                ):
                                                                                    if (
                                                                                        get_attr(
                                                                                            _locals[
                                                                                                "PartitionResult"
                                                                                            ],
                                                                                            interpolate(
                                                                                                "supportsFIPS",
                                                                                                p,
                                                                                                _locals,
                                                                                            ),
                                                                                        )
                                                                                        is True
                                                                                    ):
                                                                                        if (
                                                                                            get_attr(
                                                                                                _locals[
                                                                                                    "PartitionResult"
                                                                                                ],
                                                                                                interpolate(
                                                                                                    "supportsDualStack",
                                                                                                    p,
                                                                                                    _locals,
                                                                                                ),
                                                                                            )
                                                                                            is True
                                                                                        ):
                                                                                            return Endpoint(
                                                                                                url=interpolate(
                                                                                                    "https://{channelId}.{OperationType}-kinesis-fips.{Region}.{PartitionResult#dualStackDnsSuffix}",
                                                                                                    p,
                                                                                                    _locals,
                                                                                                ),
                                                                                                properties={},
                                                                                                headers={},
                                                                                            )
                                                                                        raise EndpointError(
                                                                                            interpolate(
                                                                                                "DualStack is enabled, but this partition does not support DualStack.",
                                                                                                p,
                                                                                                _locals,
                                                                                            )
                                                                                        )
                                                                                    raise EndpointError(
                                                                                        interpolate(
                                                                                            "FIPS is enabled, but this partition does not support FIPS.",
                                                                                            p,
                                                                                            _locals,
                                                                                        )
                                                                                    )
                                                                            if (
                                                                                p.UseFIPS
                                                                                is True
                                                                            ):
                                                                                if (
                                                                                    get_attr(
                                                                                        _locals[
                                                                                            "PartitionResult"
                                                                                        ],
                                                                                        interpolate(
                                                                                            "supportsFIPS",
                                                                                            p,
                                                                                            _locals,
                                                                                        ),
                                                                                    )
                                                                                    is True
                                                                                ):
                                                                                    return Endpoint(
                                                                                        url=interpolate(
                                                                                            "https://{channelId}.{OperationType}-kinesis-fips.{Region}.{PartitionResult#dnsSuffix}",
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
                                                                            if (
                                                                                p.UseDualStack
                                                                                is True
                                                                            ):
                                                                                if (
                                                                                    get_attr(
                                                                                        _locals[
                                                                                            "PartitionResult"
                                                                                        ],
                                                                                        interpolate(
                                                                                            "supportsDualStack",
                                                                                            p,
                                                                                            _locals,
                                                                                        ),
                                                                                    )
                                                                                    is True
                                                                                ):
                                                                                    return Endpoint(
                                                                                        url=interpolate(
                                                                                            "https://{channelId}.{OperationType}-kinesis.{Region}.{PartitionResult#dualStackDnsSuffix}",
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
                                                                                    "https://{channelId}.{OperationType}-kinesis.{Region}.{PartitionResult#dnsSuffix}",
                                                                                    p,
                                                                                    _locals,
                                                                                ),
                                                                                properties={},
                                                                                headers={},
                                                                            )
                                                                        raise EndpointError(
                                                                            interpolate(
                                                                                "ChannelARN does not support the `data` operation type.",
                                                                                p,
                                                                                _locals,
                                                                            )
                                                                        )
                                                                    raise EndpointError(
                                                                        interpolate(
                                                                            "Invalid ARN: Invalid channel id.",
                                                                            p,
                                                                            _locals,
                                                                        )
                                                                    )
                                                                raise EndpointError(
                                                                    interpolate(
                                                                        "Invalid ARN: Missing channel id.",
                                                                        p,
                                                                        _locals,
                                                                    )
                                                                )
                                                            raise EndpointError(
                                                                interpolate(
                                                                    "Operation Type is not set. Please contact service team for resolution.",
                                                                    p,
                                                                    _locals,
                                                                )
                                                            )
                                                        raise EndpointError(
                                                            interpolate(
                                                                "Partition: {arn#partition} from ARN doesn't match with partition name: {PartitionResult#name}.",
                                                                p,
                                                                _locals,
                                                            )
                                                        )
                                                    raise EndpointError(
                                                        interpolate(
                                                            "Invalid ARN: ChannelARN only supports `channel` arn types, found: `{arnType}`.",
                                                            p,
                                                            _locals,
                                                        )
                                                    )
                                            raise EndpointError(
                                                interpolate(
                                                    "Invalid ARN: No ARN type specified",
                                                    p,
                                                    _locals,
                                                )
                                            )
                                        raise EndpointError(
                                            interpolate(
                                                "Invalid ARN: The ARN was not for the Kinesis service, found: {arn#service}.",
                                                p,
                                                _locals,
                                            )
                                        )
                                    raise EndpointError(
                                        interpolate(
                                            "Invalid ARN: Invalid region.", p, _locals
                                        )
                                    )
                                raise EndpointError(
                                    interpolate(
                                        "Invalid ARN: Invalid account id.", p, _locals
                                    )
                                )
                            raise EndpointError(
                                interpolate(
                                    "Invalid ARN: Failed to parse ARN.", p, _locals
                                )
                            )
    _locals: dict[str, Any] = {}
    if p.QueueARN is not None:
        if not (p.Endpoint is not None):
            if p.Region is not None:
                _locals["PartitionResult"] = aws_partition(p.Region)
                if _locals["PartitionResult"] is not None:
                    if string_equals(p.ResourceType, interpolate("queue", p, _locals)):
                        _locals["arn"] = aws_parse_arn(p.QueueARN)
                        if _locals["arn"] is not None:
                            if is_valid_host_label(
                                get_attr(
                                    _locals["arn"], interpolate("accountId", p, _locals)
                                ),
                                False,
                            ):
                                if is_valid_host_label(
                                    get_attr(
                                        _locals["arn"],
                                        interpolate("region", p, _locals),
                                    ),
                                    False,
                                ):
                                    if string_equals(
                                        get_attr(
                                            _locals["arn"],
                                            interpolate("service", p, _locals),
                                        ),
                                        interpolate("kinesis", p, _locals),
                                    ):
                                        _locals["arnType"] = get_attr(
                                            _locals["arn"],
                                            interpolate("resourceId[0]", p, _locals),
                                        )
                                        if _locals["arnType"] is not None:
                                            if not (
                                                string_equals(
                                                    _locals["arnType"],
                                                    interpolate("", p, _locals),
                                                )
                                            ):
                                                if string_equals(
                                                    _locals["arnType"],
                                                    interpolate("queue", p, _locals),
                                                ):
                                                    if string_equals(
                                                        get_attr(
                                                            _locals["PartitionResult"],
                                                            interpolate(
                                                                "name", p, _locals
                                                            ),
                                                        ),
                                                        interpolate(
                                                            "{arn#partition}",
                                                            p,
                                                            _locals,
                                                        ),
                                                    ):
                                                        if p.OperationType is not None:
                                                            _locals["queueId"] = (
                                                                get_attr(
                                                                    _locals["arn"],
                                                                    interpolate(
                                                                        "resourceId[1]",
                                                                        p,
                                                                        _locals,
                                                                    ),
                                                                )
                                                            )
                                                            if (
                                                                _locals["queueId"]
                                                                is not None
                                                            ):
                                                                if is_valid_host_label(
                                                                    _locals["queueId"],
                                                                    False,
                                                                ):
                                                                    if string_equals(
                                                                        get_attr(
                                                                            _locals[
                                                                                "PartitionResult"
                                                                            ],
                                                                            interpolate(
                                                                                "name",
                                                                                p,
                                                                                _locals,
                                                                            ),
                                                                        ),
                                                                        interpolate(
                                                                            "aws-iso",
                                                                            p,
                                                                            _locals,
                                                                        ),
                                                                    ):
                                                                        if (
                                                                            p.UseFIPS
                                                                            is True
                                                                        ):
                                                                            if (
                                                                                p.UseDualStack
                                                                                is True
                                                                            ):
                                                                                if (
                                                                                    get_attr(
                                                                                        _locals[
                                                                                            "PartitionResult"
                                                                                        ],
                                                                                        interpolate(
                                                                                            "supportsFIPS",
                                                                                            p,
                                                                                            _locals,
                                                                                        ),
                                                                                    )
                                                                                    is True
                                                                                ):
                                                                                    if (
                                                                                        get_attr(
                                                                                            _locals[
                                                                                                "PartitionResult"
                                                                                            ],
                                                                                            interpolate(
                                                                                                "supportsDualStack",
                                                                                                p,
                                                                                                _locals,
                                                                                            ),
                                                                                        )
                                                                                        is True
                                                                                    ):
                                                                                        return Endpoint(
                                                                                            url=interpolate(
                                                                                                "https://kinesis-queues-fips.{Region}.{PartitionResult#dualStackDnsSuffix}",
                                                                                                p,
                                                                                                _locals,
                                                                                            ),
                                                                                            properties={},
                                                                                            headers={},
                                                                                        )
                                                                                    raise EndpointError(
                                                                                        interpolate(
                                                                                            "DualStack is enabled, but this partition does not support DualStack.",
                                                                                            p,
                                                                                            _locals,
                                                                                        )
                                                                                    )
                                                                                raise EndpointError(
                                                                                    interpolate(
                                                                                        "FIPS is enabled, but this partition does not support FIPS.",
                                                                                        p,
                                                                                        _locals,
                                                                                    )
                                                                                )
                                                                        if (
                                                                            p.UseFIPS
                                                                            is True
                                                                        ):
                                                                            if (
                                                                                get_attr(
                                                                                    _locals[
                                                                                        "PartitionResult"
                                                                                    ],
                                                                                    interpolate(
                                                                                        "supportsFIPS",
                                                                                        p,
                                                                                        _locals,
                                                                                    ),
                                                                                )
                                                                                is True
                                                                            ):
                                                                                return Endpoint(
                                                                                    url=interpolate(
                                                                                        "https://kinesis-queues-fips.{Region}.{PartitionResult#dnsSuffix}",
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
                                                                        if (
                                                                            p.UseDualStack
                                                                            is True
                                                                        ):
                                                                            if (
                                                                                get_attr(
                                                                                    _locals[
                                                                                        "PartitionResult"
                                                                                    ],
                                                                                    interpolate(
                                                                                        "supportsDualStack",
                                                                                        p,
                                                                                        _locals,
                                                                                    ),
                                                                                )
                                                                                is True
                                                                            ):
                                                                                return Endpoint(
                                                                                    url=interpolate(
                                                                                        "https://kinesis-queues.{Region}.{PartitionResult#dualStackDnsSuffix}",
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
                                                                                "https://kinesis-queues.{Region}.{PartitionResult#dnsSuffix}",
                                                                                p,
                                                                                _locals,
                                                                            ),
                                                                            properties={},
                                                                            headers={},
                                                                        )
                                                                    if string_equals(
                                                                        get_attr(
                                                                            _locals[
                                                                                "PartitionResult"
                                                                            ],
                                                                            interpolate(
                                                                                "name",
                                                                                p,
                                                                                _locals,
                                                                            ),
                                                                        ),
                                                                        interpolate(
                                                                            "aws-iso-b",
                                                                            p,
                                                                            _locals,
                                                                        ),
                                                                    ):
                                                                        if (
                                                                            p.UseFIPS
                                                                            is True
                                                                        ):
                                                                            if (
                                                                                p.UseDualStack
                                                                                is True
                                                                            ):
                                                                                if (
                                                                                    get_attr(
                                                                                        _locals[
                                                                                            "PartitionResult"
                                                                                        ],
                                                                                        interpolate(
                                                                                            "supportsFIPS",
                                                                                            p,
                                                                                            _locals,
                                                                                        ),
                                                                                    )
                                                                                    is True
                                                                                ):
                                                                                    if (
                                                                                        get_attr(
                                                                                            _locals[
                                                                                                "PartitionResult"
                                                                                            ],
                                                                                            interpolate(
                                                                                                "supportsDualStack",
                                                                                                p,
                                                                                                _locals,
                                                                                            ),
                                                                                        )
                                                                                        is True
                                                                                    ):
                                                                                        return Endpoint(
                                                                                            url=interpolate(
                                                                                                "https://kinesis-queues-fips.{Region}.{PartitionResult#dualStackDnsSuffix}",
                                                                                                p,
                                                                                                _locals,
                                                                                            ),
                                                                                            properties={},
                                                                                            headers={},
                                                                                        )
                                                                                    raise EndpointError(
                                                                                        interpolate(
                                                                                            "DualStack is enabled, but this partition does not support DualStack.",
                                                                                            p,
                                                                                            _locals,
                                                                                        )
                                                                                    )
                                                                                raise EndpointError(
                                                                                    interpolate(
                                                                                        "FIPS is enabled, but this partition does not support FIPS.",
                                                                                        p,
                                                                                        _locals,
                                                                                    )
                                                                                )
                                                                        if (
                                                                            p.UseFIPS
                                                                            is True
                                                                        ):
                                                                            if (
                                                                                get_attr(
                                                                                    _locals[
                                                                                        "PartitionResult"
                                                                                    ],
                                                                                    interpolate(
                                                                                        "supportsFIPS",
                                                                                        p,
                                                                                        _locals,
                                                                                    ),
                                                                                )
                                                                                is True
                                                                            ):
                                                                                return Endpoint(
                                                                                    url=interpolate(
                                                                                        "https://kinesis-queues-fips.{Region}.{PartitionResult#dnsSuffix}",
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
                                                                        if (
                                                                            p.UseDualStack
                                                                            is True
                                                                        ):
                                                                            if (
                                                                                get_attr(
                                                                                    _locals[
                                                                                        "PartitionResult"
                                                                                    ],
                                                                                    interpolate(
                                                                                        "supportsDualStack",
                                                                                        p,
                                                                                        _locals,
                                                                                    ),
                                                                                )
                                                                                is True
                                                                            ):
                                                                                return Endpoint(
                                                                                    url=interpolate(
                                                                                        "https://kinesis-queues.{Region}.{PartitionResult#dualStackDnsSuffix}",
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
                                                                                "https://kinesis-queues.{Region}.{PartitionResult#dnsSuffix}",
                                                                                p,
                                                                                _locals,
                                                                            ),
                                                                            properties={},
                                                                            headers={},
                                                                        )
                                                                    if (
                                                                        p.UseFIPS
                                                                        is True
                                                                    ):
                                                                        if (
                                                                            p.UseDualStack
                                                                            is True
                                                                        ):
                                                                            if (
                                                                                get_attr(
                                                                                    _locals[
                                                                                        "PartitionResult"
                                                                                    ],
                                                                                    interpolate(
                                                                                        "supportsFIPS",
                                                                                        p,
                                                                                        _locals,
                                                                                    ),
                                                                                )
                                                                                is True
                                                                            ):
                                                                                if (
                                                                                    get_attr(
                                                                                        _locals[
                                                                                            "PartitionResult"
                                                                                        ],
                                                                                        interpolate(
                                                                                            "supportsDualStack",
                                                                                            p,
                                                                                            _locals,
                                                                                        ),
                                                                                    )
                                                                                    is True
                                                                                ):
                                                                                    return Endpoint(
                                                                                        url=interpolate(
                                                                                            "https://{queueId}.{OperationType}-kinesis-queues-fips.{Region}.{PartitionResult#dualStackDnsSuffix}",
                                                                                            p,
                                                                                            _locals,
                                                                                        ),
                                                                                        properties={},
                                                                                        headers={},
                                                                                    )
                                                                                raise EndpointError(
                                                                                    interpolate(
                                                                                        "DualStack is enabled, but this partition does not support DualStack.",
                                                                                        p,
                                                                                        _locals,
                                                                                    )
                                                                                )
                                                                            raise EndpointError(
                                                                                interpolate(
                                                                                    "FIPS is enabled, but this partition does not support FIPS.",
                                                                                    p,
                                                                                    _locals,
                                                                                )
                                                                            )
                                                                    if (
                                                                        p.UseFIPS
                                                                        is True
                                                                    ):
                                                                        if (
                                                                            get_attr(
                                                                                _locals[
                                                                                    "PartitionResult"
                                                                                ],
                                                                                interpolate(
                                                                                    "supportsFIPS",
                                                                                    p,
                                                                                    _locals,
                                                                                ),
                                                                            )
                                                                            is True
                                                                        ):
                                                                            return Endpoint(
                                                                                url=interpolate(
                                                                                    "https://{queueId}.{OperationType}-kinesis-queues-fips.{Region}.{PartitionResult#dnsSuffix}",
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
                                                                    if (
                                                                        p.UseDualStack
                                                                        is True
                                                                    ):
                                                                        if (
                                                                            get_attr(
                                                                                _locals[
                                                                                    "PartitionResult"
                                                                                ],
                                                                                interpolate(
                                                                                    "supportsDualStack",
                                                                                    p,
                                                                                    _locals,
                                                                                ),
                                                                            )
                                                                            is True
                                                                        ):
                                                                            return Endpoint(
                                                                                url=interpolate(
                                                                                    "https://{queueId}.{OperationType}-kinesis-queues.{Region}.{PartitionResult#dualStackDnsSuffix}",
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
                                                                            "https://{queueId}.{OperationType}-kinesis-queues.{Region}.{PartitionResult#dnsSuffix}",
                                                                            p,
                                                                            _locals,
                                                                        ),
                                                                        properties={},
                                                                        headers={},
                                                                    )
                                                                raise EndpointError(
                                                                    interpolate(
                                                                        "Invalid ARN: Invalid queue id.",
                                                                        p,
                                                                        _locals,
                                                                    )
                                                                )
                                                            raise EndpointError(
                                                                interpolate(
                                                                    "Invalid ARN: Missing queue id.",
                                                                    p,
                                                                    _locals,
                                                                )
                                                            )
                                                        raise EndpointError(
                                                            interpolate(
                                                                "Operation Type is not set. Please contact service team for resolution.",
                                                                p,
                                                                _locals,
                                                            )
                                                        )
                                                    raise EndpointError(
                                                        interpolate(
                                                            "Partition: {arn#partition} from ARN doesn't match with partition name: {PartitionResult#name}.",
                                                            p,
                                                            _locals,
                                                        )
                                                    )
                                                raise EndpointError(
                                                    interpolate(
                                                        "Invalid ARN: QueueARN only supports `queue` ARN types, found: `{arnType}`.",
                                                        p,
                                                        _locals,
                                                    )
                                                )
                                        raise EndpointError(
                                            interpolate(
                                                "Invalid ARN: No ARN type specified",
                                                p,
                                                _locals,
                                            )
                                        )
                                    raise EndpointError(
                                        interpolate(
                                            "Invalid ARN: The ARN was not for the Kinesis service, found: {arn#service}.",
                                            p,
                                            _locals,
                                        )
                                    )
                                raise EndpointError(
                                    interpolate(
                                        "Invalid ARN: Invalid region.", p, _locals
                                    )
                                )
                            raise EndpointError(
                                interpolate(
                                    "Invalid ARN: Invalid account id.", p, _locals
                                )
                            )
                        raise EndpointError(
                            interpolate("Invalid ARN: Failed to parse ARN.", p, _locals)
                        )
    _locals: dict[str, Any] = {}
    if p.QueueARN is not None:
        if not (p.Endpoint is not None):
            if not (string_equals(p.ResourceType, interpolate("queue", p, _locals))):
                raise EndpointError(
                    interpolate(
                        'Invalid Configuration: ResourceType must be "queue" when QueueARN is set.',
                        p,
                        _locals,
                    )
                )
    _locals: dict[str, Any] = {}
    if not (p.Endpoint is not None):
        if p.AccountIdEndpointMode is not None:
            if not (
                string_equals(
                    p.AccountIdEndpointMode, interpolate("disabled", p, _locals)
                )
            ):
                if p.AccountId is not None:
                    if p.Region is not None:
                        _locals["PartitionResult"] = aws_partition(p.Region)
                        if _locals["PartitionResult"] is not None:
                            if not (
                                string_equals(
                                    get_attr(
                                        _locals["PartitionResult"],
                                        interpolate("name", p, _locals),
                                    ),
                                    interpolate("aws-iso", p, _locals),
                                )
                            ):
                                if not (
                                    string_equals(
                                        get_attr(
                                            _locals["PartitionResult"],
                                            interpolate("name", p, _locals),
                                        ),
                                        interpolate("aws-iso-b", p, _locals),
                                    )
                                ):
                                    if is_valid_host_label(p.AccountId, False):
                                        if p.OperationType is not None:
                                            if string_equals(
                                                p.ResourceType,
                                                interpolate("queue", p, _locals),
                                            ):
                                                if p.UseFIPS is True:
                                                    if p.UseDualStack is True:
                                                        if (
                                                            get_attr(
                                                                _locals[
                                                                    "PartitionResult"
                                                                ],
                                                                interpolate(
                                                                    "supportsFIPS",
                                                                    p,
                                                                    _locals,
                                                                ),
                                                            )
                                                            is True
                                                        ):
                                                            if (
                                                                get_attr(
                                                                    _locals[
                                                                        "PartitionResult"
                                                                    ],
                                                                    interpolate(
                                                                        "supportsDualStack",
                                                                        p,
                                                                        _locals,
                                                                    ),
                                                                )
                                                                is True
                                                            ):
                                                                return Endpoint(
                                                                    url=interpolate(
                                                                        "https://{AccountId}.{OperationType}-kinesis-queues-fips.{Region}.{PartitionResult#dualStackDnsSuffix}",
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
                                                            raise EndpointError(
                                                                interpolate(
                                                                    "DualStack is enabled, but this partition does not support DualStack.",
                                                                    p,
                                                                    _locals,
                                                                )
                                                            )
                                                        raise EndpointError(
                                                            interpolate(
                                                                "FIPS is enabled, but this partition does not support FIPS.",
                                                                p,
                                                                _locals,
                                                            )
                                                        )
                                                if p.UseFIPS is True:
                                                    if (
                                                        get_attr(
                                                            _locals["PartitionResult"],
                                                            interpolate(
                                                                "supportsFIPS",
                                                                p,
                                                                _locals,
                                                            ),
                                                        )
                                                        is True
                                                    ):
                                                        return Endpoint(
                                                            url=interpolate(
                                                                "https://{AccountId}.{OperationType}-kinesis-queues-fips.{Region}.{PartitionResult#dnsSuffix}",
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
                                                            interpolate(
                                                                "supportsDualStack",
                                                                p,
                                                                _locals,
                                                            ),
                                                        )
                                                        is True
                                                    ):
                                                        return Endpoint(
                                                            url=interpolate(
                                                                "https://{AccountId}.{OperationType}-kinesis-queues.{Region}.{PartitionResult#dualStackDnsSuffix}",
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
                                                    raise EndpointError(
                                                        interpolate(
                                                            "DualStack is enabled but this partition does not support DualStack",
                                                            p,
                                                            _locals,
                                                        )
                                                    )
                                                return Endpoint(
                                                    url=interpolate(
                                                        "https://{AccountId}.{OperationType}-kinesis-queues.{Region}.{PartitionResult#dnsSuffix}",
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
                                            if not (
                                                string_equals(
                                                    p.ResourceType,
                                                    interpolate("queue", p, _locals),
                                                )
                                            ):
                                                if p.UseFIPS is True:
                                                    if p.UseDualStack is True:
                                                        if (
                                                            get_attr(
                                                                _locals[
                                                                    "PartitionResult"
                                                                ],
                                                                interpolate(
                                                                    "supportsFIPS",
                                                                    p,
                                                                    _locals,
                                                                ),
                                                            )
                                                            is True
                                                        ):
                                                            if (
                                                                get_attr(
                                                                    _locals[
                                                                        "PartitionResult"
                                                                    ],
                                                                    interpolate(
                                                                        "supportsDualStack",
                                                                        p,
                                                                        _locals,
                                                                    ),
                                                                )
                                                                is True
                                                            ):
                                                                return Endpoint(
                                                                    url=interpolate(
                                                                        "https://{AccountId}.{OperationType}-kinesis-fips.{Region}.{PartitionResult#dualStackDnsSuffix}",
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
                                                            raise EndpointError(
                                                                interpolate(
                                                                    "DualStack is enabled, but this partition does not support DualStack.",
                                                                    p,
                                                                    _locals,
                                                                )
                                                            )
                                                        raise EndpointError(
                                                            interpolate(
                                                                "FIPS is enabled, but this partition does not support FIPS.",
                                                                p,
                                                                _locals,
                                                            )
                                                        )
                                                if p.UseFIPS is True:
                                                    if (
                                                        get_attr(
                                                            _locals["PartitionResult"],
                                                            interpolate(
                                                                "supportsFIPS",
                                                                p,
                                                                _locals,
                                                            ),
                                                        )
                                                        is True
                                                    ):
                                                        return Endpoint(
                                                            url=interpolate(
                                                                "https://{AccountId}.{OperationType}-kinesis-fips.{Region}.{PartitionResult#dnsSuffix}",
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
                                                            interpolate(
                                                                "supportsDualStack",
                                                                p,
                                                                _locals,
                                                            ),
                                                        )
                                                        is True
                                                    ):
                                                        return Endpoint(
                                                            url=interpolate(
                                                                "https://{AccountId}.{OperationType}-kinesis.{Region}.{PartitionResult#dualStackDnsSuffix}",
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
                                                    raise EndpointError(
                                                        interpolate(
                                                            "DualStack is enabled but this partition does not support DualStack",
                                                            p,
                                                            _locals,
                                                        )
                                                    )
                                                return Endpoint(
                                                    url=interpolate(
                                                        "https://{AccountId}.{OperationType}-kinesis.{Region}.{PartitionResult#dnsSuffix}",
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
                                                "Operation Type is not set. Please contact service team for resolution.",
                                                p,
                                                _locals,
                                            )
                                        )
                                    raise EndpointError(
                                        interpolate("Invalid account id.", p, _locals)
                                    )
    _locals: dict[str, Any] = {}
    if not (p.Endpoint is not None):
        if p.AccountIdEndpointMode is not None:
            if string_equals(
                p.AccountIdEndpointMode, interpolate("required", p, _locals)
            ):
                if p.Region is not None:
                    _locals["PartitionResult"] = aws_partition(p.Region)
                    if _locals["PartitionResult"] is not None:
                        if not (
                            string_equals(
                                get_attr(
                                    _locals["PartitionResult"],
                                    interpolate("name", p, _locals),
                                ),
                                interpolate("aws-iso", p, _locals),
                            )
                        ):
                            if not (
                                string_equals(
                                    get_attr(
                                        _locals["PartitionResult"],
                                        interpolate("name", p, _locals),
                                    ),
                                    interpolate("aws-iso-b", p, _locals),
                                )
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
    _locals: dict[str, Any] = {}
    if not (p.Endpoint is not None):
        if string_equals(p.ResourceType, interpolate("queue", p, _locals)):
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
                                    return Endpoint(
                                        url=interpolate(
                                            "https://kinesis-queues-fips.{Region}.{PartitionResult#dualStackDnsSuffix}",
                                            p,
                                            _locals,
                                        ),
                                        properties={},
                                        headers={},
                                    )
                                raise EndpointError(
                                    interpolate(
                                        "DualStack is enabled, but this partition does not support DualStack.",
                                        p,
                                        _locals,
                                    )
                                )
                            raise EndpointError(
                                interpolate(
                                    "FIPS is enabled, but this partition does not support FIPS.",
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
                                    "https://kinesis-queues-fips.{Region}.{PartitionResult#dnsSuffix}",
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
                            return Endpoint(
                                url=interpolate(
                                    "https://kinesis-queues.{Region}.{PartitionResult#dualStackDnsSuffix}",
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
                            "https://kinesis-queues.{Region}.{PartitionResult#dnsSuffix}",
                            p,
                            _locals,
                        ),
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
        return Endpoint(url=p.Endpoint, properties={}, headers={})
    _locals: dict[str, Any] = {}
    if p.Region is not None:
        _locals["PartitionResult"] = aws_partition(p.Region)
        if _locals["PartitionResult"] is not None:
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
                                    "https://kinesis-fips.{Region}.{PartitionResult#dualStackDnsSuffix}",
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
                        return Endpoint(
                            url=interpolate(
                                "https://kinesis.{Region}.amazonaws.com", p, _locals
                            ),
                            properties={},
                            headers={},
                        )
                    return Endpoint(
                        url=interpolate(
                            "https://kinesis-fips.{Region}.{PartitionResult#dnsSuffix}",
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
                            "https://kinesis.{Region}.{PartitionResult#dualStackDnsSuffix}",
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
                    "https://kinesis.{Region}.{PartitionResult#dnsSuffix}", p, _locals
                ),
                properties={},
                headers={},
            )
    _locals: dict[str, Any] = {}
    raise EndpointError(
        interpolate("Invalid Configuration: Missing Region", p, _locals)
    )
    raise EndpointError("No endpoint rules matched")
