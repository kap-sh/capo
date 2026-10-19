"""Generated from Smithy shape ``com.amazonaws.glue#GetMLTransformsResponse``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_glue.types.pagination_token
    import capo_glue.types.transform_list


class GetMLTransformsResponse(TypedDict, closed=True):
    transforms: "capo_glue.types.transform_list.TransformList"
    """<p>A list of machine learning transforms.</p>"""
    next_token: NotRequired["capo_glue.types.pagination_token.PaginationToken"]
    """<p>A pagination token, if more results are available.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: GetMLTransformsResponse) -> dict:
    out: dict = {}
    import capo_glue.types.transform_list

    out["Transforms"] = capo_glue.types.transform_list.serialize_aws_json_1_1(
        value["transforms"]
    )
    if "next_token" in value:
        out["NextToken"] = value["next_token"]
    return out


def deserialize_aws_json_1_1(data: dict) -> GetMLTransformsResponse:
    out: GetMLTransformsResponse = {}  # type: ignore[typeddict-item]
    if data.get("Transforms") is not None:
        import capo_glue.types.transform_list

        out["transforms"] = capo_glue.types.transform_list.deserialize_aws_json_1_1(
            data["Transforms"]
        )
    else:
        out["transforms"] = []
    if data.get("NextToken") is not None:
        out["next_token"] = data["NextToken"]
    return out
