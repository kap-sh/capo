"""Generated from Smithy shape ``com.amazonaws.glue#ListMLTransformsResponse``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_glue.types.pagination_token
    import capo_glue.types.transform_id_list


class ListMLTransformsResponse(TypedDict, closed=True):
    transform_ids: "capo_glue.types.transform_id_list.TransformIdList"
    """<p>The identifiers of all the machine learning transforms in the account, or the machine learning transforms with the specified tags.</p>"""
    next_token: NotRequired["capo_glue.types.pagination_token.PaginationToken"]
    """<p>A continuation token, if the returned list does not contain the last metric available.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: ListMLTransformsResponse) -> dict:
    out: dict = {}
    import capo_glue.types.transform_id_list

    out["TransformIds"] = capo_glue.types.transform_id_list.serialize_aws_json_1_1(
        value["transform_ids"]
    )
    if "next_token" in value:
        out["NextToken"] = value["next_token"]
    return out


def deserialize_aws_json_1_1(data: dict) -> ListMLTransformsResponse:
    out: ListMLTransformsResponse = {}  # type: ignore[typeddict-item]
    if data.get("TransformIds") is not None:
        import capo_glue.types.transform_id_list

        out["transform_ids"] = (
            capo_glue.types.transform_id_list.deserialize_aws_json_1_1(
                data["TransformIds"]
            )
        )
    else:
        out["transform_ids"] = []
    if data.get("NextToken") is not None:
        out["next_token"] = data["NextToken"]
    return out
