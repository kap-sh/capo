"""Generated from Smithy shape ``com.amazonaws.kendra#BatchDeleteFeaturedResultsSetError``."""

from typing import TYPE_CHECKING

from typing_extensions import TypedDict

if TYPE_CHECKING:
    import capo_kendra.types.error_code
    import capo_kendra.types.error_message
    import capo_kendra.types.featured_results_set_id


class BatchDeleteFeaturedResultsSetError(TypedDict, closed=True):
    id: "capo_kendra.types.featured_results_set_id.FeaturedResultsSetId"
    """<p>The identifier of the set of featured results that couldn't be removed from the index.</p>"""
    error_code: "capo_kendra.types.error_code.ErrorCode"
    """<p>The error code for why the set of featured results couldn't be removed from the index.</p>"""
    error_message: "capo_kendra.types.error_message.ErrorMessage"
    """<p>An explanation for why the set of featured results couldn't be removed from the index.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: BatchDeleteFeaturedResultsSetError) -> dict:
    out: dict = {}
    out["Id"] = value["id"]
    import capo_kendra.types.error_code

    out["ErrorCode"] = capo_kendra.types.error_code.serialize_aws_json_1_1(
        value["error_code"]
    )
    out["ErrorMessage"] = value["error_message"]
    return out


def deserialize_aws_json_1_1(data: dict) -> BatchDeleteFeaturedResultsSetError:
    out: BatchDeleteFeaturedResultsSetError = {}  # type: ignore[typeddict-item]
    if data.get("Id") is not None:
        out["id"] = data["Id"]
    else:
        out["id"] = ""
    if data.get("ErrorCode") is not None:
        import capo_kendra.types.error_code

        out["error_code"] = capo_kendra.types.error_code.deserialize_aws_json_1_1(
            data["ErrorCode"]
        )
    else:
        import typing

        out["error_code"] = typing.cast("capo_kendra.types.error_code.ErrorCode", "")
    if data.get("ErrorMessage") is not None:
        out["error_message"] = data["ErrorMessage"]
    else:
        out["error_message"] = ""
    return out
