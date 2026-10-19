"""Generated from Smithy shape ``com.amazonaws.kendra#RelevanceFeedback``."""

from typing import TYPE_CHECKING

from typing_extensions import TypedDict

if TYPE_CHECKING:
    import capo_kendra.types.relevance_type
    import capo_kendra.types.result_id


class RelevanceFeedback(TypedDict, closed=True):
    result_id: "capo_kendra.types.result_id.ResultId"
    """<p>The identifier of the search result that the user provided relevance feedback for.</p>"""
    relevance_value: "capo_kendra.types.relevance_type.RelevanceType"
    """<p>Whether the document was relevant or not relevant to the search.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: RelevanceFeedback) -> dict:
    out: dict = {}
    out["ResultId"] = value["result_id"]
    import capo_kendra.types.relevance_type

    out["RelevanceValue"] = capo_kendra.types.relevance_type.serialize_aws_json_1_1(
        value["relevance_value"]
    )
    return out


def deserialize_aws_json_1_1(data: dict) -> RelevanceFeedback:
    out: RelevanceFeedback = {}  # type: ignore[typeddict-item]
    if data.get("ResultId") is not None:
        out["result_id"] = data["ResultId"]
    else:
        out["result_id"] = ""
    if data.get("RelevanceValue") is not None:
        import capo_kendra.types.relevance_type

        out["relevance_value"] = (
            capo_kendra.types.relevance_type.deserialize_aws_json_1_1(
                data["RelevanceValue"]
            )
        )
    else:
        import typing

        out["relevance_value"] = typing.cast(
            "capo_kendra.types.relevance_type.RelevanceType", ""
        )
    return out
