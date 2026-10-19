"""Generated from Smithy shape ``com.amazonaws.xray#GetSamplingTargetsRequest``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_xray.types.sampling_boost_statistics_document_list
    import capo_xray.types.sampling_statistics_document_list


class GetSamplingTargetsRequest(TypedDict, closed=True):
    sampling_statistics_documents: "capo_xray.types.sampling_statistics_document_list.SamplingStatisticsDocumentList"
    """<p>Information about rules that the service is using to sample requests.</p>"""
    sampling_boost_statistics_documents: NotRequired[
        "capo_xray.types.sampling_boost_statistics_document_list.SamplingBoostStatisticsDocumentList"
    ]
    """<p>Information about rules that the service is using to boost sampling rate.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: GetSamplingTargetsRequest) -> dict:
    out: dict = {}
    import capo_xray.types.sampling_statistics_document_list

    out["SamplingStatisticsDocuments"] = (
        capo_xray.types.sampling_statistics_document_list.serialize_json(
            value["sampling_statistics_documents"]
        )
    )
    if "sampling_boost_statistics_documents" in value:
        import capo_xray.types.sampling_boost_statistics_document_list

        out["SamplingBoostStatisticsDocuments"] = (
            capo_xray.types.sampling_boost_statistics_document_list.serialize_json(
                value["sampling_boost_statistics_documents"]
            )
        )
    return out


def deserialize_json(data: dict) -> GetSamplingTargetsRequest:
    out: GetSamplingTargetsRequest = {}  # type: ignore[typeddict-item]
    if data.get("SamplingStatisticsDocuments") is not None:
        import capo_xray.types.sampling_statistics_document_list

        out["sampling_statistics_documents"] = (
            capo_xray.types.sampling_statistics_document_list.deserialize_json(
                data["SamplingStatisticsDocuments"]
            )
        )
    else:
        out["sampling_statistics_documents"] = []
    if data.get("SamplingBoostStatisticsDocuments") is not None:
        import capo_xray.types.sampling_boost_statistics_document_list

        out["sampling_boost_statistics_documents"] = (
            capo_xray.types.sampling_boost_statistics_document_list.deserialize_json(
                data["SamplingBoostStatisticsDocuments"]
            )
        )
    return out
