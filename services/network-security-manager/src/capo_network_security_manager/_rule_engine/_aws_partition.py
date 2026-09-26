"""AWS partitions table and ``aws.partition`` rules-engine function.

Data sourced from AWS SDK ``partitions.json``. All dispatch tables are
materialised at codegen time:

* ``_REGION_LOOKUP`` — O(1) dict of explicit region name -> partition outputs.
* ``_REGEX_LOOKUP`` — compiled-regex / outputs pairs for unknown regions.
* ``_DEFAULT_OUTPUTS`` — fallback partition (``aws``)."""

from __future__ import annotations

import re
from typing import Any

_PARTITION_AWS: dict[str, Any] = {
    "dnsSuffix": "amazonaws.com",
    "dualStackDnsSuffix": "api.aws",
    "implicitGlobalRegion": "us-east-1",
    "name": "aws",
    "supportsDualStack": True,
    "supportsFIPS": True,
}
_PARTITION_AWS_CN: dict[str, Any] = {
    "dnsSuffix": "amazonaws.com.cn",
    "dualStackDnsSuffix": "api.amazonwebservices.com.cn",
    "implicitGlobalRegion": "cn-northwest-1",
    "name": "aws-cn",
    "supportsDualStack": True,
    "supportsFIPS": True,
}
_PARTITION_AWS_EUSC: dict[str, Any] = {
    "dnsSuffix": "amazonaws.eu",
    "dualStackDnsSuffix": "api.amazonwebservices.eu",
    "implicitGlobalRegion": "eusc-de-east-1",
    "name": "aws-eusc",
    "supportsDualStack": True,
    "supportsFIPS": True,
}
_PARTITION_AWS_ISO: dict[str, Any] = {
    "dnsSuffix": "c2s.ic.gov",
    "dualStackDnsSuffix": "api.aws.ic.gov",
    "implicitGlobalRegion": "us-iso-east-1",
    "name": "aws-iso",
    "supportsDualStack": True,
    "supportsFIPS": True,
}
_PARTITION_AWS_ISO_B: dict[str, Any] = {
    "dnsSuffix": "sc2s.sgov.gov",
    "dualStackDnsSuffix": "api.aws.scloud",
    "implicitGlobalRegion": "us-isob-east-1",
    "name": "aws-iso-b",
    "supportsDualStack": True,
    "supportsFIPS": True,
}
_PARTITION_AWS_ISO_E: dict[str, Any] = {
    "dnsSuffix": "cloud.adc-e.uk",
    "dualStackDnsSuffix": "api.cloud-aws.adc-e.uk",
    "implicitGlobalRegion": "eu-isoe-west-1",
    "name": "aws-iso-e",
    "supportsDualStack": True,
    "supportsFIPS": True,
}
_PARTITION_AWS_ISO_F: dict[str, Any] = {
    "dnsSuffix": "csp.hci.ic.gov",
    "dualStackDnsSuffix": "api.aws.hci.ic.gov",
    "implicitGlobalRegion": "us-isof-south-1",
    "name": "aws-iso-f",
    "supportsDualStack": True,
    "supportsFIPS": True,
}
_PARTITION_AWS_US_GOV: dict[str, Any] = {
    "dnsSuffix": "amazonaws.com",
    "dualStackDnsSuffix": "api.aws",
    "implicitGlobalRegion": "us-gov-west-1",
    "name": "aws-us-gov",
    "supportsDualStack": True,
    "supportsFIPS": True,
}

_REGION_LOOKUP: dict[str, dict[str, Any]] = {
    "af-south-1": _PARTITION_AWS,
    "ap-east-1": _PARTITION_AWS,
    "ap-east-2": _PARTITION_AWS,
    "ap-northeast-1": _PARTITION_AWS,
    "ap-northeast-2": _PARTITION_AWS,
    "ap-northeast-3": _PARTITION_AWS,
    "ap-south-1": _PARTITION_AWS,
    "ap-south-2": _PARTITION_AWS,
    "ap-southeast-1": _PARTITION_AWS,
    "ap-southeast-2": _PARTITION_AWS,
    "ap-southeast-3": _PARTITION_AWS,
    "ap-southeast-4": _PARTITION_AWS,
    "ap-southeast-5": _PARTITION_AWS,
    "ap-southeast-6": _PARTITION_AWS,
    "ap-southeast-7": _PARTITION_AWS,
    "aws-global": _PARTITION_AWS,
    "ca-central-1": _PARTITION_AWS,
    "ca-west-1": _PARTITION_AWS,
    "eu-central-1": _PARTITION_AWS,
    "eu-central-2": _PARTITION_AWS,
    "eu-north-1": _PARTITION_AWS,
    "eu-south-1": _PARTITION_AWS,
    "eu-south-2": _PARTITION_AWS,
    "eu-west-1": _PARTITION_AWS,
    "eu-west-2": _PARTITION_AWS,
    "eu-west-3": _PARTITION_AWS,
    "il-central-1": _PARTITION_AWS,
    "me-central-1": _PARTITION_AWS,
    "me-south-1": _PARTITION_AWS,
    "mx-central-1": _PARTITION_AWS,
    "sa-east-1": _PARTITION_AWS,
    "us-east-1": _PARTITION_AWS,
    "us-east-2": _PARTITION_AWS,
    "us-west-1": _PARTITION_AWS,
    "us-west-2": _PARTITION_AWS,
    "aws-cn-global": _PARTITION_AWS_CN,
    "cn-north-1": _PARTITION_AWS_CN,
    "cn-northwest-1": _PARTITION_AWS_CN,
    "eusc-de-east-1": _PARTITION_AWS_EUSC,
    "aws-iso-global": _PARTITION_AWS_ISO,
    "us-iso-east-1": _PARTITION_AWS_ISO,
    "us-iso-west-1": _PARTITION_AWS_ISO,
    "aws-iso-b-global": _PARTITION_AWS_ISO_B,
    "us-isob-east-1": _PARTITION_AWS_ISO_B,
    "us-isob-west-1": _PARTITION_AWS_ISO_B,
    "aws-iso-e-global": _PARTITION_AWS_ISO_E,
    "eu-isoe-west-1": _PARTITION_AWS_ISO_E,
    "aws-iso-f-global": _PARTITION_AWS_ISO_F,
    "us-isof-east-1": _PARTITION_AWS_ISO_F,
    "us-isof-south-1": _PARTITION_AWS_ISO_F,
    "aws-us-gov-global": _PARTITION_AWS_US_GOV,
    "us-gov-east-1": _PARTITION_AWS_US_GOV,
    "us-gov-west-1": _PARTITION_AWS_US_GOV,
}

_REGEX_LOOKUP: tuple[tuple[re.Pattern[str], dict[str, Any]], ...] = (
    (re.compile(r"^(us|eu|ap|sa|ca|me|af|il|mx)\-\w+\-\d+$"), _PARTITION_AWS),
    (re.compile(r"^cn\-\w+\-\d+$"), _PARTITION_AWS_CN),
    (re.compile(r"^eusc\-(de)\-\w+\-\d+$"), _PARTITION_AWS_EUSC),
    (re.compile(r"^us\-iso\-\w+\-\d+$"), _PARTITION_AWS_ISO),
    (re.compile(r"^us\-isob\-\w+\-\d+$"), _PARTITION_AWS_ISO_B),
    (re.compile(r"^eu\-isoe\-\w+\-\d+$"), _PARTITION_AWS_ISO_E),
    (re.compile(r"^us\-isof\-\w+\-\d+$"), _PARTITION_AWS_ISO_F),
    (re.compile(r"^us\-gov\-\w+\-\d+$"), _PARTITION_AWS_US_GOV),
)

_DEFAULT_OUTPUTS: dict[str, Any] = _PARTITION_AWS


def aws_partition(region: Any) -> dict[str, Any] | None:
    """Resolve ``region`` to a partition outputs dict."""
    if not isinstance(region, str):
        return None
    outputs = _REGION_LOOKUP.get(region)
    if outputs is not None:
        return outputs
    for pattern, outputs in _REGEX_LOOKUP:
        if pattern.fullmatch(region):
            return outputs
    return _DEFAULT_OUTPUTS
