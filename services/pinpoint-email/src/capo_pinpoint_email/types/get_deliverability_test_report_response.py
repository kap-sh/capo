"""Generated from Smithy shape ``com.amazonaws.pinpointemail#GetDeliverabilityTestReportResponse``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

from capo_pinpoint_email.errors import DeserializationError

if TYPE_CHECKING:
    import capo_pinpoint_email.types.deliverability_test_report
    import capo_pinpoint_email.types.isp_placements
    import capo_pinpoint_email.types.message_content
    import capo_pinpoint_email.types.placement_statistics
    import capo_pinpoint_email.types.tag_list


class GetDeliverabilityTestReportResponse(TypedDict, closed=True):
    deliverability_test_report: (
        "capo_pinpoint_email.types.deliverability_test_report.DeliverabilityTestReport"
    )
    """<p>An object that contains the results of the predictive inbox placement test.</p>"""
    overall_placement: (
        "capo_pinpoint_email.types.placement_statistics.PlacementStatistics"
    )
    """<p>An object that specifies how many test messages that were sent during the predictive inbox placement test were delivered to recipients' inboxes, how many were sent to recipients' spam folders, and how many weren't delivered.</p>"""
    isp_placements: "capo_pinpoint_email.types.isp_placements.IspPlacements"
    """<p>An object that describes how the test email was handled by several email providers, including Gmail, Hotmail, Yahoo, AOL, and others.</p>"""
    message: NotRequired["capo_pinpoint_email.types.message_content.MessageContent"]
    """<p>An object that contains the message that you sent when you performed this predictive inbox placement test.</p>"""
    tags: NotRequired["capo_pinpoint_email.types.tag_list.TagList"]
    """<p>An array of objects that define the tags (keys and values) that are associated with the predictive inbox placement test.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: GetDeliverabilityTestReportResponse) -> dict:
    out: dict = {}
    import capo_pinpoint_email.types.deliverability_test_report

    out["DeliverabilityTestReport"] = (
        capo_pinpoint_email.types.deliverability_test_report.serialize_json(
            value["deliverability_test_report"]
        )
    )
    import capo_pinpoint_email.types.placement_statistics

    out["OverallPlacement"] = (
        capo_pinpoint_email.types.placement_statistics.serialize_json(
            value["overall_placement"]
        )
    )
    import capo_pinpoint_email.types.isp_placements

    out["IspPlacements"] = capo_pinpoint_email.types.isp_placements.serialize_json(
        value["isp_placements"]
    )
    if "message" in value:
        out["Message"] = value["message"]
    if "tags" in value:
        import capo_pinpoint_email.types.tag_list

        out["Tags"] = capo_pinpoint_email.types.tag_list.serialize_json(value["tags"])
    return out


def deserialize_json(data: dict) -> GetDeliverabilityTestReportResponse:
    out: GetDeliverabilityTestReportResponse = {}  # type: ignore[typeddict-item]
    if data.get("DeliverabilityTestReport") is not None:
        import capo_pinpoint_email.types.deliverability_test_report

        out["deliverability_test_report"] = (
            capo_pinpoint_email.types.deliverability_test_report.deserialize_json(
                data["DeliverabilityTestReport"]
            )
        )
    else:
        raise DeserializationError(
            "GetDeliverabilityTestReportResponse.deliverability_test_report required"
        )
    if data.get("OverallPlacement") is not None:
        import capo_pinpoint_email.types.placement_statistics

        out["overall_placement"] = (
            capo_pinpoint_email.types.placement_statistics.deserialize_json(
                data["OverallPlacement"]
            )
        )
    else:
        raise DeserializationError(
            "GetDeliverabilityTestReportResponse.overall_placement required"
        )
    if data.get("IspPlacements") is not None:
        import capo_pinpoint_email.types.isp_placements

        out["isp_placements"] = (
            capo_pinpoint_email.types.isp_placements.deserialize_json(
                data["IspPlacements"]
            )
        )
    else:
        out["isp_placements"] = []
    if data.get("Message") is not None:
        out["message"] = data["Message"]
    if data.get("Tags") is not None:
        import capo_pinpoint_email.types.tag_list

        out["tags"] = capo_pinpoint_email.types.tag_list.deserialize_json(data["Tags"])
    return out
