"""Generated from Smithy shape ``com.amazonaws.personalize#DescribeFilterResponse``."""

from typing import TYPE_CHECKING, Any

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_personalize.types.filter


class DescribeFilterResponse(TypedDict, closed=True):
    filter: NotRequired["capo_personalize.types.filter.Filter"]
    """<p>The filter's details.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: DescribeFilterResponse) -> dict:
    out: dict = {}
    if "filter" in value:
        import capo_personalize.types.filter

        out["filter"] = capo_personalize.types.filter.serialize_aws_json_1_1(
            value["filter"]
        )
    return out


def deserialize_aws_json_1_1(data: dict) -> DescribeFilterResponse:
    out: DescribeFilterResponse = {}  # type: ignore[typeddict-item]
    if data.get("filter") is not None:
        import capo_personalize.types.filter

        out["filter"] = capo_personalize.types.filter.deserialize_aws_json_1_1(
            data["filter"]
        )
    return out


def redact_sensitive(value: DescribeFilterResponse) -> dict[str, Any]:
    out: dict[str, Any] = dict(value)
    if "filter" in value:
        import capo_personalize.types.filter

        out["filter"] = capo_personalize.types.filter.redact_sensitive(value["filter"])
    return out
