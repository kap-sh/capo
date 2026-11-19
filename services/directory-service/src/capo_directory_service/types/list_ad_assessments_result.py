"""Generated from Smithy shape ``com.amazonaws.directoryservice#ListADAssessmentsResult``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_directory_service.types.assessments
    import capo_directory_service.types.next_token


class ListADAssessmentsResult(TypedDict, closed=True):
    assessments: NotRequired["capo_directory_service.types.assessments.Assessments"]
    """<p>A list of assessment summaries containing basic information about each directory assessment.</p>"""
    next_token: NotRequired["capo_directory_service.types.next_token.NextToken"]
    """<p>If not null, more results are available. Pass this value for the <code>NextToken</code> parameter in a subsequent request to retrieve the next set of items.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: ListADAssessmentsResult) -> dict:
    out: dict = {}
    if "assessments" in value:
        import capo_directory_service.types.assessments

        out["Assessments"] = (
            capo_directory_service.types.assessments.serialize_aws_json_1_1(
                value["assessments"]
            )
        )
    if "next_token" in value:
        out["NextToken"] = value["next_token"]
    return out


def deserialize_aws_json_1_1(data: dict) -> ListADAssessmentsResult:
    out: ListADAssessmentsResult = {}  # type: ignore[typeddict-item]
    if data.get("Assessments") is not None:
        import capo_directory_service.types.assessments

        out["assessments"] = (
            capo_directory_service.types.assessments.deserialize_aws_json_1_1(
                data["Assessments"]
            )
        )
    if data.get("NextToken") is not None:
        out["next_token"] = data["NextToken"]
    return out


# --- rpcv2Cbor ser/de ---
def serialize_cbor(value: ListADAssessmentsResult) -> dict:
    out: dict = {}
    if "assessments" in value:
        import capo_directory_service.types.assessments

        out["Assessments"] = capo_directory_service.types.assessments.serialize_cbor(
            value["assessments"]
        )
    if "next_token" in value:
        out["NextToken"] = value["next_token"]
    return out


def deserialize_cbor(data: dict) -> ListADAssessmentsResult:
    out: ListADAssessmentsResult = {}  # type: ignore[typeddict-item]
    if data.get("Assessments") is not None:
        import capo_directory_service.types.assessments

        out["assessments"] = capo_directory_service.types.assessments.deserialize_cbor(
            data["Assessments"]
        )
    if data.get("NextToken") is not None:
        out["next_token"] = data["NextToken"]
    return out
