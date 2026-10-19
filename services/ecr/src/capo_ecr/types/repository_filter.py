"""Generated from Smithy shape ``com.amazonaws.ecr#RepositoryFilter``."""

from typing import TYPE_CHECKING

from typing_extensions import TypedDict

if TYPE_CHECKING:
    import capo_ecr.types.repository_filter_type
    import capo_ecr.types.repository_filter_value


class RepositoryFilter(TypedDict, closed=True):
    filter: "capo_ecr.types.repository_filter_value.RepositoryFilterValue"
    """<p>The repository filter details. When the <code>PREFIX_MATCH</code> filter type is specified, this value is required and should be the repository name prefix to configure replication for.</p>"""
    filter_type: "capo_ecr.types.repository_filter_type.RepositoryFilterType"
    """<p>The repository filter type. The only supported value is <code>PREFIX_MATCH</code>, which is a repository name prefix specified with the <code>filter</code> parameter.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: RepositoryFilter) -> dict:
    out: dict = {}
    out["filter"] = value["filter"]
    import capo_ecr.types.repository_filter_type

    out["filterType"] = capo_ecr.types.repository_filter_type.serialize_aws_json_1_1(
        value["filter_type"]
    )
    return out


def deserialize_aws_json_1_1(data: dict) -> RepositoryFilter:
    out: RepositoryFilter = {}  # type: ignore[typeddict-item]
    if data.get("filter") is not None:
        out["filter"] = data["filter"]
    else:
        out["filter"] = ""
    if data.get("filterType") is not None:
        import capo_ecr.types.repository_filter_type

        out["filter_type"] = (
            capo_ecr.types.repository_filter_type.deserialize_aws_json_1_1(
                data["filterType"]
            )
        )
    else:
        import typing

        out["filter_type"] = typing.cast(
            "capo_ecr.types.repository_filter_type.RepositoryFilterType", ""
        )
    return out
