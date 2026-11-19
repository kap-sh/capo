"""Generated from Smithy shape ``com.amazonaws.comprehend#DetectToxicContentResponse``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_comprehend.types.list_of_toxic_labels


class DetectToxicContentResponse(TypedDict, closed=True):
    result_list: NotRequired[
        "capo_comprehend.types.list_of_toxic_labels.ListOfToxicLabels"
    ]
    """<p>Results of the content moderation analysis. Each entry in the results list contains a list of toxic content types identified in the text, along with a confidence score for each content type. The results list also includes a toxicity score for each entry in the results list. </p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: DetectToxicContentResponse) -> dict:
    out: dict = {}
    if "result_list" in value:
        import capo_comprehend.types.list_of_toxic_labels

        out["ResultList"] = (
            capo_comprehend.types.list_of_toxic_labels.serialize_aws_json_1_1(
                value["result_list"]
            )
        )
    return out


def deserialize_aws_json_1_1(data: dict) -> DetectToxicContentResponse:
    out: DetectToxicContentResponse = {}  # type: ignore[typeddict-item]
    if data.get("ResultList") is not None:
        import capo_comprehend.types.list_of_toxic_labels

        out["result_list"] = (
            capo_comprehend.types.list_of_toxic_labels.deserialize_aws_json_1_1(
                data["ResultList"]
            )
        )
    return out


# --- rpcv2Cbor ser/de ---
def serialize_cbor(value: DetectToxicContentResponse) -> dict:
    out: dict = {}
    if "result_list" in value:
        import capo_comprehend.types.list_of_toxic_labels

        out["ResultList"] = capo_comprehend.types.list_of_toxic_labels.serialize_cbor(
            value["result_list"]
        )
    return out


def deserialize_cbor(data: dict) -> DetectToxicContentResponse:
    out: DetectToxicContentResponse = {}  # type: ignore[typeddict-item]
    if data.get("ResultList") is not None:
        import capo_comprehend.types.list_of_toxic_labels

        out["result_list"] = (
            capo_comprehend.types.list_of_toxic_labels.deserialize_cbor(
                data["ResultList"]
            )
        )
    return out
