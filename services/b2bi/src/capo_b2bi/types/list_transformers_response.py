"""Generated from Smithy shape ``com.amazonaws.b2bi#ListTransformersResponse``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_b2bi.types.page_token
    import capo_b2bi.types.transformer_list


class ListTransformersResponse(TypedDict, closed=True):
    transformers: "capo_b2bi.types.transformer_list.TransformerList"
    """<p>Returns an array of one or more transformer objects.</p> <p>For each transformer, a <code>TransformerSummary</code> object is returned. The <code>TransformerSummary</code> contains all the details for a specific transformer.</p>"""
    next_token: NotRequired["capo_b2bi.types.page_token.PageToken"]
    """<p>When additional results are obtained from the command, a <code>NextToken</code> parameter is returned in the output. You can then pass the <code>NextToken</code> parameter in a subsequent command to continue listing additional resources.</p>"""


# --- awsJson1_0 ser/de ---
def serialize_aws_json_1_0(value: ListTransformersResponse) -> dict:
    out: dict = {}
    import capo_b2bi.types.transformer_list

    out["transformers"] = capo_b2bi.types.transformer_list.serialize_aws_json_1_0(
        value["transformers"]
    )
    if "next_token" in value:
        out["nextToken"] = value["next_token"]
    return out


def deserialize_aws_json_1_0(data: dict) -> ListTransformersResponse:
    out: ListTransformersResponse = {}  # type: ignore[typeddict-item]
    if data.get("transformers") is not None:
        import capo_b2bi.types.transformer_list

        out["transformers"] = capo_b2bi.types.transformer_list.deserialize_aws_json_1_0(
            data["transformers"]
        )
    else:
        out["transformers"] = []
    if data.get("nextToken") is not None:
        out["next_token"] = data["nextToken"]
    return out
