"""Generated from Smithy shape ``com.amazonaws.glue#ListFormTypesResponse``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_glue.types.form_type_item_list
    import capo_glue.types.token


class ListFormTypesResponse(TypedDict, closed=True):
    items: "capo_glue.types.form_type_item_list.FormTypeItemList"
    """<p>The list of form type items.</p>"""
    next_token: NotRequired["capo_glue.types.token.Token"]
    """<p>A continuation token, present if the current segment is not the last.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: ListFormTypesResponse) -> dict:
    out: dict = {}
    import capo_glue.types.form_type_item_list

    out["Items"] = capo_glue.types.form_type_item_list.serialize_aws_json_1_1(
        value["items"]
    )
    if "next_token" in value:
        out["NextToken"] = value["next_token"]
    return out


def deserialize_aws_json_1_1(data: dict) -> ListFormTypesResponse:
    out: ListFormTypesResponse = {}  # type: ignore[typeddict-item]
    if data.get("Items") is not None:
        import capo_glue.types.form_type_item_list

        out["items"] = capo_glue.types.form_type_item_list.deserialize_aws_json_1_1(
            data["Items"]
        )
    else:
        out["items"] = []
    if data.get("NextToken") is not None:
        out["next_token"] = data["NextToken"]
    return out
