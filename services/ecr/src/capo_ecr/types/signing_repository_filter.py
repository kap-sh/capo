"""Generated from Smithy shape ``com.amazonaws.ecr#SigningRepositoryFilter``."""

from typing import TYPE_CHECKING

from typing_extensions import TypedDict

if TYPE_CHECKING:
    import capo_ecr.types.signing_repository_filter_type
    import capo_ecr.types.signing_repository_filter_value


class SigningRepositoryFilter(TypedDict, closed=True):
    filter: (
        "capo_ecr.types.signing_repository_filter_value.SigningRepositoryFilterValue"
    )
    """<p>The filter value used to match repository names. When using <code>WILDCARD_MATCH</code>, the <code>*</code> character matches any sequence of characters.</p> <p>Examples:</p> <ul> <li> <p> <code>myapp/*</code> - Matches all repositories starting with <code>myapp/</code> </p> </li> <li> <p> <code>*/production</code> - Matches all repositories ending with <code>/production</code> </p> </li> <li> <p> <code>*prod*</code> - Matches all repositories containing <code>prod</code> </p> </li> </ul>"""
    filter_type: (
        "capo_ecr.types.signing_repository_filter_type.SigningRepositoryFilterType"
    )
    """<p>The type of filter to apply. Currently, only <code>WILDCARD_MATCH</code> is supported, which uses wildcard patterns to match repository names.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: SigningRepositoryFilter) -> dict:
    out: dict = {}
    out["filter"] = value["filter"]
    import capo_ecr.types.signing_repository_filter_type

    out["filterType"] = (
        capo_ecr.types.signing_repository_filter_type.serialize_aws_json_1_1(
            value["filter_type"]
        )
    )
    return out


def deserialize_aws_json_1_1(data: dict) -> SigningRepositoryFilter:
    out: SigningRepositoryFilter = {}  # type: ignore[typeddict-item]
    if data.get("filter") is not None:
        out["filter"] = data["filter"]
    else:
        out["filter"] = ""
    if data.get("filterType") is not None:
        import capo_ecr.types.signing_repository_filter_type

        out["filter_type"] = (
            capo_ecr.types.signing_repository_filter_type.deserialize_aws_json_1_1(
                data["filterType"]
            )
        )
    else:
        import typing

        out["filter_type"] = typing.cast(
            "capo_ecr.types.signing_repository_filter_type.SigningRepositoryFilterType",
            "",
        )
    return out
