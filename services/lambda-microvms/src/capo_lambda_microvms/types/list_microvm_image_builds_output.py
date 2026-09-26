"""Generated from Smithy shape ``com.amazonaws.lambdamicrovms#ListMicrovmImageBuildsOutput``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

from capo_lambda_microvms.errors import DeserializationError

if TYPE_CHECKING:
    import capo_lambda_microvms.types.microvm_image_build_summaries
    import capo_lambda_microvms.types.string


class ListMicrovmImageBuildsOutput(TypedDict, closed=True):
    next_token: NotRequired["capo_lambda_microvms.types.string.String"]
    """<p>The pagination token to use in a subsequent request to retrieve the next page of results. This value is null when there are no more results to return.</p>"""
    items: "capo_lambda_microvms.types.microvm_image_build_summaries.MicrovmImageBuildSummaries"
    """<p>The list of MicroVM image builds.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: ListMicrovmImageBuildsOutput) -> dict:
    out: dict = {}
    if "next_token" in value:
        out["nextToken"] = value["next_token"]
    import capo_lambda_microvms.types.microvm_image_build_summaries

    out["items"] = (
        capo_lambda_microvms.types.microvm_image_build_summaries.serialize_json(
            value["items"]
        )
    )
    return out


def deserialize_json(data: dict) -> ListMicrovmImageBuildsOutput:
    out: ListMicrovmImageBuildsOutput = {}  # type: ignore[typeddict-item]
    if data.get("nextToken") is not None:
        out["next_token"] = data["nextToken"]
    if data.get("items") is not None:
        import capo_lambda_microvms.types.microvm_image_build_summaries

        out["items"] = (
            capo_lambda_microvms.types.microvm_image_build_summaries.deserialize_json(
                data["items"]
            )
        )
    else:
        raise DeserializationError("ListMicrovmImageBuildsOutput.items required")
    return out
