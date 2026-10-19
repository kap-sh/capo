"""Generated from Smithy shape ``com.amazonaws.ecr#RegistryScanningRule``."""

from typing import TYPE_CHECKING

from typing_extensions import TypedDict

if TYPE_CHECKING:
    import capo_ecr.types.scan_frequency
    import capo_ecr.types.scanning_repository_filter_list


class RegistryScanningRule(TypedDict, closed=True):
    scan_frequency: "capo_ecr.types.scan_frequency.ScanFrequency"
    """<p>The frequency that scans are performed at for a private registry. When the <code>ENHANCED</code> scan type is specified, the supported scan frequencies are <code>CONTINUOUS_SCAN</code> and <code>SCAN_ON_PUSH</code>. When the <code>BASIC</code> scan type is specified, the <code>SCAN_ON_PUSH</code> scan frequency is supported. If scan on push is not specified, then the <code>MANUAL</code> scan frequency is set by default.</p>"""
    repository_filters: (
        "capo_ecr.types.scanning_repository_filter_list.ScanningRepositoryFilterList"
    )
    """<p>The repository filters associated with the scanning configuration for a private registry.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: RegistryScanningRule) -> dict:
    out: dict = {}
    import capo_ecr.types.scan_frequency

    out["scanFrequency"] = capo_ecr.types.scan_frequency.serialize_aws_json_1_1(
        value["scan_frequency"]
    )
    import capo_ecr.types.scanning_repository_filter_list

    out["repositoryFilters"] = (
        capo_ecr.types.scanning_repository_filter_list.serialize_aws_json_1_1(
            value["repository_filters"]
        )
    )
    return out


def deserialize_aws_json_1_1(data: dict) -> RegistryScanningRule:
    out: RegistryScanningRule = {}  # type: ignore[typeddict-item]
    if data.get("scanFrequency") is not None:
        import capo_ecr.types.scan_frequency

        out["scan_frequency"] = capo_ecr.types.scan_frequency.deserialize_aws_json_1_1(
            data["scanFrequency"]
        )
    else:
        import typing

        out["scan_frequency"] = typing.cast(
            "capo_ecr.types.scan_frequency.ScanFrequency", ""
        )
    if data.get("repositoryFilters") is not None:
        import capo_ecr.types.scanning_repository_filter_list

        out["repository_filters"] = (
            capo_ecr.types.scanning_repository_filter_list.deserialize_aws_json_1_1(
                data["repositoryFilters"]
            )
        )
    else:
        out["repository_filters"] = []
    return out
