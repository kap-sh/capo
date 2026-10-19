"""Generated from Smithy shape ``com.amazonaws.connect#ListDataTableAttributesResponse``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_connect.types.attribute_list
    import capo_connect.types.next_token


class ListDataTableAttributesResponse(TypedDict, closed=True):
    next_token: NotRequired["capo_connect.types.next_token.NextToken"]
    """<p>Specify the pagination token from a previous request to retrieve the next page of results.</p>"""
    attributes: "capo_connect.types.attribute_list.AttributeList"
    """<p>A list of data table attributes with their complete configuration and metadata.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: ListDataTableAttributesResponse) -> dict:
    out: dict = {}
    if "next_token" in value:
        out["NextToken"] = value["next_token"]
    import capo_connect.types.attribute_list

    out["Attributes"] = capo_connect.types.attribute_list.serialize_json(
        value["attributes"]
    )
    return out


def deserialize_json(data: dict) -> ListDataTableAttributesResponse:
    out: ListDataTableAttributesResponse = {}  # type: ignore[typeddict-item]
    if data.get("NextToken") is not None:
        out["next_token"] = data["NextToken"]
    if data.get("Attributes") is not None:
        import capo_connect.types.attribute_list

        out["attributes"] = capo_connect.types.attribute_list.deserialize_json(
            data["Attributes"]
        )
    else:
        out["attributes"] = []
    return out
