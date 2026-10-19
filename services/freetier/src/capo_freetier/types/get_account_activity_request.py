"""Generated from Smithy shape ``com.amazonaws.freetier#GetAccountActivityRequest``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_freetier.types.activity_id
    import capo_freetier.types.language_code


class GetAccountActivityRequest(TypedDict, closed=True):
    activity_id: "capo_freetier.types.activity_id.ActivityId"
    """<p> A unique identifier that identifies the activity. </p>"""
    language_code: NotRequired["capo_freetier.types.language_code.LanguageCode"]
    """<p> The language code used to return translated title and description fields. </p>"""


# --- awsJson1_0 ser/de ---
def serialize_aws_json_1_0(value: GetAccountActivityRequest) -> dict:
    out: dict = {}
    out["activityId"] = value["activity_id"]
    if "language_code" in value:
        import capo_freetier.types.language_code

        out["languageCode"] = capo_freetier.types.language_code.serialize_aws_json_1_0(
            value["language_code"]
        )
    return out


def deserialize_aws_json_1_0(data: dict) -> GetAccountActivityRequest:
    out: GetAccountActivityRequest = {}  # type: ignore[typeddict-item]
    if data.get("activityId") is not None:
        out["activity_id"] = data["activityId"]
    else:
        out["activity_id"] = ""
    if data.get("languageCode") is not None:
        import capo_freetier.types.language_code

        out["language_code"] = (
            capo_freetier.types.language_code.deserialize_aws_json_1_0(
                data["languageCode"]
            )
        )
    return out
