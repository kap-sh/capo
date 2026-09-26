"""Generated from Smithy shape ``com.amazonaws.lambdamicrovms#ListMicrovmImagesResponse``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

from capo_lambda_microvms.errors import DeserializationError

if TYPE_CHECKING:
    import capo_lambda_microvms.types.microvm_image_summaries
    import capo_lambda_microvms.types.string


class ListMicrovmImagesResponse(TypedDict, closed=True):
    next_token: NotRequired["capo_lambda_microvms.types.string.String"]
    """<p>The pagination token to use in a subsequent request to retrieve the next page of results. This value is null when there are no more results to return.</p>"""
    items: "capo_lambda_microvms.types.microvm_image_summaries.MicrovmImageSummaries"
    """<p>The list of MicroVM images.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: ListMicrovmImagesResponse) -> dict:
    out: dict = {}
    if "next_token" in value:
        out["nextToken"] = value["next_token"]
    import capo_lambda_microvms.types.microvm_image_summaries

    out["items"] = capo_lambda_microvms.types.microvm_image_summaries.serialize_json(
        value["items"]
    )
    return out


def deserialize_json(data: dict) -> ListMicrovmImagesResponse:
    out: ListMicrovmImagesResponse = {}  # type: ignore[typeddict-item]
    if data.get("nextToken") is not None:
        out["next_token"] = data["nextToken"]
    if data.get("items") is not None:
        import capo_lambda_microvms.types.microvm_image_summaries

        out["items"] = (
            capo_lambda_microvms.types.microvm_image_summaries.deserialize_json(
                data["items"]
            )
        )
    else:
        raise DeserializationError("ListMicrovmImagesResponse.items required")
    return out
